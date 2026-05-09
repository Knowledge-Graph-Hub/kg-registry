---
layout: schema_doc
mermaid: true
---

# Enum: DomainEnum




_A domain that a resource is relevant to._



URI: [kgr:DomainEnum](https://w3id.org/bridge2ai/data-sheets-schema/DomainEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| agriculture | None | The agricultural sciences |
| anatomy and development | None | The anatomy and development of organisms |
| biological systems | None | The biological sciences and systems |
| biomedical | None | The biomedical sciences, including the study of biological systems and their ... |
| chemistry and biochemistry | None | The chemical and biochemical sciences |
| clinical | None | The clinical sciences, including clinical trials and patient data |
| digital health | None | The use of digital technologies for healthcare, including telemedicine, weara... |
| drug discovery | None | The process of identifying and developing new candidate medications, includin... |
| environment | None | The environment and ecosystems |
| general | None | A general domain, not specific to any other category |
| genomics | None | The study of genomes, including genome structure, evolution,  function, mappi... |
| health | None | The health and diseases of organisms |
| immunology | None | The study of the immune system, including its structure and function, disorde... |
| information technology | None | The information technology sciences |
| investigations | None | Research investigations into specific topics |
| literature | None | The literature and publications of a domain |
| medical imaging | None | Techniques and processes for creating visual representations of the interior ... |
| microbiome | None | The study of microbial communities, their genomes, and their influence on hos... |
| microbiology | None | The microbiological sciences |
| neuroscience | None | The scientific study of the nervous system, including  brain structure, funct... |
| nutrition | None | The nutritional sciences, including diet and metabolomics |
| organisms | None | Specific organisms |
| other | None | Another domain not defined here |
| pathways | None | Biological pathways, including metabolic, signaling, and regulatory networks ... |
| pharmacology | None | The study of how drugs interact with biological systems, including  drug disc... |
| phenotype | None | The phenotypes of organisms |
| precision medicine | None | An approach to disease treatment and prevention that takes into account indiv... |
| proteomics | None | The large-scale study of proteins, their structures,  functions, and interact... |
| public health | None | The science of protecting and improving the health of people and their  commu... |
| simulation | None | Simulation and modeling of specific phenomena |
| social determinants | None | The social, economic, and environmental factors that influence health outcome... |
| systems biology | None | The computational and mathematical analysis of complex biological systems and... |
| synthetic biology | None | The design and construction of new biological parts, devices, and systems, or... |
| toxicology | None | The study of the adverse effects of chemicals on living organisms |
| translational | None | The translational sciences, including the translation of research into practi... |
| upper | None | The upper-level domain, for general-purpose data representation and integrati... |
| food science | None | The study of food, including its production, processing, preservation, and co... |
| plant science | None | The study of plants, including their biology, ecology, and interactions with ... |
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
description: A domain that a resource is relevant to.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  agriculture:
    text: agriculture
    description: The agricultural sciences.
  anatomy and development:
    text: anatomy and development
    description: The anatomy and development of organisms.
  biological systems:
    text: biological systems
    description: The biological sciences and systems.
  biomedical:
    text: biomedical
    description: The biomedical sciences, including the study of biological systems
      and their interactions.
  chemistry and biochemistry:
    text: chemistry and biochemistry
    description: The chemical and biochemical sciences.
  clinical:
    text: clinical
    description: The clinical sciences, including clinical trials and patient data.
  digital health:
    text: digital health
    description: The use of digital technologies for healthcare, including telemedicine,
      wearable devices, health information technology, and personalized medicine.
  drug discovery:
    text: drug discovery
    description: The process of identifying and developing new candidate medications,
      including target identification, validation, and compound screening.
  environment:
    text: environment
    description: The environment and ecosystems.
  general:
    text: general
    description: A general domain, not specific to any other category. It concerns
      resources that are broadly applicable across multiple domains.
  genomics:
    text: genomics
    description: The study of genomes, including genome structure, evolution,  function,
      mapping, and editing.
  health:
    text: health
    description: The health and diseases of organisms.
  immunology:
    text: immunology
    description: The study of the immune system, including its structure and function,
      disorders, and therapeutic applications.
  information technology:
    text: information technology
    description: The information technology sciences.
  investigations:
    text: investigations
    description: Research investigations into specific topics.
  literature:
    text: literature
    description: The literature and publications of a domain.
  medical imaging:
    text: medical imaging
    description: Techniques and processes for creating visual representations of the
      interior of a body for clinical analysis and medical intervention.
  microbiome:
    text: microbiome
    description: The study of microbial communities, their genomes, and their influence
      on hosts and environments.
  microbiology:
    text: microbiology
    description: The microbiological sciences.
  neuroscience:
    text: neuroscience
    description: The scientific study of the nervous system, including  brain structure,
      function, and disorders.
  nutrition:
    text: nutrition
    description: The nutritional sciences, including diet and metabolomics.
  organisms:
    text: organisms
    description: Specific organisms.
  other:
    text: other
    description: Another domain not defined here.
  pathways:
    text: pathways
    description: Biological pathways, including metabolic, signaling, and regulatory
      networks that control cellular processes.
  pharmacology:
    text: pharmacology
    description: The study of how drugs interact with biological systems, including  drug
      discovery, development, and therapeutic uses.
  phenotype:
    text: phenotype
    description: The phenotypes of organisms.
  precision medicine:
    text: precision medicine
    description: An approach to disease treatment and prevention that takes into account
      individual variability in genes, environment, and lifestyle.
  proteomics:
    text: proteomics
    description: The large-scale study of proteins, their structures,  functions,
      and interactions.
  public health:
    text: public health
    description: The science of protecting and improving the health of people and
      their  communities, including epidemiology and population health.
  simulation:
    text: simulation
    description: Simulation and modeling of specific phenomena.
  social determinants:
    text: social determinants
    description: The social, economic, and environmental factors that influence health
      outcomes and contribute to health disparities.
  systems biology:
    text: systems biology
    description: The computational and mathematical analysis of complex biological
      systems and their interactions.
  synthetic biology:
    text: synthetic biology
    description: The design and construction of new biological parts, devices, and
      systems, or the redesign of existing natural biological systems.
  toxicology:
    text: toxicology
    description: The study of the adverse effects of chemicals on living organisms.
  translational:
    text: translational
    description: The translational sciences, including the translation of research
      into practice.
  upper:
    text: upper
    description: The upper-level domain, for general-purpose data representation and
      integration.
  food science:
    text: food science
    description: The study of food, including its production, processing, preservation,
      and consumption.
  plant science:
    text: plant science
    description: The study of plants, including their biology, ecology, and interactions
      with the environment.
  stub:
    text: stub
    description: This is not a domain, but rather a category for resources that are
      not yet categorized and exist only as a placeholder.

```
</details>
