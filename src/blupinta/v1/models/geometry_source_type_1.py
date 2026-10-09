from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeometrySourceType1")


@_attrs_define
class GeometrySourceType1:
    """
    Attributes:
        kind (Literal['envelope']):
        material (Union[Unset, str]):
    """

    kind: Literal["envelope"]
    material: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        material = self.material

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if material is not UNSET:
            field_dict["material"] = material

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["envelope"], d.pop("kind"))
        if kind != "envelope":
            raise ValueError(f"kind must match const 'envelope', got '{kind}'")

        material = d.pop("material", UNSET)

        geometry_source_type_1 = cls(
            kind=kind,
            material=material,
        )

        geometry_source_type_1.additional_properties = d
        return geometry_source_type_1

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
