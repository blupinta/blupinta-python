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

from ..models.number_option_unit import NumberOptionUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition import Condition
    from ..models.translated import Translated


T = TypeVar("T", bound="NumberOption")


@_attrs_define
class NumberOption:
    """
    Attributes:
        kind (Literal['number']):
        min_ (float):
        max_ (float):
        step (float):
        unit (NumberOptionUnit):
        default (float):
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        visible_if (Union[Unset, Condition]): Shows (or allows) an option only when another holds one of some values
    """

    kind: Literal["number"]
    min_: float
    max_: float
    step: float
    unit: NumberOptionUnit
    default: float
    id: str
    name: "Translated"
    visible_if: Union[Unset, "Condition"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        min_ = self.min_

        max_ = self.max_

        step = self.step

        unit = self.unit.value

        default = self.default

        id = self.id

        name = self.name.to_dict()

        visible_if: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visible_if, Unset):
            visible_if = self.visible_if.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "min": min_,
                "max": max_,
                "step": step,
                "unit": unit,
                "default": default,
                "id": id,
                "name": name,
            }
        )
        if visible_if is not UNSET:
            field_dict["visibleIf"] = visible_if

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition import Condition
        from ..models.translated import Translated

        d = dict(src_dict)
        kind = cast(Literal["number"], d.pop("kind"))
        if kind != "number":
            raise ValueError(f"kind must match const 'number', got '{kind}'")

        min_ = d.pop("min")

        max_ = d.pop("max")

        step = d.pop("step")

        unit = NumberOptionUnit(d.pop("unit"))

        default = d.pop("default")

        id = d.pop("id")

        name = Translated.from_dict(d.pop("name"))

        _visible_if = d.pop("visibleIf", UNSET)
        visible_if: Union[Unset, Condition]
        if isinstance(_visible_if, Unset):
            visible_if = UNSET
        else:
            visible_if = Condition.from_dict(_visible_if)

        number_option = cls(
            kind=kind,
            min_=min_,
            max_=max_,
            step=step,
            unit=unit,
            default=default,
            id=id,
            name=name,
            visible_if=visible_if,
        )

        number_option.additional_properties = d
        return number_option

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
