---
layout: schema_doc
mermaid: true
---

# Enum: DumpFormatEnum




_The format of a dump of a product, generally a graph, as a file. Note the product may also be compressed._



URI: [kgr:DumpFormatEnum](https://w3id.org/bridge2ai/data-sheets-schema/DumpFormatEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| gpickle | None | The gpickle format, or the output of pickling a NetworkX graph object |
| pickle | None | The pickle format, or the output of pickling a Python object |
| neo4j | None | The Neo4j dump format, or the output of a Neo4j database dump |
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
  neo4j:
    text: neo4j
    description: The Neo4j dump format, or the output of a Neo4j database dump. The
      file usually ends in .db, .dump, or .db.dump.
  other:
    text: other
    description: Another format not defined here.

```
</details>
