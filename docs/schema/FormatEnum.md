---
layout: schema_doc
mermaid: true
---

# Enum: FormatEnum




_The serialization/format of a product._



URI: [kgr:FormatEnum](https://w3id.org/bridge2ai/data-sheets-schema/FormatEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| biopax | edam:3156 | The BioPAX format, an RDF/OWL-based standard language for representing biolog... |
| boolnet | https://cran.r-project.org/package=BoolNet | The Boolean Network (BoolNet) format, which is a format for representing Bool... |
| chebi_sdf | https://docs.google.com/document/d/11G6SmTtQRQYFT7l9h5K0faUHiAaekcLeOweMOOTIpME/edit?pli=1&tab=t.0#heading=h.7ocxce8u265h | A ChEBI-specific SDF format |
| csv | edam:3752 | The Comma-Separated Values (CSV) format |
| doc | None | The Microsoft Word Document (DOC) format, a binary file format used by Micros... |
| docx | None | The Microsoft Word Open XML Document (DOCX) format, a modern file format for ... |
| dot | https://graphviz.org/doc/info/lang.html | The DOT format, a plain text graph description language used to define the st... |
| fasta | edam:1929 | The FASTA format, a text-based format for representing nucleotide or peptide ... |
| gff | None | The General Feature Format (GFF), a standard file format for describing genes... |
| graphql | None | The GraphQL format, a query language for APIs and a runtime for executing tho... |
| hdf5 | edam:3590 | The Hierarchical Data Format version 5 (HDF5) format, a file format and set o... |
| http | None | The Hypertext Transfer Protocol (HTTP) format |
| java | None | The Java source code format, which is a text file containing Java code |
| javascript | None | The JavaScript file format, which is a text file containing JavaScript code |
| json | edam:3464 | The JavaScript Object Notation (JSON) format, a lightweight data-interchange ... |
| jsonld | edam:3749 | The JSON for Linked Data (JSON-LD) format, which extends JSON with semantics ... |
| kgx | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-json | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-jsonl | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| kgx-rdf | https://github.com/biolink/kgx/blob/master/specification/kgx-format.md | The KGX standard, which is a graph exchange format for knowledge graphs |
| mixed | None | A product that contains multiple formats or serializations |
| mysql | None | The MySQL relational database management system |
| neo4j | None | The Neo4j graph database management system |
| nquads | edam:3956 | The N-Quads format, an extension of the N-Triples format that adds an optiona... |
| ntriples | edam:3256 | The N-Triples format, a line-based, plain text serialization format for RDF g... |
| obo | edam:2196 | The Open Biomedical Ontologies (OBO) format, a file format for representing o... |
| owl | edam:2197 | The Web Ontology Language (OWL) format, a semantic web language designed to r... |
| pdf | None | The Portable Document Format (PDF), a file format developed by Adobe for pres... |
| png | None | The Portable Network Graphics (PNG) format, a raster graphics file format tha... |
| postgres | None | The PostgreSQL relational database management system |
| protobuf | None | The Protocol Buffers (Protobuf) format, a language-neutral, platform-neutral,... |
| psi_mi_mitab | https://psicquic.github.io/MITAB28Format.html | The PSI-MI MITAB format, which is a tab-delimited format for representing mol... |
| psi_mi_xml | https://www.psidev.info/psi-mi-xml-specification | The PSI-MI XML format, which is a standard for representing molecular interac... |
| python | None | The Python script format, which is a text file containing Python code |
| rdfxml | edam:3261 | The RDF/XML format, an XML syntax for expressing RDF graphs as an XML documen... |
| sbgnml | https://sbgn.github.io/sbgn/ | The Systems Biology Graphical Notation (SBGN) XML format, which is a standard... |
| sbml | https://sbml.org/ | The Systems Biology Markup Language (SBML) XML format, which is a computer-re... |
| sdf | https://www.fda.gov/media/151718/download | The Structure Data File (SDF) format |
| shacl | None | The Shapes Constraint Language (SHACL) format, a language for validating RDF ... |
| shex | None | The Shape Expressions (ShEx) format, a language for validating and describing... |
| sif | https://www.cytoscape.org/sif.html | The Simple Interaction Format (SIF), a simple text format for representing in... |
| sqlite | None | The SQLite relational database management system |
| sssom | https://mapping-commons.github.io/sssom/ | The Simple Standard for Sharing Ontological Mappings (SSSOM) format, which a ... |
| stockholm | edam:1961 | The Stockholm format, a multiple sequence alignment format used in bioinforma... |
| svg | edam:3604 | The Scalable Vector Graphics (SVG) format, an XML-based format for describing... |
| trapi-jsonl | https://raw.githubusercontent.com/NCATSTranslator/ReasonerAPI/refs/heads/master/TranslatorReasonerAPI.yaml | The Translator Reasoner API (TRAPI) format, which is a JSON Lines format for ... |
| tsv | edam:3475 | The Tab-Separated Values (TSV) format |
| ttl | edam:3255 | The Turtle (TTL) format, a textual syntax for RDF that allows RDF graphs to b... |
| txt | None | The Plain Text (TXT) format, a simple text format for representing unformatte... |
| vcf | edam:3016 | The Variant Call Format (VCF), a text file format for storing gene sequence v... |
| xgmml | edam:3618 | The eXtensible Graph Markup Language (XGMML) format, an XML-based format for ... |
| xml | edam:2332 | The Extensible Markup Language (XML) format |
| yaml | edam:3750 | The YAML Ain't Markup Language (YAML) format, a human-readable data serializa... |




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
  biopax:
    text: biopax
    description: The BioPAX format, an RDF/OWL-based standard language for representing
      biological pathways at the molecular and cellular level.
    meaning: edam:3156
  boolnet:
    text: boolnet
    description: The Boolean Network (BoolNet) format, which is a format for representing
      Boolean networks. Used with the BoolNet package in R for modeling and analyzing
      biological networks.
    meaning: https://cran.r-project.org/package=BoolNet
  chebi_sdf:
    text: chebi_sdf
    description: A ChEBI-specific SDF format. Unlike the general SDF format, Each
      data item may be longer than 80 characters and has no maximum limit. Each line
      after the Data Header is a separate data item. For example, each new line in
      the synonyms is a separate synonym.
    meaning: https://docs.google.com/document/d/11G6SmTtQRQYFT7l9h5K0faUHiAaekcLeOweMOOTIpME/edit?pli=1&tab=t.0#heading=h.7ocxce8u265h
  csv:
    text: csv
    description: The Comma-Separated Values (CSV) format. It has rows of data separated
      by newlines, and columns separated by commas.
    meaning: edam:3752
  doc:
    text: doc
    description: The Microsoft Word Document (DOC) format, a binary file format used
      by Microsoft Word. It is commonly used for word processing documents.
  docx:
    text: docx
    description: The Microsoft Word Open XML Document (DOCX) format, a modern file
      format for Microsoft Word documents. It is a zipped, XML-based file format that
      allows for more efficient storage and better compatibility with other software,
      as compared to the older DOC format.
  dot:
    text: dot
    description: The DOT format, a plain text graph description language used to define
      the structure of graphs. It is often used with Graphviz to visualize graphs.
    meaning: https://graphviz.org/doc/info/lang.html
  fasta:
    text: fasta
    description: The FASTA format, a text-based format for representing nucleotide
      or peptide sequences. It consists of a single header line followed by one or
      more lines of sequence data.
    meaning: edam:1929
  gff:
    text: gff
    description: The General Feature Format (GFF), a standard file format for describing
      genes and other features of DNA, RNA, and protein sequences. It is commonly
      used in bioinformatics for storing and sharing genomic annotations.
  graphql:
    text: graphql
    description: The GraphQL format, a query language for APIs and a runtime for executing
      those queries against your data. It allows clients to request exactly what they
      need and makes it easier to evolve APIs over time.
  hdf5:
    text: hdf5
    description: The Hierarchical Data Format version 5 (HDF5) format, a file format
      and set of tools for managing complex data. It is designed to store and organize
      large amounts of data in a hierarchical structure, allowing for efficient access
      and manipulation.
    meaning: edam:3590
  http:
    text: http
    description: The Hypertext Transfer Protocol (HTTP) format. This is a protocol
      for transferring data over the web. If a product is in this format, it is likely
      an web site or API.
  java:
    text: java
    description: The Java source code format, which is a text file containing Java
      code. It is used for writing scripts and programs in the Java language.
  javascript:
    text: javascript
    description: The JavaScript file format, which is a text file containing JavaScript
      code. It is used for writing scripts and programs in the JavaScript language.
  json:
    text: json
    description: The JavaScript Object Notation (JSON) format, a lightweight data-interchange
      format that's easy for humans to read and write and easy for machines to parse
      and generate.
    meaning: edam:3464
  jsonld:
    text: jsonld
    description: The JSON for Linked Data (JSON-LD) format, which extends JSON with
      semantics for linked data by providing a method of encoding linked data using
      JSON. It enables data in JSON to be interpreted as RDF and allows JSON data
      to be interoperable at Web-scale.
    meaning: edam:3749
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
  mixed:
    text: mixed
    description: A product that contains multiple formats or serializations. This
      is used when a product is not easily categorized into a single format, such
      as a codebase that includes multiple file types (e.g., Python scripts, JSON
      files, etc.).
  mysql:
    text: mysql
    description: The MySQL relational database management system. If a product is
      in this format, it is likely a MySQL database dump.
  neo4j:
    text: neo4j
    description: The Neo4j graph database management system. If a product is in this
      format, it is likely a Neo4j database dump. The file usually ends in .db, .dump,
      or .db.dump.
  nquads:
    text: nquads
    description: The N-Quads format, an extension of the N-Triples format that adds
      an optional fourth element to represent the graph name or context. This allows
      for representing multiple RDF graphs in a single document while maintaining
      their separation.
    meaning: edam:3956
  ntriples:
    text: ntriples
    description: The N-Triples format, a line-based, plain text serialization format
      for RDF graphs. Each line contains a single RDF triple consisting of subject,
      predicate, and object, separated by whitespace and terminated by a period.
    meaning: edam:3256
  obo:
    text: obo
    description: The Open Biomedical Ontologies (OBO) format, a file format for representing
      ontologies in the biomedical domain. It's designed to be simple and human-readable
      while supporting the necessary expressivity for representing biological concepts.
    meaning: edam:2196
  owl:
    text: owl
    description: The Web Ontology Language (OWL) format, a semantic web language designed
      to represent rich and complex knowledge about things and their relationships.
      OWL builds on RDF and adds more vocabulary for describing properties and classes.
    meaning: edam:2197
  pdf:
    text: pdf
    description: The Portable Document Format (PDF), a file format developed by Adobe
      for presenting documents in a manner independent of application software, hardware,
      and operating systems. PDF files can contain text, images, and vector graphics.
  png:
    text: png
    description: The Portable Network Graphics (PNG) format, a raster graphics file
      format that supports lossless data compression. It is commonly used for web
      images and supports transparency.
  postgres:
    text: postgres
    description: The PostgreSQL relational database management system. If a product
      is in this format, it is likely a PostgreSQL database dump.
  protobuf:
    text: protobuf
    description: The Protocol Buffers (Protobuf) format, a language-neutral, platform-neutral,
      extensible mechanism for serializing structured data. It's smaller, faster,
      and simpler than XML, designed for high-performance data interchange.
  psi_mi_mitab:
    text: psi_mi_mitab
    description: The PSI-MI MITAB format, which is a tab-delimited format for representing
      molecular interaction data. It is used to exchange information about molecular
      interactions between different databases.
    meaning: https://psicquic.github.io/MITAB28Format.html
  psi_mi_xml:
    text: psi_mi_xml
    description: The PSI-MI XML format, which is a standard for representing molecular
      interaction data in XML. It is used to exchange information about molecular
      interactions between different databases.
    meaning: https://www.psidev.info/psi-mi-xml-specification
  python:
    text: python
    description: The Python script format, which is a text file containing Python
      code. It is used for writing scripts and programs in the Python language.
  rdfxml:
    text: rdfxml
    description: The RDF/XML format, an XML syntax for expressing RDF graphs as an
      XML document. It was the first standardized syntax for RDF and is widely used
      for interchange and archiving.
    meaning: edam:3261
  sbgnml:
    text: sbgnml
    description: The Systems Biology Graphical Notation (SBGN) XML format, which is
      a standard for representing biological pathways and processes in a graphical
      form.
    meaning: https://sbgn.github.io/sbgn/
  sbml:
    text: sbml
    description: The Systems Biology Markup Language (SBML) XML format, which is a
      computer-readable format for representing models of biological processes.
    meaning: https://sbml.org/
  sdf:
    text: sdf
    description: The Structure Data File (SDF) format.
    meaning: https://www.fda.gov/media/151718/download
  shacl:
    text: shacl
    description: The Shapes Constraint Language (SHACL) format, a language for validating
      RDF graphs against a set of conditions. SHACL allows for defining constraints
      on RDF graphs, including the structure, values, and other features of data.
  shex:
    text: shex
    description: The Shape Expressions (ShEx) format, a language for validating and
      describing RDF data. ShEx provides a concise, human-readable syntax for expressing
      constraints on RDF graphs, including cardinality constraints and datatype restrictions.
  sif:
    text: sif
    description: The Simple Interaction Format (SIF), a simple text format for representing
      interactions between biological entities. It is often used to represent networks
      of interactions.
    meaning: https://www.cytoscape.org/sif.html
  sqlite:
    text: sqlite
    description: The SQLite relational database management system. If a product is
      in this format, it is likely a SQLite database dump.
  sssom:
    text: sssom
    description: The Simple Standard for Sharing Ontological Mappings (SSSOM) format,
      which a format for mapping between different ontologies and other identifier
      systems.
    meaning: https://mapping-commons.github.io/sssom/
  stockholm:
    text: stockholm
    description: The Stockholm format, a multiple sequence alignment format used in
      bioinformatics. It is commonly used for representing alignments of protein or
      nucleotide sequences.
    meaning: edam:1961
  svg:
    text: svg
    description: The Scalable Vector Graphics (SVG) format, an XML-based format for
      describing two-dimensional vector graphics.
    meaning: edam:3604
  trapi-jsonl:
    text: trapi-jsonl
    description: The Translator Reasoner API (TRAPI) format, which is a JSON Lines
      format for TRAPI responses.
    meaning: https://raw.githubusercontent.com/NCATSTranslator/ReasonerAPI/refs/heads/master/TranslatorReasonerAPI.yaml
  tsv:
    text: tsv
    description: The Tab-Separated Values (TSV) format. It has rows of data separated
      by newlines, and columns separated by tabs.
    meaning: edam:3475
  ttl:
    text: ttl
    description: The Turtle (TTL) format, a textual syntax for RDF that allows RDF
      graphs to be written in a compact and natural text form. Turtle provides prefixes
      and keywords that make RDF data more readable compared to XML or N-Triples formats.
    meaning: edam:3255
  txt:
    text: txt
    description: The Plain Text (TXT) format, a simple text format for representing
      unformatted text data.
  vcf:
    text: vcf
    description: The Variant Call Format (VCF), a text file format for storing gene
      sequence variations. It is commonly used in bioinformatics to store gene sequence
      variations, such as single nucleotide polymorphisms (SNPs).
    meaning: edam:3016
  xgmml:
    text: xgmml
    description: The eXtensible Graph Markup Language (XGMML) format, an XML-based
      format for representing graphs and networks.
    meaning: edam:3618
  xml:
    text: xml
    description: The Extensible Markup Language (XML) format. It is a markup language
      that defines a set of rules for encoding documents in a format that is both
      human-readable and machine-readable.
    meaning: edam:2332
  yaml:
    text: yaml
    description: The YAML Ain't Markup Language (YAML) format, a human-readable data
      serialization format. It is often used for configuration files and data exchange
      between languages with different data structures.
    meaning: edam:3750

```
</details>
