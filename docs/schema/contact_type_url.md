---
layout: schema_doc
mermaid: true
---



# Slot: contact_type_url


_The URL of the contact detail, if the contact_type is "other". For example, if the contact value is a username at the Gumball Project's GitLab, this may be "https://gitlab.gumballproject.org/"._





URI: [kgr:contact_type_url](https://w3id.org/bridge2ai/data-sheets-schema/contact_type_url)
Alias: contact_type_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactDetails](ContactDetails.html) | A field for details about how to contact a person or organization |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.html)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:contact_type_url |
| native | kgr:contact_type_url |




## LinkML Source

<details>
```yaml
name: contact_type_url
description: The URL of the contact detail, if the contact_type is "other". For example,
  if the contact value is a username at the Gumball Project's GitLab, this may be
  "https://gitlab.gumballproject.org/".
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: contact_type_url
owner: ContactDetails
domain_of:
- ContactDetails
range: uriorcurie

```
</details>
