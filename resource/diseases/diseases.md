---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: qingyao.huang@uzh.ch
  label: Qingyao Huang
- category: Organization
  contact_details:
  - contact_type: url
    value: https://jensenlab.org/
  label: JensenLab
description: DISEASES is a weekly updated database that integrates evidence on disease-gene
  associations from automatic text mining, manually curated literature, cancer mutation
  data, and genome-wide association studies. It provides confidence scores to facilitate
  comparison of different types and sources of evidence.
domains:
- health
- genomics
- biomedical
- literature
homepage_url: https://diseases.jensenlab.org/
id: diseases
infores_id: diseases
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: DISEASES
products:
- category: GraphicalInterface
  description: Web search interface for querying human genes and diseases to view
    integrated evidence from multiple channels
  format: http
  id: diseases.portal
  name: DISEASES Web Search
  original_source:
  - diseases
  product_url: https://diseases.jensenlab.org/
- category: Product
  description: Disease-gene associations from text mining channel with z-scores and
    confidence scores (full dataset)
  format: tsv
  id: diseases.textmining-full
  name: Text Mining Channel (Full)
  product_file_size: 1920661253
  product_url: https://download.jensenlab.org/human_disease_textmining_full.tsv
- category: Product
  description: Disease-gene associations from text mining channel with z-scores and
    confidence scores (filtered non-redundant)
  format: tsv
  id: diseases.textmining-filtered
  name: Text Mining Channel (Filtered)
  product_file_size: 48652618
  product_url: https://download.jensenlab.org/human_disease_textmining_filtered.tsv
- category: Product
  description: Disease-gene associations from manually curated knowledge channel with
    evidence types and confidence scores (full dataset)
  format: tsv
  id: diseases.knowledge-full
  name: Knowledge Channel (Full)
  product_file_size: 6883980
  product_url: https://download.jensenlab.org/human_disease_knowledge_full.tsv
- category: Product
  description: Disease-gene associations from manually curated knowledge channel with
    evidence types and confidence scores (filtered non-redundant)
  format: tsv
  id: diseases.knowledge-filtered
  name: Knowledge Channel (Filtered)
  product_file_size: 602129
  product_url: https://download.jensenlab.org/human_disease_knowledge_filtered.tsv
- category: Product
  description: Disease-gene associations from experimental data channel including
    cancer mutations and GWAS with source scores and confidence scores (full dataset)
  format: tsv
  id: diseases.experiments-full
  name: Experiments Channel (Full)
  product_file_size: 26901903
  product_url: https://download.jensenlab.org/human_disease_experiments_full.tsv
- category: Product
  description: Disease-gene associations from experimental data channel including
    cancer mutations and GWAS with source scores and confidence scores (filtered non-redundant)
  format: tsv
  id: diseases.experiments-filtered
  name: Experiments Channel (Filtered)
  product_file_size: 2567625
  product_url: https://download.jensenlab.org/human_disease_experiments_filtered.tsv
- category: Product
  description: Experimental integrated channel combining evidence from all sources
    (full dataset)
  format: tsv
  id: diseases.integrated-full
  name: Integrated Channel (Full)
  product_file_size: 648296693
  product_url: https://download.jensenlab.org/human_disease_integrated_full.tsv
- category: Product
  compression: targz
  description: Dictionary of human gene and disease names for the DISEASES tagger
  id: diseases.dictionary
  name: DISEASES Dictionary
  product_file_size: 15984342
  product_url: https://download.jensenlab.org/diseases_dictionary.tar.gz
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: Product
  description: Manually curated disease-gene associations and annotations for amyloidoses
    and amyloid deposition-related diseases extracted from biomedical literature.
  id: amyco.annotations
  name: AmyCo Curated Annotations
  original_source:
  - pubmed
  - amyco
  secondary_source:
  - diseases
publications:
- id: PMID:35348650
  preferred: true
- id: PMID:25484339
synonyms:
- DISEASES Database
- JensenLab DISEASES
taxon:
- NCBITaxon:9606
---
# DISEASES

## Overview

DISEASES is a comprehensive database that integrates disease-gene associations from multiple evidence sources. Maintained by the JensenLab and currently hosted at the Swiss Institute of Bioinformatics (University of Zurich), it provides weekly updated data combining automatic text mining, manually curated knowledge, cancer mutation data, and genome-wide association studies. The resource assigns unified confidence scores to facilitate comparison across different types of evidence.

## Data Content

DISEASES integrates disease-gene associations through four main channels:

### 1. Text Mining Channel
- Automatic extraction of disease-gene mentions from scientific literature
- Z-scores indicating co-mention strength
- Confidence scores for each association
- Links to underlying abstracts

### 2. Knowledge Channel
- Manually curated disease-gene associations from literature
- Evidence type classification
- Source database attribution
- Confidence scores

### 3. Experiments Channel
- Cancer mutation data
- Genome-wide association study (GWAS) results
- Source scores from original databases
- Confidence scores

### 4. Integrated Channel
- Experimental combination of all evidence sources
- Unified confidence scoring across channels
- Non-redundant filtered associations

## Data Organization

All downloadable files contain:
- Gene identifier and name
- Disease identifier and name
- Channel-specific evidence metrics
- Confidence scores for comparison

**Full datasets**: Complete associations from the database
**Filtered datasets**: Non-redundant associations shown in the web interface

## Key Features

- **Weekly Updates**: Regular integration of new evidence from literature and databases
- **Multiple Evidence Types**: Text mining, curated knowledge, experimental data
- **Confidence Scores**: Unified scoring system for comparing evidence quality
- **Human-Specific**: Focus on human disease-gene associations
- **Open Access**: All data available under CC BY 4.0 license
- **Interactive Search**: Web interface for exploring associations

## Access Methods

- **Web Interface**: Search and browse at https://diseases.jensenlab.org/
- **Direct Downloads**: TSV files for each channel (full and filtered)
- **Dictionary**: Gene and disease name dictionary for local text mining
- **Historical Data**: Previous versions archived on figshare

## Download Products

Each channel available in two versions:
1. **Full**: All associations in the database
2. **Filtered**: Non-redundant associations (shown in web interface)

Additional resources:
- DISEASES tagger for local installation (Unix platforms)
- Disease and gene name dictionary
- Benchmark dataset from original publication
- List of excluded PubMed IDs (papermill publications)

## Use Cases

1. **Disease Gene Discovery**: Identify candidate genes for diseases of interest
2. **Literature Mining**: Access text-mined associations from biomedical literature
3. **Evidence Integration**: Compare multiple lines of evidence for disease-gene links
4. **Network Analysis**: Build disease-gene networks for systems biology studies
5. **Validation**: Benchmark other disease-gene prediction methods
6. **Local Text Mining**: Use dictionary and tagger for custom analyses

## Management

**Current Maintainer**: Qingyao Huang (Swiss Institute of Bioinformatics, University of Zurich)

**Original Developers**:
- Sune Frankild
- Alexander Junge
- Albert Pallejà
- Dhouha Grissa
- Kalliopi Tsafou
- Lars Juhl Jensen

**Affiliation**: Novo Nordisk Foundation Center for Protein Research

## Funding

- Novo Nordisk Foundation (NNF14CC0001)
- National Institutes of Health (U54 CA189205, U24 224370)
- European Union's Seventh Framework Programme (n259348)

## License

Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## Citation

**Primary Publication**:
Grissa, D., Junge, A., Oprea, T. I., & Jensen, L. J. (2022). DISEASES 2.0: a weekly updated database of disease–gene associations from text mining and data integration. *Database*, 2022, baac019. https://doi.org/10.1093/database/baac019 (PMID: 35348650)

**Original Publication**:
Pletscher-Frankild, S., Pallejà, A., Tsafou, K., Binder, J. X., & Jensen, L. J. (2015). DISEASES: Text mining and data integration of disease–gene associations. *Methods*, 74, 83-89. (PMID: 25484339)