from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1SaveRevisionRequest")


@_attrs_define
class V1SaveRevisionRequest:
    """A version to save: a home, a line saying what changed, and the version it starts from

    Attributes:
        home (Any): the home, in any version of the format: brought to the current one as an import is
        message (str): what changed, as people read it in the project's history
        base_revision (Union[None, int]): the last version the app had when it made this home; null when the project had
            none. Another one saved since: a `conflict`, so nobody's work is overwritten unseen
        thumbnail (Union[Unset, str]): a picture of the home, WebP as base64, at most 256 kB; the version keeps none
            without it
    """

    home: Any
    message: str
    base_revision: Union[None, int]
    thumbnail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        home = self.home

        message = self.message

        base_revision: Union[None, int]
        base_revision = self.base_revision

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "home": home,
                "message": message,
                "baseRevision": base_revision,
            }
        )
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        home = d.pop("home")

        message = d.pop("message")

        def _parse_base_revision(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        base_revision = _parse_base_revision(d.pop("baseRevision"))

        thumbnail = d.pop("thumbnail", UNSET)

        v1_save_revision_request = cls(
            home=home,
            message=message,
            base_revision=base_revision,
            thumbnail=thumbnail,
        )

        v1_save_revision_request.additional_properties = d
        return v1_save_revision_request

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
