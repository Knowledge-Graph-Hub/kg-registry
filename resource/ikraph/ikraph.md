---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jinfeng@insilicom.com
  label: Jinfeng Zhang
creation_date: '2025-07-22T00:00:00Z'
curators:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://insilicom.com/
  label: Insilicom
description: A large-scale biomedical knowledge graph assembled from PubMed abstracts,
  containing over 22 million entities and 120 million relations.
domains:
- health
- biomedical
- drug discovery
- translational
- genomics
homepage_url: https://biokde.insilicom.com/
id: ikraph
last_modified_date: '2025-07-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: iKraph
products:
- category: GraphicalInterface
  description: Biomedical Knowledge Discovery Engine. Interface for iKraph with search,
    visualization, and exploration capabilities.
  format: http
  id: ikraph.site
  name: BioKDE
  original_source:
  - ikraph
  product_url: https://biokde.insilicom.com/
  secondary_source:
  - ikraph
- category: ProcessProduct
  description: Code for named entity recognition, relation extraction, and drug repurposing
    in assembly and analysis of iKraph
  id: ikraph.code
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.en.html
    label: GPL-3
  name: iKraph Code
  original_source:
  - ikraph
  product_url: https://github.com/myinsilicom/iKraph
  repository: https://github.com/myinsilicom/iKraph
  secondary_source:
  - ikraph
- category: GraphProduct
  compression: targz
  description: Graph metadata for iKraph, including a list of relations, entity type-specific
    metadata, data sources, and drug repurposing predictions.
  format: json
  id: ikraph.graph
  name: iKraph graph metadata
  original_source:
  - ikraph
  product_file_size: 61183533
  product_url: https://zenodo.org/records/14851275/files/data.tar.gz?download=1
  secondary_source:
  - ikraph
- category: GraphProduct
  compression: targz
  description: Complete graph data for iKraph with all entities and relations extracted
    from PubMed abstracts
  id: ikraph.graphdata
  name: iKraph graph data
  original_source:
  - ikraph
  product_file_size: 1440676039
  product_url: https://zenodo.org/records/14851275/files/iKraph_full.tar.gz?download=1
  secondary_source:
  - ikraph
publications:
- authors:
  - Zhang Y
  - Sui X
  - Pan F
  - Yu K
  - Li K
  - Tian S
  - Erdengasileng A
  - Han Q
  - Wang W
  - Wang J
  - Wang J
  - Sun D
  - Chung H
  - Zhou J
  - Zhou E
  - Lee B
  - Zhang P
  - Qiu X
  - Zhao T
  - Zhang J
  doi: 10.1038/s42256-025-01014-w
  id: doi:10.1038/s42256-025-01014-w
  journal: Nature Machine Intelligence
  preferred: true
  title: A comprehensive large-scale biomedical knowledge graph for AI-powered data-driven
    biomedical research
  year: '2025'
repository: https://github.com/myinsilicom/iKraph
---
# iKraph Knowledge Graph

iKraph is a comprehensive large-scale biomedical knowledge graph developed by Insilicom for AI-powered data-driven biomedical research. It represents one of the largest structured biomedical knowledge resources assembled from literature mining.

## Overview

iKraph was constructed by applying advanced natural language processing and relation extraction techniques to the entire corpus of PubMed abstracts. The knowledge graph contains over 22 million biomedical entities and 120 million relations, covering a wide range of biomedical concepts including genes, proteins, diseases, drugs, pathways, and phenotypes.

The primary goal of iKraph is to enable knowledge discovery and hypothesis generation for biomedical research and drug development. It integrates information across multiple domains to support various applications:

- Drug repurposing and discovery
- Target identification
- Biomarker discovery
- Disease mechanism exploration
- Precision medicine approaches

## Technical Details

iKraph employs a sophisticated named entity recognition and relation extraction pipeline to process biomedical literature at scale. The pipeline includes:

1. Named entity recognition for biomedical concepts
2. Relation extraction between identified entities
3. Knowledge graph construction and normalization
4. Integration with other biomedical resources
5. Quality assurance and validation

The knowledge graph is accessible through the BioKDE (Biomedical Knowledge Discovery Engine) web interface, which provides search, visualization, and exploration capabilities for researchers.

## Applications

iKraph has been successfully applied to several biomedical research areas:

- Identification of novel drug candidates for various diseases
- Discovery of previously unknown gene-disease associations
- Understanding of complex disease mechanisms
- Prediction of drug-drug interactions
- Personalized treatment recommendations

## Citation

If you use iKraph in your research, please cite:

Zhang Y, Sui X, Pan F, et al. A comprehensive large-scale biomedical knowledge graph for AI-powered data-driven biomedical research. Nature Machine Intelligence. 2025. https://doi.org/10.1038/s42256-025-01014-w