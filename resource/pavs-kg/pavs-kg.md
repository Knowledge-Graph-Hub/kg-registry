---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: robert.hoehndorf@kaust.edu.sa
  - contact_type: github
    value: leechuck
  label: Robert Hoehndorf
  orcid: 0000-0001-8149-5890
creation_date: '2026-10-05T00:00:00Z'
description: RDF knowledge graph from the Bio-Ontology Research Group at KAUST that
  represents PAVS (Phenotype-Associated Variants in Saudi Arabia), a curated database
  of clinical cases from Saudi Arabian rare disease cohorts. Each case links HPO-encoded
  phenotypes to genomic variants, genes, zygosity, pathogenicity classifications and
  MONDO/OMIM diagnoses, with annotations from ClinVar, ClinGen, gnomAD, Ensembl VEP,
  GO, GTEx and MGI. The graph also includes DDD study cases and literature phenopackets
  as comparators, and is served from a public Virtuoso SPARQL endpoint.
domains:
- biomedical
- rare disease
- genetic variation
- genomics
- phenotype
- clinical
homepage_url: https://pavs.phenomebrowser.net/
id: pavs-kg
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: PAVS Knowledge Graph
products:
- category: ProgrammingInterface
  connection_url: https://pavs.phenomebrowser.net/sparql
  description: Public Virtuoso SPARQL endpoint for the PAVS knowledge graph, containing
    Saudi case records, gene annotations, HPO disease annotations, HPO information
    content values and literature phenopackets as RDF named graphs.
  format: http
  id: pavs-kg.sparql
  is_public: true
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/sparql
- category: GraphicalInterface
  description: PAVS web portal with phenotype-based semantic similarity search, gene
    and variant browsers, and an HPO hierarchy explorer over the knowledge graph.
  format: http
  id: pavs-kg.portal
  name: PAVS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/
- category: ProgrammingInterface
  description: FastAPI REST API backing the PAVS portal, with OpenAPI documentation,
    for case search and SPARQL-backed queries.
  format: http
  id: pavs-kg.api
  name: PAVS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/api/docs
- category: Product
  description: Combined GA4GH Phenopackets v2 JSON file of all PAVS cases, with HPO
    phenotypes, variants, genes, zygosity, pathogenicity and disease diagnoses.
  format: json
  id: pavs-kg.phenopackets
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS Phenopackets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  product_url: https://raw.githubusercontent.com/bio-ontology-research-group/pavs-knowledge-graph/master/data/PAVS_phenopackets.json
- category: ProcessProduct
  description: Pipeline code that normalizes source cohort tables to HPO, MONDO, OMIM
    and HGVS, annotates variants and genes, generates Phenopackets, and produces the
    Turtle files loaded into Virtuoso.
  format: python
  id: pavs-kg.code
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: PAVS Knowledge Graph Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  product_url: https://github.com/bio-ontology-research-group/pavs-knowledge-graph
publications:
- authors:
  - Marwa Abdelhakim
  - Azza Althagafi
  - Paul N. Schofield
  - Robert Hoehndorf
  doi: 10.64898/2026.04.05.26350189
  id: doi:10.64898/2026.04.05.26350189
  journal: medRxiv
  preferred: true
  title: 'PAVS: A Standardized Database of Phenotype-Associated Variants from Saudi
    Arabian Rare Disease Patients'
  year: '2026'
repository: https://github.com/bio-ontology-research-group/pavs-knowledge-graph
synonyms:
- PAVS
- Phenotype-Associated Variants in Saudi Arabia
- PAVS KG
---
# PAVS Knowledge Graph

PAVS (Phenotype-Associated Variants in Saudi Arabia) is a curated database of genotype-phenotype data from Saudi Arabian rare disease patients, built by the Bio-Ontology Research Group at King Abdullah University of Science and Technology (KAUST). It combines 5,132 Saudi clinical cases from four Saudi cohorts and 522 cases from a mixed-population cohort, plus 1,856 cases from the Deciphering Developmental Disorders (DDD) study and 9,588 literature phenopackets from Phenopacket Store for comparison.

The pipeline normalizes phenotypes to the Human Phenotype Ontology, diseases to MONDO and OMIM, genotypes to GENO and variants to HGVS. It then annotates variants with Ensembl VEP, ClinVar, ClinGen, gnomAD and Saudi population allele frequencies, and annotates genes with gnomAD constraint metrics, GO annotations, GTEx expression and MGI mouse phenotypes. Cases are exported as GA4GH Phenopackets v2 and as RDF (Turtle), which is loaded into a Virtuoso triple store behind the PAVS web portal and SPARQL endpoint. Saudi cases are tagged with HANCESTRO and GAZ terms.

Pipeline code is GPL-3.0. Curated data, normalization and annotation are CC BY 4.0.
