---
activity_status: active
category: DataSource
creation_date: '2026-01-28T00:00:00Z'
description: A curated classification database of membrane transport proteins, organized
  by the Transporter Classification (TC) system and supporting sequence- and family-level
  exploration.
domains:
- biological systems
- proteomics
homepage_url: https://www.tcdb.org/
id: tcdb
last_modified_date: '2026-02-15T00:00:00Z'
layout: resource_detail
name: Transporter Classification Database (TCDB)
products:
- category: GraphicalInterface
  description: Main web interface for browsing transporter families, proteins, and
    curated annotations.
  format: http
  id: tcdb.portal
  name: TCDB Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/
- category: GraphicalInterface
  description: Sequence similarity search interface against TCDB transporter sequences.
  format: http
  id: tcdb.blast
  name: TCDB BLAST
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/progs/blast.php
- category: Product
  description: Complete TCDB protein sequence export.
  format: fasta
  id: tcdb.download.fasta
  name: TCDB Protein Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_file_size: 13590695
  product_url: https://www.tcdb.org/public/tcdb
- category: Product
  compression: targz
  description: Precomputed tcDoms dataset archive.
  format: mixed
  id: tcdb.download.tcdoms
  name: tcDoms Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_file_size: 14664403
  product_url: https://www.tcdb.org/public/tcDoms.tar.gz
- category: Product
  description: Tab-delimited table mapping TC systems to substrate identifiers. The
    URL ends in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.substrates
  name: TC Systems to Substrates Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/substrates/getSubstrates.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: Timeout connecting
    to URL'
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: Product
  description: Tab-delimited table with TC family definitions. The URL ends in .py,
    but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.families
  name: TC Family Definitions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_file_size: 41693
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/families.py
- category: Product
  description: Tab-delimited table mapping sequence accessions to TC identifiers.
    The URL ends in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.refseq
  name: Sequence Accessions to TCIDs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/refseq.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: Product
  description: Tab-delimited table mapping systems, subfamilies, and families to superfamilies.
    The URL ends in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.superfamilies
  name: TC Superfamily Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_file_size: 41446
  product_url: https://www.tcdb.org/cgi-bin/substrates/listSuperfamilies.py
- category: Product
  description: Tab-delimited table mapping protein accessions to TC identifiers. The
    URL ends in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.acc2tcid
  name: Accessions to TCIDs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/acc2tcid.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: Product
  description: Tab-delimited annotation mapping table for TC systems. The URL ends
    in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.go
  name: TC Annotation Mapping Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/go.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: Product
  description: Tab-delimited structure mapping table for TC systems. The URL ends
    in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.pdb
  name: TC Structure Mapping Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/pdb.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: Product
  description: Tab-delimited protein family mapping table for TC systems. The URL
    ends in .py, but this endpoint serves data, not Python source code.
  format: tsv
  id: tcdb.download.pfam
  name: TC Protein Family Mapping Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcdb
  product_url: https://www.tcdb.org/cgi-bin/projectv/public/pfam.py
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-23: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
synonyms:
- TCDB
- Transporter Classification Database
---
# Transporter Classification Database (TCDB)

TCDB is a curated classification resource for membrane transport proteins that organizes
transport systems into a hierarchical transporter classification scheme.