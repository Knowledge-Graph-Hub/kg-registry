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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Per-source node and edge CSVs downloadable from the ProKN downloads page.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>REST API documented at https://research.bioinformatics.udel.edu/ProKN/restapi.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Interactive explorer UI, REST API, and CSV downloads.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Website code on GitHub (ProKN-Website repository linked from the footer - inaccessible at eval time).</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>CSV node/edge files for each source are available for download.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Sources enumerated in the downloads tables (e.g., GlyGen, LINCS, PIR, GTEx).</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No upstream source versions or dump dates stated beyond a single "Last Updated" column.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Dependencies implied by the listed source datasets feeding ProKN.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each node/edge file name encodes its originating source.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No mention of edge deduplication steps.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>No triple-level provenance beyond source-level grouping.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>No formal edge-type schema documented.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Integrates protein-centric biomedical data and associations.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses standard identifiers (e.g., UniProt, GO, ClinVar, GTEx).</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>No build or ETL documentation provided.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>Transform steps from sources to ProKN not described.</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>No explicit schema statement.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>No release tags or versioned downloads.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues link on the ProKN website footer (repo inaccessible at eval time).</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contact email (chenc@udel.edu) provided.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>No stated update cadence.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No archive of prior versions or dumps.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Describes protein-centric integration for functional genomics and CFDE reuse.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparative evaluation reported.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope limited to protein-related knowledge spanning listed sources.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No evaluation methodology described.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No accuracy or quality metrics provided.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td style="background-color:#f8d7da;">N</td><td>No license specified on the site.</td></tr>
</tbody></table></div>
