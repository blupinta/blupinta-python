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
    from ..models.v1_project_last_revision_type_0 import V1ProjectLastRevisionType0


T = TypeVar("T", bound="V1Project")


@_attrs_define
class V1Project:
    """A project an app may read

    Attributes:
        id (str):
        name (str): its name, as its people wrote it
        address (Union[None, str]): where the home is, when they wrote it; null otherwise
        last_revision (Union['V1ProjectLastRevisionType0', None]): the last version saved; null before the first
    """

    id: str
    name: str
    address: Union[None, str]
    last_revision: Union["V1ProjectLastRevisionType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.v1_project_last_revision_type_0 import V1ProjectLastRevisionType0

        id = self.id

        name = self.name

        address: Union[None, str]
        address = self.address

        last_revision: Union[None, dict[str, Any]]
        if isinstance(self.last_revision, V1ProjectLastRevisionType0):
            last_revision = self.last_revision.to_dict()
        else:
            last_revision = self.last_revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "address": address,
                "lastRevision": last_revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_project_last_revision_type_0 import V1ProjectLastRevisionType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_address(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        address = _parse_address(d.pop("address"))

        def _parse_last_revision(
            data: object,
        ) -> Union["V1ProjectLastRevisionType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_revision_type_0 = V1ProjectLastRevisionType0.from_dict(data)

                return last_revision_type_0
            except:  # noqa: E722
                pass
            return cast(Union["V1ProjectLastRevisionType0", None], data)

        last_revision = _parse_last_revision(d.pop("lastRevision"))

        v1_project = cls(
            id=id,
            name=name,
            address=address,
            last_revision=last_revision,
        )

        v1_project.additional_properties = d
        return v1_project

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
