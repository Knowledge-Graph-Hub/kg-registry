---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://rdfportal.org/about/
  label: Database Center for Life Science (DBCLS)
creation_date: '2026-10-05T00:00:00Z'
description: RDF Portal is a repository of quality-reviewed life science datasets in
  RDF, maintained by the Database Center for Life Science (DBCLS, Japan) and formerly
  run by the National Bioscience Database Center (NBDC) as the NBDC RDF Portal. It
  hosts 67 datasets (about 231.6 billion triples when checked on 2026-10-05), from
  Japanese projects and from international sources such as UniProt, PubChem, ChEMBL,
  Ensembl and NCBI databases. Data are available through SPARQL endpoints grouped
  by provider, a GraphQL API, an MCP server (TogoMCP) and bulk RDF downloads. Licenses
  are set per dataset and listed on each dataset's page.
domains:
- biomedical
- information technology
- genomics
- proteomics
- chemistry and biochemistry
homepage_url: https://rdfportal.org/
id: rdf-portal
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: ddbj, icgc, medgen. Not accounted for, no
    known license: pdb.'
  id: https://www.ddbj.nig.ac.jp/policies-e.html
  inferred_from:
  - ddbj
  - icgc
  - medgen
  label: DDBJ (NIG BioData Science Initiative) Terms of Use; INSDC data are unrestricted-access
    and may be freely used, redistributed and modified, while JGA data are controlled-access
    under the NBDC Human Data Sharing Guidelines
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - pdb
name: RDF Portal
products:
- category: GraphicalInterface
  description: RDF Portal website, with a browsable catalog of hosted RDF datasets,
    each with provenance, license, version, statistics and SPARQL example queries.
  format: http
  id: rdf-portal.portal
  name: RDF Portal Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/
- category: GraphicalInterface
  description: Dataset catalog listing every hosted RDF dataset with tags, data provider,
    license and links to per-dataset detail pages. The dataset metadata are embedded
    in the page as JSON; no separate machine-readable dataset list was found.
  format: http
  id: rdf-portal.datasets
  name: RDF Portal Dataset Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/datasets/
- category: ProgrammingInterface
  description: SPARQL endpoint for the primary RDF Portal datasets, mostly from Japanese
    projects and partner databases (for example BacDive, BRENDA, GlyTouCan, GTDB, HGNC,
    HomoloGene, ICGC, jPOST, MediaDive, NANDO, PubCaseFinder and TogoID).
  format: http
  id: rdf-portal.sparql.primary
  name: RDF Portal Primary SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: brenda
  - relation_type: prov:wasDerivedFrom
    source: glytoucan
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: homologene
  - relation_type: prov:wasDerivedFrom
    source: icgc
  - relation_type: prov:wasDerivedFrom
    source: mediadive
  - relation_type: prov:wasDerivedFrom
    source: jpost
  product_url: https://rdfportal.org/primary/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for EBI-derived RDF datasets, including AMR portal,
    BioModels, BioSample, ChEBI, ChEMBL, Ensembl (including GRCh37), GWAS Catalog
    and Reactome.
  format: http
  id: rdf-portal.sparql.ebi
  name: RDF Portal EBI SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: chembl
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: reactome
  product_url: https://rdfportal.org/ebi/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for NCBI- and NLM-derived RDF datasets, including ClinVar,
    MedGen, MeSH, NCBI Gene, NLM Catalog, PubMed and PubTator Central.
  format: http
  id: rdf-portal.sparql.ncbi
  name: RDF Portal NCBI SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: medgen
  - relation_type: prov:wasDerivedFrom
    source: mesh
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  product_url: https://rdfportal.org/ncbi/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for SIB-derived RDF datasets, including Bgee, Cellosaurus,
    OMA, Rhea and UniProt.
  format: http
  id: rdf-portal.sparql.sib
  name: RDF Portal SIB SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: bgee
  - relation_type: prov:wasDerivedFrom
    source: cellosaurus
  - relation_type: prov:wasDerivedFrom
    source: oma
  - relation_type: prov:wasDerivedFrom
    source: rhea
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  product_url: https://rdfportal.org/sib/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for PubChem RDF.
  format: http
  id: rdf-portal.sparql.pubchem
  name: RDF Portal PubChem SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  product_url: https://rdfportal.org/pubchem/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for Protein Data Bank RDF datasets (wwPDB/RDF and BMRB/RDF).
  format: http
  id: rdf-portal.sparql.pdb
  name: RDF Portal PDB SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: pdb
  product_url: https://rdfportal.org/pdb/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for the DDBJ RDF dataset.
  format: http
  id: rdf-portal.sparql.ddbj
  name: RDF Portal DDBJ SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: ddbj
  product_url: https://rdfportal.org/ddbj/sparql
- category: ProgrammingInterface
  description: SPARQL endpoint for the DBKERO RDF dataset.
  format: http
  id: rdf-portal.sparql.kero
  name: RDF Portal KERO SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/kero/sparql
- category: ProgrammingInterface
  description: GraphQL API powered by Grasp, a GraphQL-to-SPARQL bridge developed by
    DBCLS, with a GraphiQL interface in the browser. When checked it covered UniProt,
    ChEBI, ChEMBL and MedGen.
  format: http
  id: rdf-portal.graphql
  name: RDF Portal GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: chembl
  - relation_type: prov:wasDerivedFrom
    source: medgen
  product_url: https://rdfportal.org/grasp
- category: ProgrammingInterface
  description: TogoMCP, a Model Context Protocol server from DBCLS that gives AI agents
    keyword search, SPARQL querying and TogoID identifier conversion over databases
    hosted on RDF Portal. Source code is at https://github.com/dbcls/togomcp.
  format: http
  id: rdf-portal.mcp
  name: TogoMCP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://togomcp.rdfportal.org/mcp
- category: GraphProduct
  description: Bulk downloads of hosted RDF datasets as N-Triples, one directory per
    dataset with dated and latest releases (files mostly gzip-compressed). Turtle
    copies of some datasets are under https://rdfportal.org/pub/turtle/.
  format: ntriples
  id: rdf-portal.ntriples
  name: RDF Portal N-Triples Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/pub/ntriples/
- category: DocumentationProduct
  description: RDF Portal user manual, covering dataset browsing, SPARQL endpoints,
    GraphQL, TogoMCP, statistics, downloads, tutorials and licensing questions.
  format: http
  id: rdf-portal.manual
  name: RDF Portal Manual
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/documents/manual/
- category: DocumentationProduct
  description: Guidelines for submitting RDF datasets to RDF Portal, which DBCLS reviews
    against its RDF guidelines before publication.
  format: http
  id: rdf-portal.data-submission
  name: RDF Portal Data Submission Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdf-portal
  product_url: https://rdfportal.org/documents/data_submission/
publications:
- authors:
  - Shuichi Kawashima
  - Toshiaki Katayama
  - Hideki Hatanaka
  - Tatsuya Kushida
  - Toshihisa Takagi
  doi: 10.1093/database/bay123
  id: doi:10.1093/database/bay123
  journal: Database
  preferred: true
  title: 'NBDC RDF portal: a comprehensive repository for semantic data in life sciences'
  year: '2018'
synonyms:
- NBDC RDF Portal
- DBCLS RDF Portal
---
# RDF Portal

RDF Portal is a repository of life science datasets in RDF. The National Bioscience Database Center (NBDC) of the Japan Science and Technology Agency first built it to host RDF from the Integrated Database Project. It later took in openly available RDF datasets from around the world, and since 2022 the Database Center for Life Science (DBCLS) has maintained it. DBCLS reviews every submitted dataset against the DBCLS RDF Guidelines before publishing it.

When checked on 2026-10-05, the portal listed 67 datasets with about 231.6 billion triples.

## Access

- **SPARQL endpoints**: datasets are grouped by provider behind several endpoints: `primary` (most Japanese and partner datasets), `ebi`, `ncbi`, `sib`, `pubchem`, `pdb`, `ddbj` and `kero`, all under `https://rdfportal.org/<group>/sparql`. Each dataset is a named graph.
- **GraphQL API**: `https://rdfportal.org/grasp`, using the Grasp GraphQL-to-SPARQL bridge, for a subset of datasets.
- **MCP interface**: TogoMCP at `https://togomcp.rdfportal.org/mcp`.
- **Downloads**: N-Triples (and some Turtle) files under `https://rdfportal.org/pub/`.

## Licensing

There is no portal-wide license. Each dataset's detail page gives its own license; for example, ChEMBL RDF is listed under CC BY-SA 3.0.
