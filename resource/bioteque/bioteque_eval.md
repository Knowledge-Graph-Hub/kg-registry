---
layout: eval_detail
---

# Evaluation for bioteque

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Y (Bioteque provides node-type-specific embeddings for 11 of the node types in its graph, along with downloadable sets of those individual sets of nodes mapped to their representations in the embeddings.)</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Y (Source code for assembling the KG is provided in a GitHub repository, https://github.com/sbnb-irb/bioteque. This includes source-specific scripts for retrieving data components.)</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Y (see https://bioteque.irbbarcelona.org/sources)</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Y (The list of data sources is documented and includes specific mentions of source files in its data retrieval scripts, e.g., the source for COSMIC is defined here: https://github.com/sbnb-irb/bioteque/blob/master/datasets/cosmic_mutsig/get_data.sh)</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Y (The sources of nodes and edges are provided in the documentation and the node files.)</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Y (The 2022 Bioteque paper makes two notes about duplicate resolution: "...we first mapped the samples and genes to our reference vocabulary and collapsed the duplicates by their mean value", and "We mapped the cell lines and genes to our reference vocabularies and took the mean value whenever duplicates occurred".)</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Y (The list of data sources is documented and makes specific mention of which associations are derived from which sources; see https://bioteque.irbbarcelona.org/sources)</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Y (the provided node files are provided as TSVs, though assembly of a full KG would require running the graph assembly code. It appears that the assembly code also produces nodes and edges in a TSV format.)</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Y (node identifiers are from clearly defined sources and expressed as CURIEs)</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Y (Documentation regarding the assembly code is provided; see https://github.com/sbnb-irb/bioteque)</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Y (each source has its own transform code and documentation, provided on the GitHub repo, https://github.com/sbnb-irb/bioteque)</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>schema_used</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#d4edda;">Y (the GitHub repository at https://github.com/sbnb-irb/bioteque is public and permits issue creation).</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Y (it's never explicitly stated as a contact, but the responsible organization, the Structural Bioinformatics and Network Biology Group at the Institute for Research in Biomedicine Barcelona, is identified along with a link to their home page)</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>updated_annually</td><td></td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Y (Examples of use are described in the 2022 Nat Comm paper; an example of generating predictions for drug repurposing is provided.)</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>defined_scope</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Y (Multiple evaluation methods are provided in the 2022 Nat Comm paper, primarily for embedding evaluation.)</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Y (Multiple validation methods are provided in the 2022 Nat Comm paper, including two distinct analyses involving gene expression data and protein-protein interactions, respectively.)</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC BY 4.0</td></tr>
</tbody></table></div>

