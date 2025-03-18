---
layout: schema_doc
mermaid: true
---



# Slot: orcid


_The ORCID of the individual. Do not include the "https://orcid.org/" prefix._





URI: [kgr:orcid](https://w3id.org/bridge2ai/data-sheets-schema/orcid)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Individual](Individual.html) | An individual person |  no  |







## Properties

* Range: [String](String.html)

* Regex pattern: `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:orcid |
| native | kgr:orcid |




## LinkML Source

<details>
```yaml
name: orcid
description: The ORCID of the individual. Do not include the "https://orcid.org/"
  prefix.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: orcid
owner: Individual
domain_of:
- Individual
range: string
pattern: ^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$

```
</details>
