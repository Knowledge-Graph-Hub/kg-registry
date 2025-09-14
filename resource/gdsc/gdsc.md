---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.cancerrxgene.org/
  label: Genomics of Drug Sensitivity in Cancer Project
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.sanger.ac.uk/
  label: Wellcome Sanger Institute
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.massgeneral.org/cancer/
  label: Massachusetts General Hospital Cancer Center
description: The Genomics of Drug Sensitivity in Cancer (GDSC) is a database and resource
  that characterizes cancer cell lines and their responses to anti-cancer drugs. It
  contains drug screening data for over 1000 cancer cell lines with hundreds of compounds,
  as well as genomic feature data such as mutations, copy number variations, methylation,
  and gene expression. The aim is to identify molecular features of cancers that predict
  response to anti-cancer drugs.
domains:
- biomedical
- health
- drug discovery
- genomics
- pharmacology
homepage_url: https://www.cancerrxgene.org/
id: gdsc
layout: resource_detail
license:
  id: https://www.cancerrxgene.org/legal
  label: Custom (non-commercial research use)
name: Genomics of Drug Sensitivity in Cancer
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing GDSC data including cell lines,
    compounds, and genomic features
  format: http
  id: gdsc.site
  name: GDSC Web Interface
  original_source:
  - gdsc
  product_url: https://www.cancerrxgene.org/
- category: Product
  description: Drug sensitivity data including IC50 values for cancer cell lines
  format: csv
  id: gdsc.drug_data
  name: GDSC Drug Sensitivity Data
  original_source:
  - gdsc
  product_url: https://www.cancerrxgene.org/downloads/drug_data
- category: Product
  description: ANOVA analysis results of associations between drug sensitivity and
    genomic features
  format: csv
  id: gdsc.anova
  name: GDSC ANOVA Results
  original_source:
  - gdsc
  product_url: https://www.cancerrxgene.org/downloads/anova
- category: Product
  description: Genetic feature data including mutations, copy number variations, gene
    expression, and methylation
  format: csv
  id: gdsc.genetic_features
  name: GDSC Genetic Features
  original_source:
  - gdsc
  product_url: https://www.cancerrxgene.org/downloads/genetic_features
- category: Product
  description: FTP repository with all GDSC data releases and archives
  format: csv
  id: gdsc.ftp
  name: GDSC FTP Data Repository
  original_source:
  - gdsc
  product_url: https://ftp.sanger.ac.uk/project/cancerrxgene/releases/
  warnings:
  - File was not able to be retrieved when checked on 2025-09-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-14: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
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
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- authors:
  - Yang W
  - Soares J
  - Greninger P
  - Edelman EJ
  - Lightfoot H
  - Forbes S
  - Bindal N
  - Beare D
  - Smith JA
  - Thompson IR
  - Ramaswamy S
  - Futreal PA
  - Haber DA
  - Stratton MR
  - Benes C
  - McDermott U
  - Garnett MJ
  doi: doi:10.1093/nar/gks1111
  id: http://doi.org/10.1093/nar/gks1111
  journal: Nucleic Acids Research
  preferred: true
  title: 'Genomics of Drug Sensitivity in Cancer (GDSC): a resource for therapeutic
    biomarker discovery in cancer cells'
  year: '2013'
- authors:
  - Iorio F
  - Knijnenburg TA
  - Vis DJ
  - Bignell GR
  - Menden MP
  - Schubert M
  - Aben N
  - Gonçalves E
  - Barthorpe S
  - Lightfoot H
  - Cokelaer T
  - Greninger P
  - van Dyk E
  - Chang H
  - de Silva H
  - Heyn H
  - Deng X
  - Egan RK
  - Liu Q
  - Mironenko T
  - Mitropoulos X
  - Richardson L
  - Wang J
  - Zhang T
  - Moran S
  - Sayols S
  - Soleimani M
  - Tamborero D
  - Lopez-Bigas N
  - Ross-Macdonald P
  - Esteller M
  - Gray NS
  - Haber DA
  - Stratton MR
  - Benes CH
  - Wessels LFA
  - Saez-Rodriguez J
  - McDermott U
  - Garnett MJ
  id: https://doi.org/10.1016/j.cell.2016.06.017
  journal: Cell
  title: A landscape of pharmacogenomic interactions in cancer
  year: '2016'
- authors:
  - Garnett MJ
  - Edelman EJ
  - Heidorn SJ
  - Greenman CD
  - Dastur A
  - Lau KW
  - Greninger P
  - Thompson IR
  - Luo X
  - Soares J
  - Liu Q
  - Iorio F
  - Surdez D
  - Chen L
  - Milano RJ
  - Bignell GR
  - Tam AT
  - Davies H
  - Stevenson JA
  - Barthorpe S
  - Lutz SR
  - Kogera F
  - Lawrence K
  - McLaren-Douglas A
  - Mitropoulos X
  - Mironenko T
  - Thi H
  - Richardson L
  - Zhou W
  - Jewitt F
  - Zhang T
  - O'Brien P
  - Boisvert JL
  - Price S
  - Hur W
  - Yang W
  - Deng X
  - Butler A
  - Choi HG
  - Chang JW
  - Baselga J
  - Stamenkovic I
  - Engelman JA
  - Sharma SV
  - Delattre O
  - Saez-Rodriguez J
  - Gray NS
  - Settleman J
  - Futreal PA
  - Haber DA
  - Stratton MR
  - Ramaswamy S
  - McDermott U
  - Benes CH
  id: https://doi.org/10.1038/nature11005
  journal: Nature
  title: Systematic identification of genomic markers of drug sensitivity in cancer
    cells
  year: '2012'
repository: https://github.com/CancerRxGene
---
## Overview

The Genomics of Drug Sensitivity in Cancer (GDSC) is a major collaboration between the Cancer Genome Project at the Wellcome Sanger Institute (UK) and the Center for Molecular Therapeutics at Massachusetts General Hospital Cancer Center (USA). The project aims to discover therapeutic biomarkers that can help identify patients most likely to respond to different anti-cancer drugs.

## Features

- Drug sensitivity data for over 1000 human cancer cell lines
- Screening results for hundreds of anti-cancer compounds
- Comprehensive genomic characterization of cell lines
- Statistical associations between genomic features and drug sensitivity
- Web interface for browsing and analyzing data
- Download options for all datasets
- Regular updates with new data releases

## Data Content

GDSC contains several key types of data:

1. **Drug screening data:** IC50 values and dose-response curves for cancer cell lines treated with different compounds
2. **Genomic features:** Mutations, copy number variations, gene expression, and methylation data for cancer cell lines
3. **Statistical analyses:** ANOVA results showing associations between genomic features and drug responses
4. **Annotations:** Detailed information about cell lines and compounds

## History

The GDSC database was established as part of the Cancer Genome Project at the Wellcome Sanger Institute. The first major publication describing the resource was released in 2012, with subsequent updates expanding the dataset and refining the analytical methods. The current version (Release 8.5, October 2023) includes data for 970 cell lines in GDSC1 and 969 cell lines in GDSC2, with a total of over 576,000 dose-response curves.