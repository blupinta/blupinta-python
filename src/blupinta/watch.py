"""Following a project's home as it is saved: the saved version asked with its ETag (nothing comes back when it
hasn't changed), then the project's events, which say when a new version is saved; the stream opened again when it
drops, a fresh token each time. A generator: ``for saved in watch_home(blupinta, project_id): ...``, stopped by
leaving the loop."""

from __future__ import annotations

import time
from collections.abc import Iterator
from uuid import UUID

import httpx

from .client import Blupinta
from .errors import BlupintaError, error_of
from .v1.models.v1_revision import V1Revision

#: the longest wait before opening a dropped stream again, in seconds
MOST_WAIT = 60.0

#: the refusals after which watching is pointless: the app lost the project, or its access
_GONE = {"forbidden", "not_found", "unauthenticated"}


def _events(response: httpx.Response) -> Iterator[str]:
    """The names of a stream's events as they come"""
    event = None
    for line in response.iter_lines():
        if line.startswith("event: "):
            event = line[7:]
        elif line == "" and event:
            yield event
            event = None


def watch_home(
    blupinta: Blupinta, project_id: UUID | str, *, etag: str | None = None
) -> Iterator[tuple[V1Revision, str | None]]:
    """Each saved version of the project's home with its ETag, the current one first unless it is the one of
    ``etag`` (the copy the app kept), until the loop is left or the app loses the project (a ``BlupintaError``)."""
    kept = {"etag": etag}

    def changed() -> tuple[V1Revision, str | None] | None:
        headers = {"if-none-match": kept["etag"]} if kept["etag"] else {}
        response = blupinta.http.get(f"/v1/projects/{project_id}/home", headers=headers)
        if response.status_code == 304:
            return None
        if response.status_code >= 400:
            raise error_of(response.status_code, response.content, response.headers)
        kept["etag"] = response.headers.get("etag")
        return V1Revision.from_dict(response.json()), kept["etag"]

    wait = 1.0
    while True:
        try:
            saved = changed()
            if saved:
                yield saved
            with blupinta.http.stream("GET", f"/v1/projects/{project_id}/events", timeout=None) as response:
                if response.status_code >= 400:
                    response.read()
                    raise error_of(response.status_code, response.content, response.headers)
                wait = 1.0
                for event in _events(response):
                    if event == "revision.saved":
                        saved = changed()
                        if saved:
                            yield saved
                    elif event == "access.revoked":
                        raise BlupintaError(403, "forbidden", ["access.revoked"])
                    # `token.expired`: the stream ends, and opens again with a fresh token
        except BlupintaError as e:
            if e.code in _GONE:
                raise
        except httpx.HTTPError:
            pass
        time.sleep(wait)
        wait = min(wait * 2, MOST_WAIT)
