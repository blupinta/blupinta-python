from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v1_device import V1Device


T = TypeVar("T", bound="V1Devices")


@_attrs_define
class V1Devices:
    """The devices an app declares for a project, replaced whole each time

    Attributes:
        devices (list['V1Device']):
    """

    devices: list["V1Device"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()
            devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "devices": devices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_device import V1Device

        d = dict(src_dict)
        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = V1Device.from_dict(devices_item_data)

            devices.append(devices_item)

        v1_devices = cls(
            devices=devices,
        )

        v1_devices.additional_properties = d
        return v1_devices

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
