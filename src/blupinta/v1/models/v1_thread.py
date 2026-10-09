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

if TYPE_CHECKING:
    from ..models.v1_comment import V1Comment
    from ..models.v1_comment_anchor import V1CommentAnchor


T = TypeVar("T", bound="V1Thread")


@_attrs_define
class V1Thread:
    """A conversation pinned on a plan

    Attributes:
        id (str):
        plan_id (str): the plan it is on, by the home's id
        anchor (V1CommentAnchor): Where a thread is pinned: on an element of a plan (by its kind and id), at a point of
            the plan's sheet
        resolved_at (Union[None, str]): when it was marked resolved; null while open
        created_at (str):
        comments (list['V1Comment']): its messages, oldest first
    """

    id: str
    plan_id: str
    anchor: "V1CommentAnchor"
    resolved_at: Union[None, str]
    created_at: str
    comments: list["V1Comment"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        plan_id = self.plan_id

        anchor = self.anchor.to_dict()

        resolved_at: Union[None, str]
        resolved_at = self.resolved_at

        created_at = self.created_at

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "planId": plan_id,
                "anchor": anchor,
                "resolvedAt": resolved_at,
                "createdAt": created_at,
                "comments": comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_comment import V1Comment
        from ..models.v1_comment_anchor import V1CommentAnchor

        d = dict(src_dict)
        id = d.pop("id")

        plan_id = d.pop("planId")

        anchor = V1CommentAnchor.from_dict(d.pop("anchor"))

        def _parse_resolved_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))

        created_at = d.pop("createdAt")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = V1Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        v1_thread = cls(
            id=id,
            plan_id=plan_id,
            anchor=anchor,
            resolved_at=resolved_at,
            created_at=created_at,
            comments=comments,
        )

        v1_thread.additional_properties = d
        return v1_thread

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
