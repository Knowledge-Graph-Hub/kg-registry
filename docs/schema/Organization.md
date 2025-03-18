---
layout: schema_doc
mermaid: true
---



# Class: Organization


_An organization._





URI: [kgr:Organization](https://w3id.org/bridge2ai/data-sheets-schema/Organization)






```mermaid
 classDiagram
    class Organization
    click Organization href "Organization.html"
      Contact <|-- Organization
        click Contact href "Contact.html"
      
      Organization : category
        
      Organization : email
        
      Organization : github
        
      Organization : label
        
      Organization : url
        
      
```





## Inheritance
* [Contact](Contact.html)
    * **Organization**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.html) | 0..1 <br/> [String](String.html) | The name of the organization | direct |
| [email](email.html) | 0..1 <br/> [String](String.html) | The email address of the organization | direct |
| [github](github.html) | 0..1 <br/> [String](String.html) | The GitHub organization name | direct |
| [url](url.html) | 0..1 <br/> [Uriorcurie](Uriorcurie.html) | The URL of a site for the organization | direct |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | [Contact](Contact.html) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FundingSource](FundingSource.html) | [label](label.html) | range | [Organization](Organization.html) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:Organization |
| native | kgr:Organization |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: An organization.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: Contact
attributes:
  label:
    name: label
    description: The name of the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  email:
    name: email
    description: The email address of the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Individual
    - Organization
    range: string
  github:
    name: github
    description: The GitHub organization name. Do not include a prefix.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Individual
    - Organization
    range: string
  url:
    name: url
    description: The URL of a site for the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Organization
    - Usage
    range: uriorcurie

```
</details>

### Induced

<details>
```yaml
name: Organization
description: An organization.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: Contact
attributes:
  label:
    name: label
    description: The name of the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: label
    owner: Organization
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  email:
    name: email
    description: The email address of the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: email
    owner: Organization
    domain_of:
    - Individual
    - Organization
    range: string
  github:
    name: github
    description: The GitHub organization name. Do not include a prefix.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: github
    owner: Organization
    domain_of:
    - Individual
    - Organization
    range: string
  url:
    name: url
    description: The URL of a site for the organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: url
    owner: Organization
    domain_of:
    - Organization
    - Usage
    range: uriorcurie
  category:
    name: category
    description: The category of the entity. This should be identical to its class
      name.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    is_a: type
    domain: NamedThing
    alias: category
    owner: Organization
    domain_of:
    - NamedThing
    - Contact
    range: category_type

```
</details>
