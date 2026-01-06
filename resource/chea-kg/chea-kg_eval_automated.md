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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>ChEA-KG Explorer web interface at maayanlab.cloud/chea-kg/ enables interactive exploration of TF-gene regulatory relationships with visualization</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>RESTful API available at maayanlab.cloud/chea-kg/api/ for programmatic access to transcription factor binding data</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Provides web portal, REST API, and Neo4j database access; accommodates both exploratory and computational workflows</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Complete source code available at github.com/MaayanLab/chea-kg under Ma'ayan Lab organization for transparency and reproducibility</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Neo4j database and processed ChIP-seq datasets available for download enabling local deployment and analysis</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#f8d7da;">N</td><td>ChEA-KG builds on ChEA3 ChIP-seq database but upstream sources and versions not explicitly listed in documentation</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No version tracking for underlying ChIP-seq datasets or source database snapshots documented</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#f8d7da;">N</td><td>Data import pipeline and ontology dependencies not formally documented in available resources</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#f8d7da;">N</td><td>While ChEA3 paper cited, specific source attribution for individual TF-gene relationships not provided</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No documentation of deduplication strategies for redundant TF-target associations across ChIP-seq studies</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>RDF/semantic specifications for edge relationships not documented; Neo4j schema not formally published</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Relationship types (e.g., 'targets', 'binds_to') not formally specified with ontology mappings</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 0/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>ChIP-seq derived TF-gene relationships provide actionable insights for gene regulation and transcriptional control research</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses standard HGNC gene symbols and documented TF identifiers resolvable through external databases</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>ETL process and quality control steps not documented; only high-level description of ChEA3 integration available</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>No documentation of ChIP-seq data preprocessing, filtering thresholds, or binding site calling parameters used</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>Neo4j property graph schema not formally documented; no RDF/OWL schema available for semantic integration</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>GitHub releases available at github.com/MaayanLab/chea-kg providing tagged stable versions for reproducibility</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues tracker active; Ma'ayan Lab maintains responsive maintenance of systems biology tools</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contact available through Ma'ayan Lab (avi.maayan@mssm.edu) and GitHub organization; active development team</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Part of continuously maintained Ma'ayan Lab ecosystem; repository shows recent commits and updates</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Full Git history available; prior versions accessible through GitHub releases and commits for reproducibility</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Clear use case: identify transcription factor targets for functional enrichment and regulatory network analysis</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparison with other TF-target databases (ENCODE, ReMap, or similar); no benchmarking studies published</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Well-defined scope: ChIP-seq derived transcription factor binding to gene regulatory elements</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No validation against independent experimental data (e.g., CRISPR screening, reporter assays)</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No sensitivity, specificity, or positive predictive value reported; no quantitative validation metrics available</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

