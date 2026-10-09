from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_host_references import V1HostReferences
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    *,
    body: V1HostReferences,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/host-references".format(
            project_id=project_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1HostReferences]]:
    if response.status_code == 200:
        response_200 = V1HostReferences.from_dict(response.json())

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
) -> Response[Union[V1Error, V1HostReferences]]:
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
    body: V1HostReferences,
) -> Response[Union[V1Error, V1HostReferences]]:
    """Declare the elements it needs

     Replaces what the app declared it needs of the home: elements by kind and id (a wall the app hangs a
    picture on, the room a switch belongs to). Every one must be in the last saved version
    (`invalid_input` names those that aren’t). From then on, saving a version that drops one is refused,
    naming the app, and the editor shows them as errors. An empty list declares nothing.

    Args:
        project_id (UUID):
        body (V1HostReferences): The elements an app declares it needs: saving a version that
            drops one is refused, naming the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1HostReferences]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1HostReferences,
) -> Optional[Union[V1Error, V1HostReferences]]:
    """Declare the elements it needs

     Replaces what the app declared it needs of the home: elements by kind and id (a wall the app hangs a
    picture on, the room a switch belongs to). Every one must be in the last saved version
    (`invalid_input` names those that aren’t). From then on, saving a version that drops one is refused,
    naming the app, and the editor shows them as errors. An empty list declares nothing.

    Args:
        project_id (UUID):
        body (V1HostReferences): The elements an app declares it needs: saving a version that
            drops one is refused, naming the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1HostReferences]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1HostReferences,
) -> Response[Union[V1Error, V1HostReferences]]:
    """Declare the elements it needs

     Replaces what the app declared it needs of the home: elements by kind and id (a wall the app hangs a
    picture on, the room a switch belongs to). Every one must be in the last saved version
    (`invalid_input` names those that aren’t). From then on, saving a version that drops one is refused,
    naming the app, and the editor shows them as errors. An empty list declares nothing.

    Args:
        project_id (UUID):
        body (V1HostReferences): The elements an app declares it needs: saving a version that
            drops one is refused, naming the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1HostReferences]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    body: V1HostReferences,
) -> Optional[Union[V1Error, V1HostReferences]]:
    """Declare the elements it needs

     Replaces what the app declared it needs of the home: elements by kind and id (a wall the app hangs a
    picture on, the room a switch belongs to). Every one must be in the last saved version
    (`invalid_input` names those that aren’t). From then on, saving a version that drops one is refused,
    naming the app, and the editor shows them as errors. An empty list declares nothing.

    Args:
        project_id (UUID):
        body (V1HostReferences): The elements an app declares it needs: saving a version that
            drops one is refused, naming the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1HostReferences]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
