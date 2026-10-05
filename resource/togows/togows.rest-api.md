---
category: ProgrammingInterface
connection_url: http://togows.org/
description: REST API for retrieving entries, or individual fields of entries, from
  UniProt, ENA, DDBJ, NCBI Nucleotide, NCBI Gene, dbSNP, PubMed, PDB and KEGG (entry
  endpoint), and for searching UniProt, ENA, NCBI Nucleotide, dbSNP, PubMed, OMIM
  and PDB (search endpoint), with JSON, Turtle, XML, GFF or FASTA output.
format: http
id: togows.rest-api
is_public: true
name: TogoWS REST API
original_source:
- relation_type: prov:hadPrimarySource
  source: togows
- relation_type: prov:hadPrimarySource
  source: uniprot
- relation_type: prov:hadPrimarySource
  source: ena
- relation_type: prov:hadPrimarySource
  source: ncbigene
- relation_type: prov:hadPrimarySource
  source: dbsnp
- relation_type: prov:hadPrimarySource
  source: pubmed
- relation_type: prov:hadPrimarySource
  source: pdb
- relation_type: prov:hadPrimarySource
  source: omim
- relation_type: prov:hadPrimarySource
  source: kegg
- relation_type: prov:hadPrimarySource
  source: ddbj
product_url: http://togows.org/help/
warnings:
- On 2026-10-03 PDB entry retrieval returned empty results, PDB search returned HTTP
  500 and dbSNP entry retrieval returned HTTP 404; the other databases tested (UniProt,
  ENA, DDBJ, NCBI Nucleotide, NCBI Gene, PubMed, KEGG, OMIM search) responded normally.
layout: product_detail
---
