---
layout: schema_doc
mermaid: true
---



# Class: Resource


_A top-level class for all resources in the knowledge graph registry. Each resource may have multiple products or representations, but they will all be considered part of a the same parent resource._





URI: [kgr:Resource](https://w3id.org/bridge2ai/data-sheets-schema/Resource)





```mermaid
 classDiagram
    class Resource
    click Resource href "Resource/.html"
      NamedThing <|-- Resource
        click NamedThing href "NamedThing/.html"


      Resource <|-- KnowledgeGraph
        click KnowledgeGraph href "KnowledgeGraph/.html"
      Resource <|-- DataSource
        click DataSource href "DataSource/.html"
      Resource <|-- DataModel
        click DataModel href "DataModel/.html"
      Resource <|-- Ontology
        click Ontology href "Ontology/.html"
      Resource <|-- Aggregator
        click Aggregator href "Aggregator/.html"


      Resource : activity_status





        Resource --> "0..1" ActivityStatusEnum : activity_status
        click ActivityStatusEnum href "ActivityStatusEnum/.html"



      Resource : category

      Resource : collection





        Resource --> "*" CollectionEnum : collection
        click CollectionEnum href "CollectionEnum/.html"



      Resource : contacts





        Resource --> "*" Contact : contacts
        click Contact href "Contact/.html"



      Resource : creation_date

      Resource : curators





        Resource --> "*" Contact : curators
        click Contact href "Contact/.html"



      Resource : description

      Resource : domains





        Resource --> "1..*" DomainEnum : domains
        click DomainEnum href "DomainEnum/.html"



      Resource : fairsharing_id

      Resource : funding





        Resource --> "*" FundingSource : funding
        click FundingSource href "FundingSource/.html"



      Resource : homepage_url

      Resource : id

      Resource : infores_id

      Resource : language

      Resource : last_modified_date

      Resource : layout

      Resource : license





        Resource --> "0..1" License : license
        click License href "License/.html"



      Resource : name

      Resource : products





        Resource --> "*" Product : products
        click Product href "Product/.html"



      Resource : publications





        Resource --> "*" Publication : publications
        click Publication href "Publication/.html"



      Resource : repository

      Resource : synonyms

      Resource : tags





        Resource --> "*" TagEnum : tags
        click TagEnum href "TagEnum/.html"



      Resource : taxon

      Resource : usages





        Resource --> "*" Usage : usages
        click Usage href "Usage/.html"



      Resource : version

      Resource : warnings


```





## Inheritance
* [NamedThing](NamedThing.html)
    * **Resource**
        * [KnowledgeGraph](KnowledgeGraph.html)
        * [DataSource](DataSource.html)
        * [DataModel](DataModel.html)
        * [Ontology](Ontology.html)
        * [Aggregator](Aggregator.html)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [activity_status](activity_status.html) | 0..1 <br/> [ActivityStatusEnum](ActivityStatusEnum.html) | The status of the resource | direct |
| [name](name.html) | 1 <br/> [String](String.html) | The human-readable name of the resource | direct |
| [description](description.html) | 0..1 <br/> [String](String.html) | A description of the resource | direct |
| [homepage_url](homepage_url.html) | 0..1 <br/> [Uriorcurie](Uriorcurie.html) | The primary URL of the resource | direct |
| [repository](repository.html) | 0..1 <br/> [Uriorcurie](Uriorcurie.html) | A main version control repository for the resource | direct |
| [license](license_slot.html) | 0..1 <br/> [License](License.html) | The license of the resource | direct |
| [version](version.html) | 0..1 <br/> [String](String.html) | The version of the resource | direct |
| [language](language.html) | 0..1 <br/> [String](String.html) | The human language of the resource | direct |
| [contacts](contacts.html) | * <br/> [Contact](Contact.html) | The contact point(s) for the resource | direct |
| [curators](curators.html) | * <br/> [Contact](Contact.html) | The curator(s) of the resource | direct |
| [products](products.html) | * <br/> [Product](Product.html) | The products or representations of the resource | direct |
| [domains](domains.html) | 1..* <br/> [DomainEnum](DomainEnum.html) | The domain(s) that the resource is relevant to | direct |
| [tags](tags.html) | * <br/> [TagEnum](TagEnum.html) | Tags associated with the resource | direct |
| [funding](funding.html) | * <br/> [FundingSource](FundingSource.html) | The funding source(s) for the resource | direct |
| [publications](publications.html) | * <br/> [Publication](Publication.html) | Publications associated with the resource | direct |
| [usages](usages.html) | * <br/> [Usage](Usage.html) | The usage(s) of the resource | direct |
| [fairsharing_id](fairsharing_id.html) | 0..1 <br/> [String](String.html) | The FAIRsharing ID of the resource | direct |
| [infores_id](infores_id.html) | 0..1 <br/> [String](String.html) | The Infores ID of the resource | direct |
| [taxon](taxon.html) | * <br/> [Uriorcurie](Uriorcurie.html) | The taxon or taxa that the resource is relevant to | direct |
| [synonyms](synonyms.html) | * <br/> [String](String.html) | A list of synonyms for the resource | direct |
| [id](id.html) | 1 <br/> [String](String.html) | The identifier of an entity | [NamedThing](NamedThing.html) |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | [NamedThing](NamedThing.html) |
| [warnings](warnings.html) | * <br/> [String](String.html) | A list of warnings about an item to be displayed in the interface | [NamedThing](NamedThing.html) |
| [collection](collection.html) | * <br/> [CollectionEnum](CollectionEnum.html) | A collection of entries in the registry | [NamedThing](NamedThing.html) |
| [layout](layout.html) | 1 <br/> [String](String.html) | The layout of the entity | [NamedThing](NamedThing.html) |
| [creation_date](creation_date.html) | 0..1 <br/> [Datetime](Datetime.html) | The date the entry was created | [NamedThing](NamedThing.html) |
| [last_modified_date](last_modified_date.html) | 0..1 <br/> [Datetime](Datetime.html) | The date the entry was last modified | [NamedThing](NamedThing.html) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Registry](Registry.html) | [resources](resources.html) | range | [Resource](Resource.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [components](components.html) | range | [Resource](Resource.html) |
| [SourceAssociation](SourceAssociation.html) | [source](source.html) | any_of[range] | [Resource](Resource.html) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:Resource |
| native | kgr:Resource |
| close | schema:CreativeWork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Resource
description: A top-level class for all resources in the knowledge graph registry.
  Each resource may have multiple products or representations, but they will all be
  considered part of a the same parent resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
close_mappings:
- schema:CreativeWork
is_a: NamedThing
slot_usage:
  layout:
    name: layout
    required: true
attributes:
  activity_status:
    name: activity_status
    description: The status of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: ActivityStatusEnum
  name:
    name: name
    description: The human-readable name of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: string
    required: true
  description:
    name: description
    description: A description of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    - Organization
    - Usage
    range: string
  homepage_url:
    name: homepage_url
    description: The primary URL of the resource. This may be a link to download a
      specific file, a base URL to an API, or a link to a graphical interface, but
      it should preferentially be the main page documenting the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Organization
    range: uriorcurie
  repository:
    name: repository
    description: A main version control repository for the resource. Specific products
      may have their own repositories.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: uriorcurie
  license:
    name: license
    description: The license of the resource. Individual products may have their own
      licenses.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: License
    inlined: true
  version:
    name: version
    description: The version of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    exact_mappings:
    - schema:version
    - dcterms:hasVersion
    rank: 1000
    domain_of:
    - Resource
    - StandardCompatibility
    range: string
  language:
    name: language
    description: The human language of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: string
  contacts:
    name: contacts
    description: The contact point(s) for the resource. May be an individual or organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  curators:
    name: curators
    description: The curator(s) of the resource. May be an individual or organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  products:
    name: products
    description: The products or representations of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: Product
    multivalued: true
    inlined: true
    inlined_as_list: true
  domains:
    name: domains
    description: The domain(s) that the resource is relevant to.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: DomainEnum
    required: true
    multivalued: true
  tags:
    name: tags
    description: Tags associated with the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: TagEnum
    multivalued: true
  funding:
    name: funding
    description: The funding source(s) for the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: FundingSource
    multivalued: true
  publications:
    name: publications
    description: Publications associated with the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Usage
    range: Publication
    multivalued: true
    inlined: true
    inlined_as_list: true
  usages:
    name: usages
    description: The usage(s) of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: Usage
    multivalued: true
    inlined: true
    inlined_as_list: true
  fairsharing_id:
    name: fairsharing_id
    description: The FAIRsharing ID of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: string
  infores_id:
    name: infores_id
    description: The Infores ID of the resource. Do not include the 'infores' prefix.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    - Product
    range: string
  taxon:
    name: taxon
    description: The taxon or taxa that the resource is relevant to. This is preferably
      an NCBI Taxonomy identifier, in CURIE format.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: uriorcurie
    multivalued: true
  synonyms:
    name: synonyms
    description: A list of synonyms for the resource. These may include acronyms,
      abbreviations, or other alternate names for the resource. They are not necessarily
      unique across resources.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    domain_of:
    - Resource
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Resource
description: A top-level class for all resources in the knowledge graph registry.
  Each resource may have multiple products or representations, but they will all be
  considered part of a the same parent resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
close_mappings:
- schema:CreativeWork
is_a: NamedThing
slot_usage:
  layout:
    name: layout
    required: true
attributes:
  activity_status:
    name: activity_status
    description: The status of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: activity_status
    owner: Resource
    domain_of:
    - Resource
    range: ActivityStatusEnum
  name:
    name: name
    description: The human-readable name of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: name
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: string
    required: true
  description:
    name: description
    description: A description of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: description
    owner: Resource
    domain_of:
    - Resource
    - Product
    - Organization
    - Usage
    range: string
  homepage_url:
    name: homepage_url
    description: The primary URL of the resource. This may be a link to download a
      specific file, a base URL to an API, or a link to a graphical interface, but
      it should preferentially be the main page documenting the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: homepage_url
    owner: Resource
    domain_of:
    - Resource
    - Organization
    range: uriorcurie
  repository:
    name: repository
    description: A main version control repository for the resource. Specific products
      may have their own repositories.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: repository
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: uriorcurie
  license:
    name: license
    description: The license of the resource. Individual products may have their own
      licenses.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: license
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: License
    inlined: true
  version:
    name: version
    description: The version of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    exact_mappings:
    - schema:version
    - dcterms:hasVersion
    rank: 1000
    alias: version
    owner: Resource
    domain_of:
    - Resource
    - StandardCompatibility
    range: string
  language:
    name: language
    description: The human language of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: language
    owner: Resource
    domain_of:
    - Resource
    range: string
  contacts:
    name: contacts
    description: The contact point(s) for the resource. May be an individual or organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: contacts
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  curators:
    name: curators
    description: The curator(s) of the resource. May be an individual or organization.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: curators
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  products:
    name: products
    description: The products or representations of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: products
    owner: Resource
    domain_of:
    - Resource
    range: Product
    multivalued: true
    inlined: true
    inlined_as_list: true
  domains:
    name: domains
    description: The domain(s) that the resource is relevant to.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: domains
    owner: Resource
    domain_of:
    - Resource
    range: DomainEnum
    required: true
    multivalued: true
  tags:
    name: tags
    description: Tags associated with the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: tags
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: TagEnum
    multivalued: true
  funding:
    name: funding
    description: The funding source(s) for the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: funding
    owner: Resource
    domain_of:
    - Resource
    range: FundingSource
    multivalued: true
  publications:
    name: publications
    description: Publications associated with the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: publications
    owner: Resource
    domain_of:
    - Resource
    - Usage
    range: Publication
    multivalued: true
    inlined: true
    inlined_as_list: true
  usages:
    name: usages
    description: The usage(s) of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: usages
    owner: Resource
    domain_of:
    - Resource
    range: Usage
    multivalued: true
    inlined: true
    inlined_as_list: true
  fairsharing_id:
    name: fairsharing_id
    description: The FAIRsharing ID of the resource.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: fairsharing_id
    owner: Resource
    domain_of:
    - Resource
    range: string
  infores_id:
    name: infores_id
    description: The Infores ID of the resource. Do not include the 'infores' prefix.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: infores_id
    owner: Resource
    domain_of:
    - Resource
    - Product
    range: string
  taxon:
    name: taxon
    description: The taxon or taxa that the resource is relevant to. This is preferably
      an NCBI Taxonomy identifier, in CURIE format.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: taxon
    owner: Resource
    domain_of:
    - Resource
    range: uriorcurie
    multivalued: true
  synonyms:
    name: synonyms
    description: A list of synonyms for the resource. These may include acronyms,
      abbreviations, or other alternate names for the resource. They are not necessarily
      unique across resources.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: synonyms
    owner: Resource
    domain_of:
    - Resource
    range: string
    multivalued: true
  id:
    name: id
    description: The identifier of an entity. This is used to identify it within the
      registry.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: Resource
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
    owner: Resource
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
    owner: Resource
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
    owner: Resource
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
    owner: Resource
    domain_of:
    - NamedThing
    - Organization
    range: string
    required: true
  creation_date:
    name: creation_date
    description: The date the entry was created. This is used to determine the age
      of the entity. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    alias: creation_date
    owner: Resource
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
    owner: Resource
    domain_of:
    - NamedThing
    - Organization
    range: datetime

```
</details>
