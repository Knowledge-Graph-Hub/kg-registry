---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes, can access the mapping schema biolink model which provides sematics mappings and ontological relationships, can access downloadable graph dumps in SciGraph or KGX formats.</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">Yes, can access by Monarch&#x27;s own webpage, API, Neo4j, downloadable Graph.</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Yes, Monarch provides multiple ways to download the data such as KGX TSV, KGX JSON lines, Neo4j Dump, etc.</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Yes, can access the source code for making the KG on Github.</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Yes, KGX TSV, KGX JSON lines, Neo4j Dump, etc.</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Yes, 33 heterogeneous data sources including HPOA, CTD, OMIM, Orphanet, WormBase, FlyBase, MGI, dictyBase, Xenbase, SGD, RGD, PomBase, ZFIN, NCBI, HGNC, Panther, BGeeDB, Reactome, STRING.</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">Yes, provides the version info of the sources used: <a href="https://data.monarchinitiative.org/monarch-kg-dev/latest/index.html">https://data.monarchinitiative.org/monarch-kg-dev/latest/index.html</a></td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Yes, declared dependencies through its build infrastructure in the monarch-ingest and kg-hub Github repo. Specifically, Monarch uses Poetry for the dependencies management.</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes, nodes and edges contain the most upstream source and knowledge provider information.</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes, duplicate edge and node management is taken into consideration in the construction of the KG.</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes, the triples created are captured in multiple stages of the KG ingest pipeline including the biolink preddicate mappings and the output.</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes, Biolink model. All relationships are mapped to Biolink predicates.</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 14/14</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes, Monarch KG is both human-readable and usable. Monarch provides its data in tablular formats that are easy to understand. Also, Monarch KG data and its Monarch initaitive webpage can be used in bioinformatics &amp; biomedical analysis, machine learning, NLP, LLMs, visualization &amp; exploration, etc.</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes, supports resolvable and externally linked identifiders. Monarch KG uses curie-style IDs that follow identifier conventions and are mappable to URLs for resolution. Also, it includes a column called xref which contains a list of external identifiers.</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes, Monarch made great effort to document its KG construction including data ingestion, transformation, schema usage, and KG merging.</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Yes, Monarch documented data transforms including the excluded nodes and dangling edges.</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#d4edda;">Yes, Monarch uses a documented schema, Biolink Model, and its monarch-ingest pipeline for construction.</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#d4edda;">Yes</td></tr>
<tr><td>stable_versions</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#d4edda;">Yes, Monarch provides public tracker for feature requests, bug reports on it Github repo.</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes, the contact is Monarch Initiative. Contact information is provided.</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#d4edda;">Yes, the KG is updated every month.</td></tr>
<tr><td>updated_annually</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#d4edda;">Yes, prior versions are accessible. And there is a dashoboard for QC showing what the changes are between any two versions. <a href="https://qc.monarchinitiative.org/#monarch?dataset=Development&amp;kgVersion=2025-07-09">https://qc.monarchinitiative.org/#monarch?dataset=Development&amp;kgVersion=2025-07-09</a></td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes, Monarch KG is used in Exomiser which is a tool to annotate variants and has a ChatGPT plugin through RAG to support information search. It is also integrated into the GRAPE library for graph analysis and machine learning.</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#f8d7da;">No</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes, Monarch aims to harmonize the data across the fields (gene, disease, phenotype across species) to facilitate the discovery of disease mechanism and aid the disease diagnosis.</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Yes, created Monarch Quality Control (QC) Dashboard for quality metrics that are specific to Monarch. In addition, it developed Phenotypic Inference Evaluation Framework (PhEval) to evaluate the analysis of its tool Exomiser.</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td>Kind of but not explicit. The edge data contains columns like provided_by, publications, and has_evidence to measure the accuracy or confidence.</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/10</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY 4.0</td></tr>
</tbody></table></div>

