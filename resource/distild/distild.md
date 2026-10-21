---
activity_status: unresponsive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://jensenlab.org/
  label: Jensen Lab, Novo Nordisk Foundation Center for Protein Research
creation_date: '2026-10-21T00:00:00Z'
description: DistiLD maps disease- and trait-associated SNPs and genes from genome-wide association
  studies (GWAS) onto linkage disequilibrium (LD) blocks to help identify candidate disease
  genes. It links published GWAS results to standardized ICD-10 disease codes and uses HapMap
  data to partition chromosomes into LD blocks onto which SNPs and genes are mapped. The web
  interface let users query by disease, SNP, or gene. The homepage refused connections when
  checked in October 2026 and the resource appears retired.
domains:
- genome-wide association studies
- genetic variation
- genomics
homepage_url: http://distild.jensenlab.org/
id: distild
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: DistiLD
products:
- category: GraphicalInterface
  description: Web interface for querying and visualizing disease- and trait-associated SNPs
    and genes within LD blocks, searchable by disease, SNP, or gene. The site refused connections
    when checked in October 2026.
  format: http
  id: distild.database
  name: DistiLD Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: distild
  product_url: http://distild.jensenlab.org/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: diseases
publications:
- authors:
  - Albert Pallejà
  - Heiko Horn
  - Sabrina Eliasson
  - Lars Juhl Jensen
  doi: 10.1093/nar/gkr899
  id: doi:10.1093/nar/gkr899
  journal: Nucleic Acids Research
  preferred: true
  title: 'DistiLD Database: diseases and traits in linkage disequilibrium blocks'
  year: '2012'
rrid: SCR_005943
taxon:
- NCBITaxon:9606
---

# DistiLD

## Overview

DistiLD maps disease- and trait-associated SNPs and genes from GWAS onto linkage disequilibrium (LD) blocks, linking published GWAS results to ICD-10 disease codes and partitioning chromosomes into LD blocks using HapMap data. It was built on the GWAS Catalog, Ensembl, and the Jensen Lab DISEASES resource.

## Access

- DistiLD database web interface: query by disease, SNP, or gene.

The homepage actively refused connections when checked in October 2026, so this resource is recorded with an activity status of unresponsive.

## Citation

Please cite: Pallejà A, Horn H, Eliasson S, Jensen LJ. DistiLD Database: diseases and traits in linkage disequilibrium blocks. Nucleic Acids Res. 2012;40(D1):D1036–D1040. doi:10.1093/nar/gkr899
