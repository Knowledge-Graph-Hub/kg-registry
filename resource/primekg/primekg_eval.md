---
layout: eval_detail
---

# Evaluation for primekg

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes - ClinicalBERT-based embeddings were used to group disease nodes, providing an embedding-derived version of the graph</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Yes - Available via Harvard Dataverse with raw KG (kg raw.csv) and largest connected component (kg giant.csv) https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Yes - Full source code is available on GitHub https://github.com/mims-harvard/PrimeKG</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Yes - Harvard Dataverse Repo hosts the downloadable KG and intermediate files https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Yes - 20 primary data sources listed, including DisGeNET, DrugBank, UMLS, Orphanet, etc. in the paper https://www.nature.com/articles/s41597-023-01960-3</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">Yes - Explicit versions and download dates provided for each dataset in the Methods/Data Records section</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td>Partially - Tools like goatools, beautifulsoup, regex scripts, and vocabulary mappings are mentioned in the GitHub repo, but not all formal dependencies are listed</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes - Each node contains node source; edges are annotated by type and origin</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes - Duplicates and self-loops were removed during KG preprocessing and merging</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes - Clear documentation on what triples were derived from which resource (e.g., drug–protein from DrugBank, phenotype–disease from HPO)</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes - The paper documented schema of 30 edge types and their origin ontologies</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes - Clinical and pharmacological text features are readable and interpretable (e.g., Mayo Clinic descriptions, DrugBank pharmacodynamics)</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes - Uses Mondo, DrugBank, HPO, MeSH, Entrez Gene IDs, and UMLS CUIs, which are mappable and resolvable via external resources</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes - Extensive paper + GitHub repo</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Yes - Transformations like self-loop removal, duplicate dropping, phenotype-disease resolution, and mapping across ontologies are documented</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#d4edda;">Yes - Node and edge formats, and their standardized schema, are explained in the methodology and data files</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">No - No version tags (e.g., v1.0, v1.1) are mentioned or used on Dataverse or GitHub</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#f8d7da;">No - GitHub Issues tab is not actively used for public feature requests or bug tracking</td></tr>
<tr><td>public_tracker</td><td></td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes - Maintained by Zitnik Lab at Harvard with lab contact and GitHub maintainers listed</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">No - Only one release version is available as of now (May 2022)</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#f8d7da;">No - No archived prior versions or changelog indicating updates</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes - Autism case study demonstrates disease concept resolution and clinical alignment</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#d4edda;">Yes - Compared to other KGs (e.g., SPOKE); benchmarks and references to prior systems included</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes - Focused on disease-centric precision medicine with defined coverage: 17,080 diseases, 10 biological scales, 20 sources</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Yes – Structure connectivity, edge density, text embedding-based grouping, and clinical relevance tested</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td>Partially - Uses similarity thresholds (e.g., cosine ≥ 0.98 for disease grouping); no formal metrics like precision/recall provided</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY 4.0</td></tr>
</tbody></table></div>

