---
layout: schema_doc
mermaid: true
---

# Enum: ContactTypeEnum




_The type of contact detail._



URI: [kgr:ContactTypeEnum](https://w3id.org/bridge2ai/data-sheets-schema/ContactTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| email | None | An email address for the contact |
| github | None | A GitHub username for the contact |
| url | None | A URL for the contact |
| other | None | Another type of contact detail not defined here |




## Slots

| Name | Description |
| ---  | --- |
| [contact_type](contact_type.html) | The type of contact detail |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: ContactTypeEnum
description: The type of contact detail.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  email:
    text: email
    description: An email address for the contact.
  github:
    text: github
    description: A GitHub username for the contact.
  url:
    text: url
    description: A URL for the contact. For an individual, this may be a profile on
      an official website. For an organization, this may be a link to the organization's
      site or a documentation landing page.
  other:
    text: other
    description: Another type of contact detail not defined here.

```
</details>
