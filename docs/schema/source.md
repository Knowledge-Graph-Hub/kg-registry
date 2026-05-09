---
layout: schema_doc
mermaid: true
---



# Slot: source


_The identifier of the resource or product that is related to the product through this provenance association._





URI: [kgr:source](https://w3id.org/bridge2ai/data-sheets-schema/source)
Alias: source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourceAssociation](SourceAssociation.html) | A typed provenance association from a product to another resource or product ... |  no  |






## Properties

* Range: [NamedThing](NamedThing.html)&nbsp;or&nbsp;<br />[Resource](Resource.html)&nbsp;or&nbsp;<br />[Product](Product.html)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:source |
| native | kgr:source |




## LinkML Source

<details>
```yaml
name: source
description: The identifier of the resource or product that is related to the product
  through this provenance association.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: source
owner: SourceAssociation
domain_of:
- SourceAssociation
range: NamedThing
required: true
any_of:
- range: Resource
- range: Product

```
</details>
