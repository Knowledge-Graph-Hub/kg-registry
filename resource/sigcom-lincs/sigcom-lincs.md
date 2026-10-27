---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-10-10T00:00:00Z'
description: SigCom LINCS is a web search engine from the Ma'ayan Laboratory, built
  on the Signature Commons framework, that serves more than a million gene expression
  signatures processed from LINCS (mostly L1000 chemical, shRNA, CRISPR knockout,
  overexpression, and ligand perturbations), GTEx, and GEO. Users run rank-based signature
  similarity searches to find perturbations that mimic or reverse a query signature,
  and search metadata about signatures, datasets, genes, and drugs. All data are available
  through a metadata API, a data API, and bulk downloads.
domains:
- genomics
- gene expression profiling
- drug discovery
- drug repositioning
homepage_url: https://maayanlab.cloud/sigcom-lincs/
id: sigcom-lincs
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
name: SigCom LINCS
products:
- category: GraphicalInterface
  description: Web search engine for running signature similarity searches with up
    and down gene sets or a single gene set to find mimicking and reversing perturbations,
    and for searching signature, dataset, gene, and drug metadata.
  format: http
  id: sigcom-lincs.portal
  name: SigCom LINCS Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_url: https://maayanlab.cloud/sigcom-lincs/
- category: ProgrammingInterface
  description: Signature Commons metadata API (LoopBack, OpenAPI) for querying libraries,
    signatures, entities, and their metadata.
  format: json
  id: sigcom-lincs.metadata-api
  is_public: true
  name: SigCom LINCS Metadata API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_url: https://maayanlab.cloud/sigcom-lincs/metadata-api/
- category: ProgrammingInterface
  description: Signature Commons data API (EnrichmentAPI) for rank-based signature
    similarity and set enrichment queries over the stored signature matrices.
  format: json
  id: sigcom-lincs.data-api
  is_public: true
  name: SigCom LINCS Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_url: https://maayanlab.cloud/sigcom-lincs/data-api/
- category: DocumentationProduct
  description: Jupyter notebook tutorial documenting the SigCom LINCS metadata and
    data APIs with worked examples.
  format: http
  id: sigcom-lincs.documentation
  name: SigCom LINCS Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_file_size: 15432
  product_url: https://github.com/MaayanLab/sigcom-lincs/blob/main/tutorials/SigCom%20LINCS%20Documentation.ipynb
- category: Product
  compression: gzip
  description: Consensus (mean) characteristic-direction coefficient matrix of L1000
    chemical perturbation signatures, 2021 processing.
  format: tsv
  id: sigcom-lincs.cp-consensus
  name: L1000 Chemical Perturbation Consensus Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 1897525732
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/means/cp_mean_coeff_mat.tsv.gz
- category: Product
  compression: gzip
  description: Consensus (mean) characteristic-direction coefficient matrix of L1000
    CRISPR knockout signatures, 2021 processing.
  format: tsv
  id: sigcom-lincs.xpr-consensus
  name: L1000 CRISPR Knockout Consensus Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 432492125
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/means/xpr_mean_coeff_mat.tsv.gz
- category: Product
  description: Up and down gene sets for each L1000 chemical perturbation signature
    in GMT format, 2021 processing.
  format: tsv
  id: sigcom-lincs.cp-gmt
  name: L1000 Chemical Perturbation Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 2245934983
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_cp.gmt
- category: Product
  description: Up and down gene sets for each L1000 CRISPR knockout signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.xpr-gmt
  name: L1000 CRISPR Knockout Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 438363414
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_xpr.gmt
- category: Product
  description: Up and down gene sets for each L1000 shRNA knockdown signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.shrna-gmt
  name: L1000 shRNA Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 501676713
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_shRNA.gmt
- category: Product
  description: Up and down gene sets for each L1000 overexpression signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.oe-gmt
  name: L1000 Overexpression Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 105994280
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_oe.gmt
- category: Product
  description: Characteristic-direction coefficient matrix for all individual L1000
    chemical perturbation signatures in GCTX (HDF5) format.
  format: hdf5
  id: sigcom-lincs.cp-coefficients
  name: L1000 Chemical Perturbation Signature Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 36084518760
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gctx/cd-coefficient/cp_coeff_mat.gctx
- category: Product
  description: Drug-drug cosine similarity matrix computed from L1000 landmark gene
    signatures.
  format: hdf5
  id: sigcom-lincs.drug-similarity
  name: L1000 Drug-Drug Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 4521206656
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-data-2020/similarity/L1000_2021_cosine_drug_similarity_lm.h5
- category: Product
  description: Gene-gene cosine similarity matrix computed from L1000 genetic perturbation
    signatures on landmark genes.
  format: hdf5
  id: sigcom-lincs.gene-similarity
  name: L1000 Gene-Gene Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 225768016
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-data-2020/similarity/L1000_2021_cosine_gene_similarity_lm.h5
- category: Product
  description: Metadata for the LINCS small molecules indexed in SigCom LINCS.
  format: tsv
  id: sigcom-lincs.small-molecules
  name: LINCS Small Molecule Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_file_size: 3950516
  product_url: https://s3.amazonaws.com/lincs-dcic/sigcom-lincs-metadata/LINCS_small_molecules.tsv
- category: Product
  description: Characteristic-direction gene expression signatures generated automatically
    from human GEO studies.
  format: tsv
  id: sigcom-lincs.human-geo-signatures
  name: Automatic Human GEO Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_file_size: 2106353545
  product_url: https://lincs-dcic.s3.amazonaws.com/auto-geo-sigs/human_geo_cd_sigs.tsv
- category: GraphProduct
  description: Drug-to-gene up- and down-regulation edges from SigCom LINCS L1000
    signatures (8,942 nodes, 225,509 edges).
  format: json
  id: reprotox-kg.graph.sigcom-lincs
  name: ReproTox-KG SigCom LINCS Drug-Gene Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_file_size: 114587395
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/sigcom_lincs_serialization.valid.json
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
  product_url: https://maayanlab.cloud/Enrichr/#libraries
publications:
- authors:
  - Evangelista JE
  - Clarke DJB
  - Xie Z
  - Lachmann A
  - Jeon M
  - Chen K
  - Jagodnik KM
  - Jenkins SL
  - Kuleshov MV
  - Wojciechowicz ML
  - Schürer SC
  - Medvedovic M
  - Ma'ayan A
  doi: 10.1093/nar/gkac328
  id: PMID:35524556
  journal: Nucleic Acids Res
  preferred: true
  title: 'SigCom LINCS: data and metadata search engine for a million gene expression
    signatures'
  year: '2022'
repository: https://github.com/MaayanLab/sigcom-lincs
rrid: SCR_022275
synonyms:
- Signature Commons LINCS
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# SigCom LINCS

SigCom LINCS is a gene expression signature search engine from the Ma'ayan Laboratory at the Icahn School of Medicine at Mount Sinai, built on the Signature Commons framework. As of October 2026 it indexes 1,113,059 signatures from 431 datasets. Most come from LINCS L1000 perturbations: chemical (718,055), shRNA (158,003), CRISPR knockout (140,945), overexpression (34,164), and ligand (7,546). Others come from GTEx and from automatically processed human and mouse GEO studies.

## Search and access

Users can search with up and down gene sets or a single gene set to rank signatures that mimic or reverse the query, and can search metadata for signatures, datasets, genes, and drugs. Everything in the web interface is also available through the Signature Commons metadata API and data API, both registered in SmartAPI. Bulk downloads include consensus and individual L1000 signature matrices, GMT gene sets for each perturbation type, drug-drug and gene-gene similarity matrices, small-molecule metadata, and automatic GEO signatures, along with mirrored CREEDS and CLUE files.

## Terms

The site states no license for its data. It asks users to cite Evangelista et al. 2022 (Nucleic Acids Research). SigCom LINCS feeds the SigCom LINCS drug-gene graph in ReproTox-KG.