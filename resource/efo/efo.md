---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: efo-users@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/spot/ontology/
  label: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)
description: The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for projects such as the GWAS catalog. It combines parts of several biological ontologies, such as UBERON anatomy, ChEBI chemical compounds, and Cell Ontology.
domains:
- biological systems
- biomedical
- health
- phenotype
homepage_url: https://www.ebi.ac.uk/efo/
id: efo
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache 2.0
name: Experimental Factor Ontology
repository: https://github.com/EBISPOT/efo
publications:
- id: https://doi.org/10.1093/bioinformatics/btq099
  title: Modeling Sample Variables with an Experimental Factor Ontology
  preferred: true
  authors:
  - James Malone
  - Ele Holloway
  - Tomasz Adamusiak
  - Misha Kapushesky
  - Jie Zheng
  - Nikolay Kolesnikov
  - Anna Zhukova
  - Alvis Brazma
  - Helen Parkinson
  journal: Bioinformatics
  year: "2010"
  doi: doi:10.1093/bioinformatics/btq099
products:
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - efo
  product_url: https://www.ebi.ac.uk/efo/efo.owl
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - efo
  product_url: https://www.ebi.ac.uk/efo/efo.obo
- category: GraphicalInterface
  description: Browse EFO with EBI's Ontology Lookup Service (OLS)
  format: http
  id: efo.ols
  name: EFO in OLS
  original_source:
  - efo
  product_url: https://www.ebi.ac.uk/ols/ontologies/efo
---

# Experimental Factor Ontology

The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases and for projects such as the NHGRI-EBI GWAS catalog. It combines parts of several biological ontologies, such as UBERON anatomy, ChEBI chemical compounds, Cell Ontology, and most recently, the Monarch Disease Ontology (MONDO).

The scope of EFO is to support the annotation, analysis, and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets. EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT). 

EFO has undergone significant restructuring in version 3, particularly in the disease branch, to improve classification based on current medical understanding and alignment with existing domain ontologies. This was achieved through mapping the EFO disease and disease staging branches to the Monarch Disease Ontology (MONDO).

EFO is actively maintained with regular releases available through its GitHub repository. It is widely used in biomedical resources including:

- Open Targets platform
- Gene Expression Atlas
- ArrayExpress
- And many other EBI databases and external resources

Users can browse EFO through the EBI's Ontology Lookup Service (OLS), submit new terms through GitHub issues, and download the latest release in various formats including OWL and OBO.