from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="V1Comment")


@_attrs_define
class V1Comment:
    """A message in a thread

    Attributes:
        id (str):
        author_name (Union[None, str]): who wrote it: their name, or their address when they gave none; null once their
            account is gone
        body (str):
        app_name (Union[None, str]): the app that wrote it through `/v1`, as people read its name; null when written in
            the editor
        edited_at (Union[None, str]): when it was last changed, ISO 8601; null when never
        created_at (str):
    """

    id: str
    author_name: Union[None, str]
    body: str
    app_name: Union[None, str]
    edited_at: Union[None, str]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author_name: Union[None, str]
        author_name = self.author_name

        body = self.body

        app_name: Union[None, str]
        app_name = self.app_name

        edited_at: Union[None, str]
        edited_at = self.edited_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "authorName": author_name,
                "body": body,
                "appName": app_name,
                "editedAt": edited_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_author_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        author_name = _parse_author_name(d.pop("authorName"))

        body = d.pop("body")

        def _parse_app_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        app_name = _parse_app_name(d.pop("appName"))

        def _parse_edited_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        edited_at = _parse_edited_at(d.pop("editedAt"))

        created_at = d.pop("createdAt")

        v1_comment = cls(
            id=id,
            author_name=author_name,
            body=body,
            app_name=app_name,
            edited_at=edited_at,
            created_at=created_at,
        )

        v1_comment.additional_properties = d
        return v1_comment

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
