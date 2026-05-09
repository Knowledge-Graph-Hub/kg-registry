---
layout: schema_doc
mermaid: true
---

# kg_registry_schema

A schema for representing metadata about
knowledge graphs, their sources, and their contents.

URI: https://w3id.org/knowledge-graph-hub/kg_registry_schema

Name: kg_registry_schema



## Classes

| Class | Description |
| --- | --- |
| [Contact](Contact.html) | A contact point for a resource or product, or a curator of a resource or prod... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Individual](Individual.html) | An individual person |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.html) | An organization |
| [ContactDetails](ContactDetails.html) | A field for details about how to contact a person or organization |
| [NamedThing](NamedThing.html) | A generic grouping for any identifiable entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FundingSource](FundingSource.html) | A funding source for a resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](License.html) | A license for a resource or product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Product](Product.html) | A top-level class for all products in the knowledge graph registry |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataModelProduct](DataModelProduct.html) | A product that provides the rules of a data model |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DocumentationProduct](DocumentationProduct.html) | A product that is documentation for a resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OntologyProduct](OntologyProduct.html) | A product that is an ontology, a formal representation of a set of concepts w... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.html) | A publication associated with a resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aggregator](Aggregator.html) | An aggregator of data sources |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataModel](DataModel.html) | A data model is a formal representation of concepts and relationships within ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataSource](DataSource.html) | A data source |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ontology](Ontology.html) | An ontology is a formal representation of a set of concepts within a domain a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Usage](Usage.html) | The usage of a resource |
| [Registry](Registry.html) | A registry of knowledge graphs and their components |
| [SourceAssociation](SourceAssociation.html) | A typed provenance association from a product to another resource or product ... |
| [StandardCompatibility](StandardCompatibility.html) | Details about the compatibility of a product with a particular standard, incl... |



## Slots

| Slot | Description |
| --- | --- |
| [activity_status](activity_status.html) | The status of the resource |
| [authors](authors.html) | The authors of the publication |
| [category](category.html) | The category of the entity |
| [collection](collection.html) | A collection of entries in the registry |
| [compatibility](compatibility.html) | A list of standards that the product conforms to |
| [components](components.html) | The components of the knowledge graph |
| [compression](compression.html) | The type of compression used with the product |
| [connection_url](connection_url.html) | A URL specific to the product |
| [contact_details](contact_details.html) | A field for contact details, including email, GitHub, and contact-specific UR... |
| [contact_type](contact_type.html) | The type of contact detail |
| [contact_type_name](contact_type_name.html) | The name of the contact detail, if the contact_type is "other" |
| [contact_type_url](contact_type_url.html) | The URL of the contact detail, if the contact_type is "other" |
| [contacts](contacts.html) | The contact point(s) for the resource |
| [contributors](contributors.html) | Contributors to the knowledge graph |
| [creation_date](creation_date.html) | The date the entry was created |
| [creator](creator.html) | The person or organization responsible for creating the knowledge graph |
| [curators](curators.html) | The curator(s) of the resource |
| [date_created](date_created.html) | The date the knowledge graph was created |
| [date_modified](date_modified.html) | The date the knowledge graph was last modified |
| [description](description.html) | A description of the resource |
| [doi](doi.html) | The DOI of the publication |
| [domains](domains.html) | The domain(s) that the resource is relevant to |
| [dump_format](dump_format.html) | The format of a dump of the product as a file |
| [edge_count](edge_count.html) | The number of edges in the graph |
| [fairsharing_id](fairsharing_id.html) | The FAIRsharing ID of the resource |
| [format](format.html) | The format or serialization of the product |
| [funding](funding.html) | The funding source(s) for the resource |
| [github_url](github_url.html) | The GitHub URL of the organization |
| [homepage_url](homepage_url.html) | The primary URL of the resource |
| [id](id.html) | The identifier of an entity |
| [infores_id](infores_id.html) | The Infores ID of the resource |
| [is_neo4j](is_neo4j.html) | Whether the API is for a Neo4j database |
| [is_public](is_public.html) | Whether the API is publicly accessible, or requires only publicly provided cr... |
| [journal](journal.html) | The journal the publication was published in |
| [label](label.html) | The name of the individual |
| [language](language.html) | The human language of the resource |
| [last_modified_date](last_modified_date.html) | The date the entry was last modified |
| [latest_version](latest_version.html) | The latest version of the product, or the most recent version curated in the ... |
| [layout](layout.html) | The layout of the entity |
| [license](license_slot.html) | The license of the resource |
| [logo](logo.html) | The URL of a logo for the license |
| [name](name.html) | The human-readable name of the resource |
| [node_categories](node_categories.html) | The node categories in the graph |
| [node_count](node_count.html) | The number of nodes in the graph |
| [orcid](orcid.html) | The ORCID of the individual |
| [original_source](original_source.html) | The original source(s) of the product, with the provenance relation describin... |
| [predicates](predicates.html) | The predicate types in the graph |
| [preferred](preferred.html) | Whether this is the preferred publication for the resource |
| [produced_by](produced_by.html) | The process(es) that produced the product, referred to by the identifier of e... |
| [product_file_size](product_file_size.html) | The size of the product file, in bytes |
| [product_url](product_url.html) | The URL of the product |
| [products](products.html) | The products or representations of the resource |
| [publications](publications.html) | Publications associated with the resource |
| [relation_type](relation_type.html) | The PROV-O relation type that describes how the product is related to the sou... |
| [repository](repository.html) | A main version control repository for the resource |
| [resources](resources.html) | A list of entries in the registry |
| [secondary_source](secondary_source.html) | The source(s) of the product, other than its original source, with the proven... |
| [short_id](short_id.html) | A short identifier for the organization |
| [source](source.html) | The identifier of the resource or product that is related to the product thro... |
| [standard](standard.html) | The name of the standard that the product is compatible with |
| [synonyms](synonyms.html) | A list of synonyms for the resource |
| [tags](tags.html) | Tags associated with the resource |
| [taxon](taxon.html) | The taxon or taxa that the resource is relevant to |
| [title](title.html) | The title of the publication |
| [type](type.html) | The type of usage |
| [url](url.html) | A URL for a description or example of the usage |
| [usages](usages.html) | The usage(s) of the resource |
| [users](users.html) | The user implementing or working with the resource |
| [value](value.html) | The value of the contact detail |
| [version](version.html) | The version of the resource |
| [versions](versions.html) | A list of names of versions of the product |
| [warnings](warnings.html) | A list of warnings about an item to be displayed in the interface |
| [year](year.html) | The year the publication was published |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ActivityStatusEnum](ActivityStatusEnum.html) | The status of a resource |
| [CollectionEnum](CollectionEnum.html) | Specific collections for grouping KG-Registry entries |
| [CompressionEnum](CompressionEnum.html) | The type of compression used with a product |
| [ContactTypeEnum](ContactTypeEnum.html) | The type of contact detail |
| [DomainEnum](DomainEnum.html) | A domain that a resource is relevant to |
| [DumpFormatEnum](DumpFormatEnum.html) | The format of a dump of a product, generally a graph, as a file |
| [FormatEnum](FormatEnum.html) | The serialization/format of a product |
| [ProvenanceRelationEnum](ProvenanceRelationEnum.html) | PROV-O relation types used to describe how a product is related to a resource... |
| [StandardEnum](StandardEnum.html) | The standard or standards that a product conforms to |
| [TagEnum](TagEnum.html) | General-purpose tags that can be associated with resources |
| [UsageEnum](UsageEnum.html) | The type of usage of a resource |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.html) | A binary (true or false) value |
| [CategoryType](CategoryType.html) | A primitive type in which the value denotes a class within the model |
| [Curie](Curie.html) | a compact URI |
| [Date](Date.html) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.html) | Either a date or a datetime |
| [Datetime](Datetime.html) | The combination of a date and time |
| [Decimal](Decimal.html) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.html) | A real number that conforms to the xsd:double specification |
| [Float](Float.html) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.html) | An integer |
| [Jsonpath](Jsonpath.html) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.html) | A string encoding a JSON Pointer |
| [Ncname](Ncname.html) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.html) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.html) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.html) | A string encoding a SPARQL Property Path |
| [String](String.html) | A character string |
| [Time](Time.html) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.html) | a complete URI |
| [Uriorcurie](Uriorcurie.html) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
