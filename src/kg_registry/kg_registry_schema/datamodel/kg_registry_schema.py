from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

metamodel_version = "None"
version = "0.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "kg_registry_schema",
        "default_range": "string",
        "description": "A schema for representing metadata about\n"
        "knowlege graphs, their sources, and their contents.",
        "id": "https://w3id.org/knowledge-graph-hub/kg_registry_schema",
        "imports": ["linkml:types"],
        "license": "GPL-3.0",
        "name": "kg_registry_schema",
        "prefixes": {
            "kg_registry_schema": {
                "prefix_prefix": "kg_registry_schema",
                "prefix_reference": "https://w3id.org/bridge2ai/data-sheets-schema/",
            },
            "skos": {
                "prefix_prefix": "skos",
                "prefix_reference": "http://www.w3.org/2004/02/skos/core#",
            },
        },
        "see_also": ["https://kghub.org/kg-registry/"],
        "source_file": "src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml",
        "title": "kg_registry_schema",
    }
)


class CompressionEnum(str, Enum):
    """
    The type of compression used with a graph component.
    """

    gzip = "gzip"
    tar = "tar"
    targz = "targz"
    zip = "zip"
    other = "other"


class GraphStandardEnum(str, Enum):
    """
    The standard or standards that a knowledge graph conforms to. These are not serializations, but rather the higher-level frameworks that the graph is built on.
    """

    kghub = "kghub"


class DataObject(ConfiguredBaseModel):
    """
    A data object. This may be any knowledge graph, a component of a graph, a collection of graphs, or a process for producing a component of a graph.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "close_mappings": ["schema:CreativeWork"],
            "from_schema": "https://w3id.org/knowledge-graph-hub/kg_registry_schema",
        }
    )

    id: str = Field(
        ...,
        description="""The identifier of the data object. This must be unique.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    name: str = Field(
        ...,
        description="""The name of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["DataObject"]}},
    )
    url: Optional[str] = Field(
        None,
        description="""The URL of the data object. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["DataObject"]}},
    )
    license: Optional[str] = Field(
        None,
        description="""The license of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "license", "domain_of": ["DataObject"]}},
    )
    version: Optional[str] = Field(
        None,
        description="""The version of the data object.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:version", "dcterms:hasVersion"],
            }
        },
    )
    language: Optional[str] = Field(
        None,
        description="""The human language of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "language", "domain_of": ["DataObject"]}},
    )
    contact_point: Optional[str] = Field(
        None,
        description="""The contact point for the data object. This should be an email address.""",
        json_schema_extra={"linkml_meta": {"alias": "contact_point", "domain_of": ["DataObject"]}},
    )


class KnowledgeGraph(DataObject):
    """
    A knowledge graph. This is any heterogeneous collection of data that is represented as nodes (entities) and edges (relationships) between them. The nodes and edges may have attributes associated with them.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "aliases": ["kg", "heterogeneous graph"],
            "from_schema": "https://w3id.org/knowledge-graph-hub/kg_registry_schema",
        }
    )

    part_of_collection: Optional[str] = Field(
        None,
        description="""The collection that the knowledge graph is part of.""",
        json_schema_extra={
            "linkml_meta": {"alias": "part_of_collection", "domain_of": ["KnowledgeGraph"]}
        },
    )
    source: Optional[str] = Field(
        None,
        description="""The source of the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "source", "domain_of": ["KnowledgeGraph"]}},
    )
    date_created: Optional[str] = Field(
        None,
        description="""The date the knowledge graph was created.""",
        json_schema_extra={
            "linkml_meta": {"alias": "date_created", "domain_of": ["KnowledgeGraph"]}
        },
    )
    date_modified: Optional[str] = Field(
        None,
        description="""The date the knowledge graph was last modified.""",
        json_schema_extra={
            "linkml_meta": {"alias": "date_modified", "domain_of": ["KnowledgeGraph"]}
        },
    )
    tags: Optional[List[str]] = Field(
        None,
        description="""Tags associated with the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "tags", "domain_of": ["KnowledgeGraph"]}},
    )
    contributors: Optional[str] = Field(
        None,
        description="""Contributors to the knowledge graph.""",
        json_schema_extra={
            "linkml_meta": {"alias": "contributors", "domain_of": ["KnowledgeGraph"]}
        },
    )
    is_active: Optional[bool] = Field(
        None,
        description="""The status of the knowledge graph. If actively updated, this should be true, otherwise false.""",
        json_schema_extra={"linkml_meta": {"alias": "is_active", "domain_of": ["KnowledgeGraph"]}},
    )
    components: Optional[List[str]] = Field(
        None,
        description="""The components of the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "components", "domain_of": ["KnowledgeGraph"]}},
    )
    conforms_to: Optional[List[GraphStandardEnum]] = Field(
        None,
        description="""The standard or standards that the knowledge graph conforms to. This is not the same as its serialization.""",
        json_schema_extra={
            "linkml_meta": {"alias": "conforms_to", "domain_of": ["KnowledgeGraph"]}
        },
    )
    edge_count: Optional[int] = Field(
        None,
        description="""The number of edges in the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "edge_count", "domain_of": ["KnowledgeGraph"]}},
    )
    node_count: Optional[int] = Field(
        None,
        description="""The number of nodes in the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "node_count", "domain_of": ["KnowledgeGraph"]}},
    )
    predicates: Optional[List[str]] = Field(
        None,
        description="""The predicate types in the knowledge graph.""",
        json_schema_extra={"linkml_meta": {"alias": "predicates", "domain_of": ["KnowledgeGraph"]}},
    )
    node_categories: Optional[List[str]] = Field(
        None,
        description="""The node categories in the knowledge graph.""",
        json_schema_extra={
            "linkml_meta": {"alias": "node_categories", "domain_of": ["KnowledgeGraph"]}
        },
    )
    id: str = Field(
        ...,
        description="""The identifier of the data object. This must be unique.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    name: str = Field(
        ...,
        description="""The name of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["DataObject"]}},
    )
    url: Optional[str] = Field(
        None,
        description="""The URL of the data object. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["DataObject"]}},
    )
    license: Optional[str] = Field(
        None,
        description="""The license of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "license", "domain_of": ["DataObject"]}},
    )
    version: Optional[str] = Field(
        None,
        description="""The version of the data object.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:version", "dcterms:hasVersion"],
            }
        },
    )
    language: Optional[str] = Field(
        None,
        description="""The human language of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "language", "domain_of": ["DataObject"]}},
    )
    contact_point: Optional[str] = Field(
        None,
        description="""The contact point for the data object. This should be an email address.""",
        json_schema_extra={"linkml_meta": {"alias": "contact_point", "domain_of": ["DataObject"]}},
    )


class KnowledgeGraphCollection(DataObject):
    """
    A collection of knowledge graphs.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/knowledge-graph-hub/kg_registry_schema"}
    )

    id: str = Field(
        ...,
        description="""The identifier of the data object. This must be unique.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    name: str = Field(
        ...,
        description="""The name of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["DataObject"]}},
    )
    url: Optional[str] = Field(
        None,
        description="""The URL of the data object. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["DataObject"]}},
    )
    license: Optional[str] = Field(
        None,
        description="""The license of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "license", "domain_of": ["DataObject"]}},
    )
    version: Optional[str] = Field(
        None,
        description="""The version of the data object.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:version", "dcterms:hasVersion"],
            }
        },
    )
    language: Optional[str] = Field(
        None,
        description="""The human language of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "language", "domain_of": ["DataObject"]}},
    )
    contact_point: Optional[str] = Field(
        None,
        description="""The contact point for the data object. This should be an email address.""",
        json_schema_extra={"linkml_meta": {"alias": "contact_point", "domain_of": ["DataObject"]}},
    )


class GraphComponent(DataObject):
    """
    A component of a knowledge graph.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/knowledge-graph-hub/kg_registry_schema"}
    )

    produced_by: Optional[List[str]] = Field(
        None,
        description="""The process that produced the component.""",
        json_schema_extra={
            "linkml_meta": {"alias": "produced_by", "domain_of": ["GraphComponent"]}
        },
    )
    part_of_subset: Optional[List[str]] = Field(
        None,
        description="""The subset or subsets that the component is part of.""",
        json_schema_extra={
            "linkml_meta": {"alias": "part_of_subset", "domain_of": ["GraphComponent"]}
        },
    )
    is_compressed: Optional[bool] = Field(
        None,
        description="""Whether the component is compressed. If true, the component should be decompressed before use.""",
        json_schema_extra={
            "linkml_meta": {"alias": "is_compressed", "domain_of": ["GraphComponent"]}
        },
    )
    compression: Optional[CompressionEnum] = Field(
        None,
        description="""The type of compression used with the component, e.g., tar.gz.""",
        json_schema_extra={
            "linkml_meta": {"alias": "compression", "domain_of": ["GraphComponent"]}
        },
    )
    id: str = Field(
        ...,
        description="""The identifier of the data object. This must be unique.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    name: str = Field(
        ...,
        description="""The name of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["DataObject"]}},
    )
    url: Optional[str] = Field(
        None,
        description="""The URL of the data object. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["DataObject"]}},
    )
    license: Optional[str] = Field(
        None,
        description="""The license of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "license", "domain_of": ["DataObject"]}},
    )
    version: Optional[str] = Field(
        None,
        description="""The version of the data object.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:version", "dcterms:hasVersion"],
            }
        },
    )
    language: Optional[str] = Field(
        None,
        description="""The human language of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "language", "domain_of": ["DataObject"]}},
    )
    contact_point: Optional[str] = Field(
        None,
        description="""The contact point for the data object. This should be an email address.""",
        json_schema_extra={"linkml_meta": {"alias": "contact_point", "domain_of": ["DataObject"]}},
    )


class GraphProductionProcess(DataObject):
    """
    A process for producing the individual components of a knowledge graph.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/knowledge-graph-hub/kg_registry_schema"}
    )

    id: str = Field(
        ...,
        description="""The identifier of the data object. This must be unique.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "id",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    name: str = Field(
        ...,
        description="""The name of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    description: Optional[str] = Field(
        None,
        description="""A description of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "description", "domain_of": ["DataObject"]}},
    )
    url: Optional[str] = Field(
        None,
        description="""The URL of the data object. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["DataObject"]}},
    )
    license: Optional[str] = Field(
        None,
        description="""The license of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "license", "domain_of": ["DataObject"]}},
    )
    version: Optional[str] = Field(
        None,
        description="""The version of the data object.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "version",
                "domain_of": ["DataObject"],
                "exact_mappings": ["schema:version", "dcterms:hasVersion"],
            }
        },
    )
    language: Optional[str] = Field(
        None,
        description="""The human language of the data object.""",
        json_schema_extra={"linkml_meta": {"alias": "language", "domain_of": ["DataObject"]}},
    )
    contact_point: Optional[str] = Field(
        None,
        description="""The contact point for the data object. This should be an email address.""",
        json_schema_extra={"linkml_meta": {"alias": "contact_point", "domain_of": ["DataObject"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
DataObject.model_rebuild()
KnowledgeGraph.model_rebuild()
KnowledgeGraphCollection.model_rebuild()
GraphComponent.model_rebuild()
GraphProductionProcess.model_rebuild()
