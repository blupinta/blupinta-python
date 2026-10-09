from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_file_content_type import V1FileContentType

T = TypeVar("T", bound="V1File")


@_attrs_define
class V1File:
    """A file of a project, as uploaded

    Attributes:
        sha256 (str): its content's hash: how a home names it (a drawing's `src`, a floor's image)
        content_type (V1FileContentType):
        size (int): in bytes
        name (str): its name, as uploaded
        created_at (str): when it was first uploaded, ISO 8601
    """

    sha256: str
    content_type: V1FileContentType
    size: int
    name: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        content_type = self.content_type.value

        size = self.size

        name = self.name

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "contentType": content_type,
                "size": size,
                "name": name,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        content_type = V1FileContentType(d.pop("contentType"))

        size = d.pop("size")

        name = d.pop("name")

        created_at = d.pop("createdAt")

        v1_file = cls(
            sha256=sha256,
            content_type=content_type,
            size=size,
            name=name,
            created_at=created_at,
        )

        v1_file.additional_properties = d
        return v1_file

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
