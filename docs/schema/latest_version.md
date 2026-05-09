---
layout: schema_doc
mermaid: true
---



# Slot: latest_version


_The latest version of the product, or the most recent version curated in the registry. If the product is available at a permanent link, this may be something like "latest"._





URI: [kgr:latest_version](https://w3id.org/bridge2ai/data-sheets-schema/latest_version)
Alias: latest_version

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




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:latest_version |
| native | kgr:latest_version |




## LinkML Source

<details>
```yaml
name: latest_version
description: The latest version of the product, or the most recent version curated
  in the registry. If the product is available at a permanent link, this may be something
  like "latest".
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: latest_version
owner: Product
domain_of:
- Product
range: string

```
</details>
