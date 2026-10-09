from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_manifest_bindings_item_kind import ProductManifestBindingsItemKind

T = TypeVar("T", bound="ProductManifestBindingsItem")


@_attrs_define
class ProductManifestBindingsItem:
    """
    Attributes:
        slot (str):
        kind (ProductManifestBindingsItemKind):
    """

    slot: str
    kind: ProductManifestBindingsItemKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot = self.slot

        kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slot": slot,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slot = d.pop("slot")

        kind = ProductManifestBindingsItemKind(d.pop("kind"))

        product_manifest_bindings_item = cls(
            slot=slot,
            kind=kind,
        )

        product_manifest_bindings_item.additional_properties = d
        return product_manifest_bindings_item

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
