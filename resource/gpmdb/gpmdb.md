---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.thegpm.org/
  label: The Global Proteome Machine Organization
- category: Individual
  label: Ronald C. Beavis
creation_date: '2026-10-04T00:00:00Z'
description: The Global Proteome Machine Database (GPMDB) stores peptide and protein
  identifications from tandem mass spectrometry experiments, reprocessed with the
  Global Proteome Machine pipeline and the X! Tandem search engine. It reports observed
  peptide and protein evidence, post-translational modifications and single amino
  acid variants across a very large number of public datasets, mapped mainly to Ensembl
  protein accessions. Since 2025-02-19 the GPMDB web interface rejects queries from
  US IP addresses; the REST API still answered from a US address on 2026-10-04.
domains:
- proteomics
homepage_url: https://www.thegpm.org/
id: gpmdb
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: Global Proteome Machine Database
products:
- category: GraphicalInterface
  description: GPMDB web interface for searching peptide and protein identifications,
    observation counts, modifications and variants.
  format: http
  id: gpmdb.portal
  name: GPMDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  product_url: https://gpmdb.thegpm.org/
  warnings:
  - Returned HTTP 403 when checked on 2026-10-04 from a US address. A GPM blog post
    of 2025-02-19 says US IP addresses are no longer allowed to query GPMDB.
- category: ProgrammingInterface
  description: GPMDB REST API (version 2015.02.19) returning JSON for protein and
    peptide observation counts, best expectation values, peptide sequences, charge
    states, modifications, single amino acid variants and protein sequences, keyed
    by protein accession (mainly Ensembl ENSP identifiers) or peptide sequence.
  format: json
  id: gpmdb.api
  name: GPMDB REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:used
    source: ensembl
  product_url: https://rest.thegpm.org/1
- category: ProcessProduct
  description: X! Tandem, the open source search engine that matches tandem mass spectra
    to peptide sequences and underlies the GPM pipeline that populates GPMDB. Latest
    release ALANINE (2017.02.01).
  id: gpmdb.xtandem
  license:
    id: https://opensource.org/licenses/Artistic-1.0
    label: Artistic License
  name: X! Tandem
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  product_url: https://www.thegpm.org/tandem/
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
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
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
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Robertson Craig
  - John P. Cortens
  - Ronald C. Beavis
  doi: 10.1021/pr049882h
  id: doi:10.1021/pr049882h
  journal: Journal of Proteome Research
  preferred: true
  title: Open Source System for Analyzing, Validating, and Storing Protein Identification
    Data
  year: '2004'
- authors:
  - Robertson Craig
  - Ronald C. Beavis
  doi: 10.1093/bioinformatics/bth092
  id: doi:10.1093/bioinformatics/bth092
  journal: Bioinformatics
  title: 'TANDEM: matching proteins with tandem mass spectra'
  year: '2004'
synonyms:
- GPMDB
- The Global Proteome Machine
- GPM
---
# Global Proteome Machine Database

GPMDB collects peptide and protein identifications from public tandem mass spectrometry data, reprocessed with the Global Proteome Machine (GPM) pipeline and the X! Tandem search engine. For each protein it reports how often it was observed, the peptides seen, the best expectation values, observed post-translational modifications and single amino acid variants. Proteins are keyed mainly by Ensembl protein accessions.

## Access

- **Web interface**: https://gpmdb.thegpm.org/. A GPM blog post of 2025-02-19 says that, because of the trade dispute between the USA and Canada, US IP addresses can no longer query GPMDB. The interface returned HTTP 403 from a US address on 2026-10-04.
- **REST API**: https://rest.thegpm.org/1 lists its endpoints, such as `/1/protein/count/acc=ACC` and `/1/peptide/count/seq=SEQ`. It answered from a US address on 2026-10-04. The API reports version 2015.02.19. Its listing points to documentation on wiki.thegpm.org, which did not respond.
- **X! Tandem**: the search engine is distributed from https://www.thegpm.org/tandem/ under the Artistic License.

## License

The GPM site carries a copyright notice (The Global Proteome Machine, 2024) and states no data license. X! Tandem and its documentation are under the Artistic License.