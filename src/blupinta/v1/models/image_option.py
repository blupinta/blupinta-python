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
    from ..models.condition import Condition
    from ..models.translated import Translated


T = TypeVar("T", bound="ImageOption")


@_attrs_define
class ImageOption:
    """
    Attributes:
        kind (Literal['image']):
        aspect (float): width over height of the picture's place
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        panels (Union[Unset, float]): a picture cut across panels (a multi-panel canvas), with the gap between them, m
        gap (Union[Unset, float]):
        visible_if (Union[Unset, Condition]): Shows (or allows) an option only when another holds one of some values
    """

    kind: Literal["image"]
    aspect: float
    id: str
    name: "Translated"
    panels: Union[Unset, float] = UNSET
    gap: Union[Unset, float] = UNSET
    visible_if: Union[Unset, "Condition"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        aspect = self.aspect

        id = self.id

        name = self.name.to_dict()

        panels = self.panels

        gap = self.gap

        visible_if: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visible_if, Unset):
            visible_if = self.visible_if.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "aspect": aspect,
                "id": id,
                "name": name,
            }
        )
        if panels is not UNSET:
            field_dict["panels"] = panels
        if gap is not UNSET:
            field_dict["gap"] = gap
        if visible_if is not UNSET:
            field_dict["visibleIf"] = visible_if

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition import Condition
        from ..models.translated import Translated

        d = dict(src_dict)
        kind = cast(Literal["image"], d.pop("kind"))
        if kind != "image":
            raise ValueError(f"kind must match const 'image', got '{kind}'")

        aspect = d.pop("aspect")

        id = d.pop("id")

        name = Translated.from_dict(d.pop("name"))

        panels = d.pop("panels", UNSET)

        gap = d.pop("gap", UNSET)

        _visible_if = d.pop("visibleIf", UNSET)
        visible_if: Union[Unset, Condition]
        if isinstance(_visible_if, Unset):
            visible_if = UNSET
        else:
            visible_if = Condition.from_dict(_visible_if)

        image_option = cls(
            kind=kind,
            aspect=aspect,
            id=id,
            name=name,
            panels=panels,
            gap=gap,
            visible_if=visible_if,
        )

        image_option.additional_properties = d
        return image_option

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
