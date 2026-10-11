from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="V1ProductVariantsItemOptions")


@_attrs_define
class V1ProductVariantsItemOptions:
    """ """

    additional_properties: dict[
        str, Union[bool, float, list[Union[None, str]], str]
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for componentsschemas_variant_value_type_3_item_data in prop:
                    componentsschemas_variant_value_type_3_item: Union[None, str]
                    componentsschemas_variant_value_type_3_item = (
                        componentsschemas_variant_value_type_3_item_data
                    )
                    field_dict[prop_name].append(
                        componentsschemas_variant_value_type_3_item
                    )

            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v1_product_variants_item_options = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[bool, float, list[Union[None, str]], str]:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    componentsschemas_variant_value_type_3 = []
                    _componentsschemas_variant_value_type_3 = data
                    for (
                        componentsschemas_variant_value_type_3_item_data
                    ) in _componentsschemas_variant_value_type_3:

                        def _parse_componentsschemas_variant_value_type_3_item(
                            data: object,
                        ) -> Union[None, str]:
                            if data is None:
                                return data
                            return cast(Union[None, str], data)

                        componentsschemas_variant_value_type_3_item = (
                            _parse_componentsschemas_variant_value_type_3_item(
                                componentsschemas_variant_value_type_3_item_data
                            )
                        )

                        componentsschemas_variant_value_type_3.append(
                            componentsschemas_variant_value_type_3_item
                        )

                    return componentsschemas_variant_value_type_3
                except:  # noqa: E722
                    pass
                return cast(Union[bool, float, list[Union[None, str]], str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        v1_product_variants_item_options.additional_properties = additional_properties
        return v1_product_variants_item_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[bool, float, list[Union[None, str]], str]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union[bool, float, list[Union[None, str]], str]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
