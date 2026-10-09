from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v1_host_reference import V1HostReference


T = TypeVar("T", bound="V1HostReferences")


@_attrs_define
class V1HostReferences:
    """The elements an app declares it needs: saving a version that drops one is refused, naming the app

    Attributes:
        refs (list['V1HostReference']):
    """

    refs: list["V1HostReference"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refs = []
        for refs_item_data in self.refs:
            refs_item = refs_item_data.to_dict()
            refs.append(refs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refs": refs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_host_reference import V1HostReference

        d = dict(src_dict)
        refs = []
        _refs = d.pop("refs")
        for refs_item_data in _refs:
            refs_item = V1HostReference.from_dict(refs_item_data)

            refs.append(refs_item)

        v1_host_references = cls(
            refs=refs,
        )

        v1_host_references.additional_properties = d
        return v1_host_references

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
