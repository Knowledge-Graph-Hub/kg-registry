---
layout: schema_doc
mermaid: true
---



# Slot: users


_The user implementing or working with the resource._





URI: [kgr:users](https://w3id.org/bridge2ai/data-sheets-schema/users)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Usage](Usage.html) | The usage of a resource |  no  |







## Properties

* Range: [Contact](Contact.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:users |
| native | kgr:users |




## LinkML Source

<details>
```yaml
name: users
description: The user implementing or working with the resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: users
owner: Usage
domain_of:
- Usage
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
