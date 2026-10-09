from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_ref import ModelRef
    from ..models.when import When


T = TypeVar("T", bound="ModelChoice")


@_attrs_define
class ModelChoice:
    """A model and the options that choose it; one without `when` is the fallback

    Attributes:
        model (ModelRef): A model of the catalog: its bytes' sha256, and the file it is published from (`pnpm
            catalog:assets`)
        when (Union[Unset, When]): Option values that must all hold: a choice's or a material's id, a number, yes or no
        lod (Union[Unset, ModelRef]): A model of the catalog: its bytes' sha256, and the file it is published from
            (`pnpm catalog:assets`)
    """

    model: "ModelRef"
    when: Union[Unset, "When"] = UNSET
    lod: Union[Unset, "ModelRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        when: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.to_dict()

        lod: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lod, Unset):
            lod = self.lod.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if when is not UNSET:
            field_dict["when"] = when
        if lod is not UNSET:
            field_dict["lod"] = lod

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef
        from ..models.when import When

        d = dict(src_dict)
        model = ModelRef.from_dict(d.pop("model"))

        _when = d.pop("when", UNSET)
        when: Union[Unset, When]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = When.from_dict(_when)

        _lod = d.pop("lod", UNSET)
        lod: Union[Unset, ModelRef]
        if isinstance(_lod, Unset):
            lod = UNSET
        else:
            lod = ModelRef.from_dict(_lod)

        model_choice = cls(
            model=model,
            when=when,
            lod=lod,
        )

        model_choice.additional_properties = d
        return model_choice

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
