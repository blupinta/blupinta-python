from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1_error import V1Error
from ...models.v1_webhook_created import V1WebhookCreated
from ...models.v1_webhook_input import V1WebhookInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V1WebhookInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[V1Error, V1WebhookCreated]]:
    if response.status_code == 201:
        response_201 = V1WebhookCreated.from_dict(response.json())

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
) -> Response[Union[V1Error, V1WebhookCreated]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: V1WebhookInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1WebhookCreated]]:
    """Make a webhook

     An HTTPS address of the app’s, on the public internet, that Blupinta posts each event of the
    projects the app reaches to (`V1WebhookBody`), signed: `Blupinta-Signature: t=<seconds>,v1=<hex>` is
    the HMAC-SHA256 of `<t>.<body>` with the webhook’s `secret`, given only now. Answer 2xx within 10
    seconds; anything else is tried again after 1 min, 5 min, 30 min, 2 h and 12 h. Three days of
    nothing but failures turn it off.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1WebhookInput): A webhook to make: where to post, and which events (all of them
            when none is said)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1WebhookCreated]]
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
    body: V1WebhookInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1WebhookCreated]]:
    """Make a webhook

     An HTTPS address of the app’s, on the public internet, that Blupinta posts each event of the
    projects the app reaches to (`V1WebhookBody`), signed: `Blupinta-Signature: t=<seconds>,v1=<hex>` is
    the HMAC-SHA256 of `<t>.<body>` with the webhook’s `secret`, given only now. Answer 2xx within 10
    seconds; anything else is tried again after 1 min, 5 min, 30 min, 2 h and 12 h. Three days of
    nothing but failures turn it off.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1WebhookInput): A webhook to make: where to post, and which events (all of them
            when none is said)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1WebhookCreated]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: V1WebhookInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[V1Error, V1WebhookCreated]]:
    """Make a webhook

     An HTTPS address of the app’s, on the public internet, that Blupinta posts each event of the
    projects the app reaches to (`V1WebhookBody`), signed: `Blupinta-Signature: t=<seconds>,v1=<hex>` is
    the HMAC-SHA256 of `<t>.<body>` with the webhook’s `secret`, given only now. Answer 2xx within 10
    seconds; anything else is tried again after 1 min, 5 min, 30 min, 2 h and 12 h. Three days of
    nothing but failures turn it off.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1WebhookInput): A webhook to make: where to post, and which events (all of them
            when none is said)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[V1Error, V1WebhookCreated]]
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
    body: V1WebhookInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[V1Error, V1WebhookCreated]]:
    """Make a webhook

     An HTTPS address of the app’s, on the public internet, that Blupinta posts each event of the
    projects the app reaches to (`V1WebhookBody`), signed: `Blupinta-Signature: t=<seconds>,v1=<hex>` is
    the HMAC-SHA256 of `<t>.<body>` with the webhook’s `secret`, given only now. Answer 2xx within 10
    seconds; anything else is tried again after 1 min, 5 min, 30 min, 2 h and 12 h. Three days of
    nothing but failures turn it off.

    Args:
        idempotency_key (Union[Unset, str]):
        body (V1WebhookInput): A webhook to make: where to post, and which events (all of them
            when none is said)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[V1Error, V1WebhookCreated]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
