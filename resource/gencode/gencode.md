---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: gencode-help@ebi.ac.uk
  - contact_type: url
    value: https://www.gencodegenes.org/pages/contact.html
  label: GENCODE Helpdesk
creation_date: '2025-11-26T00:00:00Z'
description: GENCODE is a comprehensive and high-quality reference annotation of the
  human and mouse genomes, providing evidence-based gene annotations including protein-coding
  genes, long non-coding RNAs, small RNAs, pseudogenes, and other genomic features
  based on manual curation and computational analysis.
domains:
- genomics
- non-coding RNA
homepage_url: https://www.gencodegenes.org/
id: gencode
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
name: GENCODE
products:
- category: Product
  compression: gzip
  description: Current comprehensive GENCODE gene annotations for the human GRCh38.p14
    genome assembly (reference chromosomes only) in GTF format. Release 50 corresponds
    to Ensembl 116.
  format: gff
  id: gencode.human.gtf
  latest_version: '50'
  name: GENCODE Human Annotations GTF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 124527720
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.annotation.gtf.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: hgnc
  - relation_type: prov:wasInformedBy
    source: ncbigene
- category: Product
  compression: gzip
  description: Current comprehensive GENCODE gene annotations for the human GRCh38.p14
    genome assembly (reference chromosomes only) in GFF3 format.
  format: gff
  id: gencode.human.gff3
  latest_version: '50'
  name: GENCODE Human Annotations GFF3
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 160590749
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.annotation.gff3.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
- category: Product
  compression: gzip
  description: Nucleotide sequences of all GENCODE human transcripts on the GRCh38
    reference chromosomes, in FASTA format.
  format: fasta
  id: gencode.human.transcripts
  latest_version: '50'
  name: GENCODE Human Transcript Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 183554921
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.transcripts.fa.gz
- category: Product
  compression: gzip
  description: Amino acid sequences of GENCODE human protein-coding transcript translations
    on the GRCh38 reference chromosomes, in FASTA format.
  format: fasta
  id: gencode.human.translations
  latest_version: '50'
  name: GENCODE Human Protein Translations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 21136991
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.pc_translations.fa.gz
- category: Product
  compression: gzip
  description: Current comprehensive GENCODE human annotation mapped back to the older
    GRCh37 assembly, in GTF format.
  format: gff
  id: gencode.human.grch37.gtf
  latest_version: 50lift37
  name: GENCODE Human Annotations Lifted to GRCh37 GTF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 159680082
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/GRCh37_mapping/gencode.v50lift37.annotation.gtf.gz
- category: MappingProduct
  compression: gzip
  description: Mapping of GENCODE human transcripts to HGNC approved gene symbols,
    from the Ensembl xref pipeline. Companion metadata files in the same release
    map transcripts to NCBI Gene (Entrez) IDs, RefSeq, UniProtKB/Swiss-Prot and
    TrEMBL, PDB, and PubMed IDs.
  format: tsv
  id: gencode.human.metadata.hgnc
  latest_version: '50'
  name: GENCODE Human HGNC Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:wasInformedBy
    source: hgnc
  - relation_type: prov:wasInformedBy
    source: ncbigene
  - relation_type: prov:wasInformedBy
    source: refseq
  - relation_type: prov:wasInformedBy
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: pdb
  - relation_type: prov:wasInformedBy
    source: pubmed
  product_file_size: 2698457
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.metadata.HGNC.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
- category: Product
  compression: gzip
  description: Current comprehensive GENCODE gene annotations for the mouse GRCm39
    genome assembly (reference chromosomes only) in GTF format. Release M39 corresponds
    to Ensembl 116.
  format: gff
  id: gencode.mouse.gtf
  latest_version: M39
  name: GENCODE Mouse Annotations GTF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 91730109
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M39/gencode.vM39.annotation.gtf.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: mgi
  - relation_type: prov:wasInformedBy
    source: ncbigene
- category: Product
  compression: gzip
  description: Current comprehensive GENCODE gene annotations for the mouse GRCm39
    genome assembly (reference chromosomes only) in GFF3 format.
  format: gff
  id: gencode.mouse.gff3
  latest_version: M39
  name: GENCODE Mouse Annotations GFF3
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 120486831
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M39/gencode.vM39.annotation.gff3.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
- category: Product
  compression: gzip
  description: Nucleotide sequences of all GENCODE mouse transcripts on the GRCm39
    reference chromosomes, in FASTA format.
  format: fasta
  id: gencode.mouse.transcripts
  latest_version: M39
  name: GENCODE Mouse Transcript Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 135512511
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M39/gencode.vM39.transcripts.fa.gz
- category: Product
  compression: gzip
  description: Amino acid sequences of GENCODE mouse protein-coding transcript translations
    on the GRCm39 reference chromosomes, in FASTA format.
  format: fasta
  id: gencode.mouse.translations
  latest_version: M39
  name: GENCODE Mouse Protein Translations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 16190224
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M39/gencode.vM39.pc_translations.fa.gz
- category: Product
  description: GENCODE Primary transcript set capturing minimal transcripts at protein
    coding genes
  format: gff
  id: gencode.primary
  latest_version: current
  name: GENCODE Primary Transcripts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_url: https://www.gencodegenes.org/pages/gencode_primary/
- category: Product
  description: GENCODE FTP site hosting all current and past human and mouse releases,
    with README files describing each file type.
  format: http
  id: gencode.ftp
  name: GENCODE FTP Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/
- category: DocumentationProduct
  description: GENCODE documentation on data access, file formats, tags, and biotypes,
    including links to Ensembl and UCSC Genome Browser views and track hubs for GENCODE
    annotation.
  format: http
  id: gencode.docs
  name: GENCODE Data Access Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: ucsc
  product_url: https://www.gencodegenes.org/pages/data_access.html
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Neo4j knowledge graph containing lncRNAs, protein-coding genes, regulatory
    interactions, and disease associations
  dump_format: neo4j
  format: neo4j
  id: lncrnalyzr.graph
  name: lncRNAlyzr Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lncrnalyzr
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: doid
  product_url: https://github.com/MaayanLab/lncRNAlyzr
- category: Product
  description: Current HuRI TSV file containing 52,569 systematically mapped binary
    human protein-protein interactions, provided as interacting Ensembl gene ID pairs
  format: tsv
  id: hrpimp.data
  latest_version: HuRI
  name: HuRI Protein-Protein Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 1681536
  product_url: https://www.interactome-atlas.org/data/HuRI.tsv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: hgnc
- category: Product
  description: Current HuRI PSI-MI formatted interaction file with detailed experimental
    information and isoform-specific ORF, transcript, and protein identifiers
  format: psi_mi_mitab
  id: hrpimp.huri.psi
  latest_version: HuRI
  name: HuRI PSI-MI Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 169848924
  product_url: https://www.interactome-atlas.org/data/HuRI.psi
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
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
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  format: http
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
- category: Product
  compression: zip
  description: Academic branch of dbNSFP (v5.4a at time of curation, about 50 GB),
    a ZIP of gzipped, tab-delimited per-chromosome variant tables, the gene table,
    column descriptions and the search_dbNSFP Java program. Variant tables are also
    offered as a single tabix-indexed BGZF file per genome build (GRCh37, GRCh38)
    for Ensembl VEP and SnpSift. Includes all upstream scores that are free for academic
    use. Free for academic and non-commercial users after registration with an institutional
    email; download links are issued on request.
  format: tsv
  id: dbnsfp.academic
  license:
    id: https://creativecommons.org/licenses/by-nc-nd/4.0/
    label: CC BY-NC-ND 4.0
  name: dbNSFP Academic Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/download
- category: Product
  compression: zip
  description: Commercial branch of dbNSFP (v5.4c at time of curation), in the same
    format as the academic branch but excluding CADD, VEST, M-CAP, MutScore, PolyPhen-2,
    PrimateAI and RGC Million Exome data, whose authors require separate commercial
    licenses. Available to subscribers under a paid license from Genos Bioinformatics.
  format: tsv
  id: dbnsfp.commercial
  license:
    id: https://www.dbnsfp.org/license
    label: Commercial license (Genos Bioinformatics LLC)
  name: dbNSFP Commercial Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/license
publications:
- authors:
  - Mudge JM
  - Carbonell-Sala S
  - Diekhans M
  - Martinez JG
  - Martin FJ
  - Frankish A
  doi: 10.1093/nar/gkae1078
  id: doi:10.1093/nar/gkae1078
  journal: Nucleic Acids Research
  preferred: true
  title: 'GENCODE 2025: reference gene annotation for human and mouse'
  year: '2025'
- authors:
  - Frankish A
  - Carbonell-Sala S
  - Diekhans M
  - Tress ML
  - Flicek P
  doi: 10.1093/nar/gkac1071
  id: doi:10.1093/nar/gkac1071
  journal: Nucleic Acids Research
  title: 'GENCODE: reference annotation for the human and mouse genomes in 2023'
  year: '2023'
- authors:
  - Harrow J
  - Frankish A
  - Gonzalez JM
  - Guigó R
  - Hubbard TJ
  doi: 10.1101/gr.135350.111
  id: doi:10.1101/gr.135350.111
  journal: Genome Research
  title: 'GENCODE: The reference human genome annotation for The ENCODE Project'
  year: '2012'
rrid: SCR_014966
synonyms:
- GENCODE
- Encyclopedia of genes and gene variants
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
version: 50 (human), M39 (mouse)
---
# GENCODE

## Overview

GENCODE (Encyclopedia of Genes and Gene Variants) is a scientific project aimed at identifying and classifying all gene features in the human and mouse genomes with high accuracy based on biological evidence. It provides comprehensive, evidence-based annotations that serve as a reference standard for genome interpretation and biomedical research.

## Mission

The goal of the GENCODE project is to identify and classify all gene features in the human and mouse genomes with high accuracy based on biological evidence, and to release these annotations for the benefit of biomedical research and genome interpretation.

## Key Features

- **Comprehensive Annotations**: Protein-coding genes, long non-coding RNAs (lncRNAs), small RNAs, pseudogenes, and other genomic features
- **Evidence-Based**: Combines manual curation with computational analysis
- **Regular Updates**: New human and mouse releases issued in step with Ensembl releases
- **High Quality**: Integrates experimental data including Capture Long-read Sequencing
- **Global Core Biodata Resource**: Recognized as essential infrastructure for life sciences research

## Current Releases (June 2026)

- **GENCODE 50**: Human annotation on GRCh38.p14 (Ensembl 116); also provided lifted back to GRCh37
- **GENCODE M39**: Mouse annotation on GRCm39 (Ensembl 116)

Human and mouse releases are made together with Ensembl releases. The current release history is at https://www.gencodegenes.org/human/releases.html and https://www.gencodegenes.org/mouse/releases.html.

## Annotation Types

### Protein-Coding Genes
- Comprehensive transcript annotations
- Alternative splicing isoforms
- Coding sequence (CDS) definitions
- Translation information

### Non-Coding RNAs
- **Long non-coding RNAs (lncRNAs)**: Significantly expanding through Capture Long-read Sequencing project integration
- **Small RNAs**: miRNAs, snoRNAs, snRNAs
- **Pseudogenes**: Processed and unprocessed pseudogenes

### Special Annotation Sets

- **GENCODE Primary**: Minimal set of transcripts at protein-coding genes
- **Promoter Windows**: First catalog of human promoter windows
- **Ribo-seq ORFs**: Non-canonical human ORFs predicted by ribosome profiling data, including peptidomics and immunopeptidomics integration

## Data Formats

- **GTF/GFF3**: Comprehensive, basic, primary-assembly, and patch/haplotype/scaffold annotation sets, plus subsets for lncRNAs, polyA features, tRNAs, pseudogenes, and promoter windows
- **FASTA**: Transcript, protein-coding transcript, lncRNA transcript, and protein translation sequences, plus the genome sequence
- **Metadata**: Tab-separated cross-references from transcripts to HGNC, NCBI Gene (Entrez), RefSeq, UniProtKB/Swiss-Prot and TrEMBL, PDB, and PubMed, plus supporting-evidence and source tables

## Applications

- RNA-seq analysis and transcript quantification
- Variant annotation and interpretation
- Comparative genomics
- Functional genomics studies
- Gene expression analysis
- Knowledge graph construction (UBKG)
- Clinical genomics and precision medicine

## Integration

The current GENCODE release is the default gene set in the Ensembl Genome Browser for human and mouse, and the UCSC Genome Browser hosts selected GENCODE releases as tracks. GENCODE annotations are also used by many other resources and projects, including UBKG (Unified Biomedical Knowledge Graph), GTEx (Genotype-Tissue Expression), and RNA-seq analysis pipelines. GENCODE collaborates with NCBI on the CCDS project.

## Consortium Members

Current participating institutions (per https://www.gencodegenes.org/pages/gencode.html):

- EMBL-EBI (European Bioinformatics Institute), lead institution
- CRG (Centre for Genomic Regulation, Barcelona)
- MIT (Massachusetts Institute of Technology)
- Yale University
- UCSC (University of California, Santa Cruz)
- CNIO (Spanish National Cancer Research Centre)
- Stanford University

The project began at the Wellcome Sanger Institute as part of ENCODE before moving to EMBL-EBI.

## Funding

GENCODE is supported by the National Human Genome Research Institute (NHGRI) of the US National Institutes of Health, through a series of grants beginning in 2003 under ENCODE, with later grants in 2013, 2017, and 2021.

## Access

- **Website**: https://www.gencodegenes.org/
- **Downloads**: https://ftp.ebi.ac.uk/pub/databases/gencode/ (human and mouse; `latest_release` points to the current release)
- **Data access guide**: https://www.gencodegenes.org/pages/data_access.html
- **Genome Browsers**: Via Ensembl and UCSC, including GENCODE track hubs
- **Helpdesk**: gencode-help@ebi.ac.uk

## Citation

When using GENCODE data, cite the most recent GENCODE paper (currently Mudge et al., GENCODE 2025, Nucleic Acids Research, doi:10.1093/nar/gkae1078) and state the release number used.

## License

GENCODE data are freely available. The website and FTP site are provided under the EMBL-EBI Terms of Use; no separate data license is stated.