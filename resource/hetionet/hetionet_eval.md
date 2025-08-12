---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes - Can access paths, DWPCs, prediction probabilities, network support breakdowns for compound–disease pairs (via Neo4j Browser &amp; guides)</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#d4edda;">Yes - fully hosted on a public Neo4j instance with Cypher queries, guides, tutorials <a href="https://neo4j.het.io/browser/">https://neo4j.het.io/browser/</a></td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#d4edda;">Yes - Downloadable as JSON, Neo4j DB, TSV; also query online in Neo4j Browser; source code &amp; intermediate datasets on GitHub, Zenodo, Figshare</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Yes, the source code and scripts are public on hetio and GitHub linked in the paper <a href="https://github.com/elifesciences-publications/hetionet">https://github.com/elifesciences-publications/hetionet</a></td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Yes - Multiple export formats (JSON, Neo4j dump, TSV)</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Yes - 29 sources documented; each node/edge carries source information in properties; full list with versions in paper <a href="https://elifesciences.org/articles/26726">https://elifesciences.org/articles/26726</a></td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#d4edda;">Yes - Versions noted: e.g., DrugBank v4.2, SIDER v4.1, LINCS L1000 (Oct 2015), Pathway Commons (with date)</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Yes - Input ontologies and databases fully listed with versions; also intermediate resources described (e.g., STARGEO, PharmacotherapyDB</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td style="background-color:#d4edda;">Yes - Node/edge properties include URLs, source, license, confidence scores (for applicable edges)</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes - Merged redundant pathways; multiple studies for same edge consolidated; non-informative gene sets removed</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes - Explicit per metaedge: e.g., binding affinities (≤1 mM), co-occurrence p-values (MEDLINE), gene interaction specifics</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes - Clear metagraph with 11 node types &amp; 24 metaedges; each with documented origin &amp; justification</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 14/14</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes - Uses standard biomedical IDs: Entrez, UMLS, MeSH, DO, Uberon</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes - Entrez Gene, DOID, MeSH IDs, InChIKeys used for easy cross-referencing</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes - Extensive: paper + Thinklab logs + GitHub issues + detailed guides</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Yes - Explained pruning (e.g., filtering Uberon terms, merging pathways, restricting GO terms by size)</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#d4edda;">Yes - Metagraph is the explicit schema; node and edge types clearly defined</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td>Partial - “v1.0” labeled, but no formal version history beyond initial</td></tr>
<tr><td>stable_versions</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>public_tracker_text</td><td>Partial - Thinklab (now static); issues can be filed on GitHub</td></tr>
<tr><td>public_tracker</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes - Daniel Himmelstein and team, contactable via GitHub, Thinklab archives, paper</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">No - Only v1.0 publicly released so far</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td style="background-color:#f8d7da;">No - Early versions mentioned but no archived download versions listed</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#f8d7da;">N</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/10</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes - Nicotine dependence (bupropion), epilepsy predictions (acamprosate)</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#d4edda;">Yes - Compared to PREDICT, Guney et al., Cheng et al.; used baselines &amp; permutation</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes - Designed for systematic drug repurposing + broader knowledge integration</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Yes - DWPC + AUROC + permutation + cross-validation + external test sets (DrugCentral, ClinicalTrials.gov)</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Yes - Probability scores, cross-validated elastic net, path-level contribution breakdowns, AUROC</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 10/10</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td>CC0 1.0</td></tr>
</tbody></table></div>

