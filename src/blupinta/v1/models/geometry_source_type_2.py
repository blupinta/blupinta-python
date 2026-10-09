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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_choice import ModelChoice


T = TypeVar("T", bound="GeometrySourceType2")


@_attrs_define
class GeometrySourceType2:
    """
    Attributes:
        kind (Literal['gltf']):
        models (list['ModelChoice']):
        material_variant (Union[Unset, str]):
    """

    kind: Literal["gltf"]
    models: list["ModelChoice"]
    material_variant: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        material_variant = self.material_variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "models": models,
            }
        )
        if material_variant is not UNSET:
            field_dict["materialVariant"] = material_variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_choice import ModelChoice

        d = dict(src_dict)
        kind = cast(Literal["gltf"], d.pop("kind"))
        if kind != "gltf":
            raise ValueError(f"kind must match const 'gltf', got '{kind}'")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelChoice.from_dict(models_item_data)

            models.append(models_item)

        material_variant = d.pop("materialVariant", UNSET)

        geometry_source_type_2 = cls(
            kind=kind,
            models=models,
            material_variant=material_variant,
        )

        geometry_source_type_2.additional_properties = d
        return geometry_source_type_2

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
