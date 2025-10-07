---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@exrna.org
  label: Extracellular RNA Communication Consortium
description: ERCC RNA Binding Protein dataset (ERCCRBP) is a collection of data focused
  on RNA binding proteins involved in extracellular RNA functions as part of the NIH
  Common Fund's Extracellular RNA Communication Consortium (ERCC) program. This dataset
  provides insights into the protein-RNA interactions important for exRNA stability,
  transport, and signaling.
domains:
- biomedical
- genomics
- chemistry and biochemistry
homepage_url: https://exrna.org/
id: erccrbp
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ERCC RNA Binding Protein Dataset
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
  - cmap
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
  - nposckan
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
  - cmap
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
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
---
# ERCC RNA Binding Protein Dataset

The ERCC RNA Binding Protein Dataset (ERCCRBP) is part of the research conducted by the NIH Common Fund's Extracellular RNA Communication Consortium (ERCC), which explores the biology and function of extracellular RNA (exRNA).

## Overview

RNA binding proteins (RBPs) play critical roles in the biology of extracellular RNA by influencing RNA stability, transport, cellular uptake, and signaling functions. The ERCCRBP dataset focuses on these protein-RNA interactions that are fundamental to understanding exRNA communication between cells and potential applications in biomarker discovery and therapeutics.

## Research Context

This dataset is part of the broader ERCC initiative which aims to:

1. Investigate the roles of RNA binding proteins in exRNA biogenesis, secretion, and transport
2. Characterize RBP-exRNA complexes found in various biofluids
3. Understand how RBPs protect exRNAs from degradation in the extracellular environment
4. Explore the potential of exRNA-RBP interactions as diagnostic biomarkers or therapeutic targets

## Research Findings

Studies of RNA binding proteins associated with extracellular RNA have revealed:
- Specific RBPs are involved in packaging RNAs into extracellular vesicles
- Different subpopulations of exRNAs associate with distinct carrier types, including RBPs
- RBPs can protect exRNAs from degradation by RNases present in biofluids
- The exRNA-RBP complex profile differs across disease states and may serve as sensitive biomarkers

## Data Access

The ERCC RNA Binding Protein dataset is referenced by other resources in the knowledge graph registry, but access to the primary data may be restricted. Interested researchers should contact the ERCC directly via the exRNA portal for information on data availability and access procedures.

## Related Resources

For more information about exRNA research and related datasets, you can visit:

- [exRNA Portal](https://exrna.org/)
- [exRNA Atlas](https://exrna-atlas.org/)
- [NIH Common Fund - ERCC](https://commonfund.nih.gov/Exrna)

The exRNA Atlas contains small RNA sequencing and qPCR-derived exRNA profiles from human and mouse biofluids, processed using standardized pipelines and quality metrics. The ERCCRBP dataset complements these resources by focusing on the protein components of exRNA complexes.