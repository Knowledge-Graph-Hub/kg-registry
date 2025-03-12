---
layout: schema_doc
mermaid: true
---

# Enum: FormatEnum




_The serialization/format of a product._



URI: [FormatEnum](FormatEnum.html)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| json | None | The JSON format |
| jsonld | None | The JSON-LD format |
| rdfxml | None | The RDF/XML format |
| ttl | None | The Turtle format |
| ntriples | None | The N-Triples format |
| nquads | None | The N-Quads format |
| owl | None | The OWL format |
| obo | None | The OBO format |
| graphql | None | The GraphQL format |
| protobuf | None | The Protobuf format |
| shacl | None | The SHACL format |
| shex | None | The ShEx format |
| kgx | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-json | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-jsonl | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-rdf | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |




## Slots

| Name | Description |
| ---  | --- |
| [format](format.html) | The format or serialization of the product |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: FormatEnum
description: The serialization/format of a product.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  json:
    text: json
    description: The JSON format.
  jsonld:
    text: jsonld
    description: The JSON-LD format.
  rdfxml:
    text: rdfxml
    description: The RDF/XML format.
  ttl:
    text: ttl
    description: The Turtle format.
  ntriples:
    text: ntriples
    description: The N-Triples format.
  nquads:
    text: nquads
    description: The N-Quads format.
  owl:
    text: owl
    description: The OWL format.
  obo:
    text: obo
    description: The OBO format.
  graphql:
    text: graphql
    description: The GraphQL format.
  protobuf:
    text: protobuf
    description: The Protobuf format.
  shacl:
    text: shacl
    description: The SHACL format.
  shex:
    text: shex
    description: The ShEx format.
  kgx:
    text: kgx
    description: The KGX standard, which is a graph exchange format for knowledge
      graphs. By default, this assumes KGX as TSV with separate node and edge files,
      usually named nodes.tsv and edges.tsv.
    meaning: https://github.com/biolink/kgx/blob/master/specification/kgx-format.md
  kgx-json:
    text: kgx-json
    description: The KGX standard, which is a graph exchange format for knowledge
      graphs. This is the JSON format, with nodes and edges in a single file.
    meaning: https://github.com/biolink/kgx/blob/master/specification/kgx-format.md
  kgx-jsonl:
    text: kgx-jsonl
    description: The KGX standard, which is a graph exchange format for knowledge
      graphs. This is the JSON Lines format, with separate node and edge files, usually
      named nodes.jsonl and edges.jsonl.
    meaning: https://github.com/biolink/kgx/blob/master/specification/kgx-format.md
  kgx-rdf:
    text: kgx-rdf
    description: The KGX standard, which is a graph exchange format for knowledge
      graphs. This is the RDF Turtle (TTL) format, with nodes and edges in a single
      file.
    meaning: https://github.com/biolink/kgx/blob/master/specification/kgx-format.md

```
</details>
