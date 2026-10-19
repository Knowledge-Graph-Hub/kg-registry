---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: larsjuhljensen
  - contact_type: url
    value: https://jensenlab.org/
  label: Lars Juhl Jensen
creation_date: '2026-10-19T00:00:00Z'
description: Tagger is the JensenLab dictionary-based named entity recognition (NER)
  engine, a fast C++ program with a Python interface that finds mentions of genes/proteins,
  chemicals, species, diseases, tissues, subcellular compartments, environments, phenotypes,
  and Gene Ontology terms in text and normalizes them to database identifiers. It
  is available as open-source software, as a public web service (tagger.jensenlab.org),
  and with precompiled dictionaries, and it produces the weekly text-mining results
  used by STRING, DISEASES, TISSUES, COMPARTMENTS, and ORGANISMS.
domains:
- literature
- natural language processing
- information technology
- software
- genomics
homepage_url: https://jensenlab.org/resources/textmining/
id: tagger
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-2-Clause
  label: BSD 2-Clause License
name: Tagger
products:
- category: ProcessProduct
  description: Source code for the tagger/tagcorpus C++ named entity recognition software
    (with Python bindings via SWIG), including documentation of the dictionary input
    files and entity type codes.
  id: tagger.repository
  license:
    id: https://opensource.org/licenses/BSD-2-Clause
    label: BSD 2-Clause License
  name: Tagger Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tagger
  product_url: https://github.com/larsjuhljensen/tagger
- category: ProgrammingInterface
  description: Public Tagger web service. Endpoints such as GetEntities and GetHTML
    accept a document and a list of entity types (NCBI Taxonomy IDs for proteins of
    a species, or negative type codes such as -1 for chemicals, -22 for GO cellular
    components, -25 for BTO tissues, -26 for diseases) and return the recognized entities
    with their normalized identifiers as TSV, XML, or annotated HTML. The service uses
    the reduced tagger dictionary. The bare host returns HTTP 400; queries must include
    an endpoint and parameters.
  format: http
  id: tagger.api
  name: Tagger Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tagger
  product_url: https://tagger.jensenlab.org/GetEntities?document=TP53&entity_types=9606&format=tsv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: tagger.dictionary
- category: Product
  compression: targz
  description: Reduced tagger dictionary used by the Tagger web service, as tab-separated
    entities, names, groups, global, preferred-name, and text files. Gene/protein names
    come from the STRING alias file, chemical names from STITCH (PubChem compound
    identifiers), and other names from NCBI Taxonomy, Gene Ontology, BRENDA Tissue
    Ontology, Disease Ontology, Environment Ontology, and the Mammalian Phenotype Ontology.
  format: tsv
  id: tagger.dictionary
  name: Tagger Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tagger
  product_file_size: 388733075
  product_url: https://download.jensenlab.org/tagger_dictionary.tar.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: stitch
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: bto
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: envo
  - relation_type: prov:wasDerivedFrom
    source: mp
- category: Product
  compression: targz
  description: Combined full dictionary (entities and names TSV files) used for the
    weekly text mining of the biomedical literature behind the JensenLab databases
    (STRING, DISEASES, TISSUES, COMPARTMENTS, ORGANISMS). Built from the STRING alias
    file, STITCH chemicals, and taxonomy and ontology resources.
  format: tsv
  id: tagger.full-dictionary
  name: Tagger Full Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tagger
  product_file_size: 3799651519
  product_url: https://download.jensenlab.org/full_dictionary.tar.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: stitch
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: bto
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: envo
  - relation_type: prov:wasDerivedFrom
    source: mp
- category: DocumentationProduct
  description: JensenLab text-mining resources page describing the Tagger software,
    the topic-specific dictionaries (organisms, compartments, tissues, diseases, phenotypes,
    environments, and per-species gene/protein dictionaries), annotated corpora, and
    related tools.
  format: http
  id: tagger.docs
  name: JensenLab Text-mining Resources
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tagger
  product_url: https://jensenlab.org/resources/textmining/
publications:
- authors:
  - Jensen LJ
  doi: 10.1101/067132
  id: doi:10.1101/067132
  journal: bioRxiv
  preferred: true
  title: 'One tagger, many uses: Illustrating the power of ontologies in dictionary-based
    named entity recognition'
  year: '2016'
- authors:
  - Pafilis E
  - Frankild SP
  - Fanini L
  - Faulwetter S
  - Pavloudi C
  - Vasileiadou A
  - Arvanitidis C
  - Jensen LJ
  doi: 10.1371/journal.pone.0065390
  id: PMID:23823062
  journal: PLoS One
  title: The SPECIES and ORGANISMS Resources for Fast and Accurate Identification of
    Taxonomic Names in Text.
  year: '2013'
repository: https://github.com/larsjuhljensen/tagger
synonyms:
- JensenLab Tagger
- tagcorpus
---
# Tagger

## Overview

Tagger is the dictionary-based named entity recognition (NER) engine developed in the group of Lars Juhl Jensen (Novo Nordisk Foundation Center for Protein Research, University of Copenhagen). It is written in C++ with a Python interface and produces the weekly-updated text-mining results of the JensenLab databases. Tagger expands orthographic variants (case, dashes before terminal numbers), supports curated stopword lists and entity groups (for example, orthologous proteins treated as one entity), and normalizes each match to a database identifier.

## Data Content

Tagger itself is software. Its outputs depend on the dictionaries it is run with. JensenLab distributes:

- A **full dictionary**, used for the weekly text mining behind STRING, DISEASES, TISSUES, COMPARTMENTS, and ORGANISMS.
- A **reduced tagger dictionary**, used by the public web service.
- Topic-specific dictionaries for organisms, compartments, tissues, diseases, phenotypes, environments, and gene/protein dictionaries for human and selected model organisms.

Gene/protein names come from the STRING alias file and chemical names from STITCH. Other entity types are built from NCBI Taxonomy, the Gene Ontology, the BRENDA Tissue Ontology, the Disease Ontology, the Environment Ontology, and phenotype ontologies. Entity types are encoded as integers: a positive NCBI Taxonomy ID means proteins of that species, and negative codes cover chemicals (-1), species (-2), GO processes, components, and functions (-21 to -23), tissues (-25), diseases (-26), environments (-27), and phenotypes.

## Access

- Source code: [github.com/larsjuhljensen/tagger](https://github.com/larsjuhljensen/tagger)
- Web service: `https://tagger.jensenlab.org/GetEntities?document=...&entity_types=...&format=tsv` (also `GetHTML` and XML output)
- Dictionaries: [download.jensenlab.org](https://download.jensenlab.org/)
- Documentation: [JensenLab text-mining resources](https://jensenlab.org/resources/textmining/)

Tagger is also used inside the EXTRACT and Reflect browser annotation tools.

## License

The Tagger source code is released under the BSD 2-Clause License. The JensenLab website content is published under CC BY 4.0.
