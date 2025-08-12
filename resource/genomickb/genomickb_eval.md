---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Y, can submit an online query and download subgraphs that meet criteria</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td>website with UI for creating queries, API supposely coming in v2, Neo4j dump available but not hosted by creators</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Y, can use online query tool or download Neo4j dump</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Y, <a href="https://github.com/tinalee-tech/KG-dataloader">https://github.com/tinalee-tech/KG-dataloader</a></td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Y, Neo4j dump</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 9/10</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Y, supplementary note 1</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Y, tables 1 (nodes)  &amp; 2 (edges), query allows users to restrict by datasource</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td>Considered but not de-duplicated. Users can restric querys to specific datasources and duplicate edges can be used for validation. EX:  ‘enhancer regulate gene’ with restriction ‘cell_line=GM12878’ and ‘data_source=EnhancerAtlas’ -&gt; 118,610 node pairs. A second query for ‘variant overlap enhancer’, ‘enhancer regulate gene’, and ‘variant correlate_with gene’ -&gt;  16,871  enhancer-gene pairs from EnhancerAtlas can be validated by GTEx eQTLs</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Y, table 2</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Y, table 2</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 9/14</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Y, they have a web interface (<a href="https://gkb.dcmb.med.umich.edu/)">https://gkb.dcmb.med.umich.edu/)</a> presenting the entities and edges in a human-readable format. It can be used to answer genomics-related questions and conduct biological analysis</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Y, uses one external ID when possible and defines globaly unique IDs for entities without such as ChIP-seq peaks</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Y, github and supplement</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Y, sup Note 1 Data Collection and Processing</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td>Uses custom schema not an existing one but does provide documentation</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 9/10</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#d4edda;">Y but still on version 1.0 despite multiple upates listed</td></tr>
<tr><td>stable_versions</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#f8d7da;">N, FAQ says to email the team</td></tr>
<tr><td>public_tracker</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Y, website has a contacts button with name/emal for both technical details and accessing the data/web server</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td>During 2022-2023 yes but not since then</td></tr>
<tr><td>updated_annually</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>prior_versions_access_text</td><td>Clearly documented chages with dates but prior versions not available. *Paper states that they store all versions internally and can revert if unexpected changes are ever made to their graph but these are not accessible publicaly</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 6/10</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td>The paper provides examples of specific queries that can be performed through the website that would normally require coding and integrating multiple data sources, but it is limited to knowledge extraction and does not show how this could be used to make novel biological discoveries</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Y, coding free queries of human genomic information including both functional, strutural, epigenetic and other relationships</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>accuracy_metrics_text</td><td>Kind of but not explicitly. Since this tool is all about data querying, confidence could be assesed by creating multiple queries like the example of using eQTLs to &quot;validate&quot; EnhancerAtlas relationships</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/10</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY-NC 4.0</td></tr>
</tbody></table></div>

