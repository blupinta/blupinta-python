from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recipe_part_type_0 import RecipePartType0
    from ..models.recipe_part_type_1 import RecipePartType1


T = TypeVar("T", bound="GeometrySourceType3")


@_attrs_define
class GeometrySourceType3:
    """
    Attributes:
        kind (Literal['recipe']):
        parts (list[Union['RecipePartType0', 'RecipePartType1']]):
    """

    kind: Literal["recipe"]
    parts: list[Union["RecipePartType0", "RecipePartType1"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_part_type_0 import RecipePartType0

        kind = self.kind

        parts = []
        for parts_item_data in self.parts:
            parts_item: dict[str, Any]
            if isinstance(parts_item_data, RecipePartType0):
                parts_item = parts_item_data.to_dict()
            else:
                parts_item = parts_item_data.to_dict()

            parts.append(parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "parts": parts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_part_type_0 import RecipePartType0
        from ..models.recipe_part_type_1 import RecipePartType1

        d = dict(src_dict)
        kind = cast(Literal["recipe"], d.pop("kind"))
        if kind != "recipe":
            raise ValueError(f"kind must match const 'recipe', got '{kind}'")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:

            def _parse_parts_item(
                data: object,
            ) -> Union["RecipePartType0", "RecipePartType1"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_recipe_part_type_0 = RecipePartType0.from_dict(
                        data
                    )

                    return componentsschemas_recipe_part_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_recipe_part_type_1 = RecipePartType1.from_dict(data)

                return componentsschemas_recipe_part_type_1

            parts_item = _parse_parts_item(parts_item_data)

            parts.append(parts_item)

        geometry_source_type_3 = cls(
            kind=kind,
            parts=parts,
        )

        geometry_source_type_3.additional_properties = d
        return geometry_source_type_3

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
