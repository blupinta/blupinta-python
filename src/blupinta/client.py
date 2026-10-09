"""A client of Blupinta's public API, ``/v1``: every operation of the generated client (``blupinta.v1.api``) called
through ``call`` (or ``acall``), its answer parsed into the generated models and a refusal raised as a
``BlupintaError``, the token on every request (a fresh one when it is a ``TokenKeeper``), plus what the generated
client leaves out: files' bytes, uploads, the project's export."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, Protocol, TypeVar
from uuid import UUID

import httpx

from .errors import BlupintaError, error_of
from .v1.client import AuthenticatedClient
from .v1.models.v1_file import V1File
from .v1.types import Response

API_ORIGIN = "https://api.blupinta.app"

T = TypeVar("T", covariant=True)


class _Operation(Protocol[T]):
    """A module of ``blupinta.v1.api``: one operation"""

    def sync_detailed(self, *args: Any, client: AuthenticatedClient, **kwargs: Any) -> Response[T]: ...

    def asyncio_detailed(self, *args: Any, client: AuthenticatedClient, **kwargs: Any) -> Awaitable[Response[T]]: ...


class _Bearer(httpx.Auth):
    """The access token on each request, asked of ``token`` each time (so a keeper may refresh it)"""

    def __init__(self, token: str | Callable[[], str]) -> None:
        self._token = token

    def auth_flow(self, request: httpx.Request):  # type: ignore[override]
        token = self._token if isinstance(self._token, str) else self._token()
        request.headers["authorization"] = f"Bearer {token}"
        yield request


def _answer(response: Response[Any]) -> Any:
    """The parsed answer of a call, or its refusal raised; ``None`` for a 304 (unchanged) or a 204"""
    if response.status_code >= 400:
        raise error_of(response.status_code, response.content, httpx.Headers(dict(response.headers)))
    return response.parsed


class Blupinta:
    """The API as the person signed in: ``token`` is an access token, or a ``TokenKeeper`` that refreshes it."""

    def __init__(
        self,
        token: str | Callable[[], str],
        base_url: str = API_ORIGIN,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.base_url = base_url
        self.client = AuthenticatedClient(base_url=base_url, token="")
        # requests go through this client: the token asked each time, a file's redirect to the CDN followed (httpx
        # drops the token when it leaves the API's origin)
        self.http = httpx.Client(
            base_url=base_url, auth=_Bearer(token), timeout=timeout, follow_redirects=True, transport=transport
        )
        self.client.set_httpx_client(self.http)
        self.client.set_async_httpx_client(
            httpx.AsyncClient(base_url=base_url, auth=_Bearer(token), timeout=timeout, follow_redirects=True)
        )

    def call(self, operation: _Operation[T], *args: Any, **kwargs: Any) -> Any:
        """Calls ``operation`` (a module of ``blupinta.v1.api``) with its arguments: its answer, or a
        ``BlupintaError``. ``blupinta.call(list_projects)``, ``blupinta.call(get_home, project_id)``"""
        try:
            return _answer(operation.sync_detailed(*args, client=self.client, **kwargs))
        except httpx.HTTPError as e:
            raise BlupintaError(0, "network", [str(e)]) from e

    async def acall(self, operation: _Operation[T], *args: Any, **kwargs: Any) -> Any:
        """``call``, awaited: for asyncio"""
        try:
            return _answer(await operation.asyncio_detailed(*args, client=self.client, **kwargs))
        except httpx.HTTPError as e:
            raise BlupintaError(0, "network", [str(e)]) from e

    def _bytes(self, path: str) -> bytes:
        try:
            response = self.http.get(path)
        except httpx.HTTPError as e:
            raise BlupintaError(0, "network", [str(e)]) from e
        if response.status_code >= 400:
            raise error_of(response.status_code, response.content, response.headers)
        return response.content

    def file(self, project_id: UUID | str, sha256: str) -> bytes:
        """The bytes of a file a saved version names (``V1Revision.files``)"""
        return self._bytes(f"/v1/projects/{project_id}/files/{sha256}")

    def thumbnail(self, project_id: UUID | str) -> bytes:
        """The last saved version's thumbnail, a WebP image"""
        return self._bytes(f"/v1/projects/{project_id}/thumbnail")

    def export(self, project_id: UUID | str) -> bytes:
        """Every saved version and the files they name, as a zip"""
        return self._bytes(f"/v1/projects/{project_id}/export")

    def upload(self, project_id: UUID | str, data: bytes, content_type: str, name: str = "file") -> V1File:
        """A file for the project's home (PNG, JPEG, WebP or PDF): its ``sha256`` is how a home names it"""
        try:
            response = self.http.post(
                f"/v1/projects/{project_id}/files",
                params={"name": name},
                content=data,
                headers={"content-type": content_type},
            )
        except httpx.HTTPError as e:
            raise BlupintaError(0, "network", [str(e)]) from e
        if response.status_code >= 400:
            raise error_of(response.status_code, response.content, response.headers)
        return V1File.from_dict(response.json())

    def close(self) -> None:
        self.http.close()

    def __enter__(self) -> Blupinta:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
