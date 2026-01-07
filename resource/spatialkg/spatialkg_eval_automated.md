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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SPARQL endpoint at frink.apps.renci.org/spatialkg/sparql provides access to SAWGraph spatial grid and administrative region data</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>SPARQL endpoint only; no REST API or web portal interface for non-expert geographic queries</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7fa;">N</td><td>Single SPARQL access method; no web UI, downloads, or alternative query mechanisms documented</td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7fa;">N</td><td>No public source code repository found; SAWGraph spatial KG construction methodology not openly available</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7fa;">N</td><td>No bulk RDF export or geographic data dumps available; SPARQL queries required for data access</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>SAWGraph spatial data integrating S2 grid cells and U.S. administrative regions clearly documented</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7fa;">N</td><td>No versioning for S2 geometry or administrative boundary source datasets documented</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>SAWGraph framework integration apparent for spatial data organization and relationships</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Geographic cells and administrative regions with documented spatial relationships from SAWGraph</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7fa;">N</td><td>No deduplication strategy documented for overlapping spatial features or boundary conflicts</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7fa;">N</td><td>RDF schema not formally documented for geographic entities and spatial relationships</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Spatial relationship types (contains, intersects, etc.) not mapped to standard GIS ontologies</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Spatial geographic data applicable to environmental science, agriculture, and water resource management</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#f8d7fa;">N</td><td>S2 grid cell and administrative region IDs not resolvable outside SPARQL endpoint; no external mapping documented</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7fa;">N</td><td>SAWGraph spatial KG construction methodology not publicly documented</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7fa;">N</td><td>How geographic data transformed into spatial knowledge graph structure not transparent</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7fa;">N</td><td>RDF schema and GIS ontology choices not published or documented</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7fa;">N</td><td>No formal versioning scheme; SPARQL endpoint updates continuously without released stable versions</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7fa;">N</td><td>No public issue tracker or development roadmap visible; limited transparency into maintenance</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>David Kedrowski (david.kedrowski@maine.edu) available as primary contact for SAWGraph Spatial KG</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7fa;">N</td><td>Update frequency and schedule for geographic data not documented</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7fa;">N</td><td>No version history or archived spatial data snapshots available for reproducibility</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Use cases in environmental monitoring and agricultural spatial analysis across contiguous U.S.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7fa;">N</td><td>No comparison with other GIS knowledge graphs or spatial databases documented</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused scope on SAWGraph spatial grid covering 48 contiguous U.S. states at Level 13 resolution</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7fa;">N</td><td>No validation against independent geospatial datasets or coordinate accuracy assessments</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7fa;">N</td><td>No reported coordinate accuracy, spatial resolution metrics, or boundary completeness documented</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

