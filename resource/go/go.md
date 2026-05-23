---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: suzia@stanford.edu
  - contact_type: github
    value: suzialeksander
  label: Suzi Aleksander
  orcid: 0000-0001-6787-2901
- category: Organization
  contact_details:
  - contact_type: url
    value: https://geneontology.org/
  id: gene-ontology-consortium
  label: Gene Ontology Consortium
creation_date: '2025-03-16T00:00:00Z'
description: The Gene Ontology (GO) provides a structured, species-independent ontology
  for describing molecular functions, biological processes, and cellular components,
  together with consortium-maintained annotation resources and causal activity models.
domains:
- biomedical
- biological systems
homepage_url: https://geneontology.org/
id: go
infores_id: go
last_modified_date: '2026-05-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Gene Ontology
products:
- category: OntologyProduct
  description: Core GO ontology in OWL format, excluding imports from external ontologies.
  format: owl
  id: go.owl
  name: GO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Core GO ontology in OBO format.
  format: obo
  id: go.obo
  name: GO OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: OntologyProduct
  description: Core GO ontology in OBO Graph JSON format.
  format: json
  id: go.json
  name: GO JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go.json
- category: OntologyProduct
  description: Fully axiomatised GO-Plus release in OWL format with imported external ontology content.
  format: owl
  id: go.extensions.go-plus.owl
  name: GO-Plus OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- category: OntologyProduct
  description: Fully axiomatised GO-Plus release in OBO Graph JSON format.
  format: json
  id: go.extensions.go-plus.json
  name: GO-Plus JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
- category: OntologyProduct
  description: GO base module in OWL format, retaining core ontology content without imported external ontologies.
  format: owl
  id: go.go-base.owl
  name: GO Base Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/go-base.owl
- category: OntologyProduct
  description: Acyclic GO release recommended for most annotation propagation workflows, in OBO format.
  format: obo
  id: go.go-basic.obo
  name: GO Basic OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- category: OntologyProduct
  description: Acyclic GO release recommended for most annotation propagation workflows, in JSON format.
  format: json
  id: go.go-basic.json
  name: GO Basic JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
- category: OntologyProduct
  description: Taxon grouping classes used by GO for high-level biological groupings.
  format: owl
  id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
- category: OntologyProduct
  description: Daily snapshot of the GO ontology in OWL format.
  format: owl
  id: go.snapshot.go.owl
  name: GO Snapshot OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- category: OntologyProduct
  description: Daily snapshot of the GO ontology in OBO format.
  format: obo
  id: go.snapshot.go.obo
  name: GO Snapshot OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
- category: GraphicalInterface
  description: Official GO browser for ontology terms, gene products, and annotations.
  format: http
  id: go.amigo
  is_public: true
  name: AmiGO 2
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://amigo.geneontology.org/amigo
- category: ProgrammingInterface
  description: Official Gene Ontology API for term, annotation, and related programmatic access.
  format: http
  id: go.api
  is_public: true
  name: Gene Ontology API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://api.geneontology.org/
- category: GraphicalInterface
  description: Browser for GO annotations and ontology terms via the GOA/QuickGO service.
  format: http
  id: goa.quickgo
  name: QuickGO Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://www.ebi.ac.uk/QuickGO/
- category: Product
  description: GO annotation download directory containing current and archived GOA files.
  format: http
  id: goa.ftp
  name: GOA Download Directory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/
- category: Product
  description: UniProtKB GO annotation files distributed through the GOA download site.
  format: txt
  id: goa.uniprot
  name: UniProt GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
- category: Product
  description: Human GO annotation files distributed through the GOA download site.
  format: txt
  id: goa.human
  name: Human GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
- category: Product
  description: Mouse GO annotation files distributed through the GOA download site.
  format: txt
  id: goa.mouse
  name: Mouse GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
- category: MappingProduct
  description: GO mapping files connecting external classification systems and annotation resources to GO terms.
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
- category: Product
  description: PDB GO annotation files distributed through the GOA download site.
  format: txt
  id: goa.pdb
  name: PDB GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
- category: Product
  description: Proteome-organized GO annotation files distributed through the GOA download site.
  format: txt
  id: goa.proteomes
  name: Proteomes GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/
- category: GraphProduct
  compression: gzip
  description: Pathway-like GO-CAM causal activity models distributed as RDF Turtle.
  format: ttl
  id: go.gocams.ttl
  name: GO-CAM TTL Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://current.geneontology.org/products/ttl/pathway-like_go-cams.tar.gz
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/10802651
  title: 'Gene ontology: tool for the unification of biology. The Gene Ontology Consortium'
- id: https://www.ncbi.nlm.nih.gov/pubmed/33290552
  title: 'The Gene Ontology resource: enriching a GOld mine'
repository: https://github.com/geneontology/go-ontology
synonyms:
- GO
taxon:
- NCBITaxon:1
---
## Overview

The Gene Ontology (GO) is a consortium-maintained ontology and knowledge resource for describing gene product function across species. It organizes biology into molecular function, biological process, and cellular component terms, and supports a large ecosystem of annotation, browsing, download, and programmatic access services.

## Scope

This page focuses on official GO products: ontology releases, GO Consortium browsers and APIs, GO annotation download surfaces, and GO-CAM causal activity model distributions. It does not enumerate downstream third-party knowledge graphs that merely ingest GO.

## Access

Use AmiGO and QuickGO for browsing, the GO API for programmatic access, OBO PURLs for ontology files, and the GOA / current release download directories for annotation and GO-CAM artifacts.

---

*This resource was automatically synchronized from the OBO Foundry registry and then curated with additional GO Consortium access points.*
