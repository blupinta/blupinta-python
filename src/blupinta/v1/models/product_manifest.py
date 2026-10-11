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

from ..models.mount import Mount
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_option import ChoiceOption
    from ..models.clearance import Clearance
    from ..models.geometry_source_type_0 import GeometrySourceType0
    from ..models.geometry_source_type_1 import GeometrySourceType1
    from ..models.geometry_source_type_2 import GeometrySourceType2
    from ..models.geometry_source_type_3 import GeometrySourceType3
    from ..models.image_option import ImageOption
    from ..models.material_option import MaterialOption
    from ..models.number_option import NumberOption
    from ..models.product_manifest_bindings_item import ProductManifestBindingsItem
    from ..models.product_manifest_links_item import ProductManifestLinksItem
    from ..models.product_manifest_media import ProductManifestMedia
    from ..models.product_manifest_size import ProductManifestSize
    from ..models.product_manifest_variants_item import ProductManifestVariantsItem
    from ..models.slots_option import SlotsOption
    from ..models.text_option import TextOption
    from ..models.toggle_option import ToggleOption
    from ..models.translated import Translated


T = TypeVar("T", bound="ProductManifest")


@_attrs_define
class ProductManifest:
    """
    Attributes:
        id (str): namespace/name, stable forever ("ikea/kallax", "jal/handmade-drawers")
        version (float): bumped on any change that can move or reshape an item
        name (Translated): App content, shared by every user: in each of the app's languages (furnishing.md F5)
        category (str): a path in the shared taxonomy: "storage/shelving", "lighting/pendant", "decor/wall-art"
        tags (list[str]):
        mount (Mount):
        options (list[Union['ChoiceOption', 'ImageOption', 'MaterialOption', 'NumberOption', 'SlotsOption',
            'TextOption', 'ToggleOption']]):
        geometry (Union['GeometrySourceType0', 'GeometrySourceType1', 'GeometrySourceType2', 'GeometrySourceType3']):
        size (ProductManifestSize): width (x), height (y), depth (z) as expressions of the options, m
        source (str): the product sheet or the measurement it comes from
        brand (Union[Unset, str]):
        description (Union[Unset, Translated]): App content, shared by every user: in each of the app's languages
            (furnishing.md F5)
        variants (Union[Unset, list['ProductManifestVariantsItem']]): option combinations the maker sells under its own
            article number (a slots option's as its slots' choices)
        clearances (Union[Unset, list['Clearance']]): the space it needs in use, beside its sides (furnishing.md §8):
            drawers pulled out, a door's swing, a chair
        bindings (Union[Unset, list['ProductManifestBindingsItem']]): what in it a house entity can drive
        media (Union[Unset, ProductManifestMedia]):
        links (Union[Unset, list['ProductManifestLinksItem']]):
    """

    id: str
    version: float
    name: "Translated"
    category: str
    tags: list[str]
    mount: Mount
    options: list[
        Union[
            "ChoiceOption",
            "ImageOption",
            "MaterialOption",
            "NumberOption",
            "SlotsOption",
            "TextOption",
            "ToggleOption",
        ]
    ]
    geometry: Union[
        "GeometrySourceType0",
        "GeometrySourceType1",
        "GeometrySourceType2",
        "GeometrySourceType3",
    ]
    size: "ProductManifestSize"
    source: str
    brand: Union[Unset, str] = UNSET
    description: Union[Unset, "Translated"] = UNSET
    variants: Union[Unset, list["ProductManifestVariantsItem"]] = UNSET
    clearances: Union[Unset, list["Clearance"]] = UNSET
    bindings: Union[Unset, list["ProductManifestBindingsItem"]] = UNSET
    media: Union[Unset, "ProductManifestMedia"] = UNSET
    links: Union[Unset, list["ProductManifestLinksItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.choice_option import ChoiceOption
        from ..models.geometry_source_type_0 import GeometrySourceType0
        from ..models.geometry_source_type_1 import GeometrySourceType1
        from ..models.geometry_source_type_2 import GeometrySourceType2
        from ..models.image_option import ImageOption
        from ..models.material_option import MaterialOption
        from ..models.number_option import NumberOption
        from ..models.slots_option import SlotsOption
        from ..models.toggle_option import ToggleOption

        id = self.id

        version = self.version

        name = self.name.to_dict()

        category = self.category

        tags = self.tags

        mount = self.mount.value

        options = []
        for options_item_data in self.options:
            options_item: dict[str, Any]
            if isinstance(options_item_data, ChoiceOption):
                options_item = options_item_data.to_dict()
            elif isinstance(options_item_data, MaterialOption):
                options_item = options_item_data.to_dict()
            elif isinstance(options_item_data, NumberOption):
                options_item = options_item_data.to_dict()
            elif isinstance(options_item_data, ToggleOption):
                options_item = options_item_data.to_dict()
            elif isinstance(options_item_data, ImageOption):
                options_item = options_item_data.to_dict()
            elif isinstance(options_item_data, SlotsOption):
                options_item = options_item_data.to_dict()
            else:
                options_item = options_item_data.to_dict()

            options.append(options_item)

        geometry: dict[str, Any]
        if isinstance(self.geometry, GeometrySourceType0):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, GeometrySourceType1):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, GeometrySourceType2):
            geometry = self.geometry.to_dict()
        else:
            geometry = self.geometry.to_dict()

        size = self.size.to_dict()

        source = self.source

        brand = self.brand

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        variants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        clearances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.clearances, Unset):
            clearances = []
            for clearances_item_data in self.clearances:
                clearances_item = clearances_item_data.to_dict()
                clearances.append(clearances_item)

        bindings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bindings, Unset):
            bindings = []
            for bindings_item_data in self.bindings:
                bindings_item = bindings_item_data.to_dict()
                bindings.append(bindings_item)

        media: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "name": name,
                "category": category,
                "tags": tags,
                "mount": mount,
                "options": options,
                "geometry": geometry,
                "size": size,
                "source": source,
            }
        )
        if brand is not UNSET:
            field_dict["brand"] = brand
        if description is not UNSET:
            field_dict["description"] = description
        if variants is not UNSET:
            field_dict["variants"] = variants
        if clearances is not UNSET:
            field_dict["clearances"] = clearances
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if media is not UNSET:
            field_dict["media"] = media
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_option import ChoiceOption
        from ..models.clearance import Clearance
        from ..models.geometry_source_type_0 import GeometrySourceType0
        from ..models.geometry_source_type_1 import GeometrySourceType1
        from ..models.geometry_source_type_2 import GeometrySourceType2
        from ..models.geometry_source_type_3 import GeometrySourceType3
        from ..models.image_option import ImageOption
        from ..models.material_option import MaterialOption
        from ..models.number_option import NumberOption
        from ..models.product_manifest_bindings_item import ProductManifestBindingsItem
        from ..models.product_manifest_links_item import ProductManifestLinksItem
        from ..models.product_manifest_media import ProductManifestMedia
        from ..models.product_manifest_size import ProductManifestSize
        from ..models.product_manifest_variants_item import ProductManifestVariantsItem
        from ..models.slots_option import SlotsOption
        from ..models.text_option import TextOption
        from ..models.toggle_option import ToggleOption
        from ..models.translated import Translated

        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        name = Translated.from_dict(d.pop("name"))

        category = d.pop("category")

        tags = cast(list[str], d.pop("tags"))

        mount = Mount(d.pop("mount"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:

            def _parse_options_item(
                data: object,
            ) -> Union[
                "ChoiceOption",
                "ImageOption",
                "MaterialOption",
                "NumberOption",
                "SlotsOption",
                "TextOption",
                "ToggleOption",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_0 = ChoiceOption.from_dict(data)

                    return componentsschemas_option_spec_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_1 = MaterialOption.from_dict(
                        data
                    )

                    return componentsschemas_option_spec_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_2 = NumberOption.from_dict(data)

                    return componentsschemas_option_spec_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_3 = ToggleOption.from_dict(data)

                    return componentsschemas_option_spec_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_4 = ImageOption.from_dict(data)

                    return componentsschemas_option_spec_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_option_spec_type_5 = SlotsOption.from_dict(data)

                    return componentsschemas_option_spec_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_option_spec_type_6 = TextOption.from_dict(data)

                return componentsschemas_option_spec_type_6

            options_item = _parse_options_item(options_item_data)

            options.append(options_item)

        def _parse_geometry(
            data: object,
        ) -> Union[
            "GeometrySourceType0",
            "GeometrySourceType1",
            "GeometrySourceType2",
            "GeometrySourceType3",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_geometry_source_type_0 = (
                    GeometrySourceType0.from_dict(data)
                )

                return componentsschemas_geometry_source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_geometry_source_type_1 = (
                    GeometrySourceType1.from_dict(data)
                )

                return componentsschemas_geometry_source_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_geometry_source_type_2 = (
                    GeometrySourceType2.from_dict(data)
                )

                return componentsschemas_geometry_source_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_geometry_source_type_3 = GeometrySourceType3.from_dict(
                data
            )

            return componentsschemas_geometry_source_type_3

        geometry = _parse_geometry(d.pop("geometry"))

        size = ProductManifestSize.from_dict(d.pop("size"))

        source = d.pop("source")

        brand = d.pop("brand", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, Translated]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = Translated.from_dict(_description)

        variants = []
        _variants = d.pop("variants", UNSET)
        for variants_item_data in _variants or []:
            variants_item = ProductManifestVariantsItem.from_dict(variants_item_data)

            variants.append(variants_item)

        clearances = []
        _clearances = d.pop("clearances", UNSET)
        for clearances_item_data in _clearances or []:
            clearances_item = Clearance.from_dict(clearances_item_data)

            clearances.append(clearances_item)

        bindings = []
        _bindings = d.pop("bindings", UNSET)
        for bindings_item_data in _bindings or []:
            bindings_item = ProductManifestBindingsItem.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        _media = d.pop("media", UNSET)
        media: Union[Unset, ProductManifestMedia]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = ProductManifestMedia.from_dict(_media)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ProductManifestLinksItem.from_dict(links_item_data)

            links.append(links_item)

        product_manifest = cls(
            id=id,
            version=version,
            name=name,
            category=category,
            tags=tags,
            mount=mount,
            options=options,
            geometry=geometry,
            size=size,
            source=source,
            brand=brand,
            description=description,
            variants=variants,
            clearances=clearances,
            bindings=bindings,
            media=media,
            links=links,
        )

        product_manifest.additional_properties = d
        return product_manifest

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
