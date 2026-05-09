---
layout: schema_doc
mermaid: true
---



# Slot: taxon


_The taxon or taxa that the resource is relevant to. This is preferably an NCBI Taxonomy identifier, in CURIE format._





URI: [kgr:taxon](https://w3id.org/bridge2ai/data-sheets-schema/taxon)
Alias: taxon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataModel](DataModel.html) | A data model is a formal representation of concepts and relationships within ... |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [Ontology](Ontology.html) | An ontology is a formal representation of a set of concepts within a domain a... |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:taxon |
| native | kgr:taxon |




## LinkML Source

<details>
```yaml
name: taxon
description: The taxon or taxa that the resource is relevant to. This is preferably
  an NCBI Taxonomy identifier, in CURIE format.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: taxon
owner: Resource
domain_of:
- Resource
range: uriorcurie
multivalued: true

```
</details>
