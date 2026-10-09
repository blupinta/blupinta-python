from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Condition")


@_attrs_define
class Condition:
    """Shows (or allows) an option only when another holds one of some values

    Attributes:
        option (str):
        in_ (list[Union[bool, float, str]]):
    """

    option: str
    in_: list[Union[bool, float, str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option

        in_ = []
        for in_item_data in self.in_:
            in_item: Union[bool, float, str]
            in_item = in_item_data
            in_.append(in_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "in": in_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = d.pop("option")

        in_ = []
        _in_ = d.pop("in")
        for in_item_data in _in_:

            def _parse_in_item(data: object) -> Union[bool, float, str]:
                return cast(Union[bool, float, str], data)

            in_item = _parse_in_item(in_item_data)

            in_.append(in_item)

        condition = cls(
            option=option,
            in_=in_,
        )

        condition.additional_properties = d
        return condition

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
