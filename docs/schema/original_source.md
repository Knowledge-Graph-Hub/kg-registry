---
layout: schema_doc
mermaid: true
---



# Slot: original_source


_The original source(s) of the product, with the provenance relation describing how the product relates to each source. This may be the parent resource or another resource. This may also be a specific product._





URI: [kgr:original_source](https://w3id.org/bridge2ai/data-sheets-schema/original_source)
Alias: original_source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentationProduct](DocumentationProduct.html) | A product that is documentation for a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that provides the rules of a data model |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [OntologyProduct](OntologyProduct.html) | A product that is an ontology, a formal representation of a set of concepts w... |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |






## Properties

* Range: [SourceAssociation](SourceAssociation.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:original_source |
| native | kgr:original_source |




## LinkML Source

<details>
```yaml
name: original_source
description: The original source(s) of the product, with the provenance relation describing
  how the product relates to each source. This may be the parent resource or another
  resource. This may also be a specific product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: original_source
owner: Product
domain_of:
- Product
range: SourceAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
