---
layout: resource_detail
activity_status: active
id: spoke
name: SPOKE
description: Scalable Precision Medicine Open Knowledge Engine (SPOKE) is a comprehensive biomedical knowledge graph that connects diverse data from multiple domains to enable discovery and precision medicine applications.
domains:
- biomedical
- health
- genomics
- clinical
- drug discovery
- precision medicine
- pharmacology
category: KnowledgeGraph
contacts:
- category: Individual
  label: "Sergio Baranzini"
  contact_details:
  - contact_type: email
    value: sergio.baranzini@ucsf.edu
- category: Individual
  label: "Sui Huang"
  contact_details:
  - contact_type: email
    value: sui.huang@ucsf.edu
- category: Organization
  label: "University of California, San Francisco"
homepage_url: https://spoke.ucsf.edu/
repository: "https://github.com/baranzini-lab/SPOKE"
license:
  id: https://spoke.rbvi.ucsf.edu/docs/licenses.html
  label: "Multiple licenses (see individual data sources)"
version: "2.0"
publications:
- id: https://doi.org/10.1093/bioinformatics/btad080
  title: "The scalable precision medicine open knowledge engine (SPOKE): a massive knowledge graph of biomedical information"
  authors:
  - "John H Morris"
  - "Karthik Soman"
  - "Riley E Akbas"
  - "X Zhou"
  - "B Smith"
  - "Elaine C Meng"
  - "CC Huang"
  - "Gabriel Cerono"
  - "G Schenk"
  - "Angela Rizk-Jackson"
  - "Sergio E Baranzini"
  journal: "Bioinformatics"
  year: "2023"
  preferred: true
- id: https://doi.org/10.1038/s41467-019-11069-0
  title: "Integrating biomedical research and electronic health records to create knowledge-based biologically meaningful machine-readable embeddings"
  authors:
  - "Charlotte A Nelson"
  - "Atul J Butte"
  - "Sergio E Baranzini"
  journal: "Nature Communications"
  year: "2019"
- id: https://doi.org/10.7554/eLife.26726
  title: "Systematic integration of biomedical knowledge prioritizes drugs for repurposing"
  authors:
  - "Daniel Scott Himmelstein"
  - "Antoine Lizee"
  - "Christine Hessler"
  - "Leo Brueggeman"
  - "Sabrina L Chen"
  - "Dexter Hadley"
  - "Ari Green"
  - "Pouya Khankhanian"
  - "Sergio E Baranzini"
  journal: "eLife"
  year: "2017"
products:
- id: spoke.graph
  name: SPOKE Graph
  description: "The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources."
  category: GraphProduct
  original_source:
  - spoke
  secondary_source:
  - spoke
- id: spoke.neighborhood_explorer
  name: SPOKE Neighborhood Explorer
  description: "Web interface that allows searching SPOKE for a node of interest and viewing its immediate connectivity neighborhood."
  category: GraphicalInterface
  product_url: https://spoke.rbvi.ucsf.edu/neighborhood.html
---

SPOKE (Scalable Precision Medicine Open Knowledge Engine) is a comprehensive biomedical knowledge graph developed at the University of California, San Francisco (UCSF). It integrates data from over 30 public databases to create a rich network of biomedical relationships. 

SPOKE is a heterogeneous network, containing different types of nodes (e.g., genes, diseases, drugs, pathways) and the edges between them represent known connections. The knowledge graph pulls data out of silos, connecting diverse information from molecular research, clinical insights, and environmental data.

SPOKE enables a wide variety of applications including suggesting testable hypotheses for researchers, implicating mechanisms of disease, and enabling more precise diagnoses and treatments for individual patients. It has been used in studies for drug repurposing, disease prediction, and integrating electronic health records with biomedical knowledge.
