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

T = TypeVar("T", bound="V1Webhook")


@_attrs_define
class V1Webhook:
    """Where an app is told what happens to the projects it reaches

    Attributes:
        id (str):
        url (str):
        events (list[V1WebhookEvent]):
        created_at (str):
        disabled_at (Union[None, str]): when it was turned off after three days of failing deliveries; null while on
        disabled_reason (Union[None, str]):
    """

    id: str
    url: str
    events: list[V1WebhookEvent]
    created_at: str
    disabled_at: Union[None, str]
    disabled_reason: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        created_at = self.created_at

        disabled_at: Union[None, str]
        disabled_at = self.disabled_at

        disabled_reason: Union[None, str]
        disabled_reason = self.disabled_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "events": events,
                "createdAt": created_at,
                "disabledAt": disabled_at,
                "disabledReason": disabled_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = V1WebhookEvent(events_item_data)

            events.append(events_item)

        created_at = d.pop("createdAt")

        def _parse_disabled_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        disabled_at = _parse_disabled_at(d.pop("disabledAt"))

        def _parse_disabled_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        disabled_reason = _parse_disabled_reason(d.pop("disabledReason"))

        v1_webhook = cls(
            id=id,
            url=url,
            events=events,
            created_at=created_at,
            disabled_at=disabled_at,
            disabled_reason=disabled_reason,
        )

        v1_webhook.additional_properties = d
        return v1_webhook

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
