---
layout: schema_doc
mermaid: true
---

# Enum: CollectionEnum




_Specific collections for grouping KG-Registry entries._



URI: [kgr:CollectionEnum](https://w3id.org/bridge2ai/data-sheets-schema/CollectionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| aop | https://aopwiki.org/ | This entity incorporates the Adverse Outcome Pathways (AOP) framework in some... |
| ber | https://www.energy.gov/science/ber/biological-and-environmental-research | A resource or product relevant to the US Department of Energy Biological and ... |
| omop | https://ohdsi.github.io/CommonDataModel/ | This entity is part of the OMOP Common Data Model ecosystem, including vocabu... |
| translator | https://ncats.nih.gov/research/research-activities/translator | This entity is part of those developed and used by the NCATS Biomedical Trans... |
| obo-foundry | https://obofoundry.org/ | This entity is an ontology from the OBO Foundry, a collaborative effort to cr... |
| okn | https://www.proto-okn.net/ | This entity is part of the Prototype Open Knowledge Network (OKN), a knowledg... |




## Slots

| Name | Description |
| ---  | --- |
| [collection](collection.html) | A collection of entries in the registry |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: CollectionEnum
description: Specific collections for grouping KG-Registry entries.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  aop:
    text: aop
    description: This entity incorporates the Adverse Outcome Pathways (AOP) framework
      in some manner.
    meaning: https://aopwiki.org/
  ber:
    text: ber
    description: A resource or product relevant to the US Department of Energy Biological
      and Environmental Research (BER) program.
    meaning: https://www.energy.gov/science/ber/biological-and-environmental-research
  omop:
    text: omop
    description: This entity is part of the OMOP Common Data Model ecosystem, including
      vocabularies and related standards used in OHDSI workflows.
    meaning: https://ohdsi.github.io/CommonDataModel/
  translator:
    text: translator
    description: This entity is part of those developed and used by the NCATS Biomedical
      Translator program.
    meaning: https://ncats.nih.gov/research/research-activities/translator
  obo-foundry:
    text: obo-foundry
    description: This entity is an ontology from the OBO Foundry, a collaborative
      effort to create reference ontologies in the biomedical domain.
    meaning: https://obofoundry.org/
  okn:
    text: okn
    description: This entity is part of the Prototype Open Knowledge Network (OKN),
      a knowledge graph network supported by the National Science Foundation (NSF).
    meaning: https://www.proto-okn.net/

```
</details>
