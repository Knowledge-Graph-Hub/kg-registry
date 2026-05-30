---
evaluation_date: '2026-05-30'
evaluator: Automated Evaluation
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Translator wiki, public repository, and release artifact page document the provider outside the graph itself.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Public TRAPI endpoint is listed on the resource page.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Resource page documents a TRAPI endpoint, release artifact download, repository, and Translator wiki documentation.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Source repository is public at broadinstitute/genetics-kp-dev.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>KGX JSONL release artifact is listed as a graph product.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>The page now lists Genebass, GenCC, ClinVar, and ClinGen as upstream sources for the primary graph product.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>The graph product records Translator release version, source version, and Biolink version.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Public docs describe MAGMA, Richards, ABC, and integrated-genetics methods layered over curated upstream sources.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Repository and wiki document both curated data resources and method-generated association layers.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No explicit deduplication policy was identified in reviewed docs.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Reviewed docs specify available method families and phenotype coverage for several association sets.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>TRAPI/Biolink compatibility is recorded for the graph release.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 6/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>The resource is explicitly intended for genetic association and disease-biology analysis.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Phenotype lists in the public repository include EFO and MONDO identifiers, and the release is Translator/TRAPI-oriented.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Translator wiki and public repository document source inputs and major method families.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Public docs describe MAGMA, Richards, ABC, and integrated genetics transformations over upstream datasets.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Biolink compatibility is recorded for the graph artifact and TRAPI endpoint.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>The page records a stable Translator release and build identifier.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Public GitHub repository exposes issues and development history.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Marc Duby and other team members are recorded on the resource page.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Current resource metadata and release history indicate active maintenance within the last year.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Versioned release and build identifiers are exposed on the graph product.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Use case is Translator-facing gene-disease analysis from integrated genetic evidence.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparative benchmark against other genetic KGs was identified during this pass.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope is focused genetic association evidence, especially GWAS-derived signals and curated clinical genetics resources.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>Multiple association-generation methods are documented, but not framed as a published evaluation suite.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No explicit quantitative accuracy metric was captured in the reviewed docs.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>MIT license is recorded on the graph release products.</td></tr>
</tbody></table></div>