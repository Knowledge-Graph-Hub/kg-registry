---
layout: eval_detail
---

# Evaluation for pharmkg

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>access_otherthanKG_text</td><td style="background-color:#d4edda;">Yes - PharmKG provides embeddings, learned low-dimensional representations for entities and relations via KGE models. It also provides top predicted paths for mechanistic interpretation (Fig 6) and t-SNE visualizations showing semantic structure (Fig 5).</td></tr>
<tr><td>access_otherthanKG</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>api_or_online_access_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>api_or_online_access</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options_text</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>multi_access_options</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>sourcecode_available_text</td><td style="background-color:#d4edda;">Yes - The full source code for KG construction, processing, and the Heterogeneous Graph Attention Network (HRGAT) embedding model is provided on the GitHub repository https://github.com/MindRank-Biotech/PharmKG/tree/master</td></tr>
<tr><td>sourcecode_available</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>downloadable_KG_text</td><td style="background-color:#d4edda;">Yes - The benchmark KG is downloadable. They also provide both the clean version (final benchmark) and the raw version (with more entities and relations); the KG dataset is guarded by Google Drive permissions to access it</td></tr>
<tr><td>downloadable_KG</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>source_list_provided_text</td><td style="background-color:#d4edda;">Yes — An integration of 6 sources (OMIM, DrugBank, PharmGKB, TTD, SIDER, HumanNet); plus entity features from MeSH, PubChem, BioBERT, BioGPS, and Connectivity Map</td></tr>
<tr><td>source_list_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>source_versions_info_text</td><td style="background-color:#f8d7da;">No - Do mention integrating “recent versions” of each source and give details of ID mapping and unification (e.g., Entrez Gene ID, MeSH hierarchy) but no explicit version numbers or file names for each data dump are shown in the text</td></tr>
<tr><td>source_versions_info</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>import_dependancies_text</td><td style="background-color:#d4edda;">Yes - The code is built on Pykeen and KG-reeval, with details for training and hyperparameters. Also mentions use of RDKit for chemical fingerprints and BioBERT for embeddings</td></tr>
<tr><td>import_dependancies</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>node_edge_sources_text</td><td>Partially - Confirms that nodes were unified with standard IDs (Entrez, MeSH, PubChem) and that duplicate synonyms were resolved, but it doesn’t state that each edge carries explicit source provenance tags — only that relations were merged and thematically assigned using Global Network of Biomedical Relationships (GNBR)</td></tr>
<tr><td>node_edge_sources</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edges_deduplication_text</td><td style="background-color:#d4edda;">Yes - Explicitly describes merging overlapping triplets, disambiguation with synonym tables, and merging semantically similar relations using clustering</td></tr>
<tr><td>edges_deduplication</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>triples_source_details_text</td><td style="background-color:#d4edda;">Yes - Explains how 29 relation types were derived, how Global Network of Biomedical Relationships (GNBR) semantic themes were mapped, and which sources contribute to which entity types and interactions</td></tr>
<tr><td>triples_source_details</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>edge_type_schema_text</td><td style="background-color:#d4edda;">Yes - Documents edge semantics: “interaction,” “disease-gene,” “chemical-gene,” “disease-chemical,” and subtypes — all mapped from Global Network of Biomedical Relationships (GNBR) semantic themes and curated bases</td></tr>
<tr><td>edge_type_schema</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>bio_usable_data_text</td><td style="background-color:#d4edda;">Yes - All entities explicitly use standard biomedical identifiers and the structure is designed to support drug repurposing, target discovery, adverse reaction prediction, etc., in real-world biomedical tasks</td></tr>
<tr><td>bio_usable_data</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>resolvable_ids_text</td><td style="background-color:#d4edda;">Yes - Genes use Entrez Gene IDs; diseases use MeSH IDs; chemicals use PubChem IDs</td></tr>
<tr><td>resolvable_ids</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>construction_docs_text</td><td style="background-color:#d4edda;">Yes - Explains the construction in detail, including entity filtering, merging, disambiguation, feature extraction, and the final schema design</td></tr>
<tr><td>construction_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>transform_docs_text</td><td style="background-color:#d4edda;">Yes - Removed trivial entities, merged low-level symptoms into MeSH parent diseases, clustered and merged redundant relation types, applied PCA for feature reduction, and explain all steps clearly</td></tr>
<tr><td>transform_docs</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>schema_used_text</td><td style="background-color:#d4edda;">Yes - 29 defined relation types with source mapping and entity categories; and semantics from Global Network of Biomedical Relationships (GNBR) themes and curated bases</td></tr>
<tr><td>schema_used</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>stable_versions_text</td><td style="background-color:#f8d7da;">No - There is no formal semantic versioning scheme mentioned for the dataset or codebase</td></tr>
<tr><td>stable_versions</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>public_tracker_text</td><td style="background-color:#f8d7da;">No - There is no mention of a public tracker for feature requests or issues</td></tr>
<tr><td>public_tracker</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>kg_contact_info_text</td><td style="background-color:#d4edda;">Yes - Two corresponding authors are provided with full institutional contacts (Prof. Yuedong Yang and Dr. Zhangming Niu) in the published paper (https://academic.oup.com/bib/article/22/4/bbaa344/6042240)</td></tr>
<tr><td>kg_contact_info</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>updated_annually_text</td><td style="background-color:#f8d7da;">No - No evidence yet. They state they plan future expansions (e.g., transcriptomics, clinical data, auto-extraction) but no recurring updates are published so far</td></tr>
<tr><td>updated_annually</td><td style="background-color:#f8d7da;">N</td></tr>
<tr><td>prior_versions_access_text</td><td>Partially - They do provide the raw version alongside the final benchmark on GitHub but do not maintain a changelog across multiple yearly versions</td></tr>
<tr><td>prior_versions_access</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>use_case_provided_text</td><td style="background-color:#d4edda;">Yes - Provide detailed case studies for Alzheimer’s disease and Parkinson’s disease for drug repurposing and target discovery, with literature validation, top scored predictions, and visualized paths</td></tr>
<tr><td>use_case_provided</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>eval_against_others_text</td><td style="background-color:#d4edda;">Yes - Benchmarked Heterogeneous Graph Attention Network (HRGAT) and 9 other KGE baselines on Hetionet and PharmKG side by side and analyzed results</td></tr>
<tr><td>eval_against_others</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>defined_scope_text</td><td style="background-color:#d4edda;">Yes - The paper is a dedicated benchmark for evaluating KGE models in biomedical relation prediction, with explicit focus on drug repurposing, target identification, and multi-relation prediction tasks</td></tr>
<tr><td>defined_scope</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>multi_eval_methods_text</td><td style="background-color:#d4edda;">Yes - Link prediction (MRR, Hits@k), downstream tasks (AUROC, AUPRC), t-tests for significance</td></tr>
<tr><td>multi_eval_methods</td><td style="background-color:#d4edda;">Y</td></tr>
<tr><td>accuracy_metrics_text</td><td style="background-color:#d4edda;">Yes - Multiple: MRR, Hits@1/3/10/100, AUROC, AUPRC, p-values for statistical tests, plus visualization and interpretability checks with t-SNE plots and path analyses</td></tr>
<tr><td>accuracy_metrics</td><td style="background-color:#d4edda;">Y</td></tr>
</tbody></table></div>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
<tr><td>License_text</td><td style="background-color:#f8d7da;">No explicit license (restricted use). The paper notes: “© The Author(s) 2020. Published by Oxford University Press. All rights reserved.” But does not reveal license information (nor does the GitHub repo)</td></tr>
</tbody></table></div>

