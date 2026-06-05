---
layout: schema_doc
mermaid: true
---

# Enum: DomainEnum




_A domain that a resource is relevant to. Each domain maps, where possible, to a concept in an external controlled vocabulary (Medical Subject Headings, MeSH; or the NCI Thesaurus, NCIT) via the permissible value's `meaning`._



URI: [kgr:DomainEnum](https://w3id.org/bridge2ai/data-sheets-schema/DomainEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| agriculture | MESH:D000383 | The agricultural and food sciences, including crop and animal production, pla... |
| anatomy and development | MESH:D000715 | The anatomy and development of organisms, including their structure, morpholo... |
| biological systems | MESH:D001690 | The biological sciences broadly, including cellular and molecular biology and... |
| biomedical | MESH:D035843 | The biomedical sciences broadly, spanning the study of biological systems in ... |
| chemistry and biochemistry | MESH:D002621 | The chemical and biochemical sciences, including the structure, properties, a... |
| clinical | MESH:D015510 | The clinical sciences concerned with the care of patients, including clinical... |
| drug discovery | MESH:D055808 | The process of identifying and developing new candidate medications, includin... |
| environment | MESH:D004777 | The environment and ecosystems, including ecology and environmental health |
| general | None | A general domain, not specific to any other category |
| genomics | MESH:D023281 | The study of genomes, including genome structure, evolution, function, mappin... |
| immunology | MESH:D000486 | The study of the immune system, including its structure and function, disorde... |
| information technology | MESH:D000073256 | The information technology and informatics sciences, including software, comp... |
| literature | MESH:D011642 | The literature and publications of a domain |
| medical imaging | MESH:D003952 | Techniques and processes for creating visual representations of the interior ... |
| microbiology | MESH:D008829 | The microbiological sciences, including the study of microbial communities (m... |
| neuroscience | MESH:D009488 | The scientific study of the nervous system, including brain structure, functi... |
| nutrition | MESH:D052756 | The nutritional sciences, including diet and metabolomics |
| organisms | NCIT:C14250 | Specific organisms or taxa |
| other | None | Another domain not defined here |
| pathways | MESH:D053858 | Biological pathways, including metabolic, signaling, and regulatory networks ... |
| pharmacology | MESH:D010600 | The study of how drugs interact with biological systems, including drug disco... |
| phenotype | MESH:D010641 | The phenotypes of organisms |
| precision medicine | MESH:D057285 | An approach to disease treatment and prevention that takes into account indiv... |
| proteomics | MESH:D040901 | The large-scale study of proteins, their structures, functions, and interacti... |
| public health | MESH:D011634 | The science of protecting and improving the health of people and their commun... |
| systems biology | MESH:D049490 | The computational and mathematical analysis of complex biological systems and... |
| toxicology | MESH:D014116 | The study of the adverse effects of chemicals on living organisms |
| stub | None | This is not a domain, but rather a category for resources that are not yet ca... |




## Slots

| Name | Description |
| ---  | --- |
| [domains](domains.html) | The domain(s) that the resource is relevant to |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: DomainEnum
description: A domain that a resource is relevant to. Each domain maps, where possible,
  to a concept in an external controlled vocabulary (Medical Subject Headings, MeSH;
  or the NCI Thesaurus, NCIT) via the permissible value's `meaning`.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  agriculture:
    text: agriculture
    description: The agricultural and food sciences, including crop and animal production,
      plant science, and food production, processing, and preservation.
    meaning: MESH:D000383
  anatomy and development:
    text: anatomy and development
    description: The anatomy and development of organisms, including their structure,
      morphology, and developmental biology.
    meaning: MESH:D000715
  biological systems:
    text: biological systems
    description: The biological sciences broadly, including cellular and molecular
      biology and other biological disciplines not better described by a more specific
      domain.
    meaning: MESH:D001690
  biomedical:
    text: biomedical
    description: The biomedical sciences broadly, spanning the study of biological
      systems in the context of health and disease. Use a more specific domain (e.g.,
      clinical) where one applies.
    meaning: MESH:D035843
  chemistry and biochemistry:
    text: chemistry and biochemistry
    description: The chemical and biochemical sciences, including the structure, properties,
      and reactions of chemical compounds.
    meaning: MESH:D002621
  clinical:
    text: clinical
    description: The clinical sciences concerned with the care of patients, including
      clinical trials, patient data, and diagnosis and treatment of disease.
    meaning: MESH:D015510
  drug discovery:
    text: drug discovery
    description: The process of identifying and developing new candidate medications,
      including target identification, validation, and compound screening.
    meaning: MESH:D055808
  environment:
    text: environment
    description: The environment and ecosystems, including ecology and environmental
      health.
    meaning: MESH:D004777
  general:
    text: general
    description: A general domain, not specific to any other category. It concerns
      resources that are broadly applicable across multiple domains, including upper-level
      and cross-domain resources.
  genomics:
    text: genomics
    description: The study of genomes, including genome structure, evolution, function,
      mapping, and editing.
    meaning: MESH:D023281
  immunology:
    text: immunology
    description: The study of the immune system, including its structure and function,
      disorders, and therapeutic applications.
    meaning: MESH:D000486
  information technology:
    text: information technology
    description: The information technology and informatics sciences, including software,
      computational methods, simulation and modeling, and digital health technologies.
    meaning: MESH:D000073256
  literature:
    text: literature
    description: The literature and publications of a domain.
    meaning: MESH:D011642
  medical imaging:
    text: medical imaging
    description: Techniques and processes for creating visual representations of the
      interior of a body for clinical analysis and medical intervention.
    meaning: MESH:D003952
  microbiology:
    text: microbiology
    description: The microbiological sciences, including the study of microbial communities
      (microbiomes) and their influence on hosts and environments.
    meaning: MESH:D008829
  neuroscience:
    text: neuroscience
    description: The scientific study of the nervous system, including brain structure,
      function, and disorders.
    meaning: MESH:D009488
  nutrition:
    text: nutrition
    description: The nutritional sciences, including diet and metabolomics.
    meaning: MESH:D052756
  organisms:
    text: organisms
    description: Specific organisms or taxa.
    meaning: NCIT:C14250
  other:
    text: other
    description: Another domain not defined here.
  pathways:
    text: pathways
    description: Biological pathways, including metabolic, signaling, and regulatory
      networks that control cellular processes.
    meaning: MESH:D053858
  pharmacology:
    text: pharmacology
    description: The study of how drugs interact with biological systems, including
      drug discovery, development, and therapeutic uses.
    meaning: MESH:D010600
  phenotype:
    text: phenotype
    description: The phenotypes of organisms.
    meaning: MESH:D010641
  precision medicine:
    text: precision medicine
    description: An approach to disease treatment and prevention that takes into account
      individual variability in genes, environment, and lifestyle.
    meaning: MESH:D057285
  proteomics:
    text: proteomics
    description: The large-scale study of proteins, their structures, functions, and
      interactions.
    meaning: MESH:D040901
  public health:
    text: public health
    description: The science of protecting and improving the health of people and
      their communities, including epidemiology, population health, and the social
      determinants of health.
    meaning: MESH:D011634
  systems biology:
    text: systems biology
    description: The computational and mathematical analysis of complex biological
      systems and their interactions.
    meaning: MESH:D049490
  toxicology:
    text: toxicology
    description: The study of the adverse effects of chemicals on living organisms.
    meaning: MESH:D014116
  stub:
    text: stub
    description: This is not a domain, but rather a category for resources that are
      not yet categorized and exist only as a placeholder.

```
</details>
