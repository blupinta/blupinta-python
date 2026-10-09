from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...types import Response


def _get_kwargs(
    webhook_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/webhooks/{webhook_id}".format(
            webhook_id=webhook_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, V1Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Union[Any, V1Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, V1Error]]:
    """Delete a webhook

     Nothing more is posted to it, deliveries on their way included.

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1Error]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, V1Error]]:
    """Delete a webhook

     Nothing more is posted to it, deliveries on their way included.

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, V1Error]
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, V1Error]]:
    """Delete a webhook

     Nothing more is posted to it, deliveries on their way included.

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1Error]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, V1Error]]:
    """Delete a webhook

     Nothing more is posted to it, deliveries on their way included.

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, V1Error]
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
