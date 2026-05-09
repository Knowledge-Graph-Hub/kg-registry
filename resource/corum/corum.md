---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.helmholtz-munich.de/
      - contact_type: email
        value: corum@helmholtz-muenchen.de
    label: "Helmholtz Zentrum München"
creation_date: '2025-07-22T00:00:00Z'
description: CORUM (Comprehensive Resource of Mammalian Protein Complexes) is a curated database of experimentally characterized protein complexes from mammalian organisms, particularly human, mouse, and rat, with a focus on manually annotated information from scientific literature.
domains:
  - proteomics
  - biomedical
  - chemistry and biochemistry
homepage_url: https://mips.helmholtz-muenchen.de/corum/
id: corum
last_modified_date: '2025-09-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
name: CORUM
products:
  - category: Product
    description: Complete dataset of all curated protein complexes in CORUM in tab-delimited format
    format: tsv
    id: corum.all_complexes
    license:
      id: https://creativecommons.org/licenses/by-nc/4.0/
      label: CC BY-NC 4.0
    name: CORUM All Complexes
    product_url: https://mips.helmholtz-muenchen.de/corum/download/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
      - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
      - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2026-01-15_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - category: Product
    description: Core dataset of manually curated, non-redundant protein complexes in CORUM in tab-delimited format
    format: tsv
    id: corum.core_complexes
    license:
      id: https://creativecommons.org/licenses/by-nc/4.0/
      label: CC BY-NC 4.0
    name: CORUM Core Complexes
    product_url: https://mips.helmholtz-muenchen.de/corum/download/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
      - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
      - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2026-01-15_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - category: Product
    description: Dataset of all CORUM protein complexes in PSI-MI XML format (Proteomics Standards Initiative)
    format: psi_mi_xml
    id: corum.psi_mi
    license:
      id: https://creativecommons.org/licenses/by-nc/4.0/
      label: CC BY-NC 4.0
    name: CORUM PSI-MI
    product_url: https://mips.helmholtz-muenchen.de/corum/download/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
      - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
      - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2026-01-15_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - category: Product
    description: Dataset of all CORUM protein complexes in PSI-MI MITAB 2.5 format
    format: psi_mi_mitab
    id: corum.mitab
    license:
      id: https://creativecommons.org/licenses/by-nc/4.0/
      label: CC BY-NC 4.0
    name: CORUM MITAB
    product_url: https://mips.helmholtz-muenchen.de/corum/download/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)'')))'
      - 'File was not able to be retrieved when checked on 2026-04-15: Error connecting to URL: HTTPSConnectionPool(host=''mips.helmholtz-muenchen.de'', port=443): Max retries exceeded with url: /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)'')))'
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1028)')))
      - File was not able to be retrieved when checked on 2026-03-30_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
      - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2026-01-15_ Error connecting to URL_ HTTPSConnectionPool(host='mips.helmholtz-muenchen.de', port=443)_ Max retries exceeded with url_ /corum/download/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED] certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - source: bioteque
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - "Stefanie Gößler"
      - Gisela Fobo
      - Barbara Wankerl
      - Christopher J. Mann
      - Hans-Werner Mewes
      - Andreas Ruepp
    doi: 10.1093/nar/gkac1015
    id: doi:10.1093/nar/gkac1015
    journal: Nucleic Acids Research
    preferred: true
    title: "CORUM: the comprehensive resource of mammalian protein complexes—2023"
    year: '2023'
  - authors:
      - Andreas Giurgiu
      - Julian Reinhard
      - Barbara Brauner
      - Irmtraud Dunger-Kaltenbach
      - Gisela Fobo
      - Goar Frishman
      - Corinna Montrone
      - Andreas Ruepp
    doi: 10.1093/nar/gky973
    id: doi:10.1093/nar/gky973
    journal: Nucleic Acids Research
    title: "CORUM: the comprehensive resource of mammalian protein complexes—2019"
    year: '2019'
  - authors:
      - Andreas Ruepp
      - Barbara Brauner
      - Irmtraud Dunger-Kaltenbach
      - Goar Frishman
      - Corinna Montrone
      - Michael Stransky
      - Brigitte Waegele
      - Thorsten Schmidt
      - Octave Noubibou Doudieu
      - "Volker Stümpflen"
      - Hans-Werner Mewes
    doi: 10.1093/nar/gkp914
    id: doi:10.1093/nar/gkp914
    journal: Nucleic Acids Research
    title: "CORUM: the comprehensive resource of mammalian protein complexes—2009"
    year: '2010'
repository: https://mips.helmholtz-muenchen.de/corum/download
taxon:
  - NCBITaxon:40674
  - NCBITaxon:10090
  - NCBITaxon:10116
  - NCBITaxon:9606
---

# CORUM - Comprehensive Resource of Mammalian Protein Complexes

CORUM is a manually curated database of experimentally characterized protein complexes from mammalian organisms. It serves as a comprehensive and high-quality resource for researchers studying protein-protein interactions, cellular functions, and disease mechanisms.

## Overview

The CORUM database focuses on protein complexes from human, mouse, and rat, with a particular emphasis on human complexes. The database is distinguished by its commitment to manual curation from scientific literature, ensuring high data quality. Every entry in CORUM is based on experimental evidence from published research papers, providing reliable information about the composition and function of protein complexes.

As of the 2023 update, CORUM contains:
- Over 4,700 protein complexes
- More than 3,300 different genes
- Approximately 20,000 protein-protein interactions

## Key Features

CORUM provides comprehensive information about each protein complex, including:

- Complex name and synonyms
- Organism source
- Protein composition (with UniProt IDs)
- Associated diseases
- Biological functions (GO terms)
- Cellular localization
- PubMed references to experimental evidence
- Tissue distribution
- Protein complex purification methods

## Data Sources and Curation

All entries in CORUM are manually extracted from scientific literature by expert curators. This manual curation approach ensures high-quality data and allows for the inclusion of detailed information that may not be captured by automated text mining approaches. The curation process focuses on:

1. Identifying experimentally verified protein complexes from peer-reviewed publications
2. Mapping protein components to standardized identifiers (UniProt)
3. Annotating complexes with functional information and disease associations
4. Cross-referencing with other databases and ontologies

## Applications

CORUM serves as a valuable resource for various research applications:

- **Proteomics**: Interpretation of mass spectrometry data and analysis of protein-protein interactions
- **Systems Biology**: Study of cellular pathways and network analysis
- **Disease Research**: Investigation of disease mechanisms and identification of therapeutic targets
- **Computational Biology**: Training and validation of protein interaction prediction algorithms
- **Functional Genomics**: Functional annotation of genes and proteins

## Data Access

CORUM data is freely available for academic and non-commercial use under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license. The database can be accessed through:

- Web interface at [https://mips.helmholtz-muenchen.de/corum/](https://mips.helmholtz-muenchen.de/corum/)
- Bulk downloads in various formats (PSI-MI XML, MITAB, plain text)
- Programmatic access via web services
