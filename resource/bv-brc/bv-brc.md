---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.bv-brc.org/
  label: Bacterial and Viral Bioinformatics Resource Center
- category: Organization
  contact_details:
  - contact_type: email
    value: help@bv-brc.org
  label: BV-BRC Help Desk
description: The Bacterial and Viral Bioinformatics Resource Center (BV-BRC) is a
  comprehensive resource for bacterial and viral infectious disease research that
  combines the data, technology, and extensive user communities from two long-running
  centers - PATRIC (the bacterial system) and IRD/ViPR (the viral systems). BV-BRC
  provides integrated data, advanced bioinformatics tools, and workflows to support
  the scientific community in understanding and combating infectious diseases.
domains:
- microbiology
- genomics
- health
- biomedical
homepage_url: https://www.bv-brc.org/
id: bv-brc
layout: resource_detail
license:
  id: https://www.bv-brc.org/about
  label: Custom
name: Bacterial and Viral Bioinformatics Resource Center
products:
- category: GraphicalInterface
  description: Web-based interface providing access to BV-BRC data, tools, and services
  format: http
  id: bv-brc.site
  name: BV-BRC Web Interface
  product_url: https://www.bv-brc.org/
- category: ProgrammingInterface
  description: Application Programming Interface for programmatic access to BV-BRC
    data
  format: http
  id: bv-brc.api
  is_public: true
  name: BV-BRC Data API
  product_url: https://www.bv-brc.org/api/doc/
- category: ProcessProduct
  description: Command Line Interface for batch access to BV-BRC data and services
  format: http
  id: bv-brc.cli
  name: BV-BRC CLI
  product_url: https://www.bv-brc.org/docs/cli_tutorial/index.html
- category: Product
  description: FTP server providing direct access to BV-BRC data files
  format: http
  id: bv-brc.ftp
  name: BV-BRC FTP
  product_url: https://www.bv-brc.org/docs/quick_references/ftp.html
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
- category: Product
  description: Trait data table listing all 140+ harmonized traits available in metaTraits,
    mapped to standardized ontologies.
  id: metatraits.traits
  name: metaTraits Trait List
  original_source:
  - bacdive
  - bv-brc
  - goldterms
  - progenomes
  product_url: https://metatraits.embl.de/traits
publications:
- authors:
  - Olson RD
  - Assaf R
  - Brettin T
  - Conrad N
  - Cucinell C
  - Davis JJ
  - Dempsey DM
  - Dickerman A
  - Dietrich EM
  - Kenyon RW
  - Kuscuoglu M
  - Lefkowitz EJ
  - Lu J
  - Machi D
  - Macken C
  - Mao C
  - Niewiadomska A
  - Nguyen M
  - Olsen GJ
  - Overbeek JC
  - Parrello B
  - Parrello V
  - Porter JS
  - Pusch GD
  - Shukla M
  - Singh I
  - Stewart L
  - Tan G
  - Thomas C
  - VanOeffelen M
  - Vonstein V
  - Wallace ZS
  - Warren AS
  - Wattam AR
  - Xia F
  - Yoo H
  - Zhang Y
  - Zmasek CM
  - Scheuermann RH
  - Stevens RL
  doi: doi:10.1093/nar/gkac1003
  id: https://pubmed.ncbi.nlm.nih.gov/36350631/
  journal: Nucleic Acids Research
  preferred: true
  title: 'Introducing the Bacterial and Viral Bioinformatics Resource Center (BV-BRC):
    a resource combining PATRIC, IRD and ViPR'
  year: '2022'
repository: https://github.com/BV-BRC
taxon:
- NCBITaxon:2
- NCBITaxon:9606
---
## Overview

The Bacterial and Viral Bioinformatics Resource Center (BV-BRC) is an information system designed to support the biomedical research community's work on bacterial and viral infectious diseases via integration of vital pathogen information with rich data and analysis tools. BV-BRC combines the data, technology, and extensive user communities from two long-running centers: PATRIC, the bacterial system, and IRD/ViPR, the viral systems.

## Features

- Support for diverse bacterial and viral infectious disease research communities
- Integration of PATRIC and IRD/ViPR resources into a unified resource
- Unified data model, database, and real-time data integration processes
- Consistent and accurate genome annotations and other derived data types
- Automated and manual curation of high value data and metadata
- Integrated analysis of multi-omics systems biology data using visual analytics tools
- Phylogenomic and epidemiological analysis for rapid outbreak response
- Explainable AI/machine learning based tools
- Private user workspace for data analysis, sharing and publishing
- Programmatic and batch access via APIs, Command-line Interface (CLI), and FTP

## Data Content

BV-BRC includes hundreds of thousands of bacterial genomes from PATRIC and over a million viral genomes from IRD/ViPR. It also hosts data on protein structure and function, clinical studies, drug targets and resistance, epidemiology, and other features.

## History

BV-BRC was formed by combining two historically independent efforts: PATRIC (Pathosystems Resource Integration Center) for bacterial data and IRD/ViPR (Influenza Research Database/Virus Pathogen Resource) for viral data. It represents an evolution and integration of these previously separate resources.

BV-BRC is the successor to PATRIC, incorporating all of PATRIC's bacterial data and functionality while expanding to include viral data from IRD/ViPR. Researchers who previously used PATRIC for bacterial genomics and bioinformatics should now use BV-BRC as it contains all the data and tools from PATRIC plus additional resources and capabilities.