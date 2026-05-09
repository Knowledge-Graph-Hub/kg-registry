---
layout: schema_doc
mermaid: true
---



# Slot: value


_The value of the contact detail. For example, an email address or URL. Do not include a prefix._





URI: [kgr:value](https://w3id.org/bridge2ai/data-sheets-schema/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactDetails](ContactDetails.html) | A field for details about how to contact a person or organization |  no  |






## Properties

* Range: [String](String.html)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:value |
| native | kgr:value |




## LinkML Source

<details>
```yaml
name: value
description: The value of the contact detail. For example, an email address or URL.
  Do not include a prefix.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: value
owner: ContactDetails
domain_of:
- ContactDetails
range: string
required: true

```
</details>
