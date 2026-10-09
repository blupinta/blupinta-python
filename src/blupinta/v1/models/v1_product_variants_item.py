from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v1_product_variants_item_options import V1ProductVariantsItemOptions


T = TypeVar("T", bound="V1ProductVariantsItem")


@_attrs_define
class V1ProductVariantsItem:
    """
    Attributes:
        options (V1ProductVariantsItemOptions):
        article (str):
    """

    options: "V1ProductVariantsItemOptions"
    article: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options = self.options.to_dict()

        article = self.article

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "article": article,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_product_variants_item_options import (
            V1ProductVariantsItemOptions,
        )

        d = dict(src_dict)
        options = V1ProductVariantsItemOptions.from_dict(d.pop("options"))

        article = d.pop("article")

        v1_product_variants_item = cls(
            options=options,
            article=article,
        )

        v1_product_variants_item.additional_properties = d
        return v1_product_variants_item

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
