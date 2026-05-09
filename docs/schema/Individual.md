---
layout: schema_doc
mermaid: true
---



# Class: Individual


_An individual person._





URI: [kgr:Individual](https://w3id.org/bridge2ai/data-sheets-schema/Individual)





```mermaid
 classDiagram
    class Individual
    click Individual href "Individual/.html"
      Contact <|-- Individual
        click Contact href "Contact/.html"

      Individual : category

      Individual : contact_details





        Individual --> "*" ContactDetails : contact_details
        click ContactDetails href "ContactDetails/.html"



      Individual : label

      Individual : orcid


```





## Inheritance
* [Contact](Contact.html)
    * **Individual**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.html) | 0..1 <br/> [String](String.html) | The name of the individual | direct |
| [orcid](orcid.html) | 0..1 <br/> [String](String.html) | The ORCID of the individual | direct |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | [Contact](Contact.html) |
| [contact_details](contact_details.html) | * <br/> [ContactDetails](ContactDetails.html) | A field for contact details, including email, GitHub, and contact-specific UR... | [Contact](Contact.html) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:Individual |
| native | kgr:Individual |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Individual
description: An individual person.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: Contact
attributes:
  label:
    name: label
    description: The name of the individual.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  orcid:
    name: orcid
    description: The ORCID of the individual. Do not include the "https://orcid.org/"
      prefix.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Individual
    range: string
    pattern: ^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$

```
</details>

### Induced

<details>
```yaml
name: Individual
description: An individual person.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: Contact
attributes:
  label:
    name: label
    description: The name of the individual.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: label
    owner: Individual
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  orcid:
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
  category:
    name: category
    description: The category of the entity. This should be identical to its class
      name.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    is_a: type
    domain: NamedThing
    alias: category
    owner: Individual
    domain_of:
    - NamedThing
    - Contact
    range: category_type
  contact_details:
    name: contact_details
    description: A field for contact details, including email, GitHub, and contact-specific
      URLs.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: contact_details
    owner: Individual
    domain_of:
    - Contact
    range: ContactDetails
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>
