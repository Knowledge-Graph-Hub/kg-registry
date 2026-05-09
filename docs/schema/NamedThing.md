---
layout: schema_doc
mermaid: true
---



# Class: NamedThing


_A generic grouping for any identifiable entity_





URI: [schema:Thing](http://schema.org/Thing)





```mermaid
 classDiagram
    class NamedThing
    click NamedThing href "NamedThing/.html"
      NamedThing <|-- Resource
        click Resource href "Resource/.html"
      NamedThing <|-- Product
        click Product href "Product/.html"
      NamedThing <|-- FundingSource
        click FundingSource href "FundingSource/.html"
      NamedThing <|-- License
        click License href "License/.html"
      NamedThing <|-- Publication
        click Publication href "Publication/.html"
      NamedThing <|-- Usage
        click Usage href "Usage/.html"

      NamedThing : category

      NamedThing : collection





        NamedThing --> "*" CollectionEnum : collection
        click CollectionEnum href "CollectionEnum/.html"



      NamedThing : creation_date

      NamedThing : id

      NamedThing : last_modified_date

      NamedThing : layout

      NamedThing : warnings


```





## Inheritance
* **NamedThing**
    * [Resource](Resource.html)
    * [Product](Product.html)
    * [FundingSource](FundingSource.html)
    * [License](License.html)
    * [Publication](Publication.html)
    * [Usage](Usage.html)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.html) | 1 <br/> [String](String.html) | The identifier of an entity | direct |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | direct |
| [warnings](warnings.html) | * <br/> [String](String.html) | A list of warnings about an item to be displayed in the interface | direct |
| [collection](collection.html) | * <br/> [CollectionEnum](CollectionEnum.html) | A collection of entries in the registry | direct |
| [layout](layout.html) | 0..1 <br/> [String](String.html) | The layout of the entity | direct |
| [creation_date](creation_date.html) | 0..1 <br/> [Datetime](Datetime.html) | The date the entry was created | direct |
| [last_modified_date](last_modified_date.html) | 0..1 <br/> [Datetime](Datetime.html) | The date the entry was last modified | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NamedThing](NamedThing.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Contact](Contact.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Resource](Resource.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [DataSource](DataSource.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [DataModel](DataModel.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Ontology](Ontology.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Aggregator](Aggregator.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Product](Product.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [GraphProduct](GraphProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [DataModelProduct](DataModelProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [OntologyProduct](OntologyProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [MappingProduct](MappingProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [ProcessProduct](ProcessProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [GraphicalInterface](GraphicalInterface.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [ProgrammingInterface](ProgrammingInterface.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [DocumentationProduct](DocumentationProduct.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [SourceAssociation](SourceAssociation.html) | [source](source.html) | range | [NamedThing](NamedThing.html) |
| [Individual](Individual.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Organization](Organization.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [FundingSource](FundingSource.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [License](License.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Publication](Publication.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |
| [Usage](Usage.html) | [category](category.html) | domain | [NamedThing](NamedThing.html) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:Thing |
| native | kgr:NamedThing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedThing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
slots:
- id
- category
- warnings
- collection
- layout
- creation_date
- last_modified_date
class_uri: schema:Thing

```
</details>

### Induced

<details>
```yaml
name: NamedThing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
attributes:
  id:
    name: id
    description: The identifier of an entity. This is used to identify it within the
      registry.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: NamedThing
    domain_of:
    - NamedThing
    - Organization
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
    owner: NamedThing
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
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  collection:
    name: collection
    description: A collection of entries in the registry. This is used to group related
      entries together. This is multivalued to allow for multiple collections.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: collection
    owner: NamedThing
    domain_of:
    - NamedThing
    range: CollectionEnum
    multivalued: true
  layout:
    name: layout
    description: The layout of the entity. This is used to determine how to display
      the entity in the web interface. For resources, this is generally 'resource_detail'.
      For products, this is generally 'product_detail'. If a value for this slot is
      not specified, pages won't contain anything from their header metadata.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: layout
    owner: NamedThing
    domain_of:
    - NamedThing
    - Organization
    range: string
  creation_date:
    name: creation_date
    description: The date the entry was created. This is used to determine the age
      of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: creation_date
    owner: NamedThing
    domain_of:
    - NamedThing
    - Organization
    range: datetime
  last_modified_date:
    name: last_modified_date
    description: The date the entry was last modified. It should be in ISO 8601 format,
      e.g., 2024-02-12T00:00:00Z.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: last_modified_date
    owner: NamedThing
    domain_of:
    - NamedThing
    - Organization
    range: datetime
class_uri: schema:Thing

```
</details>
