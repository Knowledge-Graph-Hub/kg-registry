---
category: GraphProduct
description: The AOP-Wiki RDF dataset in RDF/Turtle, covering AOPs, key events, key
  event relationships, biological events, stressors and chemicals converted from the
  AOP-Wiki XML export, together with the gene mappings (HGNC approved symbols resolved
  to Ensembl, NCBI Gene, UniProt and Protein Ontology identifiers via BridgeDb) and
  the chemical and protein cross-reference enrichments. Distributed as Turtle files
  in the data/ directory of the conversion repository (AOPWikiRDF.ttl, AOPWikiRDF-Genes.ttl,
  AOPWikiRDF-Enriched.ttl); all of them are loaded together into the SPARQL endpoint
  and are meant to be used as one dataset. Regenerated weekly.
format: ttl
id: aopwiki-rdf.ttl
latest_version: 2026.08.15
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: AOP-Wiki RDF Turtle Dataset
original_source:
- relation_type: prov:wasDerivedFrom
  source: aop-wiki
- relation_type: prov:hadPrimarySource
  source: aopwiki-rdf
- relation_type: prov:used
  source: ensembl
- relation_type: prov:used
  source: hgnc
- relation_type: prov:used
  source: ncbigene
- relation_type: prov:used
  source: pr
- relation_type: prov:used
  source: uniprot
product_url: https://github.com/marvinm2/AOPWikiRDF/tree/master/data
repository: https://github.com/marvinm2/AOPWikiRDF
layout: product_detail
---
