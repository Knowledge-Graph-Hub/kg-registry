---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://iidp.coh.org/
  label: Integrated Islet Distribution Program (IIDP)
creation_date: '2026-07-01T00:00:00Z'
description: The Integrated Islet Distribution Program (IIDP), based at City of Hope
  and funded by NIH/NIDDK, is the largest source of human islets for diabetes research
  in the United States. It procures, characterizes, and distributes high-quality human
  pancreatic islets to approved investigators, and many downstream studies deposit
  resulting omic data in public repositories such as the Gene Expression Omnibus.
domains:
- biomedical
- genomics
- clinical
homepage_url: https://iidp.coh.org/
id: iidp
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: Integrated Islet Distribution Program (IIDP)
products:
- category: DataSource
  description: Web portal for requesting human pancreatic islets and accessing associated
    islet characterization data distributed by the IIDP.
  format: http
  id: iidp.portal
  name: IIDP Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iidp
  product_url: https://iidp.coh.org/
- category: GraphProduct
  description: Pancreas-focused knowledge graph integrating genes, SNPs, pancreatic
    expression QTLs, and donor-derived islet datasets harmonized within PanKbase.
  format: http
  id: pankgraph.graph
  name: PanKgraph Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankgraph
  - relation_type: prov:wasDerivedFrom
    source: pankbase
  - relation_type: prov:hadPrimarySource
    source: hpap
  - relation_type: prov:hadPrimarySource
    source: iidp
  - relation_type: prov:hadPrimarySource
    source: prodo
  product_url: https://pankgraph.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
taxon:
- NCBITaxon:9606
---
Integrated Islet Distribution Program (IIDP)

## Description

The Integrated Islet Distribution Program (IIDP) is an NIH/NIDDK-funded program based at City of Hope that procures, characterizes, and distributes human pancreatic islets to the research community. Islets distributed by the IIDP underpin many published single-cell and functional studies, and IIDP is one of the primary upstream islet sources integrated by PanKbase.