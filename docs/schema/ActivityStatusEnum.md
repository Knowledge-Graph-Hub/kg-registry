---
layout: schema_doc
mermaid: true
---

# Enum: ActivityStatusEnum




_The status of a resource. Corresponds to those used by OBO Foundry._



URI: [ActivityStatusEnum](ActivityStatusEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| active | None | The resource is active and available |
| inactive | None | The resource is inactive |
| orphaned | None | The resource is not actively maintained |
| unresponsive | None | The resource is no longer accessible |




## Slots

| Name | Description |
| ---  | --- |
| [activity_status](activity_status.html) | The status of the resource |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: ActivityStatusEnum
description: The status of a resource. Corresponds to those used by OBO Foundry.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  active:
    text: active
    description: The resource is active and available.
  inactive:
    text: inactive
    description: The resource is inactive. Its availability may vary.
  orphaned:
    text: orphaned
    description: The resource is not actively maintained. Its availability may vary.
  unresponsive:
    text: unresponsive
    description: The resource is no longer accessible. Only its metadata is available.

```
</details>
