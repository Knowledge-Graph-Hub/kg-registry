---
evaluation_date: '2025-08-20'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>PharmKG provides embeddings, learned low-dimensional representations for entities and relations via KGE models. It also provides top predicted paths for mechanistic interpretation (Fig 6) and t-SNE visualizations showing semantic structure (Fig 5).</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>The full source code for KG construction, processing, and the Heterogeneous Graph Attention Network (HRGAT) embedding model is provided on the GitHub repository <a href="https://github.com/MindRank-Biotech/PharmKG/tree/master">https://github.com/MindRank-Biotech/PharmKG/tree/master</a></td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>The benchmark KG is downloadable. They also provide both the clean version (final benchmark) and the raw version (with more entities and relations); the KG dataset is guarded by Google Drive permissions to access it</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>An integration of 6 sources (OMIM, DrugBank, PharmGKB, TTD, SIDER, HumanNet); plus entity features from MeSH, PubChem, BioBERT, BioGPS, and Connectivity Map</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>Do mention integrating “recent versions” of each source and give details of ID mapping and unification (e.g., Entrez Gene ID, MeSH hierarchy) but no explicit version numbers or file names for each data dump are shown in the text</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>The code is built on Pykeen and KG-reeval, with details for training and hyperparameters. Also mentions use of RDKit for chemical fingerprints and BioBERT for embeddings</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Partially - Confirms that nodes were unified with standard IDs (Entrez, MeSH, PubChem) and that duplicate synonyms were resolved, but it doesn’t state that each edge carries explicit source provenance tags — only that relations were merged and thematically assigned using Global Network of Biomedical Relationships (GNBR)</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Explicitly describes merging overlapping triplets, disambiguation with synonym tables, and merging semantically similar relations using clustering</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Explains how 29 relation types were derived, how Global Network of Biomedical Relationships (GNBR) semantic themes were mapped, and which sources contribute to which entity types and interactions</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Documents edge semantics: “interaction,” “disease-gene,” “chemical-gene,” “disease-chemical,” and subtypes — all mapped from Global Network of Biomedical Relationships (GNBR) semantic themes and curated bases</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 6/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>All entities explicitly use standard biomedical identifiers and the structure is designed to support drug repurposing, target discovery, adverse reaction prediction, etc., in real-world biomedical tasks</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Genes use Entrez Gene IDs; diseases use MeSH IDs; chemicals use PubChem IDs</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Explains the construction in detail, including entity filtering, merging, disambiguation, feature extraction, and the final schema design</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Removed trivial entities, merged low-level symptoms into MeSH parent diseases, clustered and merged redundant relation types, applied PCA for feature reduction, and explain all steps clearly</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>29 defined relation types with source mapping and entity categories; and semantics from Global Network of Biomedical Relationships (GNBR) themes and curated bases</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>There is no formal semantic versioning scheme mentioned for the dataset or codebase</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>There is no mention of a public tracker for feature requests or issues</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Two corresponding authors are provided with full institutional contacts (Prof. Yuedong Yang and Dr. Zhangming Niu) in the published paper (<a href="https://academic.oup.com/bib/article/22/4/bbaa344/6042240)">https://academic.oup.com/bib/article/22/4/bbaa344/6042240)</a></td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>No evidence yet. They state they plan future expansions (e.g., transcriptomics, clinical data, auto-extraction) but no recurring updates are published so far</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Partially - They do provide the raw version alongside the final benchmark on GitHub but do not maintain a changelog across multiple yearly versions</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Provide detailed case studies for Alzheimer’s disease and Parkinson’s disease for drug repurposing and target discovery, with literature validation, top scored predictions, and visualized paths</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>Benchmarked Heterogeneous Graph Attention Network (HRGAT) and 9 other KGE baselines on Hetionet and PharmKG side by side and analyzed results</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>The paper is a dedicated benchmark for evaluating KGE models in biomedical relation prediction, with explicit focus on drug repurposing, target identification, and multi-relation prediction tasks</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Link prediction (MRR, Hits@k), downstream tasks (AUROC, AUPRC), t-tests for significance</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Multiple: MRR, Hits@1/3/10/100, AUROC, AUPRC, p-values for statistical tests, plus visualization and interpretability checks with t-SNE plots and path analyses</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>Explicit license (restricted use). The paper notes: “© The Author(s) 2020. Published by Oxford University Press. All rights reserved.” But does not reveal license information (nor does the GitHub repo)</td></tr>
</tbody></table></div>

