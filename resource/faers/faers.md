---
activity_status: active
category: DataSource
creation_date: '2025-11-04T00:00:00Z'
description: The FDA Adverse Event Reporting System (FAERS) is a database that contains adverse event reports, medication error reports, and product quality complaints resulting in adverse events submitted to the FDA. FAERS supports the FDA's post-marketing safety surveillance program for drug and therapeutic biologic products. The database adheres to ICH E2B international safety reporting guidance, and adverse events are coded using MedDRA (Medical Dictionary for Regulatory Activities) terminology. FAERS provides quarterly data files in ASCII and XML formats dating back to 2012, with archives available for earlier data.
domains:
  - pharmacology
  - drug discovery
  - clinical
  - public health
id: "faers"
infores_id: "faers"
last_modified_date: '2025-11-04T00:00:00Z'
layout: resource_detail
name: FDA Adverse Event Reporting System
homepage_url: https://www.fda.gov/drugs/surveillance/fdas-adverse-event-reporting-system-faers
contacts:
  - category: Organization
    label: FDA Center for Drug Evaluation and Research
    contact_details:
      - contact_type: email
        value: FDA-SRS@fda.hhs.gov
products:
  - id: "faers.public_dashboard"
    category: GraphicalInterface
    name: FAERS Public Dashboard
    description: Interactive dashboard for exploring FAERS data with visualizations and search capabilities
    product_url: https://fis.fda.gov/sense/app/95239e26-e0be-42d9-a960-9a5f7f1c25ee/sheet/7a47a261-d58b-4203-a8aa-6d3021737452/state/analysis
    format: http
    original_source:
      - faers
  - id: faers.quarterly_data_ascii
    category: Product
    name: FAERS Quarterly Data Files (ASCII)
    description: Quarterly data extracts in ASCII format containing demographic, drug, reaction, outcome, and source information for reported adverse events
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    format: txt
    original_source:
      - faers
  - id: "faers.quarterly_data_xml"
    category: Product
    name: FAERS Quarterly Data Files (XML)
    description: Quarterly data extracts in XML format adhering to ICH E2B standards for international safety reporting
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    format: xml
    original_source:
      - faers
  - id: "faers.faq"
    category: DocumentationProduct
    name: FAERS FAQ
    description: Frequently asked questions about FAERS data structure, reporting requirements, and data usage
    product_url: https://fis.fda.gov/extensions/FPD-FAQ/FPD-FAQ.html
    format: http
    original_source:
      - faers
  - id: "faers.electronic_submissions"
    category: GraphicalInterface
    name: FAERS Electronic Submissions Portal
    description: Portal for submitting adverse event reports electronically to the FDA
    product_url: https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-electronic-submissions
    format: http
    original_source:
      - faers
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
- **Most recent**: Q3 2025 (July-September 2025, posted October 30, 2025)

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
