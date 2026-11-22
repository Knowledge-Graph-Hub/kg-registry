---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: zhan1386@umn.edu
    label: Rui Zhang
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ncats.nih.gov/translator
    label: NCATS Biomedical Data Translator
creation_date: '2025-10-30T00:00:00Z'
description: SuppKG is a literature-derived knowledge graph of dietary supplements and their relationships with diseases, drugs, genes, and other biomedical concepts. It was built at the University of Minnesota by running SemRepDS (SemRep extended with the iDISK dietary supplement terminology) over PubMed abstracts and filtering the resulting semantic predications with a PubMedBERT-based model; nodes are UMLS concepts. The original 2021 release has 56,635 nodes and 595,222 directed edges, and a v2 rebuild on newer abstracts has 57,944 nodes and 1,321,374 edges. It was used to discover drug-supplement interactions and is served in NCATS Translator through a BioThings API.
domains:
  - nutrition
  - biomedical
  - pharmacology
  - drug interactions
  - literature
  - natural language processing
funding:
  - National Center for Complementary and Integrative Health (NCCIH) (R01AT009457)
  - Office of Dietary Supplements (ODS)
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
id: suppkg
infores_id: suppkg
last_modified_date: '2026-11-22T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: umls.'
  id: https://uts.nlm.nih.gov/uts/
  inferred_from:
  - umls
  label: UMLS License (free for individuals)
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: SuppKG
publications:
  - preferred: true
    id: doi:10.1016/j.jbi.2022.104120
    doi: 10.1016/j.jbi.2022.104120
    title: Discovering novel drug-supplement interactions using SuppKG generated from the biomedical literature
    authors:
      - Dalton Schutte
      - Jake Vasilakes
      - Anu Bompelli
      - Yuqi Zhou
      - Marcelo Fiszman
      - Hua Xu
      - Halil Kilicoglu
      - Jeffrey R. Bishop
      - Terrence Adam
      - Rui Zhang
    journal: Journal of Biomedical Informatics
    year: '2022'
products:
  - category: DocumentationProduct
    description: Translator wiki page describing SuppKG scope and example supplement-disease relationships.
    format: http
    id: suppkg.docs
    name: SuppKG Documentation
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
  - category: ProcessProduct
    description: SuppKG directory in the SemRep_DS repository, holding the SuppKG graph files and a README describing their node and edge structure.
    format: http
    id: suppkg.source-data
    name: SuppKG Source Data Repository
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: idisk
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG
  - category: GraphProduct
    compression: other
    description: Original (2021) SuppKG as a bzip2-compressed NetworkX gpickle (NetworkX 2.5, Python 3.8, pickle protocol 5) with 56,635 UMLS concept nodes and 595,222 directed edges over 31 predicates; each edge carries the source sentences, PubMed IDs and PubMedBERT confidence scores.
    dump_format: gpickle
    format: mixed
    id: suppkg.graph.gpickle
    name: SuppKG NetworkX gpickle
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: idisk
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: semrep
        relation_type: prov:wasInfluencedBy
    product_file_size: 71635045
    product_url: https://raw.githubusercontent.com/zhang-informatics/SemRep_DS/main/SuppKG/supp_kg.gpickle.bz2
  - category: GraphProduct
    compression: other
    description: Original (2021) SuppKG as NetworkX node-link JSON in a bzip2-compressed tar archive, loadable with networkx.readwrite.json_graph.node_link_graph(); same content as the gpickle release.
    format: json
    id: suppkg.graph.json
    name: SuppKG Node-Link JSON
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: idisk
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: semrep
        relation_type: prov:wasInfluencedBy
    product_file_size: 68821417
    product_url: https://raw.githubusercontent.com/zhang-informatics/SemRep_DS/main/SuppKG/supp_kg.json.tar.bz2
  - category: GraphProduct
    compression: other
    description: SuppKG v2, rebuilt from additional PubMed abstracts published after the 2021 pull, as a NetworkX edge list in a bzip2-compressed tar archive (nx.read_edgelist gives a MultiDiGraph with 57,944 nodes and 1,321,374 edges). PubMed IDs, sentences and confidence scores are omitted in v2.
    format: txt
    id: suppkg.v2.edgelist
    name: SuppKG v2 Edge List
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: idisk
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: semrep
        relation_type: prov:wasInfluencedBy
    product_file_size: 57233095
    product_url: https://raw.githubusercontent.com/zhang-informatics/SemRep_DS/main/SuppKG/suppkg_v2.edgelist.tar.bz2
  - category: ProgrammingInterface
    description: BioThings API (infores:biothings-suppkg) serving the original 595,222 SuppKG subject-predicate-object records, including UMLS identifiers, semantic types, PubMed IDs, sentences and confidence scores; it backs the Service Provider TRAPI in NCATS Translator.
    format: http
    id: suppkg.biothings-api
    is_public: true
    name: BioThings SuppKG API
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: biothings
        relation_type: prov:wasInfluencedBy
    product_url: https://pending.biothings.io/suppkg/metadata
  - category: ProgrammingInterface
    description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
      querying the BioThings and other APIs registered to the team in SmartAPI.
    format: http
    id: service-kp.trapi
    is_public: true
    name: Service Provider TRAPI
    original_source:
    - relation_type: prov:hadPrimarySource
      source: service-kp
    - relation_type: prov:hadPrimarySource
      source: biothings
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: complexportal
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: litvar
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: ols
    - relation_type: prov:hadPrimarySource
      source: alliance
    - relation_type: prov:hadPrimarySource
      source: bindingdb
    - relation_type: prov:hadPrimarySource
      source: bioplanet
    - relation_type: prov:hadPrimarySource
      source: ddinter
    - relation_type: prov:hadPrimarySource
      source: dgidb
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: gene2phenotype
    - relation_type: prov:hadPrimarySource
      source: foodb
    - relation_type: prov:hadPrimarySource
      source: gtrx
    - relation_type: prov:hadPrimarySource
      source: hp
    - relation_type: prov:hadPrimarySource
      source: idisk
    - relation_type: prov:hadPrimarySource
      source: innatedb
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: pfocr
    - relation_type: prov:hadPrimarySource
      source: repodb
    - relation_type: prov:hadPrimarySource
      source: rhea
    - relation_type: prov:hadPrimarySource
      source: semmeddb
    - relation_type: prov:hadPrimarySource
      source: suppkg
    - relation_type: prov:hadPrimarySource
      source: ttd
    - relation_type: prov:hadPrimarySource
      source: uberon
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: clingen
    - relation_type: prov:hadPrimarySource
      source: cpdb
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: aeolus
    - relation_type: prov:hadPrimarySource
      source: chebi
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: mondo
    - relation_type: prov:hadPrimarySource
      source: civic
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: dbsnp
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:hadPrimarySource
      source: text-mining-kp
    - relation_type: prov:hadPrimarySource
      source: gdsc
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:wasInformedBy
      source: biothings-explorer
    - relation_type: prov:hadPrimarySource
      source: mygene
    - relation_type: prov:hadPrimarySource
      source: mychem
    - relation_type: prov:hadPrimarySource
      source: mydisease
    - relation_type: prov:hadPrimarySource
      source: fooddata-central
    - relation_type: prov:hadPrimarySource
      source: myvariant
    product_url: https://bte.transltr.io/v1/team/Service%20Provider
repository: https://github.com/zhang-informatics/SemRep_DS
synonyms:
  - SuppKG
  - Dietary Supplement Knowledge Graph
taxon:
  - NCBITaxon:9606
---

# SuppKG

## Overview

SuppKG is a knowledge graph of dietary supplements built from the biomedical
literature by the University of Minnesota Institute for Health Informatics. It
was generated by running SemRepDS (SemRep extended with the iDISK dietary
supplement terminology loaded into the UMLS) over about 600,000 PubMed
abstracts, then filtering the extracted semantic predications with a
PubMedBERT-based model. Nodes are UMLS concepts (CUIs) carrying their semantic
types and the terms found in the abstracts; edges use 31 SemRep predicates such
as TREATS, INTERACTS_WITH and METHOD_OF.

## Releases

- **SuppKG (2021)**: 56,635 nodes and 595,222 directed edges. Each edge keeps
  the supporting sentences, PubMed IDs and model confidence scores. Distributed
  as a NetworkX gpickle and as node-link JSON.
- **SuppKG v2**: rebuilt with the same pipeline on abstracts published since
  the 2021 pull, with 57,944 nodes and 1,321,374 edges. Distributed as a
  NetworkX edge list; PubMed IDs, sentences and confidence scores are omitted.

All files are in the
[SemRep_DS repository](https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG),
which declares no license.

## Use

The 2022 Journal of Biomedical Informatics paper used SuppKG with discovery
patterns to propose novel drug-supplement interactions. In the NCATS
Biomedical Data Translator, the 2021 release is served through the BioThings
SuppKG API (`infores:biothings-suppkg`), which the Service Provider TRAPI
queries.

## Automated Evaluation

- View the automated evaluation: [suppkg automated evaluation](suppkg_eval_automated.html)
