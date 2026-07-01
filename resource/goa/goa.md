---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/GOA/contactus
  id: ebi
  label: GOA Team at EMBL-EBI
creation_date: '2025-10-29T00:00:00Z'
description: 'The Gene Ontology Annotation (GOA) Database provides high-quality Gene
  Ontology (GO) annotations to proteins in the UniProt Knowledgebase (UniProtKB),
  RNA molecules from RNAcentral, and protein complexes from the Complex Portal. GOA
  files contain a mixture of manual annotations supplied by members of the Gene Ontology
  Consortium and computationally assigned GO terms describing gene products. All annotations
  are clearly indicated by associated evidence codes with links to source data. Files
  are released approximately every four weeks in coordination with UniProtKB releases.

  '
domains:
- genomics
- biological systems
- proteomics
homepage_url: https://www.ebi.ac.uk/GOA/
id: goa
infores_id: goa
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: GOA
products:
- category: GraphicalInterface
  description: Web portal for accessing GOA information, statistics, and navigation
    to downloads
  format: http
  id: goa.portal
  name: GOA Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://www.ebi.ac.uk/GOA/
- category: GraphicalInterface
  description: Browser for searching and viewing Gene Ontology terms and GOA annotations
  format: http
  id: goa.quickgo
  name: QuickGO Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://www.ebi.ac.uk/QuickGO/
- category: Product
  description: FTP site containing current and archived GOA annotation files for all
    species
  format: http
  id: goa.ftp
  name: GOA FTP Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: rnacentral
  - relation_type: prov:wasInformedBy
    source: complexportal
- category: Product
  description: GO annotations for all UniProtKB entries
  format: txt
  id: goa.uniprot
  latest_version: '232'
  name: UniProt GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
- category: Product
  description: GO annotations for human proteins
  format: txt
  id: goa.human
  name: Human GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
- category: Product
  description: GO annotations for mouse proteins
  format: txt
  id: goa.mouse
  name: Mouse GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
- category: MappingProduct
  description: Files containing transitive assignments of InterPro matches, UniProtKB
    keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected
    GO terms
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
- category: Product
  description: GO annotations for PDB entries
  format: txt
  id: goa.pdb
  name: PDB GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
- category: Product
  description: GO annotations organized by proteomes
  format: txt
  id: goa.proteomes
  name: Proteomes GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/
- category: DocumentationProduct
  description: Documentation including FAQ, About pages, and contact information
  format: http
  id: goa.documentation
  name: GOA Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://www.ebi.ac.uk/GOA/about
- category: GraphProduct
  description: HumanGOA Automat
  format: kgx-jsonl
  id: automat.humangoa
  infores_id: automat-human-goa
  name: humangoa_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/HumanGOA_Automat/06f107a4e9e8e547/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for GOA distributed via the NCATS Translator
    release site (release 2026_03_06; build goa_2026-01-23_5fdd3125_2025sep1_4.3.6;
    source version 2026-01-23; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 1132872
  format: kgx-jsonl
  id: translator.goa.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator GOA KGX Graph
  node_count: 91993
  original_source:
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/goa/latest/
  versions:
  - '2026_03_06'
  - goa_2026-01-23_5fdd3125_2025sep1_4.3.6
- category: Product
  compression: 7z
  description: Compressed CSV file containing ProteomeHD v1.1, with 10,323 proteins
    measured across 294 SILAC ratios
  format: csv
  id: proteomehd.data
  name: ProteomeHD Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  product_file_size: 9427082
  product_url: https://raw.githubusercontent.com/Rappsilber-Laboratory/ProteomeHD/master/Data/ProteomeHD_v1_1.7z
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: GraphProduct
  description: GP_KG.txt
  edge_count: 1246726
  format: txt
  id: gp-kg.graph
  name: GP-KG
  node_count: 61146
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gp-kg
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: goa
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: phenomebrowser
  - relation_type: prov:wasDerivedFrom
    source: treatkb
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
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

### Download Site

Current and archived GOA annotation files are available through the EBI GOA download
site (https://ftp.ebi.ac.uk/pub/databases/GO/goa/). Each species-specific directory
contains README files describing available files and their content. Archived annotation
sets are maintained to support historical analyses and reproducibility.

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

- **Website**: https://www.ebi.ac.uk/GOA/
- **QuickGO Browser**: https://www.ebi.ac.uk/QuickGO/
- **Download Site**: https://ftp.ebi.ac.uk/pub/databases/GO/goa/
- **FAQ**: https://www.ebi.ac.uk/GOA/faq
- **About**: https://www.ebi.ac.uk/GOA/about
- **Contact**: https://www.ebi.ac.uk/GOA/contactus
- **Twitter**: @QuickGO_EBI