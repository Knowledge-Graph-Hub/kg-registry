---
id: hp
name: Human Phenotype Ontology (HPO)
description: The Human Phenotype Ontology (HPO) is a structured and controlled vocabulary
  for the phenotypic features encountered in human hereditary and other disease.
activity_status: active
homepage_url: http://www.human-phenotype-ontology.org/
repository: https://github.com/obophenotype/human-phenotype-ontology
license:
  id: https://hpo.jax.org/app/license
  label: hpo
collection:
- obo-foundry
layout: resource_detail
category: Ontology
domains:
- biological systems
taxon:
- NCBITaxon:9606
contacts:
- category: Individual
  label: Sebastian Koehler
  orcid: 0000-0002-5316-1399
  contact_details:
  - contact_type: email
    value: dr.sebastian.koehler@gmail.com
  - contact_type: github
    value: drseb
products:
- id: hp.json
  name: Official HPO release in obographs JSON format
  description: Simple, manually curated version of the ontology without the use of
    a reasoner, and without any imported terms, in obographs JSON format.
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp.json
- id: hp.obo
  name: Official HPO release in OBO format
  description: Simple, manually curated version of the ontology without the use of
    a reasoner, and without any imported terms, in OBO file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp.obo
- id: hp.owl
  name: Official HPO release in OWL
  description: Manually classified version of the ontology without the use of a reasoner,
    with imported terms, in OWL format (RDF/XML).
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp.owl
- id: hp.hp-base.json
  name: HPO base release in obographs JSON format
  description: Manually curated version of the ontology without the use of a reasoner,
    with references to imported terms, in obographs JSON file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-base.json
- id: hp.hp-base.obo
  name: HPO base release in OBO format
  description: Manually curated version of the ontology without the use of a reasoner,
    with references to imported terms, in OBO file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-base.obo
- id: hp.hp-base.owl
  name: HPO base release in OWL format
  description: Manually curated version of the ontology without the use of a reasoner,
    with references to imported terms, in OWL (RDF/XML) file format.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-base.owl
- id: hp.hp-full.json
  name: HPO full release in obographs JSON format
  description: Version of the ontology automatically classified with the use of a
    reasoner, including all imported terms, in obographs JSON file format.
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-full.json
- id: hp.hp-full.obo
  name: HPO full release in OBO format
  description: Version of the ontology automatically classified with the use of a
    reasoner, including all imported terms, in OBO file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-full.obo
- id: hp.hp-full.owl
  name: HPO full release in OWL format
  description: Version of the ontology automatically classified with the use of a
    reasoner, including all imported terms, in OWL (RDF/XML) file format.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-full.owl
- id: hp.hp-international.json
  name: HPO International Edition in obographs JSON format
  description: Version of the ontology corresponding to the primary release (hp.owl),
    with translated labels, synonyms, and definitions, in obographs JSON file format.
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-international.json
- id: hp.hp-international.obo
  name: HPO International Edition in OBO format
  description: Version of the ontology corresponding to the primary release (hp.owl),
    with translated labels, synonyms, and definitions, in OBO file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-international.obo
- id: hp.hp-international.owl
  name: HPO International Edition in OWL format
  description: Version of the ontology corresponding to the primary release (hp.owl),
    with translated labels, synonyms, and definitions, in OWL (RDF/XML) file format.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-international.owl
- id: hp.hp-simple-non-classified.json
  name: HPO simple, manually classified, without imports in obographs JSON format
  description: Simple, manually curated version of the ontology without the use of
    a reasoner, and without any imported terms, in obographs JSON file format.
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.json
- id: hp.hp-simple-non-classified.obo
  name: HPO simple, manually classified, without imports in OBO format
  description: Simple, manually curated version of the ontology without the use of
    a reasoner, and without any imported terms, in OBO file format.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.obo
- id: hp.hp-simple-non-classified.owl
  name: HPO simple, manually classified, without imports in OWL format
  description: Simple, manually curated version of the ontology without the use of
    a reasoner, and without any imported terms, in OWL (RDF/XML) file format.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.owl
- id: hp.phenotype.hpoa
  name: HPO Annotations (Phenotype to Disease)
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/phenotype.hpoa
- id: hp.phenotype_to_genes.txt
  name: HPO phenotype to gene annotations
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/phenotype_to_genes.txt
- id: hp.genes_to_phenotype.txt
  name: HPO gene to phenotype annotations
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/hp/genes_to_phenotype.txt
---

## Description

The Human Phenotype Ontology (HPO) is a structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease.

## Contacts

- Sebastian Koehler (dr.sebastian.koehler@gmail.com) [ORCID: 0000-0002-5316-1399](https://orcid.org/0000-0002-5316-1399)

## Products

### Official HPO release in obographs JSON format

Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in obographs JSON format.

**URL**: [http://purl.obolibrary.org/obo/hp.json](http://purl.obolibrary.org/obo/hp.json)

**Format**: json

### Official HPO release in OBO format

Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OBO file format.

**URL**: [http://purl.obolibrary.org/obo/hp.obo](http://purl.obolibrary.org/obo/hp.obo)

**Format**: obo

### Official HPO release in OWL

Manually classified version of the ontology without the use of a reasoner, with imported terms, in OWL format (RDF/XML).

**URL**: [http://purl.obolibrary.org/obo/hp.owl](http://purl.obolibrary.org/obo/hp.owl)

**Format**: owl

### HPO base release in obographs JSON format

Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in obographs JSON file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-base.json](http://purl.obolibrary.org/obo/hp/hp-base.json)

**Format**: obo

### HPO base release in OBO format

Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in OBO file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-base.obo](http://purl.obolibrary.org/obo/hp/hp-base.obo)

**Format**: obo

### HPO base release in OWL format

Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in OWL (RDF/XML) file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-base.owl](http://purl.obolibrary.org/obo/hp/hp-base.owl)

**Format**: owl

### HPO full release in obographs JSON format

Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in obographs JSON file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-full.json](http://purl.obolibrary.org/obo/hp/hp-full.json)

**Format**: json

### HPO full release in OBO format

Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in OBO file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-full.obo](http://purl.obolibrary.org/obo/hp/hp-full.obo)

**Format**: obo

### HPO full release in OWL format

Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in OWL (RDF/XML) file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-full.owl](http://purl.obolibrary.org/obo/hp/hp-full.owl)

**Format**: owl

### HPO International Edition in obographs JSON format

Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in obographs JSON file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-international.json](http://purl.obolibrary.org/obo/hp/hp-international.json)

**Format**: json

### HPO International Edition in OBO format

Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in OBO file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-international.obo](http://purl.obolibrary.org/obo/hp/hp-international.obo)

**Format**: obo

### HPO International Edition in OWL format

Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in OWL (RDF/XML) file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-international.owl](http://purl.obolibrary.org/obo/hp/hp-international.owl)

**Format**: owl

### HPO simple, manually classified, without imports in obographs JSON format

Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in obographs JSON file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.json](http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.json)

**Format**: json

### HPO simple, manually classified, without imports in OBO format

Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OBO file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.obo](http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.obo)

**Format**: obo

### HPO simple, manually classified, without imports in OWL format

Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OWL (RDF/XML) file format.

**URL**: [http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.owl](http://purl.obolibrary.org/obo/hp/hp-simple-non-classified.owl)

**Format**: owl

### HPO Annotations (Phenotype to Disease)

https://hpo.jax.org/app/data/annotations

**URL**: [http://purl.obolibrary.org/obo/hp/phenotype.hpoa](http://purl.obolibrary.org/obo/hp/phenotype.hpoa)

**Format**: tsv

### HPO phenotype to gene annotations

https://hpo.jax.org/app/data/annotations

**URL**: [http://purl.obolibrary.org/obo/hp/phenotype_to_genes.txt](http://purl.obolibrary.org/obo/hp/phenotype_to_genes.txt)

**Format**: tsv

### HPO gene to phenotype annotations

https://hpo.jax.org/app/data/annotations

**URL**: [http://purl.obolibrary.org/obo/hp/genes_to_phenotype.txt](http://purl.obolibrary.org/obo/hp/genes_to_phenotype.txt)

**Format**: tsv

## Publications

- [The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease.](https://www.ncbi.nlm.nih.gov/pubmed/18950739)
- [The Human Phenotype Ontology: Semantic Unification of Common and Rare Disease.](https://www.ncbi.nlm.nih.gov/pubmed/26119816)
- [The Human Phenotype Ontology project: linking molecular biology and disease through phenotype data.](https://www.ncbi.nlm.nih.gov/pubmed/24217912)
- [Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources.](https://www.ncbi.nlm.nih.gov/pubmed/30476213)

**Domains**: biological systems

**Taxon**: NCBITaxon:9606

---

*This resource was automatically synchronized from the OBO Foundry registry.*
