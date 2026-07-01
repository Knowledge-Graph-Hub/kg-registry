---
layout: intro_doc
---

# Resources

All Resources have the following attributes:

- `name`: Human-readable name (required)
- `description`: Detailed description
- `homepage_url`: Primary resource URL
- `repository`: Version control repository
- `license`: Resource licensing information
- `version`: Resource version
- `domain`: Primary scientific domain (see _Domains_ below)
- `contacts`: List of contact points
- `products`: Specific representations of the resource
- `activity_status`: Current state of the resource (active, inactive, etc.)
- `use_instead`: KG-Registry Resource ID(s) that replace this resource (see _Pointing to a Replacement Resource_ below)
- `tags`: Categorization tags
- `funding`: Funding source information

## Specialized Resource Types

Each Resource may have a more specific type.

### KnowledgeGraph

A specialized Resource for graph-based data:
- Tracks graph creation and modification dates
- Lists contributors and components
- Represents nodes and edges data collection

### DataSource

This Resource provides data. The data may or may not be in a graph structure.

### DataModel

This Resource defines a data structure, i.e., a way to describe how data is organized and how its components relate to one another.

### Ontology

This Resource defines an ontology, or a formal representation of a set of concepts within a domain and the relationships between those concepts.

### Aggregator

This Resource combines multiple data sources.

## Pointing to a Replacement Resource

Some resources are obsoleted or absorbed by others over time. When that happens
we do not delete the older Resource's page — its metadata still has historical
and provenance value — but we point visitors toward whatever they should use in
its place. This is done with the `use_instead` field, which holds one or more
KG-Registry Resource IDs. On the Resource page these appear as a "Use instead"
notice linking to the replacement(s).

We apply `use_instead` conservatively, only when both of the following hold:

- **The resource is not active.** Its `activity_status` is `inactive`,
  `orphaned`, or `unresponsive`. We do not redirect users away from an active
  resource, even if a similar one exists.
- **There is a clear replacement.** This is usually one of two situations:
  - A newer resource was explicitly intended to supersede the older one (for
    example, a version 2 released under a new identifier), or
  - The older resource has been subsumed by, merged into, or fully absorbed by
    another resource that now covers its content.

When neither a clear successor nor an absorbing resource exists — for instance a
resource that was simply discontinued — we leave `use_instead` empty and rely on
the `activity_status` banner alone. If a resource was split into several
successors, or was subsumed by more than one resource, list each replacement ID.

The value of each `use_instead` entry must be an existing KG-Registry Resource
ID (the `id` of the replacement's page), not a name or URL.

## Domains

Each Resource is annotated with one or more domains describing the kinds of
information it provides. Wherever possible a domain maps to a concept in an
external controlled vocabulary — the Medical Subject Headings (MeSH) or, where
MeSH lacks a suitable concept, the NCI Thesaurus (NCIT). These mappings are
recorded as the `meaning` of each value in `DomainEnum` and are shown as links
on each Resource page.

Resources may cover one or more of the following domains:

| Domain | Description | Controlled vocabulary |
| --- | --- | --- |
| **agriculture** | Agricultural and food sciences, including crops, animals, plant science, and food production | [MeSH:D000383](https://meshb.nlm.nih.gov/record/ui?ui=D000383) |
| **anatomy and development** | The anatomy, structure, and developmental biology of organisms | [MeSH:D000715](https://meshb.nlm.nih.gov/record/ui?ui=D000715) |
| **biological systems** | The biological sciences broadly, where no more specific domain applies | [MeSH:D001690](https://meshb.nlm.nih.gov/record/ui?ui=D001690) |
| **biomedical** | The biomedical sciences spanning health and disease | [MeSH:D035843](https://meshb.nlm.nih.gov/record/ui?ui=D035843) |
| **chemistry and biochemistry** | The chemical and biochemical sciences | [MeSH:D002621](https://meshb.nlm.nih.gov/record/ui?ui=D002621) |
| **clinical** | The clinical sciences, including trials, patient data, diagnosis, and treatment | [MeSH:D015510](https://meshb.nlm.nih.gov/record/ui?ui=D015510) |
| **drug discovery** | Identification and development of new candidate medications | [MeSH:D055808](https://meshb.nlm.nih.gov/record/ui?ui=D055808) |
| **environment** | The environment, ecosystems, ecology, and environmental health | [MeSH:D004777](https://meshb.nlm.nih.gov/record/ui?ui=D004777) |
| **general** | Broadly applicable, cross-domain, or upper-level resources | — |
| **genomics** | The study of genomes, including structure, function, mapping, and editing | [MeSH:D023281](https://meshb.nlm.nih.gov/record/ui?ui=D023281) |
| **immunology** | The study of the immune system and its disorders | [MeSH:D000486](https://meshb.nlm.nih.gov/record/ui?ui=D000486) |
| **information technology** | Informatics, software, computational methods, simulation, and digital health | [MeSH:D000073256](https://meshb.nlm.nih.gov/record/ui?ui=D000073256) |
| **literature** | The literature and publications of a domain | [MeSH:D011642](https://meshb.nlm.nih.gov/record/ui?ui=D011642) |
| **medical imaging** | Techniques for visual representation of the body for clinical analysis | [MeSH:D003952](https://meshb.nlm.nih.gov/record/ui?ui=D003952) |
| **microbiology** | The microbiological sciences, including microbiomes | [MeSH:D008829](https://meshb.nlm.nih.gov/record/ui?ui=D008829) |
| **neuroscience** | The study of the nervous system and its disorders | [MeSH:D009488](https://meshb.nlm.nih.gov/record/ui?ui=D009488) |
| **nutrition** | The nutritional sciences, including diet and metabolomics | [MeSH:D052756](https://meshb.nlm.nih.gov/record/ui?ui=D052756) |
| **organisms** | Specific organisms or taxa | [NCIT:C14250](http://purl.obolibrary.org/obo/NCIT_C14250) |
| **pathways** | Biological pathways: metabolic, signaling, and regulatory networks | [MeSH:D053858](https://meshb.nlm.nih.gov/record/ui?ui=D053858) |
| **pharmacology** | How drugs interact with biological systems | [MeSH:D010600](https://meshb.nlm.nih.gov/record/ui?ui=D010600) |
| **phenotype** | The phenotypes of organisms | [MeSH:D010641](https://meshb.nlm.nih.gov/record/ui?ui=D010641) |
| **precision medicine** | Treatment/prevention accounting for individual variability | [MeSH:D057285](https://meshb.nlm.nih.gov/record/ui?ui=D057285) |
| **proteomics** | The large-scale study of proteins | [MeSH:D040901](https://meshb.nlm.nih.gov/record/ui?ui=D040901) |
| **public health** | Population health, epidemiology, and social determinants of health | [MeSH:D011634](https://meshb.nlm.nih.gov/record/ui?ui=D011634) |
| **systems biology** | Computational/mathematical analysis of complex biological systems | [MeSH:D049490](https://meshb.nlm.nih.gov/record/ui?ui=D049490) |
| **toxicology** | The adverse effects of chemicals on living organisms | [MeSH:D014116](https://meshb.nlm.nih.gov/record/ui?ui=D014116) |
| **other** | Another domain not defined here | — |

(The `stub` value is reserved for auto-generated placeholder pages and is not a
subject-matter domain.)
