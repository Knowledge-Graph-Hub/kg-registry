---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: ols-support@ebi.ac.uk
      - contact_type: github
        value: EBISPOT
      - contact_type: url
        value: https://www.ebi.ac.uk/spot/oxo/contact
    id: ebi
    label: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)
creation_date: '2025-11-04T00:00:00Z'
description: OxO (Ontology Xref Service) is a cross-ontology mapping service developed by EMBL-EBI's Samples, Phenotypes and Ontologies Team (SPOT). The current version, OxO2, is an SSSOM-compliant reimplementation that is backwards compatible with OxO version 1. It aggregates mappings extracted from ontologies loaded in the Ontology Lookup Service (OLS) together with curated SSSOM mapping sets (e.g., Mondo, Uberon, uPheno, IMPC/MGI mouse-human mappings, Bioregistry, Biomappings, SeMRA, and EBI text-to-ontology mappings), and generates SSSOM-based cross-set inferred mappings. Mappings can be searched through a web interface and a REST API.
domains:
  - biomedical
  - general
  - biological systems
homepage_url: https://www.ebi.ac.uk/spot/oxo/
id: oxo
infores_id: oxo
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: Ontology Xref Service
products:
  - category: GraphicalInterface
    description: OxO2 web interface for searching and browsing ontology cross-references and SSSOM mappings, including asserted mappings from OLS ontologies and curated mapping sets, plus inferred cross-set mappings
    format: http
    id: oxo.portal
    name: OxO Web Interface
    original_source:
      - source: oxo
        relation_type: prov:hadPrimarySource
      - source: ols
        relation_type: prov:hadPrimarySource
      - source: bioregistry
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: upheno
        relation_type: prov:hadPrimarySource
      - source: impc
        relation_type: prov:hadPrimarySource
      - source: mgi
        relation_type: prov:hadPrimarySource
      - source: monarchinitiative
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: biomappings
        relation_type: prov:hadPrimarySource
      - source: semra
        relation_type: prov:hadPrimarySource
    product_url: https://www.ebi.ac.uk/spot/oxo/
  - category: ProgrammingInterface
    connection_url: https://www.ebi.ac.uk/spot/oxo/api/v2
    description: OxO2 REST API (OpenAPI 3) for querying mappings, mapping sets, and ontologies; supports SSSOM-shaped JSON and SSSOM TSV export of mapping search results. Also exposes legacy OxO v1-compatible endpoints.
    format: http
    id: oxo.api
    is_public: true
    name: OxO2 REST API
    original_source:
      - source: oxo
        relation_type: prov:hadPrimarySource
      - source: ols
        relation_type: prov:hadPrimarySource
      - source: bioregistry
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: upheno
        relation_type: prov:hadPrimarySource
      - source: impc
        relation_type: prov:hadPrimarySource
      - source: mgi
        relation_type: prov:hadPrimarySource
      - source: monarchinitiative
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: biomappings
        relation_type: prov:hadPrimarySource
      - source: semra
        relation_type: prov:hadPrimarySource
    product_url: https://www.ebi.ac.uk/spot/oxo/swagger-ui.html
repository: https://github.com/EBISPOT/oxo2
synonyms:
  - OxO
  - OxO2
---

# Ontology Xref Service (OxO)

## Overview

OxO (Ontology Xref Service) is a service developed and maintained by EMBL-EBI's Samples, Phenotypes and Ontologies Team (SPOT) for cross-ontology term mapping. The service facilitates the discovery of mappings between terms from different ontological resources, enabling data integration and interoperability across biomedical databases and tools.

The service currently deployed at [https://www.ebi.ac.uk/spot/oxo/](https://www.ebi.ac.uk/spot/oxo/) is **OxO2**, an [SSSOM](https://mapping-commons.github.io/sssom/)-compliant reimplementation of OxO that is backwards compatible with OxO version 1. As of October 2026 (data release 2026-10-26), OxO2 serves roughly 26.6 million mappings (11.5 million asserted, 15.1 million inferred) from 366 mapping sets (299 ontology-derived and 67 curated sets).

## Data Sources

OxO2 aggregates mapping data from:
- **Ontologies in the Ontology Lookup Service (OLS)**: cross-references and mappings extracted from ~300 ontologies (e.g., EFO, MONDO, HP, MP, UBERON, CL, GO, ChEBI, NCIT, DOID, ORDO).
- **Curated SSSOM mapping sets**, including:
  - Mondo mapping sets (e.g., Mondo to ICD-10-CM, Mondo to HP)
  - Uberon core mappings and uPheno cross-species phenotype mappings
  - Mouse-human mappings from the SSSOM mapping commons (IMPC and MGI MP-HP mappings, Pistoia Alliance mappings)
  - Monarch mapping commons sets (e.g., LOINC to ChEBI/GO/Uberon/CL/PR/NCBITaxon, HPO to SNOMED, gene mappings)
  - Bioregistry, Biomappings, and SeMRA mapping databases
  - OMOP2OBO mappings
  - EBI text-to-ontology mappings for projects such as the GWAS Catalog, Open Targets, UK Biobank, ClinVar/EVA, Human Cell Atlas, MetaboLights, and others
- **Inferred mappings**: OxO2 computes SSSOM cross-set inferences; asserted mappings are ranked above inferred ones, and shorter inference chains rank higher.

## Access

- **Web interface**: [https://www.ebi.ac.uk/spot/oxo/](https://www.ebi.ac.uk/spot/oxo/)
- **REST API**: endpoints rooted at `https://www.ebi.ac.uk/spot/oxo/api/v2`, documented via Swagger UI at [https://www.ebi.ac.uk/spot/oxo/swagger-ui.html](https://www.ebi.ac.uk/spot/oxo/swagger-ui.html) (OpenAPI spec at `https://www.ebi.ac.uk/spot/oxo/v3/api-docs`). Mapping search results can be exported as SSSOM TSV.
- **Source code**: [https://github.com/EBISPOT/oxo2](https://github.com/EBISPOT/oxo2) (Apache License 2.0)

## Related Services

OxO is part of the SPOT suite of ontology services at EMBL-EBI:
- **OLS (Ontology Lookup Service)**: Repository and browser for biomedical ontologies
- **ZOOMA**: Service for mapping free-text annotations to ontology terms

## Information Resource ID

This resource has the Information Resource identifier: `infores:oxo`

## Contact and Support

For questions or issues regarding OxO:
- **Email**: ols-support@ebi.ac.uk
- **Issue tracker**: [https://github.com/EBISPOT/oxo2/issues](https://github.com/EBISPOT/oxo2/issues)
- **Organization**: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)

## Use Cases

1. **Data Integration**: Mapping identifiers when merging datasets using different ontologies
2. **Ontology Alignment**: Finding equivalent terms for ontology harmonization projects
3. **Cross-Database Queries**: Translating queries across databases using different terminologies
4. **Semantic Interoperability**: Enabling communication between systems using different vocabularies
