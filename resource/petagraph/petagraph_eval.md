---
layout: eval_detail
---

# Evaluation for petagraph

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">yes, portions of the graph that are open licensed are available from https://osf.io/6jtc9/files/osfstorage</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">yes, (ish), neo4j dump can be downloaded if you have a UMLS license key, and there are instructions to build a neo4j from sources in the github repository. Ish, because it's not specifically hosted, you need to host it yourself.</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#f8d7da;">no, (ish) completed graph can only be downloaded as neo4j, components to build the graph can also be downloaded, but that doesn't quite feel like it makes a yes</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">yes, ETL of upstream sources lives in https://github.com/x-atlas-consortia/ubkg-etl/</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">yes (with UMLS api key)</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">yes, methods section of paper https://www.nature.com/articles/s41597-024-04070-w#Sec2</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">yes, ish, some source versions listed in https://github.com/TaylorResearchLab/Petagraph/tree/main/Scientific_Data_2024</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">yes, ubkg etl has requirements.txt, petagraph has requirements-test.txt</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes. They either come from existing ontologies or have one file per datasource with edges and nodes that are being added.</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes - Yes. Bidirectional edges are only for Concept–Concept; other edges are unidirectional. Redundancies are minimized using binning and source normalization</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes, methods of paper</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">yes custom schema defined in paper</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes, csv files</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes, concept CUI with codes corresponding to common external ID/s</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes, well documented github</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td>guidlines for formatting ontologies in user guide, method explain preprocessing steps</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td>Start with ontologies and standards in the UBKG and add in omics data based on their paper defined in the schema</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">No, lists date last updated but no version</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>public_tracker</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes, contributors listed https://osf.io/6jtc9/</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#d4edda;">Yes, frequent small updates</td></tr>
<tr><td>updated_annually</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>prior_versions_access_text</td><td>recent acitivty documents date of all changes and person who made them but prior versions not accessible https://osf.io/6jtc9/</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes, several in paper</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes integrating/analyzing multiomics datasets</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td>link prediction tasks auROC, precision-recall, top tissues associated w a disease, and shortest path analysis of subgraphs</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Yes. AUC-ROC, Precision-Recall curves, common neighbors vs random, structural metrics compared to randomized graphs</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY-NC-ND 4.0</td></tr>
</tbody></table></div>

