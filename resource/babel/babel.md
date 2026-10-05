---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/NCATSTranslator/Babel/issues
  - contact_type: github
    value: NCATSTranslator
  label: RENCI / NCATS Biomedical Data Translator SRI team
creation_date: '2026-10-04T00:00:00Z'
description: Babel is the NCATS Biomedical Data Translator pipeline, built at RENCI,
  that groups equivalent identifiers from many biomedical vocabularies into cliques
  and assigns each clique a preferred identifier, label and Biolink type. Release
  2026jul22 holds about 605.9 million CURIEs in 388.5 million cliques, built against
  Biolink Model 4.4.3. Its compendia, synonym and conflation files back the Translator
  Node Normalizer and Name Resolver services.
domains:
- biomedical
- information technology
- metadata
homepage_url: https://github.com/NCATSTranslator/Babel
id: babel
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT (code)
name: Babel
products:
- category: Product
  description: Babel compendia, one file per Biolink type (for example Gene, Protein,
    Disease, ChemicalEntity, SmallMolecule, AnatomicalEntity). Each line is a JSON
    object for one clique, listing its identifiers with labels, descriptions and taxa,
    plus the preferred name and information content. Files carry a .txt extension;
    the Gene and Protein files (about 17.8 GB and 46.7 GB) are also split into parts.
  format: json
  id: babel.compendia
  latest_version: 2026jul22
  name: Babel Compendia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: meddra
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: cl
  product_url: https://stars.renci.org/var/babel_outputs/latest/compendia/
- category: Product
  compression: gzip
  description: Synonym files for each Babel type, one JSON object per CURIE with its
    names, Biolink types, preferred name and clique size, as loaded into the Name
    Resolver. Includes DrugChemical and GeneProtein conflated versions.
  format: json
  id: babel.synonyms
  latest_version: 2026jul22
  name: Babel Synonyms
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://stars.renci.org/var/babel_outputs/latest/synonyms/
- category: MappingProduct
  description: Conflation files that merge cliques across types, DrugChemical.txt
    and GeneProtein.txt, each line a JSON array of the clique identifiers to treat
    as one concept.
  format: json
  id: babel.conflation
  latest_version: 2026jul22
  name: Babel Conflation Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://stars.renci.org/var/babel_outputs/latest/conflation/
- category: GraphProduct
  compression: gzip
  description: Babel compendia in KGX JSON Lines format, with node and edge files
    for each Biolink type.
  format: kgx-jsonl
  id: babel.kgx
  latest_version: 2026jul22
  name: Babel KGX Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://stars.renci.org/var/babel_outputs/latest/kgx/
- category: Product
  description: DuckDB databases and Apache Parquet exports of the Babel outputs (Concord,
    Identifier and Metadata tables) for faster querying than the JSON files.
  format: parquet
  id: babel.duckdb
  latest_version: 2026jul22
  name: Babel DuckDB and Parquet Exports
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://stars.renci.org/var/babel_outputs/latest/duckdb/
- category: ProcessProduct
  description: Source code for the Babel pipeline (Snakemake and Python), with per-release
    notes in the releases directory.
  format: python
  id: babel.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: Babel Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://github.com/NCATSTranslator/Babel
- category: DocumentationProduct
  description: Babel documentation on the download layout and the custom JSON data
    formats of the compendia, synonym and conflation files.
  format: http
  id: babel.docs
  name: Babel Data Formats Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  product_url: https://github.com/NCATSTranslator/Babel/blob/main/docs/DataFormats.md
publications:
- authors:
  - Evan Morris
  - Gaurav Vaidya
  - Phil Owen
  - Jason Reilly
  - Karamarie Fecho
  - Patrick Wang
  - Yaphet Kebede
  - E. Kathleen Carter
  - Chris Bizon
  doi: 10.48550/arXiv.2601.10008
  id: doi:10.48550/arXiv.2601.10008
  journal: arXiv
  preferred: true
  title: 'The "I" in FAIR: Translating from Interoperability in Principle to Interoperation
    in Practice'
  year: '2026'
repository: https://github.com/NCATSTranslator/Babel
synonyms:
- NCATS Babel
- Translator Babel
version: 2026jul22
---
# Babel

Babel builds cliques of equivalent identifiers across biomedical vocabularies for the NCATS Biomedical Data Translator. It reads identifiers and cross-references from sources such as UniProtKB, PubChem, NCBI Gene, Ensembl, UMLS, ChEMBL, MeSH, ChEBI, the OBO ontologies and DrugBank, merges them into cliques by Biolink type, and picks a preferred identifier and label for each clique. RRID: SCR_028595.

## Releases

Downloads live at <https://stars.renci.org/var/babel_outputs/>, with one directory per release. The `latest/` directory pointed to release 2026jul22 when checked on 2026-10-04 (its `VERSION.txt` says so). That release was built with Babel about v1.18.1 against Biolink Model 4.4.3 and holds 605,864,191 CURIEs in 388,490,111 cliques. The release notes are in the repository under `releases/2026jul22/`. UniProtKB, PubChem compounds, InChIKeys and NCBI Gene make up most identifiers.

Each release contains `compendia/`, `synonyms/`, `conflation/`, `kgx/` and `duckdb/` directories, plus reports, benchmarks and logs. The compendia and conflation files use a custom JSON Lines format described in `docs/DataFormats.md`, even though they carry a `.txt` extension.

## Use

Babel outputs are loaded into the Translator [Node Normalizer](https://nodenormalization-sri.renci.org/docs) (NodeNorm), which maps identifiers to preferred CURIEs, and the [Name Resolver](https://name-resolution-sri.renci.org/docs) (NameRes), which looks up concepts by name.

The code is under the MIT license. The release outputs carry no separate data license, and individual sources keep their own terms.
