from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="V1RevisionRow")


@_attrs_define
class V1RevisionRow:
    """A saved version of a project's home, without the home itself

    Attributes:
        number (int): the version's number, from 1, never reused
        message (str): what its author wrote when saving it
        author_name (Union[None, str]): who saved it: their name, or their address when they gave none; null once their
            account is gone
        restored_from (Union[None, int]): the version it brought back, when it was a restore; null otherwise
        created_at (str): when it was saved, ISO 8601
    """

    number: int
    message: str
    author_name: Union[None, str]
    restored_from: Union[None, int]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        message = self.message

        author_name: Union[None, str]
        author_name = self.author_name

        restored_from: Union[None, int]
        restored_from = self.restored_from

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "message": message,
                "authorName": author_name,
                "restoredFrom": restored_from,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        message = d.pop("message")

        def _parse_author_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        author_name = _parse_author_name(d.pop("authorName"))

        def _parse_restored_from(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        restored_from = _parse_restored_from(d.pop("restoredFrom"))

        created_at = d.pop("createdAt")

        v1_revision_row = cls(
            number=number,
            message=message,
            author_name=author_name,
            restored_from=restored_from,
            created_at=created_at,
        )

        v1_revision_row.additional_properties = d
        return v1_revision_row

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
