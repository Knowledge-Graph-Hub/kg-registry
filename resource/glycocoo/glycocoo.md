---
activity_status: active
category: Ontology
creation_date: '2025-10-29T00:00:00Z'
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: "yamadaissaku"
      - contact_type: email
        value: "issaku@noguchi.or.jp"
    label: Issaku Yamada
  - category: Individual
    contact_details:
      - contact_type: email
        value: "m.campbell@griffith.edu.au"
    label: Matthew P Campbell
  - category: Individual
    contact_details:
      - contact_type: email
        value: "kkiyoko@soka.ac.jp"
    label: Kiyoko F Aoki-Kinoshita
description: The Glycoconjugate Ontology (GlycoCoO) is a standard semantic framework for describing and representing glycoproteomics and glycolipidomics data in RDF format. It provides a formal representation of glycoconjugate structures (glycoproteins and glycolipids), their associated metadata including publication information, biological source data, experimental evidence, and abundance ratios. GlycoCoO extends GlycoRDF by creating subclasses of ReferencedCompound including ReferencedGlycoconjugate, ReferencedProtein, and ReferencedLipid, enabling comprehensive annotation of glycan structures attached to proteins and lipids with contextual information such as glycosylation sites, disease associations, tissue and cell line sources, and analytical methods. The ontology supports both complete structural information and compositional data, can represent single glycans or glycoform mixtures at specific sites, and accommodates partially missing site information when no mapping is performed. It has been adopted by major glycoproteomics databases including UniCarbKB, GlyConnect, and GlycoNAVI, enabling federated queries across resources to retrieve integrated information about glycoconjugates from multiple publications and experimental contexts.
domains:
  - chemistry and biochemistry
  - biological systems
  - biomedical
homepage_url: https://github.com/glycoinfo/GlycoCoO
id: "glycocoo"
last_modified_date: '2025-10-29T00:00:00Z'
layout: resource_detail
name: GlycoConjugate Ontology (GlycoCoO)
publications:
  - authors:
      - Issaku Yamada
      - Matthew P Campbell
      - Nathan Edwards
      - Leyla Jael Castro
      - Frederique Lisacek
      - Julien Mariethoz
      - Tamiko Ono
      - Rene Ranzinger
      - Daisuke Shinmachi
      - Kiyoko F Aoki-Kinoshita
    category: Publication
    id: "https://doi.org/10.1093/glycob/cwab013"
    journal: Glycobiology
    preferred: true
    title: 'The glycoconjugate ontology (GlycoCoO) for standardizing the annotation of glycoconjugate data and its application'
    year: "2021"
products:
  - category: OntologyProduct
    description: The GlycoCoO OWL ontology file defining classes and predicates for glycoconjugate structures and their metadata
    format: owl
    id: "glycocoo.ontology"
    name: GlycoCoO OWL Ontology
    product_url: https://github.com/glycoinfo/GlycoCoO/blob/master/ontology/glycocoo.owl
  - category: DocumentationProduct
    description: GitHub Wiki with developer information, database providers, and prefix documentation
    format: http
    id: "glycocoo.wiki"
    name: GlycoCoO Wiki Documentation
    product_url: https://github.com/glycoinfo/GlycoCoO/wiki
  - category: Product
    description: Sample RDF data files demonstrating GlycoCoO usage with examples from UniCarbKB, GlyConnect, and GlycoNAVI
    format: http
    id: "glycocoo.rdf-samples"
    name: GlycoCoO RDF Sample Data
    product_url: https://github.com/glycoinfo/GlycoCoO/tree/master/RDF_Sample
  - category: Product
    description: Example SPARQL queries for querying glycoconjugate data across federated endpoints
    format: http
    id: "glycocoo.sparql-examples"
    name: GlycoCoO SPARQL Query Examples
    product_url: https://github.com/glycoinfo/GlycoCoO/blob/master/SPARQL_Query.md
---

# GlycoConjugate Ontology (GlycoCoO)

## Overview

The Glycoconjugate Ontology (GlycoCoO) is a standard semantic framework developed to address the need for digital standards in representing glycoproteins and glycolipids. It provides a comprehensive ontology for describing glycoconjugate structures and their functions, enabling the integration of glycoproteomics and glycolipidomics data within the Semantic Web ecosystem.

## Motivation and Background

Recent advances in glycoproteomics protocols have led to a sustainable increase in reporting proteins with their attached glycans and glycosylation sites. However, very few of these reports are deposited into databases due to the absence of digital standards. GlycoCoO addresses this challenge by providing a framework that can:

- Represent glycans as complete structures or compositions
- Store single glycans or represent glycoforms on specific glycosylation sites
- Handle partially missing site information when no site mapping is performed
- Store abundances or ratios of glycans within a glycoform of a specific site

## Ontology Structure

GlycoCoO extends the GlycoRDF ontology by creating specialized subclasses:

### Core Classes

- **ReferencedGlycoconjugate**: Represents glycoconjugates (glycoproteins and glycolipids) with their associated metadata
- **ReferencedProtein**: Describes proteins with glycosylation site information using FALDO (Feature Annotation Location Description Ontology)
- **ReferencedLipid**: Represents lipid components of glycolipids
- **Compound**: The superclass encompassing glycan structures, typically pointing to GlyTouCan IDs
- **Citation**: Publication and bibliographic information using Dublin Core and Bibliographic Ontology
- **Source**: Biological source information including tissue, cell line, and taxonomy using Uberon and Cell Ontology
- **Evidence**: Experimental evidence with subclasses for analytical methods (NMR, LC, MS)

### Relationship to GlycoRDF

GlycoCoO reuses and extends GlycoRDF concepts by maintaining the ReferencedCompound mechanism for linking compounds with their evidence, source, and citation information. This approach allows the same glycan to be described with different metadata sets from different publications or experimental contexts.

## Implementation and Adoption

GlycoCoO has been adopted by major glycoproteomics databases:

### UniCarbKB
- Provides approximately 1,530 glycoprotein entries
- Contains over 4,000 annotated glycosylation sites
- Includes 4,000 glycan structures (partial and fully defined)
- SPARQL endpoint: http://sparql.unicarbkb.org

### GlyConnect
- Features 22,600 glycosylation sites on roughly 2,200 UniProtKB-referenced glycoproteins
- Contains almost 4,000 glycans and 3,400 glycosylation sites
- Supported by 900 articles
- Includes 3,300 human N- and O-glycopeptides
- SPARQL endpoint: https://glyconnect.expasy.org/rdf

### GlycoNAVI
- Stores information on glycan abundance ratios of glycoforms
- Contains 1,297 glycans, 178 abundance ratio data points
- Includes 102 disease states, 9 tissues, and 178 articles
- SPARQL endpoint: https://sparql.glyconavi.org/sparql

## Applications and Benefits

The adoption of GlycoCoO enables:

1. **Federated Queries**: Single SPARQL queries can retrieve integrated information from multiple databases simultaneously
2. **Data Integration**: Common glycans and metadata can be identified across different resources
3. **Disease Association Analysis**: Disease annotations and their citations can be accumulated from diverse sources
4. **Source Tracking**: Biological source information including tissues, cell lines, and organisms can be traced across databases
5. **Publication Integration**: Overlapping and unique publications can be identified across resources

## Technical Features

- **Semantic Web Compatibility**: Uses RDF triples for data representation enabling SPARQL queries
- **Ontology Reuse**: Integrates established ontologies including UniProt Core, Bibliographic Ontology, DCMI, HUPO-PSI-MS, Uberon, Cell Ontology, Gene Ontology, Disease Ontology, and Cellosaurus
- **Flexible Data Model**: Accommodates both complete structural information and partial/compositional data
- **Site-Specific Annotation**: Supports detailed annotation of glycosylation sites using FALDO for precise position information
- **Abundance Data**: Can represent quantitative information about glycan abundance and ratios

## Development and Maintenance

GlycoCoO was developed through international collaboration:

- Originated at the Japanese BioHackathon 2012
- Further developed at the Glyco-BioHackathon China 2013
- Maintained on GitHub with contributions from multiple developers
- Available through BioPortal for ontology browsing
- Version controlled using Semantic Versioning

The ontology is continuously updated and maintained by a consortium of glycoinformatics researchers from institutions worldwide, including the National Bioscience Database Center (NBDC) of JST, Glycoinformatics Consortium (GLIC), Institute for Glycomics (Griffith University), and Swiss Institute of Bioinformatics.

## Standardization and Prefixes

GlycoCoO uses standardized prefixes for consistent data representation:

- `gco:` - http://purl.jp/bio/12/glyco/conjugate#
- `glycan:` - http://purl.jp/bio/12/glyco/glycan#
- `faldo:` - http://biohackathon.org/resource/faldo#
- `sio:` - http://semanticscience.org/resource/
- `codao:` - http://purl.glycoinfo.org/ontology/codao#

## Future Directions

The GlycoCoO framework continues to evolve with plans for:

- Integration with the Protein Ontology (PRO) to capture glycoproteoform complexity
- Expansion to lipid ontologies for comprehensive glycolipid representation
- Development of a glycoconjugate repository with unique accession numbers
- Enhanced support for heterogeneity in site-specific protein glycosylation
- Integration with GlyGen for comprehensive glycoscience data resources
