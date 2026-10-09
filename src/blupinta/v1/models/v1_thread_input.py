from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v1_comment_anchor import V1CommentAnchor


T = TypeVar("T", bound="V1ThreadInput")


@_attrs_define
class V1ThreadInput:
    """A thread to open: where, and its first message

    Attributes:
        plan_id (str):
        anchor (V1CommentAnchor): Where a thread is pinned: on an element of a plan (by its kind and id), at a point of
            the plan's sheet
        body (str):
    """

    plan_id: str
    anchor: "V1CommentAnchor"
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_id = self.plan_id

        anchor = self.anchor.to_dict()

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "planId": plan_id,
                "anchor": anchor,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_comment_anchor import V1CommentAnchor

        d = dict(src_dict)
        plan_id = d.pop("planId")

        anchor = V1CommentAnchor.from_dict(d.pop("anchor"))

        body = d.pop("body")

        v1_thread_input = cls(
            plan_id=plan_id,
            anchor=anchor,
            body=body,
        )

        v1_thread_input.additional_properties = d
        return v1_thread_input

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
