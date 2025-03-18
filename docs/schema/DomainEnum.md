---
layout: schema_doc
mermaid: true
---

# Enum: DomainEnum




_The domain that a resource is most relevant to._



URI: [DomainEnum](DomainEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| upper | None | The upper-level domain, for general-purpose data representation and integrati... |
| anatomy and development | None | The anatomy and development of organisms |
| health | None | The health and diseases of organisms |
| phenotype | None | The phenotypes of organisms |
| investigations | None | Research investigations into specific topics |
| environment | None | The environment and ecosystems |
| chemistry and biochemistry | None | The chemical and biochemical sciences |
| microbiology | None | The microbiological sciences |
| agriculture | None | The agricultural sciences |
| nutrition | None | The nutritional sciences, including diet and metabolomics |
| biological systems | None | The biological sciences and systems |
| information technology | None | The information technology sciences |
| organisms | None | Specific organisms |
| simulation | None | Simulation and modeling of specific phenomena |
| other | None | Another domain not defined here |




## Slots

| Name | Description |
| ---  | --- |
| [domain](domain.html) | The domain that the resource is relevant to |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: DomainEnum
description: The domain that a resource is most relevant to.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  upper:
    text: upper
    description: The upper-level domain, for general-purpose data representation and
      integration.
  anatomy and development:
    text: anatomy and development
    description: The anatomy and development of organisms.
  health:
    text: health
    description: The health and diseases of organisms.
  phenotype:
    text: phenotype
    description: The phenotypes of organisms.
  investigations:
    text: investigations
    description: Research investigations into specific topics.
  environment:
    text: environment
    description: The environment and ecosystems.
  chemistry and biochemistry:
    text: chemistry and biochemistry
    description: The chemical and biochemical sciences.
  microbiology:
    text: microbiology
    description: The microbiological sciences.
  agriculture:
    text: agriculture
    description: The agricultural sciences.
  nutrition:
    text: nutrition
    description: The nutritional sciences, including diet and metabolomics.
  biological systems:
    text: biological systems
    description: The biological sciences and systems.
  information technology:
    text: information technology
    description: The information technology sciences.
  organisms:
    text: organisms
    description: Specific organisms.
  simulation:
    text: simulation
    description: Simulation and modeling of specific phenomena.
  other:
    text: other
    description: Another domain not defined here.

```
</details>
