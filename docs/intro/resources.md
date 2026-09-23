---
layout: intro_doc
---

# Resources

All Resources have the following attributes:

- `name`: Human-readable name (required)
- `description`: Detailed description
- `homepage_url`: Primary resource URL
- `repository`: Version control repository
- `license`: Resource licensing information. When none is provided, the build fills this in from upstream sources and marks it `status: inferred` (see _License Inheritance_ below)
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

## License Inheritance

A KnowledgeGraph or Aggregator that provides no `license` is, by default,
bound by the licenses of the sources it was built from. The build fills in
`license` for such resources with the most restrictive license found among
their sources and marks it with `status: inferred`. A license without a
`status` is one the resource provided. The build never overwrites a provided
license. To replace an inferred license, edit the `license` block and drop the
`status` line and the `inferred_from`, `unresolved_sources`, and
`restrictiveness` lines with it.

On the resource page and in the registry table an inferred license shows as
the license label followed by "(inferred)". Hovering over that word lists the
sources that imposed it.

```yaml
license:
  id: https://www.omim.org/help/agreement
  inferred_from:
  - omim
  - umls
  label: OMIM Use Agreement
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
```

Sources are read from the resource's `components` field and from the
`original_source` and `secondary_source` associations on the products the
resource owns. Only associations whose relation carries content count:
`prov:hadPrimarySource`, `prov:wasDerivedFrom`, and `prov:used`.
`prov:wasInfluencedBy` and `prov:wasInformedBy` are ignored.

Each source is resolved to a license in this order: the license on the named
product, then the source resource's own `license`, then the most restrictive
license among that resource's products, then the source resource's own
inferred license. A source with no license anywhere is listed under
`unresolved_sources` and does not affect the result.

Licenses are ranked on a coarse ladder, least to most restrictive:

| Tier | Meaning | Examples |
|------|---------|----------|
| public domain | No rights reserved | CC0, Public Domain Mark, U.S. federal government works |
| permissive | Attribution, nothing more | CC BY, MIT, BSD, Apache, ODC-By |
| copyleft | Same or compatible license on reuse | CC BY-SA, ODbL, GPL family |
| non-commercial | Non-commercial or academic use only | CC BY-NC, CC BY-NC-SA, academic licenses |
| no derivatives | Redistribution without modification only | CC BY-ND, CC BY-NC-ND |
| custom | Terms that could not be placed on the ladder | Terms of use, subscriptions, controlled access, "varies" |

`custom` sits at the top because such terms have to be read before any reuse.
A license is placed by its URL first and by its label when the URL is not
recognized. A label that names several licenses lands on the most restrictive
one it names.

The inferred license lists `inferred_from`, the sources at the winning tier,
`unresolved_sources`, and `restrictiveness`, the tier itself. Inference runs
during `make` and can also be run on its own:

```
make infer-licenses-dry-run
make infer-licenses
make license-report
```

The report (`reports/license-inference.tsv`) covers every KnowledgeGraph and
Aggregator, including those with a declared license, and flags a `conflict`
when the declared license is less restrictive than what the sources impose.
A conflict is not an error in the registry. It is something to check with the
resource's maintainers.

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
MeSH lacks a suitable concept, the NCI Thesaurus (NCIT) or EDAM. These mappings are
recorded as the `meaning` of each value in `DomainEnum` and are shown as links
on each Resource page.

Domains form a two-level hierarchy. The broad domains below describe a field.
The specific domains that follow them name a narrower subject, such as a disease
area or a kind of data, and each one records its broad domain with `is_a`. A
Resource that lists a specific domain also lists its broad domain, so filtering
by a broad domain still finds it. Use a specific domain when the Resource is
substantially about that subject, not when the subject is one part of a larger
aggregate.

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
| **humanities and cultural heritage** | The humanities and cultural heritage: art history, architecture, musicology, media and performing arts, archaeology, history, and the collections that document them | [MeSH:D006809](https://meshb.nlm.nih.gov/record/ui?ui=D006809) |
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
| **research funding** | Research projects, grants and payments, funding programmes, and the organizations that fund or carry out research | [NCIT:C17090](http://purl.obolibrary.org/obo/NCIT_C17090) |
| **systems biology** | Computational/mathematical analysis of complex biological systems | [MeSH:D049490](https://meshb.nlm.nih.gov/record/ui?ui=D049490) |
| **toxicology** | The adverse effects of chemicals on living organisms | [MeSH:D014116](https://meshb.nlm.nih.gov/record/ui?ui=D014116) |
| **transportation** | Transportation and transport infrastructure: railway, road, air, and maritime networks and their assets | [MeSH:D014186](https://meshb.nlm.nih.gov/record/ui?ui=D014186) |
| **other** | Another domain not defined here | — |

Specific domains, grouped by the broad domain they belong to:

| Domain | Broad domain | Description | Controlled vocabulary |
| --- | --- | --- | --- |
| **aging** | biological systems | Aging and longevity, including cellular senescence | [MeSH:D000375](https://meshb.nlm.nih.gov/record/ui?ui=D000375) |
| **cell biology** | biological systems | Cells and cell types, including cell lines, cell markers, and subcellular structures | [MeSH:D003585](https://meshb.nlm.nih.gov/record/ui?ui=D003585) |
| **single-cell analysis** | biological systems | Data and methods that measure molecules in individual cells, including single-cell and spatial atlases | [MeSH:D059010](https://meshb.nlm.nih.gov/record/ui?ui=D059010) |
| **cancer** | biomedical | Cancer and other neoplasms, including tumor genomics, cancer cell lines, oncology treatment, and cancer registries | [MeSH:D009369](https://meshb.nlm.nih.gov/record/ui?ui=D009369) |
| **cardiovascular disease** | biomedical | Diseases of the heart and blood vessels, including hypertension | [MeSH:D002318](https://meshb.nlm.nih.gov/record/ui?ui=D002318) |
| **diabetes mellitus** | biomedical | Diabetes mellitus, including type 1 and type 2 diabetes and the pancreatic islet biology that underlies them | [MeSH:D003920](https://meshb.nlm.nih.gov/record/ui?ui=D003920) |
| **infectious disease** | biomedical | Infectious diseases, including their pathogens, transmission, epidemiology, diagnosis, and treatment | [MeSH:D003141](https://meshb.nlm.nih.gov/record/ui?ui=D003141) |
| **rare disease** | biomedical | Rare diseases, including rare Mendelian and other genetic disorders, their phenotypes, genes, and treatments | [MeSH:D035583](https://meshb.nlm.nih.gov/record/ui?ui=D035583) |
| **cheminformatics** | chemistry and biochemistry | Computational representation, identification, and classification of chemical structures | [MeSH:D000080911](https://meshb.nlm.nih.gov/record/ui?ui=D000080911) |
| **enzymes** | chemistry and biochemistry | Enzymes, including their classification, reactions, and catalytic mechanisms | [MeSH:D004798](https://meshb.nlm.nih.gov/record/ui?ui=D004798) |
| **glycomics** | chemistry and biochemistry | The study of glycans and glycoconjugates | [MeSH:D054794](https://meshb.nlm.nih.gov/record/ui?ui=D054794) |
| **metabolomics** | chemistry and biochemistry | The large-scale study of metabolites and lipids, including mass spectrometry and NMR data | [MeSH:D055432](https://meshb.nlm.nih.gov/record/ui?ui=D055432) |
| **natural products** | chemistry and biochemistry | Compounds derived from plants, microorganisms, or animals, including traditional medicines | [NCIT:C1907](http://purl.obolibrary.org/obo/NCIT_C1907) |
| **clinical coding** | clinical | Clinical terminologies and code sets for diagnoses, procedures, observations, and medications | [MeSH:D059019](https://meshb.nlm.nih.gov/record/ui?ui=D059019) |
| **clinical trials** | clinical | Clinical trials, including trial registries and the data standards used to report them | [MeSH:D002986](https://meshb.nlm.nih.gov/record/ui?ui=D002986) |
| **electronic health records** | clinical | Electronic health records and observational health data derived from them | [MeSH:D057286](https://meshb.nlm.nih.gov/record/ui?ui=D057286) |
| **drug repositioning** | drug discovery | The discovery of new indications for existing drugs, including computational repurposing methods and their benchmarks | [MeSH:D058492](https://meshb.nlm.nih.gov/record/ui?ui=D058492) |
| **high-throughput screening** | drug discovery | Large-scale screening of chemical or genetic perturbations, including cell line sensitivity and perturbation profiling | [MeSH:D057166](https://meshb.nlm.nih.gov/record/ui?ui=D057166) |
| **air pollution** | environment | Air quality and emissions to air | [MeSH:D000397](https://meshb.nlm.nih.gov/record/ui?ui=D000397) |
| **climate** | environment | Climate and climate change, including climate models and drought | [MeSH:D002980](https://meshb.nlm.nih.gov/record/ui?ui=D002980) |
| **ecology** | environment | The interactions of organisms with each other and their environment, including ecological networks | [MeSH:D004463](https://meshb.nlm.nih.gov/record/ui?ui=D004463) |
| **environmental exposure** | environment | Exposure of people and organisms to environmental agents and the health effects of those exposures | [MeSH:D004781](https://meshb.nlm.nih.gov/record/ui?ui=D004781) |
| **geographic information systems** | environment | Geospatial data, including place names, administrative boundaries, and infrastructure maps | [MeSH:D040362](https://meshb.nlm.nih.gov/record/ui?ui=D040362) |
| **sustainability** | environment | Sustainability and environmental, social, and governance (ESG) reporting | [MeSH:D000076502](https://meshb.nlm.nih.gov/record/ui?ui=D000076502) |
| **water resources** | environment | Surface water, groundwater, drinking water, and hydrology | [MeSH:D062066](https://meshb.nlm.nih.gov/record/ui?ui=D062066) |
| **wildfires** | environment | Wildfires and their burn severity and smoke | [MeSH:D000075923](https://meshb.nlm.nih.gov/record/ui?ui=D000075923) |
| **epigenomics** | genomics | Genome-wide chromatin state and organization, including chromatin conformation and regulatory element annotation | [MeSH:D057890](https://meshb.nlm.nih.gov/record/ui?ui=D057890) |
| **gene expression profiling** | genomics | Measurement of gene expression across tissues, cells, and conditions, including transcriptomic signatures | [MeSH:D020869](https://meshb.nlm.nih.gov/record/ui?ui=D020869) |
| **gene regulation** | genomics | The regulation of gene expression, including transcription factors, their binding sites, promoters, and enhancers | [MeSH:D005786](https://meshb.nlm.nih.gov/record/ui?ui=D005786) |
| **genetic variation** | genomics | Germline and somatic genetic variants, including their frequencies, effects, and clinical interpretation | [MeSH:D014644](https://meshb.nlm.nih.gov/record/ui?ui=D014644) |
| **genome-wide association studies** | genomics | Genome-wide association studies and related statistical genetics, including QTL and Mendelian randomization analyses | [MeSH:D055106](https://meshb.nlm.nih.gov/record/ui?ui=D055106) |
| **molecular evolution** | genomics | The evolution of genes and proteins, including orthology, gene families, and comparative analysis | [MeSH:D019143](https://meshb.nlm.nih.gov/record/ui?ui=D019143) |
| **non-coding RNA** | genomics | RNAs that are not translated into protein, including microRNAs, long non-coding RNAs, and ribosomal and transfer RNAs | [MeSH:D022661](https://meshb.nlm.nih.gov/record/ui?ui=D022661) |
| **population genetics** | genomics | Genetic variation within and between populations, including human ancestry | [MeSH:D005828](https://meshb.nlm.nih.gov/record/ui?ui=D005828) |
| **vaccines** | immunology | Vaccines and vaccination, including vaccine adverse events | [MeSH:D014612](https://meshb.nlm.nih.gov/record/ui?ui=D014612) |
| **machine learning** | information technology | Machine learning and artificial intelligence, including AI-ready data and models | [MeSH:D000069550](https://meshb.nlm.nih.gov/record/ui?ui=D000069550) |
| **metadata** | information technology | Metadata vocabularies and standards for describing resources, datasets, and provenance | [MeSH:D000071253](https://meshb.nlm.nih.gov/record/ui?ui=D000071253) |
| **software** | information technology | Software, including package registries, software supply chains, and vulnerabilities | [MeSH:D012984](https://meshb.nlm.nih.gov/record/ui?ui=D012984) |
| **natural language processing** | literature | Text mining and natural language processing of the literature, including text-mined knowledge graphs and annotated corpora | [MeSH:D009323](https://meshb.nlm.nih.gov/record/ui?ui=D009323) |
| **scholarly communication** | literature | Scholarly publications and their metadata, including citations, authors, and research contributions | [MeSH:D000073820](https://meshb.nlm.nih.gov/record/ui?ui=D000073820) |
| **host-pathogen interactions** | microbiology | Interactions between pathogens and their hosts, including pathogen genomics and virulence | [MeSH:D054884](https://meshb.nlm.nih.gov/record/ui?ui=D054884) |
| **microbiome** | microbiology | Microbial communities, including host-associated microbiomes and metagenomes | [MeSH:D064307](https://meshb.nlm.nih.gov/record/ui?ui=D064307) |
| **mental disorders** | neuroscience | Mental and psychiatric disorders, including substance use disorders | [MeSH:D001523](https://meshb.nlm.nih.gov/record/ui?ui=D001523) |
| **neurodegenerative disease** | neuroscience | Neurodegenerative diseases, including Alzheimer disease and related dementias | [MeSH:D019636](https://meshb.nlm.nih.gov/record/ui?ui=D019636) |
| **food** | nutrition | Foods, their composition, and their relationship to diet and health | [MeSH:D005502](https://meshb.nlm.nih.gov/record/ui?ui=D005502) |
| **biodiversity** | organisms | The variety of life, including species occurrence, conservation status, and invasive species | [MeSH:D044822](https://meshb.nlm.nih.gov/record/ui?ui=D044822) |
| **domestic animals** | organisms | Domestic animals, including companion animals and livestock breeds | [MeSH:D000829](https://meshb.nlm.nih.gov/record/ui?ui=D000829) |
| **human populations** | organisms | Human population groups, including ancestry, ethnicity, and demographic groups | [MeSH:D044382](https://meshb.nlm.nih.gov/record/ui?ui=D044382) |
| **insects** | organisms | Insects, including their anatomy, behavior, and genomics | [MeSH:D007313](https://meshb.nlm.nih.gov/record/ui?ui=D007313) |
| **model organisms** | organisms | Model organisms and the databases that serve their research communities | [EDAM:topic_0621](http://edamontology.org/topic_0621) |
| **plants** | organisms | Plants, including crops and their anatomy, traits, and genomics | [MeSH:D010944](https://meshb.nlm.nih.gov/record/ui?ui=D010944) |
| **taxonomy** | organisms | The naming and classification of organisms and the relationships among taxa | [NCIT:C17469](http://purl.obolibrary.org/obo/NCIT_C17469) |
| **metabolism** | pathways | Metabolic pathways and genome-scale metabolic network reconstructions | [MeSH:D008660](https://meshb.nlm.nih.gov/record/ui?ui=D008660) |
| **signal transduction** | pathways | Signaling pathways and networks that transmit signals within and between cells | [MeSH:D015398](https://meshb.nlm.nih.gov/record/ui?ui=D015398) |
| **drug interactions** | pharmacology | Interactions between drugs and between drugs and foods or natural products | [MeSH:D004347](https://meshb.nlm.nih.gov/record/ui?ui=D004347) |
| **pharmacogenomics** | pharmacology | The influence of genetic variation on drug response | [MeSH:D010597](https://meshb.nlm.nih.gov/record/ui?ui=D010597) |
| **pharmacovigilance** | pharmacology | The monitoring of drug and device safety, including adverse event reports and side effects | [MeSH:D060735](https://meshb.nlm.nih.gov/record/ui?ui=D060735) |
| **post-translational modification** | proteomics | Post-translational modifications of proteins, such as phosphorylation | [MeSH:D011499](https://meshb.nlm.nih.gov/record/ui?ui=D011499) |
| **protein domains** | proteomics | Protein families, domains, and functional sites | [MeSH:D000072417](https://meshb.nlm.nih.gov/record/ui?ui=D000072417) |
| **protein interactions** | proteomics | Physical interactions between proteins, including protein complexes | [MeSH:D060066](https://meshb.nlm.nih.gov/record/ui?ui=D060066) |
| **protein structure** | proteomics | The three-dimensional structure of proteins, whether determined experimentally or predicted | [MeSH:D011487](https://meshb.nlm.nih.gov/record/ui?ui=D011487) |
| **criminal justice** | public health | Crime, courts, and the justice system, including crime reporting and court records | [MeSH:D003416](https://meshb.nlm.nih.gov/record/ui?ui=D003416) |
| **disasters** | public health | Disasters and emergencies, including disaster declarations, humanitarian response, and critical infrastructure | [MeSH:D004190](https://meshb.nlm.nih.gov/record/ui?ui=D004190) |
| **disease registries** | public health | Population-based registries of disease cases, such as cancer registries | [MeSH:D012042](https://meshb.nlm.nih.gov/record/ui?ui=D012042) |
| **epidemiology** | public health | The distribution and determinants of disease in populations, including disease surveillance and outbreaks | [MeSH:D004813](https://meshb.nlm.nih.gov/record/ui?ui=D004813) |
| **social determinants of health** | public health | The social and economic conditions that shape health, including housing, income, services, and rurality | [MeSH:D064890](https://meshb.nlm.nih.gov/record/ui?ui=D064890) |
| **adverse outcome pathways** | toxicology | Adverse outcome pathways linking molecular initiating events to adverse outcomes | [MeSH:D000073931](https://meshb.nlm.nih.gov/record/ui?ui=D000073931) |

(The `stub` value is reserved for auto-generated placeholder pages and is not a
subject-matter domain.)
