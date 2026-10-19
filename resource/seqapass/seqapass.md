---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: seqapass.support@epa.gov
  label: US EPA SeqAPASS Support
creation_date: '2026-10-19T00:00:00Z'
description: Sequence Alignment to Predict Across Species Susceptibility (SeqAPASS)
  is an online US EPA screening tool for extrapolating chemical toxicity information
  from data-rich model organisms (e.g., human, mouse, rat, zebrafish) to thousands
  of non-target species. Many chemicals act through known protein targets. Using
  protein sequence and structure data from the NCBI protein database, SeqAPASS compares
  amino acid sequence and protein structure similarity across species to predict
  whether those targets are present, and so whether the species are likely to be
  susceptible. Version 8 can also generate protein structures across species and
  report metrics on their quality.
domains:
- toxicology
- environment
- ecology
- proteomics
- protein structure
- genomics
- molecular evolution
homepage_url: https://www.epa.gov/comptox-tools/sequence-alignment-predict-across-species-susceptibility-seqapass-resource-hub
id: seqapass
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: SeqAPASS (Sequence Alignment to Predict Across Species Susceptibility)
products:
- category: GraphicalInterface
  description: The SeqAPASS web application for cross-species comparison of chemical
    protein targets by primary amino acid sequence, functional domain, and individual
    amino acid residue similarity, with protein structure generation in version 8.
    A user account is required.
  format: http
  id: seqapass.app
  is_public: true
  name: SeqAPASS Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: seqapass
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  product_url: https://seqapass.epa.gov/seqapass/
- category: DocumentationProduct
  description: SeqAPASS V8 user guide describing how to run and interpret cross-species
    susceptibility queries.
  format: http
  id: seqapass.user-guide
  name: SeqAPASS User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: seqapass
  product_url: https://www.epa.gov/comptox-tools/seqapass-user-guide
publications:
- authors:
  - Carlie A. LaLone
  - Daniel L. Villeneuve
  - David Lyons
  - Henry W. Helgen
  - Serina L. Robinson
  - Joseph A. Swintek
  - Travis W. Saari
  - Gerald T. Ankley
  doi: 10.1093/toxsci/kfw119
  id: https://doi.org/10.1093/toxsci/kfw119
  journal: Toxicological Sciences
  preferred: true
  title: 'Editor''s Highlight: Sequence Alignment to Predict Across Species Susceptibility
    (SeqAPASS): A Web-Based Tool for Addressing the Challenges of Cross-Species Extrapolation
    of Chemical Toxicity'
  year: '2016'
- authors:
  - Jon A. Doering
  - Sehan Lee
  - Kurt Kristiansen
  - Linn Evenseth
  - Mace G. Barron
  - Ingebrigt Sylte
  - Carlie A. LaLone
  doi: 10.1093/toxsci/kfy186
  id: https://doi.org/10.1093/toxsci/kfy186
  journal: Toxicological Sciences
  title: In Silico Site-Directed Mutagenesis Informs Species-Specific Predictions
    of Chemical Susceptibility Derived From the Sequence Alignment to Predict Across
    Species Susceptibility (SeqAPASS) Tool
  year: '2018'
---
# SeqAPASS (Sequence Alignment to Predict Across Species Susceptibility)

## Overview

SeqAPASS is a fast, online screening tool from the US EPA that lets researchers and regulators extrapolate toxicity information across species. Toxicity data are plentiful for a few model organisms and scarce for most other plants and animals. SeqAPASS addresses this gap by checking whether the protein target a chemical acts on is conserved in non-target species, such as pollinators or threatened and endangered species. It supports cross-species extrapolation as a new approach methodology (NAM) and reduces reliance on animal testing.

## Data Content

- Cross-species comparisons of chemical protein targets based on primary amino acid sequence, functional domain, and key amino acid residue similarity.
- Protein sequence data from the NCBI protein database. Version 8 adds protein structure generation and structure quality metrics.
- Published case studies include the estrogen receptor (EDSP), the insect ecdysone receptor, and the honey bee nicotinic acetylcholine receptor.

## Access

- Web application (account required): https://seqapass.epa.gov/seqapass/
- Resource hub: https://www.epa.gov/comptox-tools/sequence-alignment-predict-across-species-susceptibility-seqapass-resource-hub
- User guide: https://www.epa.gov/comptox-tools/seqapass-user-guide

## License

SeqAPASS is developed by the US EPA. As a work of the U.S. federal government it is generally in the public domain (U.S. Government Work). The underlying sequence data come from NCBI.
