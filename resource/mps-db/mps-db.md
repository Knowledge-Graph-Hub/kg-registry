---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: MPSHELP@pitt.edu
  - contact_type: url
    value: https://www.csb.pitt.edu/
  label: MPS-Db Help Desk, University of Pittsburgh
- category: Individual
  contact_details:
  - contact_type: email
    value: mes234@pitt.edu
  label: Mark Schurdak
creation_date: '2026-10-03T00:00:00Z'
description: The Microphysiology Systems Database (MPS-Db) was a web-based database
  developed at the University of Pittsburgh Drug Discovery Institute and Department
  of Computational and Systems Biology for capturing, managing, analyzing and sharing
  experimental data from microphysiology systems, from static microplate models to
  multi-organ microfluidic organ-on-chip models. It linked these data to reference
  chemical, bioactivity, preclinical, clinical and post-marketing data from ChEMBL,
  PubChem, DrugBank, UniChem, OpenFDA and FAERS, and served as the data platform for
  the NCATS Tissue Chip Testing Center program. The Pitt-hosted MPS-Db is no longer
  available in its published form - its homepage now redirects to EveAnalytics, a
  login-only commercial successor platform operated under license from the University
  of Pittsburgh.
domains:
- drug discovery
- toxicology
- pharmacology
- anatomy and development
homepage_url: https://mps.csb.pitt.edu/
id: mps-db
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://doi.org/10.1039/c9lc01047e
  label: Custom (free for non-profit research use with citation; license required for
    for-profit use)
name: Microphysiology Systems Database
products:
- category: GraphicalInterface
  description: MPS-Db web portal for browsing, analyzing and sharing microphysiology
    system study data alongside reference compound, bioactivity, preclinical and clinical
    data drawn from ChEMBL, PubChem, DrugBank, UniChem and FAERS (via OpenFDA).
  format: http
  id: mps-db.portal
  name: MPS-Db Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mps-db
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://mps.csb.pitt.edu/
  warnings:
  - As of 2026-10-03 this URL redirects (HTTP 302) to EveAnalytics (eveanalytics.com),
    the commercial successor platform; the Pitt-hosted portal is no longer available.
- category: GraphicalInterface
  description: EveAnalytics, the commercial successor to the MPS-Db (formerly the BioSystics
    Analytics Platform), aggregating microphysiology system data with linked preclinical
    and clinical databases. Operated under license from the University of Pittsburgh.
  format: http
  id: mps-db.eveanalytics
  name: EveAnalytics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mps-db
  product_url: https://eveanalytics.com/
  warnings:
  - EveAnalytics requires an account; access is offered through trial and paid license
    registration, and no content is available without logging in.
publications:
- authors:
  - Albert Gough
  - Lawrence Vernetti
  - Luke Bergenthal
  - Tong Ying Shun
  - D Lansing Taylor
  doi: 10.1089/aivt.2016.0011
  id: doi:10.1089/aivt.2016.0011
  journal: Applied In Vitro Toxicology
  title: The Microphysiology Systems Database for Analyzing and Modeling Compound
    Interactions with Human and Animal Organ Models
  year: '2016'
- authors:
  - Mark Schurdak
  - Lawrence Vernetti
  - Luke Bergenthal
  - Quinn K Wolter
  - Tong Ying Shun
  - Sandra Karcher
  - D Lansing Taylor
  - Albert Gough
  doi: 10.1039/c9lc01047e
  id: doi:10.1039/c9lc01047e
  journal: Lab on a Chip
  preferred: true
  title: Applications of the microphysiology systems database for experimental ADME-Tox
    and disease models
  year: '2020'
synonyms:
- MPS-Db
- MPS Database
- BioSystics Analytics Platform
- BioSystics-AP
---
# Microphysiology Systems Database (MPS-Db)

The Microphysiology Systems Database (MPS-Db) was developed at the University of
Pittsburgh Drug Discovery Institute and Department of Computational and Systems
Biology. It captured, managed, analyzed and shared experimental data from
microphysiology systems (MPS), ranging from static microplate models to integrated
multi-organ microfluidic organ-on-chip models (RRID:SCR_021126).

## Data

Study data were linked to physicochemical, bioactivity and clinical information for
compounds, automatically curated from OpenFDA, PubChem, TogoWS, UniChem, DrugBank and
ChEMBL. Adverse event data from FAERS and prescription estimates from the CDC's
National Ambulatory Medical Care Survey and National Hospital Ambulatory Medical Care
Survey were used to normalize clinical liver-toxicity findings. The MPS-Db served as
the data platform for the NCATS Tissue Chip Testing Center (TCTC) program; the 2020
paper reports 32 experimental MPS models covering 10 organs within TCTC.

Registered users could keep studies private, share them with collaborators, or make
them public. Summary text, metadata, raw and processed data, protocols and images
could be downloaded for analysis in other software.

## Status

The Pitt-hosted MPS-Db is no longer available in its published form. As of
2026-10-03, https://mps.csb.pitt.edu/ redirects to https://eveanalytics.com/.
University of Pittsburgh pages state that the MPS-Db was rebranded as the BioSystics
Analytics Platform (BioSystics-AP) when BioSystics, Inc. spun out of the university
in 2022; the platform now operates as EveAnalytics, whose site footer reads
"University of Pittsburgh. Used under license". EveAnalytics requires an account,
with trial and paid license registration.

The 2020 paper states that source code was available on GitHub for non-profit use,
but no repository URL was given.

## License

Per the 2020 paper: "All use of the MPS-Db and content is free for non-profit
research applications provided any published works reference the MPS Database
website." Use of the data or tools for for-profit applications required a license.

## Funding

NIH/NCATS (5UH3TR00503, 3UH3TR00503-04S1), NIH 1S10-OD01226, and US EPA STAR
83573601.
