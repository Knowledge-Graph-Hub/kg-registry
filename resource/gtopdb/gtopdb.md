---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: enquiries@guidetopharmacology.org
  label: Guide to Pharmacology Help Desk
- category: Individual
  contact_details:
  - contact_type: email
    value: jamie.davies@ed.ac.uk
  label: Jamie Davies
description: The IUPHAR/BPS Guide to PHARMACOLOGY is an expert-curated resource providing
  quantitative information on drug targets and the substances that act on them, including
  approved drugs and experimental therapeutics
domains:
- pharmacology
- health
- biomedical
- drug discovery
- translational
homepage_url: https://www.guidetopharmacology.org
id: gtopdb
infores_id: gtopdb
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: Guide to Pharmacology
products:
- category: GraphicalInterface
  description: A web-based interface for accessing and browsing drug target data,
    ligand information, and pharmacological interactions
  id: gtopdb.web
  name: Guide to Pharmacology Web Interface
  product_url: https://www.guidetopharmacology.org
- category: ProgrammingInterface
  description: RESTful web services enabling computational access to most of the GtoPdb
    data in JSON format
  id: gtopdb.api.rest
  name: Guide to Pharmacology REST API
  product_url: https://www.guidetopharmacology.org/webServices.jsp
- category: Product
  description: Complete list of drug targets and their families with detailed information
  format: csv
  id: gtopdb.targets.csv
  name: GtoPdb Targets and Families
  product_url: https://www.guidetopharmacology.org/DATA/targets_and_families.csv
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: Complete list of ligands including drugs, small molecules, and other
    bioactive compounds
  format: csv
  id: gtopdb.ligands.csv
  name: GtoPdb Ligands Dataset
  product_url: https://www.guidetopharmacology.org/DATA/ligands.csv
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: Comprehensive dataset of all interactions between ligands and targets
  format: csv
  id: gtopdb.interactions.csv
  name: GtoPdb Interactions Dataset
  product_url: https://www.guidetopharmacology.org/DATA/interactions.csv
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: Detailed interactions list for approved drugs and their targets
  format: csv
  id: gtopdb.approved_drugs.csv
  name: GtoPdb Approved Drugs Dataset
  product_url: https://www.guidetopharmacology.org/DATA/approved_drug_detailed_interactions.csv
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: SDF file containing chemical structures with SMILES for all ligands
    in the database
  format: sdf
  id: gtopdb.download.sdf
  name: GtoPdb Ligand SDF File
  product_url: https://www.guidetopharmacology.org/DATA/all_ligands.sdf
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: RDF/linked data format of the GtoPdb data (target-ligand interactions
    with supporting information)
  format: rdfxml
  id: gtopdb.download.rdf
  name: GtoPdb RDF Dataset
  product_url: https://www.guidetopharmacology.org/DATA/rdf/2025.1/gtp-rdf.n3
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: Product
  description: Complete PostgreSQL database dump of the current Guide to Pharmacology
    database
  id: gtopdb.database
  name: GtoPdb Full Database
  product_url: https://www.guidetopharmacology.org/DATA/public_iuphardb_v2025.1.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-07: No Content-Length
    header found'
- category: GraphicalInterface
  description: An extension of the Guide to PHARMACOLOGY database providing immunological
    access-point to GtoPdb data
  id: gtopdb.immunopharmacology
  name: Guide to IMMUNOPHARMACOLOGY
  product_url: https://www.guidetopharmacology.org/immuno/index.jsp
- category: GraphicalInterface
  description: A specialized portal providing optimized access for the malaria research
    community
  id: gtopdb.malaria
  name: Guide to MALARIA PHARMACOLOGY
  product_url: https://www.guidetopharmacology.org/malaria/index.jsp
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
publications:
- authors:
  - Harding SD
  - Armstrong JF
  - Faccenda E
  - Southan C
  - Alexander SPH
  - Davenport AP
  - Spedding M
  - Davies JA
  doi: doi:10.1093/nar/gkad944
  id: https://doi.org/10.1093/nar/gkad944
  journal: Nucleic Acids Research
  preferred: true
  title: The IUPHAR/BPS Guide to PHARMACOLOGY in 2024
  year: '2024'
repository: https://www.guidetopharmacology.org/download.jsp
---
## Guide to Pharmacology (GtoPdb)

The IUPHAR/BPS Guide to PHARMACOLOGY (GtoPdb) is an expert-curated resource providing authoritative information on drug targets and the substances that act on them. It's developed as a collaboration between the International Union of Basic and Clinical Pharmacology (IUPHAR) and the British Pharmacological Society (BPS).

### Overview

GtoPdb serves as a "one-stop shop" portal to pharmacological information, containing quantitative data on drug targets and the prescription medicines and experimental drugs that act on them. The database focuses on interactions between human proteins and their ligands, with information primarily derived from high-quality pharmacological and medicinal chemistry literature.

### Key Features

- **Comprehensive Target Coverage**: Information on receptors, ion channels, nuclear hormone receptors, kinases, enzymes, transporters, and other drug targets
- **Detailed Ligand Information**: Data on approved drugs, experimental compounds, endogenous substances, and natural products
- **Quantitative Pharmacology**: Binding affinities, functional assay data, and other quantitative measurements
- **Expert Curation**: All data are expert-reviewed and curated by the GtoPdb team and IUPHAR committees
- **Rich Cross-References**: Links to other key databases including Ensembl, UniProt, PubChem, ChEMBL, and DrugBank
- **Specialized Portals**: Includes focused resources like the Guide to Immunopharmacology and Guide to Malaria Pharmacology

### Data Access

The database is accessible through multiple means:

1. **Web Interface**: The primary way to browse and search the data interactively
2. **REST API**: Programmatic access to GtoPdb data in JSON format
3. **Downloadable Files**: Various file formats including CSV/TSV, SDF, and RDF
4. **Full Database Download**: Complete PostgreSQL database dump for local installation

### Target Classes

GtoPdb covers all major pharmacological target classes:

- G protein-coupled receptors (GPCRs)
- Ion channels
- Nuclear hormone receptors
- Kinases
- Catalytic receptors
- Transporters
- Enzymes
- Other protein targets

### Ligand Types

The database includes detailed information on:

- Approved drugs
- Synthetic organic compounds
- Metabolites
- Natural products
- Endogenous peptides
- Other peptides
- Inorganics
- Antibodies
- Labeled ligands

### Update Cycle

GtoPdb follows a regular release cycle, with major updates several times per year. The database is continually growing with new target and ligand entries, focusing particularly on targets of current and potential future approved drugs.