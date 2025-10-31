---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: expander.agent@gmail.com
  label: Expander Agent Team
- category: Individual
  contact_details:
  - contact_type: email
    value: stephen.ramsey@oregonstate.edu
  label: Stephen Ramsey
- category: Individual
  contact_details:
  - contact_type: email
    value: edeutsch@systemsbiology.org
  label: Eric Deutsch
- category: Individual
  contact_details:
  - contact_type: email
    value: dmk333@psu.edu
  label: David Koslicki
creation_date: '2025-10-31T00:00:00Z'
description: ARAX (Expander Agent) is a graph-based modular reasoning tool for translational
  biomedicine developed as part of the NCATS Biomedical Data Translator program. It
  provides a web browser user interface and TRAPI-compliant API for encoding translational
  biomedical questions and integrating knowledge across multiple sources. ARAX features
  ARAXi, an intuitive domain-specific language for specifying knowledge graph analysis
  workflows. The system accesses around 40 Knowledge Providers covering over 100 underlying
  knowledge sources and provides versatile methods for scoring and ranking result
  subgraphs. ARAX uses RTX-KG2 as its primary knowledge graph and supports query planning,
  knowledge gathering, overlay of contextual information, filtering, and result ranking
  through five core modules (Expander, Overlay, Filter, Resultify, and Ranker).
domains:
- biomedical
- precision medicine
- health
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Expander-Agent
id: arax
infores_id: arax
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
name: ARAX Translator Reasoner
products:
- category: ProgrammingInterface
  description: TRAPI-compliant API endpoint for programmatic access to ARAX reasoning
    capabilities. Supports v1.3+ of the Translator Reasoner API standard. Provides
    /query, /asyncquery, and /entity endpoints.
  id: arax.api
  name: ARAX TRAPI API
  original_source:
  - arax
  product_url: https://arax.ncats.io/api/arax/v1.4/ui/
- category: GraphicalInterface
  description: Web browser interface for querying ARAX and exploring answers. Provides
    interactive visual query graph builder, TRAPI operations input, TRAPI JSON input,
    and ARAXi workflow language input methods.
  format: http
  id: arax.ui
  name: ARAX Web UI
  original_source:
  - arax
  product_url: https://arax.ncats.io/
- category: DocumentationProduct
  description: ARAXi domain-specific language documentation for expressing knowledge
    graph analysis workflows.
  id: arax.araxi.docs
  name: ARAXi Documentation
  original_source:
  - arax
  product_file_size: 12191
  product_url: https://github.com/RTXteam/RTX/blob/master/code/ARAX/Documentation/DSL_Documentation.md
- category: ProgrammingInterface
  description: Source code repository for ARAX and the RTX system including ARAX-specific
    modules and RTX-KG2 knowledge graph.
  id: arax.github
  name: RTX GitHub Repository
  original_source:
  - arax
  product_url: https://github.com/RTXteam/RTX
- category: DocumentationProduct
  description: Example queries and workflows demonstrating ARAX capabilities for various
    translational biomedicine use cases.
  id: arax.examples
  name: ARAX Examples
  original_source:
  - arax
  product_url: https://github.com/RTXteam/RTX/tree/master/code/ARAX/Examples
publications:
- doi: 10.1093/bioinformatics/btad082
  id: btad082
  journal: Bioinformatics
  title: 'ARAX: a graph-based modular reasoning tool for translational biomedicine'
  year: '2023'
synonyms:
- ARAX
- Expander Agent
---
## Description

ARAX is a computational reasoning tool for translational biomedicine that provides an intuitive system for querying and exploring biomedical knowledge and data. As one of six reasoning engines in the NCATS Biomedical Data Translator system, ARAX enables researchers to formulate complex biomedical questions and integrate knowledge across multiple sources to generate ranked answers.

## Key Features

### ARAXi Workflow Language
- Intuitive procedural language for expressing knowledge graph analysis workflows
- Five core modules: Expander, Overlay, Filter, Resultify, and Ranker
- Modular design simplifies construction and reuse of workflows
- Supports incremental query graph construction with add_qnode and add_qedge commands

### Knowledge Federation
- Access to ~40 Knowledge Providers (KPs) covering 100+ underlying knowledge sources
- Dynamically selects TRAPI-compliant KPs from SmartAPI registry
- Supports ~135 node categories and 281 edge predicates
- 76,443 distinct meta-triples (subject-predicate-object combinations)

### ARAX Modules
1. **Expander**: Queries multiple KPs to build answer knowledge graphs
2. **Overlay**: Annotates graphs with contextual quantitative information (Fisher exact test, Jaccard similarity, drug-treats-disease probability, PubMed co-occurrence, clinical data, exposure data)
3. **Filter**: Selectively removes nodes/edges based on thresholds
4. **Resultify**: Finds subgraphs fulfilling query patterns
5. **Ranker**: Scores and ranks results using multi-metric approach

### ARAX Node Synonymizer
- Maps between equivalent concept identifiers from different vocabularies
- Combines evidence from SRI Node Normalizer, RTX-KG2 same_as relations, identical names, and semantic type compatibility
- Facilitates seamless integration of results from multiple KPs

## Use Cases

### Bipolar Disorder Research
Explored connections between D-amino acid oxidase (DAO) and bipolar disorder via protein intermediaries, successfully identifying N-methyl-D-aspartate receptors (NMDARs) in top results.

### COVID-19 Mechanism of Action
Identified remdesivir's mechanism of action through RNA-directed RNA polymerase, revealing "Virus Replication" as a key mediator and potential downstream therapeutic targets like interferon type I.

### Drug Repurposing
Link prediction model for drug-treats-disease relationships, successfully distinguishing between existing treats relationships and non-treats edges in RTX-KG2.

## Technical Details

### Standards Compliance
- TRAPI (Translator Reasoner API) v1.3+ compliant
- Biolink Model for semantic layer
- Uses standardized node categories and edge predicates
- Compatible with translator ecosystem

### Primary Knowledge Graph
- RTX-KG2 as core KP with 73 knowledge sources
- Integrates data from ChEMBL, DrugBank, Reactome, OBO Foundry, KEGG, SemMedDB, UniProtKB, UMLS, and more
- Semantically standardized with Biolink model

### Query Input Methods
1. Interactive visual query graph builder (no coding required)
2. TRAPI operations (guided entry with drop-downs)
3. TRAPI JSON (for workflow sharing)
4. ARAXi workflow language (for complex custom workflows)

## Interfaces

### Web Browser Interface
- Interactive query graph builder
- Visual knowledge graph display
- Ranked results with detailed provenance
- Persistent URLs for result retrieval
- Synonym lookup service
- System activity monitoring

### Programmatic API
- /query endpoint for synchronous queries
- /asyncquery endpoint for long-running queries
- /entity endpoint for node synonymization
- OpenAPI documentation available

## Translator Ecosystem

ARAX is part of the NCATS Biomedical Data Translator, a distributed computational system for accelerating translational science with a layered architecture:
- **Reasoning Engines (ARA)**: ARAX is one of six reasoning engines
- **Knowledge Providers (KP)**: ARAX queries ~40 registered KPs
- **Coordinating Services**: Interpret and route queries
- **Standard Interfaces**: TRAPI for message exchange

## Development and Support

Developed by a collaborative team including:
- Oregon State University
- Institute for Systems Biology
- Pennsylvania State University
- RTX team members

Supported by NCATS through NIH awards OT2TR003428 and OT2TR002520.

## Limitations and Future Work

- System actively developed; no guarantee of indefinite result retention
- For research purposes only; not for clinical treatment decisions
- Future enhancements planned:
  - Improved Node Synonymizer accuracy
  - Enhanced drug-treats-disease prediction via alternative embedding models
  - Query backtracking for better pruning strategies

## Related Resources

- RTX-KG2: Primary knowledge graph used by ARAX
- Biolink Model: Semantic layer specification
- SmartAPI: Registry of TRAPI-compliant services
- Other Translator ARAs: ROBOKOP, BioThings Explorer, mediKanren, ARAGORN

## Citation

Glen, A. K., Ma, C., Deutsch, E. W., Ramsey, S. A., Koslicki, D., et al. (2023). ARAX: a graph-based modular reasoning tool for translational biomedicine. Bioinformatics, 39(3), btad082. DOI: 10.1093/bioinformatics/btad082