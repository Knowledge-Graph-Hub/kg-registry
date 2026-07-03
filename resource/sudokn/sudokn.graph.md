---
category: GraphProduct
description: The SUDOKN manufacturing capability knowledge graph in RDF (Turtle),
  representing the capabilities of small and medium-sized U.S. manufacturers. Company
  profiles (manufacturing processes, materials, industries served, certifications,
  NAICS classification, and locations) are built by web-scraping raw text from manufacturer
  company websites and extracting triples with an LLM-based ETL pipeline, using terms
  from the SUDOKN application ontology (built on the Industrial Ontology Foundry and
  Basic Formal Ontology). Served through the SUDOKN SPARQL and Triple Pattern Fragments
  endpoints.
format: ttl
id: sudokn.graph
name: SUDOKN Manufacturing Capability Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: sudokn
product_url: https://github.com/SUDOKN/graph
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: us-census
layout: product_detail
---
