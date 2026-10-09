from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_thread import V1Thread
from ...models.v1_thread_input import V1ThreadInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    body: V1ThreadInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/threads".format(
            project_id=project_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1Thread]]:
    if response.status_code == 201:
        response_201 = V1Thread.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = V1Error.from_dict(response.json())

        return response_400

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
) -> Response[Union[V1Error, V1Thread]]:
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
    body: V1ThreadInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1Thread]]:
    """Open a thread

     A thread pinned on a plan, on one of its elements or at a point, with its first message, written as
    the person (anyone who can look at the project may comment); it says the app wrote it.

    Args:
        project_id (UUID):
        idempotency_key (Union[Unset, str]):
        body (V1ThreadInput): A thread to open: where, and its first message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Thread]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1ThreadInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1Thread]]:
    """Open a thread

     A thread pinned on a plan, on one of its elements or at a point, with its first message, written as
    the person (anyone who can look at the project may comment); it says the app wrote it.

    Args:
        project_id (UUID):
        idempotency_key (Union[Unset, str]):
        body (V1ThreadInput): A thread to open: where, and its first message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Thread]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1ThreadInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1Thread]]:
    """Open a thread

     A thread pinned on a plan, on one of its elements or at a point, with its first message, written as
    the person (anyone who can look at the project may comment); it says the app wrote it.

    Args:
        project_id (UUID):
        idempotency_key (Union[Unset, str]):
        body (V1ThreadInput): A thread to open: where, and its first message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Thread]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1ThreadInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1Thread]]:
    """Open a thread

     A thread pinned on a plan, on one of its elements or at a point, with its first message, written as
    the person (anyone who can look at the project may comment); it says the app wrote it.

    Args:
        project_id (UUID):
        idempotency_key (Union[Unset, str]):
        body (V1ThreadInput): A thread to open: where, and its first message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Thread]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
