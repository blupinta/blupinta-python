from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_webhook_event import V1WebhookEvent

T = TypeVar("T", bound="V1Delivery")


@_attrs_define
class V1Delivery:
    """One event posted, or on its way, to a webhook

    Attributes:
        id (str):
        event (V1WebhookEvent): What a webhook may be told
        created_at (str):
        attempts (int):
        delivered_at (Union[None, str]): when the app answered 2xx; null until then
        last_status (Union[None, int]): the last try's HTTP status; null when no answer came
        last_error (Union[None, str]):
        next_attempt_at (Union[None, str]): when it is tried again; null once delivered or given up
    """

    id: str
    event: V1WebhookEvent
    created_at: str
    attempts: int
    delivered_at: Union[None, str]
    last_status: Union[None, int]
    last_error: Union[None, str]
    next_attempt_at: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event = self.event.value

        created_at = self.created_at

        attempts = self.attempts

        delivered_at: Union[None, str]
        delivered_at = self.delivered_at

        last_status: Union[None, int]
        last_status = self.last_status

        last_error: Union[None, str]
        last_error = self.last_error

        next_attempt_at: Union[None, str]
        next_attempt_at = self.next_attempt_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event": event,
                "createdAt": created_at,
                "attempts": attempts,
                "deliveredAt": delivered_at,
                "lastStatus": last_status,
                "lastError": last_error,
                "nextAttemptAt": next_attempt_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        event = V1WebhookEvent(d.pop("event"))

        created_at = d.pop("createdAt")

        attempts = d.pop("attempts")

        def _parse_delivered_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        delivered_at = _parse_delivered_at(d.pop("deliveredAt"))

        def _parse_last_status(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        last_status = _parse_last_status(d.pop("lastStatus"))

        def _parse_last_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_error = _parse_last_error(d.pop("lastError"))

        def _parse_next_attempt_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_attempt_at = _parse_next_attempt_at(d.pop("nextAttemptAt"))

        v1_delivery = cls(
            id=id,
            event=event,
            created_at=created_at,
            attempts=attempts,
            delivered_at=delivered_at,
            last_status=last_status,
            last_error=last_error,
            next_attempt_at=next_attempt_at,
        )

        v1_delivery.additional_properties = d
        return v1_delivery

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
