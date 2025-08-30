---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://pubchem.ncbi.nlm.nih.gov/contact
  label: National Center for Biotechnology Information (NCBI)
description: PubChem is an open chemistry database that collects information on chemical
  structures, identifiers, chemical and physical properties, biological activities,
  patents, health, safety, toxicity data, and other information.
domains:
- chemistry and biochemistry
- health
homepage_url: https://pubchem.ncbi.nlm.nih.gov/
id: pubchem
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: PubChem
products:
- category: Product
  compression: gzip
  description: Compound structures, properties, and other information in ASN.1 format
  format: xml
  id: pubchem.compounds.asn
  name: PubChem Compounds ASN
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/ASN/
  secondary_source:
  - pubchem
- category: Product
  compression: gzip
  description: Compound structures, properties, and other information in SDF format
  format: sdf
  id: pubchem.compounds.sdf
  name: PubChem Compounds SDF
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/
  secondary_source:
  - pubchem
- category: Product
  compression: gzip
  description: PubChem substance information in ASN.1 format
  format: xml
  id: pubchem.substances.asn
  name: PubChem Substances ASN
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/ASN/
  secondary_source:
  - pubchem
- category: Product
  compression: gzip
  description: PubChem substance information in SDF format
  format: sdf
  id: pubchem.substances.sdf
  name: PubChem Substances SDF
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/SDF/
  secondary_source:
  - pubchem
- category: Product
  compression: gzip
  description: PubChem BioAssay data in ASN.1 format
  format: xml
  id: pubchem.bioassay.asn
  name: PubChem BioAssay ASN
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/ASN/
  secondary_source:
  - pubchem
- category: Product
  compression: gzip
  description: PubChem BioAssay data in XML format
  format: xml
  id: pubchem.bioassay.xml
  name: PubChem BioAssay XML
  original_source:
  - pubchem
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/XML/
  secondary_source:
  - pubchem
- category: ProgrammingInterface
  description: The PubChem Power User Gateway (PUG) REST service
  id: pubchem.pug.rest
  is_public: true
  name: PubChem PUG REST API
  original_source:
  - pubchem
  product_url: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
  secondary_source:
  - pubchem
- category: GraphProduct
  compression: zip
  description: Nodes from PubChem Database
  format: csv
  id: biomarkerkg.nodes.compound
  name: BKG Compound Nodes
  original_source:
  - pubchem
  product_file_size: 871
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Compound.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
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
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
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
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
publications:
- authors:
  - Kim S
  - Chen J
  - Cheng T
  - Gindulyte A
  - He J
  - He S
  - Li Q
  - Shoemaker BA
  - Thiessen PA
  - Yu B
  - Zaslavsky L
  - Zhang J
  - Bolton EE
  doi: doi:10.1093/nar/gky1033
  id: doi:10.1093/nar/gky1033
  preferred: true
  title: PubChem 2019 update - improved access to chemical data
  year: '2019'
repository: https://github.com/ncbi/NCBI-Datasets
---
PubChem is a database of chemical molecules and their activities against biological assays maintained by the National Center for Biotechnology Information (NCBI), a component of the National Library of Medicine, which is part of the United States National Institutes of Health (NIH).

The system contains three primary databases:
- PubChem Substance: Contains more than 309 million records of chemical samples submitted by over 900 data sources
- PubChem Compound: Contains more than 114 million unique chemical structures derived from PubChem Substance
- PubChem BioAssay: Contains bioactivity results from over 1.3 million high-throughput screening programs

PubChem data is available through a web interface, programmatically via the PUG REST API, and as bulk downloads via FTP. The system supports structure searches, chemical property information, biological activities, safety and toxicity information, patents, literature citations, and links to related resources.

All PubChem data is in the public domain and can be freely downloaded and used for both commercial and non-commercial purposes.