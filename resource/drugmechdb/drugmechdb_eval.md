---
evaluation_date: '2025-08-13'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Paths that describe the mechanism of action for drug/disease indication pair</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Website, can view all paths or only those related to a specific drug or disease</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Can download from zenodo or use website</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Https://github.com/SuLab/DrugMechDB</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Kind of on zenodo, but what they are calling a KG is a collection of entries for drug/disease pairs and the paths connecting them. Raw KG containing all edges between all entries does not appear to exist</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Table with node sources. Indications: DrugCentral ( according to GH, randomly sampled from availble drug-disease pairs, does not include all of them), paths: Mechanism of Action section from DrugBank, description section within Inxight Drugs, review articles, GeneOntology , UniProt, Reactome, and well-sources Wikipedia articles. No Primary experimental results are included. All are verified by curators</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>Date given for DrugCentral download, cannot find info for other sources</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>There are requirements.txt and .yaml files in the KG&#x27;s downloadable .zip file on Zenodo (<a href="https://zenodo.org/records/8139357)">https://zenodo.org/records/8139357)</a> showing the dependencies.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each entry consist of ‘graph’, ‘links’, ‘nodes’, and ‘reference’ keys. Graph contains the drug/disease pair, links contains relationships informative to the indication, nodes contains information about all entities in link, and reference contains all the sources for the entire relationship but not specifically for individual nodes/edges</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>Paths are manually curated</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Edges between informative nodes in a path do not contain orignal source infromation. Informative paths have citations for the entire path, not indivudal triples within them.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>BioLink, but does not specify exactly what sources are used for each edge type</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Json files</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>All nodes come from existing sources</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>Not really. Everything is &quot;manually curated&quot;</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>BioLink</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td></td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub Issues. Also includes a guide for how users can submit their own curated paths.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Indirectly. website indicated the lab who owns it, but does not provide a point of contact</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>V1 released in 2019 with one update less than a year later, same with V2 in 2023, no other updates</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>All versions availble, V2 has publication associated but detailed change logs for minor updates not available</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>They used an external KG to evaluate agreement between types of associations present in both graphs and calculate a p-value representing when the simulated percentage of matching was greater than or equal to the observed percentage</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Mechanisms of action by which a drug treats a disease</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td></td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Agreement with MechRepoNet</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC0 1.0 Universal</td></tr>
</tbody></table></div>

