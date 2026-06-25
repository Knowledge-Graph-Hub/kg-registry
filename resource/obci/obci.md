---
activity_status: active
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: dan5@georgetown.edu
  - contact_type: github
    value: nataled
  label: Darren A. Natale
  orcid: 0000-0001-5809-9523
creation_date: '2026-06-18T00:00:00Z'
description: An OWL-formatted ontology that formally defines biomarkers of clinical
  interest for diseases, phenotypes, and effects, including the FDA-NIH BEST-aligned
  biomarker role classifications (diagnostic, prognostic, predictive, monitoring,
  pharmacodynamic/response, safety, and susceptibility/risk biomarkers). OBCI is developed
  by the clinical-biomarkers group associated with the GlyGen and OncoMX biomarker
  data resources, and supplies the "role" / best-classification vocabulary used by
  downstream biomarker knowledge graphs.
domains:
- biomedical
- clinical
- precision medicine
homepage_url: https://github.com/clinical-biomarkers/OBCI
id: obci
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Ontology for Biomarkers of Clinical Interest
products:
- category: OntologyProduct
  description: Ontology for Biomarkers of Clinical Interest, OWL format. Defines biomarker
    classes and their clinical role classifications (e.g. diagnostic, prognostic,
    predictive, monitoring, pharmacodynamic/response, safety, susceptibility/risk
    biomarkers).
  format: owl
  id: obci.owl
  name: OBCI, OWL format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obci
  product_file_size: 195392
  product_url: https://proteininformationresource.org/staff/nataled/OBCI/obci.owl
- category: GraphProduct
  compression: zip
  description: Nodes from OBCI
  format: csv
  id: biomarkerkg.nodes.role
  name: BKG Role Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarkerkg
  - relation_type: prov:hadPrimarySource
    source: obci
  product_file_size: 276
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Role.nodes.zip
- category: GraphProduct
  compression: zip
  description: Biomarker to Role relationships (has_best_classification)
  format: csv
  id: biomarkerkg.edges.role
  name: BKG Role Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarkerkg
  - relation_type: prov:hadPrimarySource
    source: obci
  product_file_size: 355306
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Role.edges.zip
repository: https://github.com/clinical-biomarkers/OBCI
---
The Ontology for Biomarkers of Clinical Interest (OBCI) is an OWL-formatted ontology that formally defines biomarkers for diseases, phenotypes, and effects. It is developed and maintained by the clinical-biomarkers group, the same community responsible for the GlyGen and OncoMX biomarker data resources.

OBCI organizes biomarkers both by their molecular and anatomical characteristics (for example, genetic variation biomarkers, RNA biomarkers, small molecule biomarkers, blood plasma biomarkers, and urine biomarkers) and by their clinical role. The role classifications follow the FDA-NIH BEST (Biomarkers, EndpointS, and other Tools) framework and include diagnostic, monitoring, pharmacodynamic/response, predictive, prognostic, safety, and susceptibility/risk biomarkers. These role classes are the source of the "best classification" / role vocabulary consumed by downstream biomarker knowledge graphs such as the BiomarkerKG (BKG), which links each biomarker to its best classification via a `has_best_classification` relationship.

The ontology is distributed in OWL format and is registered in the Bioregistry under the prefix `obci`. As of the OBCI 2024-10-18 release, the ontology declares the IRI `http://purl.obolibrary.org/obo/obci.owl` and is in the process of OBO Foundry submission, though that PURL is not yet resolving; the authoritative download is hosted at the Protein Information Resource.