---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: ORegAnno (the Open Regulatory Annotation database) is a community-driven,
  literature-curated resource of regulatory regions, transcription factor binding
  sites, regulatory polymorphisms, and regulatory interactions across multiple species.
  It served as an upstream primary source for regulatory annotation resources such
  as DoRothEA. The original standalone interactive site (oreganno.org) is no longer
  operational and now redirects to the UCSC Genome Browser; the curated ORegAnno 3.0
  data set lives on as a track and bulk download in the UCSC Genome Browser and is
  also distributed via Ensembl.
domains:
- genomics
- systems biology
- gene regulation
homepage_url: https://genome.ucsc.edu/cgi-bin/hgTrackUi?org=Human&g=oreganno
id: oreganno
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/lgpl.html
  label: LGPL (stated by ORegAnno for its data and web application)
name: ORegAnno
products:
- category: Product
  description: ORegAnno 3.0 regulatory annotation as a UCSC Genome Browser track and
    bulk download (human, hg38).
  format: gff
  id: oreganno.ucsc
  name: ORegAnno UCSC Track Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oreganno
  product_file_size: 20472081
  product_url: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/oreganno.txt.gz
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
publications:
- authors:
  - Robert Lesurf
  - Kelsy C. Cotto
  - Grace Wang
  - Malachi Griffith
  - Katayoon Kasaian
  - Steven J. M. Jones
  - Stephen B. Montgomery
  - Obi L. Griffith
  doi: 10.1093/nar/gkv1203
  id: https://www.ncbi.nlm.nih.gov/pubmed/26578589
  journal: Nucleic Acids Res
  preferred: true
  title: 'ORegAnno 3.0: a community-driven resource for curated regulatory annotation'
  year: '2016'
---
# ORegAnno

## Overview

ORegAnno (the Open Regulatory Annotation database) is an open, community-curated
collection of regulatory annotation. It captures regulatory regions, transcription
factor binding sites, regulatory polymorphisms, and curated regulatory interactions,
each linked to supporting literature evidence and target genes across multiple species.

## Status

ORegAnno is largely a legacy resource. The original standalone site at oreganno.org
is no longer operational as an interactive database and now redirects to the UCSC
Genome Browser. The curated ORegAnno 3.0 data persists through the UCSC Genome Browser
(ORegAnno track and bulk downloads) and Ensembl, which is how the data remains
accessible today.

## Contents

- Curated regulatory regions and transcription factor binding sites
- Regulatory polymorphisms and regulatory interactions
- Literature-backed evidence linking regulatory features to target genes
- Multi-species coverage

## Access

- UCSC Genome Browser ORegAnno track and `goldenPath` bulk downloads
- Ensembl regulatory annotation

## Relationship to other resources

ORegAnno served as an upstream primary source for downstream regulatory resources,
including DoRothEA.

## Citation

Lesurf R, Cotto KC, Wang G, et al. "ORegAnno 3.0: a community-driven resource for
curated regulatory annotation." Nucleic Acids Res. 2016. doi:10.1093/nar/gkv1203