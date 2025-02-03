---
layout: resource_detail
activity_status: active
id: rhea
name: Rhea, the Annotated Reactions Database
description: Rhea is an expert-curated knowledgebase of chemical and transport reactions
  of biological interest
domain: chemistry and biochemistry
contact:
  orcid: 0000-0003-4423-4370
  github: cthoyt
  email: cthoyt@gmail.com
  label: Charles Tapley Hoyt
url: https://biopragmatics.github.io/obo-db-ingest/
tracker: https://github.com/biopragmatics/pyobo/issues
repository: https://github.com/biopragmatics/obo-db-ingest
products:
- id: rhea.owl
  name: Rhea, the Annotated Reactions Database OWL release
  description: OWL release of Rhea, the Annotated Reactions Database
  tags:
    - biopragmatics
  url: https://w3id.org/biopragmatics/resources/rhea/rhea.owl
  category: Product
- id: rhea.obo
  name: Rhea, the Annotated Reactions Database OBO release
  description: OBO release of Rhea, the Annotated Reactions Database
  tags:
    - biopragmatics
  url: https://w3id.org/biopragmatics/resources/rhea/rhea.obo
  category: Product
- id: rhea.sssom
  name: Rhea, the Annotated Reactions Database SSSOM release
  description: SSSOM release of Rhea, the Annotated Reactions Database
  tags:
    - biopragmatics
  url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom
  category: Product
uri_prefix: http://purl.obolibrary.org/obo/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
category: DataGraph
---

Rhea is an expert-curated knowledgebase of chemical and transport reactions of biological interest. Enzyme-catalyzed and spontaneously occurring reactions are curated from peer-reviewed literature and represented in a computationally tractable manner by using the ChEBI (Chemical Entities of Biological Interest) ontology to describe reaction participants.

Rhea covers the reactions described by the IUBMB Enzyme Nomenclature as well as many additional reactions and can be used for enzyme annotation, genome-scale metabolic modeling and omics-related analyses. Rhea is the standard for enzyme and transporter annotation in UniProtKB.
