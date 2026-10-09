"""The SDK against Blupinta's API: run by Blupinta's own tests, which start its server and give the address, a token,
a project and a home to save; skipped without them."""

import json
import os
import threading
import time

import pytest

from blupinta import Blupinta, BlupintaError, watch_home
from blupinta.v1.api.homes import check_home
from blupinta.v1.api.projects import get_home, get_project, list_projects, list_revisions, save_revision
from blupinta.v1.models import V1HomeCheckRequest, V1SaveRevisionRequest

API = os.environ.get("BLUPINTA_TEST_API")
pytestmark = pytest.mark.skipif(not API, reason="needs Blupinta's test server")


@pytest.fixture
def blupinta():
    with Blupinta(os.environ["BLUPINTA_TEST_TOKEN"], base_url=API) as client:
        yield client


@pytest.fixture
def project_id():
    return os.environ["BLUPINTA_TEST_PROJECT"]


@pytest.fixture
def home():
    with open(os.environ["BLUPINTA_TEST_HOME"]) as file:
        return json.load(file)


def test_reads_the_projects_a_home_and_its_files(blupinta, project_id):
    projects = blupinta.call(list_projects)
    assert [p.name for p in projects.rows] == ["Casa"]
    saved = blupinta.call(get_home, project_id)
    assert saved.number == 1
    assert [f.content_type for f in saved.files] == ["image/png"]
    assert blupinta.file(project_id, saved.files[0].sha256).startswith(b"\x89PNG")
    assert len(blupinta.call(list_revisions, project_id).rows) == 1


def test_checks_a_home(blupinta, home):
    checked = blupinta.call(check_home, body=V1HomeCheckRequest.from_dict({"home": home}))
    assert checked.is_valid is True


def test_a_refusal_is_an_error_with_the_apis_code(blupinta, project_id, home):
    with pytest.raises(BlupintaError) as missing:
        blupinta.call(get_project, "00000000-0000-4000-8000-000000000000")
    assert missing.value.code == "not_found"
    stale = V1SaveRevisionRequest.from_dict({"home": home, "message": "Tardi", "baseRevision": None})
    with pytest.raises(BlupintaError) as conflict:
        blupinta.call(save_revision, project_id, body=stale)
    assert conflict.value.code == "conflict"


def test_follows_the_home_as_versions_are_saved(blupinta, project_id, home):
    versions = watch_home(blupinta, project_id)
    first, etag = next(versions)
    assert first.number == 1 and etag

    saved = {}

    def save():
        time.sleep(0.5)
        body = V1SaveRevisionRequest.from_dict({"home": home, "message": "Da Python", "baseRevision": 1})
        saved["row"] = blupinta.call(save_revision, project_id, body=body)

    saving = threading.Thread(target=save)
    saving.start()
    second, _ = next(versions)
    assert second.number == 2 and second.message == "Da Python"
    versions.close()
    # the event may come before the save's own answer: the client stays open until it has it
    saving.join(10)
    assert saved["row"].number == 2


def test_uploads_a_file(blupinta, project_id):
    uploaded = blupinta.upload(project_id, b"\x89PNG\r\n\x1a\n\x05\x05\x05", "image/png", name="nuovo.png")
    assert uploaded.name == "nuovo.png" and len(uploaded.sha256) == 64
