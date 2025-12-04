---
activity_status: inactive
category: DataSource
creation_date: '2025-12-03T00:00:00Z'
description: PharmacotherapyDB is a curated catalog of medical indications between small molecule compounds and complex human diseases. It was created as part of a network-based drug repurposing project and differentiates between disease-modifying (DM) and symptomatic (SYM) treatments, with each indication reviewed by multiple physicians. The initial release contains 97 diseases and 601 drugs, with 755 disease-modifying therapies, 390 symptomatic therapies, and 243 non-indications. The catalog uses standardized vocabularies (Disease Ontology and DrugBank) to facilitate data integration and adheres to pathophysiological principles.
domains:
  - drug discovery
  - pharmacology
  - biomedical
homepage_url: https://github.com/dhimmel/indications
id: "pharmacotherapydb"
infores_id: "pharmacotherapydb"
last_modified_date: '2025-12-03T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/publicdomain/zero/1.0/"
  label: CC0-1.0
name: PharmacotherapyDB
publications:
  - id: "doi:10.7554/eLife.26726"
    title: 'Systematic integration of biomedical knowledge prioritizes drugs for repurposing'
    journal: eLife
    year: "2017"
    doi: "10.7554/eLife.26726"
    preferred: true
products:
  - category: GraphicalInterface
    description: A browser interface for a knowledge graph for Alzheimer's Disease.
    format: http
    id: "alzkb.browser"
    name: AlzKB Graph Database Browser
    original_source:
      - aop-db
      - bgee
      - disgenet
      - doid
      - drugbank
      - dsstox
      - go
      - gwascatalog
      - hrpimp
      - lincs-l1000
      - mesh
      - ncbigene
      - pharmacotherapydb
      - pid
      - pubchem
      - reactome
      - sider
      - tissues
      - uberon
      - wikipathways
    product_url: https://alzkb.ai:7473/login
    secondary_source:
      - alzkb
      - hetionet
  - category: GraphProduct
    description: Memgraph data release for AlzKB.
    id: "alzkb.data"
    name: AlzKB Data Release (Version 2.0.0)
    original_source:
      - aop-db
      - bgee
      - disgenet
      - doid
      - drugbank
      - dsstox
      - go
      - gwascatalog
      - hrpimp
      - lincs-l1000
      - mesh
      - ncbigene
      - pharmacotherapydb
      - pid
      - pubchem
      - reactome
      - reactome
      - sider
      - tissues
      - uberon
      - wikipathways
    product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
    secondary_source:
      - alzkb
      - hetionet
---

# PharmacotherapyDB

PharmacotherapyDB is a curated catalog of medical indications between small molecule compounds and complex human diseases. Created as part of a network-based drug repurposing project, it differentiates between disease-modifying (DM) and symptomatic (SYM) treatments, with each indication reviewed by multiple physicians. The initial release contains 97 diseases, 601 drugs, 755 disease-modifying therapies, 390 symptomatic therapies, and 243 non-indications. The catalog uses standardized vocabularies (Disease Ontology and DrugBank) to facilitate data integration and is designed as a gold standard for computational drug repurposing approaches.
