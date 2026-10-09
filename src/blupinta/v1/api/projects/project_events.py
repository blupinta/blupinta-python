from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...types import Response


def _get_kwargs(
    project_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/events".format(
            project_id=project_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, str]]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

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
) -> Response[Union[V1Error, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[V1Error, str]]:
    """What happens to the project, as it happens

     A stream of server-sent events (`text/event-stream`) that stays open. `revision.saved` (data:
    `V1RevisionSaved`) when a version is saved: read it then. `access.revoked` when the app is
    disconnected or loses the project, `token.expired` when the access token runs out: the stream ends
    after either, and the app reconnects with a fresh token (or not at all, once revoked). A comment
    line every 25 seconds keeps it open through proxies.

    Args:
        project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[V1Error, str]]:
    """What happens to the project, as it happens

     A stream of server-sent events (`text/event-stream`) that stays open. `revision.saved` (data:
    `V1RevisionSaved`) when a version is saved: read it then. `access.revoked` when the app is
    disconnected or loses the project, `token.expired` when the access token runs out: the stream ends
    after either, and the app reconnects with a fresh token (or not at all, once revoked). A comment
    line every 25 seconds keeps it open through proxies.

    Args:
        project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, str]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[V1Error, str]]:
    """What happens to the project, as it happens

     A stream of server-sent events (`text/event-stream`) that stays open. `revision.saved` (data:
    `V1RevisionSaved`) when a version is saved: read it then. `access.revoked` when the app is
    disconnected or loses the project, `token.expired` when the access token runs out: the stream ends
    after either, and the app reconnects with a fresh token (or not at all, once revoked). A comment
    line every 25 seconds keeps it open through proxies.

    Args:
        project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[V1Error, str]]:
    """What happens to the project, as it happens

     A stream of server-sent events (`text/event-stream`) that stays open. `revision.saved` (data:
    `V1RevisionSaved`) when a version is saved: read it then. `access.revoked` when the app is
    disconnected or loses the project, `token.expired` when the access token runs out: the stream ends
    after either, and the app reconnects with a fresh token (or not at all, once revoked). A comment
    line every 25 seconds keeps it open through proxies.

    Args:
        project_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, str]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
