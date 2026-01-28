---
evaluation_date: '2026-01-28'
evaluator: Automated evaluation (GPT-5.2-Codex)
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>No embeddings or external artifacts beyond KG data and metadata are described on the site or repo.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Web server provides interactive Search and Query interfaces for browsing and subgraph exploration.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Web UI plus downloadable raw KG files and entity metadata from the Download Center.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Open source code available in the UniBioMap GitHub repository.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Downloadable CSV/TSV graph files (e.g., unibiomap.links.csv, unibiomap.auxs.tsv, predictions) and JSON entity metadata.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#f8d7da;">N</td><td>Site notes integration from many resources but does not enumerate a source list on the main pages.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No upstream source versions or dates listed on the site or repo.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Repository documents required setup and prerequisites (e.g., DrugBank credentials and manual preparation steps).</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#f8d7da;">N</td><td>No per-node/per-edge source mapping described in the web docs.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No deduplication strategy documented.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>No triple-level provenance described.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>No explicit edge-type schema published on the site or repo.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Biomedical KG focused on proteins, compounds, diseases, pathways, GO, and phenotypes.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Identifiers normalized to standard resources (e.g., UniProt accessions, chemical structure identifiers).</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>About page and README describe a modular ingestion/normalization pipeline and build steps.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>No detailed transformation rules or ETL mapping documents are provided.</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>No formal schema specification is described.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>No releases or versioned data snapshots advertised.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues are enabled for the UniBioMap repository.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#f8d7da;">N</td><td>No direct contact email listed on the UniBioMap site or in the repository README.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>No stated update cadence.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No archive of prior versions available.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Site describes interactive search and multi-entity query for subgraph exploration.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>About page highlights comparisons with existing biomedical KGs (figure caption on statistics/comparisons).</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Explicit scope around protein- and compound-centered biomedical knowledge with six entity types.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No multiple evaluation methodologies described.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No accuracy/quality metrics reported on the site or in the repository.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td style="background-color:#d4edda;">Y</td><td>Download page states KG data files are provided under CC BY-NC 4.0; code is MIT licensed on GitHub.</td></tr>
</tbody></table></div>
