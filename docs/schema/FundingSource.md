---
layout: schema_doc
mermaid: true
---



# Class: FundingSource


_A funding source for a resource._





URI: [kgr:FundingSource](https://w3id.org/bridge2ai/data-sheets-schema/FundingSource)






```mermaid
 classDiagram
    class FundingSource
    click FundingSource href "FundingSource.html"
      NamedThing <|-- FundingSource
        click NamedThing href "NamedThing.html"
      
      FundingSource : category
        
      FundingSource : id
        
      FundingSource : label
        
          
    
    
    FundingSource --> "0..1" Organization : label
    click Organization href "Organization.html"

        
      FundingSource : layout
        
      FundingSource : warnings
        
      
```





## Inheritance
* [NamedThing](NamedThing.html)
    * **FundingSource**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.html) | 0..1 <br/> [Organization](Organization.html) | The organization providing the funding | direct |
| [id](id.html) | 1 <br/> [String](String.html) | The identifier of an entity | [NamedThing](NamedThing.html) |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | [NamedThing](NamedThing.html) |
| [warnings](warnings.html) | * <br/> [String](String.html) | A list of warnings about an item to be displayed in the interface | [NamedThing](NamedThing.html) |
| [layout](layout.html) | 0..1 <br/> [String](String.html) | The layout of the entity | [NamedThing](NamedThing.html) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Resource](Resource.html) | [funding](funding.html) | range | [FundingSource](FundingSource.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [funding](funding.html) | range | [FundingSource](FundingSource.html) |
| [DataSource](DataSource.html) | [funding](funding.html) | range | [FundingSource](FundingSource.html) |
| [DataModel](DataModel.html) | [funding](funding.html) | range | [FundingSource](FundingSource.html) |
| [Aggregator](Aggregator.html) | [funding](funding.html) | range | [FundingSource](FundingSource.html) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:FundingSource |
| native | kgr:FundingSource |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FundingSource
description: A funding source for a resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: NamedThing
attributes:
  label:
    name: label
    description: The organization providing the funding.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: Organization

```
</details>

### Induced

<details>
```yaml
name: FundingSource
description: A funding source for a resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
is_a: NamedThing
attributes:
  label:
    name: label
    description: The organization providing the funding.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    alias: label
    owner: FundingSource
    domain_of:
    - Individual
    - Organization
    - FundingSource
    - License
    - Usage
    range: Organization
  id:
    name: id
    description: The identifier of an entity. This is used to identify it within the
      registry.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: FundingSource
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
    owner: FundingSource
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
    owner: FundingSource
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
    owner: FundingSource
    domain_of:
    - NamedThing
    range: string

```
</details>
