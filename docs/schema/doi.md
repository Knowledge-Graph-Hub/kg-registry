---
layout: schema_doc
mermaid: true
---



# Slot: doi


_The DOI of the publication. This should include the doi: prefix._





URI: [kgr:doi](https://w3id.org/bridge2ai/data-sheets-schema/doi)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.html) | A publication associated with a resource |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:doi |
| native | kgr:doi |




## LinkML Source

<details>
```yaml
name: doi
description: 'The DOI of the publication. This should include the doi: prefix.'
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: doi
owner: Publication
domain_of:
- Publication
range: uriorcurie

```
</details>
