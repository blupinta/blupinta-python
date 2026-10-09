from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_home_check import V1HomeCheck
from ...models.v1_home_check_request import V1HomeCheckRequest
from ...types import Response


def _get_kwargs(
    *,
    body: V1HomeCheckRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/homes/check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1HomeCheck]]:
    if response.status_code == 200:
        response_200 = V1HomeCheck.from_dict(response.json())

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
) -> Response[Union[V1Error, V1HomeCheck]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: V1HomeCheckRequest,
) -> Response[Union[V1Error, V1HomeCheck]]:
    """Check a home file

     What Blupinta’s own checks say of a home file, of any version of the format: brought to the current
    one as an import would, read, and checked as saving a version is. Nothing is kept. A file that isn’t
    a home answers `format` problems, each with its path.

    Args:
        body (V1HomeCheckRequest): A home file to check: any version of the format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1HomeCheck]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: V1HomeCheckRequest,
) -> Optional[Union[V1Error, V1HomeCheck]]:
    """Check a home file

     What Blupinta’s own checks say of a home file, of any version of the format: brought to the current
    one as an import would, read, and checked as saving a version is. Nothing is kept. A file that isn’t
    a home answers `format` problems, each with its path.

    Args:
        body (V1HomeCheckRequest): A home file to check: any version of the format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1HomeCheck]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: V1HomeCheckRequest,
) -> Response[Union[V1Error, V1HomeCheck]]:
    """Check a home file

     What Blupinta’s own checks say of a home file, of any version of the format: brought to the current
    one as an import would, read, and checked as saving a version is. Nothing is kept. A file that isn’t
    a home answers `format` problems, each with its path.

    Args:
        body (V1HomeCheckRequest): A home file to check: any version of the format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1HomeCheck]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: V1HomeCheckRequest,
) -> Optional[Union[V1Error, V1HomeCheck]]:
    """Check a home file

     What Blupinta’s own checks say of a home file, of any version of the format: brought to the current
    one as an import would, read, and checked as saving a version is. Nothing is kept. A file that isn’t
    a home answers `format` problems, each with its path.

    Args:
        body (V1HomeCheckRequest): A home file to check: any version of the format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1HomeCheck]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
