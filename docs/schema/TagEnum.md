---
layout: schema_doc
mermaid: true
---

# Enum: TagEnum




_General-purpose tags that can be associated with resources._



URI: [TagEnum](TagEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| biopragmatics | None | A resource or product aggregated by the BioPragmatics project |
| core | None | A core KG-Hub resource |
| translator | None | A resource used by the NCATS Translator program |




## Slots

| Name | Description |
| ---  | --- |
| [tags](tags.html) | Tags associated with the resource |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: TagEnum
description: General-purpose tags that can be associated with resources.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  biopragmatics:
    text: biopragmatics
    description: A resource or product aggregated by the BioPragmatics project.
  core:
    text: core
    description: A core KG-Hub resource.
  translator:
    text: translator
    description: A resource used by the NCATS Translator program.

```
</details>
