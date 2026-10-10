---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
- category: Individual
  contact_details:
  - contact_type: email
    value: alexander.lachmann@mssm.edu
  label: Alexander Lachmann
creation_date: '2026-10-10T00:00:00Z'
description: Geneshot is a search engine from the Ma'ayan Laboratory that takes arbitrary
  search terms and returns human genes ranked by how often they are co-mentioned with
  those terms in PubMed, using GeneRIF and the automatically generated AutoRIF gene-publication
  associations. It also predicts further related genes from gene-gene similarity matrices
  built from ARCHS4 co-expression, Tagger literature co-occurrence, Enrichr gene-list
  co-occurrence, and GeneRIF/AutoRIF co-mentions. Results can be filtered by druggable
  genome families.
domains:
- literature
- genomics
- biomedical
homepage_url: https://maayanlab.cloud/geneshot/
id: geneshot
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0 (source code); commercial users should contact Mount Sinai Innovation
    Partners for licensing
name: Geneshot
products:
- category: GraphicalInterface
  description: Web search engine that returns genes ranked by co-mention with arbitrary
    search terms in PubMed, with gene function prediction and gene set augmentation
    pages.
  format: http
  id: geneshot.portal
  name: Geneshot Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  product_url: https://maayanlab.cloud/geneshot/
- category: ProgrammingInterface
  description: REST API with POST endpoints to search PubMed-linked gene rankings,
    retrieve gene publications and histograms, and get associated or predicted genes
    from similarity matrices.
  format: json
  id: geneshot.api
  is_public: true
  name: Geneshot API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  product_url: https://maayanlab.cloud/geneshot/api.html
- category: Product
  description: Download page for the GeneRIF and AutoRIF gene-publication associations
    and the gene-gene similarity matrices used by Geneshot.
  format: http
  id: geneshot.downloads
  name: Geneshot Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  product_url: https://maayanlab.cloud/geneshot/download.html
- category: Product
  description: Human gene to PubMed article associations from NCBI GeneRIF, with dates
    replaced by publication dates.
  format: tsv
  id: geneshot.generif
  name: GeneRIF Gene-Publication Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 14546796
  product_url: https://s3.amazonaws.com/mssm-data/generif.tsv
- category: Product
  description: Automatically generated human gene to PubMed article associations,
    built by querying PubMed with all human gene symbols.
  format: tsv
  id: geneshot.autorif
  name: AutoRIF Gene-Publication Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 626888558
  product_url: https://s3.amazonaws.com/mssm-data/autorif.tsv
- category: Product
  compression: zip
  description: Gene-gene correlation matrix from ARCHS4 human RNA-seq data, used by
    Geneshot to predict related genes.
  format: tsv
  id: geneshot.archs4-correlation
  name: ARCHS4 Gene Co-expression Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: archs4
  product_file_size: 4246282120
  product_url: https://s3.amazonaws.com/mssm-data/correlation.tsv.zip
- category: Product
  description: Gene-gene co-occurrence matrix computed from gene lists submitted to
    Enrichr, used by Geneshot to predict related genes.
  format: tsv
  id: geneshot.enrichr-cooccurrence
  name: Enrichr Gene Co-occurrence Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_file_size: 1593574495
  product_url: https://s3.amazonaws.com/mssm-data/list_off_co.tsv
- category: Product
  description: Statistics for the 29 drug set libraries (109,284 terms) served by
    DrugEnrichr, built from ATC, the Drug Repurposing Hub, KINOMEscan, PharmGKB and
    OFFSIDES, DrugCentral, CREEDS, Geneshot, L1000FWD, SIDER, and STITCH. Each library
    can be downloaded as a GMT-style text file from the geneSetLibrary endpoint (mode=text&libraryName=<library>).
  format: json
  id: drugenrichr.libraries
  name: DrugEnrichr Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  product_file_size: 4251
  product_url: https://maayanlab.cloud/DrugEnrichr/datasetStatistics
- category: GraphProduct
  description: Core ReproTox-KG graph linking birth defects, drugs, and genes from
    DrugShot, DrugEnrichr, and GeneShot literature co-mention evidence (1,433 nodes,
    2,252 edges).
  format: json
  id: reprotox-kg.graph.core
  name: ReproTox-KG Core Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  product_file_size: 1649245
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/reprotox_serialization.valid.json
- category: GraphProduct
  description: Birth defect phenotype to gene associations from GeneShot literature
    co-mentions (6,064 nodes, 13,487 edges).
  format: json
  id: reprotox-kg.graph.geneshot-hpo
  name: ReproTox-KG GeneShot HPO-Gene Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: geneshot
  product_file_size: 7214043
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/Geneshot_HPO_to_Gene.valid.json
publications:
- authors:
  - Lachmann A
  - Schilder BM
  - Wojciechowicz ML
  - Torre D
  - Kuleshov MV
  - Keenan AB
  - Ma'ayan A
  doi: 10.1093/nar/gkz393
  id: PMID:31114885
  journal: Nucleic Acids Res
  preferred: true
  title: 'Geneshot: search engine for ranking genes from arbitrary text queries'
  year: '2019'
synonyms:
- GeneShot
taxon:
- NCBITaxon:9606
---
# Geneshot

Geneshot, from the Ma'ayan Laboratory at the Icahn School of Medicine at Mount Sinai, ranks human genes by their relevance to any search terms. It queries PubMed through NCBI E-utilities and cross-references the matching articles with gene-publication associations from GeneRIF (about 396,000) or AutoRIF (about 4.9 million), an automated expansion built by querying PubMed with every human gene symbol. Genes are ranked by how often they are co-mentioned with the search terms.

## Predictions and data

Geneshot predicts further related genes from gene-gene similarity matrices: ARCHS4 RNA-seq co-expression, Tagger literature co-occurrence, Enrichr gene-list co-occurrence, and GeneRIF/AutoRIF co-mentions. Results can be filtered to druggable genome families (kinases, ion channels, and GPCRs, including understudied members). The association files and similarity matrices are downloadable; the download page lists older, smaller file sizes than the files now served.

## Access and terms

Geneshot is available as a web application and a REST API. Its help page states that the source code is available under the Apache License 2.0 and that commercial users should contact Mount Sinai Innovation Partners, but the GitHub repository it links (MaayanLab/geneshot) returned 404 when checked on 2026-10-10. Geneshot feeds the GeneShot HPO-gene graph in ReproTox-KG.