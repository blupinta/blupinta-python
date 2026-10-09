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
    from ..models.v1_home_problem import V1HomeProblem


T = TypeVar("T", bound="V1HomeCheck")


@_attrs_define
class V1HomeCheck:
    """What the server says of a home file

    Attributes:
        read_as (Union[None, int]): the format's version the file says it is; null when it says none
        checked_at (int): the version it was checked at: the current one, the file brought to it first as an import
            would
        is_valid (bool): nothing in it keeps it from being saved as a version
        problems (list['V1HomeProblem']):
    """

    read_as: Union[None, int]
    checked_at: int
    is_valid: bool
    problems: list["V1HomeProblem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_as: Union[None, int]
        read_as = self.read_as

        checked_at = self.checked_at

        is_valid = self.is_valid

        problems = []
        for problems_item_data in self.problems:
            problems_item = problems_item_data.to_dict()
            problems.append(problems_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "readAs": read_as,
                "checkedAt": checked_at,
                "isValid": is_valid,
                "problems": problems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_home_problem import V1HomeProblem

        d = dict(src_dict)

        def _parse_read_as(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        read_as = _parse_read_as(d.pop("readAs"))

        checked_at = d.pop("checkedAt")

        is_valid = d.pop("isValid")

        problems = []
        _problems = d.pop("problems")
        for problems_item_data in _problems:
            problems_item = V1HomeProblem.from_dict(problems_item_data)

            problems.append(problems_item)

        v1_home_check = cls(
            read_as=read_as,
            checked_at=checked_at,
            is_valid=is_valid,
            problems=problems,
        )

        v1_home_check.additional_properties = d
        return v1_home_check

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
