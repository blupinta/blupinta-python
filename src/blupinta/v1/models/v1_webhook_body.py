from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_webhook_event import V1WebhookEvent

if TYPE_CHECKING:
    from ..models.v1_webhook_body_data import V1WebhookBodyData


T = TypeVar("T", bound="V1WebhookBody")


@_attrs_define
class V1WebhookBody:
    """The body posted to a webhook. Its headers: `Blupinta-Event`, `Blupinta-Delivery` (the same id on every retry) and
    `Blupinta-Signature: t=<seconds>,v1=<hex>`, the HMAC-SHA256 of `<t>.<body>` with the webhook's secret

        Attributes:
            id (str): the delivery's id
            type_ (V1WebhookEvent): What a webhook may be told
            created_at (str): when it happened, ISO 8601
            data (V1WebhookBodyData):
    """

    id: str
    type_: V1WebhookEvent
    created_at: str
    data: "V1WebhookBodyData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        created_at = self.created_at

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "createdAt": created_at,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_webhook_body_data import V1WebhookBodyData

        d = dict(src_dict)
        id = d.pop("id")

        type_ = V1WebhookEvent(d.pop("type"))

        created_at = d.pop("createdAt")

        data = V1WebhookBodyData.from_dict(d.pop("data"))

        v1_webhook_body = cls(
            id=id,
            type_=type_,
            created_at=created_at,
            data=data,
        )

        v1_webhook_body.additional_properties = d
        return v1_webhook_body

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
