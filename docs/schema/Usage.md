---
layout: schema_doc
mermaid: true
---



# Class: Usage


_The usage of a resource. This may be actual, experimental, or theoretical._





URI: [kgr:Usage](https://w3id.org/bridge2ai/data-sheets-schema/Usage)






```mermaid
 classDiagram
    class Usage
    click Usage href "Usage.html"
      NamedThing <|-- Usage
        click NamedThing href "NamedThing.html"
      
      Usage : category
        
      Usage : description
        
      Usage : id
        
      Usage : label
        
      Usage : layout
        
      Usage : publications
        
          
    
    
    Usage --> "*" Publication : publications
    click Publication href "Publication.html"

        
      Usage : type
        
          
    
    
    Usage --> "0..1" UsageEnum : type
    click UsageEnum href "UsageEnum.html"

        
      Usage : url
        
      Usage : users
        
          
    
    
    Usage --> "*" Contact : users
    click Contact href "Contact.html"

        
      Usage : warnings
        
      
```





## Inheritance
* [NamedThing](NamedThing.html)
    * **Usage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.html) | 0..1 <br/> [String](String.html) | The label of the usage | direct |
| [description](description.html) | 0..1 <br/> [String](String.html) | A description of the usage | direct |
| [url](url.html) | 0..1 <br/> [Uriorcurie](Uriorcurie.html) | A URL for a description or example of the usage | direct |
| [users](users.html) | * <br/> [Contact](Contact.html) | The user implementing or working with the resource | direct |
| [publications](publications.html) | * <br/> [Publication](Publication.html) | Publications associated with the usage | direct |
| [type](type.html) | 0..1 <br/> [UsageEnum](UsageEnum.html) | The type of usage | direct |
| [id](id.html) | 1 <br/> [String](String.html) | The identifier of an entity | [NamedThing](NamedThing.html) |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | [NamedThing](NamedThing.html) |
| [warnings](warnings.html) | * <br/> [String](String.html) | A list of warnings about an item to be displayed in the interface | [NamedThing](NamedThing.html) |
| [layout](layout.html) | 0..1 <br/> [String](String.html) | The layout of the entity | [NamedThing](NamedThing.html) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Resource](Resource.html) | [usages](usages.html) | range | [Usage](Usage.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [usages](usages.html) | range | [Usage](Usage.html) |
| [DataSource](DataSource.html) | [usages](usages.html) | range | [Usage](Usage.html) |
| [DataModel](DataModel.html) | [usages](usages.html) | range | [Usage](Usage.html) |
| [Aggregator](Aggregator.html) | [usages](usages.html) | range | [Usage](Usage.html) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:Usage |
| native | kgr:Usage |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Usage
description: The usage of a resource. This may be actual, experimental, or theoretical.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: NamedThing
attributes:
  label:
    name: label
    description: The label of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  description:
    name: description
    description: A description of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Resource
    - Product
    - Usage
    range: string
  url:
    name: url
    description: A URL for a description or example of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Product
    - Organization
    - Usage
    range: uriorcurie
  users:
    name: users
    description: The user implementing or working with the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Usage
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  publications:
    name: publications
    description: Publications associated with the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Resource
    - Usage
    range: Publication
    multivalued: true
    inlined: true
    inlined_as_list: true
  type:
    name: type
    description: The type of usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Usage
    range: UsageEnum

```
</details>

### Induced

<details>
```yaml
name: Usage
description: The usage of a resource. This may be actual, experimental, or theoretical.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: NamedThing
attributes:
  label:
    name: label
    description: The label of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: label
    owner: Usage
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: string
  description:
    name: description
    description: A description of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: description
    owner: Usage
    domain_of:
    - Resource
    - Product
    - Usage
    range: string
  url:
    name: url
    description: A URL for a description or example of the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: url
    owner: Usage
    domain_of:
    - Product
    - Organization
    - Usage
    range: uriorcurie
  users:
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
  publications:
    name: publications
    description: Publications associated with the usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: publications
    owner: Usage
    domain_of:
    - Resource
    - Usage
    range: Publication
    multivalued: true
    inlined: true
    inlined_as_list: true
  type:
    name: type
    description: The type of usage.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: type
    owner: Usage
    domain_of:
    - Usage
    range: UsageEnum
  id:
    name: id
    description: The identifier of an entity. This is used to identify it within the
      registry.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: Usage
    domain_of:
    - NamedThing
    range: string
    required: true
  category:
    name: category
    description: The category of the entity. This should be identical to its class
      name.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    is_a: type
    domain: NamedThing
    alias: category
    owner: Usage
    domain_of:
    - NamedThing
    - Contact
    range: category_type
  warnings:
    name: warnings
    description: A list of warnings about an item to be displayed in the interface.
      These should primarily warn users about unavailable resources, broken links,
      and other obstacles to using a resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: warnings
    owner: Usage
    domain_of:
    - NamedThing
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  layout:
    name: layout
    description: The layout of the entity. This is used to determine how to display
      the entity in the web interface. For resources, this is generally 'resource_detail'.
      For products, this is generally 'product_detail'.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: layout
    owner: Usage
    domain_of:
    - NamedThing
    range: string

```
</details>
