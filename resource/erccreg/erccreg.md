---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@exrna.org
  label: Extracellular RNA Communication Consortium
description: ERCC Regulatory Element dataset (erccreg) is a collection of data related
  to regulatory elements of extracellular RNA as part of the NIH Common Fund's Extracellular
  RNA Communication Consortium (ERCC) program. This dataset focuses on RNA-based regulatory
  mechanisms involved in extracellular communication.
domains:
- biomedical
- genomics
- chemistry and biochemistry
homepage_url: https://exrna.org/
id: erccreg
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ERCC Regulatory Element Dataset
products:
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
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
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
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
---
# ERCC Regulatory Element Dataset

The ERCC Regulatory Element Dataset (erccreg) is part of the research output from the NIH Common Fund's Extracellular RNA Communication Consortium (ERCC), which explores the biology and function of extracellular RNA (exRNA).

## Overview

Extracellular RNA was once thought to exist in a stable form only inside cells, where it served as an intermediate in the translation from genes to proteins. However, research has revealed that RNAs can play a role in a variety of complex cellular functions, including cell-to-cell communication. The ERCC Regulatory Element Dataset focuses on the regulatory elements and mechanisms associated with exRNA function.

## Research Context

This dataset is part of the broader ERCC initiative which aims to:

1. Discover fundamental biological principles about the mechanisms of exRNA generation, secretion, and transport
2. Identify and develop a catalog of exRNA found in normal human body fluids
3. Investigate the potential for using exRNAs in the clinic as therapeutic molecules or biomarkers of disease

## Data Access

The ERCC Regulatory Element dataset is referenced by other resources in the knowledge graph registry, but access to the primary data may be restricted. Interested researchers should contact the ERCC directly via the exRNA portal for information on data availability and access procedures.

## Related Resources

For more information about exRNA research and related datasets, you can visit:

- [exRNA Portal](https://exrna.org/)
- [exRNA Atlas](https://exrna-atlas.org/)
- [NIH Common Fund - ERCC](https://commonfund.nih.gov/Exrna)

The exRNA Atlas contains small RNA sequencing and qPCR-derived exRNA profiles from human and mouse biofluids, processed using standardized pipelines and quality metrics.