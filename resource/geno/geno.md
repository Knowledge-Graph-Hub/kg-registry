---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Matthew Brush
  orcid: 0000-0002-1048-5019
  contact_details:
  - contact_type: email
    value: mhb120@gmail.com
  - contact_type: github
    value: mbrush
creation_date: '2025-09-04T00:00:00Z'
description: An integrated ontology for representing the genetic variations described
  in genotypes, and their causal relationships to phenotype and diseases.
domains:
- genomics
- genetic variation
- biological systems
homepage_url: https://github.com/monarch-initiative/GENO-ontology/
id: geno
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Genotype Ontology
products:
- category: OntologyProduct
  description: GENO
  format: owl
  id: geno.owl
  name: GENO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geno
  product_file_size: 172287
  product_url: http://purl.obolibrary.org/obo/geno.owl
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gff
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: skos
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Genotype Ontology (GENO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains GENO_nodes.tsv and GENO_edges.tsv.
  edge_count: 1942
  format: kgx
  id: geno.kg-bioportal
  latest_version: '2026-02-02'
  name: GENO KGX graph (KG-Bioportal)
  node_count: 1352
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geno
  product_file_size: 69665
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/GENO.tar.gz
- category: ProgrammingInterface
  connection_url: https://pavs.phenomebrowser.net/sparql
  description: Public Virtuoso SPARQL endpoint for the PAVS knowledge graph, containing Saudi
    case records, gene annotations, HPO disease annotations, HPO information content values
    and literature phenopackets as RDF named graphs.
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
  description: PAVS web portal with phenotype-based semantic similarity search, gene and variant
    browsers, and an HPO hierarchy explorer over the knowledge graph.
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
  description: FastAPI REST API backing the PAVS portal, with OpenAPI documentation, for case
    search and SPARQL-backed queries.
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
  description: Combined GA4GH Phenopackets v2 JSON file of all PAVS cases, with HPO phenotypes,
    variants, genes, zygosity, pathogenicity and disease diagnoses.
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
publications: []
repository: https://github.com/monarch-initiative/GENO-ontology
---
## Description

An integrated ontology for representing the genetic variations described in genotypes, and their causal relationships to phenotype and diseases.

## Contacts

- Matthew Brush (mhb120@gmail.com) [ORCID: 0000-0002-1048-5019](https://orcid.org/0000-0002-1048-5019)

## Products

### GENO

GENO

**URL**: [http://purl.obolibrary.org/obo/geno.owl](http://purl.obolibrary.org/obo/geno.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*
