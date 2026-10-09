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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_comment_anchor_ref import V1CommentAnchorRef


T = TypeVar("T", bound="V1CommentAnchor")


@_attrs_define
class V1CommentAnchor:
    """Where a thread is pinned: on an element of a plan (by its kind and id), at a point of the plan's sheet

    Attributes:
        at (list[float]): the point, in the plan's sheet units
        ref (Union[Unset, V1CommentAnchorRef]): the element, when it is on one: `{ kind: 'wall', id: 'north' }`
    """

    at: list[float]
    ref: Union[Unset, "V1CommentAnchorRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = []
        for at_item_data in self.at:
            at_item: float
            at_item = at_item_data
            at.append(at_item)

        ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_comment_anchor_ref import V1CommentAnchorRef

        d = dict(src_dict)
        at = []
        _at = d.pop("at")
        for at_item_data in _at:

            def _parse_at_item(data: object) -> float:
                return cast(float, data)

            at_item = _parse_at_item(at_item_data)

            at.append(at_item)

        _ref = d.pop("ref", UNSET)
        ref: Union[Unset, V1CommentAnchorRef]
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = V1CommentAnchorRef.from_dict(_ref)

        v1_comment_anchor = cls(
            at=at,
            ref=ref,
        )

        v1_comment_anchor.additional_properties = d
        return v1_comment_anchor

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
