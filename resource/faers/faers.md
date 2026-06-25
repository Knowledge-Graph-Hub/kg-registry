---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: FDA-SRS@fda.hhs.gov
  id: fda
  label: FDA Center for Drug Evaluation and Research
creation_date: '2025-11-04T00:00:00Z'
description: The FDA Adverse Event Monitoring System (AEMS), formerly the FDA Adverse
  Event Reporting System (FAERS), is a database that contains adverse event reports,
  medication error reports, and product quality complaints resulting in adverse events
  submitted to the FDA. AEMS/FAERS supports the FDA's post-marketing safety surveillance
  program for drug and therapeutic biologic products. The database adheres to ICH
  E2B international safety reporting guidance, and adverse events are coded using
  MedDRA (Medical Dictionary for Regulatory Activities) terminology. FAERS provides
  quarterly data files in ASCII and XML formats dating back to 2012, with archives
  available for earlier data.
domains:
- pharmacology
- drug discovery
- clinical
- public health
homepage_url: https://www.fda.gov/drugs/surveillance/fdas-adverse-event-reporting-system-faers
id: faers
infores_id: faers
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: FDA Adverse Event Reporting System
products:
- category: GraphicalInterface
  description: Interactive dashboard for exploring FAERS data with visualizations
    and search capabilities
  format: http
  id: faers.public_dashboard
  name: FAERS Public Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  product_url: https://fis.fda.gov/sense/app/95239e26-e0be-42d9-a960-9a5f7f1c25ee/sheet/7a47a261-d58b-4203-a8aa-6d3021737452/state/analysis
- category: Product
  description: Quarterly data extracts in ASCII format containing demographic, drug,
    reaction, outcome, and source information for reported adverse events
  format: txt
  id: faers.quarterly_data_ascii
  latest_version: 2026Q1
  name: FAERS Quarterly Data Files (ASCII)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
- category: Product
  description: Quarterly data extracts in XML format adhering to ICH E2B standards
    for international safety reporting
  format: xml
  id: faers.quarterly_data_xml
  latest_version: 2026Q1
  name: FAERS Quarterly Data Files (XML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
- category: DocumentationProduct
  description: Frequently asked questions about FAERS data structure, reporting requirements,
    and data usage
  format: http
  id: faers.faq
  name: FAERS FAQ
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  product_url: https://fis.fda.gov/extensions/FPD-FAQ/FPD-FAQ.html
- category: GraphicalInterface
  description: Portal for submitting adverse event reports electronically to the FDA
  format: http
  id: faers.electronic_submissions
  name: FAERS Electronic Submissions Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  product_url: https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-electronic-submissions
- category: Product
  description: Standardized and deduplicated version of FDA FAERS data with drug names
    mapped to RxNorm and adverse event outcomes mapped to SNOMED-CT, including pre-computed
    summary statistics for drug-outcome relationships.
  id: aeolus.standardized_data
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: AEOLUS Standardized FAERS Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: aeolus
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.8q0s4
- category: GraphProduct
  description: GP-KG tab-delimited knowledge graph containing 1,246,726 associations
    between 61,146 entities from multiple genotypic and phenotypic databases
  format: tsv
  id: kg-predict.gpkg
  name: GP-KG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: umls
- category: GraphProduct
  description: GP_KG.txt
  edge_count: 1246726
  id: gp-kg.graph
  name: GP-KG
  node_count: 61146
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gp-kg
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: goa
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: phenomebrowser
  - relation_type: prov:wasDerivedFrom
    source: treatkb
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
synonyms:
- AEMS
- FDA Adverse Event Monitoring System
- FAERS
- FDA Adverse Event Reporting System
taxon:
- NCBITaxon:9606
---
# FDA Adverse Event Reporting System

## Overview

The FDA Adverse Event Reporting System (FAERS) is a comprehensive database maintained by the FDA Center for Drug Evaluation and Research (CDER) that collects and analyzes adverse event reports, medication error reports, and product quality complaints for drug and therapeutic biologic products. The system is a critical component of the FDA's post-marketing safety surveillance program, enabling ongoing monitoring of drug safety after products reach the market.

## Data Content

FAERS contains reports from multiple sources:
- Healthcare professionals (physicians, pharmacists, nurses)
- Consumers
- Pharmaceutical manufacturers (mandatory reporting)
- Legal representatives

### Data Structure

The FAERS database follows the ICH E2B international safety reporting standard and includes:
- **Demographic and administrative information**: Patient age, sex, weight, report dates
- **Drug information**: Name, dose, route, indication, therapy dates
- **Adverse event information**: MedDRA-coded reactions, outcomes, seriousness
- **Reporter information**: Source type, qualifications
- **Narrative descriptions**: Event details and outcomes

All adverse events are coded using MedDRA (Medical Dictionary for Regulatory Activities) terminology, enabling standardized analysis and international data exchange.

## Data Products

### Quarterly Data Files
FAERS provides complete data extracts on a quarterly basis:
- **Available from**: 2012-present (with archives for earlier data)
- **Formats**: ASCII and XML (SGML for older files)
- **Update frequency**: Quarterly (posted ~30-60 days after quarter end)
- **Most recent**: Q1 2026 (January-March 2026, posted April 28, 2026)

### Public Dashboard
Interactive web-based dashboard providing:
- Searchable database of adverse event reports
- Visualization tools for trend analysis
- Summary statistics and aggregated data views
- Export capabilities for further analysis

## Use Cases

1. **Pharmacovigilance**: Post-marketing surveillance and signal detection
2. **Drug Safety Research**: Studying patterns of adverse events
3. **Regulatory Science**: Supporting FDA safety assessments and label updates
4. **Comparative Effectiveness Research**: Analyzing real-world drug outcomes
5. **Clinical Decision Support**: Informing prescribing decisions
6. **Public Health Monitoring**: Tracking medication error trends

## Related Resources

- **AEOLUS**: A cleaned and standardized version of FAERS with duplicate removal, RxNorm drug mapping, and SNOMED-CT outcome mapping
- **nSIDES**: Machine learning-based adverse drug event databases including OnSIDES, OffSIDES, and TwoSIDES
- **AERO**: Adverse Event Reporting Ontology for standardizing adverse event data entry

## Information Resource ID

This resource has the Information Resource identifier: `infores:faers`

## Important Notes

- FAERS data cannot prove that a drug caused an adverse event; reports reflect suspicions of healthcare providers and consumers
- Reporting biases exist: serious events, new drugs, and heavily marketed drugs may be over-represented
- Duplicate reports may exist despite FDA efforts to remove them
- Individual case reports are available through FOIA requests
- The database does not include denominators (total number of people taking drugs), limiting causal inference