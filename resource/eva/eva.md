---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: eva-helpdesk@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/eva/
  - contact_type: github
    value: EBIvariation
  id: ebi
  label: European Variation Archive team, EMBL-EBI
creation_date: '2026-10-04T00:00:00Z'
description: The European Variation Archive (EVA) is EMBL-EBI's open-access archive
  for genetic variation data from all species. It accepts submitted VCF studies, archives
  and annotates the variants, and assigns submitted (SS) and clustered (RS) variant
  accessions. For non-human species it took over the legacy dbSNP variant data and
  is now the reference archive that issues RS IDs, released as periodic RefSNP releases
  (release 9, May 2026, covering 315 species).
domains:
- genomics
- genetic variation
homepage_url: https://www.ebi.ac.uk/eva/
id: eva
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: European Variation Archive
products:
- category: GraphicalInterface
  description: EVA web portal with the Study Browser, Variant Browser, RS release
    pages, submission instructions and help.
  format: http
  id: eva.portal
  name: EVA Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://www.ebi.ac.uk/eva/
- category: GraphicalInterface
  description: Variant Browser for querying EVA variants by study, gene, chromosomal
    location or variant identifier, per species and assembly.
  format: http
  id: eva.variant-browser
  name: EVA Variant Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://www.ebi.ac.uk/eva/?Variant-Browser
- category: ProgrammingInterface
  description: EVA REST web services (v1) for studies, files, variants, segments,
    genes and species metadata, documented with Swagger UI.
  format: http
  id: eva.api
  name: EVA REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://www.ebi.ac.uk/eva/webservices/rest/swagger-ui.html
  repository: https://github.com/EBIvariation/eva-ws
- category: ProgrammingInterface
  description: EVA accessioning web services for looking up submitted (SS) and clustered
    (RS) variant accessions, documented with Swagger UI.
  format: http
  id: eva.identifiers-api
  name: EVA Identifiers API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://www.ebi.ac.uk/eva/webservices/identifiers/swagger-ui.html
- category: Product
  description: EVA RefSNP (RS) releases, one directory per release, browsable by species
    and by assembly accession. Each assembly folder holds current, merged, deprecated
    and merged-deprecated RS ID files (VCF and text, gzip), and each species folder
    an unmapped IDs file. Release 9 (May 2026) covers 315 species. RS IDs for non-human
    species include variants imported from dbSNP.
  format: mixed
  id: eva.rs-releases
  latest_version: release_9
  name: EVA RefSNP Releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  product_url: https://ftp.ebi.ac.uk/pub/databases/eva/rs_releases/
- category: Product
  description: EVA FTP site with one directory per EVA project (PRJEB accession) holding
    the submitted VCF files for projects loaded into the variant warehouse, plus ClinVar
    and COVID-19 release folders.
  format: vcf
  id: eva.ftp
  name: EVA FTP Project Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://ftp.ebi.ac.uk/pub/databases/eva/
- category: DocumentationProduct
  description: EVA help pages, including FAQs, accessioning details and data submission
    guidance.
  format: http
  id: eva.help
  name: EVA Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://www.ebi.ac.uk/eva/?Help
- category: ProcessProduct
  description: EVA source code repositories on GitHub, including the web services,
    pipeline, accessioning service and OmicsDI exporter (web services under Apache-2.0).
  format: mixed
  id: eva.code
  name: EVA GitHub Organization
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eva
  product_url: https://github.com/EBIvariation
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Timothe Cezard
  - Fiona Cunningham
  - Sarah E Hunt
  - Baron Koylass
  - Nitin Kumar
  - Gary Saunders
  - April Shen
  - Andres F Silva
  - Kirill Tsukanov
  - Sundararaman Venkataraman
  - Paul Flicek
  - Helen Parkinson
  - Thomas M Keane
  doi: 10.1093/nar/gkab960
  id: doi:10.1093/nar/gkab960
  journal: Nucleic Acids Research
  preferred: true
  title: 'The European Variation Archive: a FAIR resource of genomic variation for
    all species'
  year: '2022'
repository: https://github.com/EBIvariation
synonyms:
- EVA
---
# European Variation Archive

The European Variation Archive (EVA) at EMBL-EBI is an open-access archive of genetic variation data for all species. Researchers submit variant studies in VCF format, and EVA archives, validates and annotates them and assigns permanent accessions:

- **SS (SubSnp)** accessions for each submitted allele change in a study.
- **RS (RefSnp)** accessions for clusters of SS IDs at the same locus.

EVA's workflow is aligned with NCBI's dbSNP, dbVar and ClinVar. Since dbSNP stopped accepting non-human variants, EVA imported the legacy dbSNP non-human data and is now the archive that issues RS IDs for non-human species.

## Access

- **Web portal** with a Study Browser and a Variant Browser.
- **REST API** (v1) and an **identifiers API** for SS/RS accession lookups, both documented with Swagger UI.
- **FTP**: submitted VCF files per project, and periodic **RefSNP releases** organized by species and assembly (release 9, May 2026, 315 species).

## Notes

- Data are open access under the EMBL-EBI Terms of Use. I found no separate data license statement on the EVA site.
- EVA is indexed by OmicsDI.
- The release FTP has no stable `latest` link. The `eva.rs-releases` product points to the release index and records `release_9` as the latest version.