"""A script's first lines with blupinta: connect with a code typed on a phone, list the projects, read a home, then
follow each new version. Compiled by the package's tests, so it can't drift from it."""

from blupinta import Blupinta, TokenKeeper, start_device_sign_in, watch_home
from blupinta.v1.api.projects import get_home, list_projects

signing_in = start_device_sign_in("openid offline_access projects:read")
print(f"Open {signing_in.verification_uri} and type {signing_in.user_code}")
tokens = signing_in.tokens()

with Blupinta(TokenKeeper(tokens, client_id="device")) as blupinta:
    project = blupinta.call(list_projects).rows[0]
    saved = blupinta.call(get_home, project.id)
    print(f"{saved.home['name']}: version {saved.number}")
    for saved, _etag in watch_home(blupinta, project.id, etag=None):
        print(f"new version {saved.number}: {saved.message}")
