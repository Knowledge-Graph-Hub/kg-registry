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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Broad Institute web interface and KGX files available at molepro.s3.amazonaws.com</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>Part of Translator network but direct KG API not documented for public use</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>KGX nodes/edges TSV downloads and source code access available</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Complete source at github.com/broadinstitute/molecular-data-provider</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>KGX files available but no comprehensive RDF/graph database dumps</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Integrates data from multiple molecular databases and biomedical sources</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No version tracking for upstream molecular data sources</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Source code shows integration pipeline and data dependencies</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Molecular entities and relationships sourced from documented databases</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7fa;">N</td><td>No documentation of deduplication strategy</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Schema not formally documented</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Relationship types not formally mapped to ontologies</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Molecular data translates from chemical scale to systems biology applications</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses standard chemical and gene identifiers resolvable through external databases</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>ETL methodology not formally documented beyond source code</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>Data integration steps not transparent in published documentation</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>Schema documentation not published; KGX format used but ontology mapping unclear</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>GitHub releases available with tagged versions</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues tracker active; Broad Institute maintains project</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Sandrine Muller (ORCID 0000-0001-5998-3003) available for contact</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Part of Translator network with continuous updates</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Full GitHub history and releases available</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Translator use case: molecular to systems-level knowledge integration</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No benchmarking against other molecular data providers documented</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused on molecular-scale biomedical data translation</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No systematic validation framework published</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No accuracy, precision, or recall metrics reported</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

