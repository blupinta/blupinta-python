from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_product import V1Product
from ...types import Response


def _get_kwargs(
    namespace: str,
    name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/products/{namespace}/{name}".format(
            namespace=namespace,
            name=name,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1Product]]:
    if response.status_code == 200:
        response_200 = V1Product.from_dict(response.json())

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
) -> Response[Union[V1Error, V1Product]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[V1Error, V1Product]]:
    """One product, whole

     A product of the catalog as a home holds it among its `products`: its options, sizes as expressions
    of them, geometry, clearances, what a house entity may drive in it, its thumbnails.

    Args:
        namespace (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Product]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[V1Error, V1Product]]:
    """One product, whole

     A product of the catalog as a home holds it among its `products`: its options, sizes as expressions
    of them, geometry, clearances, what a house entity may drive in it, its thumbnails.

    Args:
        namespace (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Product]
    """

    return sync_detailed(
        namespace=namespace,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[V1Error, V1Product]]:
    """One product, whole

     A product of the catalog as a home holds it among its `products`: its options, sizes as expressions
    of them, geometry, clearances, what a house entity may drive in it, its thumbnails.

    Args:
        namespace (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1Product]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[V1Error, V1Product]]:
    """One product, whole

     A product of the catalog as a home holds it among its `products`: its options, sizes as expressions
    of them, geometry, clearances, what a house entity may drive in it, its thumbnails.

    Args:
        namespace (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1Product]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            name=name,
            client=client,
        )
    ).parsed
