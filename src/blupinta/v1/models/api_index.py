from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_index_scopes import ApiIndexScopes


T = TypeVar("T", bound="ApiIndex")


@_attrs_define
class ApiIndex:
    """`GET /v1`: what the public API is, for whoever builds an app on it

    Attributes:
        name (str):
        version (Literal['v1']):
        resource (str): the resource an app's token must be for (`resource` when asking it)
        issuer (str): where tokens come from: the OpenID provider
        discovery (str): the provider's discovery document
        scopes (ApiIndexScopes): the scopes `/v1` understands, each with what it gives
        endpoints (list[str]): every operation, as `METHOD /path`
        openapi (str): the OpenAPI document describing every operation
        docs (str): the guide's page for developers
    """

    name: str
    version: Literal["v1"]
    resource: str
    issuer: str
    discovery: str
    scopes: "ApiIndexScopes"
    endpoints: list[str]
    openapi: str
    docs: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        resource = self.resource

        issuer = self.issuer

        discovery = self.discovery

        scopes = self.scopes.to_dict()

        endpoints = self.endpoints

        openapi = self.openapi

        docs = self.docs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "resource": resource,
                "issuer": issuer,
                "discovery": discovery,
                "scopes": scopes,
                "endpoints": endpoints,
                "openapi": openapi,
                "docs": docs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_index_scopes import ApiIndexScopes

        d = dict(src_dict)
        name = d.pop("name")

        version = cast(Literal["v1"], d.pop("version"))
        if version != "v1":
            raise ValueError(f"version must match const 'v1', got '{version}'")

        resource = d.pop("resource")

        issuer = d.pop("issuer")

        discovery = d.pop("discovery")

        scopes = ApiIndexScopes.from_dict(d.pop("scopes"))

        endpoints = cast(list[str], d.pop("endpoints"))

        openapi = d.pop("openapi")

        docs = d.pop("docs")

        api_index = cls(
            name=name,
            version=version,
            resource=resource,
            issuer=issuer,
            discovery=discovery,
            scopes=scopes,
            endpoints=endpoints,
            openapi=openapi,
            docs=docs,
        )

        api_index.additional_properties = d
        return api_index

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
