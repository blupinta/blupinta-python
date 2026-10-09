from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v1_error_code import V1ErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1Error")


@_attrs_define
class V1Error:
    """The body of a refusal

    Attributes:
        error (V1ErrorCode): What `/v1` answers when it refuses
        error_id (Union[Unset, str]): the server's id for a `server_error`, to quote when asking for help
        problems (Union[Unset, list[str]]): what is wrong, for `invalid_input`, `conflict`, `invalid_home`,
            `blocking_problems`
    """

    error: V1ErrorCode
    error_id: Union[Unset, str] = UNSET
    problems: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        error_id = self.error_id

        problems: Union[Unset, list[str]] = UNSET
        if not isinstance(self.problems, Unset):
            problems = self.problems

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if error_id is not UNSET:
            field_dict["errorId"] = error_id
        if problems is not UNSET:
            field_dict["problems"] = problems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = V1ErrorCode(d.pop("error"))

        error_id = d.pop("errorId", UNSET)

        problems = cast(list[str], d.pop("problems", UNSET))

        v1_error = cls(
            error=error,
            error_id=error_id,
            problems=problems,
        )

        v1_error.additional_properties = d
        return v1_error

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
