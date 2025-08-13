---
evaluation_date: '2025-08-13'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>ClinicalBERT-based embeddings were used to group disease nodes, providing an embedding-derived version of the graph</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Available via Harvard Dataverse with raw KG (kg raw.csv) and largest connected component (kg giant.csv) <a href="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM">https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM</a></td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Full source code is available on GitHub <a href="https://github.com/mims-harvard/PrimeKG">https://github.com/mims-harvard/PrimeKG</a></td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Harvard Dataverse Repo hosts the downloadable KG and intermediate files <a href="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM">https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM</a></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>20 primary data sources listed, including DisGeNET, DrugBank, UMLS, Orphanet, etc. in the paper <a href="https://www.nature.com/articles/s41597-023-01960-3">https://www.nature.com/articles/s41597-023-01960-3</a></td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Explicit versions and download dates provided for each dataset in the Methods/Data Records section</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Partially - Tools like goatools, beautifulsoup, regex scripts, and vocabulary mappings are mentioned in the GitHub repo, but not all formal dependencies are listed</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each node contains node source; edges are annotated by type and origin</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Duplicates and self-loops were removed during KG preprocessing and merging</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Clear documentation on what triples were derived from which resource (e.g., drug–protein from DrugBank, phenotype–disease from HPO)</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>The paper documented schema of 30 edge types and their origin ontologies</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Clinical and pharmacological text features are readable and interpretable (e.g., Mayo Clinic descriptions, DrugBank pharmacodynamics)</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses Mondo, DrugBank, HPO, MeSH, Entrez Gene IDs, and UMLS CUIs, which are mappable and resolvable via external resources</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Extensive paper + GitHub repo</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Transformations like self-loop removal, duplicate dropping, phenotype-disease resolution, and mapping across ontologies are documented</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Node and edge formats, and their standardized schema, are explained in the methodology and data files</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>No version tags (e.g., v1.0, v1.1) are mentioned or used on Dataverse or GitHub</td></tr>
<tr><td>Public tracker information</td><td></td><td>GitHub Issues tab is not actively used for public feature requests or bug tracking</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Maintained by Zitnik Lab at Harvard with lab contact and GitHub maintainers listed</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>Only one release version is available as of now (May 2022)</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No archived prior versions or changelog indicating updates</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/4</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Autism case study demonstrates disease concept resolution and clinical alignment</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>Compared to other KGs (e.g., SPOKE); benchmarks and references to prior systems included</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused on disease-centric precision medicine with defined coverage: 17,080 diseases, 10 biological scales, 20 sources</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Structure connectivity, edge density, text embedding-based grouping, and clinical relevance tested</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Partially - Uses similarity thresholds (e.g., cosine ≥ 0.98 for disease grouping); no formal metrics like precision/recall provided</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

