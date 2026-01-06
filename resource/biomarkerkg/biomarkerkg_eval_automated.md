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
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>BKG provides a web interface (BKG Explorer) for querying and exploring biomarker-anatomy, biomarker-compound, biomarker-condition, biomarker-role, and biomarker-variant relationships</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#f8d7da;">N</td><td>The BKG web interface does not provide direct API access based on available documentation</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Multiple downloadable data formats available including CSV files organized by node and edge types from S3 bucket</td></tr>
<tr><td>Source code availability</td><td style="background-color:#f8d7da;">N</td><td>No public source code repository mentioned for KG construction</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Individual CSV files for nodes (Anatomy, Biomarker, Compound, Condition, Role, Variant) and edges are available for download</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Integrates data from well-known sources: GlyGen Biomarker Database, Uber-Anatomy Ontology (Uberon), PubChem, Human Disease Ontology (DOID), and dbSNP</td></tr>
<tr><td>Source versions information</td><td style="background-color:#f8d7da;">N</td><td>Specific version information for source databases is not provided in the available documentation</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Declares explicit relationships (node edge types): determined_using_sample_from (Anatomy), indicated_by_above/below_normal_level_of (Compound), diagnostic_for/indicates_risk_of/prognostic_for (Condition), has_best_classification (Role)</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Each product file is described with a specific relationship type (e.g., Biomarker to Anatomy relationships, Biomarker to Condition relationships)</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#f8d7da;">N</td><td>No explicit documentation of deduplication mechanisms at the edges level</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Relationship types are clearly defined with meaningful semantic labels (diagnostic_for, prognostic_for, indicates_risk_of_developing, etc.)</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Uses Uberon anatomy, DOID disease ontology, dbSNP variant IDs, and PubChem compound identifiers which are resolvable</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#f8d7da;">N</td><td>Detailed construction documentation is not publicly available</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#f8d7da;">N</td><td>Data transformation steps and filtering procedures are not documented in available resources</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Clear edge type schema with defined semantic relationships between biomarkers and other entity types</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#f8d7da;">N</td><td>No formal versioning scheme mentioned (no v1.0, v2.0, etc.)</td></tr>
<tr><td>Schema used</td><td style="background-color:#f8d7da;">N</td><td>No public issue tracker or GitHub repository visible for tracking feature requests or bugs</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Contact information provided: avi.maayan@mssm.edu (MaayanLab)</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>Partially - KG is actively maintained but no formal update frequency documented (appears to be an active development project)</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#f8d7da;">N</td><td>No archived prior versions or changelog available</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>BKG is designed for biomarker discovery and exploration, relevant for clinical diagnostics and precision medicine applications</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#f8d7da;">N</td><td>No comparisons with other biomarker knowledge bases mentioned in available documentation</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 3/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>Focused scope on biomarker relationships across anatomical structures, compounds, conditions, roles, and genetic variants</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#f8d7da;">N</td><td>No quantitative evaluation metrics or benchmarks provided in available documentation</td></tr>
<tr><td>Defined scope</td><td style="background-color:#f8d7da;">N</td><td>Accuracy, precision, recall, or other quality metrics are not reported</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#f8d7da;">N</td><td>No explicit evaluation methods comparison provided in documentation</td></tr>
<tr><td>Accuracy metrics</td><td></td><td></td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 1/4</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>CC-BY-4.0 (inferred from MaayanLab standard practice; not explicitly stated in resource metadata)</td></tr>
</tbody></table></div>

