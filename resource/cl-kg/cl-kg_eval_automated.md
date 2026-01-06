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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Cell Ontology via OBO repository and CellXGene integration for single cell transcriptomics data from multiple studies</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>Neo4j instance accessible via browser interface at cellular-semantics.sanger.ac.uk but no documented REST or programmatic API</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#f8d7da;">N</td><td>Single access mechanism through Neo4j browser; no SPARQL endpoint, downloads, or alternative query interfaces documented</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Complete source code available at github.com/Cellular-Semantics/CL_KG with Apache 2.0 license enabling reproducibility</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>No bulk export format documented; Neo4j queries only method to extract data from KG instance</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Cell Ontology and CellXGene datasets clearly identified as primary sources for cell type and transcriptomics data</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>No documentation of specific Cell Ontology version or CellXGene data snapshot dates used in KG construction</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>GitHub repository shows integration pipeline and dependencies for ontology alignment and annotation</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Cell types traceable to Cell Ontology identifiers; transcriptomics associations sourced from CellXGene studies</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No documentation of deduplication strategy for redundant cell type assignments across studies</td></tr>
<tr><td>Triples source details</td><td style="background-color:#f8d7fa;">N</td><td>Neo4j property graph structure but no RDF schema or formal ontology mappings documented</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#f8d7da;">N</td><td>Relationship types between cells and ontology terms not formally mapped to standard ontologies</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Cell type hierarchies and transcriptomics annotations directly applicable to single cell analysis and cell biology research</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses stable Cell Ontology identifiers and CellXGene cell type standardized vocabulary resolvable externally</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#f8d7da;">N</td><td>ETL methodology not formally documented beyond source code; integration approach not transparent in publications</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>How CellXGene transcriptomics hierarchies map to Neo4j structure not documented</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>Neo4j graph schema not formally published; no RDF or OWL specification available for semantic integration</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>GitHub releases available with tagged stable versions enabling reproducibility</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub issues tracker active; Cellular Semantics project maintains the resource</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>Ugur Bayindir (ORCID 0000-0002-6012-3729) available for contact; active development team</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>Repository shows regular commits and updates reflecting CellXGene data additions</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Full Git history and release archives available for reproducibility</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Clear use case: cell type annotation and standardization for single cell transcriptomics studies</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No comparison with other cell type ontologies or cell annotation standards (e.g., LSAC, CellTypist)</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Focused scope on Cell Ontology integration with CellXGene transcriptomics data</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No systematic validation of cell type annotation accuracy against independent datasets</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#f8d7fa;">N</td><td>No reported precision/recall for cell type predictions or annotation completeness metrics</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 2/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td></td></tr>
</tbody></table></div>

