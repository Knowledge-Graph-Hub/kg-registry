---
layout: schema_doc
mermaid: true
---



# Slot: relation_type


_The PROV-O relation type that describes how the product is related to the source._





URI: [kgr:relation_type](https://w3id.org/bridge2ai/data-sheets-schema/relation_type)
Alias: relation_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourceAssociation](SourceAssociation.html) | A typed provenance association from a product to another resource or product ... |  no  |






## Properties

* Range: [ProvenanceRelationEnum](ProvenanceRelationEnum.html)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:relation_type |
| native | kgr:relation_type |




## LinkML Source

<details>
```yaml
name: relation_type
description: The PROV-O relation type that describes how the product is related to
  the source.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: relation_type
owner: SourceAssociation
domain_of:
- SourceAssociation
range: ProvenanceRelationEnum
required: true

```
</details>
