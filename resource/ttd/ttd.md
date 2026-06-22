---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: zhangyintao@zju.edu.cn
  label: Feng Zhu
- category: Organization
  contact_details:
  - contact_type: url
    value: https://idrblab.org/ttd/
  label: College of Pharmaceutical Sciences, Zhejiang University
- category: Individual
  contact_details:
  - contact_type: url
    value: https://bidd.group/index.html#people
  label: Yuzong Chen
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bidd.group/index.html#people
  label: Department of Pharmacy, National University of Singapore
creation_date: '2025-10-29T00:00:00Z'
description: 'The Therapeutic Target Database (TTD) is a comprehensive aggregator
  providing information about known and explored therapeutic protein and nucleic acid
  targets, targeted diseases, pathway information, and corresponding drugs directed
  at these targets. TTD 2024 includes extensive druggability information across three
  perspectives: molecular interactions/regulations, human system profiles, and cell-based
  expression variations. The database encompasses 3,730 targets (including 532 successful,
  1,442 clinical trial, 239 preclinical/patented, and 1,517 literature-reported targets)
  and 39,862 drugs, with druggability characteristics covering ligand-specific binding
  pockets, protein-protein interaction networks, microbiota-drug regulations, target
  similarity profiles, pathway involvements, tissue distributions, and cell-based
  expression variations across different diseases and perturbations.'
domains:
- biomedical
- drug discovery
- genomics
- proteomics
- pharmacology
homepage_url: https://idrblab.org/ttd/
id: ttd
infores_id: ttd
last_modified_date: '2026-05-27T00:00:00Z'
layout: resource_detail
license:
  id: https://idrblab.org/ttd/
  label: Freely accessible for research and educational purposes
name: Therapeutic Target Database
products:
- category: GraphicalInterface
  description: Main web portal for browsing and searching TTD targets, drugs, biomarkers,
    and pathways
  format: http
  id: ttd.portal
  name: TTD Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.org/ttd/
- category: Product
  description: Raw format target information including all TTD target data
  format: txt
  id: ttd.targets-raw
  name: TTD Targets Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-01-TTD_target_download.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Raw format drug information including all TTD drug data
  format: txt
  id: ttd.drugs-raw
  name: TTD Drug Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-02-TTD_drug_download.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Cross-matching identifiers between TTD drugs and public databases
  format: txt
  id: ttd.crossmatch
  name: Cross-matching Drug IDs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-03-Drug_xrefs.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Synonyms of drugs and small molecules in TTD
  format: txt
  id: ttd.synonyms
  name: Drug Synonyms
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-04-Drug_synonyms.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Drug to disease mapping with ICD identifiers
  format: txt
  id: ttd.drug-disease
  name: Drug-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-05-Drug_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to disease mapping with ICD identifiers
  format: txt
  id: ttd.target-disease
  name: Target-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-06-Target_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to drug mapping with mode of action information
  format: csv
  id: ttd.target-drug
  name: Target-Drug Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-07-Drug-TargetMapping.xlsx
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Biomarker to disease mapping with ICD identifiers
  format: txt
  id: ttd.biomarker-disease
  name: Biomarker-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-08-Biomarker_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to compound mapping with experimental activity data
  format: txt
  id: ttd.target-compound
  name: Target-Compound Activity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-09-Target_compound_activity.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: UniProt IDs for all targets in TTD
  format: txt
  id: ttd.uniprot-all
  name: All Target UniProt IDs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P2-01-TTD_uniprot_all.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Sequence data for all targets in FASTA format
  format: fasta
  id: ttd.sequences-all
  name: All Target Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P2-06-All_target_seq.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Structure data for all drugs in SDF format
  format: sdf
  id: ttd.structures-all
  name: All Drug Structures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P3-01-Drug_structure.sdf
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: SMILES and InChI representations for approved drugs
  format: txt
  id: ttd.smiles-inchi
  name: Drug SMILES and InChI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P3-06-Drug_SMILE_InChI.txt
- category: Product
  description: KEGG pathway data for all targets
  format: txt
  id: ttd.kegg-pathways
  name: Target KEGG Pathways
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P4-01-Target_KEGG_pathway.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: WikiPathways data for all targets
  format: txt
  id: ttd.wiki-pathways
  name: Target WikiPathways
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P4-06-Target_wikipathway.txt
  warnings: []
- category: Product
  description: Drug combination data including synergistic, additive, and antagonistic
    interactions
  format: txt
  id: ttd.drug-combinations
  name: Drug Combinations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P5-01-Drug_combination_synergism_anti-counteractive.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: DocumentationProduct
  description: Help documentation and user guide for TTD
  format: http
  id: ttd.help
  name: TTD Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://idrblab.org/ttd/help
  warnings:
  - File was not able to be retrieved when checked on 2026-03-08_ HTTP 404 error when
    accessing file
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  format: mixed
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for TTD distributed via the NCATS Translator
    release site (release 2026_03_06; build ttd_2024_03_30_0a11135d_2025sep1_4.3.6;
    source version 2024_03_30; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 69317
  format: kgx-jsonl
  id: translator.ttd.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator TTD KGX Graph
  node_count: 25564
  original_source:
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://kgx-storage.rtx.ai/releases/ttd/latest/
  versions:
  - '2026_03_06'
  - ttd_2024_03_30_0a11135d_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: GraphicalInterface
  description: Graphical interface for MedKG
  id: medkb.site
  name: MedKG Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: http://pitools.niper.ac.in/medkg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: medkg
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
- category: GraphProduct
  compression: gzip
  description: PharMeBINet V2 JSON release published on February 6, 2024.
  format: json
  id: pharmebinet.json
  latest_version: v2
  name: PharMeBINet JSON Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1942958027
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 TSV release published on February 6, 2024.
  format: tsv
  id: pharmebinet.tsv
  latest_version: v2
  name: PharMeBINet TSV Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1922614551
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 GraphML release published on February 6, 2024.
  format: mixed
  id: pharmebinet.graphml
  latest_version: v2
  name: PharMeBINet GraphML Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 2027519087
  product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
  format: neo4j
  id: pharmebinet.neo4j
  latest_version: v2
  name: PharMeBINet Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3847978577
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
  dump_format: neo4j
  format: neo4j
  id: pharmebinet.neo4j.dump
  latest_version: v2
  name: PharMeBINet Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3598325722
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
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
publications:
- authors:
  - Ying Zhou
  - Yintao Zhang
  - Donghai Zhao
  - Xinyuan Yu
  - Xinyi Shen
  - Yuan Zhou
  - Shanshan Wang
  - Yunqing Qiu
  - Yuzong Chen
  - Feng Zhu
  category: Publication
  doi: 10.1093/nar/gkad751
  id: doi:10.1093/nar/gkad751
  journal: Nucleic Acids Research
  preferred: true
  title: 'TTD: Therapeutic Target Database describing target druggability information'
  year: '2024'
- authors:
  - Yuan Zhou
  - Ying Zhang
  - Xueya Lian
  - Fengcheng Li
  - Chaoxin Wang
  - Feng Zhu
  - Yunqing Qiu
  - Yuzong Chen
  category: Publication
  doi: 10.1093/nar/gkab953
  id: doi:10.1093/nar/gkab953
  journal: Nucleic Acids Research
  preferred: false
  title: 'Therapeutic target database update 2022: facilitating drug discovery with
    enriched comparative data of targeted agents'
  year: '2022'
taxon:
- NCBITaxon:9606
---
# Therapeutic Target Database

## Overview

The Therapeutic Target Database (TTD) is a comprehensive aggregator providing specialized information about therapeutic protein and nucleic acid targets, their targeted diseases, pathway information, and corresponding drugs. TTD serves as an essential resource for drug discovery and development, facilitating target assessment, validation, and druggability evaluation.

## Mission and Scope

TTD's primary mission is to facilitate research and early development of targeted therapeutics by providing comprehensive druggability information for therapeutic targets. The database aggregates and integrates data from multiple sources including FDA approvals, clinical trial databases (ClinicalTrials.gov), pharmaceutical company pipeline reports, patent databases, and scientific literature.

## Database Content

### Targets and Drugs

As of the 2024 update, TTD contains:

- **3,730 therapeutic targets** categorized by development status:
  - 532 successful targets (targeted by FDA-approved drugs)
  - 1,442 clinical trial targets
  - 239 preclinical/patented targets
  - 1,517 literature-reported targets

- **39,862 drugs** across development stages:
  - 2,895 approved drugs
  - 11,796 clinical trial drugs
  - 5,041 preclinical/patented drugs
  - 20,130 experimental drugs

### Druggability Information

TTD 2024 introduces comprehensive druggability characteristics from three distinct perspectives:

#### 1. Molecular Interactions and Regulations

- **Ligand-Specific Binding Pockets**: Over 22,431 co-crystal structures providing drug binding pocket information for 1,237 targets, with residues interacting with drugs at distances <5Å highlighted
- **Protein-Protein Interaction Networks**: Network properties (degree, betweenness centrality, clustering coefficient, etc.) calculated for 2,163 targets based on a human PPI network of 9,309 proteins and 52,713 interactions
- **Microbiota-Drug Bidirectional Regulations**: 9,812 interactions between 663 drugs and 686 microbes across 20 phyla, describing how microbiota affects drug metabolism and how drugs regulate microbe abundance

#### 2. Human System Features

- **Target Similarity Profiles**: Similarity to human proteins outside target families calculated via BLAST (E-value <0.005) for 3,005 targets, helping assess off-target interactions
- **Pathway Involvements**: 241 life-essential KEGG pathways associated with 2,881 targets, indicating target positions in critical biological processes
- **Tissue/Organ Distributions**: Protein expression data across 32 human tissues for 2,001 targets, helping evaluate potential adverse drug reactions

#### 3. Cell-Based Expression Variations

- **Varied Expressions Across Cell Types**: Expression profiles for 2,845 targets across 1,742 cell types from 7,289 samples, covering 121 disease classes defined by WHO ICD-11
- **Exogenous Stimulus-Induced Differential Expression**: Expression changes induced by 625 exogenous factors (drugs, infections, environmental stimuli) for 2,862 targets across 313 cell lines
- **Endogenous Factor-Modified Expression**: Expression alterations by 447 endogenous factors (mutations, expression variations) for 2,841 targets across 198 cell lines

## Data Organization and Access

### Search and Browse Functions

TTD provides multiple search interfaces:
- Full-text search across targets and drugs
- Search by ICD-11 defined disease classes
- Biomarker search
- Drug scaffold search
- Batch search for multiple TTD IDs

### Downloadable Data

TTD offers comprehensive downloadable datasets including:

- **Target Information**: UniProt IDs, sequences (FASTA), pathway data (KEGG and WikiPathways) for all targets or filtered by development status
- **Drug Information**: Structures (SDF format), SMILES/InChI representations, biologic drug sequences, cross-references to public databases
- **Mapping Data**: Target-disease, drug-disease, biomarker-disease, target-drug, and target-compound activity mappings
- **Drug Combinations**: Synergistic, additive, and antagonistic drug combination data with mechanistic classifications
- **Synonym Data**: Comprehensive synonyms for drugs and small molecules

## Key Features and Updates

### 2024 Update Highlights

The TTD 2024 update significantly expanded druggability information:

- Nine categories of druggability characteristics collected via systematic review
- Druggability data organized into three perspectives: molecular, system, and cellular
- Batch search functionality for uploading lists of TTD IDs
- Full download capability for all search results
- Enhanced cross-linking to pathway databases

### Historical Development

TTD has undergone continuous enhancement since 2002:

- **2022**: Added structure-based activity landscapes, prodrug information, co-target data
- **2020**: Integrated target regulators (microRNAs, transcription factors), patented agents with activity values
- **2018**: Incorporated differential expression profiles in patients vs. healthy individuals, multitarget drug combinations
- **2016**: Added pathway cross-links for targets and drugs
- **2014**: Introduced biomarkers and drug scaffolds
- **2012**: Added target validation information and QSAR models
- **2010**: Included clinical trial drugs and similarity search

## Applications and Impact

TTD data has been widely adopted for:

- **Drug Repurposing**: Tools like LigAdvisor and DrugRep utilize TTD data
- **Target Discovery**: Servers like CoVex and DeepCancerMap leverage TTD information
- **Adverse Drug Reaction Prediction**: Systems like MEDICASCY and H-RACS use TTD data
- **Scientific Research**: Hundreds of studies use TTD for genetic variant-disease associations, molecular characteristics of infections, target variability, and antifungal therapy discovery

## Technical Infrastructure

TTD is maintained by the College of Pharmaceutical Sciences at Zhejiang University (China) in collaboration with the Department of Pharmacy at the National University of Singapore. The database is freely accessible without login requirements at https://idrblab.org/ttd/ and supports research and educational purposes.

## Data Quality and Curation

Target and drug data in TTD undergo rigorous validation:

- Approved drugs collected from authoritative FDA publications
- Clinical trial drugs sourced from ClinicalTrials.gov, PhRMA reports, and company pipelines
- Preclinical/patented drugs extracted from company reports and patent databases
- Target status determined by highest drug development status
- Target validation requires demonstrated functional roles in disease and drug modulation capability

## Funding and Support

TTD development is supported by:
- Natural Science Foundation of Zhejiang Province
- Alibaba-Zhejiang University Joint Research Center of Future Digital Healthcare
- Alibaba Cloud
- Information Technology Center of Zhejiang University

## Future Directions

TTD continues to expand its coverage of druggability characteristics and aims to facilitate the exploration of novel targets and discovery of new therapeutics. Future updates will focus on:
- Integration of additional single-cell expression data
- Expanded coverage of drug-target-disease relationships
- Enhanced computational tools for druggability assessment
- Improved cross-referencing with other biomedical databases

## Citation

When using TTD, please cite:

Zhou Y, Zhang YT, Zhao DH, Yu XY, Shen XY, Zhou Y, Wang SS, Qiu YQ, Chen YZ, Zhu F. TTD: Therapeutic Target Database describing target druggability information. Nucleic Acids Research. 2024; 52(D1):D1465-D1477. doi:10.1093/nar/gkad751. PMID: 37713619.