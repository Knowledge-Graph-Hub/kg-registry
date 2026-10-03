---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biostudies@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/biostudies/arrayexpress
  label: BioStudies team, EMBL-EBI
creation_date: '2026-10-03T00:00:00Z'
description: ArrayExpress is EMBL-EBI's archive of functional genomics experiments,
  holding raw and processed data and MIAME/MINSEQE-compliant metadata from microarray
  and high-throughput sequencing studies, including bulk and single-cell RNA-seq.
  Since 2021 it has been served as a collection within BioStudies, and its accessions
  keep the E-XXXX-n form. It is the European counterpart of NCBI GEO and supplies
  the experiments reanalyzed by Expression Atlas.
domains:
- genomics
- gene expression profiling
- single-cell analysis
- biological systems
homepage_url: https://www.ebi.ac.uk/biostudies/arrayexpress
id: arrayexpress
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: ArrayExpress
products:
- category: GraphicalInterface
  description: Searchable web interface for browsing ArrayExpress functional genomics
    studies, their sample and protocol metadata, and their data files.
  format: http
  id: arrayexpress.portal
  name: ArrayExpress Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search
  description: BioStudies REST API endpoint for searching ArrayExpress studies, returning
    JSON; per-study metadata and file listings are available from the BioStudies studies
    endpoints.
  format: http
  id: arrayexpress.api
  is_public: true
  name: ArrayExpress Search API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search
- category: Product
  description: FTP/HTTPS archive of ArrayExpress study files, organized by accession
    prefix, including IDF and SDRF (MAGE-TAB) metadata, raw data and processed data
    files.
  format: mixed
  id: arrayexpress.ftp
  name: ArrayExpress FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://ftp.ebi.ac.uk/pub/databases/biostudies/
- category: GraphicalInterface
  description: Annotare, the web-based submission tool for depositing microarray and
    sequencing experiments and their metadata into ArrayExpress.
  format: http
  id: arrayexpress.annotare
  name: Annotare Submission Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/fg/annotare/
- category: MappingProduct
  description: CSV files, one per database, linking Europe PMC articles to accessions
    text-mined from their full text, covering ArrayExpress, BioStudies, ChEBI, Cellosaurus,
    AlphaFold DB, BioProject, BioSample, BRENDA, CATH and others.
  format: csv
  id: europepmc.textmined-terms
  name: Europe PMC Text-Mined Database Accession Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://ftp.ebi.ac.uk/pub/databases/pmc/TextMinedTerms/
- category: Product
  description: Sample metadata for every organoid sample in OrganoidDB, with study
    and sample accessions, tissue, platform, species, PubMed ID and sample characteristics.
  format: csv
  id: organoiddb.all-organoid-samples
  name: OrganoidDB all organoid samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 3258002
  product_url: http://www.inbirg.com/organoid_db/download/all_org_samples
- category: Product
  description: Sample metadata for the organoid samples used by the OrganoidDB organoid
    specificity search.
  format: csv
  id: organoiddb.organoid-specificity-samples
  name: OrganoidDB organoid specificity samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 257601
  product_url: http://www.inbirg.com/organoid_db/download/org_specificity_samples
- category: Product
  description: Sample metadata for the primary tissue and cell line samples that OrganoidDB
    uses for comparison with organoids.
  format: csv
  id: organoiddb.general-samples
  name: OrganoidDB general samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 94026
  product_url: http://www.inbirg.com/organoid_db/download/general_samples
publications:
- authors:
  - Ugis Sarkans
  - "Anja F\xFCllgrabe"
  - Ahmed Ali
  - Awais Athar
  - Ehsan Behrangi
  - Nestor Diaz
  - Silvie Fexova
  - Nancy George
  - Haider Iqbal
  - Sandeep Kurri
  - Jhoan Munoz
  - Juan Rada
  - Irene Papatheodorou
  - Alvis Brazma
  doi: 10.1093/nar/gkaa1062
  id: doi:10.1093/nar/gkaa1062
  journal: Nucleic Acids Research
  preferred: true
  title: From ArrayExpress to BioStudies
  year: '2021'
- authors:
  - Awais Athar
  - "Anja F\xFCllgrabe"
  - Nancy George
  - Haider Iqbal
  - Laura Huerta
  - Ahmed Ali
  - Catherine Snow
  - Nuno A Fonseca
  - Robert Petryszak
  - Irene Papatheodorou
  - Ugis Sarkans
  - Alvis Brazma
  doi: 10.1093/nar/gky964
  id: doi:10.1093/nar/gky964
  journal: Nucleic Acids Research
  title: ArrayExpress update - from bulk to single-cell expression data
  year: '2019'
synonyms:
- AE
---
# ArrayExpress

ArrayExpress is EMBL-EBI's archive of functional genomics experiments. It holds raw
and processed data and MIAME/MINSEQE-compliant metadata from microarray and
high-throughput sequencing studies, including bulk and single-cell RNA-seq. It is the
European counterpart of NCBI GEO and supplies the experiments reanalyzed by Expression
Atlas.

Since 2021 ArrayExpress has been served as a collection within BioStudies. Accessions
keep the `E-XXXX-n` form (for example `E-MTAB-17130`). The BioStudies API reported
80,947 ArrayExpress studies on 2026-10-03.

## Access

- Web interface: https://www.ebi.ac.uk/biostudies/arrayexpress
- Search API: https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search
- Per-study info, including download links: `https://www.ebi.ac.uk/biostudies/api/v1/studies/<accession>/info`
- Files: https://ftp.ebi.ac.uk/pub/databases/biostudies/ (for example
  `E-MTAB-/130/E-MTAB-17130/Files/` holds the IDF, SDRF and processed data for
  E-MTAB-17130)
- Submissions: Annotare, https://www.ebi.ac.uk/fg/annotare/

## License

The site links the EMBL-EBI Terms of Use. Individual studies may carry their own
terms; no single data license is stated.
