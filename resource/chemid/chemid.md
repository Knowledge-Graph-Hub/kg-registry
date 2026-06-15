---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/
  label: National Library of Medicine
creation_date: '2026-06-02T00:00:00Z'
description: ChemIDplus was a National Library of Medicine chemical identification
  resource for chemical names, synonyms, structures, and substance identifiers; its
  content is now available through PubChem.
domains:
- chemistry and biochemistry
- environment
- biomedical
homepage_url: https://pubchem.ncbi.nlm.nih.gov/source/ChemIDplus
id: chemid
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/copyright.html
  label: NLM copyright information
name: ChemIDplus
products:
- category: GraphicalInterface
  description: PubChem source page for ChemIDplus, providing the current access point
    for ChemIDplus substance records and annotations after the standalone NLM service
    was retired.
  id: chemid.pubchem-source
  name: ChemIDplus in PubChem
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemid
  product_url: https://pubchem.ncbi.nlm.nih.gov/source/ChemIDplus
  secondary_source:
  - relation_type: prov:used
    source: pubchem
- category: DocumentationProduct
  description: NLM guide for locating migrated ChemIDplus content within PubChem.
  id: chemid.pubchem-guide
  name: Accessing ChemIDplus Content from PubChem
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemid
  product_url: https://www.nlm.nih.gov/toxnet/Accessing_ChemIDplus_Content_from_PubChem.pdf
  secondary_source:
  - relation_type: prov:used
    source: pubchem
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-15: No Content-Length
    header found'
- category: MappingProduct
  description: Downloadable Excel and CSV files containing DSSTox identifiers mapped
    to CAS numbers, InChIKeys, SMILES, molecular formulas, and other chemical identifiers
    for over 1.2 million substances
  format: mixed
  id: dsstoxdb.downloads
  latest_version: 10.23645/epacomptox.5588566.v8
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0
  name: DSSTox Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  product_url: https://epa.figshare.com/articles/dataset/Chemistry_Dashboard_Data_DSSTox_Identifiers_Mapped_to_CAS_Numbers_and_Names/5588566
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: epa-srs
  - relation_type: prov:wasInformedBy
    source: chemid
  - relation_type: prov:wasInformedBy
    source: pubchem
synonyms:
- Chemical Identification Plus
- ChemIDplus
warnings:
- NLM retired the standalone ChemIDplus chemical information site; current access
  is through PubChem.
---
# ChemIDplus

ChemIDplus was an NLM chemical identification resource used for names, synonyms,
structures, and identifiers for chemical substances cited in NLM databases. The
standalone service has been retired, and ChemIDplus content is now surfaced
through PubChem.