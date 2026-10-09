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
    from ..models.translated import Translated


T = TypeVar("T", bound="ChoiceOptionChoicesItem")


@_attrs_define
class ChoiceOptionChoicesItem:
    """
    Attributes:
        id (str):
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        params (Union[Unset, ChoiceOptionChoicesItemParams]):
    """

    id: str
    name: "Translated"
    params: Union[Unset, "ChoiceOptionChoicesItemParams"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.to_dict()

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_option_choices_item_params import (
            ChoiceOptionChoicesItemParams,
        )
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

        choice_option_choices_item = cls(
            id=id,
            name=name,
            params=params,
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
