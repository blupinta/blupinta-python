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
    from ..models.choice_option_choices_item_params import ChoiceOptionChoicesItemParams
    from ..models.condition import Condition
    from ..models.translated import Translated


T = TypeVar("T", bound="ChoiceOptionChoicesItem")


@_attrs_define
class ChoiceOptionChoicesItem:
    """
    Attributes:
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        params (Union[Unset, ChoiceOptionChoicesItemParams]):
        allowed_if (Union[Unset, list['Condition']]): A rule between options (furnishing.md §3, a modular system): a
            value is offered only while every condition holds (BESTÅ's 180 frame only in white)
    """

    id: str
    name: "Translated"
    params: Union[Unset, "ChoiceOptionChoicesItemParams"] = UNSET
    allowed_if: Union[Unset, list["Condition"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.to_dict()

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        allowed_if: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allowed_if, Unset):
            allowed_if = []
            for componentsschemas_allowed_if_item_data in self.allowed_if:
                componentsschemas_allowed_if_item = (
                    componentsschemas_allowed_if_item_data.to_dict()
                )
                allowed_if.append(componentsschemas_allowed_if_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params
        if allowed_if is not UNSET:
            field_dict["allowedIf"] = allowed_if

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_option_choices_item_params import (
            ChoiceOptionChoicesItemParams,
        )
        from ..models.condition import Condition
        from ..models.translated import Translated

        d = dict(src_dict)
        id = d.pop("id")

        name = Translated.from_dict(d.pop("name"))

        _params = d.pop("params", UNSET)
        params: Union[Unset, ChoiceOptionChoicesItemParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ChoiceOptionChoicesItemParams.from_dict(_params)

        allowed_if = []
        _allowed_if = d.pop("allowedIf", UNSET)
        for componentsschemas_allowed_if_item_data in _allowed_if or []:
            componentsschemas_allowed_if_item = Condition.from_dict(
                componentsschemas_allowed_if_item_data
            )

            allowed_if.append(componentsschemas_allowed_if_item)

        choice_option_choices_item = cls(
            id=id,
            name=name,
            params=params,
            allowed_if=allowed_if,
        )

        choice_option_choices_item.additional_properties = d
        return choice_option_choices_item

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
