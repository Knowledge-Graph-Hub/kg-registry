---
layout: schema_doc
mermaid: true
---


# Slot: status 


_Whether the license was provided by the resource's curators or maintainers, or inferred by the build process from the licenses of the resource's upstream sources. If absent, the license is provided._






URI: [kgr:status](https://w3id.org/bridge2ai/data-sheets-schema/status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.html) | A license for a resource or product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LicenseStatusEnum](LicenseStatusEnum.html) |
| Domain Of | [License](License.html) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [License](License.html) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:status |
| native | kgr:status |




## LinkML Source

<details>
```yaml
name: status
description: Whether the license was provided by the resource's curators or maintainers,
  or inferred by the build process from the licenses of the resource's upstream sources.
  If absent, the license is provided.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
owner: License
domain_of:
- License
range: LicenseStatusEnum

```
</details>
