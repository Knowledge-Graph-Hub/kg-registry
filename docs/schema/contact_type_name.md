---
layout: schema_doc
mermaid: true
---



# Slot: contact_type_name


_The name of the contact detail, if the contact_type is "other". For example, if the contact value is a username at the Gumball Project's GitLab, this may be "Gumball Project GitLab"._





URI: [kgr:contact_type_name](https://w3id.org/bridge2ai/data-sheets-schema/contact_type_name)
Alias: contact_type_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactDetails](ContactDetails.html) | A field for details about how to contact a person or organization |  no  |






## Properties

* Range: [String](String.html)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:contact_type_name |
| native | kgr:contact_type_name |




## LinkML Source

<details>
```yaml
name: contact_type_name
description: The name of the contact detail, if the contact_type is "other". For example,
  if the contact value is a username at the Gumball Project's GitLab, this may be
  "Gumball Project GitLab".
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: contact_type_name
owner: ContactDetails
domain_of:
- ContactDetails
range: string

```
</details>
