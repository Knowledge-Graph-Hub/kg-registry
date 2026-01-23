---
evaluation_date: '2026-01-23'
evaluator: Automated evaluation (GPT-5.1-Codex-Max)
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>No published embeddings or derived artifacts beyond the mapping triples.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SPARQL endpoint at https://frink.apps.renci.org/identifier-mappings/sparql.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Both SPARQL and a Triple Pattern Fragments endpoint (https://frink.apps.renci.org/ldf/identifier-mappings).</td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7da;">N</td><td>No code repository linked for the extraction/hosting pipeline.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>No dump or download link provided.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>States the graph is a subset of the Wikidata RDF dump focused on identifier mappings.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No dump date or version of Wikidata specified.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Depends on Wikidata RDF dumps for mapping predicates.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Nodes and edges originate from Wikidata mapping triples.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No mention of deduplication.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Does not enumerate triple-level provenance.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Uses standard predicates (e.g., skos:exactMatch) but no explicit edge type schema is described.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Identifier mappings are broadly usable, including for biomedical integration.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>External identifiers are represented as RDF IRIs and are resolvable.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>No build or ingestion pipeline documentation provided.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Notes conversion of Wikidata custom predicates to standard ones like skos:exactMatch.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>States use of standard RDF predicates (e.g., SKOS exactMatch) for mappings.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>No release cadence or version tags are listed.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>No issue tracker linked for this graph.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contact provided: Mahir Morshed (morshedm@renci.org).</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>No stated update schedule.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No access to historical versions.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Intended for cross-referencing Wikidata entities to external identifier systems.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparative evaluation reported.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope limited to identifier-mapping triples extracted from Wikidata.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No evaluation methodology described.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No accuracy or quality metrics provided.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td style="background-color:#d4edda;">CC0 1.0</td><td>Inherits Wikidata's CC0 license; FRINK provides the subset.</td></tr>
</tbody></table></div>

