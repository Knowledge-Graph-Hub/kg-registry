from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.0.2"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'kgr',
     'default_range': 'string',
     'description': 'A schema for representing metadata about\n'
                    'knowlege graphs, their sources, and their contents.',
     'id': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema',
     'imports': ['linkml:types'],
     'license': 'GPL-3.0',
     'name': 'kg_registry_schema',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'kgr': {'prefix_prefix': 'kgr',
                          'prefix_reference': 'https://w3id.org/bridge2ai/data-sheets-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'see_also': ['https://kghub.org/kg-registry/'],
     'source_file': 'src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml',
     'title': 'kg_registry_schema',
     'types': {'category_type': {'description': 'A primitive type in which the '
                                                'value denotes a class within the '
                                                'model.',
                                 'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema',
                                 'name': 'category_type',
                                 'typeof': 'string'}}} )

class ActivityStatusEnum(str, Enum):
    """
    The status of a resource. Corresponds to those used by OBO Foundry.
    """
    # The resource is active and available.
    active = "active"
    # The resource is inactive. Its availability may vary.
    inactive = "inactive"
    # The resource is not actively maintained. Its availability may vary.
    orphaned = "orphaned"
    # The resource is no longer accessible. Only its metadata is available.
    unresponsive = "unresponsive"


class CompressionEnum(str, Enum):
    """
    The type of compression used with a product.
    """
    # The gzip compression algorithm. This file ends in .gz.
    gzip = "gzip"
    # The tar archive format. This file ends in .tar.
    tar = "tar"
    # A tar archive that is also gzip compressed. This file ends in .tar.gz.
    targz = "targz"
    # The rar archive format. This file ends in .rar.
    rar = "rar"
    # The zip archive format. This file ends in .zip.
    zip = "zip"
    # The 7z archive format. This file ends in .7z.
    number_7z = "7z"
    # Another compression format not defined here.
    other = "other"


class DomainEnum(str, Enum):
    """
    The domain that a resource is most relevant to.
    """
    # The upper-level domain, for general-purpose data representation and integration.
    upper = "upper"
    # The anatomy and development of organisms.
    anatomy_and_development = "anatomy and development"
    # The health and diseases of organisms.
    health = "health"
    # The phenotypes of organisms.
    phenotype = "phenotype"
    # Research investigations into specific topics.
    investigations = "investigations"
    # The environment and ecosystems.
    environment = "environment"
    # The chemical and biochemical sciences.
    chemistry_and_biochemistry = "chemistry and biochemistry"
    # The microbiological sciences.
    microbiology = "microbiology"
    # The agricultural sciences.
    agriculture = "agriculture"
    # The nutritional sciences, including diet and metabolomics.
    nutrition = "nutrition"
    # The biological sciences and systems.
    biological_systems = "biological systems"
    # The information technology sciences.
    information_technology = "information technology"
    # Specific organisms.
    organisms = "organisms"
    # Simulation and modeling of specific phenomena.
    simulation = "simulation"
    # Another domain not defined here.
    other = "other"


class GraphStandardEnum(str, Enum):
    """
    The standard or standards that a knowledge graph conforms to. These are not serializations, but rather the higher-level frameworks that the graph is built on.
    """
    # The KG-Hub standard, which is a general-purpose knowledge graph standard.
    kghub = "kghub"


class TagEnum(str, Enum):
    """
    General-purpose tags that can be associated with resources.
    """
    # A resource or product aggregated by the BioPragmatics project.
    biopragmatics = "biopragmatics"
    # A core KG-Hub resource.
    core = "core"
    # A resource used by the NCATS Translator program.
    translator = "translator"


class UsageEnum(str, Enum):
    """
    The type of usage of a resource.
    """
    # The resource is actually used in the specified way.
    actual = "actual"
    # The resource is used in the specified way for experimental purposes.
    experimental = "experimental"
    # The resource is not used in the specified way, but it could be.
    theoretical = "theoretical"
    # The resource is used in a way not defined here.
    other = "other"



class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/NamedThing","http://schema.org/Thing","kgr:NamedThing","schema:Thing"] = Field(default="NamedThing", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Registry(ConfiguredBaseModel):
    """
    A registry of knowledge graphs and their components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    registry_entries: Optional[List[Union[Resource,KnowledgeGraph,DataGraph,DataModel,Mapping,ProductionProcess]]] = Field(default=None, description="""A list of entries in the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'registry_entries', 'domain_of': ['Registry']} })


class Resource(NamedThing):
    """
    A top-level class for all resources in the knowledge graph registry. Each resource may have multiple products or representations, but they will all be considered part of a the same parent resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Resource","kgr:Resource"] = Field(default="Resource", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class KnowledgeGraph(Resource):
    """
    A knowledge graph resource. This is any heterogeneous collection of data that is represented as nodes (entities) and edges (relationships) between them. The nodes and edges may have attributes associated with them. This is not identical to the graph *product*, as a single KnowledgeGraph may have multiple products or representations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['kg', 'heterogeneous graph'],
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    creator: Optional[str] = Field(default=None, description="""The person or organization responsible for creating the knowledge graph.""", json_schema_extra = { "linkml_meta": {'alias': 'creator', 'domain_of': ['KnowledgeGraph']} })
    date_created: Optional[str] = Field(default=None, description="""The date the knowledge graph was created.""", json_schema_extra = { "linkml_meta": {'alias': 'date_created', 'domain_of': ['KnowledgeGraph']} })
    date_modified: Optional[str] = Field(default=None, description="""The date the knowledge graph was last modified.""", json_schema_extra = { "linkml_meta": {'alias': 'date_modified', 'domain_of': ['KnowledgeGraph']} })
    contributors: Optional[str] = Field(default=None, description="""Contributors to the knowledge graph.""", json_schema_extra = { "linkml_meta": {'alias': 'contributors', 'domain_of': ['KnowledgeGraph']} })
    components: Optional[List[str]] = Field(default=None, description="""The components of the knowledge graph.""", json_schema_extra = { "linkml_meta": {'alias': 'components', 'domain_of': ['KnowledgeGraph']} })
    conforms_to: Optional[List[GraphStandardEnum]] = Field(default=None, description="""The standard or standards that the knowledge graph conforms to. This is not the same as its serialization.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to', 'domain_of': ['KnowledgeGraph']} })
    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/KnowledgeGraph","kgr:KnowledgeGraph"] = Field(default="KnowledgeGraph", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class DataGraph(Resource):
    """
    A data source, rendered as graph nodes and edges. This is not identical to the graph *product*, as a single DataGraph may have multiple products or representations. May be a component of a knowledge graph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    produced_by: Optional[List[str]] = Field(default=None, description="""The process that produced the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['DataGraph']} })
    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/DataGraph","kgr:DataGraph"] = Field(default="DataGraph", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class DataModel(Resource):
    """
    A data model, such as an ontology or schema. May be a use in construction of a knowledge graph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/DataModel","kgr:DataModel"] = Field(default="DataModel", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Mapping(Resource):
    """
    A mapping between two or more data sources. May be a use in construction of a knowledge graph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Mapping","kgr:Mapping"] = Field(default="Mapping", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class ProductionProcess(Resource):
    """
    A process for producing a resource and/or its products.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Union[Product,GraphProduct,DataModelProduct,MappingProduct,ProcessProduct,GraphicalInterface,ProgrammingInterface]]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[str]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the resource. This is used to determine how to display the resource in the web interface. It should generally be 'resource_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['Resource']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/ProductionProcess","kgr:ProductionProcess"] = Field(default="ProductionProcess", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Product(NamedThing):
    """
    A top-level class for all products in the knowledge graph registry. This includes any specific files, APIs, or any other accessible representations of a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Product","kgr:Product"] = Field(default="Product", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class GraphProduct(Product):
    """
    A product that is a graph, represented as nodes and edges.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    edge_count: Optional[int] = Field(default=None, description="""The number of edges in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'edge_count', 'domain_of': ['GraphProduct']} })
    node_count: Optional[int] = Field(default=None, description="""The number of nodes in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_count', 'domain_of': ['GraphProduct']} })
    predicates: Optional[List[str]] = Field(default=None, description="""The predicate types in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'predicates', 'domain_of': ['GraphProduct']} })
    node_categories: Optional[List[str]] = Field(default=None, description="""The node categories in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_categories', 'domain_of': ['GraphProduct']} })
    is_kgx: Optional[bool] = Field(default=None, description="""Whether the graph is in KGX format.""", json_schema_extra = { "linkml_meta": {'alias': 'is_kgx', 'domain_of': ['GraphProduct']} })
    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/GraphProduct","kgr:GraphProduct"] = Field(default="GraphProduct", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class DataModelProduct(Product):
    """
    A product that is a data model, such as an ontology or schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/DataModelProduct","kgr:DataModelProduct"] = Field(default="DataModelProduct", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class MappingProduct(Product):
    """
    A product that is a mapping between two or more data sources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/MappingProduct","kgr:MappingProduct"] = Field(default="MappingProduct", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class ProcessProduct(Product):
    """
    A product that is a process or algorithm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/ProcessProduct","kgr:ProcessProduct"] = Field(default="ProcessProduct", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class GraphicalInterface(Product):
    """
    A product that is a graphical interface to a resource. Similar to the \"browsers\" field in OBO Foundry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/GraphicalInterface","kgr:GraphicalInterface"] = Field(default="GraphicalInterface", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class ProgrammingInterface(Product):
    """
    A product that is a programming interface (API) to a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[str] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[str]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/ProgrammingInterface","kgr:ProgrammingInterface"] = Field(default="ProgrammingInterface", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Contact(NamedThing):
    """
    A contact point for a resource or product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Contact","kgr:Contact"] = Field(default="Contact", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Individual(Contact):
    """
    An individual person.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The name of the individual.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    email: Optional[str] = Field(default=None, description="""The email address of the individual.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Individual', 'Organization']} })
    github: Optional[str] = Field(default=None, description="""The GitHub username of the individual. Do not include a prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'github', 'domain_of': ['Individual', 'Organization']} })
    orcid: Optional[str] = Field(default=None, description="""The ORCID of the individual. Do not include the \"https://orcid.org/\" prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['Individual']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Individual","kgr:Individual"] = Field(default="Individual", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })

    @field_validator('orcid')
    def pattern_orcid(cls, v):
        pattern=re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid orcid format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid orcid format: {v}")
        return v


class Organization(Contact):
    """
    An organization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The name of the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    email: Optional[str] = Field(default=None, description="""The email address of the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Individual', 'Organization']} })
    github: Optional[str] = Field(default=None, description="""The GitHub organization name. Do not include a prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'github', 'domain_of': ['Individual', 'Organization']} })
    url: Optional[str] = Field(default=None, description="""The URL of a site for the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Organization","kgr:Organization"] = Field(default="Organization", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class FundingSource(NamedThing):
    """
    A funding source for a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The organization providing the funding.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/FundingSource","kgr:FundingSource"] = Field(default="FundingSource", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class License(NamedThing):
    """
    A license for a resource or product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The name of the license.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    url: Optional[str] = Field(default=None, description="""The URL of the license.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    logo: Optional[str] = Field(default=None, description="""The URL of a logo for the license. This is added at metadata parsing time.""", json_schema_extra = { "linkml_meta": {'alias': 'logo', 'domain_of': ['License']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/License","kgr:License"] = Field(default="License", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Publication(NamedThing):
    """
    A publication associated with a resource. Its id should be a DOI (with prefix), but a URL is acceptable if a DOI is not available.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    preferred: Optional[bool] = Field(default=None, description="""Whether this is the preferred publication for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'preferred', 'domain_of': ['Publication']} })
    title: Optional[str] = Field(default=None, description="""The title of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    authors: Optional[List[str]] = Field(default=None, description="""The authors of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'authors', 'domain_of': ['Publication']} })
    journal: Optional[str] = Field(default=None, description="""The journal the publication was published in.""", json_schema_extra = { "linkml_meta": {'alias': 'journal', 'domain_of': ['Publication']} })
    year: Optional[str] = Field(default=None, description="""The year the publication was published.""", json_schema_extra = { "linkml_meta": {'alias': 'year', 'domain_of': ['Publication']} })
    doi: Optional[str] = Field(default=None, description="""The DOI of the publication. This should include the doi: prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'doi', 'domain_of': ['Publication']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Publication","kgr:Publication"] = Field(default="Publication", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


class Usage(NamedThing):
    """
    The usage of a resource. This may be actual, experimental, or theoretical.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The label of the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    description: Optional[str] = Field(default=None, description="""A description of the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    url: Optional[str] = Field(default=None, description="""A URL for a description or example of the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['Resource', 'Product', 'Organization', 'License', 'Usage']} })
    users: Optional[List[Union[Contact,Individual,Organization]]] = Field(default=None, description="""The user implementing or working with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'users', 'domain_of': ['Usage']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    type: Optional[UsageEnum] = Field(default=None, description="""The type of usage.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Literal["https://w3id.org/bridge2ai/data-sheets-schema/Usage","kgr:Usage"] = Field(default="Usage", description="""The category of the resource. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain': 'NamedThing',
         'domain_of': ['NamedThing'],
         'is_a': 'type'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Registry.model_rebuild()
Resource.model_rebuild()
KnowledgeGraph.model_rebuild()
DataGraph.model_rebuild()
DataModel.model_rebuild()
Mapping.model_rebuild()
ProductionProcess.model_rebuild()
Product.model_rebuild()
GraphProduct.model_rebuild()
DataModelProduct.model_rebuild()
MappingProduct.model_rebuild()
ProcessProduct.model_rebuild()
GraphicalInterface.model_rebuild()
ProgrammingInterface.model_rebuild()
Contact.model_rebuild()
Individual.model_rebuild()
Organization.model_rebuild()
FundingSource.model_rebuild()
License.model_rebuild()
Publication.model_rebuild()
Usage.model_rebuild()

