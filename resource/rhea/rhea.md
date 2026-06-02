---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: Rhea Team
creation_date: '2025-03-09T00:00:00Z'
description: Rhea is an expert-curated knowledgebase of chemical and transport reactions
  of biological interest.
domains:
- chemistry and biochemistry
homepage_url: https://www.rhea-db.org/
id: rhea
infores_id: rhea
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Rhea
products:
- category: Product
  description: rhea OBO
  format: obo
  id: obo-db-ingest.rhea.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 4826502
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.obo
- category: Product
  compression: gzip
  description: rhea OWL
  format: owl
  id: obo-db-ingest.rhea.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 7945039
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.owl.gz
- category: Product
  compression: gzip
  description: rhea OBO Graph JSON
  format: json
  id: obo-db-ingest.rhea.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 5228738
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.json.gz
- category: MappingProduct
  description: rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: m-csa
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
- category: ProgrammingInterface
  description: Plover-hosted TRAPI web API for querying the Multiomics Microbiome
    knowledge graph
  format: http
  id: microbiomekg.api
  is_public: true
  name: MicrobiomeKG Plover TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: eupathdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: microbiomekg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://multiomics.transltr.io/mbkp
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 12464495186
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-raw-20250222.tar.gz
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4623010863
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-function-20250222.tar.gz
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
- category: Product
  description: TSV export of lipid-related enzymes with UniProt, Rhea, and evidence
    links.
  format: tsv
  id: swisslipid.enzymes
  name: SwissLipids Enzymes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 126760
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=enzymes.tsv
- category: Product
  description: rhea Nodes TSV
  format: tsv
  id: obo-db-ingest.rhea.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 981824
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.tsv
publications:
- authors:
  - Bansal P
  - Morgat A
  - Axelsen KB
  - Muthukrishnan V
  - Coudert E
  - Aimo L
  - Hyka-Nouspikel N
  - Gasteiger E
  - Kerhornou A
  - Neto TB
  - Pozzato M
  - Blatter MC
  - Ignatchenko A
  - Redaschi N
  - Bridge A
  doi: doi:10.1093/nar/gkab1016
  id: doi:10.1093/nar/gkab1016
  preferred: true
  title: Rhea, the reaction knowledgebase in 2022
  year: '2021'
---
Rhea is an expert-curated knowledgebase of chemical and transport reactions of biological interest. Enzyme-catalyzed and spontaneously occurring reactions are curated from peer-reviewed literature and represented in a computationally tractable manner by using the ChEBI (Chemical Entities of Biological Interest) ontology to describe reaction participants.

Rhea covers the reactions described by the IUBMB Enzyme Nomenclature as well as many additional reactions and can be used for enzyme annotation, genome-scale metabolic modeling and omics-related analyses. Rhea is the standard for enzyme and transporter annotation in UniProtKB.