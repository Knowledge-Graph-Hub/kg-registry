---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: bindingdb@gmail.com
  - contact_type: url
    value: https://www.bindingdb.org/rwd/bind/sendmail.jsp
  label: BindingDB
- category: Organization
  contact_details:
  - contact_type: url
    value: https://pharmacy.ucsd.edu/
  label: Skaggs School of Pharmacy and Pharmaceutical Sciences, University of California
    San Diego
description: BindingDB is a public, web-accessible database of measured binding affinities
  between small, drug-like molecules and protein targets, focusing on the interactions
  of proteins with small, drug-like molecules. It contains 3.0M data points for 1.3M
  compounds and 9.6K targets, serving as a crucial resource for drug discovery, pharmacology,
  and related fields.
domains:
- biomedical
- drug discovery
- chemistry and biochemistry
- pharmacology
fairsharing_id: FAIRsharing.3b36hk
homepage_url: https://www.bindingdb.org/rwd/bind/index.jsp
id: bindingdb
layout: resource_detail
license:
  id: https://www.bindingdb.org/rwd/bind/info.jsp
  label: CC BY 4.0
name: BindingDB
products:
- category: Product
  compression: zip
  description: Full dataset containing all binding measurements in BindingDB with
    2D compound structures
  format: sdf
  id: bindingdb.all_2d
  name: BindingDB All Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_All_2D_202507_sdf.zip
- category: Product
  compression: zip
  description: Full dataset containing all binding measurements in BindingDB with
    3D compound structures
  format: sdf
  id: bindingdb.all_3d
  name: BindingDB All Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_All_3D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Full dataset containing all binding measurements in BindingDB in tab-separated
    values format
  format: tsv
  id: bindingdb.all_tsv
  name: BindingDB All Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_All_202507_tsv.zip
- category: Product
  compression: zip
  description: Data curated from articles by BindingDB with 2D compound structures
  format: sdf
  id: bindingdb.articles_2d
  name: BindingDB Articles Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_BindingDB_Articles_2D_202507_sdf.zip
- category: Product
  compression: zip
  description: Data curated from articles by BindingDB with 3D compound structures
  format: sdf
  id: bindingdb.articles_3d
  name: BindingDB Articles Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_BindingDB_Articles_3D_202507_sdf.zip
- category: Product
  compression: zip
  description: Data curated from articles by BindingDB in tab-separated values format
  format: tsv
  id: bindingdb.articles_tsv
  name: BindingDB Articles Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_BindingDB_Articles_202507_tsv.zip
- category: Product
  compression: zip
  description: Data in BindingDB drawn from ChEMBL with 2D compound structures
  format: sdf
  id: bindingdb.chembl_2d
  name: BindingDB ChEMBL Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_ChEMBL_2D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from ChEMBL with 3D compound structures
  format: sdf
  id: bindingdb.chembl_3d
  name: BindingDB ChEMBL Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_ChEMBL_3D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from ChEMBL in tab-separated values format
  format: tsv
  id: bindingdb.chembl_tsv
  name: BindingDB ChEMBL Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_ChEMBL_202507_tsv.zip
- category: Product
  compression: zip
  description: Data in BindingDB drawn from Patents with 2D compound structures
  format: sdf
  id: bindingdb.patents_2d
  name: BindingDB Patents Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Patents_2D_202507_sdf.zip
- category: Product
  compression: zip
  description: Data in BindingDB drawn from Patents with 3D compound structures
  format: sdf
  id: bindingdb.patents_3d
  name: BindingDB Patents Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Patents_3D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from Patents in tab-separated values format
  format: tsv
  id: bindingdb.patents_tsv
  name: BindingDB Patents Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Patents_202507_tsv.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from PubChem with 2D compound structures
  format: sdf
  id: bindingdb.pubchem_2d
  name: BindingDB PubChem Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_PubChem_2D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from PubChem with 3D compound structures
  format: sdf
  id: bindingdb.pubchem_3d
  name: BindingDB PubChem Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_PubChem_3D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: Data in BindingDB drawn from PubChem in tab-separated values format
  format: tsv
  id: bindingdb.pubchem_tsv
  name: BindingDB PubChem Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_PubChem_202507_tsv.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: COVID-19 related binding data with 2D compound structures
  format: sdf
  id: bindingdb.covid19_2d
  name: BindingDB COVID-19 Data (2D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Covid-19_2D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: COVID-19 related binding data with 3D compound structures
  format: sdf
  id: bindingdb.covid19_3d
  name: BindingDB COVID-19 Data (3D structures)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Covid-19_3D_202507_sdf.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  compression: zip
  description: COVID-19 related binding data in tab-separated values format
  format: tsv
  id: bindingdb.covid19_tsv
  name: BindingDB COVID-19 Data (TSV)
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/downloads/BindingDB_Covid-19_202507_tsv.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: Product
  description: FASTA format protein sequences of all protein targets in BindingDB
  format: fasta
  id: bindingdb.target_sequences
  name: BindingDB Target Sequences
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDBTargetSequences.fasta
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: MappingProduct
  description: Mapping of BindingDB monomer (compound) IDs to PubChem CIDs
  id: bindingdb.cid_mapping
  name: BindingDB-PubChem CID Mapping
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDB_CID.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: MappingProduct
  description: Mapping of BindingDB monomer (compound) IDs to PubChem SIDs
  id: bindingdb.sid_mapping
  name: BindingDB-PubChem SID Mapping
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDB_SID.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: MappingProduct
  description: Mapping of BindingDB monomer (compound) IDs to ChEBI IDs
  id: bindingdb.chebi_mapping
  name: BindingDB-ChEBI Mapping
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDB_CHEBI_ID.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: MappingProduct
  description: Mapping of BindingDB monomer (compound) IDs to DrugBank IDs
  id: bindingdb.drugbank_mapping
  name: BindingDB-DrugBank Mapping
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDB_DrugBankID.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: MappingProduct
  description: Mapping of BindingDB polymer (single protein) IDs to UniProt IDs
  id: bindingdb.uniprot_mapping
  name: BindingDB-UniProt Mapping
  product_url: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?download_file=/rwd/bind/BindingDB_UniProt.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
- category: ProgrammingInterface
  description: RESTful web services for programmatic access to BindingDB data
  id: bindingdb.api
  name: BindingDB RESTful API
  product_url: https://www.bindingdb.org/rwd/bind/BindingDBRESTfulAPI.jsp
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
  - gwas-catalog
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
publications:
- authors:
  - Tiqing Liu
  - Linda Hwang
  - Stephen K Burley
  - Carmen I Nitsche
  - Christopher Southan
  - W Patrick Walters
  - Michael K Gilson
  doi: 10.1093/nar/gkae1075
  id: doi:10.1093/nar/gkae1075
  journal: Nucleic Acids Research
  title: 'BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding
    data'
  year: '2025'
---
# BindingDB

BindingDB is a public, web-accessible database of measured binding affinities between small, drug-like molecules and protein targets. As the first public molecular recognition database, BindingDB supports research, education, and practice in drug discovery, pharmacology, and related fields.

## Database Content

BindingDB contains approximately:
- 3.0 million binding data measurements
- 1.3 million unique compounds
- 9.6 thousand protein targets

Of these, approximately 1.5 million measurements for 695,000 compounds and 4,700 targets were directly curated by BindingDB curators from scientific literature and patents.

## Data Sources

BindingDB integrates data from multiple sources:
- Articles curated directly by BindingDB staff
- US Patents (7,942 patents curated as of 2025)
- ChEMBL database
- PubChem
- PDSP Ki Database
- CSAR dataset
- Data from specialized labs

## Data Curation

BindingDB curates data from:
1. **US Patents**: Patents back to 2013 are included, containing 1.2+ million binding measurements across 599,874 compounds and 2,931 target proteins.
2. **Scientific Literature**: Selected journals are systematically curated, including:
   - ACS Chemical Biology
   - Biochemistry
   - ChemBioChem
   - Journal of Biological Chemistry
   - Nature Chemical Biology
   - And many others

## Data Access

The data is available through:
- Web interface for browsing and searching
- Downloadable datasets in multiple formats (SDF, TSV)
- RESTful API for programmatic access
- KNIME workflows for data retrieval and target prediction
- Browser extension (BDBFind) that integrates with scientific literature

## Special Features

- COVID-19 related binding data collection
- Target protein sequences in FASTA format
- Compound ID mappings to external databases (PubChem, ChEBI, DrugBank)
- Validation sets for computational methods
- Docked complex structures