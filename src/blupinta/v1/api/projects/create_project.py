from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_project import V1Project
from ...models.v1_project_input import V1ProjectInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V1ProjectInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1Project]]:
    if response.status_code == 201:
        response_201 = V1Project.from_dict(response.json())

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
) -> Response[Union[V1Error, V1Project]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: V1ProjectInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1Project]]:
    """Create a project

     A new project in the person’s account, its home empty and in their language; the app may then read
    and write it as one of its own projects.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1ProjectInput): A project's name and where it is

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Project]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: V1ProjectInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1Project]]:
    """Create a project

     A new project in the person’s account, its home empty and in their language; the app may then read
    and write it as one of its own projects.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1ProjectInput): A project's name and where it is

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Project]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: V1ProjectInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1Project]]:
    """Create a project

     A new project in the person’s account, its home empty and in their language; the app may then read
    and write it as one of its own projects.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1ProjectInput): A project's name and where it is

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Project]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: V1ProjectInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1Project]]:
    """Create a project

     A new project in the person’s account, its home empty and in their language; the app may then read
    and write it as one of its own projects.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1ProjectInput): A project's name and where it is

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Project]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
