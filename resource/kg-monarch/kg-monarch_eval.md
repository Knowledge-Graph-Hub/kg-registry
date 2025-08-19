---
evaluation_date: '2025-08-19'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Can access the mapping schema biolink model which provides sematics mappings and ontological relationships, can access downloadable graph dumps in SciGraph or KGX formats.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Can access by Monarch&#x27;s own webpage, API, Neo4j, downloadable Graph.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Monarch provides multiple ways to download the data such as KGX TSV, KGX JSON lines, Neo4j Dump, etc.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Can access the source code for making the KG on Github.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>KGX TSV, KGX JSON lines, Neo4j Dump, etc.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>33 heterogeneous data sources including HPOA, CTD, OMIM, Orphanet, WormBase, FlyBase, MGI, dictyBase, Xenbase, SGD, RGD, PomBase, ZFIN, NCBI, HGNC, Panther, BGeeDB, Reactome, STRING.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Provides the version info of the sources used: <a href="https://data.monarchinitiative.org/monarch-kg-dev/latest/index.html">https://data.monarchinitiative.org/monarch-kg-dev/latest/index.html</a></td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Declared dependencies through its build infrastructure in the monarch-ingest and kg-hub Github repo. Specifically, Monarch uses Poetry for the dependencies management.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Nodes and edges contain the most upstream source and knowledge provider information.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Duplicate edge and node management is taken into consideration in the construction of the KG.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>The triples created are captured in multiple stages of the KG ingest pipeline including the biolink preddicate mappings and the output.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Biolink model. All relationships are mapped to Biolink predicates.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Monarch KG is both human-readable and usable. Monarch provides its data in tablular formats that are easy to understand. Also, Monarch KG data and its Monarch initaitive webpage can be used in bioinformatics &amp; biomedical analysis, machine learning, NLP, LLMs, visualization &amp; exploration, etc.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Supports resolvable and externally linked identifiders. Monarch KG uses curie-style IDs that follow identifier conventions and are mappable to URLs for resolution. Also, it includes a column called xref which contains a list of external identifiers.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Monarch made great effort to document its KG construction including data ingestion, transformation, schema usage, and KG merging.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Monarch documented data transforms including the excluded nodes and dangling edges.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Monarch uses a documented schema, Biolink Model, and its monarch-ingest pipeline for construction.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td></td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Monarch provides public tracker for feature requests, bug reports on it Github repo.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>The contact is Monarch Initiative. Contact information is provided.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>The KG is updated every month.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Prior versions are accessible. And there is a dashoboard for QC showing what the changes are between any two versions. <a href="https://qc.monarchinitiative.org/#monarch?dataset=Development&amp;kgVersion=2025-07-09">https://qc.monarchinitiative.org/#monarch?dataset=Development&amp;kgVersion=2025-07-09</a></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Monarch KG is used in Exomiser which is a tool to annotate variants and has a ChatGPT plugin through RAG to support information search. It is also integrated into the GRAPE library for graph analysis and machine learning.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Monarch aims to harmonize the data across the fields (gene, disease, phenotype across species) to facilitate the discovery of disease mechanism and aid the disease diagnosis.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Created Monarch Quality Control (QC) Dashboard for quality metrics that are specific to Monarch. In addition, it developed Phenotypic Inference Evaluation Framework (PhEval) to evaluate the analysis of its tool Exomiser.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Kind of but not explicit. The edge data contains columns like provided_by, publications, and has_evidence to measure the accuracy or confidence.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

