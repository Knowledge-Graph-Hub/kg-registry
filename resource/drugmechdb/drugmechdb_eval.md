---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Y, paths that describe the mechanism of action for drug/disease indication pair</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td>website, can view all paths or only those related to a specific drug or disease</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Y Can download from zenodo or use website</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Y: <a href="https://github.com/SuLab/DrugMechDB">https://github.com/SuLab/DrugMechDB</a></td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td>Kind of on zenodo, but what they are calling a KG is a collection of entries for drug/disease pairs and the paths connecting them. Raw KG containing all edges between all entries does not appear to exist</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 8/10</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td>table with node sources. Indications: DrugCentral ( according to GH, randomly sampled from availble drug-disease pairs, does not include all of them), paths: Mechanism of Action section from DrugBank, description section within Inxight Drugs, review articles, GeneOntology , UniProt, Reactome, and well-sources Wikipedia articles. No Primary experimental results are included. All are verified by curators</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td>Date given for DrugCentral download, cannot find info for other sources</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Y, there are requirements.txt and .yaml files in the KG&#x27;s downloadable .zip file on Zenodo (<a href="https://zenodo.org/records/8139357)">https://zenodo.org/records/8139357)</a> showing the dependencies.</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td>each entry consist of ‘graph’, ‘links’, ‘nodes’, and ‘reference’ keys. Graph contains the drug/disease pair, links contains relationships informative to the indication, nodes contains information about all entities in link, and reference contains all the sources for the entire relationship but not specifically for individual nodes/edges</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td>paths are manually curated</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>triples_source_details_text</td><td>edges between informative nodes in a path do not contain orignal source infromation. Informative paths have citations for the entire path, not indivudal triples within them.</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>edge_type_schema_text</td><td>BioLink, but does not specify exactly what sources are used for each edge type</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/14</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">yes, json files</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">yes, all nodes come from existing sources</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#f8d7da;">Not really. Everything is &quot;manually curated&quot;</td></tr>
<tr><td>construction_docs</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>transform_docs</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>schema_used_text</td><td>BioLink</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/10</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>stable_versions</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>public_tracker_text</td><td>GitHub Issues. Also includes a guide for how users can submit their own curated paths.</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td>indirectly. website indicated the lab who owns it, but does not provide a point of contact</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">N (V1 released in 2019 with one update less than a year later, same with V2 in 2023, no other updates)</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td>All versions availble, V2 has publication associated but detailed change logs for minor updates not available</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/10</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>eval_against_others_text</td><td>They used an external KG to evaluate agreement between types of associations present in both graphs and calculate a p-value representing when the simulated percentage of matching was greater than or equal to the observed percentage</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes, mechanisms of action by which a drug treats a disease</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>accuracy_metrics_text</td><td>agreement with MechRepoNet</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/10</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC0 1.0 Universal</td></tr>
</tbody></table></div>

