from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_products_language import SearchProductsLanguage
from ...models.search_products_mount import SearchProductsMount
from ...models.search_products_sort import SearchProductsSort
from ...models.v1_error import V1Error
from ...models.v1_product_page import V1ProductPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    brand: Union[Unset, list[str]] = UNSET,
    mount: Union[Unset, SearchProductsMount] = UNSET,
    family: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchProductsSort] = UNSET,
    language: Union[Unset, SearchProductsLanguage] = UNSET,
    limit: Union[Unset, int] = UNSET,
    after: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["category"] = category

    json_brand: Union[Unset, list[str]] = UNSET
    if not isinstance(brand, Unset):
        json_brand = brand

    params["brand"] = json_brand

    json_mount: Union[Unset, str] = UNSET
    if not isinstance(mount, Unset):
        json_mount = mount.value

    params["mount"] = json_mount

    params["family"] = family

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_language: Union[Unset, str] = UNSET
    if not isinstance(language, Unset):
        json_language = language.value

    params["language"] = json_language

    params["limit"] = limit

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/products",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1ProductPage]]:
    if response.status_code == 200:
        response_200 = V1ProductPage.from_dict(response.json())

        return response_200

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
) -> Response[Union[V1Error, V1ProductPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    brand: Union[Unset, list[str]] = UNSET,
    mount: Union[Unset, SearchProductsMount] = UNSET,
    family: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchProductsSort] = UNSET,
    language: Union[Unset, SearchProductsLanguage] = UNSET,
    limit: Union[Unset, int] = UNSET,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1ProductPage]]:
    """Search the catalog

     Blupinta’s catalog of products searched as the editor searches it: words, narrowed by category,
    brand, mount and colour family, in pages.

    Args:
        q (Union[Unset, str]):
        category (Union[Unset, str]):
        brand (Union[Unset, list[str]]):
        mount (Union[Unset, SearchProductsMount]):
        family (Union[Unset, str]):
        sort (Union[Unset, SearchProductsSort]):
        language (Union[Unset, SearchProductsLanguage]):
        limit (Union[Unset, int]):
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1ProductPage]]
    """

    kwargs = _get_kwargs(
        q=q,
        category=category,
        brand=brand,
        mount=mount,
        family=family,
        sort=sort,
        language=language,
        limit=limit,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    brand: Union[Unset, list[str]] = UNSET,
    mount: Union[Unset, SearchProductsMount] = UNSET,
    family: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchProductsSort] = UNSET,
    language: Union[Unset, SearchProductsLanguage] = UNSET,
    limit: Union[Unset, int] = UNSET,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1ProductPage]]:
    """Search the catalog

     Blupinta’s catalog of products searched as the editor searches it: words, narrowed by category,
    brand, mount and colour family, in pages.

    Args:
        q (Union[Unset, str]):
        category (Union[Unset, str]):
        brand (Union[Unset, list[str]]):
        mount (Union[Unset, SearchProductsMount]):
        family (Union[Unset, str]):
        sort (Union[Unset, SearchProductsSort]):
        language (Union[Unset, SearchProductsLanguage]):
        limit (Union[Unset, int]):
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1ProductPage]
    """

    return sync_detailed(
        client=client,
        q=q,
        category=category,
        brand=brand,
        mount=mount,
        family=family,
        sort=sort,
        language=language,
        limit=limit,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    brand: Union[Unset, list[str]] = UNSET,
    mount: Union[Unset, SearchProductsMount] = UNSET,
    family: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchProductsSort] = UNSET,
    language: Union[Unset, SearchProductsLanguage] = UNSET,
    limit: Union[Unset, int] = UNSET,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1ProductPage]]:
    """Search the catalog

     Blupinta’s catalog of products searched as the editor searches it: words, narrowed by category,
    brand, mount and colour family, in pages.

    Args:
        q (Union[Unset, str]):
        category (Union[Unset, str]):
        brand (Union[Unset, list[str]]):
        mount (Union[Unset, SearchProductsMount]):
        family (Union[Unset, str]):
        sort (Union[Unset, SearchProductsSort]):
        language (Union[Unset, SearchProductsLanguage]):
        limit (Union[Unset, int]):
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1ProductPage]]
    """

    kwargs = _get_kwargs(
        q=q,
        category=category,
        brand=brand,
        mount=mount,
        family=family,
        sort=sort,
        language=language,
        limit=limit,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    brand: Union[Unset, list[str]] = UNSET,
    mount: Union[Unset, SearchProductsMount] = UNSET,
    family: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchProductsSort] = UNSET,
    language: Union[Unset, SearchProductsLanguage] = UNSET,
    limit: Union[Unset, int] = UNSET,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1ProductPage]]:
    """Search the catalog

     Blupinta’s catalog of products searched as the editor searches it: words, narrowed by category,
    brand, mount and colour family, in pages.

    Args:
        q (Union[Unset, str]):
        category (Union[Unset, str]):
        brand (Union[Unset, list[str]]):
        mount (Union[Unset, SearchProductsMount]):
        family (Union[Unset, str]):
        sort (Union[Unset, SearchProductsSort]):
        language (Union[Unset, SearchProductsLanguage]):
        limit (Union[Unset, int]):
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1ProductPage]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            category=category,
            brand=brand,
            mount=mount,
            family=family,
            sort=sort,
            language=language,
            limit=limit,
            after=after,
        )
    ).parsed
