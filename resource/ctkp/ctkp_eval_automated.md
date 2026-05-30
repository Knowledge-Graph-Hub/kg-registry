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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Translator wiki, SmartAPI registration, and source repository provide public documentation outside the graph artifact itself.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SmartAPI documents a public TRAPI 1.5 endpoint for the Multiomics Clinical Trials KP.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>The page documents a release artifact, Translator wiki documentation, and SmartAPI registration.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Public source repository exists at multiomicsKP/clinical_trials_kp.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>KGX JSONL release artifact is listed on the resource page.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>The primary graph product explicitly records AACT and ClinicalTrials.gov provenance.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>The page records Translator release version, build identifier, source version, and Biolink version.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Reviewed docs explain that CTKP depends on AACT-mediated ClinicalTrials.gov content.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Wiki documents trial identifiers, interventions, conditions, and adverse events as core graph content.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No explicit deduplication policy was identified.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Wiki names representative predicates and node categories used by the provider.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Biolink predicates and Translator TRAPI exposure are documented.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 6/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>The resource exposes clinically relevant intervention-condition-trial associations.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>NCT identifiers and standard Translator/Biolink categories are documented.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Translator wiki explains the source and the broad association types exposed by the graph.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Docs make clear that AACT is the transformation layer between ClinicalTrials.gov and the KP graph.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Biolink predicates and TRAPI/Biolink compatibility are documented.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Stable Translator release and build identifiers are listed.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Public GitHub repository provides issue tracking and code history.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Resource page now includes a maintainer contact via the public repository identity.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Source repository shows recent updates and the resource page has current release metadata.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Release/build version fields are preserved on the graph product.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Provider is designed for Translator-facing clinical trial evidence and intervention-condition associations.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparative benchmark against other trial KGs was identified.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope is clearly bounded to ClinicalTrials.gov data mediated through AACT.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No explicit evaluation framework was identified in public docs.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No quantitative accuracy metrics were captured during this pass.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>MIT license is recorded on the graph release products.</td></tr>
</tbody></table></div>