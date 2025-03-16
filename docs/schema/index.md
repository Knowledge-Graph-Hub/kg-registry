---
layout: schema_doc
mermaid: true
---

# kg_registry_schema

A schema for representing metadata about
knowlege graphs, their sources, and their contents.

URI: https://w3id.org/knowledge-graph-hub/kg_registry_schema

Name: kg_registry_schema



## Classes

| Class | Description |
| --- | --- |
| [Contact](Contact.html) | A contact point for a resource or product. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Individual](Individual.html) | An individual person. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.html) | An organization. |
| [NamedThing](NamedThing.html) | A generic grouping for any identifiable entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FundingSource](FundingSource.html) | A funding source for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](License.html) | A license for a resource or product. The id field should be a URL to the license text, e.g., https://creativecommons.org/licenses/by/4.0/ |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Product](Product.html) | A top-level class for all products in the knowledge graph registry. This includes any specific files, APIs, or any other accessible representations of a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource. Similar to the "browsers" field in OBO Foundry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources. The sources should be identified in the original_source field. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.html) | A publication associated with a resource. Its id should be a DOI (with prefix), but a URL is acceptable if a DOI is not available. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry. Each resource may have multiple products or representations, but they will all be considered part of a the same parent resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aggregator](Aggregator.html) | An aggregator of data sources. Note that this may be a data source itself, and its products may undergo changes in the process of their inclusion in the aggregator. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataModel](DataModel.html) | A data model, such as an ontology or schema. May be used in construction of a knowledge graph. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataSource](DataSource.html) | A data source. One data source may have multiple products. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource. This is any heterogeneous collection of data that is represented as nodes (entities) and edges (relationships) between them. The nodes and edges may have attributes associated with them. This is not identical to the graph *product*, as a single KnowledgeGraph may have multiple products or representations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Usage](Usage.html) | The usage of a resource. This may be actual, experimental, or theoretical. |
| [Registry](Registry.html) | A registry of knowledge graphs and their components. |
| [StandardCompatibility](StandardCompatibility.html) | Details about the compatibility of a product with a particular standard, including data models such as Biolink Model and graph standards such as KGX. |



## Slots

| Slot | Description |
| --- | --- |
| [activity_status](activity_status.html) | The status of the resource |
| [authors](authors.html) | The authors of the publication |
| [category](category.html) | The category of the entity |
| [compatibility](compatibility.html) | A list of standards that the product conforms to |
| [components](components.html) | The components of the knowledge graph |
| [compression](compression.html) | The type of compression used with the product |
| [connection_url](connection_url.html) | A URL specific to the product |
| [contacts](contacts.html) | The contact point(s) for the resource |
| [contributors](contributors.html) | Contributors to the knowledge graph |
| [creator](creator.html) | The person or organization responsible for creating the knowledge graph |
| [date_created](date_created.html) | The date the knowledge graph was created |
| [date_modified](date_modified.html) | The date the knowledge graph was last modified |
| [description](description.html) | A description of the resource |
| [doi](doi.html) | The DOI of the publication |
| [domain](domain.html) | The domain that the resource is relevant to |
| [dump_format](dump_format.html) | The format of a dump of the product as a file |
| [edge_count](edge_count.html) | The number of edges in the graph |
| [email](email.html) | The email address of the individual |
| [fairsharing_id](fairsharing_id.html) | The FAIRsharing ID of the resource |
| [format](format.html) | The format or serialization of the product |
| [funding](funding.html) | The funding source(s) for the resource |
| [github](github.html) | The GitHub username of the individual |
| [homepage_url](homepage_url.html) | The primary URL of the resource |
| [id](id.html) | The identifier of an entity |
| [infores_id](infores_id.html) | The Infores ID of the resource |
| [is_neo4j](is_neo4j.html) | Whether the API is for a Neo4j database |
| [is_public](is_public.html) | Whether the API is publicly accessible, or requires only publicly provided cr... |
| [journal](journal.html) | The journal the publication was published in |
| [label](label.html) | The name of the individual |
| [language](language.html) | The human language of the resource |
| [layout](layout.html) | The layout of the entity |
| [license](license.html) | The license of the resource |
| [logo](logo.html) | The URL of a logo for the license |
| [name](name.html) | The human-readable name of the resource |
| [node_categories](node_categories.html) | The node categories in the graph |
| [node_count](node_count.html) | The number of nodes in the graph |
| [orcid](orcid.html) | The ORCID of the individual |
| [original_source](original_source.html) | The original source(s) of the product, referred to  by the identifier of each... |
| [predicates](predicates.html) | The predicate types in the graph |
| [preferred](preferred.html) | Whether this is the preferred publication for the resource |
| [produced_by](produced_by.html) | The process(es) that produced the product, referred to by the identifier of e... |
| [product_url](product_url.html) | The URL of the product |
| [products](products.html) | The products or representations of the resource |
| [publications](publications.html) | Publications associated with the resource |
| [repository](repository.html) | A main version control repository for the resource |
| [resources](resources.html) | A list of entries in the registry |
| [secondary_source](secondary_source.html) | The source(s) of the product, other than its original source, referred to by ... |
| [standard](standard.html) | The name of the standard that the product is compatible with |
| [tags](tags.html) | Tags associated with the resource |
| [title](title.html) | The title of the publication |
| [type](type.html) | The type of usage |
| [url](url.html) | The URL of a site for the organization |
| [usages](usages.html) | The usage(s) of the resource |
| [users](users.html) | The user implementing or working with the resource |
| [version](version.html) | The version of the resource |
| [warnings](warnings.html) | A list of warnings about an item to be displayed in the interface |
| [year](year.html) | The year the publication was published |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ActivityStatusEnum](ActivityStatusEnum.html) | The status of a resource |
| [CompressionEnum](CompressionEnum.html) | The type of compression used with a product |
| [DomainEnum](DomainEnum.html) | The domain that a resource is most relevant to |
| [DumpFormatEnum](DumpFormatEnum.html) | The format of a dump of a product, generally a graph, as a file |
| [FormatEnum](FormatEnum.html) | The serialization/format of a product |
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
