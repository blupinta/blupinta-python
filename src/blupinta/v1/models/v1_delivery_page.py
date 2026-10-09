from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v1_delivery import V1Delivery


T = TypeVar("T", bound="V1DeliveryPage")


@_attrs_define
class V1DeliveryPage:
    """A webhook's latest deliveries, newest first

    Attributes:
        rows (list['V1Delivery']):
        next_ (Union[None, str]):
    """

    rows: list["V1Delivery"]
    next_: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        next_: Union[None, str]
        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_delivery import V1Delivery

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = V1Delivery.from_dict(rows_item_data)

            rows.append(rows_item)

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        v1_delivery_page = cls(
            rows=rows,
            next_=next_,
        )

        v1_delivery_page.additional_properties = d
        return v1_delivery_page

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
