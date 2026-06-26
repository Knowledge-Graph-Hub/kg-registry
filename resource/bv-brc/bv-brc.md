---
activity_status: active
category: DataSource
collection:
- ber
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
creation_date: '2025-05-28T00:00:00Z'
description: The Bacterial and Viral Bioinformatics Resource Center (BV-BRC) is a
  comprehensive resource for bacterial and viral infectious disease research that
  combines the data, technology, and extensive user communities from two long-running
  centers - PATRIC (the bacterial system) and IRD/ViPR (the viral systems). BV-BRC
  provides integrated data, advanced bioinformatics tools, and workflows to support
  the scientific community in understanding and combating infectious diseases.
domains:
- microbiology
- genomics
- biomedical
homepage_url: https://www.bv-brc.org/
id: bv-brc
last_modified_date: '2025-12-13T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/
- category: ProgrammingInterface
  description: Application Programming Interface for programmatic access to BV-BRC
    data
  format: http
  id: bv-brc.api
  is_public: true
  name: BV-BRC Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/api/doc/
- category: ProcessProduct
  description: Command Line Interface for batch access to BV-BRC data and services
  format: http
  id: bv-brc.cli
  name: BV-BRC CLI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/cli_tutorial/index.html
- category: Product
  description: FTP server providing direct access to BV-BRC data files
  format: http
  id: bv-brc.ftp
  name: BV-BRC FTP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/quick_references/ftp.html
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
  description: Trait data table listing all 140+ harmonized traits available in metaTraits,
    mapped to standardized ontologies.
  format: http
  id: metatraits.traits
  name: metaTraits Trait List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: goldterms
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:hadPrimarySource
    source: progenomes
  product_url: https://metatraits.embl.de/traits
- category: Product
  description: Family-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.family-summary
  name: metaTraits NCBI Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 913932
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.genus-summary
  name: metaTraits NCBI Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2431808
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.ncbi.species-summary
  name: metaTraits NCBI Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 6523019
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_species_summary_no_predictions.tsv.gz
- category: Product
  description: Family-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.family-summary
  name: metaTraits GTDB Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 1513013
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.genus-summary
  name: metaTraits GTDB Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 4965442
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.species-summary
  name: metaTraits GTDB Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 12570522
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_species_summary_no_predictions.tsv.gz
- category: GraphicalInterface
  description: BV-BRC web portal that hosts legacy PATRIC bacterial genomics data
    and tools alongside expanded viral resources
  format: http
  id: patric.web
  name: PATRIC/BV-BRC Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/
- category: Product
  description: Legacy PATRIC bacterial genome data and annotations now available through
    BV-BRC genome data views and services
  format: mixed
  id: patric.genomes
  name: PATRIC Genome Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/quick_start/data_functionality_overview.html
  warnings: []
- category: ProgrammingInterface
  description: BV-BRC REST Data API for querying and retrieving public data, including
    data inherited from PATRIC
  format: http
  id: patric.api
  name: BV-BRC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/system_documentation/system_architecture.html#data-api
- category: DocumentationProduct
  description: BV-BRC quick-start overview for PATRIC users, describing how legacy
    PATRIC data, tools, services, website, and infrastructure were incorporated into
    BV-BRC
  format: http
  id: patric.bv_brc_overview
  name: BV-BRC Overview for PATRIC Users
  original_source:
  - relation_type: prov:hadPrimarySource
    source: patric
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  product_url: https://www.bv-brc.org/docs/quick_start/data_functionality_overview.html
  warnings: []
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
  doi: 10.1093/nar/gkac1003
  id: https://pubmed.ncbi.nlm.nih.gov/36350631/
  journal: Nucleic Acids Res
  preferred: true
  title: 'Introducing the Bacterial and Viral Bioinformatics Resource Center (BV-BRC): a resource combining PATRIC, IRD and ViPR'
  year: '2023'
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