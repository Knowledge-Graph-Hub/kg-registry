---
layout: intro_doc
---

# Enumerations

## ActivityStatusEnum
Describes resource availability:
- `active`: Fully available
- `inactive`: Variable availability
- `orphaned`: Not maintained
- `unresponsive`: Metadata only

## DomainEnum
Scientific domains describing the information a resource provides. Each value
maps, where possible, to a controlled vocabulary concept (MeSH or NCIT) via its
`meaning`. Examples:
- Biomedical
- Clinical
- Genomics
- Proteomics
- Anatomy & Development
- Environment
- And more (see [Domains](resources.html#domains) for the full list and mappings)

## FormatEnum
Data serialization formats:
- JSON
- RDF/XML
- Turtle
- OWL
- GraphQL
- KGX variants

## StandardEnum
Compatibility standards:
- Biolink Model
- KG-Hub standard

## Other Enumerations
- `CompressionEnum`: Compression types
- `TagEnum`: Resource tags
- `UsageEnum`: Usage classification