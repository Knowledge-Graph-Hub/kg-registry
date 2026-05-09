---
layout: schema_doc
mermaid: true
---



# Slot: versions


_A list of names of versions of the product._





URI: [kgr:versions](https://w3id.org/bridge2ai/data-sheets-schema/versions)
Alias: versions

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

* Range: [String](String.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:versions |
| native | kgr:versions |
| exact | schema:version, dcterms:hasVersion |




## LinkML Source

<details>
```yaml
name: versions
description: A list of names of versions of the product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
exact_mappings:
- schema:version
- dcterms:hasVersion
rank: 1000
alias: versions
owner: Product
domain_of:
- Product
range: string
multivalued: true

```
</details>
