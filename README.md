# blupinta

The official Python SDK for [Blupinta](https://blupinta.app)'s public API, `https://api.blupinta.app/v1`: every
operation typed (`blupinta.v1`, generated from the API's OpenAPI document), the person signed in with the device flow,
a home followed as its versions are saved, webhooks checked. Python 3.10 or later.

```sh
pip install blupinta
```

```python
from blupinta import Blupinta, TokenKeeper, start_device_sign_in, watch_home
from blupinta.v1.api.projects import get_home, list_projects

signing_in = start_device_sign_in("openid offline_access projects:read")
print(f"Go to {signing_in.verification_uri} and type {signing_in.user_code}")
tokens = signing_in.tokens()

blupinta = Blupinta(TokenKeeper(tokens, client_id="device", on_tokens=save))
projects = blupinta.call(list_projects)
saved = blupinta.call(get_home, projects.rows[0].id)
print(saved.number, saved.home["name"])

for saved, etag in watch_home(blupinta, projects.rows[0].id):
    print("new version", saved.number)
```

- `blupinta.call(operation, ...)` calls any module of `blupinta.v1.api` and returns its model; `await
  blupinta.acall(...)` does the same with asyncio. A refusal raises `BlupintaError`, with the API's `code`
  (`not_found`, `conflict`...), its `problems` and, for a 429, `retry_after`.
- `blupinta.file(project_id, sha256)`, `thumbnail`, `export`, `upload`: what isn't JSON.
- `watch_home(blupinta, project_id, etag=...)`: each saved version, from the one after the copy you kept.
- `is_signed_webhook(body, signature, secret)`: whether a webhook's post came from Blupinta.

A home is a `dict` in Blupinta's home format (its schema: `https://blupinta.app/schema/home-<version>.json`). To check
one, `blupinta.call(check_home, body=...)` asks Blupinta's own checks.

The guide: <https://docs.blupinta.app/reference/public-api/>. Apache License 2.0.
