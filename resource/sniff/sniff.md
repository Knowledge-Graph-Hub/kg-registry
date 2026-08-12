---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    label: Matt Gehring
    orcid: 0009-0001-9531-2861
    contact_details:
      - contact_type: email
        value: matt@sniff.world
      - contact_type: url
        value: https://sniff.world/about/
creation_date: '2026-08-12T00:00:00Z'
description: An open canine genetics atlas covering breed-stratified variant data, canine disease associations, and dog-to-human gene orthology, published with an evidence-graded, Biolink-conformant knowledge graph.
domains:
  - genomics
  - organisms
  - biomedical
  - phenotype
homepage_url: https://sniff.world/
id: sniff
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Sniff
products:
  - category: GraphProduct
    description: A Biolink-conformant KGX TSV node file for the Sniff cross-species substrate, covering dog and human genes and canine and human diseases. Part of the facts-only federation bundle intended for ingest into other knowledge graphs.
    format: kgx
    id: sniff.federation-nodes
    name: Sniff KGX federation export, nodes
    node_categories:
      - biolink:Gene
      - biolink:Disease
    node_count: 36915
    compatibility:
      - standard: biolink
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ensembl
      - relation_type: prov:wasDerivedFrom
        source: mondo
    product_file_size: 3726803
    product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/sniff_nodes.tsv
  - category: GraphProduct
    description: A Biolink-conformant KGX TSV edge file for the Sniff cross-species substrate, covering dog-to-human orthology and canine disease associations. Every edge carries provenance and an evidence level, and all edges with a knowledge level of prediction are excluded.
    format: kgx
    id: sniff.federation-edges
    name: Sniff KGX federation export, edges
    edge_count: 19823
    predicates:
      - biolink:orthologous_to
      - biolink:causes
      - biolink:gene_associated_with_condition
      - biolink:associated_with_increased_likelihood_of
    compatibility:
      - standard: biolink
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ensembl
      - relation_type: prov:wasDerivedFrom
        source: mondo
    product_file_size: 5247253
    product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/sniff_edges.tsv
  - category: Product
    description: A JSON manifest for the Sniff KGX federation export, providing node and edge counts, per-predicate and per-evidence-tier breakdowns, build provenance, and SHA256 checksums for verification of the bundle.
    format: json
    id: sniff.federation-manifest
    name: Sniff KGX federation export manifest
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    product_file_size: 4365
    product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/manifest.json
  - category: Product
    description: A sites-only VCF of the Sniff Atlas variant catalogue, containing allele frequencies for 9,667,790 imputed variants across 14,478 dogs and 188 breeds on the CanFam4 assembly, restricted to variants with allele frequency at or above 1%.
    compression: gzip
    format: vcf
    id: sniff.atlas-vcf
    name: Sniff Atlas sites VCF (v1.0.1)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    latest_version: 1.0.1
    product_url: https://zenodo.org/records/20566358
  - category: GraphicalInterface
    description: The Sniff web interface, providing browsers for breeds, genes, diseases, variants, and contributing studies, an interactive atlas view, and a natural-language query view.
    format: http
    id: sniff.browser
    name: Sniff web interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    product_url: https://sniff.world/
  - category: ProgrammingInterface
    description: A Model Context Protocol server exposing Sniff data for programmatic and agent-based access.
    format: http
    id: sniff.mcp
    name: sniff-mcp
    license:
      id: https://opensource.org/licenses/MIT
      label: MIT
    original_source:
      - relation_type: prov:hadPrimarySource
        source: sniff
    product_url: https://github.com/Sniffscore/sniff-mcp
    repository: https://github.com/Sniffscore/sniff-mcp
publications:
  - id: https://doi.org/10.5281/zenodo.20566358
    doi: doi:10.5281/zenodo.20566358
    title: 'Sniff Atlas v1.0.1: an open, breed-stratified catalogue of common canine coding variants with calibrated protein-language-model pathogenicity and an evidence-graded knowledge graph'
    authors:
      - Matt Gehring
    journal: Zenodo
    year: '2026'
    preferred: true
repository: https://github.com/Sniffscore
taxon:
  - NCBITaxon:9615
  - NCBITaxon:9606
version: 1.0.1
---

Sniff is an open canine genetics resource that catalogues genetic variation across dog breeds and links canine conditions to their human disease counterparts. It is built and maintained by Matt Gehring at Candor Systems LLC as an independent, non-commercial project.

The v1.0.1 Atlas release provides allele frequencies for 9,667,790 imputed variants drawn from 14,478 dogs across 188 breeds on the CanFam4 assembly, restricted to variants at 1% allele frequency or above, with pathogenicity predictions from three complementary tools.

Layered on the variant catalogue is an evidence-graded knowledge graph, released separately as a Biolink-conformant KGX TSV bundle of 36,915 nodes and 19,823 edges. Nodes are genes and diseases; edges cover dog-to-human orthology, gene-disease causation, and canine disease associations established from OMIA. Orthology edges are stratified into high-corroborated, high, and moderate evidence tiers, and the export deliberately excludes any edge with a knowledge level of prediction, so that predictions never enter a downstream graph as facts.

Sniff aggregates and cross-links data from several upstream resources, including CanVAS, OMIA, Dog10K, Darwin's Ark, the Golden Retriever Lifetime Study, ClinVar, Ensembl, gnomAD, and Mondo. Contributing studies are individually credited on the Sniff site.
