---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: lincs-help@broadinstitute.org
  id: broad
  label: Broad Institute LINCS Transcriptomics Center
creation_date: '2025-01-08T00:00:00Z'
description: The LINCS L1000 is a high-throughput, reduced representation gene expression
  profiling assay developed as part of the NIH Library of Integrated Network-Based
  Cellular Signatures (LINCS) Program. L1000 directly measures 978 landmark genes
  and computationally infers the expression of 11,350 additional genes, enabling cost-effective
  large-scale transcriptional profiling at approximately $2 per sample. The technology
  was developed to create a Connectivity Map (CMap) that catalogs cellular responses
  to genetic and chemical perturbations, facilitating drug discovery, mechanism of
  action determination, and functional annotation of genetic variants. The LINCS L1000
  dataset comprises over 1.3 million gene expression profiles representing responses
  to 19,811 chemical compounds, genetic perturbations targeting 5,075 genes (via shRNA
  knockdowns and cDNA overexpression), and 314 biologics across multiple cell lines
  and time points.
domains:
- drug discovery
homepage_url: https://lincsproject.org/LINCS/
id: lincs-l1000
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: LINCS L1000
products:
- category: GraphicalInterface
  description: The Connectivity Map (CMap) database containing over 1.3 million L1000
    gene expression profiles from chemical, genetic, and biologic perturbations. Includes
    web-based analysis tools for signature search and perturbagen class discovery.
  format: http
  id: lincs-l1000.cmap
  name: LINCS Connectivity Map (CMap)
  product_url: https://clue.io
- category: GraphicalInterface
  description: The CLUE platform provides interactive analysis tools and data access
    for the LINCS L1000 Connectivity Map dataset, including query tools, visualization,
    and APIs for programmatic access.
  format: http
  id: lincs-l1000.clue
  name: CLUE Platform
  product_url: https://clue.io
- category: Product
  description: LINCS L1000 data deposited in the Gene Expression Omnibus, including
    raw and processed gene expression data at multiple levels of preprocessing for
    all 1.3+ million profiles.
  format: http
  id: lincs-l1000.geo
  name: LINCS L1000 GEO Dataset
  product_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742
  warnings:
  - 'File was not able to be retrieved when checked on 2025-11-19: Timeout connecting
    to URL'
  - File was not able to be retrieved when checked on 2025-11-10_ Timeout connecting
    to URL
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Subramanian, A.
  - Narayan, R.
  - Corsello, S.M.
  - Peck, D.D.
  - Natoli, T.E.
  - Lu, X.
  - Gould, J.
  - Davis, J.F.
  - Tubelli, A.A.
  - Asiedu, J.K.
  - Lahr, D.L.
  - Hirschman, J.E.
  - Liu, Z.
  - Donahue, M.
  - Julian, B.
  - Khan, M.
  - Wadden, D.
  - Smith, I.C.
  - Lam, D.
  - Liberzon, A.
  - Toder, C.
  - Bagul, M.
  - Orzechowski, M.
  - Enache, O.M.
  - Piccioni, F.
  - Johnson, S.A.
  - Lyons, N.J.
  - Berger, A.H.
  - Shamji, A.F.
  - Brooks, A.N.
  - Vrcic, A.
  - Flynn, C.
  - Rosains, J.
  - Takeda, D.Y.
  - Hu, R.
  - Davison, D.
  - Lamb, J.
  - Ardlie, K.
  - Hogstrom, L.
  - Greenside, P.
  - Gray, N.S.
  - Clemons, P.A.
  - Silver, S.
  - Wu, X.
  - Zhao, W.N.
  - Read-Button, W.
  - Wu, X.
  - Haggarty, S.J.
  - Ronco, L.V.
  - Boehm, J.S.
  - Schreiber, S.L.
  - Doench, J.G.
  - Bittker, J.A.
  - Root, D.E.
  - Wong, B.
  - Golub, T.R.
  doi: 10.1016/j.cell.2017.10.049
  id: lincs_l1000_paper
  journal: Cell
  preferred: true
  title: 'A Next Generation Connectivity Map: L1000 platform and the first 1,000,000
    profiles'
  year: '2017'
repository: https://github.com/cmap/l1000-jupyter
taxon:
- NCBITaxon:9606
---

## Overview

The LINCS L1000 platform represents a major advance in high-throughput transcriptional profiling technology. By measuring only 978 carefully selected "landmark" genes and using computational inference for the remaining transcriptome, L1000 achieves dramatic cost reduction (approximately $2 per sample) while maintaining high reproducibility and comparability to RNA-seq. This breakthrough enabled the generation of over 1.3 million gene expression profiles as part of the NIH LINCS Program, creating one of the largest publicly available transcriptional profiling resources.

## Key Features

### Technology
- **Landmark genes**: 978 directly measured genes selected through data-driven analysis of 12,000+ microarray profiles
- **Inferred genes**: 11,350 genes computationally inferred with 81% showing high accuracy
- **Platform**: Ligation-mediated amplification (LMA) with Luminex bead-based detection
- **Cost**: Approximately $2 per profile (vs. traditional microarrays or RNA-seq)
- **Reproducibility**: >88% of technical replicates show Spearman correlation >0.9
- **Validation**: Highly comparable to RNA-seq (median cross-platform correlation 0.84)

### Dataset Composition (CMap-L1000v1)
- **1,319,138 L1000 profiles** comprising:
  - **19,811 small molecule compounds** (drugs, tool compounds, screening libraries)
  - **18,493 shRNAs** targeting 5,075 genes for loss-of-function studies
  - **3,462 cDNAs** for gain-of-function studies
  - **314 biologics**
  - **473,647 signatures** (consolidating biological replicates)
  
- **Cell line coverage**:
  - 9 core cancer cell lines (Touchstone reference dataset)
  - Up to 77 cell lines for Discovery dataset
  - Includes neuronal cell types (NPCs and differentiated neurons)

- **Time points**: 6h and 24h for chemical perturbations, 96h for genetic perturbations

### Applications
- **Drug discovery**: Mechanism of action (MOA) determination, off-target effect identification
- **Compound annotation**: Functional classification of uncharacterized molecules via connectivity to Perturbagen Classes (PCLs)
- **Genetic variant interpretation**: Assess functional impact of disease-associated alleles (e.g., FBXW7, KEAP1, PTEN)
- **Clinical trial analysis**: Evaluate target engagement and identify resistance mechanisms
- **Connectivity mapping**: Discover relationships between genes, drugs, and disease states through gene expression signatures
- **Bioactivity screening**: Identify transcriptionally active compounds from screening libraries

## Data Access and Tools

### Primary Data Portals
- **CLUE Platform** (https://clue.io): Interactive analysis tools, signature search, data downloads, and APIs
- **GEO** (GSE92742): Raw and processed data at multiple preprocessing levels
- **GitHub** (https://github.com/cmap/cmapM): Pre-processing code and tools

### Additional LINCS Resources
- **SigCom LINCS** (https://maayanlab.cloud/sigcom-lincs): Search across 1.5M+ signatures
- **L1000FWD** (https://maayanlab.cloud/L1000FWD/): L1000 Characteristic Direction Signature Search Engine
- **iLINCS** (http://www.ilincs.org): Integrated LINCS data portal
- **LINCS Data Portal** (http://lincsportal.ccs.miami.edu/dcic-portal/): DCIC data coordination center

### Data Levels
1. **Level 1**: Raw bead count and fluorescence intensity
2. **Level 2**: Deconvoluted data (assigning expression to two genes per bead color)
3. **Level 3**: Normalized data (LISS + quantile normalization) with inferred gene expression
4. **Level 4**: Differential expression (z-scores)
5. **Level 5**: Replicate-consensus signatures

## Methodology Highlights

### Perturbagen Classes (PCLs)
171 high-confidence Perturbagen Classes have been defined, representing groups of perturbagens with shared mechanisms. These include:
- 92 compound classes (e.g., HDAC inhibitors, kinase inhibitors)
- 60 loss-of-function gene classes
- 17 gain-of-function gene classes

PCLs enhance interpretability by aggregating similar perturbagens to strengthen on-target signals while diminishing off-target effects.

### Consensus Gene Signatures (CGS)
To mitigate strong off-target effects of shRNAs (where seed sequence effects often exceed on-target effects), a Consensus Gene Signature algorithm was developed that identifies consistent gene expression changes across multiple shRNAs targeting the same gene.

### Query Methodology
The Connectivity Map uses a weighted connectivity score (WTCS) approach similar to Gene Set Enrichment Analysis, computing similarity between query gene signatures and database signatures. Results are normalized and summarized across cell lines using quantile-based metrics (τ scores) to identify robust connections.

## Key Publications and Citations

**Primary Reference**:
- Subramanian A, Narayan R, Corsello SM, et al. A Next Generation Connectivity Map: L1000 platform and the first 1,000,000 profiles. *Cell*. 2017;171(6):1437-1452.e17. doi:10.1016/j.cell.2017.10.049

**Additional Resources**:
- Original Connectivity Map concept: Lamb J, et al. The Connectivity Map: using gene-expression signatures to connect small molecules, genes, and disease. *Science*. 2006;313(5795):1929-1935.
- Detailed protocols: https://clue.io/sop-L1000.pdf
- Connectopedia knowledge base: https://clue.io/connectopedia

## Funding

Supported by NIH grants including 5U54HG006093, U54HG008699, and 5U01HG008699 as part of the NIH Common Fund LINCS Program.