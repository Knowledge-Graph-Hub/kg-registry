---
layout: schema_doc
mermaid: true
---



# Slot: authors


_The authors of the publication._





URI: [kgr:authors](https://w3id.org/bridge2ai/data-sheets-schema/authors)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.html) | A publication associated with a resource |  no  |







## Properties

* Range: [String](String.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:authors |
| native | kgr:authors |




## LinkML Source

<details>
```yaml
name: authors
description: The authors of the publication.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: authors
owner: Publication
domain_of:
- Publication
range: string
multivalued: true

```
</details>
