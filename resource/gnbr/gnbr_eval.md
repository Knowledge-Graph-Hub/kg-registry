---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>can access themes which relate to the path types and their score</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7da;">N</td><td>but can get code to process data</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>but its very weirdly done; separated into files by edge types</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>but NLP so not many databases used</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>pubtator annotations from april 30, 2016</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>detailed dependancy path extraction;</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>each edge has a lot of information; NLP was used and the sentance that constructed something is listed</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>counted as a co occurance; feature not a bug used to inform network</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>very limited</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>NLP; had four interaction types and three node types</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>all information coming from publications outside of KG</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>uses UMLS IDs for rare diseases</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>specifies where disease and drug nodes come from</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>eliminated paths containing dependencies of type conj</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>self documented and reported with downloads</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>7 versions available</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>but not updated since 2019</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>and indicated which version was used in the paper</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>drug disease indications ; 2 case studies</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>compared to gold standard drug indications; relationships from other databases for those gotten using NLP methods</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>drug repurposing</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>case studies; drug-disease path analysis; validation using DGIdb; used lit review to verify novel drug</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>performance on gold standard drug indications calculate AUROC; dendrograms of the themes</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

