---
activity_status: active
category: KnowledgeGraph
collection:
  - aop
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://insight-project.org/
    label: INSIGHT Project Team
  - category: Individual
    contact_details:
      - contact_type: email
        value: dario.greco@tuni.fi
    label: Dario Greco
  - category: Individual
    contact_details:
      - contact_type: email
        value: angela.serra@tuni.fi
    label: Angela Serra
creation_date: '2025-08-30T00:00:00Z'
description: INSIGHT (Integrated Models for the Development and Assessment of High Impact Chemicals and Materials) is a Horizon Europe project (Grant Agreement 101137742, January 2024 to December 2027) coordinated from Tampere University that is building a computational framework for Safe and Sustainable by Design (SSbD) assessment of chemicals and materials. The framework links a data graph, a model graph and an Impact Outcome Pathway (IOP) graph, extending the Adverse Outcome Pathway concept to connect chemical and material properties with health, environmental, social and economic impacts. The INSIGHT knowledge graph integrates curated toxicogenomics data, gene-key event-AOP annotations, CTD chemical-gene-disease relationships, exposure and life cycle inventory data, and literature-mined associations, and is being validated in case studies on PFAS, graphene-based materials, bio-based synthetic amorphous silica and antimicrobial coatings.
domains:
  - toxicology
  - adverse outcome pathways
  - environment
  - sustainability
  - chemistry and biochemistry
  - genomics
  - gene expression profiling
homepage_url: https://insight-project.org/
id: insight
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
name: INSIGHT
publications:
  - id: doi:10.1016/j.csbj.2025.03.042
    doi: 10.1016/j.csbj.2025.03.042
    title: 'INSIGHT: An integrated framework for safe and sustainable chemical and material assessment'
    authors:
      - Angela Serra
      - Dimitrios Zouraris
      - Alexandra Schaffert
      - Marcella Torres Maia
      - Periklis Tsiros
      - Ishita Virmani
      - Emanuele Di Lieto
      - Laura Aliisa Saarimäki
      - Jack Morikka
      - Rafael Riudavets-Puig
      - Dimitra-Danai Varsou
      - Konstantinos D. Papavasileiou
      - Panagiotis D. Kolokathis
      - Dimitris G. Mintis
      - Haralampos Tzoupis
      - Andreas Tsoumanis
      - Georgia Melagraki
      - Alex Arvanitidis
      - Philip Doganis
      - Vasileios Minadakis
      - Giannis Savvas
      - Adrien Perello-y-bestard
      - Stefano Cucurachi
      - Marija Buljan
      - Fotini Nikiforou
      - Achilleas Karakoltzidis
      - Spyros Karakitsios
      - Dimosthenis A. Sarigiannis
      - Steffi Friedrichs
      - Christian Seitz
      - Tomas Navarrete Gutierrez
      - Panagiotis Isigonis
      - Sébastien Cambier
      - Antonino Marvuglia
      - Gottlieb Georg Lindner
      - Jacques-Aurélien Sergent
      - L. Cristiana Gheorghe
      - Laura-Jayne A. Bradford
      - Seung-Geun Park
      - Seung Min Ha
      - Zayakhuu Gerelkhuu
      - Tae Hyun Yoon
      - Romana Petry
      - Diego Stéfani Teodoro Martinez
      - David A. Winkler
      - Peter Wick
      - Thomas E. Exner
      - Francesco Dondero
      - Tommaso Serchi
      - Willie Peijnenburg
      - Haralambos Sarimveis
      - Martin Paparella
      - Iseult Lynch
      - Antreas Afantitis
      - Dario Greco
    journal: Computational and Structural Biotechnology Journal
    year: '2025'
    preferred: true
products:
  - category: GraphicalInterface
    description: INSIGHT project website with the project's research approach, consortium, news and dissemination materials.
    format: http
    id: insight.portal
    name: INSIGHT Project Portal
    original_source:
      - source: insight
        relation_type: prov:hadPrimarySource
    product_url: https://insight-project.org/
  - category: Product
    description: Curated, harmonized and standardized collection of PFAS toxicogenomics data (Zenodo, CC BY 4.0), co-funded by INSIGHT. It reprocesses public transcriptomic datasets from GEO (human, mouse and rat liver and other systems) with quality control, normalized expression matrices, raw counts, filtered and unfiltered differentially expressed genes and curation scripts, plus new THP-1 macrophage profiles for seven PFAS, structured for linkage to Adverse Outcome Pathways.
    format: mixed
    id: insight.pfas_toxicogenomics
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC BY 4.0
    name: PFAS Toxicogenomics Data Collection
    original_source:
      - source: insight
        relation_type: prov:hadPrimarySource
      - source: gene-expression-omnibus
        relation_type: prov:hadPrimarySource
    product_url: https://zenodo.org/records/17985510
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
  - NCBITaxon:10116
---

# INSIGHT

## Overview

INSIGHT (Integrated Models for the Development and Assessment of High Impact Chemicals and Materials) is a Horizon Europe project (Grant Agreement 101137742, HORIZON-CL4-2023-RESILIENCE-01, January 2024 to December 2027) building an integrated framework for Safe and Sustainable by Design (SSbD) assessment of chemicals and materials. The framework links three graphs:

- a **data graph** (knowledge graph) of curated toxicogenomics data, gene-key event-AOP annotations derived from the AOP-Wiki, chemical-gene-disease-pathway relationships from CTD, and planned apical endpoints from ECOTOX and PubChem bioassays, plus literature-mined associations;
- a **model graph** of computational models (hosted on platforms such as Jaqpot and the Enalos Cloud Platform);
- an **Impact Outcome Pathway (IOP) graph** that extends Adverse Outcome Pathways to environmental, social and economic impacts.

Case studies cover PFAS, graphene-based materials, bio-based synthetic amorphous silica and antimicrobial coatings.

## Access

- Project website: https://insight-project.org/
- PFAS toxicogenomics data collection: https://zenodo.org/records/17985510 (doi:10.5281/zenodo.17985510, CC BY 4.0)
- Other project deliverables and datasets are published on Zenodo under grant 101137742.

As of 2026-10-27 the integrated INSIGHT knowledge graph itself is not publicly downloadable.

## Citation

Serra A, Zouraris D, Schaffert A, et al. INSIGHT: An integrated framework for safe and sustainable chemical and material assessment. Computational and Structural Biotechnology Journal. 2025;29:125-137. doi:10.1016/j.csbj.2025.03.042

## Automated Evaluation

- View the automated evaluation: [insight automated evaluation](insight_eval_automated.html)
