---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bbglab.irbbarcelona.org
  - contact_type: github
    value: bbglab
  label: Barcelona Biomedical Genomics Lab (bbglab), IRB Barcelona
creation_date: '2026-11-12T00:00:00Z'
description: IntOGen is a framework and web platform that identifies mutational cancer
  driver genes by running a pipeline of complementary driver discovery methods over
  somatic mutation data from tumor cohorts, and publishes the resulting Compendium
  of Cancer Genes. The 2024.09.20 release analyzes 271 cohorts (about 33,000 tumor
  samples across 87 cancer types) from sources such as TCGA, PCAWG, ICGC, the Hartwig
  Medical Foundation, St. Jude, and CPTAC, and reports 633 driver genes with their
  mutational features, combined significance, and consensus mode of action per cohort.
domains:
- biomedical
- cancer
- genomics
- genetic variation
- precision medicine
homepage_url: https://www.intogen.org/
id: intogen
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: IntOGen
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing cancer driver genes, cohorts,
    cancer types, and mutation distributions in the current IntOGen release.
  format: http
  id: intogen.portal
  is_public: true
  name: IntOGen Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://www.intogen.org/search
- category: Product
  compression: zip
  description: Compendium of Cancer Genes from the current IntOGen release, containing
    the catalog of driver genes (Compendium_Cancer_Genes.tsv) and the unfiltered driver
    results (Unfiltered_drivers.tsv) across all analyzed cohorts, with tumor type,
    mutated samples, method-specific and combined significance, and mode of action.
    Cohorts are drawn from TCGA, PCAWG, ICGC, Hartwig Medical Foundation, and other
    sequencing projects; genes are annotated with Ensembl canonical transcripts and
    the COSMIC Cancer Gene Census.
  format: tsv
  id: intogen.drivers
  is_public: true
  latest_version: '2024.09.20'
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: IntOGen Compendium of Cancer Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:hadPrimarySource
    source: icgc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  product_file_size: 964758
  product_url: https://www.intogen.org/download?file=IntOGen-Drivers-20240920.zip
- category: Product
  compression: zip
  description: Table of the cohorts analyzed in the current IntOGen release (cohorts.tsv),
    with cancer type, data source, sequencing platform, literature reference, treatment
    status, and sample and mutation counts for each cohort.
  format: tsv
  id: intogen.cohorts
  is_public: true
  latest_version: '2024.09.20'
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: IntOGen Cohorts Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:hadPrimarySource
    source: icgc
  product_file_size: 13918
  product_url: https://www.intogen.org/download?file=IntOGen-Cohorts-20240920.zip
- category: ProcessProduct
  description: Source code of the IntOGen pipeline (intogen-plus), which combines
    multiple driver discovery methods to identify cancer driver genes from somatic mutation
    data.
  format: mixed
  id: intogen.pipeline
  is_public: true
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.en.html
    label: GPL-3.0
  name: IntOGen Pipeline Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://github.com/bbglab/intogen-plus
- category: DocumentationProduct
  description: Documentation for the IntOGen pipeline, covering its methods, inputs,
    outputs, and post-processing of driver gene results.
  format: http
  id: intogen.docs
  is_public: true
  name: IntOGen Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://intogen.readthedocs.io/en/latest/
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
  - Francisco Martínez-Jiménez
  - Ferran Muiños
  - Inés Sentís
  - Jordi Deu-Pons
  doi: 10.1038/s41568-020-0290-x
  id: doi:10.1038/s41568-020-0290-x
  journal: Nature Reviews Cancer
  preferred: true
  title: A compendium of mutational cancer driver genes
  year: '2020'
repository: https://github.com/bbglab/intogen-plus
rrid: SCR_027727
taxon:
- NCBITaxon:9606
---
# IntOGen

IntOGen (Integrative OncoGenomics) is developed by the Barcelona Biomedical Genomics Lab at IRB Barcelona. It runs a pipeline of complementary driver discovery methods (dNdScv, CBaSE, OncodriveFML, OncodriveCLUSTL, HotMAPS, smRegions, and MutPanning) over somatic mutation data from tumor sequencing cohorts and combines their results to produce the Compendium of Cancer Genes, a catalog of mutational cancer driver genes per cohort and tumor type, each annotated with its mutational features and consensus mode of action (loss of function, activating, or ambiguous).

The 2024.09.20 release covers 271 cohorts and reports 633 driver genes. It switched to MANE reference transcripts, updated the Hartwig Medical Foundation data with Oncotree-based tumor type annotation, and updated annotation to Cancer Gene Census v99. Data released by IntOGen are dedicated to the public domain under CC0 1.0; the pipeline source code is released under GPL-3.0.
