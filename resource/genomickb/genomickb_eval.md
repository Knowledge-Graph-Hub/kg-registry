---
evaluation_date: '2025-08-19'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Can submit an online query and download subgraphs that meet criteria</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Website with UI for creating queries, API supposely coming in v2, Neo4j dump available but not hosted by creators</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Can use online query tool or download Neo4j dump</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Https://github.com/tinalee-tech/KG-dataloader</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Neo4j dump</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Supplementary note 1</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Import dependencies</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Tables 1 (nodes)  &amp; 2 (edges), query allows users to restrict by datasource</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Considered but not de-duplicated. Users can restric querys to specific datasources and duplicate edges can be used for validation. EX:  ‘enhancer regulate gene’ with restriction ‘cell_line=GM12878’ and ‘data_source=EnhancerAtlas’ -&gt; 118,610 node pairs. A second query for ‘variant overlap enhancer’, ‘enhancer regulate gene’, and ‘variant correlate_with gene’ -&gt;  16,871  enhancer-gene pairs from EnhancerAtlas can be validated by GTEx eQTLs</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Table 2</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Table 2</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>They have a web interface (<a href="https://gkb.dcmb.med.umich.edu/)">https://gkb.dcmb.med.umich.edu/)</a> presenting the entities and edges in a human-readable format. It can be used to answer genomics-related questions and conduct biological analysis</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses one external ID when possible and defines globaly unique IDs for entities without such as ChIP-seq peaks</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Github and supplement</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Sup Note 1 Data Collection and Processing</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Uses custom schema not an existing one but does provide documentation</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>But still on version 1.0 despite multiple upates listed</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>FAQ says to email the team</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Website has a contacts button with name/emal for both technical details and accessing the data/web server</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>During 2022-2023 yes but not since then</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Clearly documented chages with dates but prior versions not available. *Paper states that they store all versions internally and can revert if unexpected changes are ever made to their graph but these are not accessible publicaly</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#f8d7da;">N</td><td>The paper provides examples of specific queries that can be performed through the website that would normally require coding and integrating multiple data sources, but it is limited to knowledge extraction and does not show how this could be used to make novel biological discoveries</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Coding free queries of human genomic information including both functional, strutural, epigenetic and other relationships</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Kind of but not explicitly. Since this tool is all about data querying, confidence could be assesed by creating multiple queries like the example of using eQTLs to &quot;validate&quot; EnhancerAtlas relationships</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY-NC 4.0</td></tr>
</tbody></table></div>

