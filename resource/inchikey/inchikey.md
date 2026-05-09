---
activity_status: active
category: DataModel
creation_date: '2026-02-18T00:00:00Z'
description: InChIKey is a fixed-length hashed representation of the IUPAC International Chemical Identifier (InChI), used for indexing and linking chemical structures across resources.
domains:
  - chemistry and biochemistry
  - drug discovery
homepage_url: https://www.inchi-trust.org/
id: inchikey
last_modified_date: '2026-02-18T00:00:00Z'
layout: resource_detail
name: InChIKey
products:
  - category: DocumentationProduct
    description: InChI Trust documentation and supporting material for the InChI/InChIKey identifier standard.
    format: http
    id: inchikey.docs
    name: InChI/InChIKey Documentation
    original_source:
      - source: inchikey
        relation_type: prov:hadPrimarySource
    product_url: https://www.inchi-trust.org/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
synonyms:
  - InChI key
  - IUPAC InChIKey
---

# InChIKey

InChIKey is a compact chemical structure identifier used broadly for interoperability.
