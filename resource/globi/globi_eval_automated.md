---
evaluation_date: '2026-01-06'
evaluator: Automated Evaluation
layout: eval_detail
made_by_ai: true
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>GloBI Portal at globalbioticinteractions.org provides interactive search and browsing of species interaction records</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>REST-style API endpoints available for programmatic access to species interaction data in JSON/CSV formats</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Three documented access methods: web portal, REST API, and bulk dataset downloads (TSV/CSV)</td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7da;">N</td><td>No public source code repository identified; curation and pipeline implementation not openly available</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Bulk data exports available as TSV/CSV via Zenodo; complete integrated interaction datasets downloadable</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 4/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Integrates species interactions from many primary datasets; sources available through dataset listing at globalbioticinteractions.org/datasets</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No explicit versioning of upstream data sources documented; unclear when source datasets are synchronized</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#f8d7da;">N</td><td>Data integration pipeline not documented; unclear how datasets are harmonized and deduplicated</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#f8d7da;">N</td><td>Individual interaction records not linked to source publications or primary datasets; provenance not explicitly tracked</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No documentation of deduplication strategy for duplicate species interaction records across sources</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7da;">N</td><td>Interaction records stored as normalized TSV; RDF or semantic web representation not provided</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Well-defined relationship types for ecological interactions (predation, parasitism, pollination, mutualism, host-pathogen)</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Species interaction data directly applicable to ecology, biodiversity conservation, and food web research</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#f8d7da;">N</td><td>Taxonomic names normalized but not mapped to stable identifiers (NCBI Taxonomy, WoRMS); limited ID resolvability</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>No formal documentation of data curation pipeline, quality control, or integration methodology published</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>Name normalization and taxonomic reconciliation procedures not documented in technical documentation</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>TSV-based flat schema; no formal graph schema, ontology, or RDF representation documented</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#f8d7da;">N</td><td>Continuous data stream without formal versioning; Zenodo snapshots not tagged with release versions</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#f8d7da;">N</td><td>No public issue tracker or development roadmap visible; limited transparency into data updates and maintenance</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#f8d7da;">N</td><td>No explicit contact information or maintainer listed; support via globalbioticinteractions.org website unclear</td></tr>
<tr><td>Updated annually</td><td style="background-color:#f8d7da;">N</td><td>Last modification date indicates recent updates but no formal release schedule or versioning cadence documented</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>Historical snapshots not clearly versioned or archived; difficult to retrieve prior versions for reproducibility</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 0/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Clear use cases: ecological network analysis, species interaction discovery, biodiversity research support</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparison with other species interaction databases (BioTIME, Mangal, or similar); relative coverage not assessed</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused scope: species-to-species interactions with standardized relationship types across ecological domains</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No systematic validation framework; accuracy of interaction records and taxonomy not formally assessed</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7da;">N</td><td>No reported precision/recall for interaction prediction or taxonomy resolution; no false positive rate documented</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

