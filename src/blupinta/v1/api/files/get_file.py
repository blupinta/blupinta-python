from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    sha256: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/files/{sha256}".format(
            project_id=project_id,
            sha256=sha256,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, V1Error, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.content)
        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 401:
        response_401 = V1Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = V1Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = V1Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = V1Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = V1Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, V1Error, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    sha256: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, V1Error, str]]:
    """A file a version names

     A file of the project that one of its saved versions names by its sha256 (a drawing, a floor’s
    image). The answer is a redirect to the file on Blupinta’s CDN, signed for a few minutes: follow it.
    Files never change, so keep them as long as you like.

    Args:
        project_id (UUID):
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1Error, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sha256=sha256,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    sha256: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, V1Error, str]]:
    """A file a version names

     A file of the project that one of its saved versions names by its sha256 (a drawing, a floor’s
    image). The answer is a redirect to the file on Blupinta’s CDN, signed for a few minutes: follow it.
    Files never change, so keep them as long as you like.

    Args:
        project_id (UUID):
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, V1Error, str]
    """

    return sync_detailed(
        project_id=project_id,
        sha256=sha256,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    sha256: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, V1Error, str]]:
    """A file a version names

     A file of the project that one of its saved versions names by its sha256 (a drawing, a floor’s
    image). The answer is a redirect to the file on Blupinta’s CDN, signed for a few minutes: follow it.
    Files never change, so keep them as long as you like.

    Args:
        project_id (UUID):
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1Error, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sha256=sha256,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    sha256: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, V1Error, str]]:
    """A file a version names

     A file of the project that one of its saved versions names by its sha256 (a drawing, a floor’s
    image). The answer is a redirect to the file on Blupinta’s CDN, signed for a few minutes: follow it.
    Files never change, so keep them as long as you like.

    Args:
        project_id (UUID):
        sha256 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, V1Error, str]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            sha256=sha256,
            client=client,
        )
    ).parsed
