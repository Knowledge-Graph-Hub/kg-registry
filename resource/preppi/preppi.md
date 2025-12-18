---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://wiki.c2b2.columbia.edu/honiglab_public/index.php/Main_Page
  label: Honig Laboratory
- category: Individual
  contact_details:
  - contact_type: other
    value: Professor, Columbia University Department of Biochemistry and Molecular
      Biophysics
  label: Barry Honig
creation_date: '2025-11-10T00:00:00Z'
description: 'PrePPI (Predicting Protein-Protein Interactions) is a computational
  structure-based database of predicted protein-protein interactions for the human
  proteome, developed by the Honig Laboratory at Columbia University. The database
  employs a Bayesian framework that integrates structural information with non-structural
  supporting evidence to predict protein-protein interactions. PrePPI uses structural
  modeling to generate putative protein interaction interfaces, scores these structural
  models, and combines the structural scores with functional clues and other evidence
  sources to produce confidence scores for predicted interactions. The database provides
  comprehensive coverage of the human interactome, going beyond experimentally determined
  interactions to include computationally predicted interactions with varying levels
  of confidence. PrePPI is particularly valuable for identifying novel protein interactions
  that may not yet have been experimentally validated but show promise based on structural
  compatibility and functional context. Users can query the database by entering UniProt
  accession numbers or common gene/protein names to retrieve interaction partners
  and supporting evidence. The resource includes a high-confidence interactome subset
  that can be downloaded, representing predictions with the strongest supporting evidence.
  PrePPI complements experimental protein interaction databases by providing structure-based
  predictions that can guide experimental validation efforts and inform systems biology
  studies of protein interaction networks. The database is freely accessible through
  a web interface that allows interactive exploration of predicted interactions and
  their confidence scores.

  '
domains:
- proteomics
- chemistry and biochemistry
homepage_url: https://honiglab.c2b2.columbia.edu/PrePPI/
id: preppi
infores_id: preppi
last_modified_date: '2025-11-10T00:00:00Z'
layout: resource_detail
name: PrePPI
products:
- category: GraphicalInterface
  description: Web search interface for querying PrePPI predicted protein-protein
    interactions by UniProt accession or gene name
  id: preppi.search
  name: PrePPI Search Interface
  product_url: https://honiglab.c2b2.columbia.edu/PrePPI/
- category: Product
  description: High-confidence PrePPI interactome dataset for download
  format: txt
  id: preppi.download
  name: PrePPI High-Confidence Interactome
  original_source:
  - preppi
  product_url: https://honiglab.c2b2.columbia.edu/PrePPI/ref/preppi.human_af.interactome.txt.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-12-17_ Error connecting
    to URL_ HTTPSConnectionPool(host='honiglab.c2b2.columbia.edu', port=443)_ Max
    retries exceeded with url_ /PrePPI/ref/preppi.human_af.interactome.txt.tar.gz
    (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - File was not able to be retrieved when checked on 2025-12-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='honiglab.c2b2.columbia.edu', port=443)_ Max
    retries exceeded with url_ /PrePPI/ref/preppi.human_af.interactome.txt.tar.gz
    (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1000)')))
  - File was not able to be retrieved when checked on 2025-11-21_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2025-12-18_ Error connecting
    to URL_ HTTPSConnectionPool(host='honiglab.c2b2.columbia.edu', port=443)_ Max
    retries exceeded with url_ /PrePPI/ref/preppi.human_af.interactome.txt.tar.gz
    (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ unable to get local issuer certificate (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-12-18: Error connecting
    to URL: HTTPSConnectionPool(host=''honiglab.c2b2.columbia.edu'', port=443): Max
    retries exceeded with url: /PrePPI/ref/preppi.human_af.interactome.txt.tar.gz
    (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: unable to get local issuer certificate (_ssl.c:1017)'')))'
publications:
- doi: 10.1016/j.jmb.2023.168052
  id: doi:10.1016/j.jmb.2023.168052
  title: 'PrePPI: a structure-informed database of protein-protein interactions'
synonyms:
- PrePPI
- Predicting Protein-Protein Interactions
taxon:
- NCBITaxon:9606
---
