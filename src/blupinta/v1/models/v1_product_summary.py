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

from ..models.v1_product_summary_mount import V1ProductSummaryMount

if TYPE_CHECKING:
    from ..models.v1_product_summary_name import V1ProductSummaryName


T = TypeVar("T", bound="V1ProductSummary")


@_attrs_define
class V1ProductSummary:
    """A product of the catalog as a search lists it

    Attributes:
        id (str): `namespace/name`, stable forever ("ikea/kallax"): read it whole at
            `/v1/catalog/products/{namespace}/{name}`
        version (int): bumped on any change that can move or reshape an item made of it
        brand (Union[None, str]):
        name (V1ProductSummaryName):
        category (str): a path in the catalog's taxonomy ("storage/shelving")
        mount (V1ProductSummaryMount):
        thumbnails (list[str]): its thumbnails, by sha256: `/v1/catalog/thumbnails/{sha256}`
    """

    id: str
    version: int
    brand: Union[None, str]
    name: "V1ProductSummaryName"
    category: str
    mount: V1ProductSummaryMount
    thumbnails: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        brand: Union[None, str]
        brand = self.brand

        name = self.name.to_dict()

        category = self.category

        mount = self.mount.value

        thumbnails = self.thumbnails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "brand": brand,
                "name": name,
                "category": category,
                "mount": mount,
                "thumbnails": thumbnails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_product_summary_name import V1ProductSummaryName

        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        def _parse_brand(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        brand = _parse_brand(d.pop("brand"))

        name = V1ProductSummaryName.from_dict(d.pop("name"))

        category = d.pop("category")

        mount = V1ProductSummaryMount(d.pop("mount"))

        thumbnails = cast(list[str], d.pop("thumbnails"))

        v1_product_summary = cls(
            id=id,
            version=version,
            brand=brand,
            name=name,
            category=category,
            mount=mount,
            thumbnails=thumbnails,
        )

        v1_product_summary.additional_properties = d
        return v1_product_summary

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
