---
layout: schema_doc
mermaid: true
---



# Slot: label



URI: [kgr:label](https://w3id.org/bridge2ai/data-sheets-schema/label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Individual](Individual.html) | An individual person |  no  |
| [FundingSource](FundingSource.html) | A funding source for a resource |  no  |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [Organization](Organization.html) | An organization |  no  |
| [License](License.html) | A license for a resource or product |  no  |







## Properties

* Range: [String](String.html)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:label |
| native | kgr:label |




## LinkML Source

<details>
```yaml
name: label
alias: label
domain_of:
- Individual
- Organization
- FundingSource
- License
- Usage
range: string

```
</details>
