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
  product_file_size: 359471390
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
  product_file_size: 126917161
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
    metadata in GFF3-style attributes for display in IGV. Files are named as listed
    in fileList.tab; the URL given is one example file.
  format: txt
  id: chip-atlas.peaks.assembled
  name: ChIP-Atlas Assembled Peak-call Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: sra
  product_file_size: 637430253
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
  product_file_size: 21398659343
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
  product_file_size: 2603130
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
  product_file_size: 270398
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
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.1
  compression: gzip
  description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph,
    exported as a biolink-typed KGX graph (~47M nodes / ~151M edges, ~9.6 GB compressed
    across node and edge files in both TSV and JSON Lines, plus a manifest). A practical
    projection of the full graph for human-centric biomedical use. Sources without
    compatible redistribution terms are excluded (full OMIM data, CTD, PanelApp, miRDB,
    and the SpliceAI and AlphaMissense variant-prediction layers). Published on Zenodo.
  edge_count: 150949120
  format: kgx
  id: biobtree.graph.human-subgraph
  latest_version: v2-2026-11
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC-BY-NC-SA-4.0
  name: BioBTree Knowledge Graph - Human Subgraph (KGX)
  node_categories:
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellLine
  - biolink:CellularComponent
  - biolink:CodingSequence
  - biolink:Disease
  - biolink:DiseaseOrPhenotypicFeature
  - biolink:Drug
  - biolink:Exon
  - biolink:Gene
  - biolink:GrossAnatomicalStructure
  - biolink:MacromolecularComplex
  - biolink:MolecularActivity
  - biolink:NoncodingRNAProduct
  - biolink:NucleicAcidSequenceMotif
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:ProteinDomain
  - biolink:ProteinFamily
  - biolink:Publication
  - biolink:RegulatoryRegion
  - biolink:SequenceVariant
  - biolink:SmallMolecule
  - biolink:Transcript
  node_count: 47361928
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  predicates:
  - biolink:actively_involved_in
  - biolink:affects
  - biolink:associated_with
  - biolink:close_match
  - biolink:derives_from
  - biolink:directly_physically_interacts_with
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:gene_product_of
  - biolink:has_adverse_event
  - biolink:has_gene_product
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:in_clinical_trials_for
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:member_of
  - biolink:mentions
  - biolink:orthologous_to
  - biolink:paralogous_to
  - biolink:participates_in
  - biolink:physically_interacts_with
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:transcribed_from
  - biolink:translates_to
  - biolink:treats_or_applied_or_studied_to_treat
  product_url: https://doi.org/10.5281/zenodo.20816741
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
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
rrid: SCR_015511
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