---
layout: schema_doc
mermaid: true
---



# Slot: contact_type


_The type of contact detail._





URI: [kgr:contact_type](https://w3id.org/bridge2ai/data-sheets-schema/contact_type)
Alias: contact_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactDetails](ContactDetails.html) | A field for details about how to contact a person or organization |  no  |






## Properties

* Range: [ContactTypeEnum](ContactTypeEnum.html)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:contact_type |
| native | kgr:contact_type |




## LinkML Source

<details>
```yaml
name: contact_type
description: The type of contact detail.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: contact_type
owner: ContactDetails
domain_of:
- ContactDetails
range: ContactTypeEnum
required: true

```
</details>
