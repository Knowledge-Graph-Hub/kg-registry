---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes – The KG enables extraction of disease mappings, disease profiles, and pathogenesis paths, as shown in the case studies (e.g., 3-hop paths from Wilson disease)</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">Yes – Public Neo4j instance available: <a href="https://disease.ncats.io">https://disease.ncats.io</a></td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>sourcecode_available_text</td><td>Partially – The in-house framework stitcher is mentioned and linked (<a href="https://github.com/ncats/stitcher),">https://github.com/ncats/stitcher),</a> but full KG generation scripts for GARD KG are not public</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Y (networkx pickle)</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/10</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Y, integrates 34 distinct biomedical resources</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td>ORPHADATA v4.0  Gene Ontology  Human Phenotype Ontology  GO annotations Pathway Commons (PTC) Pharos v3.8.0</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td>Partially – Tools like stitcher and OWL file parsing are mentioned, but not declared formally like a software repo would</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes – each node/edge carries provenance via stitch keys (e.g., N_Name, I_CODE)</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td>Partially – Mappings and harmonization discussed, but no explicit deduplication process for edges described</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes – Object properties defined per source and integration method (e.g., has_phenotype, I_CODE, N_Name)</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes – Meta-ontology schema is described with object properties and their meanings (Table 3)</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 11/14</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes – Disease profiles, drug-disease associations, and harmonization rules demonstrate biomedical applicability</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td>The paper explicitly mentions using &quot;Unique Ingredient Identifier (UNII),&quot; &quot;MONDO ID,&quot; and &quot;OMIM ID&quot; for mappings, indicating that external identifiers are a core part of their entity resolution strategy</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes – Detailed methods section describes data collection, mapping strategies, and harmonization</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td>The paper notes that &quot;data cleanup was performed,&quot; mentioning specific examples like restricting prefixes for OMIM IDs and Orphanet IDs. It also discusses the challenges of programmatic annotation, such as preventing the annotation of generic terms like &quot;Disease&quot; or &quot;Syndrome&quot;</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td>The paper outlines a &quot;meta-ontology&quot; that serves as the schema for the knowledge graph. This includes a clear definition of primary classes and object properties used to structure the data; documented in tables 2–4</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/10</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>public_tracker</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes – Corresponding author: qian.zhu@nih.gov and NCATS/ NIH team affiliation listed</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#d4edda;">Yes - Suggests updates over time; indicates continually updated</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/10</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes – Four detailed case studies: disease mapping, disease profiling, data harmonization, pathogenesis exploration</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td>The paper compares its approach with other similar efforts, such as the semantic Diseasecard and the Monarch Initiative, placing its own work in the context of the broader field; but no explicit benchmarking</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes – Focused on rare diseases, especially those curated in GARD, and integrating relevant biomedical data</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td>Partially – Demonstrates utility via case studies but lacks formal quantitative evaluation (mapping stats in tables 6,7,10)</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td>The paper&#x27;s semi-automatic mapping process for FDA orphan designations includes a manual curation step where curators labeled mappings as &quot;Done,&quot; &quot;Approximate,&quot; or &quot;Failed,&quot; providing a clear way to measure the confidence or accuracy of the mappings</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/10</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY 4.0</td></tr>
</tbody></table></div>

