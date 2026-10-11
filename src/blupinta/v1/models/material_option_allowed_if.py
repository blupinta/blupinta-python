from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition import Condition


T = TypeVar("T", bound="MaterialOptionAllowedIf")


@_attrs_define
class MaterialOptionAllowedIf:
    """the materials sold only with some other values, by material"""

    additional_properties: dict[str, list["Condition"]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemas_allowed_if_item_data in prop:
                componentsschemas_allowed_if_item = (
                    componentsschemas_allowed_if_item_data.to_dict()
                )
                field_dict[prop_name].append(componentsschemas_allowed_if_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition import Condition

        d = dict(src_dict)
        material_option_allowed_if = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemas_allowed_if_item_data in _additional_property:
                componentsschemas_allowed_if_item = Condition.from_dict(
                    componentsschemas_allowed_if_item_data
                )

                additional_property.append(componentsschemas_allowed_if_item)

            additional_properties[prop_name] = additional_property

        material_option_allowed_if.additional_properties = additional_properties
        return material_option_allowed_if

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list["Condition"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list["Condition"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
