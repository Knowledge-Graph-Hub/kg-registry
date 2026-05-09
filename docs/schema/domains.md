---
layout: schema_doc
mermaid: true
---



# Slot: domains


_The domain(s) that the resource is relevant to._





URI: [kgr:domains](https://w3id.org/bridge2ai/data-sheets-schema/domains)
Alias: domains

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

* Range: [DomainEnum](DomainEnum.html)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:domains |
| native | kgr:domains |




## LinkML Source

<details>
```yaml
name: domains
description: The domain(s) that the resource is relevant to.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: domains
owner: Resource
domain_of:
- Resource
range: DomainEnum
required: true
multivalued: true

```
</details>
