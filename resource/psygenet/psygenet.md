---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@psygenet.org
  - contact_type: url
    value: http://ibi.imim.es/
  label: Integrative Biomedical Informatics Group (IBI), Research Programme on Biomedical
    Informatics (GRIB), IMIM / Universitat Pompeu Fabra
- category: Individual
  contact_details:
  - contact_type: email
    value: laura.furlong@upf.edu
  label: Laura I. Furlong
creation_date: '2025-07-12T00:00:00Z'
description: PsyGeNET is a knowledge resource on psychiatric disorders and their associated
  genes, integrating expert-curated and text-mined data from the literature. It provides
  gene-disease associations for psychiatric disorders, supporting research in psychiatric
  genetics and genomics.
domains:
- biomedical
- genomics
- neuroscience
- mental disorders
funding:
- Instituto de Salud Carlos III (ISCIII) (CP10/00524)
- Instituto de Salud Carlos III (ISCIII) (PI13/00082)
- Instituto de Salud Carlos III (ISCIII) (PT13/0001/0023)
- European Commission Horizon 2020 (634143)
- European Commission Horizon 2020 (676559)
homepage_url: https://www.psygenet.org/
id: psygenet
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: PsyGeNET
products:
- category: Product
  description: Gene-disease associations for psychiatric disorders as a gzipped tar
    archive of a tab-delimited file (psygenet_v02.txt) with gene, UMLS disease concept,
    psychiatric disorder class, supporting abstract counts, source and score; the PsyGeNET
    2.0 homepage reports 3,771 associations between 1,549 genes and 117 psychiatric
    disease concepts.
  format: tsv
  id: psygenet.genedisease
  name: PsyGeNET Gene-Disease Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://web.archive.org/web/20230105023523/http://www.psygenet.org/ds/PsyGeNET/results/all_GeneDiseaseAssociations.tar.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  warnings:
  - The original download link on psygenet.org returned HTTP 404 on 2026-11-12; the
    product URL points to an Internet Archive copy of the file captured in January
    2023.
- category: Product
  description: PsyGeNET corpus of expert-annotated sentences from MEDLINE abstracts
    describing gene-psychiatric disorder associations, with gene, UMLS disease concept,
    PubMed ID and association type, distributed as a tar archive with a readme.
  format: mixed
  id: psygenet.corpus
  name: PsyGeNET Corpus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://web.archive.org/web/20220128194746/http://www.psygenet.org/ds/PsyGeNET/results/psygenetCorpus.tar
  warnings:
  - The original download link on psygenet.org returned HTTP 404 on 2026-11-12; the
    product URL points to an Internet Archive copy of the file captured in January
    2022.
- category: ProcessProduct
  description: R/Bioconductor package for querying PsyGeNET and performing comorbidity
    studies with PsyGeNET data
  format: http
  id: psygenet.psygenet2r
  license:
    id: https://spdx.org/licenses/MIT.html
    label: MIT
  name: psygenet2r R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psygenet
  product_url: https://bioconductor.org/packages/3.20/bioc/html/psygenet2r.html
  repository: https://git.bioconductor.org/packages/psygenet2r
  warnings:
  - psygenet2r was deprecated in Bioconductor 3.20 and removed with the Bioconductor
    3.21 release; the product URL points to the last Bioconductor 3.20 package page.
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  format: http
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
publications:
- authors:
  - Alba Gutiérrez-Sacristán
  - Solène Grosdidier
  - Olga Valverde
  - Marta Torrens
  - Àlex Bravo
  - Janet Piñero
  - Ferran Sanz
  - Laura I. Furlong
  doi: 10.1093/bioinformatics/btv301
  id: doi:10.1093/bioinformatics/btv301
  journal: Bioinformatics
  preferred: true
  title: 'PsyGeNET: a knowledge platform on psychiatric disorders and their genes'
  year: '2015'
- authors:
  - Alba Gutiérrez-Sacristán
  - Carles Hernández-Ferrer
  - Juan R González
  - Laura I Furlong
  doi: 10.1093/bioinformatics/btx506
  id: doi:10.1093/bioinformatics/btx506
  journal: Bioinformatics
  title: 'psygenet2r: a R/Bioconductor package for the analysis of psychiatric disease
    genes'
  year: '2017'
- authors:
  - Alba Gutiérrez-Sacristán
  - Àlex Bravo
  - Marta Portero-Tresserra
  - Olga Valverde
  - Antonio Armario
  - M.C. Blanco-Gandía
  - Adriana Farré
  - Lierni Fernández-Ibarrondo
  - Francina Fonseca
  - Jesús Giraldo
  - Angela Leis
  - Anna Mané
  - M.A. Mayer
  - Sandra Montagud-Romero
  - Roser Nadal
  - Jordi Ortiz
  - Francisco Javier Pavon
  - Ezequiel Jesús Perez
  - Marta Rodríguez-Arias
  - Antonia Serrano
  - Marta Torrens
  - Vincent Warnault
  - Ferran Sanz
  - Laura I. Furlong
  doi: 10.1093/database/bax043
  id: doi:10.1093/database/bax043
  journal: Database
  title: Text mining and expert curation to develop a database on psychiatric diseases
    and their genes
  year: '2017'
rrid: SCR_014406
synonyms:
- Psychiatric disorders Gene association NETwork
taxon:
- NCBITaxon:9606
version: '2.0'
warnings:
- The PsyGeNET homepage responded on 2026-06-02 but identifies itself as an incomplete
  Wayback Machine Downloader copy, so direct website functionality may be unavailable.
- Several PsyGeNET subpages checked on 2026-06-02 either returned 404 or redirected
  to unrelated content; use the site and downloads with caution.
---
# PsyGeNET

PsyGeNET (Psychiatric disorders Gene association NETwork) is a psychiatric-disorder gene association resource developed by the Integrative Biomedical Informatics Group (GRIB, IMIM/UPF, Barcelona). Associations were extracted from MEDLINE with the BeFree text-mining tool and then reviewed by a team of 22 domain experts. Version 2.0 (data updated September 2016) covers depression, bipolar disorder, schizophrenia, alcohol, cocaine and cannabis use disorders, and substance-induced depressive and psychotic disorders, with 3,771 associations between 1,549 genes and 117 disease concepts.

The original web application is no longer reliably available: psygenet.org now serves an incomplete static copy and its download links return 404. The gene-disease association file and the PsyGeNET corpus remain available through Internet Archive copies, and the psygenet2r R package was removed from Bioconductor in release 3.21. The archived legal notice states that the database is released under CC BY-NC-SA 4.0 (the archived downloads page instead mentions the Open Database License).