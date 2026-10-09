from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_home_problem_detail import V1HomeProblemDetail


T = TypeVar("T", bound="V1HomeProblem")


@_attrs_define
class V1HomeProblem:
    """One problem the server finds in a home

    Attributes:
        kind (str): `format`: the file isn't a home of the format (`message` says what, with its path); otherwise a
            check that blocks saving it as a version: `area-without-rooms`, `open-room`, `crossing`, `overlap`,
            `degenerate`, `shared-region`…
        message (Union[Unset, str]): for `format`: what is wrong, with its path in the file
        plan (Union[Unset, str]): the plan it concerns, by id, when it concerns one
        detail (Union[Unset, V1HomeProblemDetail]): the problem as the checks found it: its walls, rooms, points, by the
            home's ids
    """

    kind: str
    message: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    detail: Union[Unset, "V1HomeProblemDetail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        message = self.message

        plan = self.plan

        detail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if plan is not UNSET:
            field_dict["plan"] = plan
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_home_problem_detail import V1HomeProblemDetail

        d = dict(src_dict)
        kind = d.pop("kind")

        message = d.pop("message", UNSET)

        plan = d.pop("plan", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: Union[Unset, V1HomeProblemDetail]
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = V1HomeProblemDetail.from_dict(_detail)

        v1_home_problem = cls(
            kind=kind,
            message=message,
            plan=plan,
            detail=detail,
        )

        v1_home_problem.additional_properties = d
        return v1_home_problem

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
