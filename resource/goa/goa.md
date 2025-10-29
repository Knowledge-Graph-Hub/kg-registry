---
id: goa
category: DataSource
name: GOA
description: >
  The Gene Ontology Annotation (GOA) Database provides high-quality Gene Ontology (GO) annotations to proteins in the UniProt Knowledgebase (UniProtKB), RNA molecules from RNAcentral, and protein complexes from the Complex Portal. GOA files contain a mixture of manual annotations supplied by members of the Gene Ontology Consortium and computationally assigned GO terms describing gene products. All annotations are clearly indicated by associated evidence codes with links to source data. Files are released approximately every four weeks in coordination with UniProtKB releases.
creation_date: '2025-10-29T00:00:00Z'
last_modified_date: '2025-10-29T00:00:00Z'
domains:
  - genomics
  - biological systems
  - proteomics
homepage_url: https://www.ebi.ac.uk/GOA/index
contacts:
  - category: Organization
    label: GOA Team at EMBL-EBI
    contact_details:
      - contact_type: url
        value: https://www.ebi.ac.uk/GOA/contactus
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
layout: resource_detail
products:
  - id: goa.portal
    category: GraphicalInterface
    name: GOA Website
    description: Web portal for accessing GOA information, statistics, and navigation to downloads
    product_url: https://www.ebi.ac.uk/GOA/index
    format: http
  - id: goa.quickgo
    category: GraphicalInterface
    name: QuickGO Browser
    description: Browser for searching and viewing Gene Ontology terms and GOA annotations
    product_url: https://www.ebi.ac.uk/QuickGO/
    format: http
  - id: goa.ftp
    category: Product
    name: GOA FTP Site
    description: FTP site containing current and archived GOA annotation files for all species
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/
    format: http
  - id: goa.uniprot
    category: Product
    name: UniProt GOA Annotations
    description: GO annotations for all UniProtKB entries
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
    format: txt
    original_source:
      - uniprot
  - id: goa.human
    category: Product
    name: Human GOA Annotations
    description: GO annotations for human proteins
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
    format: txt
    original_source:
      - uniprot
  - id: goa.mouse
    category: Product
    name: Mouse GOA Annotations
    description: GO annotations for mouse proteins
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
    format: txt
    original_source:
      - uniprot
  - id: goa.mapping-files
    category: MappingProduct
    name: GO Mapping Files
    description: Files containing transitive assignments of InterPro matches, UniProtKB keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected GO terms
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
    format: txt
  - id: goa.pdb
    category: Product
    name: PDB GOA Annotations
    description: GO annotations for PDB entries
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
    format: txt
    original_source:
      - pdb
  - id: goa.proteomes
    category: Product
    name: Proteomes GOA Annotations
    description: GO annotations organized by proteomes
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/
    format: txt
  - id: goa.documentation
    category: DocumentationProduct
    name: GOA Documentation
    description: Documentation including FAQ, About pages, and contact information
    product_url: https://www.ebi.ac.uk/GOA/newto
    format: http
---

## Overview

The Gene Ontology Annotation (GOA) Database is a comprehensive resource providing high-quality Gene Ontology (GO) annotations to biological entities including proteins in the UniProt Knowledgebase (UniProtKB), RNA molecules from RNAcentral, and protein complexes from the Complex Portal. As a key component of the Gene Ontology Consortium infrastructure, GOA serves as a central hub for functional annotation of gene products across multiple species and databases.

## Mission and Scope

GOA aims to provide comprehensive, high-quality GO annotations that describe the molecular functions, biological processes, and cellular components associated with gene products. The database integrates both manual expert annotations supplied by members of the Gene Ontology Consortium and computationally assigned GO terms, with all annotation types clearly indicated by associated evidence codes and linked to source data.

## Data Content and Organization

### Annotation Types

GOA provides two primary types of annotations:

- **Manual Annotations**: Expert-curated annotations supplied by members of the Gene Ontology Consortium, based on published literature and experimental evidence
- **Computational Annotations**: Automatically assigned GO terms based on sequence similarity, domain matches, and other computational methods

All annotations include evidence codes that clearly indicate the type and quality of supporting evidence, ensuring transparency and enabling users to assess annotation reliability.

### Species Coverage

GOA provides comprehensive annotation sets for multiple model organisms and species, including:

- **UniProt**: All UniProtKB entries
- **Model Organisms**: Human, mouse, rat, zebrafish, fly (Drosophila), worm (C. elegans), yeast (S. cerevisiae), Arabidopsis, chicken, cow, dog, pig, Dictyostelium
- **Structural Biology**: PDB (Protein Data Bank) entries
- **Proteomes**: Annotations organized by reference proteomes
- **Pre-release**: Early access to annotations for emerging pathogens (e.g., SARS-CoV-2)

## Data Access and Products

### QuickGO Browser

The QuickGO browser (https://www.ebi.ac.uk/QuickGO/) provides a user-friendly web interface for searching and viewing Gene Ontology terms and annotations. Users can explore GO term hierarchies, view annotations for specific gene products, and access detailed evidence supporting each annotation.

### FTP Downloads

Current and archived GOA annotation files are available through the GOA FTP site (ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/). Each species-specific directory contains README files describing available files and their content. Archived annotation sets are maintained to support historical analyses and reproducibility.

### File Formats

GOA annotations are provided in standard Gene Ontology annotation formats, making them compatible with a wide range of bioinformatics tools and workflows. Files include:

- **Annotation Files**: Complete sets of GO annotations for each species
- **Mapping Files**: Transitive assignments connecting database identifiers to GO terms
- **ID Mapping Files**: Cross-references between UniProtKB and other databases

## GO Mapping Files

GOA provides specialized mapping files that enable automatic generation of GO annotations through transitive assignment. These files contain mappings from:

- **InterPro**: Protein domain matches to GO terms
- **UniProtKB Keywords**: Controlled vocabulary terms to GO terms
- **Subcellular Locations**: Cellular compartment annotations to GO terms
- **Enzyme Commission (EC) Numbers**: Enzymatic activities to GO terms
- **HAMAP**: Microbial protein family matches to GO terms

These mapping files are used in conjunction with annotated databases like UniProtKB to generate automatic (IEA-evidenced) GO annotations, significantly expanding annotation coverage.

## Release Cycle and Updates

All GOA files are released approximately every four weeks, coordinated with UniProtKB releases. This regular release schedule ensures that users have access to the most current annotations, incorporating new literature-based annotations and updates to computational predictions.

## Integration with Other Resources

GOA integrates closely with several major biological databases and resources:

- **UniProt**: Primary source of protein sequence and annotation data
- **Gene Ontology Consortium**: Collaborative network providing expert annotations
- **RNAcentral**: Source of RNA molecule identifiers and sequences
- **Complex Portal**: Source of protein complex information
- **QuickGO**: Provides search and visualization capabilities for GO annotations
- **InterPro**: Protein domain and family classifications used for annotation inference
- **PDB**: Structural biology database providing 3D structure context

## Applications and Impact

GOA annotations support a wide range of research applications:

- **Functional Genomics**: Understanding gene and protein functions across species
- **Comparative Biology**: Identifying conserved functions and evolutionary relationships
- **Pathway Analysis**: Enrichment analysis and functional interpretation of gene sets
- **Disease Research**: Linking genetic variants to functional consequences
- **Drug Discovery**: Target identification and understanding molecular mechanisms
- **Systems Biology**: Network analysis and modeling of biological systems

## Data Quality and Curation

GOA maintains high annotation quality through:

- **Expert Curation**: Manual annotations by trained biocurators with domain expertise
- **Evidence Codes**: Transparent indication of annotation support and reliability
- **Literature Support**: Direct links to publications supporting each annotation
- **Community Feedback**: Mechanisms for users to report issues and suggest improvements
- **Regular Updates**: Frequent releases incorporating new experimental evidence

## Contact and Support

The GOA team at EMBL-EBI provides support and welcomes feedback through their contact page (https://www.ebi.ac.uk/GOA/contactus). The team maintains active social media presence through the QuickGO Twitter account (@QuickGO_EBI) for announcements and updates.

## Technical Infrastructure

GOA is hosted at EMBL-EBI (European Bioinformatics Institute) at the Wellcome Genome Campus in Hinxton, Cambridgeshire, UK. The database benefits from EMBL-EBI's robust infrastructure, ensuring high availability, data security, and reliable access for the global research community.

## Additional Resources

- **Website**: https://www.ebi.ac.uk/GOA/index
- **QuickGO Browser**: https://www.ebi.ac.uk/QuickGO/
- **FTP Site**: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/
- **FAQ**: https://www.ebi.ac.uk/GOA/faq
- **About**: https://www.ebi.ac.uk/GOA/newto
- **Contact**: https://www.ebi.ac.uk/GOA/contactus
- **Twitter**: @QuickGO_EBI
