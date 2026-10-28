---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ideaconsult.net/
  label: IDEAconsult Ltd (ExCAPE project)
- category: Individual
  contact_details:
  - contact_type: url
    value: https://orcid.org/0000-0002-8755-3394
  label: Nina Jeliazkova
creation_date: '2026-10-28T00:00:00Z'
description: ExCAPE-DB (the ExCAPE chemogenomics database) is an integrated, large-scale,
  open-access dataset of structure-activity relationship data built for big-data analysis
  in chemogenomics. It combines active and inactive compound-target bioactivity annotations
  from the two public sources ChEMBL and PubChem into a single standardized, normalized
  dataset of over 70 million SAR data points, with chemical structures, target information,
  and activity annotations. It was created for the EU Horizon 2020 ExCAPE project and
  is provided both as a downloadable dataset and through a searchable web interface.
domains:
- cheminformatics
- chemistry and biochemistry
- drug discovery
- machine learning
- information technology
homepage_url: https://solr.ideaconsult.net/search/excape/
id: excape-db
last_modified_date: '2026-10-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: ExCAPE-DB
products:
- category: GraphicalInterface
  description: ExCAPE-DB searchable web interface (Solr-based) for querying the ExCAPE
    chemogenomics dataset by compound and target.
  format: http
  id: excape-db.search
  name: ExCAPE-DB Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: excape-db
  product_url: https://solr.ideaconsult.net/search/excape/
- category: Product
  description: The ExCAPE chemogenomics dataset (over 70 million SAR data points integrating
    ChEMBL and PubChem bioactivity annotations), distributed on Zenodo; version 2 fixed
    SMILES errors.
  format: tsv
  compression: targz
  id: excape-db.dataset
  name: ExCAPE Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: excape-db
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://doi.org/10.5281/zenodo.675987
publications:
- authors:
  - Jiangming Sun
  - Nina Jeliazkova
  - Vladimir Chupakhin
  - Jose-Felipe Golib-Dzib
  - Ola Engkvist
  - Lars Carlsson
  - Jörg Wegner
  - Hugo Ceulemans
  - Ivan Georgiev
  - Vedrin Jeliazkov
  - et al.
  doi: 10.1186/s13321-017-0203-5
  id: doi:10.1186/s13321-017-0203-5
  journal: Journal of Cheminformatics
  preferred: true
  title: 'ExCAPE-DB: an integrated large scale dataset facilitating Big Data analysis
    in chemogenomics'
  year: '2017'
synonyms:
- ExCAPE chemogenomics database
---
# ExCAPE-DB

## Overview

ExCAPE-DB (the ExCAPE chemogenomics database) is an integrated, open-access dataset of structure-activity relationship data for big-data analysis in chemogenomics. It merges active and inactive compound-target bioactivity annotations from ChEMBL and PubChem into a single standardized dataset of over 70 million SAR data points, with chemical structures, target information, and activity annotations. It was built for the EU Horizon 2020 ExCAPE project.

## Access

- Searchable web interface (Solr) at solr.ideaconsult.net/search/excape.
- Downloadable dataset on Zenodo (concept DOI 10.5281/zenodo.675987, CC BY-SA 4.0); version 2 (2019) fixed SMILES errors.

## Citation

Sun J, Jeliazkova N, Chupakhin V, et al. ExCAPE-DB: an integrated large scale dataset facilitating Big Data analysis in chemogenomics. J Cheminform. 2017;9:17. doi:10.1186/s13321-017-0203-5
