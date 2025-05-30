---
layout: resource_detail
id: gtopdb
name: Guide to Pharmacology
description: The IUPHAR/BPS Guide to PHARMACOLOGY is an expert-curated resource providing quantitative information on drug targets and the substances that act on them, including approved drugs and experimental therapeutics
domains:
  - pharmacology
  - health
  - biomedical
  - drug discovery
  - translational
contacts:
  - category: Organization
    label: Guide to Pharmacology Help Desk
    contact_details:
      - contact_type: email
        value: enquiries@guidetopharmacology.org
  - category: Individual
    label: Jamie Davies
    contact_details:
      - contact_type: email
        value: jamie.davies@ed.ac.uk
license:
  id: http://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
homepage_url: https://www.guidetopharmacology.org
repository: https://www.guidetopharmacology.org/download.jsp
category: DataSource
activity_status: active
infores_id: gtopdb
products:
  - id: gtopdb.web
    name: Guide to Pharmacology Web Interface
    description: A web-based interface for accessing and browsing drug target data, ligand information, and pharmacological interactions
    product_url: https://www.guidetopharmacology.org
    category: GraphicalInterface
  - id: gtopdb.api.rest
    name: Guide to Pharmacology REST API
    description: RESTful web services enabling computational access to most of the GtoPdb data in JSON format
    product_url: https://www.guidetopharmacology.org/webServices.jsp
    category: ProgrammingInterface
  - id: gtopdb.targets.csv
    name: GtoPdb Targets and Families
    description: Complete list of drug targets and their families with detailed information
    product_url: https://www.guidetopharmacology.org/DATA/targets_and_families.csv
    category: Product
    format: csv
  - id: gtopdb.ligands.csv
    name: GtoPdb Ligands Dataset
    description: Complete list of ligands including drugs, small molecules, and other bioactive compounds
    product_url: https://www.guidetopharmacology.org/DATA/ligands.csv
    category: Product
    format: csv
  - id: gtopdb.interactions.csv
    name: GtoPdb Interactions Dataset
    description: Comprehensive dataset of all interactions between ligands and targets
    product_url: https://www.guidetopharmacology.org/DATA/interactions.csv
    category: Product
    format: csv
  - id: gtopdb.approved_drugs.csv
    name: GtoPdb Approved Drugs Dataset
    description: Detailed interactions list for approved drugs and their targets
    product_url: https://www.guidetopharmacology.org/DATA/approved_drug_detailed_interactions.csv
    category: Product
    format: csv
  - id: gtopdb.download.sdf
    name: GtoPdb Ligand SDF File
    description: SDF file containing chemical structures with SMILES for all ligands in the database
    product_url: https://www.guidetopharmacology.org/DATA/all_ligands.sdf
    category: Product
    format: sdf
  - id: gtopdb.download.rdf
    name: GtoPdb RDF Dataset
    description: RDF/linked data format of the GtoPdb data (target-ligand interactions with supporting information)
    product_url: https://www.guidetopharmacology.org/DATA/rdf/2025.1/gtp-rdf.n3
    category: Product
    format: rdfxml
  - id: gtopdb.database
    name: GtoPdb Full Database
    description: Complete PostgreSQL database dump of the current Guide to Pharmacology database
    product_url: https://www.guidetopharmacology.org/DATA/public_iuphardb_v2025.1.zip
    category: Product
  - id: gtopdb.immunopharmacology
    name: Guide to IMMUNOPHARMACOLOGY
    description: An extension of the Guide to PHARMACOLOGY database providing immunological access-point to GtoPdb data
    product_url: https://www.guidetopharmacology.org/immuno/index.jsp
    category: GraphicalInterface
  - id: gtopdb.malaria
    name: Guide to MALARIA PHARMACOLOGY
    description: A specialized portal providing optimized access for the malaria research community
    product_url: https://www.guidetopharmacology.org/malaria/index.jsp
    category: GraphicalInterface
publications:
  - id: https://doi.org/10.1093/nar/gkad944
    preferred: true
    title: The IUPHAR/BPS Guide to PHARMACOLOGY in 2024
    authors:
        - Harding SD
        - Armstrong JF
        - Faccenda E
        - Southan C
        - Alexander SPH
        - Davenport AP
        - Spedding M
        - Davies JA
    journal: Nucleic Acids Research
    year: 2024
    doi: doi:10.1093/nar/gkad944
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
