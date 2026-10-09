from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductManifestSize")


@_attrs_define
class ProductManifestSize:
    """width (x), height (y), depth (z) as expressions of the options, m

    Attributes:
        w (str):
        h (str):
        d (str):
    """

    w: str
    h: str
    d: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        w = self.w

        h = self.h

        d = self.d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "w": w,
                "h": h,
                "d": d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        w = d.pop("w")

        h = d.pop("h")

        d = d.pop("d")

        product_manifest_size = cls(
            w=w,
            h=h,
            d=d,
        )

        product_manifest_size.additional_properties = d
        return product_manifest_size

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
