---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: sergio.baranzini@ucsf.edu
  label: Sergio Baranzini
- category: Individual
  contact_details:
  - contact_type: url
    value: https://isbscience.org/
  label: Sui Huang
- category: Organization
  label: University of California, San Francisco
creation_date: '2025-03-09T00:00:00Z'
description: Scalable Precision Medicine Open Knowledge Engine (SPOKE) is a comprehensive
  biomedical knowledge graph that connects diverse data from multiple domains to enable
  discovery and precision medicine applications.
domains:
- biomedical
- genomics
- clinical
- drug discovery
- precision medicine
- pharmacology
homepage_url: https://spoke.ucsf.edu/
id: spoke
infores_id: spoke
last_modified_date: '2026-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://spoke.rbvi.ucsf.edu/docs/licenses.html
  label: Multiple licenses (see individual data sources)
name: SPOKE
products:
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: ProgrammingInterface
  description: REST API for programmatic access to SPOKE, including node and edge
    types, neighborhoods, and the metagraph.
  format: http
  id: spoke.api
  is_public: true
  name: SPOKE REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke
  product_url: https://spoke.rbvi.ucsf.edu/swagger/
- category: DocumentationProduct
  description: Documentation of each SPOKE node and edge type and the data source
    it is drawn from.
  format: http
  id: spoke.nodes-edges-docs
  name: SPOKE Nodes and Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke
  product_url: https://spoke.rbvi.ucsf.edu/docs/index.html
- category: GraphicalInterface
  description: Web interface that allows searching SPOKE for a node of interest and
    viewing its immediate connectivity neighborhood.
  format: http
  id: spoke.neighborhood_explorer
  name: SPOKE Neighborhood Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke
  product_url: https://spoke.rbvi.ucsf.edu/neighborhood.html
- category: ProgrammingInterface
  description: SPARQL endpoint for querying the SPOKE knowledge graph through the
    Open Knowledge Network (OKN) query service
  format: http
  id: spoke.sparql
  name: SPOKE SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke
  product_url: https://apps.okn.us/spoke-okn/sparql
- category: DocumentationProduct
  description: SPOKE data and tools page describing access paths, visualizations,
    and related resources.
  format: http
  id: spoke.docs
  name: SPOKE Data and Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphProduct
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  format: ttl
  id: spoke-okn.graph
  name: SPOKE-OKN Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke-okn
  - relation_type: prov:wasDerivedFrom
    source: spoke
  product_url: https://spoke.ucsf.edu
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bgee
  - relation_type: prov:wasInfluencedBy
    source: bindingdb
  - relation_type: prov:wasInfluencedBy
    source: bv-brc
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: civic
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  - relation_type: prov:wasInfluencedBy
    source: diseases
  - relation_type: prov:wasInfluencedBy
    source: doid
  - relation_type: prov:wasInfluencedBy
    source: drugbank
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: foodb
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: gwascatalog
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: interpro
  - relation_type: prov:wasInfluencedBy
    source: kegg
  - relation_type: prov:wasInfluencedBy
    source: lincs-l1000
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: metacyc
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: ncbitaxon
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pathophenodb
  - relation_type: prov:wasInfluencedBy
    source: pfam
  - relation_type: prov:wasInfluencedBy
    source: pid
  - relation_type: prov:wasInfluencedBy
    source: protcid
  - relation_type: prov:wasInfluencedBy
    source: pubmed
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: sider
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
publications:
- authors:
  - John H Morris
  - Karthik Soman
  - Rabia E Akbas
  - Xiaoyuan Zhou
  - Brett Smith
  - Elaine C Meng
  - Conrad C Huang
  - Gabriel Cerono
  - Gundolf Schenk
  - Angela Rizk-Jackson
  - Adil Harroud
  - Lauren Sanders
  - Sylvain V Costes
  - Krish Bharat
  - Arjun Chakraborty
  - Alexander R Pico
  - Taline Mardirossian
  - Michael Keiser
  - Alice Tang
  - Josef Hardi
  - Yongmei Shi
  - Mark Musen
  - Sharat Israni
  - Sui Huang
  - Peter W Rose
  - Charlotte A Nelson
  - Sergio E Baranzini
  doi: 10.1093/bioinformatics/btad080
  id: https://doi.org/10.1093/bioinformatics/btad080
  journal: Bioinformatics
  preferred: true
  title: 'The scalable precision medicine open knowledge engine (SPOKE): a massive
    knowledge graph of biomedical information'
  year: '2023'
- authors:
  - Karthik Soman
  - Peter W Rose
  - John H Morris
  - Rabia E Akbas
  - Brett Smith
  - Braian Peetoom
  - Catalina Villouta-Reyes
  - Gabriel Cerono
  - Yongmei Shi
  - Angela Rizk-Jackson
  - Sharat Israni
  - Charlotte A Nelson
  - Sui Huang
  - Sergio E Baranzini
  doi: 10.1093/bioinformatics/btae560
  id: https://doi.org/10.1093/bioinformatics/btae560
  journal: Bioinformatics
  title: Biomedical knowledge graph-optimized prompt generation for large language
    models
  year: '2024'
- authors:
  - Sergio E Baranzini
  - Katy Börner
  - John Morris
  - Charlotte A Nelson
  - Karthik Soman
  - Erica Schleimer
  - Michael Keiser
  - Mark Musen
  - Roger Pearce
  - Tahsin Reza
  - Brett Smith
  - Bruce W Herr
  - Boris Oskotsky
  - Angela Rizk-Jackson
  - Katherine P Rankin
  - Stephan J Sanders
  - Riley Bove
  - Peter W Rose
  - Sharat Israni
  - Sui Huang
  doi: 10.1002/aaai.12037
  id: https://doi.org/10.1002/aaai.12037
  journal: AI Magazine
  title: A biomedical open knowledge network harnesses the power of AI to understand
    deep human biology
  year: '2022'
- authors:
  - Charlotte A Nelson
  - Atul J Butte
  - Sergio E Baranzini
  doi: 10.1038/s41467-019-11069-0
  id: https://doi.org/10.1038/s41467-019-11069-0
  journal: Nature Communications
  title: Integrating biomedical research and electronic health records to create knowledge-based
    biologically meaningful machine-readable embeddings
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
  doi: 10.7554/eLife.26726
  id: https://doi.org/10.7554/eLife.26726
  journal: eLife
  title: Systematic integration of biomedical knowledge prioritizes drugs for repurposing
  year: '2017'
repository: https://github.com/BaranziniLab
taxon:
- NCBITaxon:9606
---
SPOKE (Scalable Precision Medicine Open Knowledge Engine) is a comprehensive biomedical knowledge graph developed at the University of California, San Francisco (UCSF). It integrates data from dozens of public databases to create a rich network of biomedical relationships.

SPOKE is a heterogeneous network, containing different types of nodes (e.g., genes, diseases, drugs, pathways) and the edges between them represent known connections. The knowledge graph pulls data out of silos, connecting diverse information from molecular research, clinical insights, and environmental data.

SPOKE enables a wide variety of applications including suggesting testable hypotheses for researchers, implicating mechanisms of disease, and enabling more precise diagnoses and treatments for individual patients. It has been used in studies for drug repurposing, disease prediction, and integrating electronic health records with biomedical knowledge. SPOKE data are updated on a rotating weekly schedule rather than in numbered releases. SPOKE is available for both academic and commercial use; commercial licensing is handled through Mate Bioservices. Sui Huang (Institute for Systems Biology) and Sharat Israni are lead investigators alongside Sergio Baranzini.

In KG-Registry, the owned products capture the main SPOKE access points, while the detailed original-source provenance on the graph product records the many upstream resources incorporated into the network.

## Evaluation

- View the evaluation: [spoke evaluation](spoke_eval.html)