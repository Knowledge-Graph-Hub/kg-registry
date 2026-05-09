---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Karen Eilbeck
    orcid: 0000-0002-0831-6427
    contact_details:
      - contact_type: email
        value: keilbeck@genetics.utah.edu
      - contact_type: github
        value: keilbeck
creation_date: '2025-06-25T00:00:00Z'
description: A structured controlled vocabulary for sequence annotation, for the exchange of annotation data and for the description of sequence objects in databases.
domains:
  - chemistry and biochemistry
homepage_url: http://www.sequenceontology.org/
id: so
infores_id: so
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Sequence types and features ontology
products:
  - category: OntologyProduct
    description: Main SO OWL release
    format: owl
    id: so.owl
    name: Main SO OWL release
    product_file_size: 291621
    product_url: http://purl.obolibrary.org/obo/so.owl
    original_source:
      - source: so
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Main SO release in OBO Format
    format: obo
    id: so.obo
    name: Main SO release in OBO Format
    product_file_size: 193405
    product_url: http://purl.obolibrary.org/obo/so.obo
    original_source:
      - source: so
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: This subset includes only locatable sequence features and is designed for use in such outputs as GFF3
    format: owl
    id: so.subsets.SOFA.owl
    name: Sequence Ontology Feature Annotation (SOFA) subset (OWL)
    product_file_size: 43606
    product_url: http://purl.obolibrary.org/obo/so/subsets/SOFA.owl
    original_source:
      - source: so
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: This subset includes only locatable sequence features and is designed for use in such outputs as GFF3
    format: obo
    id: so.subsets.SOFA.obo
    name: Sequence Ontology Feature Annotation (SOFA) subset (OBO Format)
    product_file_size: 28447
    product_url: http://purl.obolibrary.org/obo/so/subsets/SOFA.obo
    original_source:
      - source: so
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: bioportal
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: genemania
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: OntologyProduct
    description: The latest release of EFO in OWL format
    format: owl
    id: efo.owl
    name: EFO OWL
    original_source:
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 240665663
    product_url: https://www.ebi.ac.uk/efo/efo.owl
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
  - category: OntologyProduct
    description: The latest release of EFO in OBO format
    format: obo
    id: efo.obo
    name: EFO OBO
    original_source:
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 64058275
    product_url: https://www.ebi.ac.uk/efo/efo.obo
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
repository: https://github.com/The-Sequence-Ontology/SO-Ontologies
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/15892872
    title: 'The Sequence Ontology: a tool for the unification of genome annotations.'
  - id: https://www.ncbi.nlm.nih.gov/pubmed/20226267
    title: Evolution of the Sequence Ontology terms and relationships.
---

## Description

A structured controlled vocabulary for sequence annotation, for the exchange of annotation data and for the description of sequence objects in databases.

## Contacts

- Karen Eilbeck (keilbeck@genetics.utah.edu) [ORCID: 0000-0002-0831-6427](https://orcid.org/0000-0002-0831-6427)

## Products

### Main SO OWL release

Main SO OWL release

**URL**: [http://purl.obolibrary.org/obo/so.owl](http://purl.obolibrary.org/obo/so.owl)

**Format**: owl

### Main SO release in OBO Format

Main SO release in OBO Format

**URL**: [http://purl.obolibrary.org/obo/so.obo](http://purl.obolibrary.org/obo/so.obo)

**Format**: obo

### Sequence Ontology Feature Annotation (SOFA) subset (OWL)

This subset includes only locatable sequence features and is designed for use in such outputs as GFF3

**URL**: [http://purl.obolibrary.org/obo/so/subsets/SOFA.owl](http://purl.obolibrary.org/obo/so/subsets/SOFA.owl)

**Format**: owl

### Sequence Ontology Feature Annotation (SOFA) subset (OBO Format)

This subset includes only locatable sequence features and is designed for use in such outputs as GFF3

**URL**: [http://purl.obolibrary.org/obo/so/subsets/SOFA.obo](http://purl.obolibrary.org/obo/so/subsets/SOFA.obo)

**Format**: obo

## Publications

- [The Sequence Ontology: a tool for the unification of genome annotations.](https://www.ncbi.nlm.nih.gov/pubmed/15892872)
- [Evolution of the Sequence Ontology terms and relationships.](https://www.ncbi.nlm.nih.gov/pubmed/20226267)

**Domains**: chemistry and biochemistry

---

*This resource was automatically synchronized from the OBO Foundry registry.*
