---
evaluation_date: '2025-08-14'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Can access paths, DWPCs, prediction probabilities, network support breakdowns for compound–disease pairs (via Neo4j Browser &amp; guides)</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Fully hosted on a public Neo4j instance with Cypher queries, guides, tutorials <a href="https://neo4j.het.io/browser/">https://neo4j.het.io/browser/</a></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Downloadable as JSON, Neo4j DB, TSV; also query online in Neo4j Browser; source code &amp; intermediate datasets on GitHub, Zenodo, Figshare</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>The source code and scripts are public on hetio and GitHub linked in the paper <a href="https://github.com/elifesciences-publications/hetionet">https://github.com/elifesciences-publications/hetionet</a></td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Multiple export formats (JSON, Neo4j dump, TSV)</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>29 sources documented; each node/edge carries source information in properties; full list with versions in paper <a href="https://elifesciences.org/articles/26726">https://elifesciences.org/articles/26726</a></td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Versions noted: e.g., DrugBank v4.2, SIDER v4.1, LINCS L1000 (Oct 2015), Pathway Commons (with date)</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Input ontologies and databases fully listed with versions; also intermediate resources described (e.g., STARGEO, PharmacotherapyDB</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Node/edge properties include URLs, source, license, confidence scores (for applicable edges)</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Merged redundant pathways; multiple studies for same edge consolidated; non-informative gene sets removed</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Explicit per metaedge: e.g., binding affinities (≤1 mM), co-occurrence p-values (MEDLINE), gene interaction specifics</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Clear metagraph with 11 node types &amp; 24 metaedges; each with documented origin &amp; justification</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Uses standard biomedical IDs: Entrez, UMLS, MeSH, DO, Uberon</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Entrez Gene, DOID, MeSH IDs, InChIKeys used for easy cross-referencing</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Extensive: paper + Thinklab logs + GitHub issues + detailed guides</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Explained pruning (e.g., filtering Uberon terms, merging pathways, restricting GO terms by size)</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Metagraph is the explicit schema; node and edge types clearly defined</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Partial - “v1.0” labeled, but no formal version history beyond initial</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Partial - Thinklab (now static); issues can be filed on GitHub</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Daniel Himmelstein and team, contactable via GitHub, Thinklab archives, paper</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>Only v1.0 publicly released so far</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>Early versions mentioned but no archived download versions listed</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Nicotine dependence (bupropion), epilepsy predictions (acamprosate)</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>Compared to PREDICT, Guney et al., Cheng et al.; used baselines &amp; permutation</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Designed for systematic drug repurposing + broader knowledge integration</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>DWPC + AUROC + permutation + cross-validation + external test sets (DrugCentral, ClinicalTrials.gov)</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Probability scores, cross-validated elastic net, path-level contribution breakdowns, AUROC</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC0 1.0</td></tr>
</tbody></table></div>

