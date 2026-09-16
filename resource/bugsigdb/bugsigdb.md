---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: lwaldron
  label: Levi Waldron
  orcid: 0000-0003-2725-0694
- category: Organization
  contact_details:
  - contact_type: github
    value: waldronlab
  label: Waldron Lab
creation_date: '2026-09-16T00:00:00Z'
description: BugSigDB is a community-editable database of manually curated microbial
  signatures from published differential abundance studies of host-associated microbiomes.
  Each signature lists the taxa reported as increased or decreased between two conditions
  and is annotated with study geography, health outcome, host body site and experimental,
  epidemiological and statistical methods using controlled vocabulary. The initial
  release held more than 2,500 signatures from more than 600 studies on three host
  species. The site is a Semantic MediaWiki. Data are exported hourly to GitHub and
  released periodically on Zenodo, and the bugsigdbr Bioconductor package gives access
  from R.
domains:
- biomedical
- microbiology
homepage_url: https://bugsigdb.org/
id: bugsigdb
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: BugSigDB
products:
- category: GraphicalInterface
  description: Semantic MediaWiki site for browsing, searching and curating published
    microbial signatures
  format: http
  id: bugsigdb.site
  name: BugSigDB web site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bugsigdb
  product_url: https://bugsigdb.org/
- category: Product
  description: Hourly export of all complete BugSigDB studies, experiments and signatures
    as a single CSV file, with signature identifiers added
  format: csv
  id: bugsigdb.full_dump
  name: BugSigDB full dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bugsigdb
  product_file_size: 3276228
  product_url: https://raw.githubusercontent.com/waldronlab/BugSigDBExports/main/full_dump.csv
  repository: https://github.com/waldronlab/BugSigDBExports
- category: Product
  description: Hourly exports of BugSigDB signatures as GMT gene-set files, one file
    per combination of taxonomic level (genus, species, mixed) and identifier type
    (NCBI Taxonomy, MetaPhlAn, taxon name)
  format: tsv
  id: bugsigdb.gmt
  name: BugSigDB signature GMT files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bugsigdb
  product_url: https://github.com/waldronlab/BugSigDBExports
  repository: https://github.com/waldronlab/BugSigDBExports
- category: Product
  description: Periodic manually reviewed stable data releases of BugSigDB on Zenodo,
    under the concept DOI 10.5281/zenodo.5606165
  format: csv
  id: bugsigdb.zenodo
  name: BugSigDB stable releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bugsigdb
  product_url: https://doi.org/10.5281/zenodo.5606165
- category: ProgrammingInterface
  description: bugsigdbr, an R/Bioconductor package for accessing published microbial
    signatures from BugSigDB
  format: http
  id: bugsigdb.bugsigdbr
  is_public: true
  name: bugsigdbr
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bugsigdb
  product_url: https://bioconductor.org/packages/bugsigdbr/
- category: ProgrammingInterface
  description: REST API and MCP server over the production MicroMap Neo4j graph, with
    endpoints for taxa, diseases, metabolites, drugs, genes, proteins, pathways, biomarker
    signatures, papers, cross-feeding networks, provenance and graph traversal. Access
    requires a Graphomics API key. The API application code is in the open-source
    repository.
  format: http
  id: micromap.api
  is_neo4j: true
  is_public: false
  name: MicroMap API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: micromap
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: disbiome
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: chembl
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: semmeddb
  - relation_type: prov:wasDerivedFrom
    source: gutmdisorder
  - relation_type: prov:wasDerivedFrom
    source: bugsigdb
  - relation_type: prov:wasDerivedFrom
    source: gmrepo
  - relation_type: prov:wasDerivedFrom
    source: mbodymap
  product_url: https://www.graphomics.com/docs
publications:
- authors:
  - Geistlinger L
  - Mirzayi C
  - Zohra F
  - Azhar R
  - Elsafoury S
  - Grieve C
  - Wokaty J
  - Gamboa-Tuz SD
  - Sengupta P
  - Hecht I
  - Ravikrishnan A
  - Gonçalves RS
  - Franzosa E
  - Raman K
  - Carey V
  - Dowd JB
  - Jones HE
  - Davis S
  - Segata N
  - Huttenhower C
  - Waldron L
  doi: 10.1038/s41587-023-01872-y
  id: https://www.ncbi.nlm.nih.gov/pubmed/37697152
  journal: Nat Biotechnol
  preferred: true
  title: BugSigDB captures patterns of differential abundance across a broad range
    of host-associated microbial signatures
  year: '2024'
repository: https://github.com/waldronlab/BugSigDB
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
---
BugSigDB is a curated database of microbial signatures from published
differential abundance studies. A signature is the set of taxa a study reported
as increased or decreased between two groups, with the study design, the host,
the body site and the outcome recorded in controlled vocabulary.

## Content

The Nature Biotechnology paper describes more than 2,500 signatures from more
than 600 studies on three host species. The database is community-editable and
grows past those numbers. Records are organized as studies, experiments and
signatures.

## Access

The wiki at https://bugsigdb.org/ is the curation interface. The
[BugSigDBExports](https://github.com/waldronlab/BugSigDBExports) repository
holds hourly exports: a full CSV dump and GMT files for each taxonomic level
and identifier type. Stable, manually reviewed releases are archived on Zenodo
under the concept DOI 10.5281/zenodo.5606165. The `bugsigdbr` package on
Bioconductor reads these exports from R.

The wiki returned HTTP 403 from the curation network on 2026-09-16 and I did
not read it directly. The export repository README and its `.zenodo.json`
metadata were the sources for this page.

## Licensing

The Zenodo metadata in the export repository declares CC-BY-4.0.

## Used by

[MicroMap](micromap) loads BugSigDB signatures as one of its association
sources.