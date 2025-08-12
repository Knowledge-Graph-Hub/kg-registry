---
layout: eval_detail
---

# Evaluation for robokop

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Y, can access subgraphs through query searches</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">Y: neo4j, ExEmPLAR (experimental tool for queries of Neo4j graphs), website with "question builder" feature, automat queries (cypher and TRAPI)</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Y, can download or query searches in multiple ways</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Y, https://github.com/RobokopU24/ORION (this is not the original GH from the paper but is now the one they are using)</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Y, https://stars.renci.org/var/plater/graphs/RobokopKG/6fe13d850fdbf89c/</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Y, metadata contains all source info</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">Y metadata includes links and versions for all sources</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Y, github lists docker requirements and graph spec file with example provided</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Y, node and edges contain primary knowledge source attribute and, if relationship is inferred, any algorithms/methods used</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#f8d7da;">not explicitly mentioned in paper or docs, but github for creating KG/metadata records have an "edge_normalization_version" so it appears they do</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td>one-hop connection schema has summary of all edge types (node 1 type, node 2 type, relationship), and individual edges include the original data source, but sources per triple type were not explicitly stated/summarized</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>edge_type_schema_text</td><td>one-hop connection schema has summary of all edge types, and individual edges include the original data source, but sources per edge type were not explicitly stated</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes, json files</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Y, choose one external representative entity ID and map synonyms using existing equivalencies and specailized rules</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Y, github repo for construction with reaonsable documentation on how to use it in general, and metadata files include exact versions of functions that were used when creating their KG</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#f8d7da;">not explicitly described but metadata contains all preprocessing steps per source with versions of each normalization strategies used</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td>BioLink</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#d4edda;">Y, github</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td>Contact form provided on website and weekly office hours over zoom</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td>accessible for bulk download. No chnage log, but each comes with metadata that documents all source ingests (including versions) and preprocessing steps used for each source</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Y, 4 ranging from simple linear queries to discovering mechanistic links</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Y, informative subgrahs are ranked according to number of supporting publications and literarure co-occurence of entity pairs</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>Open-Source MIT License</td></tr>
</tbody></table></div>

