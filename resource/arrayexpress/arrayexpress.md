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
  - relation_type: prov:hadPrimarySource
    source: biostudies
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
    source: biostudies
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
- category: Product
  description: FTP archive containing processed expression data files, experiment
    metadata, and analysis results for bulk RNA-seq experiments
  format: http
  id: expressionatlas.ftp-bulk
  name: Expression Atlas FTP (Bulk Data)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/
- category: Product
  description: Individual experiment data downloads in TSV format containing expression
    matrices and statistical results
  format: tsv
  id: expressionatlas.experiment-downloads
  name: Expression Atlas Experiment Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/gxa/download
- category: Product
  description: Normalized gene expression data and raw count matrices delivered as
    R SummarizedExperiment objects via the ExpressionAtlas Bioconductor package, which
    downloads and imports Expression Atlas experiment data into R for computational
    analysis
  format: mixed
  id: expressionatlas.r-objects
  name: Expression Atlas R Data Objects
  original_source:
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://bioconductor.org/packages/ExpressionAtlas/
- category: Product
  description: Baseline expression summary data across human tissues and cell types
    from GTEx, Human Protein Atlas and other major studies
  format: tsv
  id: expressionatlas.baseline-summary
  name: Expression Atlas Baseline Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/gxa/baseline/experiments
- category: Product
  description: Differential gene expression results across diseases, perturbations,
    and comparative studies with statistical significance metrics
  format: tsv
  id: expressionatlas.differential-results
  name: Expression Atlas Differential Results
  original_source:
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/gxa/experiments?experimentType=differential
- category: Product
  description: FTP/HTTPS archive of BioStudies study files, organized by accession
    prefix, including Europe PMC supplementary data and ArrayExpress experiment files.
  format: mixed
  id: biostudies.ftp
  name: BioStudies FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://ftp.ebi.ac.uk/pub/databases/biostudies/
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
- category: Product
  description: ArrayExpress record E-MTAB-797, Open TG-GATEs gene expression data from rat
    primary hepatocytes treated in vitro (Affymetrix Rat Genome 230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-in-vitro
  name: Open TG-GATEs in ArrayExpress (Rat In Vitro)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-797
- category: Product
  description: ArrayExpress record E-MTAB-798, Open TG-GATEs gene expression data from human
    primary hepatocytes treated in vitro (Affymetrix Human Genome U133 Plus 2.0).
  format: http
  id: open-tggates.arrayexpress-human-in-vitro
  name: Open TG-GATEs in ArrayExpress (Human In Vitro)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-798
- category: Product
  description: ArrayExpress record E-MTAB-799, Open TG-GATEs gene expression data from rat
    liver and kidney after single-dose in vivo exposure (Affymetrix Rat Genome 230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-single-dose
  name: Open TG-GATEs in ArrayExpress (Rat In Vivo Single Dose)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-799
- category: Product
  description: ArrayExpress record E-MTAB-800, Open TG-GATEs gene expression data from rat
    liver and kidney after repeated-dose in vivo exposure (Affymetrix Rat Genome 230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-repeat-dose
  name: Open TG-GATEs in ArrayExpress (Rat In Vivo Repeated Dose)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-800
publications:
- authors:
  - Ugis Sarkans
  - Anja Füllgrabe
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
  - Anja Füllgrabe
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
