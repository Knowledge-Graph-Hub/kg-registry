---
evaluation_date: '2026-01-06'
evaluator: Automated Evaluation
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Wikidata web portal at wikidata.org provides browsing and editing interface for 119+ million data items</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SPARQL query service at query.wikidata.org supports complex semantic queries; RESTful action API available</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Five documented access methods: web portal, SPARQL endpoint, query editor, bulk dumps, and REST API</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Mediawiki-based platform; source code publicly available through Wikimedia organization repositories</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Complete database dumps in JSON, RDF/XML, TTL formats available as compressed archives at dumps.wikimedia.org</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Data sourced from Wikipedia articles, Wikimedia projects, and external linked open data sources</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No explicit versioning of upstream Wikipedia or external data sources; continuous updates without version tracking</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Explicit relationships documented for Wikipedia article mappings and interlinking with VIAF, GND, and other identifiers</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each item traceable to Wikimedia source; edit history provides attribution of knowledge statements</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>While community identifies duplicates, no formal deduplication algorithm documented; merging handled ad-hoc</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>RDF export schema partially documented but source attribution for individual statements not explicit</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Extensive property vocabulary used but mapping to standard ontologies (RDF, OWL) not fully formalized</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Wikidata includes extensive biomedical data: genes, proteins, diseases, drugs, and biological pathways</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Wikidata IDs (Q-identifiers) are stable and resolvable; cross-references to standard identifiers (Uniprot, NCBI Gene, etc.)</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>While edit history is transparent, formal KG construction methodology not documented; wiki-based approach</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>RDF/TTL dump generation process not formally documented; no data quality control procedures published</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>Uses Wikidata property model; mapping to RDF schema and standard ontologies incomplete</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Database dumps published regularly with dates; snapshot releases available for reproducibility</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>Phabricator system used for tracking but not specifically scoped to Wikidata KG development</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Wikimedia Foundation provides support; contact available through wikidata.org/wiki/Wikidata:Contact</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Continuously updated knowledge base; new dumps published regularly (weekly/monthly snapshot releases)</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Historical dumps available through archive; complete edit history accessible for any item or statement</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Clear use cases: central structured data repository for Wikipedia, machine-readable linked data access, integration hub</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No formal comparison with other general-purpose knowledge graphs (DBpedia, YAGO); relative completeness not quantified</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope well-defined: comprehensive general knowledge base with 119+ million items covering all domains</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No systematic evaluation framework published; quality assessment relies on community and edit history</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No reported accuracy metrics, precision/recall, or data quality benchmarks; community-driven validation</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

