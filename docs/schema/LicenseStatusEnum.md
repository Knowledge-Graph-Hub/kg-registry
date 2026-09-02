---
layout: schema_doc
mermaid: true
---



# Enum: LicenseStatusEnum 




_How a license came to be recorded on a resource._




URI: [kgr:LicenseStatusEnum](https://w3id.org/bridge2ai/data-sheets-schema/LicenseStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| provided | None | Declared by the resource's curators or maintainers |
| inferred | None | Filled in by the build process as the most restrictive license among the reso... |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.html) | Whether the license was provided by the resource's curators or maintainers, o... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: LicenseStatusEnum
description: How a license came to be recorded on a resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  provided:
    text: provided
    description: Declared by the resource's curators or maintainers. This is the default
      when no status is recorded.
  inferred:
    text: inferred
    description: Filled in by the build process as the most restrictive license among
      the resource's upstream sources, because the resource declares no license of
      its own.

```
</details>

