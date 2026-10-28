---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-10-19T00:00:00Z'
description: Drugmonizome is a database and search engine from the Ma'ayan Laboratory,
  built on the Signature Commons framework, that abstracts drug and small-molecule
  attributes from 13 resources into 35 drug set libraries (110,903 drug sets covering
  14,579 small molecules). Libraries cover targets, mechanisms of action, indications,
  side effects, pharmacogenomic variants, chemical fingerprints, literature co-mentions,
  and L1000-induced gene expression and enriched terms. Users can search drug sets
  and run drug set enrichment analysis, and the companion Drugmonizome-ML Appyter
  builds machine learning pipelines on the same libraries.
domains:
- pharmacology
- drug discovery
- drug repositioning
- cheminformatics
- chemistry and biochemistry
- machine learning
- information technology
homepage_url: https://maayanlab.cloud/drugmonizome/
id: drugmonizome
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: Drugmonizome
products:
- category: GraphicalInterface
  description: Web search engine for querying drug set libraries by term or drug,
    and for submitting drug lists for drug set enrichment analysis against the Drugmonizome
    libraries.
  format: http
  id: drugmonizome.portal
  name: Drugmonizome Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  product_url: https://maayanlab.cloud/drugmonizome/
- category: ProgrammingInterface
  description: Signature Commons metadata API (LoopBack, OpenAPI) for querying Drugmonizome
    resources, libraries, drug sets, and small-molecule entities and their metadata.
  format: json
  id: drugmonizome.metadata-api
  is_public: true
  name: Drugmonizome Metadata API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  product_url: https://maayanlab.cloud/drugmonizome/metadata-api/
- category: ProgrammingInterface
  description: Signature Commons data API (EnrichmentAPI) for fast drug set enrichment
    queries over the Drugmonizome libraries.
  format: json
  id: drugmonizome.data-api
  is_public: true
  name: Drugmonizome Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  product_url: https://maayanlab.cloud/drugmonizome/data-api/
- category: Product
  description: The 35 Drugmonizome drug set libraries, listed with metadata and per-library
    download links. Each library is downloadable as a GMT-like DMT file keyed by InChIKey
    or by drug name. Sources are DrugBank (targets, enzymes, carriers, transporters,
    ATC codes), DrugCentral targets, the Drug Repurposing Hub (targets and mechanisms
    of action), STITCH targets, KINOMEscan kinases, SIDER side effects and indications,
    PharmGKB variants and OFFSIDES side effects, PubChem and RDKit MACCS chemical
    fingerprints, Geneshot literature and predicted genes (including ARCHS4 coexpression
    and Enrichr co-occurrence), CREEDS signatures, and L1000FWD signatures, Enrichr
    GO and KEGG terms, and SEP-L1000 predicted side effects.
  format: json
  id: drugmonizome.libraries
  name: Drugmonizome Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: repohub
  - relation_type: prov:wasDerivedFrom
    source: stitch
  - relation_type: prov:wasDerivedFrom
    source: kinomescan
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: geneshot
  - relation_type: prov:wasDerivedFrom
    source: archs4
  - relation_type: prov:wasDerivedFrom
    source: enrichr
  - relation_type: prov:wasDerivedFrom
    source: creeds
  - relation_type: prov:wasDerivedFrom
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: sep-l1000
  product_url: https://maayanlab.cloud/drugmonizome/metadata-api/libraries
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-27: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-10-28: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Drugmonizome-ML Appyter, a Jupyter-notebook-based web app that builds
    customized machine learning pipelines from selected Drugmonizome drug set libraries
    to predict drug attributes such as side effects.
  format: http
  id: drugmonizome.ml-appyter
  name: Drugmonizome-ML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  product_url: https://appyters.maayanlab.cloud/Drugmonizome_ML/
  repository: https://github.com/MaayanLab/Drugmonizome-ML
publications:
- authors:
  - Kropiwnicki E
  - Evangelista JE
  - Stein DJ
  - Clarke DJB
  - Lachmann A
  - Kuleshov MV
  - Jeon M
  - Jagodnik KM
  - Ma'ayan A
  doi: 10.1093/database/baab017
  id: PMID:33787872
  journal: Database (Oxford)
  preferred: true
  title: 'Drugmonizome and Drugmonizome-ML: integration and abstraction of small molecule
    attributes for drug enrichment analysis and machine learning'
  year: '2021'
repository: https://github.com/MaayanLab/drugmonizome
rrid: SCR_024821
synonyms:
- Drugmonizome-ML
taxon:
- NCBITaxon:9606
---
# Drugmonizome

Drugmonizome is a drug set database and search engine from the Ma'ayan Laboratory at the Icahn School of Medicine at Mount Sinai, built on the Signature Commons framework. It processes drug and small-molecule attributes from public resources into drug set libraries, where each set groups the small molecules that share a target, side effect, mechanism, chemical feature, or other attribute. Drugmonizome-ML is a companion Appyter that uses these libraries as features for machine learning.

## Data Content

As of October 2026 the metadata API lists 13 resources, 35 libraries, 110,903 drug sets, and 14,579 small-molecule entities. Libraries come from DrugBank (targets, enzymes, carriers, transporters, and ATC codes), DrugCentral, the Drug Repurposing Hub, STITCH, KINOMEscan, SIDER (side effects and indications), PharmGKB (variants and OFFSIDES side effects), PubChem and RDKit MACCS fingerprints, Geneshot (literature-associated and predicted genes, including predictions from ARCHS4 coexpression and Enrichr), CREEDS signatures, and L1000FWD. The L1000FWD libraries include up- and down-regulated genes, enriched GO and KEGG terms computed with Enrichr, and side effects predicted by SEP-L1000. Small molecules are identified by InChIKey.

## Access

The web application supports term and drug searches and drug set enrichment analysis. The Signature Commons metadata API and data API expose the same content programmatically. Each library can be downloaded as a DMT file keyed by InChIKey or by drug name; the download links are listed in the metadata API. Drugmonizome-ML runs as an Appyter at appyters.maayanlab.cloud.

## License

The Drugmonizome GitHub repository is released under CC BY-NC-SA 4.0. No separate data license was found on the web site. Users are asked to cite Kropiwnicki et al. 2021 (Database).