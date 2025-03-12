---
layout: schema_doc
mermaid: true
---

# Enum: DumpFormatEnum




_The format of a dump of a product, generally a graph, as a file. Note the product may also be compressed._



URI: [DumpFormatEnum](DumpFormatEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| gpickle | None | The gpickle format, or the output of pickling a NetworkX graph object |
| pickle | None | The pickle format, or the output of pickling a Python object |
| other | None | Another format not defined here |




## Slots

| Name | Description |
| ---  | --- |
| [dump_format](dump_format.html) | The format of a dump of the product as a file |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: DumpFormatEnum
description: The format of a dump of a product, generally a graph, as a file. Note
  the product may also be compressed.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  gpickle:
    text: gpickle
    description: The gpickle format, or the output of pickling a NetworkX graph object.
      This file ends in .gpickle.
  pickle:
    text: pickle
    description: The pickle format, or the output of pickling a Python object. This
      file ends in .pkl or .pickle.
  other:
    text: other
    description: Another format not defined here.

```
</details>
