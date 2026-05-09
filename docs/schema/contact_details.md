---
layout: schema_doc
mermaid: true
---



# Slot: contact_details


_A field for contact details, including email, GitHub, and contact-specific URLs._





URI: [kgr:contact_details](https://w3id.org/bridge2ai/data-sheets-schema/contact_details)
Alias: contact_details

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.html) | An organization |  no  |
| [Individual](Individual.html) | An individual person |  no  |
| [Contact](Contact.html) | A contact point for a resource or product, or a curator of a resource or prod... |  no  |






## Properties

* Range: [ContactDetails](ContactDetails.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:contact_details |
| native | kgr:contact_details |




## LinkML Source

<details>
```yaml
name: contact_details
description: A field for contact details, including email, GitHub, and contact-specific
  URLs.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: contact_details
domain_of:
- Contact
range: ContactDetails
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
