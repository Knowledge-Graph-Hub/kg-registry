---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@yeastract.com
  - contact_type: url
    value: https://yeastract-plus.org/yeastract/scerevisiae/contact.php
  label: YEASTRACT+ team, Instituto Superior Técnico, Universidade de Lisboa
- category: Individual
  contact_details:
  - contact_type: email
    value: pedro.tiago.monteiro@tecnico.ulisboa.pt
  label: Pedro T Monteiro
- category: Individual
  contact_details:
  - contact_type: email
    value: mnpct@tecnico.ulisboa.pt
  label: Miguel C Teixeira
creation_date: '2026-10-10T00:00:00Z'
description: YEASTRACT (Yeast Search for Transcriptional Regulators And Consensus
  Tracking) is a curated repository of documented regulatory associations between
  transcription factors (TFs) and target genes, and of TF binding sites, in Saccharomyces
  cerevisiae, compiled by manual curation of the published literature. It is now part
  of the YEASTRACT+ portal, which also hosts PathoYeastract (pathogenic Candida species
  and Cryptococcus neoformans), N.C.Yeastract (non-conventional biotechnological yeasts),
  and CommunityYeastract (automatically generated databases for further species and
  strains). YEASTRACT+ provides tools to search regulators, targets, and associations,
  analyze promoter motifs, rank genes by TF or GO term, compare regulatory networks
  across species through orthology, and combine regulatory data with genome-scale
  metabolic models. In 2023 the portal held over 300,000 documented regulatory associations
  across 11 yeast species, about 215,000 of them for S. cerevisiae.
domains:
- gene regulation
- genomics
- microbiology
- model organisms
- organisms
homepage_url: https://yeastract-plus.org/
id: yeastract
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://yeastract-plus.org/termsusage.php
  label: YEASTRACT+ Terms of Usage
name: YEASTRACT
products:
- category: GraphicalInterface
  description: YEASTRACT+ portal giving access to the Yeastract, PathoYeastract, N.C.Yeastract,
    and CommunityYeastract databases and cross-species tools for transcription regulation
    analysis in yeasts.
  format: http
  id: yeastract.portal
  name: YEASTRACT+ Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_url: https://yeastract-plus.org/
- category: GraphicalInterface
  description: Yeastract web interface for Saccharomyces cerevisiae, with searches
    for TFs, target genes, and regulatory associations, DNA motif searches, promoter
    analysis, regulation matrix generation, and ranking of genes by TF or GO term.
    Associations are manually curated from the literature; gene and GO annotations
    come from SGD.
  format: http
  id: yeastract.scerevisiae
  name: Yeastract (S. cerevisiae)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  product_url: https://yeastract-plus.org/yeastract/scerevisiae/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: sgd
  - relation_type: prov:wasInformedBy
    source: go
- category: GraphicalInterface
  description: PathoYeastract web interface with curated TF-target gene regulatory
    associations for pathogenic yeasts (Candida glabrata, C. albicans, C. tropicalis,
    C. parapsilosis, C. auris, and Cryptococcus neoformans). Associations are manually
    curated from the literature; GO annotations for Candida genes come from the Candida
    Genome Database.
  format: http
  id: yeastract.pathoyeastract
  name: PathoYeastract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  product_url: https://yeastract-plus.org/pathoyeastract/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: candida-genome-database
  - relation_type: prov:wasInformedBy
    source: go
- category: GraphicalInterface
  description: N.C.Yeastract web interface with curated TF-target gene regulatory
    associations for non-conventional yeasts (Zygosaccharomyces bailii, Kluyveromyces
    lactis, K. marxianus, Yarrowia lipolytica, Komagataella phaffii, and Rhodotorula
    toruloides), curated from the literature.
  format: http
  id: yeastract.ncyeastract
  name: N.C.Yeastract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  product_url: https://yeastract-plus.org/ncyeastract/
- category: GraphicalInterface
  description: CommunityYeastract, a set of automatically generated YEASTRACT-like
    databases for additional yeast species and strains (such as Saccharomyces boulardii
    strains and Schizosaccharomyces pombe 972h-) that predict regulation from homologous
    genes in the curated YEASTRACT+ databases.
  format: http
  id: yeastract.community
  name: CommunityYeastract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yeastract
  product_url: https://yeastract-plus.org/community/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pombase
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
publications:
- authors:
  - Teixeira MC
  - Viana R
  - Palma M
  - Oliveira J
  - Galocha M
  - Mota MN
  - Couceiro D
  - Pereira MG
  - Antunes M
  - Costa IV
  - Pais P
  - Parada C
  - Chaouiya C
  - Sá-Correia I
  - Monteiro PT
  doi: 10.1093/nar/gkac1041
  id: PMID:36350610
  journal: Nucleic Acids Res
  preferred: true
  title: 'YEASTRACT+: a portal for the exploitation of global transcription regulation
    and metabolic model data in yeast biotechnology and pathogenesis'
  year: '2023'
- authors:
  - Monteiro PT
  - Oliveira J
  - Pais P
  - Antunes M
  - Palma M
  - Cavalheiro M
  - Galocha M
  - Godinho CP
  - Martins LC
  - Bourbon N
  - Mota MN
  - Ribeiro RA
  - Viana R
  - Sá-Correia I
  - Teixeira MC
  doi: 10.1093/nar/gkz859
  id: PMID:31586406
  journal: Nucleic Acids Res
  title: 'YEASTRACT+: a portal for cross-species comparative genomics of transcription
    regulation in yeasts'
  year: '2020'
- authors:
  - Teixeira MC
  - Monteiro PT
  - Palma M
  - Costa C
  - Godinho CP
  - Pais P
  - Cavalheiro M
  - Antunes M
  - Lemos A
  - Pedreira T
  - Sá-Correia I
  doi: 10.1093/nar/gkx842
  id: PMID:29036684
  journal: Nucleic Acids Res
  title: 'YEASTRACT: an upgraded database for the analysis of transcription regulatory
    networks in Saccharomyces cerevisiae'
  year: '2018'
- authors:
  - Teixeira MC
  - Monteiro P
  - Jain P
  - Tenreiro S
  - Fernandes AR
  - Mira NP
  - Alenquer M
  - Freitas AT
  - Oliveira AL
  - Sá-Correia I
  doi: 10.1093/nar/gkj013
  id: PMID:16381908
  journal: Nucleic Acids Res
  title: 'The YEASTRACT database: a tool for the analysis of transcription regulatory
    associations in Saccharomyces cerevisiae'
  year: '2006'
taxon:
- NCBITaxon:4932
- NCBITaxon:5478
- NCBITaxon:5476
- NCBITaxon:5482
- NCBITaxon:5480
- NCBITaxon:498019
- NCBITaxon:5207
- NCBITaxon:4954
- NCBITaxon:28985
- NCBITaxon:4911
- NCBITaxon:4952
- NCBITaxon:460519
- NCBITaxon:5286
---
# YEASTRACT

## Overview

YEASTRACT (Yeast Search for Transcriptional Regulators And Consensus Tracking) is a curated database of transcription regulation in *Saccharomyces cerevisiae*, first described in 2006. Since 2020 it has been part of the YEASTRACT+ portal, maintained at Instituto Superior Técnico, Universidade de Lisboa, and most recently described in Teixeira et al. 2023 (Nucleic Acids Research).

## Data Content

The portal holds documented regulatory associations between transcription factors (TFs) and target genes, along with TF binding sites, manually curated from the published literature. It covers four databases: Yeastract (*S. cerevisiae*, about 215,000 associations in 2023), PathoYeastract (*Candida glabrata*, *C. albicans*, *C. tropicalis*, *C. parapsilosis*, *C. auris*, and *Cryptococcus neoformans*), N.C.Yeastract (non-conventional yeasts such as *Yarrowia lipolytica*, *Kluyveromyces lactis*, and *Komagataella phaffii*), and CommunityYeastract, which generates databases for further species and strains from orthology without species-specific curated data. GO annotations come from SGD, the Candida Genome Database, and PomBase.

## Access

All data are accessed through the web interfaces, which provide searches for regulators, targets, and associations, DNA motif and promoter analysis, regulation matrices, cross-species comparisons through orthologs, and tools that combine regulatory data with genome-scale metabolic models. The flat-file download page currently lists no files and asks users to contact the team for specific data. The REST web services are no longer maintained.

## License

The YEASTRACT+ Terms of Usage state that there are no restrictions on use or redistribution of the data beyond those set by the original data owners (the authors of the curated articles). Users may not reproduce substantial parts of the content in ways that would compete with YEASTRACT+, and must cite the 2023 YEASTRACT+ publication.
