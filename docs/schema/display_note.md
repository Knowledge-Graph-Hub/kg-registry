---
layout: schema_doc
mermaid: true
---


# Slot: display_note 


_For an inferred license, a sentence explaining where the license came from, for display beside it. The build composes this from the other inferred fields so that every view of the registry shows the same wording; a curator does not write it, and anything written here is overwritten._






URI: [kgr:display_note](https://w3id.org/bridge2ai/data-sheets-schema/display_note)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.html) | A license for a resource or product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.html) |
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
| self | kgr:display_note |
| native | kgr:display_note |




## LinkML Source

<details>
```yaml
name: display_note
description: For an inferred license, a sentence explaining where the license came
  from, for display beside it. The build composes this from the other inferred fields
  so that every view of the registry shows the same wording; a curator does not write
  it, and anything written here is overwritten.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
owner: License
domain_of:
- License
range: string

```
</details>
