---
layout: schema_doc
mermaid: true
---

# Enum: CompressionEnum




_The type of compression used with a product._



URI: [CompressionEnum](CompressionEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| gpickle | None | The gpickle format, or the output of pickling a NetworkX graph object |
| gzip | None | The gzip compression algorithm |
| pickle | None | The pickle format, or the output of pickling a Python object |
| tar | None | The tar archive format |
| targz | None | A tar archive that is also gzip compressed |
| rar | None | The rar archive format |
| zip | None | The zip archive format |
| 7z | None | The 7z archive format |
| other | None | Another compression format not defined here |




## Slots

| Name | Description |
| ---  | --- |
| [compression](compression.html) | The type of compression used with the product |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: CompressionEnum
description: The type of compression used with a product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  gpickle:
    text: gpickle
    description: The gpickle format, or the output of pickling a NetworkX graph object.
      This file ends in .gpickle.
  gzip:
    text: gzip
    description: The gzip compression algorithm. This file ends in .gz.
  pickle:
    text: pickle
    description: The pickle format, or the output of pickling a Python object. This
      file ends in .pkl or .pickle.
  tar:
    text: tar
    description: The tar archive format. This file ends in .tar.
  targz:
    text: targz
    description: A tar archive that is also gzip compressed. This file ends in .tar.gz.
  rar:
    text: rar
    description: The rar archive format. This file ends in .rar.
  zip:
    text: zip
    description: The zip archive format. This file ends in .zip.
  7z:
    text: 7z
    description: The 7z archive format. This file ends in .7z.
  other:
    text: other
    description: Another compression format not defined here.

```
</details>
