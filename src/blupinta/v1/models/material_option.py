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
    from ..models.material_option_allowed_if import MaterialOptionAllowedIf
    from ..models.translated import Translated


T = TypeVar("T", bound="MaterialOption")


@_attrs_define
class MaterialOption:
    """
    Attributes:
        kind (Literal['material']):
        materials (list[str]): the library's materials it is sold in
        default (str):
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        allowed_if (Union[Unset, MaterialOptionAllowedIf]): the materials sold only with some other values, by material
        visible_if (Union[Unset, Condition]): Shows (or allows) an option only when another holds one of some values
    """

    kind: Literal["material"]
    materials: list[str]
    default: str
    id: str
    name: "Translated"
    allowed_if: Union[Unset, "MaterialOptionAllowedIf"] = UNSET
    visible_if: Union[Unset, "Condition"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        materials = self.materials

        default = self.default

        id = self.id

        name = self.name.to_dict()

        allowed_if: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.allowed_if, Unset):
            allowed_if = self.allowed_if.to_dict()

        visible_if: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visible_if, Unset):
            visible_if = self.visible_if.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "materials": materials,
                "default": default,
                "id": id,
                "name": name,
            }
        )
        if allowed_if is not UNSET:
            field_dict["allowedIf"] = allowed_if
        if visible_if is not UNSET:
            field_dict["visibleIf"] = visible_if

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition import Condition
        from ..models.material_option_allowed_if import MaterialOptionAllowedIf
        from ..models.translated import Translated

        d = dict(src_dict)
        kind = cast(Literal["material"], d.pop("kind"))
        if kind != "material":
            raise ValueError(f"kind must match const 'material', got '{kind}'")

        materials = cast(list[str], d.pop("materials"))

        default = d.pop("default")

        id = d.pop("id")

        name = Translated.from_dict(d.pop("name"))

        _allowed_if = d.pop("allowedIf", UNSET)
        allowed_if: Union[Unset, MaterialOptionAllowedIf]
        if isinstance(_allowed_if, Unset):
            allowed_if = UNSET
        else:
            allowed_if = MaterialOptionAllowedIf.from_dict(_allowed_if)

        _visible_if = d.pop("visibleIf", UNSET)
        visible_if: Union[Unset, Condition]
        if isinstance(_visible_if, Unset):
            visible_if = UNSET
        else:
            visible_if = Condition.from_dict(_visible_if)

        material_option = cls(
            kind=kind,
            materials=materials,
            default=default,
            id=id,
            name=name,
            allowed_if=allowed_if,
            visible_if=visible_if,
        )

        material_option.additional_properties = d
        return material_option

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
