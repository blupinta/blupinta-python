from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.translated import Translated


T = TypeVar("T", bound="SlotsOptionChoicesItem")


@_attrs_define
class SlotsOptionChoicesItem:
    """
    Attributes:
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
    """

    id: str
    name: "Translated"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translated import Translated

        d = dict(src_dict)
        id = d.pop("id")

        name = Translated.from_dict(d.pop("name"))

        slots_option_choices_item = cls(
            id=id,
            name=name,
        )

        slots_option_choices_item.additional_properties = d
        return slots_option_choices_item

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
