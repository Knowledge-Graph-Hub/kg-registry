---
activity_status: active
category: DataSource
creation_date: '2025-06-27T00:00:00Z'
description: UK Biobank is a large-scale biomedical database and research resource
  containing genetic, lifestyle and health information from half a million UK participants,
  designed to improve the prevention, diagnosis and treatment of a wide range of serious
  and life-threatening illnesses.
domains:
- biomedical
- genomics
- clinical
- phenotype
- genome-wide association studies
homepage_url: https://www.ukbiobank.ac.uk/
id: ukbiobank
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ukbiobank.ac.uk/terms-and-conditions/
  label: UK Biobank Data Access Agreement
name: UK Biobank
products:
- category: GraphicalInterface
  description: The UK Biobank Data Showcase provides summary statistics of all UK
    Biobank data and allows researchers to identify variables for inclusion in research
    applications.
  format: http
  id: ukbiobank.showcase
  name: UK Biobank Data Showcase
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  product_url: https://biobank.ndph.ox.ac.uk/showcase/
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  format: http
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
- category: Product
  description: Dryad archive for PRS Atlas results, including PRS association results
    at P less than 5e-05 and P less than 5e-08 thresholds
  format: http
  id: prsatlas.dryad
  name: PRS Atlas Dryad Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.h18c66b
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
- category: Product
  description: PRS Atlas results using the P less than 5e-05 polygenic risk score
    threshold, archived by Dryad
  format: txt
  id: prsatlas.results_5e05
  name: PRS Atlas Results P less than 5e-05
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/downloads/file_stream/83029
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
  warnings: []
- category: Product
  description: PRS Atlas results using the P less than 5e-08 polygenic risk score
    threshold, archived by Dryad
  format: txt
  id: prsatlas.results_5e08
  name: PRS Atlas Results P less than 5e-08
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/downloads/file_stream/83030
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
  warnings: []
- category: GraphProduct
  description: Neo4j construction artifacts for CardioKG, including Cypher scripts
    to create graph nodes and add edges. The GitHub repository is no longer available;
    these files are inside the archived Zenodo snapshot.
  dump_format: neo4j
  format: neo4j
  id: cardiokg.neo4j
  name: CardioKG Neo4j graph construction scripts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cardiokg
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: mondo
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: uniprot
  - relation_type: prov:used
    source: string
  - relation_type: prov:used
    source: opentargets
  product_url: https://doi.org/10.5281/zenodo.16025953
- category: Product
  description: CardioKG supporting data tables for anatomy and cardiac magnetic resonance
    anatomy mappings. The GitHub repository is no longer available; these files are
    inside the archived Zenodo snapshot.
  format: csv
  id: cardiokg.data
  name: CardioKG supporting data tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cardiokg
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  product_url: https://doi.org/10.5281/zenodo.16025953
- category: Product
  description: Downloadable Enrichr gene set libraries (more than 200 libraries across
    transcription, pathways, ontologies, diseases/drugs, cell types, crowd-contributed,
    and legacy categories), each retrievable as a GMT-style tab-delimited text file
    via the geneSetLibrary endpoint (e.g. geneSetLibrary?mode=text&libraryName=KEGG_2021_Human).
    Libraries are compiled from external databases including GO, KEGG, Reactome, WikiPathways,
    MSigDB, ChEA/ENCODE, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, OMIM, GWAS Catalog,
    HPO, MGI, CellMarker, and others.
  format: txt
  id: enrichr.libraries
  name: Enrichr Gene Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://maayanlab.cloud/Enrichr/#libraries
- category: GraphicalInterface
  description: OxO2 web interface for searching and browsing ontology cross-references
    and SSSOM mappings, including asserted mappings from OLS ontologies and curated
    mapping sets, plus inferred cross-set mappings
  format: http
  id: oxo.portal
  name: OxO Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/spot/oxo/api/v2
  description: OxO2 REST API (OpenAPI 3) for querying mappings, mapping sets, and
    ontologies; supports SSSOM-shaped JSON and SSSOM TSV export of mapping search
    results. Also exposes legacy OxO v1-compatible endpoints.
  format: http
  id: oxo.api
  is_public: true
  name: OxO2 REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/swagger-ui.html
publications:
- authors:
  - Clare Bycroft
  - Colin Freeman
  - Desislava Petkova
  - Gavin Band
  - Lloyd T. Elliott
  - Kevin Sharp
  - Allan Motyer
  - Damjan Vukcevic
  - Olivier Delaneau
  - Jared O'Connell
  - Adrian Cortes
  - Samantha Welsh
  - Alan Young
  - Mark Effingham
  - Gil McVean
  - Stephen Leslie
  - Naomi Allen
  - Peter Donnelly
  - Jonathan Marchini
  doi: 10.1038/s41586-018-0579-z
  id: doi:10.1038/s41586-018-0579-z
  journal: Nature
  title: The UK Biobank resource with deep phenotyping and genomic data
  year: '2018'
- authors:
  - Cathie Sudlow
  - John Gallacher
  - Naomi Allen
  - Valerie Beral
  - Paul Burton
  - John Danesh
  - Paul Downey
  - Paul Elliott
  - Jane Green
  - Martin Landray
  - Bette Liu
  - Paul Matthews
  - Giok Ong
  - Jill Pell
  - Alan Silman
  - Alan Young
  - Tim Sprosen
  - Tim Peakman
  - Rory Collins
  doi: 10.1371/journal.pmed.1001779
  id: doi:10.1371/journal.pmed.1001779
  journal: PLOS Medicine
  title: 'UK Biobank: An Open Access Resource for Identifying the Causes of a Wide
    Range of Complex Diseases of Middle and Old Age'
  year: '2015'
taxon:
- NCBITaxon:9606
---
# UK Biobank

UK Biobank is a large-scale biomedical database and research resource, containing in-depth genetic and health information from half a million UK participants. The database is regularly augmented with additional data and is globally accessible to approved researchers undertaking vital research into the most common and life-threatening diseases.

## Overview

UK Biobank recruited 500,000 people aged between 40-69 years in 2006-2010 from across the UK. With their consent, they provided detailed information about their lifestyle, physical measures, and had blood, urine and saliva samples collected and stored for future analysis. UK Biobank's database is a major contributor to the advancement of modern medicine and treatment and has enabled several scientific discoveries that improve human health.

## Data Resources

UK Biobank contains an unprecedented wealth of biological data, including:

- **Genotyping data** for all 500,000 participants
- **Whole exome sequencing** data for 200,000 participants
- **Whole genome sequencing** data for 200,000 participants
- **Health-related outcomes** via linkage to electronic health records
- **Imaging data** (brain, heart, body) for 100,000 participants
- **Extensive phenotype data** including physical measurements, biomarkers, and questionnaire data

## Access Model

UK Biobank is not an open access resource - researchers must apply for access and their institutions must sign a Material Transfer Agreement. However, it is designed to be widely accessible to bona fide researchers for health-related research that is in the public interest. The application process includes:

1. Registration with UK Biobank
2. Submission of a research application
3. Payment of access fees (which vary depending on the institution type)
4. Approval by UK Biobank's Access Committee

## Impact on Knowledge Graphs

While UK Biobank data itself is not openly available as downloadable products, it has been utilized in the creation of numerous derived knowledge graphs and resources. It serves as a critical source for:

- Genotype-phenotype association studies
- Risk prediction models
- Biomarker discovery
- Drug target validation
- Clinical decision support systems

## Related Resources

UK Biobank data has been used by numerous projects that have then made their derivative analyses publicly available, including:

- PheWAS (Phenome-Wide Association Studies) catalogs
- GWAS (Genome-Wide Association Studies) summaries
- Polygenic risk scores
- Various disease prediction models

## More Information

For more detailed information about UK Biobank, visit:
- [UK Biobank Website](https://www.ukbiobank.ac.uk/)
- [Data Showcase](https://biobank.ndph.ox.ac.uk/showcase/)
- [Access Application Process](https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access)