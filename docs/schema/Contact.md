---
layout: schema_doc
mermaid: true
---



# Class: Contact


_A contact point for a resource or product, or a curator of a resource or product._





URI: [kgr:Contact](https://w3id.org/bridge2ai/data-sheets-schema/Contact)





```mermaid
 classDiagram
    class Contact
    click Contact href "Contact/.html"
      Contact <|-- Individual
        click Individual href "Individual/.html"
      Contact <|-- Organization
        click Organization href "Organization/.html"

      Contact : category

      Contact : contact_details





        Contact --> "*" ContactDetails : contact_details
        click ContactDetails href "ContactDetails/.html"




```





## Inheritance
* **Contact**
    * [Individual](Individual.html)
    * [Organization](Organization.html)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [category](category.html) | 0..1 <br/> [CategoryType](CategoryType.html) | The category of the entity | direct |
| [contact_details](contact_details.html) | * <br/> [ContactDetails](ContactDetails.html) | A field for contact details, including email, GitHub, and contact-specific UR... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Resource](Resource.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [Resource](Resource.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [KnowledgeGraph](KnowledgeGraph.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [DataSource](DataSource.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [DataSource](DataSource.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [DataModel](DataModel.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [DataModel](DataModel.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [Ontology](Ontology.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [Ontology](Ontology.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [Aggregator](Aggregator.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [Aggregator](Aggregator.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [Product](Product.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [Product](Product.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [GraphProduct](GraphProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [GraphProduct](GraphProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [DataModelProduct](DataModelProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [DataModelProduct](DataModelProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [OntologyProduct](OntologyProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [OntologyProduct](OntologyProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [MappingProduct](MappingProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [MappingProduct](MappingProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [ProcessProduct](ProcessProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [ProcessProduct](ProcessProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [GraphicalInterface](GraphicalInterface.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [GraphicalInterface](GraphicalInterface.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [ProgrammingInterface](ProgrammingInterface.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [ProgrammingInterface](ProgrammingInterface.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [DocumentationProduct](DocumentationProduct.html) | [contacts](contacts.html) | range | [Contact](Contact.html) |
| [DocumentationProduct](DocumentationProduct.html) | [curators](curators.html) | range | [Contact](Contact.html) |
| [Usage](Usage.html) | [users](users.html) | range | [Contact](Contact.html) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:Contact |
| native | kgr:Contact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Contact
description: A contact point for a resource or product, or a curator of a resource
  or product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
slots:
- category
- contact_details

```
</details>

### Induced

<details>
```yaml
name: Contact
description: A contact point for a resource or product, or a curator of a resource
  or product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
attributes:
  category:
    name: category
    description: The category of the entity. This should be identical to its class
      name.
    from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
    rank: 1000
    is_a: type
    domain: NamedThing
    alias: category
    owner: Contact
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
    owner: Contact
    domain_of:
    - Contact
    range: ContactDetails
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>
