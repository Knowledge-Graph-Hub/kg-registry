---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: tflink.net@gmail.com
  - contact_type: url
    value: https://tflink.net/
  label: TFLink team
- category: Individual
  contact_details:
  - contact_type: email
    value: arieszter@gmail.com
  label: Eszter Ari
- category: Individual
  contact_details:
  - contact_type: email
    value: Tamas.Korcsmaros@earlham.ac.uk
  label: Tamás Korcsmáros
creation_date: '2026-10-10T00:00:00Z'
description: TFLink is an integrated gateway to transcription factor (TF) to target
  gene interactions, TF binding site locations, and binding site sequences for human
  and six model organisms (mouse, rat, zebrafish, fruit fly, nematode, and yeast).
  It integrates small-scale and large-scale experimental evidence from ten source
  databases, including TRRUST, GTRD, ReMap, JASPAR, and DoRothEA, recording the source
  database, detection method, and PubMed IDs for each record. Version 1.0 holds about
  11.8 million interactions between 3,984 TFs and 110,808 target genes, available
  through a web interface and as downloadable tables and MITAB, GMT, GFF3, and FASTA
  files.
domains:
- gene regulation
- genomics
- model organisms
- organisms
homepage_url: https://tflink.net/
id: tflink
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://tflink.net/faq/
  label: Free for non-commercial use
name: TFLink
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching TF-target interactions by
    organism, gene name, UniProt ID, NCBI Gene ID, role (TF or target), and evidence
    scale, with an entry page for each gene.
  format: http
  id: tflink.browse
  name: TFLink Browse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  product_url: https://tflink.net/browse/
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
- category: DocumentationProduct
  description: Frequently asked questions covering file formats, source database versions
    and download dates, terms of use, and the project team.
  format: http
  id: tflink.faq
  name: TFLink FAQ
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  product_url: https://tflink.net/faq/
- category: ProcessProduct
  description: Source code of the TFLink website.
  format: http
  id: tflink.website-code
  name: TFLink Website Source
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tflink
  product_url: https://github.com/NetBiol/TFlink
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
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
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
publications:
- authors:
  - Liska O
  - Bohár B
  - Hidas A
  - Korcsmáros T
  - Papp B
  - Fazekas D
  - Ari E
  doi: 10.1093/database/baac083
  id: PMID:36124642
  journal: Database (Oxford)
  preferred: true
  title: 'TFLink: an integrated gateway to access transcription factor-target gene
    interactions for multiple species'
  year: '2022'
repository: https://github.com/NetBiol/TFlink
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:7955
- NCBITaxon:7227
- NCBITaxon:6239
- NCBITaxon:4932
version: '1.0'
---
# TFLink

TFLink gathers transcription factor (TF) to target gene interactions and TF binding sites for human and six model organisms in one place. It was developed by researchers at the Biological Research Centre Szeged, Eötvös Loránd University, and the Earlham Institute, and is described in Liska et al. 2022 (Database).

## Data

Version 1.0 combines records from ten source databases: DoRothEA, GTRD, HTRIdb, JASPAR, ORegAnno, REDfly, ReMap, TRED, TRRUST, and Yeastract. Each interaction keeps its source database, detection method, and PubMed IDs, and is flagged as small-scale (low-throughput) or large-scale (high-throughput) evidence. Proteins and genes are identified by UniProt and NCBI Gene IDs. Human has the most data, about 6.7 million interactions among 1,606 TFs and 20,139 targets, followed by mouse (about 4.1 million). Zebrafish has only large-scale data.

## Access

Interactions can be browsed and searched on the website or downloaded per organism as simple tables, PSI-MI MITAB 2.8, and GMT gene sets. Binding sites are downloadable as tables, GFF3 annotations, and FASTA sequences. Each file type is split into small-scale, large-scale, and combined sets. The download files date from April 2022. The FAQ states that TFLink is freely available for non-commercial use.