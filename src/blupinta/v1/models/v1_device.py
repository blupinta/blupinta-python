from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_device_kind import V1DeviceKind

T = TypeVar("T", bound="V1Device")


@_attrs_define
class V1Device:
    """A device an app knows, for the editor's binding pickers

    Attributes:
        id (str): the app's own name for it: a Home Assistant entity_id (`light.soggiorno`)
        name (str): as people read it
        kind (V1DeviceKind): `cover`: shutters, curtains, awnings
        room (Union[None, str]): the room it is in, as the app calls it; null when it doesn't say
    """

    id: str
    name: str
    kind: V1DeviceKind
    room: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        kind = self.kind.value

        room: Union[None, str]
        room = self.room

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "room": room,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        kind = V1DeviceKind(d.pop("kind"))

        def _parse_room(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        room = _parse_room(d.pop("room"))

        v1_device = cls(
            id=id,
            name=name,
            kind=kind,
            room=room,
        )

        v1_device.additional_properties = d
        return v1_device

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
