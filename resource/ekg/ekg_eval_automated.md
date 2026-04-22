---
evaluation_date: '2026-04-22'
evaluator: Automated evaluation (GPT-5.4)
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Raw epidemiological extractions are downloadable as CSV in addition to the graph serializations.</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Public SPARQL endpoint at https://api-vast.jrc.service.ec.europa.eu/sparql/ and faceted browser at https://api-vast.jrc.service.ec.europa.eu/fct/.</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>RDF/XML download, Turtle download, raw CSV download, SPARQL endpoint, and browser interface are all available.</td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7da;">N</td><td>The paper cites a GitHub repository for the extraction pipeline, but the cited repository was not publicly resolvable at evaluation time.</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>The complete graph is downloadable from the JRC catalogue in RDF/XML and Turtle.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>The paper clearly states that eKG is extracted from WHO Disease Outbreak News and enriched through BioPortal and GeoNames mappings.</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No explicit versioning or snapshot identifiers are given for the upstream WHO DON corpus or the external ontologies used in alignment.</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>The construction reuses IDO, BFO, OBO Foundry terms, BioPortal ontology links, and GeoNames identifiers.</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>The paper explains how outbreak entities come from DON reports and how diseases and locations are linked to external ontology and GeoNames resources.</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>The paper discusses minimizing duplication through ontology grounding, but it does not document a specific edge deduplication procedure.</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Provenance is described at the dataset and entity-linking level, not as explicit triple-level provenance metadata.</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Relations are described using RDF/OWL with reused ontology properties such as <code>skos:related</code> and OBO relations, and the paper documents the TBox/ABox structure.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>The graph is designed for epidemiological and public-health analysis over infectious disease outbreaks.</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>The graph uses resolvable JRC namespace IRIs and links out to BioPortal ontology entities and GeoNames identifiers.</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>The <em>Scientific Data</em> article provides a detailed methods section describing extraction, FAIR publishing, ontology alignment, and services.</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>The paper documents the ETL and LLM ensemble pipeline used to transform WHO DON reports into structured extractions and then into RDF/OWL.</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>eKG explicitly uses RDF, OWL, Linked Open Data principles, and ontology reuse from IDO/BFO/OBO with documented class mappings.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>The dataset has persistent URLs and a DOI-backed landing page, but no explicit versioned releases are exposed in the curated metadata.</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>No public issue tracker or repository tracker was accessible at evaluation time.</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>The JRC dataset page and article provide Sergio Consoli as a contact.</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>The paper describes the resource as daily-updated, and the JRC catalogue records a modified date of 2025-10-10.</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No archive of prior graph releases or historical snapshots was identified from the public landing page.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>The stated purpose is epidemiological research, outbreak surveillance, and structured querying over WHO DON reports.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>The paper compares the ensemble against multiple open-source LLMs and OpenAI GPT baselines for extraction tasks.</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>The resource scope is clearly defined as outbreak information extracted from WHO Disease Outbreak News and enriched for public-health knowledge representation.</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>The paper reports benchmark classification metrics on a gold-standard subset and also includes a qualitative comparison of reconstructed outbreak trends against WHO counts.</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>Precision, Recall, and F1 are reported across multiple extraction tasks, with the ensemble achieving the best F1 values in the presented tables.</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td style="background-color:#d4edda;">Y</td><td>The paper and JRC catalogue state that the produced data and ontology are available under CC BY 4.0.</td></tr>
</tbody></table></div>
