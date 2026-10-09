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


T = TypeVar("T", bound="RecipePartType1")


@_attrs_define
class RecipePartType1:
    """
    Attributes:
        shape (Literal['model']):
        models (list['ModelChoice']):
        at (list[str]): Three expressions of the options, m: x, y, z or w, h, d
        count (Union[Unset, str]): how many, an expression; 0 leaves it out (an option switching a part off)
        index (Union[Unset, str]): the name each copy's number (0, 1, …) goes by in the part's expressions
        name (Union[Unset, str]): what the part is ("drawer 1"), for clearances and, later, animation
    """

    shape: Literal["model"]
    models: list["ModelChoice"]
    at: list[str]
    count: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        at = self.at

        count = self.count

        index = self.index

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shape": shape,
                "models": models,
                "at": at,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_choice import ModelChoice

        d = dict(src_dict)
        shape = cast(Literal["model"], d.pop("shape"))
        if shape != "model":
            raise ValueError(f"shape must match const 'model', got '{shape}'")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelChoice.from_dict(models_item_data)

            models.append(models_item)

        at = cast(list[str], d.pop("at"))

        count = d.pop("count", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        recipe_part_type_1 = cls(
            shape=shape,
            models=models,
            at=at,
            count=count,
            index=index,
            name=name,
        )

        recipe_part_type_1.additional_properties = d
        return recipe_part_type_1

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
