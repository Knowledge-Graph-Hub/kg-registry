---
evaluation_date: '2025-08-13'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Can access subgraphs through query searches</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Neo4j, ExEmPLAR (experimental tool for queries of Neo4j graphs), website with &quot;question builder&quot; feature, automat queries (cypher and TRAPI)</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Can download or query searches in multiple ways</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Https://github.com/RobokopU24/ORION (this is not the original GH from the paper but is now the one they are using)</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Https://stars.renci.org/var/plater/graphs/RobokopKG/6fe13d850fdbf89c/</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Metadata contains all source info</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Metadata includes links and versions for all sources</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Github lists docker requirements and graph spec file with example provided</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Node and edges contain primary knowledge source attribute and, if relationship is inferred, any algorithms/methods used</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Not explicitly mentioned in paper or docs, but github for creating KG/metadata records have an &quot;edge_normalization_version&quot; so it appears they do</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>One-hop connection schema has summary of all edge types (node 1 type, node 2 type, relationship), and individual edges include the original data source, but sources per triple type were not explicitly stated/summarized</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>One-hop connection schema has summary of all edge types, and individual edges include the original data source, but sources per edge type were not explicitly stated</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Json files</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Choose one external representative entity ID and map synonyms using existing equivalencies and specailized rules</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Github repo for construction with reaonsable documentation on how to use it in general, and metadata files include exact versions of functions that were used when creating their KG</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Not explicitly described but metadata contains all preprocessing steps per source with versions of each normalization strategies used</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>BioLink</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Github</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contact form provided on website and weekly office hours over zoom</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Accessible for bulk download. No chnage log, but each comes with metadata that documents all source ingests (including versions) and preprocessing steps used for each source</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>4 ranging from simple linear queries to discovering mechanistic links</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Defined scope</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Informative subgrahs are ranked according to number of supporting publications and literarure co-occurence of entity pairs</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>Open-Source MIT License</td></tr>
</tbody></table></div>

