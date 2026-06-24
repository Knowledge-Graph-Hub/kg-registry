---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.sanger.ac.uk/tool/gdsc-genomics-drug-sensitivity-cancer/
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
creation_date: '2025-05-28T00:00:00Z'
description: The Genomics of Drug Sensitivity in Cancer (GDSC) is a database and resource
  that characterizes cancer cell lines and their responses to anti-cancer drugs. It
  contains drug screening data for over 1000 cancer cell lines with hundreds of compounds,
  as well as genomic feature data such as mutations, copy number variations, methylation,
  and gene expression. The aim is to identify molecular features of cancers that predict
  response to anti-cancer drugs.
domains:
- biomedical
- drug discovery
- genomics
- pharmacology
homepage_url: https://www.sanger.ac.uk/tool/gdsc-genomics-drug-sensitivity-cancer/
id: gdsc
infores_id: gdsc
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.sanger.ac.uk/tool/gdsc-genomics-drug-sensitivity-cancer/
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
  - relation_type: prov:hadPrimarySource
    source: gdsc
  product_url: https://www.sanger.ac.uk/tool/gdsc-genomics-drug-sensitivity-cancer/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: GraphicalInterface
  description: Primary web portal for searching and browsing cancer pharmacogenomics
    data across multiple integrated datasets with interactive dose-response curve
    visualization
  format: http
  id: pharmacodb.portal
  name: PharmacoDB Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: https://pharmacodb.ca/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: ProgrammingInterface
  description: RESTful JSON API providing programmatic access to cell lines, compounds,
    tissues, datasets, experiments, and intersections data
  format: http
  id: pharmacodb.api
  is_public: true
  name: PharmacoDB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: http://api.pharmacodb.ca/v1/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: DocumentationProduct
  description: Comprehensive user documentation covering search functionality, datasets,
    tissues, cell lines, experiments, genes, compounds, and biomarker discovery features
  format: http
  id: pharmacodb.documentation
  name: PharmacoDB Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  product_url: https://pharmacodb.ca/documentation
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ccle
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: ctrp
- category: Product
  description: Drug screening data from various platforms including GDSC, PRISM, and
    CTD2
  format: csv
  id: depmap.drug_sensitivity
  name: DepMap Drug Sensitivity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: prism
  - relation_type: prov:wasDerivedFrom
    source: ctd2
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
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
  year: '2012'
- authors:
  - Iorio F
  - Knijnenburg TA
  - Vis DJ
  - Bignell GR
  - Menden MP
  - Schubert M
  - Aben N
  - "Gon\xE7alves E"
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
  doi: 10.1016/j.cell.2016.06.017
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
  doi: 10.1038/nature11005
  id: https://doi.org/10.1038/nature11005
  journal: Nature
  title: Systematic identification of genomic markers of drug sensitivity in cancer
    cells
  year: '2012'
repository: https://github.com/CancerRxGene
taxon:
- NCBITaxon:9606
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