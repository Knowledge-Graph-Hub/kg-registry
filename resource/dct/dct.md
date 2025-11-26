---
activity_status: active
category: Ontology
description: Dublin Core Metadata Terms (DCT) is a vocabulary of standardized metadata elements for describing resources, providing interoperable metadata standards for resource discovery across digital libraries and information systems.
domains: []
id: "dct"
homepage_url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
layout: resource_detail
name: Dublin Core Terms
synonyms:
  - DCT
  - DCMI Terms
  - Dublin Core
  - Dublin Core Metadata Initiative
products:
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: "ubkg.neo4j"
    name: UBKG Neo4j Docker Distribution
    original_source:
      - hgnc
      - loinc
      - icd10
      - snomedct
      - uberon
      - pato
      - cl
      - doid
      - obi
      - obib
      - edam
      - hsapdv
      - sbo
      - mi
      - chebi
      - mp
      - ordo
      - uniprot
      - uo
      - mondo
      - efo
      - pgo
      - gencode
      - reactome
      - hra
      - hubmap
      - sennet
      - stellar
      - dct
      - clinvar
      - connectivitymap
      - hp
      - mp
      - msigdb
      - wikipathways
      - clingen
      - string
      - 4dn
      - erccrbp
      - erccreg
      - faldo
      - glycordf
      - glycocoo
      - gtex
      - kidsfirst
      - lincs
      - motrpac
      - mw
      - npo
      - sckan
      - disgenet
      - biomarker
      - opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - ubkg
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: "ubkg.csv"
    name: UBKG Ontology CSV Files
    original_source:
      - hgnc
      - loinc
      - icd10
      - snomedct
      - uberon
      - pato
      - cl
      - doid
      - obi
      - obib
      - edam
      - hsapdv
      - sbo
      - mi
      - chebi
      - mp
      - ordo
      - uniprot
      - uo
      - mondo
      - efo
      - pgo
      - gencode
      - reactome
      - hra
      - hubmap
      - sennet
      - stellar
      - dct
      - clinvar
      - connectivitymap
      - hp
      - mp
      - msigdb
      - wikipathways
      - clingen
      - string
      - 4dn
      - erccrbp
      - erccreg
      - faldo
      - glycordf
      - glycocoo
      - gtex
      - kidsfirst
      - lincs
      - motrpac
      - mw
      - npo
      - sckan
      - disgenet
      - biomarker
      - opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - ubkg
warnings:
  - This is an automatically generated stub page. Please replace with accurate information about this resource.
---

# Dublin Core Terms

## Overview

Dublin Core Metadata Terms (DCT) is a vocabulary of metadata elements maintained by the Dublin Core Metadata Initiative (DCMI). It provides a standardized set of terms for describing resources such as documents, datasets, images, and digital objects, enabling interoperable metadata across diverse information systems.

## Key Components

### Core Elements (15 basic elements)
- **Title**: Name of the resource
- **Creator**: Entity responsible for creating the content
- **Subject**: Topic or theme of the resource
- **Description**: Account of the resource content
- **Publisher**: Entity responsible for making the resource available
- **Contributor**: Entity that contributed to the resource
- **Date**: Temporal information about the resource
- **Type**: Nature or genre of the resource
- **Format**: Physical or digital manifestation
- **Identifier**: Unambiguous reference (DOI, ISBN, URI)
- **Source**: Related resource from which the current resource is derived
- **Language**: Language of the intellectual content
- **Relation**: Related resource
- **Coverage**: Spatial or temporal scope
- **Rights**: Information about rights held in and over the resource

### Extended Terms
The full DCT vocabulary includes:
- Refined versions of core elements (e.g., dcterms:created, dcterms:modified)
- Additional properties for more specific descriptions
- Classes for resource types
- Vocabulary encoding schemes
- Syntax encoding schemes

## Applications

- **Digital Libraries**: Standardized cataloging and resource discovery
- **Data Repositories**: Consistent metadata for datasets and research outputs
- **Semantic Web**: RDF-compatible vocabulary for linked data
- **Knowledge Graphs**: Metadata annotation and provenance tracking
- **Information Systems**: Cross-platform metadata interoperability
- **Archives and Museums**: Cultural heritage resource description

## Metadata Standards

Dublin Core supports multiple representation formats:
- RDF/XML
- JSON-LD
- Turtle
- HTML with RDFa
- XML

## Integration

Dublin Core Terms are widely integrated in:
- Institutional repositories (DSpace, Fedora)
- Digital asset management systems
- Knowledge graphs and semantic web applications
- UBKG (Unified Biomedical Knowledge Graph)
- Metadata crosswalks and mappings
- OAI-PMH (Open Archives Initiative Protocol)

## Governance

Dublin Core is maintained by the Dublin Core Metadata Initiative (DCMI), an international organization dedicated to promoting widespread adoption of interoperable metadata standards.

## Resources

- Official Specification: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- User Guide: https://www.dublincore.org/resources/userguide/
- RDF Schema: http://purl.org/dc/terms/

For examples of Dublin Core Terms usage in biomedical knowledge graphs, see the [UBKG project](https://ubkg.docs.xconsortia.org/).
