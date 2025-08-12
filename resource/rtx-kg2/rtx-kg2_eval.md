---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>, RTX-KG2 is able to provide various biomedical information through queries. It is also used as backend to support ARAX&#x27;s path reasoning and path ranking (<a href="https://github.com/RTXteam/RTX)">https://github.com/RTXteam/RTX)</a> .</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>, can access by API query, and Neo4j.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>, multiple ways to access including downloadable versions, API (SmartAPI), web browser user interface (seems not currently working).</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>, Github (<a href="https://github.com/RTXteam/RTX-KG2)">https://github.com/RTXteam/RTX-KG2)</a></td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>, downloadable versions are available on Github</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>, 70 sources Table 1 (UMLS, SemMedDB, ChEMBL, DrugBank, Reactome, SMPDB, and 64 additional knowledge sources).</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>, it documents the versions of the upstream sources used (<a href="https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).">https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).</a></td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>, in the requirements file.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>, node&#x27;s ID contains source information and edge contains primary knowledge source.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>, it provides a pre-canonicalized graph version (RTX-KG2pre, with semantically duplicated concepts) and a canonicalized version (RTX-KG2c, withthout semantically duplicated concepts)</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>, in the final output KG, each edge includes the source that reated that triple.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>, it uses Biolink Model for as the schema standard for both nodes and edges.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>, it is used for other biological applications such as answering translational science questions, drug repositioning, identifying new therapeutic targets, and understanding drug mechanisms.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>, it uses resolvable IDs for the entities.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>, it has clear and step by step documentation on construction on its Github repo</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>, in Appendix</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>, Biolink model and extract-transform-load (ETL) approach for construction.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>, it is using semantic versioning (e.g., KG2.7.3)</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>, provides public tracker for requests, bug reports on it Github repo.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>, it provides contact information of the KG2 Team.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>, once per month (mentioned in Discussion).</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>, the prior versions are accessible (<a href="https://github.com/ncats/translator-lfs-artifacts/blob/main/README.md)">https://github.com/ncats/translator-lfs-artifacts/blob/main/README.md)</a> with documented changes (<a href="https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).">https://github.com/RTXteam/RTX-KG2/blob/master/docs/kg2-versions.md).</a></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>, it is currently being used by multiple Translator reasoning agents such as ARAX (Autonomous Relay Agent X).</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>, it is compared to four other KGs (Hetionet, SPOKE, the SRI Reference Knowledge Graph, and ROBOKOP)</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>, it is a part of NCATS Biomedical Data Translator project to support automated biomedical reasoning and question answering. It aims to create a semantically standardized, computable, and interoperable biomedical KG that supports translational reasoning and biomedical discovery.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>, it is not only evaluated with other KGs, but also evaluated on the tools that utilize it such as ARAX, mediKanren, BioThings Explorer, and  ARAGORN.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>, the nodes and edges contain evidence, provenance, and other information for measuring accuracy and confidence.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

