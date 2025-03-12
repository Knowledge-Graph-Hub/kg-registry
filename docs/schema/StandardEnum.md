---
layout: schema_doc
mermaid: true
---

# Enum: StandardEnum




_The standard or standards that a product conforms to. These are not serializations, but rather the higher-level frameworks that the product is built on._



URI: [StandardEnum](StandardEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| biolink | https://biolink.github.io/biolink-model/ | The Biolink Model, a standard for representing biological entities and relati... |
| kghub | https://kghub.org/ | The KG-Hub standard, which is a general-purpose knowledge graph standard |




## Slots

| Name | Description |
| ---  | --- |
| [standard](standard.html) | The name of the standard that the product is compatible with |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: StandardEnum
description: The standard or standards that a product conforms to. These are not serializations,
  but rather the higher-level frameworks that the product is built on.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  biolink:
    text: biolink
    description: The Biolink Model, a standard for representing biological entities
      and relationships.
    meaning: https://biolink.github.io/biolink-model/
  kghub:
    text: kghub
    description: The KG-Hub standard, which is a general-purpose knowledge graph standard.
    meaning: https://kghub.org/

```
</details>
