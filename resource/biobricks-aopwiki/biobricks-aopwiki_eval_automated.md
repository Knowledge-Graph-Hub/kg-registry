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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SPARQL endpoint at frink.apps.renci.org/biobricks-aopwiki/sparql enables querying AOP pathway data</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>SPARQL endpoint available but no REST API or user-friendly web interface for non-expert queries</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td>Single access mechanism (SPARQL); no web portal, downloadable RDF, or alternative query methods</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Complete source code and RDF generation pipeline at github.com/biobricks-ai/aopwikirdf-kg</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>No bulk RDF/Turtle download; SPARQL queries required to retrieve data</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Source clearly identified as AOP-Wiki, NIVA's adverse outcome pathway database</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No documented AOP-Wiki version used; unclear how frequently data is synchronized</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>RDF generation scripts available in GitHub showing integration process and dependencies</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>AOP pathway data transformed to RDF with clear relationships between molecular initiating events and adverse outcomes</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No documentation of deduplication strategy for duplicate AOP pathways or overlapping relationships</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>RDF schema documentation not provided; ontology mappings unclear</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Relationship types not formally mapped to standard ontologies (RDF, OWL)</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>AOP pathway data directly applicable to toxicology and adverse effect prediction</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Nodes use stable AOP-Wiki identifiers resolvable through NIVA's AOP-Wiki website</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>RDF generation methodology not formally documented beyond source code</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>No documentation of how AOP-Wiki hierarchical data maps to RDF structure</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>RDF vocabulary and ontology choices not formally published or documented</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>GitHub releases available for BioBricks AOP-Wiki with tagged stable versions</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues tracker active; BioBricks team maintains the project</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Maintainer Tom Luechtefeld available; BioBricks organization provides support</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Part of active BioBricks ecosystem; repository shows regular commits</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Full GitHub history available; prior versions accessible for reproducibility</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Clear use case: support toxicological risk assessment through structured AOP pathway data</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparison with other AOP databases or structured toxicology knowledge graphs</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused scope: adverse outcome pathways linking molecular events to population-level effects</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No systematic validation or accuracy assessment framework documented</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No reported accuracy, precision, or coverage metrics for AOP data completeness</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

