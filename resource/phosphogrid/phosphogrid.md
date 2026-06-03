---
activity_status: orphaned
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: biogridadmin@gmail.com
      - contact_type: url
        value: https://phosphogrid.org/about.php
    label: PhosphoGRID Team
creation_date: '2026-06-02T00:00:00Z'
description: PhosphoGRID is a curated resource of experimentally verified in vivo protein phosphorylation sites in Saccharomyces cerevisiae, including kinase and phosphatase annotations, experimental conditions, functional effects, and links to yeast resources.
domains:
  - proteomics
  - biological systems
  - biomedical
homepage_url: https://phosphogrid.org/
id: phosphogrid
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: PhosphoGRID
products:
  - category: GraphicalInterface
    description: Legacy PhosphoGRID web portal for searching experimentally verified in vivo yeast phosphorylation sites by ORF, gene name, or external identifier.
    id: phosphogrid.portal
    name: PhosphoGRID Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phosphogrid
    product_url: https://phosphogrid.org/
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: biogrid
      - relation_type: prov:wasInformedBy
        source: sgd
  - category: Product
    compression: zip
    description: BioGRID latest post-translational modification download archive containing PTM and PTMREL files with BioGRID PTM records and annotation data; the current PhosphoGRID site redirects search and download activity into BioGRID.
    format: tsv
    id: biogrid.ptms-latest
    license:
      id: https://biogrid-downloads.nyc3.digitaloceanspaces.com/LICENSE.txt
      label: MIT License
    name: BioGRID Latest PTM Download
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biogrid
    product_file_size: 59206317
    product_url: https://downloads.thebiogrid.org/Download/BioGRID/Latest-Release/BIOGRID-PTMS-LATEST.ptm.zip
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: phosphogrid
  - category: GraphProduct
    description: Current iPTMnet PTM record table with PTM type, source, UniProt protein, organism, site, enzyme, relation identifiers, and publication evidence.
    format: tsv
    id: iptmnet.ptm
    license:
      id: https://creativecommons.org/licenses/by-nc-sa/4.0/
      label: CC BY-NC-SA 4.0
    name: iPTMnet PTM Table
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iptmnet
    product_file_size: 44116546
    product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dbptm
      - relation_type: prov:wasDerivedFrom
        source: dbsno
      - relation_type: prov:wasDerivedFrom
        source: efip
      - relation_type: prov:wasDerivedFrom
        source: hprd
      - relation_type: prov:wasDerivedFrom
        source: nextprot
      - relation_type: prov:wasDerivedFrom
        source: p3db
      - relation_type: prov:wasDerivedFrom
        source: phosphoelm
      - relation_type: prov:wasDerivedFrom
        source: phosphogrid
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
      - relation_type: prov:wasDerivedFrom
        source: phosphat
      - relation_type: prov:wasDerivedFrom
        source: pombase
      - relation_type: prov:wasDerivedFrom
        source: pubtator
      - relation_type: prov:wasDerivedFrom
        source: rlims-p
      - relation_type: prov:wasDerivedFrom
        source: signor
      - relation_type: prov:wasDerivedFrom
        source: uniprot
publications:
  - doi: 10.1093/database/bat026
    id: doi:10.1093/database/bat026
    journal: Database
    preferred: true
    title: 'The PhosphoGRID Saccharomyces cerevisiae protein phosphorylation site database: version 2.0 update'
    year: '2013'
  - doi: 10.1093/database/bap026
    id: doi:10.1093/database/bap026
    journal: Database
    title: PhosphoGRID, a database of experimentally verified in vivo protein phosphorylation sites from the budding yeast Saccharomyces cerevisiae
    year: '2010'
taxon:
  - NCBITaxon:559292
synonyms:
  - Phosphorylation Site Search
warnings:
  - PhosphoGRID search results and downloads are permanently redirected into BioGRID for broader post-translational modification curation.
---

# PhosphoGRID

PhosphoGRID is a legacy yeast phosphorylation-site resource. Its curated
Saccharomyces cerevisiae phosphosite annotations are represented in the current
BioGRID post-translational modification infrastructure and in iPTMnet.
