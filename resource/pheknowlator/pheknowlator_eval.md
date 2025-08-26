---
evaluation_date: '2025-08-26'
evaluator: Not specified
layout: eval_detail
---

## Access Level and Types
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Access to data outside of the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>Prebuilt node embeddings (created using DeepWalk variants, v1.0.0); Jupyter notebooks for entity/path search and RDF querying; OWL-NETS abstractions for analysis. Future plans also mention providing more embeddings using GRAPE</td></tr>
<tr><td>API or online access to the knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>(API/SPARQL). Hosted SPARQL endpoint (Blazegraph) with proxy UI and deployment code. Neo4j hosting not mentioned</td></tr>
<tr><td>Multiple access options available</td><td style="background-color:#d4edda;">Y</td><td>Zenodo community archives, GitHub releases, PyPI package, Docker images, SPARQL endpoint, plus logs/metadata</td></tr>
<tr><td>Source code availability</td><td style="background-color:#d4edda;">Y</td><td>Full repo on GitHub and installable via PyPI; notebooks for OWL-NETS, RDF queries, and entity search</td></tr>
<tr><td>Downloadable knowledge graph</td><td style="background-color:#d4edda;">Y</td><td>11 monthly builds (2019–2021), each with 12 KG types (class/instance × standard/inverse × OWL vs. OWL-NETS ± harmonization), provided in standard formats</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Provenance of Nodes and Edges
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Source list provided</td><td style="background-color:#d4edda;">Y</td><td>Comprehensive source lists (Supp. Table 12) + edge_source_metadata.txt, ontology_source_metadata.txt, downloaded_build_metadata.txt</td></tr>
<tr><td>Source versions information</td><td style="background-color:#d4edda;">Y</td><td>Metadata capture provider, filenames, URLs, licenses, download dates; per-build logs and version tags</td></tr>
<tr><td>Import dependencies</td><td style="background-color:#d4edda;">Y</td><td>Methods detail OWLTools, ROBOT (noted as future improvement), Blazegraph, DBCLS SPARQL proxy, Docker, NetworkX, Gephi/OpenOrd, GitHub Actions/Google Cloud specs, etc. The wiki/docs enumerate inputs and environment</td></tr>
<tr><td>Node and edge sources</td><td style="background-color:#d4edda;">Y</td><td>Largely yes - build metadata record which sources contribute which node/edge types; evidence such as PubMed IDs added for some relationships (e.g., CTD). Fine-grained per-triple provenance is not universal</td></tr>
<tr><td>Edges deduplication</td><td style="background-color:#d4edda;">Y</td><td>Partial - Explicit handling of inverse/symmetric relations; self-loops reported. No standalone deduplication policy document - supports inverse/bidirectional relation strategy and treats implicitly symmetric interaction edges</td></tr>
<tr><td>Triples source details</td><td style="background-color:#d4edda;">Y</td><td>Figure 8 walk-through (e.g., ClinVar → variant–disease); Table 5 counts edges by relation/source rules</td></tr>
<tr><td>Edge type schema</td><td style="background-color:#d4edda;">Y</td><td>Predicates from Relation Ontology (RO); OWL-NETS converts OWL to hybrid triples; harmonization rules (rdf:type ↔ rdfs:subClassOf) per knowledge model</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 7/7</p>

## Documented standards, schema, construction
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Biological usable data</td><td style="background-color:#d4edda;">Y</td><td>Outputs in RDF/XML, N-Triples, and JSON/TSV with resolvable IRIs; queryable via SPARQL; broadly compatible with standard bio/semantic-web tooling and pipelines</td></tr>
<tr><td>Resolvable IDs</td><td style="background-color:#d4edda;">Y</td><td>Uses HGNC, Entrez, Ensembl, PRO, ChEBI, Uberon, HPO, MONDO, etc.; explicit ID mapping during preparation</td></tr>
<tr><td>Construction documentation</td><td style="background-color:#d4edda;">Y</td><td>Strong yes - Detailed wiki, notebooks, per-build pages, logs, and metadata; SPARQL deployment docs</td></tr>
<tr><td>Transformation documentation</td><td style="background-color:#d4edda;">Y</td><td>Ontology cleaning with reports; data preparation steps (replace NaN, unnest, reformat IDs); filtering/mapping dictionaries logged</td></tr>
<tr><td>Schema used</td><td style="background-color:#d4edda;">Y</td><td>Semantic-web first: OBO Foundry grounding, RO relations, OWL complex graphs, OWL-NETS abstraction. (Biolink/Bioregistry noted as future integration.)</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Update frequency and versioning
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Stable versions</td><td style="background-color:#d4edda;">Y</td><td>Semantic Versioning used for code/docs; builds labeled (e.g., v2.1.0); artifacts versioned on GitHub/Zenodo/Docker</td></tr>
<tr><td>Public tracker information</td><td style="background-color:#d4edda;">Y</td><td>GitHub Issues; community bug reports acknowledged</td></tr>
<tr><td>Knowledge graph contact information</td><td style="background-color:#d4edda;">Y</td><td>GitHub repo mentions contact as Tiffany Callahan (first author)</td></tr>
<tr><td>Updated annually</td><td style="background-color:#d4edda;">Y</td><td>The paper states, &quot;Eleven monthly PKT Human Disease benchmark KG builds were created between September 2, 2019 and November 1, 2021.&quot; This confirms that the KG is updated monthly, which is more than once per year</td></tr>
<tr><td>Prior versions access</td><td style="background-color:#d4edda;">Y</td><td>Zenodo community archive + GitHub releases/wiki per build; file manifests and changes described</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## Evaluation - Metrics and Fitness for Purpose
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>Use case provided</td><td style="background-color:#d4edda;">Y</td><td>There is a dedicatd section in the paper. Applications include toxicogenomic inference, depression→AD causal features, MGMLink, RNA-KG, HuBMAP/SenNet ingestion, pathway “cartooning,” etc.</td></tr>
<tr><td>Evaluation against other models</td><td style="background-color:#d4edda;">Y</td><td>Qualitative) - Survey vs 14 open-source builders; feature coverage and maturity compared (no head-to-head same-data build</td></tr>
<tr><td>Defined scope</td><td style="background-color:#d4edda;">Y</td><td>Human disease mechanisms spanning central dogma, pathways, variants, treatments across multiple biological scales</td></tr>
<tr><td>Multiple evaluation methods</td><td style="background-color:#d4edda;">Y</td><td>Tool survey, computational performance (runtime/memory), structural stats (nodes/edges/density/self-loops), visualizations, embeddings/tasks, and qualitative comparison in a systematic manner</td></tr>
<tr><td>Accuracy metrics</td><td style="background-color:#d4edda;">Y</td><td>No universal per-triple confidence score; but includes evidence IDs for some relations, reasoner-based logical consistency, and encourages task-level evaluation using benchmarks/embeddings</td></tr>
</tbody></table></div>
<p><strong>Section Score:</strong> 5/5</p>

## License Information
<div class="table-responsive">
<table class="table table-striped">
<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>
<tr><td>License</td><td></td><td>Apache 2.0 License</td></tr>
</tbody></table></div>

