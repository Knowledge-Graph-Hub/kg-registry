---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.genomernai.org/
  label: GenomeRNAi
creation_date: '2026-06-17T00:00:00Z'
description: GenomeRNAi is a database containing phenotypes from cell-based and in
  vivo RNA interference (RNAi) screens in Drosophila and Homo sapiens. It also
  provides a curated resource of RNAi reagents and their predicted specificity and
  efficiency.
domains:
- genomics
- organisms
homepage_url: http://www.genomernai.org/
id: genomernai
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: GenomeRNAi
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching RNAi phenotypes and reagents.
  format: http
  id: genomernai.site
  is_public: true
  name: GenomeRNAi Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomernai
  product_url: http://www.genomernai.org/
- category: Product
  description: Bulk downloads of RNAi phenotype and reagent datasets.
  format: mixed
  id: genomernai.downloads
  name: GenomeRNAi Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomernai
  product_url: http://www.genomernai.org/Download
publications:
- authors:
  - Esther E. Schmidt
  - Oliver Pelz
  - Svetlana Buhlmann
  - Grainne Kerr
  - Thomas Horn
  - Michael Boutros
  doi: 10.1093/nar/gks1170
  id: https://doi.org/10.1093/nar/gks1170
  journal: Nucleic Acids Research
  preferred: true
  title: 'GenomeRNAi: a database for cell-based and in vivo RNAi phenotypes, 2013 update'
  year: '2013'
---
# GenomeRNAi

GenomeRNAi is a database of phenotypes obtained from RNA interference (RNAi) screens in
Drosophila and human cells, together with information on the RNAi reagents used. It
enables comparison of phenotypic results across studies and assessment of reagent quality.

Content includes:

- Phenotypes from published cell-based and in vivo RNAi screens
- RNAi reagents (dsRNAs, siRNAs) with predicted specificity and efficiency
- A "frame" annotation indicating reagent quality
- Bulk downloads of phenotype and reagent data

GeneCards integrates RNAi phenotype data from GenomeRNAi.
