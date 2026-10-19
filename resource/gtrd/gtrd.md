---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: gtrd@biosoft.ru
  - contact_type: url
    value: https://gtrd.biouml.org/
  label: GTRD team (BIOSOFT.RU, Novosibirsk)
- category: Individual
  contact_details:
  - contact_type: email
    value: fedor@biouml.org
  label: Fedor Kolpakov
creation_date: '2026-10-10T00:00:00Z'
description: GTRD (Gene Transcription Regulation Database) is a database of uniformly
  annotated and processed next-generation sequencing data on gene transcription regulation,
  including ChIP-seq, ChIP-exo, DNase-seq, MNase-seq, ATAC-seq, FAIRE-seq, and RNA-seq
  from cells with altered transcription factor activity. Raw data are collected from
  GEO, SRA, ENCODE, and modENCODE, annotated with controlled vocabularies and ontologies,
  and processed with uniform workflows to produce transcription factor binding site
  peaks and meta-clusters, open chromatin regions and footprints, nucleosome positions,
  and predicted transcription factor target genes for nine species (human, mouse,
  rat, zebrafish, fruit fly, nematode, budding and fission yeast, and Arabidopsis).
  Data are available through a web interface, bulk downloads, and UCSC/Ensembl track
  hubs.
domains:
- gene regulation
- epigenomics
- genomics
- model organisms
- organisms
homepage_url: https://gtrd.biouml.org/
id: gtrd
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://wiki.biouml.org/index.php/GTRD
  label: Free for non-commercial use with citation; commercial use requires a license
name: GTRD
products:
- category: GraphicalInterface
  description: GTRD web interface for browsing and searching transcription factors,
    experiments, binding sites, meta-clusters, and target genes, with a built-in BioUML
    genome browser.
  format: http
  id: gtrd.portal
  name: GTRD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  product_url: https://gtrd.biouml.org/
- category: Product
  description: GTRD bulk download directory with plain-text results of uniform annotation
    and analysis, including experiment metadata, peak and meta-cluster intervals for
    ChIP-seq, ChIP-exo, DNase-seq, and MNase-seq, bigBed files, target gene lists,
    and genome browser track hubs. Raw data were obtained from GEO, SRA, ENCODE, and
    modENCODE.
  format: http
  id: gtrd.downloads
  name: GTRD Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: modencode
  product_url: https://gtrd.biouml.org/downloads/current/
- category: Product
  description: Per-species archives of transcription factor ChIP-seq peaks called
    with GEM, MACS2, PICS, and SISSRs on uniformly reprocessed ChIP-seq data from
    GEO, SRA, ENCODE, and modENCODE.
  format: http
  id: gtrd.chip-seq_peaks
  name: GTRD ChIP-seq Peaks
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: sra
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: modencode
  product_url: http://gtrd.biouml.org:8888/downloads/current/intervals/chip-seq/
- category: Product
  description: Per-species lists of transcription factor target genes and transcripts,
    one file per TF (named by UniProt ID), where a gene is a target if its promoter
    or gene body region contains a GTRD meta-cluster for that TF. Genes and transcripts
    are identified by Ensembl IDs.
  format: http
  id: gtrd.target_genes
  name: GTRD Transcription Factor Target Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  product_url: http://gtrd.biouml.org:8888/downloads/current/intervals/target_genes/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: uniprot
- category: Product
  description: UCSC-format track hub with GTRD bigBed and bigWig tracks for hg38,
    mm10, rn6, danRer11, dm6, ce11, sacCer3, S. pombe, and TAIR10 genome assemblies,
    viewable in the UCSC and Ensembl genome browsers.
  format: txt
  id: gtrd.track_hub
  name: GTRD Track Hub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrd
  product_file_size: 136
  product_url: http://gtrd.biouml.org:8888/downloads/current/gtrdHub/hub.txt
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
  - Kolmykov S
  - Yevshin I
  - Kulyashov M
  - Sharipov R
  - Kondrakhin Y
  - Makeev VJ
  - Kulakovskiy IV
  - Kel A
  - Kolpakov F
  doi: 10.1093/nar/gkaa1057
  id: PMID:33231677
  journal: Nucleic Acids Res
  preferred: true
  title: 'GTRD: an integrated view of transcription regulation'
  year: '2021'
- authors:
  - Yevshin I
  - Sharipov R
  - Kolmykov S
  - Kondrakhin Y
  - Kolpakov F
  doi: 10.1093/nar/gky1128
  id: PMID:30445619
  journal: Nucleic Acids Res
  title: 'GTRD: a database on gene transcription regulation-2019 update'
  year: '2019'
- authors:
  - Yevshin I
  - Sharipov R
  - Valeev T
  - Kel A
  - Kolpakov F
  doi: 10.1093/nar/gkw951
  id: PMID:27924024
  journal: Nucleic Acids Res
  title: 'GTRD: a database of transcription factor binding sites identified by ChIP-seq
    experiments'
  year: '2017'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:7955
- NCBITaxon:7227
- NCBITaxon:6239
- NCBITaxon:4932
- NCBITaxon:4896
- NCBITaxon:3702
---
# GTRD

## Overview

GTRD (Gene Transcription Regulation Database) collects public sequencing experiments related to transcription regulation and reprocesses them with uniform pipelines. It is developed by Fedor Kolpakov's group at BIOSOFT.RU and the Federal Research Center for Information and Computational Technologies in Novosibirsk, Russia, on the BioUML platform and is described in Kolmykov et al. 2021 (Nucleic Acids Research).

## Data Content

Raw ChIP-seq, ChIP-exo, DNase-seq, MNase-seq, ATAC-seq, FAIRE-seq, and RNA-seq data are taken from GEO, SRA, ENCODE, and modENCODE and annotated with cell types, conditions, and target transcription factors using controlled vocabularies and ontologies. Uniform workflows produce TF binding peaks from several peak callers, merged meta-clusters, open chromatin regions and footprints, nucleosome positions, allele-specific binding events, and promoter-based TF target gene lists. Release 20.06 contained over 35,000 TF ChIP-seq experiments across nine species: human, mouse, rat, zebrafish, *Drosophila melanogaster*, *Caenorhabditis elegans*, *Saccharomyces cerevisiae*, *Schizosaccharomyces pombe*, and *Arabidopsis thaliana*.

## Access

The web interface supports browsing and searching by TF, gene, cell type, or experiment. Bulk results are available from the downloads directory as plain-text intervals, metadata tables, bigBed files, and target gene lists, and GTRD tracks can be loaded into the UCSC or Ensembl genome browsers through a track hub.

## License

The GTRD wiki states that the database may be used freely for non-commercial purposes as long as it is properly cited. Commercial users should contact gtrd@biosoft.ru to arrange a license.