---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.grnpedia.org/trrust/
  label: Network Biology Laboratory, Yonsei University
creation_date: '2026-06-18T00:00:00Z'
description: TRRUST (Transcriptional Regulatory Relationships Unraveled by Sentence-based
  Text mining) is a manually curated database of human and mouse transcriptional regulatory
  networks. Its interactions are extracted from sentences in PubMed abstracts using
  sentence-based text mining followed by manual expert curation, capturing transcription
  factor (TF) to target-gene relationships along with the mode of regulation (activation,
  repression, or unknown). The v2 release contains 8,444 human and 6,552 mouse TF-target
  regulatory interactions derived from over 11,000 PubMed articles, each linked to
  the supporting literature evidence. TRRUST serves as an upstream primary source
  for derived regulatory-network resources such as DoRothEA.
domains:
- genomics
- systems biology
- gene regulation
- literature
- natural language processing
homepage_url: https://www.grnpedia.org/trrust/
id: trrust
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: Creative Commons Attribution-ShareAlike 4.0 International
name: TRRUST
products:
- category: Product
  description: TRRUST web resource for browsing and searching manually curated human
    and mouse transcription factor-target regulatory interactions.
  format: http
  id: trrust.web
  name: TRRUST Web Resource
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_url: https://www.grnpedia.org/trrust/
- category: Product
  description: TRRUST v2 human transcription factor-target regulatory interactions
    in tab-separated format, with TF, target gene, mode of regulation, and supporting
    PubMed identifiers.
  format: tsv
  id: trrust.human.tsv
  name: TRRUST Human Interactions (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_file_size: 297659
  product_url: https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv
- category: Product
  description: TRRUST v2 mouse transcription factor-target regulatory interactions
    in tab-separated format, with TF, target gene, mode of regulation, and supporting
    PubMed identifiers.
  format: tsv
  id: trrust.mouse.tsv
  name: TRRUST Mouse Interactions (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_file_size: 220353
  product_url: https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv
- category: GraphProduct
  description: Core TF–target regulon knowledge graph (multi-species) with confidence
    levels (A–E)
  format: r
  id: dorothea.graph
  name: DoRothEA Regulon Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
- category: Product
  description: Download page listing interaction tables, MITAB files, GMT gene sets,
    and binding site tables, GFF3 annotations, and FASTA sequences for each organism,
    split into small-scale, large-scale, and combined evidence.
  format: http
  id: tflink.downloads
  name: TFLink Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_url: https://tflink.net/download/
- category: GraphProduct
  compression: gzip
  description: All TF-target gene interactions for Homo sapiens (small- and large-scale
    evidence combined), with UniProt IDs, NCBI Gene IDs, and names of TF and target,
    detection methods, PubMed IDs, source databases, and a small-scale flag.
  format: tsv
  id: tflink.interactions.human
  name: TFLink Human Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 309414866
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_interactions_All_simpleFormat_v1.0.tsv.gz
- category: GraphProduct
  compression: gzip
  description: All TF-target gene interactions for Mus musculus (small- and large-scale
    evidence combined), with UniProt IDs, NCBI Gene IDs, and names of TF and target,
    detection methods, PubMed IDs, source databases, and a small-scale flag.
  format: tsv
  id: tflink.interactions.mouse
  name: TFLink Mouse Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 175017529
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Mus_musculus_interactions_All_simpleFormat_v1.0.tsv.gz
- category: GraphProduct
  description: All TF-target gene interactions for Rattus norvegicus (small- and large-scale
    evidence combined), with UniProt IDs, NCBI Gene IDs, and names of TF and target,
    detection methods, PubMed IDs, source databases, and a small-scale flag.
  format: tsv
  id: tflink.interactions.rat
  name: TFLink Rat Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 13039333
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Rattus_norvegicus_interactions_All_simpleFormat_v1.0.tsv
- category: GraphProduct
  description: All TF-target gene interactions for Danio rerio (small- and large-scale
    evidence combined), with UniProt IDs, NCBI Gene IDs, and names of TF and target,
    detection methods, PubMed IDs, source databases, and a small-scale flag.
  format: tsv
  id: tflink.interactions.zebrafish
  name: TFLink Zebrafish Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 3475764
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Danio_rerio_interactions_All_simpleFormat_v1.0.tsv
- category: GraphProduct
  description: All TF-target gene interactions for Drosophila melanogaster (small-
    and large-scale evidence combined), with UniProt IDs, NCBI Gene IDs, and names
    of TF and target, detection methods, PubMed IDs, source databases, and a small-scale
    flag.
  format: tsv
  id: tflink.interactions.fly
  name: TFLink Fruit Fly Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 56515864
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Drosophila_melanogaster_interactions_All_simpleFormat_v1.0.tsv
- category: GraphProduct
  description: All TF-target gene interactions for Caenorhabditis elegans (small-
    and large-scale evidence combined), with UniProt IDs, NCBI Gene IDs, and names
    of TF and target, detection methods, PubMed IDs, source databases, and a small-scale
    flag.
  format: tsv
  id: tflink.interactions.worm
  name: TFLink Nematode Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 48412163
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Caenorhabditis_elegans_interactions_All_simpleFormat_v1.0.tsv
- category: GraphProduct
  description: All TF-target gene interactions for Saccharomyces cerevisiae (small-
    and large-scale evidence combined), with UniProt IDs, NCBI Gene IDs, and names
    of TF and target, detection methods, PubMed IDs, source databases, and a small-scale
    flag.
  format: tsv
  id: tflink.interactions.yeast
  name: TFLink Yeast Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 44170257
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Saccharomyces_cerevisiae_interactions_All_simpleFormat_v1.0.tsv
- category: GraphProduct
  compression: gzip
  description: All human TF-target gene interactions in PSI-MI MITAB 2.8 format.
  format: psi_mi_mitab
  id: tflink.interactions.human.mitab
  name: TFLink Human Interactions (MITAB)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 229583092
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_interactions_All_mitab_v1.0.tsv.gz
- category: Product
  description: Human gene sets, one per transcription factor, listing its target genes
    by NCBI Gene ID, in GMT format. Versions keyed by UniProt ID and protein name
    are also offered.
  format: tsv
  id: tflink.gmt.human
  name: TFLink Human TF Target Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 37812545
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_interactions_All_GMT_ncbiGeneID_v1.0.gmt
- category: Product
  compression: gzip
  description: Genomic locations of human TF binding sites, with the binding TF, target
    gene, and source database.
  format: tsv
  id: tflink.binding-sites.human
  name: TFLink Human Binding Sites
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 160559406
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_bindingSites_All_annotation_v1.0.tsv.gz
- category: Product
  description: Human TF binding site locations as a GFF3 annotation file.
  format: gff
  id: tflink.binding-sites.human.gff3
  name: TFLink Human Binding Sites (GFF3)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 958134562
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_bindingSites_All_annotation_v1.0.gff3
- category: Product
  description: Nucleotide sequences of human TF binding sites in FASTA format.
  format: fasta
  id: tflink.binding-sites.human.fasta
  name: TFLink Human Binding Site Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: redfly
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_file_size: 1138803022
  product_url: https://cdn.netbiol.org/tflink/download_files/TFLink_Homo_sapiens_bindingSites_All_v1.0.fasta
- category: Product
  description: Downloadable Enrichr gene set libraries (more than 200 libraries across
    transcription, pathways, ontologies, diseases/drugs, cell types, crowd-contributed,
    and legacy categories), each retrievable as a GMT-style tab-delimited text file
    via the geneSetLibrary endpoint (e.g. geneSetLibrary?mode=text&libraryName=KEGG_2021_Human).
    Libraries are compiled from external databases including GO, KEGG, Reactome, WikiPathways,
    MSigDB, ChEA/ENCODE, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, OMIM, GWAS Catalog,
    HPO, MGI, CellMarker, and others.
  format: txt
  id: enrichr.libraries
  name: Enrichr Gene Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://maayanlab.cloud/Enrichr/#libraries
publications:
- authors:
  - Han H
  - Cho JW
  - Lee S
  - Yun A
  - Kim H
  - Bae D
  - Yang S
  - Kim CY
  - Lee M
  - Kim E
  - Lee S
  - Kang B
  - Jeong D
  - Kim Y
  - Jeon HN
  - Jung H
  - Nam S
  - Chung M
  - Kim JH
  - Lee I
  doi: 10.1093/nar/gkx1013
  id: https://www.ncbi.nlm.nih.gov/pubmed/29087512
  journal: Nucleic Acids Res
  preferred: true
  title: 'TRRUST v2: an expanded reference database of human and mouse transcriptional
    regulatory interactions'
  year: '2018'
rrid: SCR_022554
---
# TRRUST

TRRUST is a manually curated data source of human and mouse transcriptional regulatory
interactions, providing transcription factor-target relationships with their mode of
regulation and supporting literature evidence. It is an upstream primary source of
derived regulatory-network resources such as DoRothEA.