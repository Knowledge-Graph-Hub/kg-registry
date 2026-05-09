---
layout: schema_doc
mermaid: true
---



# Slot: synonyms


_A list of synonyms for the resource. These may include acronyms, abbreviations, or other alternate names for the resource. They are not necessarily unique across resources._





URI: [kgr:synonyms](https://w3id.org/bridge2ai/data-sheets-schema/synonyms)
Alias: synonyms

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

* Range: [String](String.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:synonyms |
| native | kgr:synonyms |




## LinkML Source

<details>
```yaml
name: synonyms
description: A list of synonyms for the resource. These may include acronyms, abbreviations,
  or other alternate names for the resource. They are not necessarily unique across
  resources.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: synonyms
owner: Resource
domain_of:
- Resource
range: string
multivalued: true

```
</details>
