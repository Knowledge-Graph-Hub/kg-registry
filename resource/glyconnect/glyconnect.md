---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: glyconnect@sib.swiss
  - contact_type: url
    value: https://glyconnect.expasy.org/
  id: sib
  label: GlyConnect Team - SIB Swiss Institute of Bioinformatics
creation_date: '2025-05-07T00:00:00Z'
description: GlyConnect is a knowledgebase of glycoproteins spanning protein, glycosite
  and glycan information, with data on various species, tissues, and disease associations.
domains:
- biological systems
- chemistry and biochemistry
homepage_url: https://glyconnect.expasy.org/
id: glyconnect
last_modified_date: '2025-12-07T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: GlyConnect
products:
- category: GraphicalInterface
  description: Web interface for exploring GlyConnect data
  id: glyconnect.site
  is_public: true
  name: GlyConnect Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  product_url: https://glyconnect.expasy.org/
- category: ProgrammingInterface
  description: RESTful API for accessing GlyConnect data
  id: glyconnect.api.rest
  is_public: true
  name: GlyConnect RESTful API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  product_url: https://glyconnect.expasy.org/api
- category: ProgrammingInterface
  description: SPARQL endpoint for querying GlyConnect RDF data
  id: glyconnect.api.sparql
  is_public: true
  name: GlyConnect SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  product_url: https://glyconnect.expasy.org/rdf
- category: Product
  description: Compositions dataset containing glycan compositions
  format: csv
  id: glyconnect.compositions
  name: GlyConnect Glycan Compositions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  product_url: https://glyconnect.expasy.org/downloads/compositions/
- category: Product
  description: Immunoglobulins dataset containing glycans commonly found on immunoglobulins
  format: csv
  id: glyconnect.immunoglobulins
  name: GlyConnect Immunoglobulins Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  product_url: https://glyconnect.expasy.org/downloads/Immunoglobulins/
- category: Product
  description: Sample RDF data files demonstrating GlycoCoO usage with examples from
    UniCarbKB, GlyConnect, and GlycoNAVI
  format: http
  id: glycocoo.rdf-samples
  name: GlycoCoO RDF Sample Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  product_url: https://github.com/glycoinfo/GlycoCoO/tree/master/RDF_Sample
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: glycordf
  - relation_type: prov:wasInformedBy
    source: unicarbkb
  - relation_type: prov:wasInformedBy
    source: glyconnect
  - relation_type: prov:wasInformedBy
    source: glyconavi
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
publications:
- authors:
  - Alocci D
  - Mariethoz J
  - Gastaldello A
  - Gasteiger E
  - Karlsson NG
  - Kolarich D
  - Packer NH
  - Lisacek F
  doi: 10.1021/acs.jproteome.8b00766
  id: doi:10.1021/acs.jproteome.8b00766
  journal: Journal of Proteome Research
  title: 'GlyConnect: Glycoproteomics Goes Visual, Interactive, and Analytical'
  year: '2019'
---
GlyConnect is a comprehensive knowledgebase of glycoproteomics data maintained by the SIB Swiss Institute of Bioinformatics. It integrates information spanning three key levels of glycobiology: proteins, glycosites (the specific locations where glycans attach to proteins), and glycan structures.

The database provides curated glycoproteomic data from various species, tissues, and disease states, with a particular focus on human glycoproteins. GlyConnect uses the Symbol Nomenclature for Glycans (SNFG) standard for representing glycan structures in a visually consistent way.

Key features of GlyConnect include:

- Integration of glycoprotein data across multiple species
- Mapping of glycan structures to specific attachment sites on proteins
- Association of glycan profiles with diseases and tissues
- Specialized datasets for important glycoprotein families (e.g., immunoglobulins)
- Human milk oligosaccharide (HMO) data
- COVID-19 related glycosylation data
- O-linked monosaccharide information

GlyConnect serves as a valuable resource for researchers in glycobiology, proteomics, and biomedical sciences by providing a unified view of the complex relationships between proteins and their glycosylation patterns. The database is regularly updated and expanded to include new glycoproteomic data.

Access to GlyConnect is provided through a user-friendly web interface, programmatic access via RESTful and SPARQL APIs, and bulk downloads of specialized datasets.