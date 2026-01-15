---
evaluation_date: '2026-01-15'
evaluator: Automated Evaluation
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Zenodo v5 package includes inputs/processed data and ontology alongside KG (Zenodo 10.5281/zenodo.17079767).</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>SPARQL endpoint at https://qlever.earthmetabolome.org/api/metrin-kg and hosted query UI.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>SPARQL endpoint, web query editor, and RDF dump on Zenodo.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Code in GitHub repos earth-metabolome-initiative/metrin-kg and earth_metabolome_ontology.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>RDF dump provided via Zenodo (v1-v5 releases, e.g., 10.5281/zenodo.17079767).</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Zenodo description lists pf1600, Globi, TRY, structure metadata and ontology inputs.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Zenodo provides versioned releases (v1–v5) with DOI per version.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Build tutorial documents MySQL, Ontop, Pipenv and other required tools in repo README.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>KG construction docs map entities/edges from pf1600, Globi, TRY and structure metadata into EMI-based triples.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No explicit deduplication process described.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Per-triple provenance not documented.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Edge predicates defined by the EMI ontology used to generate the KG.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Metabolomics, taxonomy, traits, and interactions content (METRIN-KG dataset).</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses w3id.org/emi IRIs and external IDs from source datasets.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>README and tutorials describe KG generation workflow and configuration files.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Step-by-step instructions for mapping, Ontop materialization, and data loading.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>EMI ontology (w3id.org/emi) provides the schema for nodes and predicates.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Versioned Zenodo releases (v1–v5) with persistent DOIs.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Issues enabled on GitHub (earth-metabolome-initiative/metrin-kg, earth_metabolome_ontology).</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Contact via GitHub issues and project team listed on Zenodo.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Multiple releases throughout 2025 (v1–v5) and active development.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Zenodo retains all prior versions (v1–v4) alongside latest.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>KG targets metabolomics/traits/interactions for Earth Metabolome Initiative datasets.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparative evaluation reported.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Scope defined in README and Zenodo description (METRIN-KG for metabolites, traits, interactions).</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No multiple evaluation methodologies described.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No accuracy or quality metrics provided.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td style="background-color:#d4edda;">Y</td><td>CC0-1.0 (repo LICENSE and Zenodo record).</td></tr>
</tbody></table></div>

