---
layout: schema_doc
mermaid: true
---

# Enum: ProvenanceRelationEnum




_PROV-O relation types used to describe how a product is related to a resource or product source._



URI: [kgr:ProvenanceRelationEnum](https://w3id.org/bridge2ai/data-sheets-schema/ProvenanceRelationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| prov:hadPrimarySource | prov:hadPrimarySource | The source is a primary source for this product |
| prov:wasDerivedFrom | prov:wasDerivedFrom | The product was derived from, transformed from, updated from, or constructed ... |
| prov:wasInfluencedBy | prov:wasInfluencedBy | The product was influenced by the source in a broad provenance sense |
| prov:wasInformedBy | prov:wasInformedBy | The product was informed by the source, for cases where information from the ... |
| prov:used | prov:used | The product was produced by an activity that used the source as an input, ref... |




## Slots

| Name | Description |
| ---  | --- |
| [relation_type](relation_type.html) | The PROV-O relation type that describes how the product is related to the sou... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: ProvenanceRelationEnum
description: PROV-O relation types used to describe how a product is related to a
  resource or product source.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  prov:hadPrimarySource:
    text: prov:hadPrimarySource
    description: The source is a primary source for this product. This is the default
      relation type for original_source associations.
    meaning: prov:hadPrimarySource
  prov:wasDerivedFrom:
    text: prov:wasDerivedFrom
    description: The product was derived from, transformed from, updated from, or
      constructed based on the source.
    meaning: prov:wasDerivedFrom
  prov:wasInfluencedBy:
    text: prov:wasInfluencedBy
    description: The product was influenced by the source in a broad provenance sense.
      This is the default relation type for secondary_source associations when a more
      specific PROV-O relation is not known.
    meaning: prov:wasInfluencedBy
  prov:wasInformedBy:
    text: prov:wasInformedBy
    description: The product was informed by the source, for cases where information
      from the source affected the product without implying direct derivation.
    meaning: prov:wasInformedBy
  prov:used:
    text: prov:used
    description: The product was produced by an activity that used the source as an
      input, reference, ontology, vocabulary, or other entity.
    meaning: prov:used

```
</details>
