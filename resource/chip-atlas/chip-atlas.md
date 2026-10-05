---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: okishinya@kumamoto-u.ac.jp
  label: Shinya Oki
- category: Individual
  contact_details:
  - contact_type: email
    value: zou@kumamoto-u.ac.jp
  label: Zhaonan Zou
creation_date: '2026-10-05T00:00:00Z'
description: ChIP-Atlas is a data-mining suite that integrates and uniformly reprocesses
  nearly all public ChIP-seq, ATAC-seq, DNase-seq and Bisulfite-seq experiments deposited
  in the Sequence Read Archive for six model organisms (human, mouse, rat, fruit fly,
  nematode and budding yeast). It provides peak calls, coverage tracks, target gene
  predictions, colocalization analyses, enrichment analysis, differential analysis
  and, since version 3.0, chromosome architecture data, with manually curated antigen
  and cell type annotations.
domains:
- genomics
- epigenomics
- gene regulation
homepage_url: https://chip-atlas.org/
id: chip-atlas
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ChIP-Atlas
products:
- category: GraphicalInterface
  description: ChIP-Atlas web portal with the Peak Browser, Target Genes, Colocalization,
    Enrichment Analysis, Diff Analysis and experiment search tools for exploring reprocessed
    public ChIP-seq, ATAC-seq, DNase-seq and Bisulfite-seq data.
  format: http
  id: chip-atlas.portal
  name: ChIP-Atlas Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.org/
- category: Product
  description: Metadata table describing every ChIP-seq, ATAC-seq, DNase-seq and Bisulfite-seq
    experiment (SRX, DRX or ERX accession) in ChIP-Atlas, including genome assembly,
    curated antigen and cell type classes, and processing statistics.
  format: tsv
  id: chip-atlas.experimentlist
  name: ChIP-Atlas experimentList.tab
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/metadata/experimentList.tab
- category: Product
  description: Table listing the assembled peak-call BED files used by the Peak Browser,
    by genome, track type, antigen, cell type class and significance threshold.
  format: tsv
  id: chip-atlas.filelist
  name: ChIP-Atlas fileList.tab
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  product_url: https://chip-atlas.dbcls.jp/data/metadata/fileList.tab
- category: Product
  description: Peak calls (MACS2, BED4 and BigBed) and coverage tracks (BigWig) for
    each individual experiment, at MACS2 Q-value thresholds of 1e-05, 1e-10 and 1e-20,
    plus methylation rate, coverage and hypo-, partially and hyper-methylated region
    files for Bisulfite-seq. Files are addressed by genome assembly and experiment
    accession under the data directory.
  format: mixed
  id: chip-atlas.peaks.each
  name: ChIP-Atlas Per-Experiment Peak Calls and Coverage
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/
- category: Product
  description: Assembled BED9 peak-call files used in the Peak Browser, concatenating
    peaks across experiments by antigen or track type and cell type class, with sample
    metadata in GFF3-style attributes for display in IGV. Files are named
    as listed in fileList.tab; the URL given is one example file.
  format: txt
  id: chip-atlas.peaks.assembled
  name: ChIP-Atlas Assembled Peak-call Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/hg19/assembled/Oth.ALL.05.GATA2.AllCell.bed
- category: Product
  compression: gzip
  description: Lighter version of all peak-call data for each genome assembly and
    significance threshold, as gzipped BED files with experiment accessions in place
    of full metadata.
  format: txt
  id: chip-atlas.peaks.light
  name: ChIP-Atlas All Peaks (Light)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/hg38/allPeaks_light/allPeaks_light.hg38.05.bed.gz
- category: Product
  description: Predicted target genes of each transcription factor or other DNA-binding
    protein, as TSV tables of binding scores near transcription start sites within
    1, 5 or 10 kb, across all experiments for that protein. Files follow the pattern
    [Genome]/target/[Protein].[Distance].tsv; the URL given is one example file.
  format: tsv
  id: chip-atlas.targetgenes
  name: ChIP-Atlas Target Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/hg19/target/POU5F1.5.tsv
- category: Product
  description: Colocalization scores between pairs of transcription factors or other
    DNA-binding proteins within each cell type class, as TSV tables per protein and
    cell type class. Files follow the pattern [Genome]/colo/[Protein].[Cell_type_class].tsv;
    the URL given is one example file.
  format: tsv
  id: chip-atlas.colocalization
  name: ChIP-Atlas Colocalization
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_url: https://chip-atlas.dbcls.jp/data/hg19/colo/POU5F1.Pluripotent_stem_cell.tsv
- category: ProgrammingInterface
  description: Programmatic access to ChIP-Atlas Enrichment Analysis and Diff Analysis
    through HTTP requests, documented on the project wiki.
  format: http
  id: chip-atlas.api
  name: ChIP-Atlas Analysis API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  product_url: https://github.com/inutano/chip-atlas/wiki/Perform-Enrichment-Analysis-programmatically
- category: DocumentationProduct
  description: ChIP-Atlas documentation covering data sources, primary processing,
    annotation, each analysis tool, download URL patterns and table schemas.
  format: http
  id: chip-atlas.docs
  name: ChIP-Atlas Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  product_url: https://github.com/inutano/chip-atlas/wiki
publications:
- authors:
  - Zhaonan Zou
  - Tazro Ohta
  - Shinya Oki
  doi: 10.1093/nar/gkae358
  id: doi:10.1093/nar/gkae358
  journal: Nucleic Acids Research
  preferred: true
  title: 'ChIP-Atlas 3.0: a data-mining suite to explore chromosome architecture together
    with large-scale regulome data'
  year: '2024'
- authors:
  - Zhaonan Zou
  - Tazro Ohta
  - Fumihito Miura
  - Shinya Oki
  doi: 10.1093/nar/gkac199
  id: doi:10.1093/nar/gkac199
  journal: Nucleic Acids Research
  title: 'ChIP-Atlas 2021 update: a data-mining suite for exploring epigenomic landscapes
    by fully integrating ChIP-seq, ATAC-seq and Bisulfite-seq data'
  year: '2022'
- authors:
  - Shinya Oki
  - Tazro Ohta
  - Go Shioi
  - Hideki Hatanaka
  - Osamu Ogasawara
  - Yoshihiro Okuda
  - Hideya Kawaji
  - Ryo Nakaki
  - Jun Sese
  - Chikara Meno
  doi: 10.15252/embr.201846255
  id: doi:10.15252/embr.201846255
  journal: The EMBO Reports
  title: 'ChIP‐Atlas: a data‐mining suite powered by full integration of public ChIP‐seq
    data'
  year: '2018'
repository: https://github.com/inutano/chip-atlas
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:7227
- NCBITaxon:6239
- NCBITaxon:4932
---
# ChIP-Atlas

ChIP-Atlas is a data-mining suite for public epigenomic and regulome data. It selects ChIP-seq, ATAC-seq, DNase-seq and Bisulfite-seq experiments from the Sequence Read Archive (SRX, DRX and ERX accessions) for human, mouse, rat, *Drosophila melanogaster*, *Caenorhabditis elegans* and *Saccharomyces cerevisiae*, and reprocesses them with a uniform pipeline (Bowtie2 alignment, MACS2 peak calling at three significance thresholds, BigWig coverage). Curators annotate the antigen and cell type of each experiment, using standard gene nomenclatures (HGNC, MGI, RGD, FlyBase, WormBase, SGD) and unified cell line names.

The web portal offers a Peak Browser (via IGV), Target Genes, Colocalization, Enrichment Analysis and Diff Analysis. ChIP-Atlas 3.0 added chromosome architecture data. It is developed by Shinya Oki, Zhaonan Zou and colleagues with the Database Center for Life Science (DBCLS); the current contacts are at Kumamoto University, and processing runs on the NIG Supercomputer.

## Downloads

Files are served from `https://chip-atlas.dbcls.jp/data/`, with paths documented on the [project wiki](https://github.com/inutano/chip-atlas/wiki). Metadata tables (`experimentList.tab`, `fileList.tab`, `analysisList.tab`, `antigenList.tab`, `celltypeList.tab`) are under `data/metadata/`. Per-experiment BED, BigBed and BigWig files, assembled Peak Browser BED files, gzipped "light" peak sets, and Target Genes and Colocalization TSV tables sit in per-genome directories (for example `data/hg38/`).

## License

The portal says all ChIP-Atlas data and analysis tools are licensed under CC BY 4.0, with attribution to the ChIP-Atlas publications. The website source code on GitHub is MIT licensed. An older snapshot in the NBDC Life Science Database Archive (doi:10.18908/lsdba.nbdc01558-000) is listed there as CC BY-SA.
