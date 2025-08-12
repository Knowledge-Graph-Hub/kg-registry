---
layout: eval_detail
---

# Evaluation for rtx-kg2

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes, RTX-KG2 is able to provide various biomedical information through queries. It is also used as backend to support ARAX's path reasoning and path ranking (https://github.com/RTXteam/RTX) .</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">Yes, can access by API query, and Neo4j.</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Yes, multiple ways to access including downloadable versions, API (SmartAPI), web browser user interface (seems not currently working).</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Yes, Github (https://github.com/RTXteam/RTX-KG2)</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Yes, downloadable versions are available on Github</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Yes, 70 sources Table 1 (UMLS, SemMedDB, ChEMBL, DrugBank, Reactome, SMPDB, and 64 additional knowledge sources).</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">Yes, it documents the versions of the upstream sources used (https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Yes, in the requirements file.</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes, node's ID contains source information and edge contains primary knowledge source.</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes, it provides a pre-canonicalized graph version (RTX-KG2pre, with semantically duplicated concepts) and a canonicalized version (RTX-KG2c, withthout semantically duplicated concepts)</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes, in the final output KG, each edge includes the source that reated that triple.</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes, it uses Biolink Model for as the schema standard for both nodes and edges.</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes, it is used for other biological applications such as answering translational science questions, drug repositioning, identifying new therapeutic targets, and understanding drug mechanisms.</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes, it uses resolvable IDs for the entities.</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes, it has clear and step by step documentation on construction on its Github repo</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Yes, in Appendix</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#d4edda;">Yes, Biolink model and extract-transform-load (ETL) approach for construction.</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#d4edda;">Yes, it is using semantic versioning (e.g., KG2.7.3)</td></tr>
<tr><td>stable_versions</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#d4edda;">Yes, provides public tracker for requests, bug reports on it Github repo.</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes, it provides contact information of the KG2 Team.</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#d4edda;">Yes, once per month (mentioned in Discussion).</td></tr>
<tr><td>updated_annually</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#d4edda;">Yes, the prior versions are accessible (https://github.com/ncats/translator-lfs-artifacts/blob/main/README.md) with documented changes (https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes, it is currently being used by multiple Translator reasoning agents such as ARAX (Autonomous Relay Agent X).</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#d4edda;">Yes, it is compared to four other KGs (Hetionet, SPOKE, the SRI Reference Knowledge Graph, and ROBOKOP)</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes, it is a part of NCATS Biomedical Data Translator project to support automated biomedical reasoning and question answering. It aims to create a semantically standardized, computable, and interoperable biomedical KG that supports translational reasoning and biomedical discovery.</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Yes, it is not only evaluated with other KGs, but also evaluated on the tools that utilize it such as ARAX, mediKanren, BioThings Explorer, and  ARAGORN.</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Yes, the nodes and edges contain evidence, provenance, and other information for measuring accuracy and confidence.</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY 4.0</td></tr>
</tbody></table></div>

