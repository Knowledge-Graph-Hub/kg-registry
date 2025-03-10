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
    # The gpickle format, or the output of pickling a NetworkX graph object. This file ends in .gpickle.
    gpickle = "gpickle"
    # The gzip compression algorithm. This file ends in .gz.
    gzip = "gzip"
    # The pickle format, or the output of pickling a Python object. This file ends in .pkl or .pickle.
    pickle = "pickle"
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


class DumpFormatEnum(str, Enum):
    """
    The format of a dump of a product, generally a graph, as a file. Note the product may also be compressed.
    """
    # The gpickle format, or the output of pickling a NetworkX graph object. This file ends in .gpickle.
    gpickle = "gpickle"
    # The pickle format, or the output of pickling a Python object. This file ends in .pkl or .pickle.
    pickle = "pickle"
    # Another format not defined here.
    other = "other"


class FormatEnum(str, Enum):
    """
    The serialization/format of a product.
    """
    # The JSON format.
    json = "json"
    # The JSON-LD format.
    jsonld = "jsonld"
    # The RDF/XML format.
    rdfxml = "rdfxml"
    # The Turtle format.
    ttl = "ttl"
    # The N-Triples format.
    ntriples = "ntriples"
    # The N-Quads format.
    nquads = "nquads"
    # The OWL format.
    owl = "owl"
    # The OBO format.
    obo = "obo"
    # The GraphQL format.
    graphql = "graphql"
    # The Protobuf format.
    protobuf = "protobuf"
    # The SHACL format.
    shacl = "shacl"
    # The ShEx format.
    shex = "shex"
    # The KGX standard, which is a graph exchange format for knowledge graphs. By default, this assumes KGX as TSV with separate node and edge files, usually named nodes.tsv and edges.tsv.
    kgx = "kgx"
    # The KGX standard, which is a graph exchange format for knowledge graphs. This is the JSON format, with nodes and edges in a single file.
    kgx_json = "kgx-json"
    # The KGX standard, which is a graph exchange format for knowledge graphs. This is the JSON Lines format, with separate node and edge files, usually named nodes.jsonl and edges.jsonl.
    kgx_jsonl = "kgx-jsonl"
    # The KGX standard, which is a graph exchange format for knowledge graphs. This is the RDF Turtle (TTL) format, with nodes and edges in a single file.
    kgx_rdf = "kgx-rdf"


class StandardEnum(str, Enum):
    """
    The standard or standards that a product conforms to. These are not serializations, but rather the higher-level frameworks that the product is built on.
    """
    # The Biolink Model, a standard for representing biological entities and relationships.
    biolink = "biolink"
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
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class Registry(ConfiguredBaseModel):
    """
    A registry of knowledge graphs and their components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    resources: Optional[List[Resource]] = Field(default=None, description="""A list of entries in the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'resources', 'domain_of': ['Registry']} })


class Contact(ConfiguredBaseModel):
    """
    A contact point for a resource or product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })


class Resource(NamedThing):
    """
    A top-level class for all resources in the knowledge graph registry. Each resource may have multiple products or representations, but they will all be considered part of a the same parent resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    homepage_url: Optional[str] = Field(default=None, description="""The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage_url', 'domain_of': ['Resource']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource', 'StandardCompatibility'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


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
    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    homepage_url: Optional[str] = Field(default=None, description="""The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage_url', 'domain_of': ['Resource']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource', 'StandardCompatibility'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class DataSource(Resource):
    """
    A data source. One data source may have multiple products.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    homepage_url: Optional[str] = Field(default=None, description="""The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage_url', 'domain_of': ['Resource']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource', 'StandardCompatibility'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class DataModel(Resource):
    """
    A data model, such as an ontology or schema. May be used in construction of a knowledge graph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    homepage_url: Optional[str] = Field(default=None, description="""The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage_url', 'domain_of': ['Resource']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource', 'StandardCompatibility'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class Aggregator(Resource):
    """
    An aggregator of data sources. Note that this may be a data source itself, and its products may undergo changes in the process of their inclusion in the aggregator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    activity_status: Optional[ActivityStatusEnum] = Field(default=None, description="""The status of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_status', 'domain_of': ['Resource']} })
    name: str = Field(default=..., description="""The human-readable name of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    homepage_url: Optional[str] = Field(default=None, description="""The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage_url', 'domain_of': ['Resource']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the resource. Specific products may have their own repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the resource. Individual products may have their own licenses.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    version: Optional[str] = Field(default=None, description="""The version of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Resource', 'StandardCompatibility'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    language: Optional[str] = Field(default=None, description="""The human language of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Resource']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    products: Optional[List[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domain: DomainEnum = Field(default=..., description="""The domain that the resource is relevant to. This is not multivalued.""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['Resource']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[List[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[List[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class Product(NamedThing):
    """
    A top-level class for all products in the knowledge graph registry. This includes any specific files, APIs, or any other accessible representations of a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class GraphProduct(Product):
    """
    A product that is a graph, represented as nodes and edges.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    edge_count: Optional[int] = Field(default=None, description="""The number of edges in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'edge_count', 'domain_of': ['GraphProduct']} })
    node_count: Optional[int] = Field(default=None, description="""The number of nodes in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_count', 'domain_of': ['GraphProduct']} })
    predicates: Optional[List[str]] = Field(default=None, description="""The predicate types in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'predicates', 'domain_of': ['GraphProduct']} })
    node_categories: Optional[List[str]] = Field(default=None, description="""The node categories in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_categories', 'domain_of': ['GraphProduct']} })
    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class DataModelProduct(Product):
    """
    A product that is a data model, such as an ontology or schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class MappingProduct(Product):
    """
    A product that is a mapping between two or more data sources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class ProcessProduct(Product):
    """
    A product that is a process or algorithm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class GraphicalInterface(Product):
    """
    A product that is a graphical interface to a resource. Similar to the \"browsers\" field in OBO Foundry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class ProgrammingInterface(Product):
    """
    A product that is a programming interface (API) to a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    is_public: Optional[bool] = Field(default=None, description="""Whether the API is publicly accessible, or requires only publicly provided credentials.""", json_schema_extra = { "linkml_meta": {'alias': 'is_public', 'domain_of': ['ProgrammingInterface']} })
    is_neo4j: Optional[bool] = Field(default=None, description="""Whether the API is for a Neo4j database.""", json_schema_extra = { "linkml_meta": {'alias': 'is_neo4j', 'domain_of': ['ProgrammingInterface']} })
    connection_url: Optional[str] = Field(default=None, description="""A URL specific to the product. For example, a URL to a specific Neo4j database. Do not include a prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'connection_url', 'domain_of': ['ProgrammingInterface']} })
    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[str] = Field(default=None, description="""The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source', 'domain_of': ['Product']} })
    derived_from: Optional[str] = Field(default=None, description="""The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Product']} })
    url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[List[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[List[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[List[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


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
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
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
    url: Optional[str] = Field(default=None, description="""The URL of a site for the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })


class FundingSource(NamedThing):
    """
    A funding source for a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[Organization] = Field(default=None, description="""The organization providing the funding.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class License(NamedThing):
    """
    A license for a resource or product. The id field should be a URL to the license text, e.g., https://creativecommons.org/licenses/by/4.0/
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    label: Optional[str] = Field(default=None, description="""The name of the license.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Individual',
                       'Organization',
                       'FundingSource',
                       'License',
                       'Usage']} })
    logo: Optional[str] = Field(default=None, description="""The URL of a logo for the license. This is added at metadata parsing time.""", json_schema_extra = { "linkml_meta": {'alias': 'logo', 'domain_of': ['License']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


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
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


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
    url: Optional[str] = Field(default=None, description="""A URL for a description or example of the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Product', 'Organization', 'Usage']} })
    users: Optional[List[Contact]] = Field(default=None, description="""The user implementing or working with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'users', 'domain_of': ['Usage']} })
    publications: Optional[List[Publication]] = Field(default=None, description="""Publications associated with the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    type: Optional[UsageEnum] = Field(default=None, description="""The type of usage.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[List[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })


class StandardCompatibility(ConfiguredBaseModel):
    """
    Details about the compatibility of a product with a particular standard, including data models such as Biolink Model and graph standards such as KGX.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    standard: Optional[StandardEnum] = Field(default=None, description="""The name of the standard that the product is compatible with.""", json_schema_extra = { "linkml_meta": {'alias': 'standard', 'domain_of': ['StandardCompatibility']} })
    version: Optional[str] = Field(default=None, description="""If applicable, the most recent version of the standard that the product is known to be compatible with, e.g., 4.2.5""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Resource', 'StandardCompatibility']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Registry.model_rebuild()
Contact.model_rebuild()
Resource.model_rebuild()
KnowledgeGraph.model_rebuild()
DataSource.model_rebuild()
DataModel.model_rebuild()
Aggregator.model_rebuild()
Product.model_rebuild()
GraphProduct.model_rebuild()
DataModelProduct.model_rebuild()
MappingProduct.model_rebuild()
ProcessProduct.model_rebuild()
GraphicalInterface.model_rebuild()
ProgrammingInterface.model_rebuild()
Individual.model_rebuild()
Organization.model_rebuild()
FundingSource.model_rebuild()
License.model_rebuild()
Publication.model_rebuild()
Usage.model_rebuild()
StandardCompatibility.model_rebuild()

