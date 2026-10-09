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
    from ..models.v1_product_summary import V1ProductSummary


T = TypeVar("T", bound="V1ProductPage")


@_attrs_define
class V1ProductPage:
    """A page of a catalog search

    Attributes:
        rows (list['V1ProductSummary']):
        total (int): how many products the search found in all
        next_ (Union[None, str]): where the next page starts, to send back as `after`; null on the last page
    """

    rows: list["V1ProductSummary"]
    total: int
    next_: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        total = self.total

        next_: Union[None, str]
        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "total": total,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_product_summary import V1ProductSummary

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = V1ProductSummary.from_dict(rows_item_data)

            rows.append(rows_item)

        total = d.pop("total")

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        v1_product_page = cls(
            rows=rows,
            total=total,
            next_=next_,
        )

        v1_product_page.additional_properties = d
        return v1_product_page

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
