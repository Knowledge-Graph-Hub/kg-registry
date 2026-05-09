---
activity_status: active
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: rene@ccrc.uga.edu
  label: Rene Ranzinger
- category: Individual
  contact_details:
  - contact_type: email
    value: kkiyoko@soka.ac.jp
  label: Kiyoko F. Aoki-Kinoshita
creation_date: '2025-10-29T00:00:00Z'
curators:
- category: Individual
  contact_details:
  - contact_type: github
    value: ReneRanzinger
  label: Rene Ranzinger
- category: Individual
  contact_details:
  - contact_type: email
    value: kkiyoko@soka.ac.jp
  label: Kiyoko F. Aoki-Kinoshita
description: 'GlycoRDF is a standardized ontology for representing glycomics data
  in Resource Description Framework (RDF) format. It provides a common machine-readable
  interface for glycomics databases, enabling integration and cross-referencing of
  glycan structures, biological source information, publications, and experimental
  data. Developed by an international consortium of glycomics bioinformatics experts,
  GlycoRDF defines classes and predicates for diverse glycomics data types including
  glycan sequences, monosaccharide compositions, biological sources, literature references,
  NMR data, mass spectrometry data, and liquid chromatography-mass spectrometry data.
  The ontology reuses concepts from established ontologies including UniProt Core,
  Bibliographic Ontology, Dublin Core Metadata Initiative, and HUPO-PSI Mass Spectrometry
  Ontology. GlycoRDF has been adopted by major glycomics database providers including
  CSDB, MonosaccharideDB, GlycomeDB, UniCarbKB, GlycoEpitope, GlycoNAVI, and GlycoProtDB,
  facilitating semantic web applications and SPARQL queries across heterogeneous glycomics
  data sources.

  '
domains:
- chemistry and biochemistry
- biological systems
- biomedical
homepage_url: http://www.glycoinfo.org/GlycoRDF/
id: glycordf
last_modified_date: '2025-10-29T00:00:00Z'
layout: resource_detail
name: 'GlycoRDF: An Ontology to Standardize Glycomics Data in RDF'
products:
- category: OntologyProduct
  description: OWL ontology file defining the GlycoRDF standard for representing glycomics
    data in RDF format
  format: owl
  id: glycordf.ontology
  name: GlycoRDF Ontology (OWL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_file_size: 32914
  product_url: https://github.com/ReneRanzinger/GlycoRDF/blob/master/ontology/glycan.owl
- category: GraphicalInterface
  description: NCBO BioPortal entry for browsing and exploring the GlycoRDF ontology
  format: http
  id: glycordf.bioportal
  name: GlycoRDF BioPortal Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_url: https://bioportal.bioontology.org/ontologies/GLYCORDF
- category: DocumentationProduct
  description: Comprehensive documentation of the GlycoRDF ontology classes, predicates,
    and usage examples
  format: doc
  id: glycordf.documentation
  name: GlycoRDF Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_file_size: 62492
  product_url: https://github.com/ReneRanzinger/GlycoRDF/blob/master/ontology/documentation.docx
- category: GraphicalInterface
  description: Official project homepage with overview, documentation, and links to
    database implementations
  format: http
  id: glycordf.homepage
  name: GlycoRDF Project Homepage
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_url: http://www.glycoinfo.org/GlycoRDF/
- category: GraphicalInterface
  description: GitHub repository containing ontology files, documentation, and source
    code for RDF generation
  format: http
  id: glycordf.github
  name: GlycoRDF GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_url: https://github.com/glycoinfo/GlycoRDF
- category: DocumentationProduct
  description: Wiki with developer information, database provider documentation, and
    implementation guidelines
  format: http
  id: glycordf.wiki
  name: GlycoRDF Wiki
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_url: https://github.com/ReneRanzinger/GlycoRDF/wiki
- category: ProcessProduct
  description: Java source code for generating GlycoRDF data from glycomics databases
  format: java
  id: glycordf.java-source
  name: GlycoRDF Java Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  repository: https://github.com/glycoinfo/GlycoRDF
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
publications:
- authors:
  - Rene Ranzinger
  - Kiyoko F. Aoki-Kinoshita
  - Matthew P. Campbell
  - Shin Kawano
  - "Thomas L\xFCtteke"
  - Shujiro Okuda
  - Daisuke Shinmachi
  - Toshihide Shikanai
  - Hiromichi Sawaki
  - Philip Toukach
  category: Publication
  id: https://doi.org/10.1093/bioinformatics/btu732
  journal: Bioinformatics
  preferred: true
  title: 'GlycoRDF: an ontology to standardize glycomics data in RDF'
  year: '2015'
- authors:
  - Kiyoko F. Aoki-Kinoshita
  category: Publication
  id: https://doi.org/10.1186/2041-1480-4-39
  journal: Journal of Biomedical Semantics
  preferred: false
  title: Introducing glycomics data into the Semantic Web
  year: '2013'
repository: https://github.com/glycoinfo/GlycoRDF
tags:
- biopragmatics
---
## Overview

GlycoRDF is a collaborative effort by the international glycomics community to create a standardized representation for glycomics data using Resource Description Framework (RDF) and Web Ontology Language (OWL). The ontology addresses the critical need for data integration across diverse glycomics databases, which historically have used incompatible formats and representations for glycan structures and associated metadata.

## Motivation and Background

Over the past decades, numerous glycomics databases have been developed independently, each with unique data representations and interfaces. This fragmentation has created "disconnected islands" of valuable glycomics data, making it difficult to perform comprehensive queries across resources or to integrate glycan information with other life science data. GlycoRDF solves this problem by providing a common RDF standard that allows different databases to express their data in a unified, machine-readable format.

## Ontology Structure

GlycoRDF is organized around five core concepts represented as classes:

### 1. Compound Class
Represents biological molecules, including glycans and glycoconjugates. Subclasses include:
- **Saccharide**: General glycan structures
- **NGlycan**: N-linked glycans
- **OGlycan**: O-linked glycans
- Glycoconjugate classes for molecules containing both glycan and non-glycan components (peptides, proteins, lipids)

Each glycan can be represented in multiple sequence formats including GlycoCT, LinearCode, IUPAC, and WURCS. Monosaccharide compositions and cross-references to other databases are also supported.

### 2. Citation Class
Captures literature references including articles, book chapters, and thesis documents. Reuses predicates from Dublin Core Metadata Initiative (DCMI) and Bibliographic Ontology for describing publication information. Supports references to PubMed and DOI.

### 3. Source Class
Describes the biological origin of glycan molecules with subclasses:
- **SourceNatural**: For glycans extracted from biological organisms, with detailed specification of species, organ, tissue, fluid, cell type, cell line, strains, life stage, and associated diseases
- **SourceSynthetic**: For chemically synthesized glycans

Uses existing dictionaries and ontologies such as UniProt Taxonomy for species information and Medical Subject Headings (MeSH) for tissue classification.

### 4. Evidence Class
Represents experimental data with subclasses for specific techniques:
- **EvidenceNMR**: Nuclear magnetic resonance data
- **EvidenceLC**: Liquid chromatography data
- **EvidenceMS**: Mass spectrometry data (reuses terms from HUPO-PSI Mass Spectrometry Ontology)

### 5. ReferencedCompound Class
Groups primary information to link glycan structures with publications, biological sources, and experimental evidence. This grouping enables complex queries such as "Which experimental data support that glycan X was found in organism Y?" or "Which papers report identification of sialic acid-containing structures by positive mode ESI-MS?"

## Implementation and Adoption

GlycoRDF has been widely adopted by the glycomics community. Database providers that have implemented GlycoRDF exports include:

- **CSDB** (Carbohydrate Structure Database)
- **GlycomeDB** (integrated glycan structure database)
- **MonosaccharideDB** (monosaccharide nomenclature database)
- **UniCarbKB** (glycoprotein glycan structures database)
- **GlycoEpitope** (carbohydrate epitopes and antibodies database)
- **GlycoNAVI** (Japanese glycomics portal)
- **GlycoProtDB** (glycoprotein database)

These databases provide GlycoRDF data through various access methods including statically generated RDF files, web services generating RDF on-the-fly, and documented APIs.

## Applications and Benefits

GlycoRDF enables:

1. **Cross-database queries**: Query multiple glycomics databases simultaneously using SPARQL
2. **Data integration**: Combine glycan data with protein, gene, and pathway information from other life science resources
3. **Machine learning**: Access standardized data for computational analysis and prediction
4. **Data mash-ups**: Create applications that integrate information from diverse sources
5. **Semantic web interoperability**: Link glycomics data to the broader semantic web ecosystem

## Technical Features

- **Extensible design**: Can accommodate new data types and experimental techniques through subclassing
- **Reuse of established ontologies**: Leverages UniProt Core, Bibliographic Ontology, DCMI, and HUPO-PSI-MS
- **Standardized dictionaries**: Defines unique URIs for common glycomics terms (monosaccharide configurations, substituents, representation schemes, sequence formats)
- **Flexible sequence representation**: Supports multiple glycan sequence formats
- **Cross-reference support**: Enables mapping between database entries using owl:sameAs and rdfs:seeAlso predicates

## Development and Maintenance

GlycoRDF was developed through collaborative efforts at the Japanese BioHackathon workshop in Toyama (2012) and an international Glyco-BioHackathon in Dalian, China (2013). The ontology is maintained on GitHub and is registered in the NCBO BioPortal for easy browsing and exploration.

## Future Directions

The GlycoRDF initiative continues to work toward:
- Expanding the list of database providers implementing the standard
- Linking glycomics data with genomics and proteomics resources
- Establishing SPARQL endpoints and triplestores for direct querying
- Developing user-friendly web interfaces for non-technical researchers
- Supporting federated queries across multiple glycomics databases