---
evaluation_date: '2025-08-12'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Bioteque provides node-type-specific embeddings for 11 of the node types in its graph, along with downloadable sets of those individual sets of nodes mapped to their representations in the embeddings.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Source code for assembling the KG is provided in a GitHub repository, <a href="https://github.com/sbnb-irb/bioteque.">https://github.com/sbnb-irb/bioteque.</a> This includes source-specific scripts for retrieving data components.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>See <a href="https://bioteque.irbbarcelona.org/sources">https://bioteque.irbbarcelona.org/sources</a></td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>The list of data sources is documented and includes specific mentions of source files in its data retrieval scripts, e.g., the source for COSMIC is defined here: <a href="https://github.com/sbnb-irb/bioteque/blob/master/datasets/cosmic_mutsig/get_data.sh">https://github.com/sbnb-irb/bioteque/blob/master/datasets/cosmic_mutsig/get_data.sh</a></td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>The sources of nodes and edges are provided in the documentation and the node files.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>The 2022 Bioteque paper makes two notes about duplicate resolution: &quot;...we first mapped the samples and genes to our reference vocabulary and collapsed the duplicates by their mean value&quot;, and &quot;We mapped the cell lines and genes to our reference vocabularies and took the mean value whenever duplicates occurred&quot;.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>The list of data sources is documented and makes specific mention of which associations are derived from which sources; see <a href="https://bioteque.irbbarcelona.org/sources">https://bioteque.irbbarcelona.org/sources</a></td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>The provided node files are provided as TSVs, though assembly of a full KG would require running the graph assembly code. It appears that the assembly code also produces nodes and edges in a TSV format.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Node identifiers are from clearly defined sources and expressed as CURIEs</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Documentation regarding the assembly code is provided; see <a href="https://github.com/sbnb-irb/bioteque">https://github.com/sbnb-irb/bioteque</a></td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Each source has its own transform code and documentation, provided on the GitHub repo, <a href="https://github.com/sbnb-irb/bioteque">https://github.com/sbnb-irb/bioteque</a></td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>(the GitHub repository at <a href="https://github.com/sbnb-irb/bioteque">https://github.com/sbnb-irb/bioteque</a> is public and permits issue creation).</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>It&#x27;s never explicitly stated as a contact, but the responsible organization, the Structural Bioinformatics and Network Biology Group at the Institute for Research in Biomedicine Barcelona, is identified along with a link to their home page</td></tr>
<tr><td>Updated annually</td><td></td><td></td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/4</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Examples of use are described in the 2022 Nat Comm paper; an example of generating predictions for drug repurposing is provided.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Defined scope</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Multiple evaluation methods are provided in the 2022 Nat Comm paper, primarily for embedding evaluation.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Multiple validation methods are provided in the 2022 Nat Comm paper, including two distinct analyses involving gene expression data and protein-protein interactions, respectively.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC BY 4.0</td></tr>
</tbody></table></div>

