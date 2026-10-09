from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_webhook_event import V1WebhookEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1WebhookInput")


@_attrs_define
class V1WebhookInput:
    """A webhook to make: where to post, and which events (all of them when none is said)

    Attributes:
        url (str): an HTTPS address on the public internet
        events (Union[Unset, list[V1WebhookEvent]]):
    """

    url: str
    events: Union[Unset, list[V1WebhookEvent]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = V1WebhookEvent(events_item_data)

            events.append(events_item)

        v1_webhook_input = cls(
            url=url,
            events=events,
        )

        v1_webhook_input.additional_properties = d
        return v1_webhook_input

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
