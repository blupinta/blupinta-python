from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipe_part_type_0_shape import RecipePartType0Shape
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.material_ref_type_0 import MaterialRefType0
    from ..models.material_ref_type_1 import MaterialRefType1
    from ..models.when import When


T = TypeVar("T", bound="RecipePartType0")


@_attrs_define
class RecipePartType0:
    """
    Attributes:
        shape (RecipePartType0Shape):
        size (list[str]): Three expressions of the options, m: x, y, z or w, h, d
        material (Union['MaterialRefType0', 'MaterialRefType1']): A part's finish: what a material option holds, or a
            material of the library
        at (list[str]): Three expressions of the options, m: x, y, z or w, h, d
        count (Union[Unset, str]): how many, an expression; 0 leaves it out (an option switching a part off)
        slots (Union[Unset, str]): one copy per slot of this slots option (`count` of them in each, then): in the part's
            `when` and its models', the option names this slot's own value; `index` names the slot's position
        copy (Union[Unset, str]): in a part made per slot with a count, the name each copy's number within its slot goes
            by
        when (Union[Unset, When]): Option values that must all hold: a choice's or a material's id, a number, yes or no;
            in a part made per slot, null for its slot left empty
        index (Union[Unset, str]): the name each copy's number (0, 1, …) goes by in the part's expressions
        name (Union[Unset, str]): what the part is ("drawer 1"), for clearances and, later, animation
    """

    shape: RecipePartType0Shape
    size: list[str]
    material: Union["MaterialRefType0", "MaterialRefType1"]
    at: list[str]
    count: Union[Unset, str] = UNSET
    slots: Union[Unset, str] = UNSET
    copy: Union[Unset, str] = UNSET
    when: Union[Unset, "When"] = UNSET
    index: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.material_ref_type_0 import MaterialRefType0

        shape = self.shape.value

        size = self.size

        material: dict[str, Any]
        if isinstance(self.material, MaterialRefType0):
            material = self.material.to_dict()
        else:
            material = self.material.to_dict()

        at = self.at

        count = self.count

        slots = self.slots

        copy = self.copy

        when: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.to_dict()

        index = self.index

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shape": shape,
                "size": size,
                "material": material,
                "at": at,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if slots is not UNSET:
            field_dict["slots"] = slots
        if copy is not UNSET:
            field_dict["copy"] = copy
        if when is not UNSET:
            field_dict["when"] = when
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material_ref_type_0 import MaterialRefType0
        from ..models.material_ref_type_1 import MaterialRefType1
        from ..models.when import When

        d = dict(src_dict)
        shape = RecipePartType0Shape(d.pop("shape"))

        size = cast(list[str], d.pop("size"))

        def _parse_material(
            data: object,
        ) -> Union["MaterialRefType0", "MaterialRefType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_material_ref_type_0 = MaterialRefType0.from_dict(data)

                return componentsschemas_material_ref_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_material_ref_type_1 = MaterialRefType1.from_dict(data)

            return componentsschemas_material_ref_type_1

        material = _parse_material(d.pop("material"))

        at = cast(list[str], d.pop("at"))

        count = d.pop("count", UNSET)

        slots = d.pop("slots", UNSET)

        copy = d.pop("copy", UNSET)

        _when = d.pop("when", UNSET)
        when: Union[Unset, When]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = When.from_dict(_when)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        recipe_part_type_0 = cls(
            shape=shape,
            size=size,
            material=material,
            at=at,
            count=count,
            slots=slots,
            copy=copy,
            when=when,
            index=index,
            name=name,
        )

        recipe_part_type_0.additional_properties = d
        return recipe_part_type_0

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
