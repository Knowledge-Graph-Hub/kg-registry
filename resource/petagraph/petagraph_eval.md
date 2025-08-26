---
evaluation_date: '2025-08-25'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Portions of the graph that are open licensed are available from <a href="https://osf.io/6jtc9/files/osfstorage">https://osf.io/6jtc9/files/osfstorage</a></td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>(ish), neo4j dump can be downloaded if you have a UMLS license key, and there are instructions to build a neo4j from sources in the github repository. Ish, because it&#x27;s not specifically hosted, you need to host it yourself.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>(ish) completed graph can only be downloaded as neo4j, components to build the graph can also be downloaded, but that doesn&#x27;t quite feel like it makes a yes</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>ETL of upstream sources lives in <a href="https://github.com/x-atlas-consortia/ubkg-etl/">https://github.com/x-atlas-consortia/ubkg-etl/</a></td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>With UMLS api key</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Methods section of paper <a href="https://www.nature.com/articles/s41597-024-04070-w#Sec2">https://www.nature.com/articles/s41597-024-04070-w#Sec2</a></td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Ish, some source versions listed in <a href="https://github.com/TaylorResearchLab/Petagraph/tree/main/Scientific_Data_2024">https://github.com/TaylorResearchLab/Petagraph/tree/main/Scientific_Data_2024</a></td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Ubkg etl has requirements.txt, petagraph has requirements-test.txt</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>. They either come from existing ontologies or have one file per datasource with edges and nodes that are being added.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Yes. Bidirectional edges are only for Concept–Concept; other edges are unidirectional. Redundancies are minimized using binning and source normalization</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Methods of paper</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Custom schema defined in paper</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Csv files</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Concept CUI with codes corresponding to common external ID/s</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Well documented github</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Guidlines for formatting ontologies in user guide, method explain preprocessing steps</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Start with ontologies and standards in the UBKG and add in omics data based on their paper defined in the schema</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>Lists date last updated but no version</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contributors listed <a href="https://osf.io/6jtc9/">https://osf.io/6jtc9/</a></td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Frequent small updates</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Recent acitivty documents date of all changes and person who made them but prior versions not accessible <a href="https://osf.io/6jtc9/">https://osf.io/6jtc9/</a></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Several in paper</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Integrating/analyzing multiomics datasets</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Link prediction tasks auROC, precision-recall, top tissues associated w a disease, and shortest path analysis of subgraphs</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>. AUC-ROC, Precision-Recall curves, common neighbors vs random, structural metrics compared to randomized graphs</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY-NC-ND 4.0</td></tr>
</tbody></table></div>

