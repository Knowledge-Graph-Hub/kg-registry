---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://groups.google.com/forum/#!forum/faldo
  label: FALDO Google Group
description: FALDO (Feature Annotation Location Description Ontology) is an ontology
  for describing sequence feature locations using RDF/OWL. It provides a standardized
  way to represent genomic and protein sequence positions, regions, and strands in
  Semantic Web formats.
domains:
- genomics
- biological systems
- information technology
homepage_url: http://biohackathon.org/resource/faldo
id: faldo
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: FALDO
products:
- category: OntologyProduct
  description: FALDO ontology in Turtle/RDF format for describing feature locations
    on sequences
  format: ttl
  id: faldo.ttl
  name: FALDO Ontology (Turtle)
  original_source:
  - faldo
  product_file_size: 13615
  product_url: http://biohackathon.org/resource/faldo.ttl
- category: OntologyProduct
  description: FALDO ontology in RDF/XML format
  format: rdfxml
  id: faldo.rdf
  name: FALDO Ontology (RDF/XML)
  original_source:
  - faldo
  product_file_size: 25812
  product_url: http://biohackathon.org/resource/faldo.rdf
- category: DocumentationProduct
  description: Interactive ontology browser with class and property descriptions
  format: http
  id: faldo.browser
  name: FALDO Ontology Browser
  original_source:
  - faldo
  product_url: http://biohackathon.org/resource/faldo
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
repository: https://github.com/OBioFoundry/FALDO
synonyms:
- Feature Annotation Location Description Ontology
---
# FALDO

## Overview

FALDO (Feature Annotation Location Description Ontology) is an ontology designed to describe the locations of sequence features in a Species Web-compatible manner using RDF and OWL. Created during the BioHackathon 2012 and 2013 meetings, FALDO provides a standardized vocabulary for representing genomic and protein sequence positions, regions, and their associated properties such as strand orientation.

## Purpose

FALDO addresses the need for a consistent way to represent sequence feature locations across different biological databases and formats. It enables:

- Interoperability between genomic databases using Semantic Web technologies
- Standardized representation of sequence coordinates
- Support for both exact and fuzzy position descriptions
- Strand-aware position annotations
- Integration with existing formats like GFF3, GTF, and INSDC

## Key Concepts

### Position Types

FALDO defines several types of positions:

1. **ExactPosition**: Precisely known positions with specific coordinate values
2. **FuzzyPosition**: Positions without exact data
3. **InBetweenPosition**: Positions between two exact positions (e.g., restriction enzyme cut sites)
4. **InRangePosition**: Positions known to be within a range
5. **OneOfPosition**: Position known to be one of several specified locations

### Strand Information

- **ForwardStrandPosition**: Position on forward/positive (5' to 3') strand ('+' in GFF3)
- **ReverseStrandPosition**: Position on reverse/complement (3' to 5') strand ('-' in GFF3)
- **BothStrandsPosition**: Feature on both strands
- **StrandedPosition**: Parent class when strand is known

### Regions and Collections

- **Region**: Length of sequence with start and end positions representing a feature
- **CollectionOfRegions**: Multiple regions (e.g., join() and order() in INSDC)
- **ListOfRegions**: Ordered list of regions
- **BagOfRegions**: Unordered collection of regions

### Protein-Specific

- **N-TerminalPosition**: Start of protein/polypeptide (free amine group)
- **C-TerminalPosition**: End of protein/polypeptide (free carboxyl group)

## Coordinate System

- **1-based closed coordinates**: First amino acid or nucleotide has position value 1
- **Nucleotide sequences**: Count from 5' end
- **Amino acid sequences**: Count from N-terminus
- **Reference-based**: Position values anchored to a reference sequence (contig, chromosome, etc.)

## Properties

### Core Properties

- **location**: Links a feature to its position or region
- **begin**: Inclusive beginning of a position (start)
- **end**: Inclusive end of a position
- **reference**: Resource that position value is anchored to
- **position**: Offset along reference (integer ≥ 1)
- **before/after**: For InBetweenPosition descriptions

## Use Cases

1. **Genome Annotation**: Describing gene, exon, and other feature locations
2. **Protein Annotation**: Marking active sites, domains, and motifs
3. **Data Integration**: Combining genomic data from multiple sources
4. **Format Conversion**: Translating between GFF3, GTF, and RDF representations
5. **Semantic Queries**: SPARQL queries across genomic databases
6. **Linked Data**: Connecting genomic features across resources

## Format Compatibility

FALDO can represent features from:
- GFF3 (General Feature Format)
- GTF (Gene Transfer Format)
- INSDC feature tables
- UniProt feature annotations

## Serialization Formats

Available in multiple RDF serializations:
- **Turtle (.ttl)**: Human-readable RDF format
- **RDF/XML (.rdf)**: XML-based RDF format

## Example Usage

FALDO allows expressing locations like:
- "Gene X is located on chromosome 1 from position 1000 to 2000 on the forward strand"
- "Cleavage site is between amino acids 42 and 43"
- "Binding site is somewhere between positions 100 and 150"

## Management

**Creation**: BioHackathon 2012 and 2013

**Maintenance**: Community-maintained through GitHub

**Support**: Google Groups forum for discussions

**Repository**: https://github.com/OBioFoundry/FALDO

## Funding

FALDO development has been supported by:
- National Bioscience Database Center (NBDC) of Japan Science and Technology Agency (JST)
- Database Center for Life Science (DBCLS)
- Research Organization of Information and Systems (ROIS)
- Swiss Institute of Bioinformatics (SIB)
- Swiss Federal Government (SERI)
- NIH (R24OD011883)
- U.S. Department of Energy (DE-AC02-05CH11231)
- Scottish Government Rural and Environmental Research and Analysis Directorate
- DNA Databank of Japan (DDBJ)

## License

Licensed under Creative Commons Zero (CC0 1.0) - Public Domain Dedication

## Related Standards

- SPIN (SPARQL Inferencing Notation)
- OWL (Web Ontology Language)
- RDF (Resource Description Framework)

## Community

- **Discussion Forum**: https://groups.google.com/forum/#!forum/faldo
- **Documentation**: https://github.com/OBF/FALDO
- **Ontology Browser**: http://biohackathon.org/resource/faldo