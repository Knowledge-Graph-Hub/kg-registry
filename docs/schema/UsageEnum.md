---
layout: schema_doc
mermaid: true
---

# Enum: UsageEnum




_The type of usage of a resource._



URI: [UsageEnum](UsageEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| actual | None | The resource is actually used in the specified way |
| experimental | None | The resource is used in the specified way for experimental purposes |
| theoretical | None | The resource is not used in the specified way, but it could be |
| other | None | The resource is used in a way not defined here |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.html) | The type of usage |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: UsageEnum
description: The type of usage of a resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  actual:
    text: actual
    description: The resource is actually used in the specified way.
  experimental:
    text: experimental
    description: The resource is used in the specified way for experimental purposes.
  theoretical:
    text: theoretical
    description: The resource is not used in the specified way, but it could be.
  other:
    text: other
    description: The resource is used in a way not defined here.

```
</details>
