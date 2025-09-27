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
version = "0.0.4"


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
    root: dict[str, Any] = {}
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
                    'knowledge graphs, their sources, and their contents.',
     'id': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema',
     'imports': ['linkml:types', 'kg_registry_schema_formats'],
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

class DumpFormatEnum(str, Enum):
    """
    The format of a dump of a product, generally a graph, as a file. Note the product may also be compressed.
    """
    gpickle = "gpickle"
    """
    The gpickle format, or the output of pickling a NetworkX graph object. This file ends in .gpickle.
    """
    pickle = "pickle"
    """
    The pickle format, or the output of pickling a Python object. This file ends in .pkl or .pickle.
    """
    neo4j = "neo4j"
    """
    The Neo4j dump format, or the output of a Neo4j database dump. The file usually ends in .db, .dump, or .db.dump.
    """
    other = "other"
    """
    Another format not defined here.
    """


class FormatEnum(str, Enum):
    """
    The serialization/format of a product.
    """
    boolnet = "boolnet"
    """
    The Boolean Network (BoolNet) format, which is a format for representing Boolean networks. Used with the BoolNet package in R for modeling and analyzing biological networks.
    """
    chebi_sdf = "chebi_sdf"
    """
    A ChEBI-specific SDF format. Unlike the general SDF format, Each data item may be longer than 80 characters and has no maximum limit. Each line after the Data Header is a separate data item. For example, each new line in the synonyms is a separate synonym.
    """
    csv = "csv"
    """
    The Comma-Separated Values (CSV) format. It has rows of data separated by newlines, and columns separated by commas.
    """
    doc = "doc"
    """
    The Microsoft Word Document (DOC) format, a binary file format used by Microsoft Word. It is commonly used for word processing documents.
    """
    docx = "docx"
    """
    The Microsoft Word Open XML Document (DOCX) format, a modern file format for Microsoft Word documents. It is a zipped, XML-based file format that allows for more efficient storage and better compatibility with other software, as compared to the older DOC format.
    """
    dot = "dot"
    """
    The DOT format, a plain text graph description language used to define the structure of graphs. It is often used with Graphviz to visualize graphs.
    """
    fasta = "fasta"
    """
    The FASTA format, a text-based format for representing nucleotide or peptide sequences. It consists of a single header line followed by one or more lines of sequence data.
    """
    graphql = "graphql"
    """
    The GraphQL format, a query language for APIs and a runtime for executing those queries against your data. It allows clients to request exactly what they need and makes it easier to evolve APIs over time.
    """
    hdf5 = "hdf5"
    """
    The Hierarchical Data Format version 5 (HDF5) format, a file format and set of tools for managing complex data. It is designed to store and organize large amounts of data in a hierarchical structure, allowing for efficient access and manipulation.
    """
    http = "http"
    """
    The Hypertext Transfer Protocol (HTTP) format. This is a protocol for transferring data over the web. If a product is in this format, it is likely an web site or API.
    """
    java = "java"
    """
    The Java source code format, which is a text file containing Java code. It is used for writing scripts and programs in the Java language.
    """
    javascript = "javascript"
    """
    The JavaScript file format, which is a text file containing JavaScript code. It is used for writing scripts and programs in the JavaScript language.
    """
    json = "json"
    """
    The JavaScript Object Notation (JSON) format, a lightweight data-interchange format that's easy for humans to read and write and easy for machines to parse and generate.
    """
    jsonld = "jsonld"
    """
    The JSON for Linked Data (JSON-LD) format, which extends JSON with semantics for linked data by providing a method of encoding linked data using JSON. It enables data in JSON to be interpreted as RDF and allows JSON data to be interoperable at Web-scale.
    """
    kgx = "kgx"
    """
    The KGX standard, which is a graph exchange format for knowledge graphs. By default, this assumes KGX as TSV with separate node and edge files, usually named nodes.tsv and edges.tsv.
    """
    kgx_json = "kgx-json"
    """
    The KGX standard, which is a graph exchange format for knowledge graphs. This is the JSON format, with nodes and edges in a single file.
    """
    kgx_jsonl = "kgx-jsonl"
    """
    The KGX standard, which is a graph exchange format for knowledge graphs. This is the JSON Lines format, with separate node and edge files, usually named nodes.jsonl and edges.jsonl.
    """
    kgx_rdf = "kgx-rdf"
    """
    The KGX standard, which is a graph exchange format for knowledge graphs. This is the RDF Turtle (TTL) format, with nodes and edges in a single file.
    """
    mixed = "mixed"
    """
    A product that contains multiple formats or serializations. This is used when a product is not easily categorized into a single format, such as a codebase that includes multiple file types (e.g., Python scripts, JSON files, etc.).
    """
    mysql = "mysql"
    """
    The MySQL relational database management system. If a product is in this format, it is likely a MySQL database dump.
    """
    neo4j = "neo4j"
    """
    The Neo4j graph database management system. If a product is in this format, it is likely a Neo4j database dump. The file usually ends in .db, .dump, or .db.dump.
    """
    nquads = "nquads"
    """
    The N-Quads format, an extension of the N-Triples format that adds an optional fourth element to represent the graph name or context. This allows for representing multiple RDF graphs in a single document while maintaining their separation.
    """
    ntriples = "ntriples"
    """
    The N-Triples format, a line-based, plain text serialization format for RDF graphs. Each line contains a single RDF triple consisting of subject, predicate, and object, separated by whitespace and terminated by a period.
    """
    obo = "obo"
    """
    The Open Biomedical Ontologies (OBO) format, a file format for representing ontologies in the biomedical domain. It's designed to be simple and human-readable while supporting the necessary expressivity for representing biological concepts.
    """
    owl = "owl"
    """
    The Web Ontology Language (OWL) format, a semantic web language designed to represent rich and complex knowledge about things and their relationships. OWL builds on RDF and adds more vocabulary for describing properties and classes.
    """
    pdf = "pdf"
    """
    The Portable Document Format (PDF), a file format developed by Adobe for presenting documents in a manner independent of application software, hardware, and operating systems. PDF files can contain text, images, and vector graphics.
    """
    postgres = "postgres"
    """
    The PostgreSQL relational database management system. If a product is in this format, it is likely a PostgreSQL database dump.
    """
    protobuf = "protobuf"
    """
    The Protocol Buffers (Protobuf) format, a language-neutral, platform-neutral, extensible mechanism for serializing structured data. It's smaller, faster, and simpler than XML, designed for high-performance data interchange.
    """
    psi_mi_mitab = "psi_mi_mitab"
    """
    The PSI-MI MITAB format, which is a tab-delimited format for representing molecular interaction data. It is used to exchange information about molecular interactions between different databases.
    """
    psi_mi_xml = "psi_mi_xml"
    """
    The PSI-MI XML format, which is a standard for representing molecular interaction data in XML. It is used to exchange information about molecular interactions between different databases.
    """
    python = "python"
    """
    The Python script format, which is a text file containing Python code. It is used for writing scripts and programs in the Python language.
    """
    rdfxml = "rdfxml"
    """
    The RDF/XML format, an XML syntax for expressing RDF graphs as an XML document. It was the first standardized syntax for RDF and is widely used for interchange and archiving.
    """
    sbgnml = "sbgnml"
    """
    The Systems Biology Graphical Notation (SBGN) XML format, which is a standard for representing biological pathways and processes in a graphical form.
    """
    sbml = "sbml"
    """
    The Systems Biology Markup Language (SBML) XML format, which is a computer-readable format for representing models of biological processes.
    """
    sdf = "sdf"
    """
    The Structure Data File (SDF) format.
    """
    shacl = "shacl"
    """
    The Shapes Constraint Language (SHACL) format, a language for validating RDF graphs against a set of conditions. SHACL allows for defining constraints on RDF graphs, including the structure, values, and other features of data.
    """
    shex = "shex"
    """
    The Shape Expressions (ShEx) format, a language for validating and describing RDF data. ShEx provides a concise, human-readable syntax for expressing constraints on RDF graphs, including cardinality constraints and datatype restrictions.
    """
    sif = "sif"
    """
    The Simple Interaction Format (SIF), a simple text format for representing interactions between biological entities. It is often used to represent networks of interactions.
    """
    sqlite = "sqlite"
    """
    The SQLite relational database management system. If a product is in this format, it is likely a SQLite database dump.
    """
    sssom = "sssom"
    """
    The Simple Standard for Sharing Ontological Mappings (SSSOM) format, which a format for mapping between different ontologies and other identifier systems.
    """
    svg = "svg"
    """
    The Scalable Vector Graphics (SVG) format, an XML-based format for describing two-dimensional vector graphics.
    """
    trapi_jsonl = "trapi-jsonl"
    """
    The Translator Reasoner API (TRAPI) format, which is a JSON Lines format for TRAPI responses.
    """
    tsv = "tsv"
    """
    The Tab-Separated Values (TSV) format. It has rows of data separated by newlines, and columns separated by tabs.
    """
    ttl = "ttl"
    """
    The Turtle (TTL) format, a textual syntax for RDF that allows RDF graphs to be written in a compact and natural text form. Turtle provides prefixes and keywords that make RDF data more readable compared to XML or N-Triples formats.
    """
    txt = "txt"
    """
    The Plain Text (TXT) format, a simple text format for representing unformatted text data.
    """
    vcf = "vcf"
    """
    The Variant Call Format (VCF), a text file format for storing gene sequence variations. It is commonly used in bioinformatics to store gene sequence variations, such as single nucleotide polymorphisms (SNPs).
    """
    xgmml = "xgmml"
    """
    The eXtensible Graph Markup Language (XGMML) format, an XML-based format for representing graphs and networks.
    """
    xml = "xml"
    """
    The Extensible Markup Language (XML) format. It is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
    """
    yaml = "yaml"
    """
    The YAML Ain't Markup Language (YAML) format, a human-readable data serialization format. It is often used for configuration files and data exchange between languages with different data structures.
    """


class ActivityStatusEnum(str, Enum):
    """
    The status of a resource. Corresponds to those used by OBO Foundry.
    """
    active = "active"
    """
    The resource is active and available.
    """
    inactive = "inactive"
    """
    The resource is inactive. Its availability may vary.
    """
    orphaned = "orphaned"
    """
    The resource is not actively maintained. Its availability may vary.
    """
    unresponsive = "unresponsive"
    """
    The resource is no longer accessible. Only its metadata is available.
    """


class CompressionEnum(str, Enum):
    """
    The type of compression used with a product.
    """
    gpickle = "gpickle"
    """
    The gpickle format, or the output of pickling a NetworkX graph object. This file ends in .gpickle.
    """
    gzip = "gzip"
    """
    The gzip compression algorithm. This file ends in .gz.
    """
    pickle = "pickle"
    """
    The pickle format, or the output of pickling a Python object. This file ends in .pkl or .pickle.
    """
    tar = "tar"
    """
    The tar archive format. This file ends in .tar.
    """
    targz = "targz"
    """
    A tar archive that is also gzip compressed. This file ends in .tar.gz.
    """
    rar = "rar"
    """
    The rar archive format. This file ends in .rar.
    """
    zip = "zip"
    """
    The zip archive format. This file ends in .zip.
    """
    number_7z = "7z"
    """
    The 7z archive format. This file ends in .7z.
    """
    other = "other"
    """
    Another compression format not defined here.
    """


class ContactTypeEnum(str, Enum):
    """
    The type of contact detail.
    """
    email = "email"
    """
    An email address for the contact.
    """
    github = "github"
    """
    A GitHub username for the contact.
    """
    url = "url"
    """
    A URL for the contact. For an individual, this may be a profile on an official website. For an organization, this may be a link to the organization's site or a documentation landing page.
    """
    other = "other"
    """
    Another type of contact detail not defined here.
    """


class DomainEnum(str, Enum):
    """
    A domain that a resource is relevant to.
    """
    agriculture = "agriculture"
    """
    The agricultural sciences.
    """
    anatomy_and_development = "anatomy and development"
    """
    The anatomy and development of organisms.
    """
    biological_systems = "biological systems"
    """
    The biological sciences and systems.
    """
    biomedical = "biomedical"
    """
    The biomedical sciences, including the study of biological systems and their interactions.
    """
    chemistry_and_biochemistry = "chemistry and biochemistry"
    """
    The chemical and biochemical sciences.
    """
    clinical = "clinical"
    """
    The clinical sciences, including clinical trials and patient data.
    """
    digital_health = "digital health"
    """
    The use of digital technologies for healthcare, including telemedicine, wearable devices, health information technology, and personalized medicine.
    """
    drug_discovery = "drug discovery"
    """
    The process of identifying and developing new candidate medications, including target identification, validation, and compound screening.
    """
    environment = "environment"
    """
    The environment and ecosystems.
    """
    genomics = "genomics"
    """
    The study of genomes, including genome structure, evolution,  function, mapping, and editing.
    """
    health = "health"
    """
    The health and diseases of organisms.
    """
    immunology = "immunology"
    """
    The study of the immune system, including its structure and function, disorders, and therapeutic applications.
    """
    information_technology = "information technology"
    """
    The information technology sciences.
    """
    investigations = "investigations"
    """
    Research investigations into specific topics.
    """
    literature = "literature"
    """
    The literature and publications of a domain.
    """
    medical_imaging = "medical imaging"
    """
    Techniques and processes for creating visual representations of the interior of a body for clinical analysis and medical intervention.
    """
    microbiome = "microbiome"
    """
    The study of microbial communities, their genomes, and their influence on hosts and environments.
    """
    microbiology = "microbiology"
    """
    The microbiological sciences.
    """
    neuroscience = "neuroscience"
    """
    The scientific study of the nervous system, including  brain structure, function, and disorders.
    """
    nutrition = "nutrition"
    """
    The nutritional sciences, including diet and metabolomics.
    """
    organisms = "organisms"
    """
    Specific organisms.
    """
    other = "other"
    """
    Another domain not defined here.
    """
    pathways = "pathways"
    """
    Biological pathways, including metabolic, signaling, and regulatory networks that control cellular processes.
    """
    pharmacology = "pharmacology"
    """
    The study of how drugs interact with biological systems, including  drug discovery, development, and therapeutic uses.
    """
    phenotype = "phenotype"
    """
    The phenotypes of organisms.
    """
    precision_medicine = "precision medicine"
    """
    An approach to disease treatment and prevention that takes into account individual variability in genes, environment, and lifestyle.
    """
    proteomics = "proteomics"
    """
    The large-scale study of proteins, their structures,  functions, and interactions.
    """
    public_health = "public health"
    """
    The science of protecting and improving the health of people and their  communities, including epidemiology and population health.
    """
    simulation = "simulation"
    """
    Simulation and modeling of specific phenomena.
    """
    social_determinants = "social determinants"
    """
    The social, economic, and environmental factors that influence health outcomes and contribute to health disparities.
    """
    systems_biology = "systems biology"
    """
    The computational and mathematical analysis of complex biological systems and their interactions.
    """
    synthetic_biology = "synthetic biology"
    """
    The design and construction of new biological parts, devices, and systems, or the redesign of existing natural biological systems.
    """
    toxicology = "toxicology"
    """
    The study of the adverse effects of chemicals on living organisms.
    """
    translational = "translational"
    """
    The translational sciences, including the translation of research into practice.
    """
    upper = "upper"
    """
    The upper-level domain, for general-purpose data representation and integration.
    """
    food_science = "food science"
    """
    The study of food, including its production, processing, preservation, and consumption.
    """
    plant_science = "plant science"
    """
    The study of plants, including their biology, ecology, and interactions with the environment.
    """
    stub = "stub"
    """
    This is not a domain, but rather a category for resources that are not yet categorized and exist only as a placeholder.
    """


class StandardEnum(str, Enum):
    """
    The standard or standards that a product conforms to. These are not serializations, but rather the higher-level frameworks that the product is built on.
    """
    biolink = "biolink"
    """
    The Biolink Model, a standard for representing biological entities and relationships.
    """
    kghub = "kghub"
    """
    The KG-Hub standard, which is a general-purpose knowledge graph standard.
    """


class TagEnum(str, Enum):
    """
    General-purpose tags that can be associated with resources.
    """
    biopragmatics = "biopragmatics"
    """
    A resource or product aggregated by the BioPragmatics project.
    """
    core = "core"
    """
    A core KG-Hub resource.
    """
    translator = "translator"
    """
    A resource used by the NCATS Translator program.
    """


class UsageEnum(str, Enum):
    """
    The type of usage of a resource.
    """
    actual = "actual"
    """
    The resource is actually used in the specified way.
    """
    experimental = "experimental"
    """
    The resource is used in the specified way for experimental purposes.
    """
    theoretical = "theoretical"
    """
    The resource is not used in the specified way, but it could be.
    """
    other = "other"
    """
    The resource is used in a way not defined here.
    """


class CollectionEnum(str, Enum):
    """
    Specific collections for grouping KG-Registry entries.
    """
    aop = "aop"
    """
    This entity incorporates the Adverse Outcome Pathways (AOP) framework in some manner.
    """
    ber = "ber"
    """
    A resource or product relevant to the US Department of Energy Biological and Environmental Research (BER) program.
    """
    translator = "translator"
    """
    This entity is part of those developed and used by the NCATS Biomedical Translator program.
    """



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
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class Registry(ConfiguredBaseModel):
    """
    A registry of knowledge graphs and their components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    resources: Optional[list[Resource]] = Field(default=None, description="""A list of entries in the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'resources', 'domain_of': ['Registry']} })


class Contact(ConfiguredBaseModel):
    """
    A contact point for a resource or product, or a curator of a resource or product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    contact_details: Optional[list[ContactDetails]] = Field(default=None, description="""A field for contact details, including email, GitHub, and contact-specific URLs.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_details', 'domain_of': ['Contact']} })


class Resource(NamedThing):
    """
    A top-level class for all resources in the knowledge graph registry. Each resource may have multiple products or representations, but they will all be considered part of a the same parent resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema',
         'slot_usage': {'layout': {'name': 'layout', 'required': True}}})

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
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    products: Optional[list[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domains: list[DomainEnum] = Field(default=..., description="""The domain(s) that the resource is relevant to.""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['Resource']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[list[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[list[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: str = Field(default=..., description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    components: Optional[list[str]] = Field(default=None, description="""The components of the knowledge graph.""", json_schema_extra = { "linkml_meta": {'alias': 'components', 'domain_of': ['KnowledgeGraph']} })
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
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    products: Optional[list[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domains: list[DomainEnum] = Field(default=..., description="""The domain(s) that the resource is relevant to.""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['Resource']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[list[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[list[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: str = Field(default=..., description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    products: Optional[list[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domains: list[DomainEnum] = Field(default=..., description="""The domain(s) that the resource is relevant to.""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['Resource']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[list[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[list[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: str = Field(default=..., description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    products: Optional[list[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domains: list[DomainEnum] = Field(default=..., description="""The domain(s) that the resource is relevant to.""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['Resource']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[list[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[list[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: str = Field(default=..., description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact point(s) for the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the resource. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    products: Optional[list[Product]] = Field(default=None, description="""The products or representations of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['Resource']} })
    domains: list[DomainEnum] = Field(default=..., description="""The domain(s) that the resource is relevant to.""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['Resource']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    funding: Optional[list[str]] = Field(default=None, description="""The funding source(s) for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['Resource']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    usages: Optional[list[Usage]] = Field(default=None, description="""The usage(s) of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'usages', 'domain_of': ['Resource']} })
    fairsharing_id: Optional[str] = Field(default=None, description="""The FAIRsharing ID of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'fairsharing_id', 'domain_of': ['Resource']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the resource. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: str = Field(default=..., description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class Product(NamedThing):
    """
    A top-level class for all products in the knowledge graph registry. This includes any specific files, APIs, or any other accessible representations of a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class GraphProduct(Product):
    """
    A product that is a graph, represented as nodes and edges.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    edge_count: Optional[int] = Field(default=None, description="""The number of edges in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'edge_count', 'domain_of': ['GraphProduct']} })
    node_count: Optional[int] = Field(default=None, description="""The number of nodes in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_count', 'domain_of': ['GraphProduct']} })
    predicates: Optional[list[str]] = Field(default=None, description="""The predicate types in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'predicates', 'domain_of': ['GraphProduct']} })
    node_categories: Optional[list[str]] = Field(default=None, description="""The node categories in the graph.""", json_schema_extra = { "linkml_meta": {'alias': 'node_categories', 'domain_of': ['GraphProduct']} })
    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class DataModelProduct(Product):
    """
    A product that is a data model, such as an ontology or schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class MappingProduct(Product):
    """
    A product that is a mapping between two or more data sources. The sources should be identified in the original_source field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class ProcessProduct(Product):
    """
    A product that is a process or algorithm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class GraphicalInterface(Product):
    """
    A product that is a graphical interface to a resource. Similar to the \"browsers\" field in OBO Foundry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class DocumentationProduct(Product):
    """
    A product that is documentation for a resource. This may be a website, a stand-alone document, or a collection of documents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    name: str = Field(default=..., description="""The human-readable name of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Product']} })
    description: Optional[str] = Field(default=None, description="""A description of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Resource', 'Product', 'Usage']} })
    original_source: Optional[list[str]] = Field(default=None, description="""The original source(s) of the product, referred to  by the identifier of each resource. This may be the parent resource or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'original_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    secondary_source: Optional[list[str]] = Field(default=None, description="""The source(s) of the product, other than its original source, referred to by the identifier of each resource. This may be an Aggregator or another resource. This may also be a specific product.""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_source',
         'any_of': [{'range': 'Resource'}, {'range': 'Product'}],
         'domain_of': ['Product']} })
    product_url: Optional[str] = Field(default=None, description="""The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface.""", json_schema_extra = { "linkml_meta": {'alias': 'product_url', 'domain_of': ['Product']} })
    product_file_size: Optional[int] = Field(default=None, description="""The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible.""", json_schema_extra = { "linkml_meta": {'alias': 'product_file_size', 'domain_of': ['Product']} })
    produced_by: Optional[list[str]] = Field(default=None, description="""The process(es) that produced the product, referred to by the identifier of each process.""", json_schema_extra = { "linkml_meta": {'alias': 'produced_by', 'domain_of': ['Product']} })
    repository: Optional[str] = Field(default=None, description="""A main version control repository for the product.""", json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Resource', 'Product']} })
    license: Optional[License] = Field(default=None, description="""The license of the product. This may differ from that of the parent resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource', 'Product']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The type of compression used with the product. If this is not specified, it is assumed to be uncompressed.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Product']} })
    contacts: Optional[list[Contact]] = Field(default=None, description="""The contact points for the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'contacts', 'domain_of': ['Resource', 'Product']} })
    curators: Optional[list[Contact]] = Field(default=None, description="""The curator(s) of the product. May be an individual or organization.""", json_schema_extra = { "linkml_meta": {'alias': 'curators', 'domain_of': ['Resource', 'Product']} })
    tags: Optional[list[TagEnum]] = Field(default=None, description="""Tags associated with the product.""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['Resource', 'Product']} })
    infores_id: Optional[str] = Field(default=None, description="""The Infores ID of the product. Do not include the 'infores' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'infores_id', 'domain_of': ['Resource', 'Product']} })
    compatibility: Optional[list[StandardCompatibility]] = Field(default=None, description="""A list of standards that the product conforms to. This is not the same as its serialization/format.""", json_schema_extra = { "linkml_meta": {'alias': 'compatibility', 'domain_of': ['Product']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format or serialization of the product. Generally corresponds to the file extension.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Product']} })
    dump_format: Optional[DumpFormatEnum] = Field(default=None, description="""The format of a dump of the product as a file. Note the product may also be compressed.""", json_schema_extra = { "linkml_meta": {'alias': 'dump_format', 'domain_of': ['Product']} })
    versions: Optional[list[str]] = Field(default=None, description="""A list of names of versions of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'versions',
         'domain_of': ['Product'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion']} })
    latest_version: Optional[str] = Field(default=None, description="""The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like \"latest\".""", json_schema_extra = { "linkml_meta": {'alias': 'latest_version', 'domain_of': ['Product']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class ContactDetails(ConfiguredBaseModel):
    """
    A field for details about how to contact a person or organization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    contact_type: ContactTypeEnum = Field(default=..., description="""The type of contact detail.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_type', 'domain_of': ['ContactDetails']} })
    contact_type_name: Optional[str] = Field(default=None, description="""The name of the contact detail, if the contact_type is \"other\". For example, if the contact value is a username at the Gumball Project's GitLab, this may be \"Gumball Project GitLab\".""", json_schema_extra = { "linkml_meta": {'alias': 'contact_type_name', 'domain_of': ['ContactDetails']} })
    contact_type_url: Optional[str] = Field(default=None, description="""The URL of the contact detail, if the contact_type is \"other\". For example, if the contact value is a username at the Gumball Project's GitLab, this may be \"https://gitlab.gumballproject.org/\".""", json_schema_extra = { "linkml_meta": {'alias': 'contact_type_url', 'domain_of': ['ContactDetails']} })
    value: str = Field(default=..., description="""The value of the contact detail. For example, an email address or URL. Do not include a prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['ContactDetails']} })


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
    orcid: Optional[str] = Field(default=None, description="""The ORCID of the individual. Do not include the \"https://orcid.org/\" prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['Individual']} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    contact_details: Optional[list[ContactDetails]] = Field(default=None, description="""A field for contact details, including email, GitHub, and contact-specific URLs.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_details', 'domain_of': ['Contact']} })

    @field_validator('orcid')
    def pattern_orcid(cls, v):
        pattern=re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid orcid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid orcid format: {v}"
            raise ValueError(err_msg)
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
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    contact_details: Optional[list[ContactDetails]] = Field(default=None, description="""A field for contact details, including email, GitHub, and contact-specific URLs.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_details', 'domain_of': ['Contact']} })


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
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


class Publication(NamedThing):
    """
    A publication associated with a resource. Its id should be in CURIE format, so it may be a DOI (with prefix) or a URL.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/knowledge-graph-hub/kg_registry_schema'})

    preferred: Optional[bool] = Field(default=None, description="""Whether this is the preferred publication for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'preferred', 'domain_of': ['Publication']} })
    title: Optional[str] = Field(default=None, description="""The title of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    authors: Optional[list[str]] = Field(default=None, description="""The authors of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'authors', 'domain_of': ['Publication']} })
    journal: Optional[str] = Field(default=None, description="""The journal the publication was published in.""", json_schema_extra = { "linkml_meta": {'alias': 'journal', 'domain_of': ['Publication']} })
    year: Optional[str] = Field(default=None, description="""The year the publication was published.""", json_schema_extra = { "linkml_meta": {'alias': 'year', 'domain_of': ['Publication']} })
    doi: Optional[str] = Field(default=None, description="""The DOI of the publication. This does not need to include a prefix of any kind, as it will be formatted as a URL.""", json_schema_extra = { "linkml_meta": {'alias': 'doi', 'domain_of': ['Publication']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
    url: Optional[str] = Field(default=None, description="""A URL for a description or example of the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Usage']} })
    users: Optional[list[Contact]] = Field(default=None, description="""The user implementing or working with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'users', 'domain_of': ['Usage']} })
    publications: Optional[list[Publication]] = Field(default=None, description="""Publications associated with the usage.""", json_schema_extra = { "linkml_meta": {'alias': 'publications', 'domain_of': ['Resource', 'Usage']} })
    type: Optional[UsageEnum] = Field(default=None, description="""The type of usage.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Usage']} })
    id: str = Field(default=..., description="""The identifier of an entity. This is used to identify it within the registry.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:identifier'} })
    category: Optional[str] = Field(default=None, description="""The category of the entity. This should be identical to its class name.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'domain': 'NamedThing',
         'domain_of': ['NamedThing', 'Contact'],
         'is_a': 'type'} })
    warnings: Optional[list[str]] = Field(default=None, description="""A list of warnings about an item to be displayed in the interface. These should primarily warn users about unavailable resources, broken links, and other obstacles to using a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['NamedThing']} })
    collection: Optional[list[CollectionEnum]] = Field(default=None, description="""A collection of entries in the registry. This is used to group related entries together. This is multivalued to allow for multiple collections.""", json_schema_extra = { "linkml_meta": {'alias': 'collection', 'domain_of': ['NamedThing']} })
    layout: Optional[str] = Field(default=None, description="""The layout of the entity. This is used to determine how to display the entity in the web interface. For resources, this is generally 'resource_detail'. For products, this is generally 'product_detail'. If a value for this slot is not specified, pages won't contain anything from their header metadata.""", json_schema_extra = { "linkml_meta": {'alias': 'layout', 'domain_of': ['NamedThing']} })
    creation_date: Optional[datetime ] = Field(default=None, description="""The date the entry was created. This is used to determine the age of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['NamedThing']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.""", json_schema_extra = { "linkml_meta": {'alias': 'last_modified_date', 'domain_of': ['NamedThing']} })


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
DocumentationProduct.model_rebuild()
ContactDetails.model_rebuild()
Individual.model_rebuild()
Organization.model_rebuild()
FundingSource.model_rebuild()
License.model_rebuild()
Publication.model_rebuild()
Usage.model_rebuild()
StandardCompatibility.model_rebuild()

