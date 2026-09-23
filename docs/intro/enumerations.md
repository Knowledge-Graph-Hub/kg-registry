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
maps, where possible, to a controlled vocabulary concept (MeSH, NCIT, or EDAM) via its
`meaning`. Broad domains have specific domains beneath them, linked by `is_a`
(for example, `neurodegenerative disease` is a `neuroscience` domain). Examples:
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