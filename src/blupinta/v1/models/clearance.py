from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clearance_side import ClearanceSide
from ..models.clearance_use import ClearanceUse

T = TypeVar("T", bound="Clearance")


@_attrs_define
class Clearance:
    """
    Attributes:
        use (ClearanceUse): What a clearance is kept free for, named in the editor's warnings
        side (ClearanceSide): the side it opens out of, as the product faces: across its whole width on the front or
            back, its depth on a side
        depth (str): how far out, m, as an expression of the options
        source (str): where the measure comes from: the product sheet, a measurement, a usual allowance
    """

    use: ClearanceUse
    side: ClearanceSide
    depth: str
    source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use = self.use.value

        side = self.side.value

        depth = self.depth

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use": use,
                "side": side,
                "depth": depth,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use = ClearanceUse(d.pop("use"))

        side = ClearanceSide(d.pop("side"))

        depth = d.pop("depth")

        source = d.pop("source")

        clearance = cls(
            use=use,
            side=side,
            depth=depth,
            source=source,
        )

        clearance.additional_properties = d
        return clearance

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
