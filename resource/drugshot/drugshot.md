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
    value: eryk.kropiwnicki@icahn.mssm.edu
  label: Eryk Kropiwnicki
creation_date: '2026-10-10T00:00:00Z'
description: DrugShot is a web server from the Ma'ayan Laboratory that takes any biomedical
  search term and returns drugs and small molecules ranked by how often they are co-mentioned
  with that term in PubMed, using the automatically generated DrugRIF and AutoRIF
  drug-publication associations. It also predicts additional compounds from drug-drug
  similarity matrices built from literature co-mentions and from L1000 drug-induced
  gene expression signatures.
domains:
- literature
- drug discovery
- drug repositioning
- biomedical
homepage_url: https://maayanlab.cloud/drugshot/
id: drugshot
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0 (source code); commercial users should contact Mount Sinai Innovation
    Partners for licensing
name: DrugShot
products:
- category: GraphicalInterface
  description: Web server that returns drugs and small molecules ranked by co-mention
    with any biomedical search term in PubMed, with drug set augmentation.
  format: http
  id: drugshot.portal
  name: DrugShot Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_url: https://maayanlab.cloud/drugshot/
- category: ProgrammingInterface
  description: REST API with POST endpoints to search PubMed-linked drug rankings,
    retrieve drug publications, and get associated drugs from literature co-mention
    or L1000 signature similarity.
  format: json
  id: drugshot.api
  is_public: true
  name: DrugShot API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_url: https://maayanlab.cloud/drugshot/api.html
- category: Product
  description: Download page for the DrugRIF and AutoRIF drug-publication associations
    and the drug-drug similarity matrices used by DrugShot.
  format: http
  id: drugshot.downloads
  name: DrugShot Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_url: https://maayanlab.cloud/drugshot/download.html
- category: Product
  compression: gzip
  description: About 2 million drug to PubMed article associations, built by querying
    PubMed with the InChIKeys of Drugmonizome and SEP-L1000 compounds via PubChem.
  format: tsv
  id: drugshot.drugrif
  name: DrugRIF Drug-Publication Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_file_size: 9016822
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/DrugRIF.tsv.gz
- category: Product
  compression: gzip
  description: About 8 million drug to PubMed article associations, built by querying
    PubMed with drug names matched to MeSH.
  format: tsv
  id: drugshot.autorif
  name: AutoRIF Drug-Publication Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 33310010
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/AutoRIF.tsv.gz
- category: Product
  description: Drug-drug similarity matrix from cosine similarity of L1000 drug-induced
    gene expression signatures (SEP-L1000), used to predict related compounds.
  format: hdf5
  id: drugshot.l1000-similarity
  name: L1000 Drug-Drug Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 1550026868
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/L1000_coexpression.h5
- category: Product
  description: Drug-drug co-mention matrix computed from AutoRIF literature associations.
  format: hdf5
  id: drugshot.autorif-cooccurrence
  name: AutoRIF Drug Co-mention Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 162117904
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/autorif_cooccur.h5
- category: Product
  description: Drug-drug co-mention matrix computed from DrugRIF literature associations.
  format: hdf5
  id: drugshot.drugrif-cooccurrence
  name: DrugRIF Drug Co-mention Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 153696656
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/drugrif_cooccur.h5
- category: ProcessProduct
  description: Source code for the DrugShot web server, with notebooks for building
    the DrugRIF associations and similarity matrices. Apache-2.0 license.
  format: python
  id: drugshot.source
  name: DrugShot Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_url: https://github.com/MaayanLab/drugshot
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
  description: Birth defect phenotype to drug associations from DrugShot literature
    co-mentions (2,802 nodes, 12,502 edges).
  format: json
  id: reprotox-kg.graph.drugshot-hpo
  name: ReproTox-KG DrugShot HPO-Drug Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_file_size: 8941255
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/Drugshot_HPO_to_Drug.valid.json
publications:
- authors:
  - Kropiwnicki E
  - Lachmann A
  - Clarke DJB
  - Xie Z
  - Jagodnik KM
  - Ma'ayan A
  doi: 10.1186/s12859-022-04590-5
  id: PMID:35183110
  journal: BMC Bioinformatics
  preferred: true
  title: 'DrugShot: querying biomedical search terms to retrieve prioritized lists
    of small molecules'
  year: '2022'
repository: https://github.com/MaayanLab/drugshot
---
# DrugShot

DrugShot, from the Ma'ayan Laboratory at the Icahn School of Medicine at Mount Sinai, ranks drugs and small molecules by their relevance to any biomedical search term. It queries PubMed through NCBI E-utilities and cross-references the matching articles with automatically generated drug-publication associations.

## Data

DrugRIF holds about 2 million drug-publication associations, built by querying PubMed with the InChIKeys of Drugmonizome and SEP-L1000 compounds through PubChem. AutoRIF holds about 8 million, built by querying PubMed with drug names matched to MeSH. DrugShot predicts additional compounds from drug-drug similarity matrices based on DrugRIF and AutoRIF co-mentions and on cosine similarity of L1000 drug-induced gene expression signatures from SEP-L1000. All of these files are downloadable. (On the download page, the AutoRIF link points to the DrugRIF file; the AutoRIF file listed here is the one the application loads.)

## Access and terms

DrugShot is available as a web application and a REST API. The source code is on GitHub under the Apache License 2.0; commercial users are asked to contact Mount Sinai Innovation Partners. DrugShot feeds the DrugShot HPO-drug graph in ReproTox-KG.