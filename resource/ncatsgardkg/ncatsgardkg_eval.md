---
evaluation_date: '2025-08-13'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>The KG enables extraction of disease mappings, disease profiles, and pathogenesis paths, as shown in the case studies (e.g., 3-hop paths from Wilson disease)</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Public Neo4j instance available: <a href="https://disease.ncats.io">https://disease.ncats.io</a></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Partially – The in-house framework stitcher is mentioned and linked (<a href="https://github.com/ncats/stitcher),">https://github.com/ncats/stitcher),</a> but full KG generation scripts for GARD KG are not public</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Networkx pickle</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Integrates 34 distinct biomedical resources</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>ORPHADATA v4.0  Gene Ontology  Human Phenotype Ontology  GO annotations Pathway Commons (PTC) Pharos v3.8.0</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Partially – Tools like stitcher and OWL file parsing are mentioned, but not declared formally like a software repo would</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each node/edge carries provenance via stitch keys (e.g., N_Name, I_CODE)</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Partially – Mappings and harmonization discussed, but no explicit deduplication process for edges described</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Object properties defined per source and integration method (e.g., has_phenotype, I_CODE, N_Name)</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Meta-ontology schema is described with object properties and their meanings (Table 3)</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Disease profiles, drug-disease associations, and harmonization rules demonstrate biomedical applicability</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>The paper explicitly mentions using &quot;Unique Ingredient Identifier (UNII),&quot; &quot;MONDO ID,&quot; and &quot;OMIM ID&quot; for mappings, indicating that external identifiers are a core part of their entity resolution strategy</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Detailed methods section describes data collection, mapping strategies, and harmonization</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>The paper notes that &quot;data cleanup was performed,&quot; mentioning specific examples like restricting prefixes for OMIM IDs and Orphanet IDs. It also discusses the challenges of programmatic annotation, such as preventing the annotation of generic terms like &quot;Disease&quot; or &quot;Syndrome&quot;</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>The paper outlines a &quot;meta-ontology&quot; that serves as the schema for the knowledge graph. This includes a clear definition of primary classes and object properties used to structure the data; documented in tables 2–4</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Corresponding author: qian.zhu@nih.gov and NCATS/ NIH team affiliation listed</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>Suggests updates over time; indicates continually updated</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Four detailed case studies: disease mapping, disease profiling, data harmonization, pathogenesis exploration</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>The paper compares its approach with other similar efforts, such as the semantic Diseasecard and the Monarch Initiative, placing its own work in the context of the broader field; but no explicit benchmarking</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused on rare diseases, especially those curated in GARD, and integrating relevant biomedical data</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Partially – Demonstrates utility via case studies but lacks formal quantitative evaluation (mapping stats in tables 6,7,10)</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>The paper&#x27;s semi-automatic mapping process for FDA orphan designations includes a manual curation step where curators labeled mappings as &quot;Done,&quot; &quot;Approximate,&quot; or &quot;Failed,&quot; providing a clear way to measure the confidence or accuracy of the mappings</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

