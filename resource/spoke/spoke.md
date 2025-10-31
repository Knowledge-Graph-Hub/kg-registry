---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: sergio.baranzini@ucsf.edu
    label: Sergio Baranzini
  - category: Individual
    contact_details:
      - contact_type: email
        value: sui.huang@ucsf.edu
    label: Sui Huang
  - category: Organization
    label: University of California, San Francisco
description: Scalable Precision Medicine Open Knowledge Engine (SPOKE) is a comprehensive biomedical knowledge graph that connects diverse data from multiple domains to enable discovery and precision medicine applications.
domains:
  - biomedical
  - health
  - genomics
  - clinical
  - drug discovery
  - precision medicine
  - pharmacology
homepage_url: https://spoke.ucsf.edu/
id: spoke
layout: resource_detail
license:
  id: https://spoke.rbvi.ucsf.edu/docs/licenses.html
  label: Multiple licenses (see individual data sources)
name: SPOKE
products:
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
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
  - category: GraphicalInterface
    description: Web interface that allows searching SPOKE for a node of interest and viewing its immediate connectivity neighborhood.
    format: http
    id: spoke.neighborhood_explorer
    name: SPOKE Neighborhood Explorer
    product_url: https://spoke.rbvi.ucsf.edu/neighborhood.html
publications:
  - authors:
      - John H Morris
      - Karthik Soman
      - Riley E Akbas
      - X Zhou
      - B Smith
      - Elaine C Meng
      - CC Huang
      - Gabriel Cerono
      - G Schenk
      - Angela Rizk-Jackson
      - Sergio E Baranzini
    id: https://doi.org/10.1093/bioinformatics/btad080
    journal: Bioinformatics
    preferred: true
    title: 'The scalable precision medicine open knowledge engine (SPOKE): a massive knowledge graph of biomedical information'
    year: '2023'
  - authors:
      - Charlotte A Nelson
      - Atul J Butte
      - Sergio E Baranzini
    id: https://doi.org/10.1038/s41467-019-11069-0
    journal: Nature Communications
    title: Integrating biomedical research and electronic health records to create knowledge-based biologically meaningful machine-readable embeddings
    year: '2019'
  - authors:
      - Daniel Scott Himmelstein
      - Antoine Lizee
      - Christine Hessler
      - Leo Brueggeman
      - Sabrina L Chen
      - Dexter Hadley
      - Ari Green
      - Pouya Khankhanian
      - Sergio E Baranzini
    id: https://doi.org/10.7554/eLife.26726
    journal: eLife
    title: Systematic integration of biomedical knowledge prioritizes drugs for repurposing
    year: '2017'
repository: https://github.com/baranzini-lab/SPOKE
version: '2.0'
infores_id: spoke
---

SPOKE (Scalable Precision Medicine Open Knowledge Engine) is a comprehensive biomedical knowledge graph developed at the University of California, San Francisco (UCSF). It integrates data from over 30 public databases to create a rich network of biomedical relationships. 

SPOKE is a heterogeneous network, containing different types of nodes (e.g., genes, diseases, drugs, pathways) and the edges between them represent known connections. The knowledge graph pulls data out of silos, connecting diverse information from molecular research, clinical insights, and environmental data.

SPOKE enables a wide variety of applications including suggesting testable hypotheses for researchers, implicating mechanisms of disease, and enabling more precise diagnoses and treatments for individual patients. It has been used in studies for drug repurposing, disease prediction, and integrating electronic health records with biomedical knowledge.

## Evaluation

- View the evaluation: [spoke evaluation](spoke_eval.html)
