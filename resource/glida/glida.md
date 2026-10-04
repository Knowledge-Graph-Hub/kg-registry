---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://pharminfo.pharm.kyoto-u.ac.jp/
  label: PharmacoInformatics Laboratory, Graduate School of Pharmaceutical Sciences,
    Kyoto University
creation_date: '2026-10-04T00:00:00Z'
description: GLIDA (GPCR-LIgand DAtabase) was a database of G protein-coupled receptors
  (GPCRs) and their known ligands, built by the PharmacoInformatics Laboratory at
  Kyoto University for chemical genomics research and GPCR-related drug discovery.
  It linked biological information on GPCRs with chemical information on their ligands,
  could be searched from either side, and offered a GPCR-ligand correlation map and
  analysis tools. Its last listed version was 2.04 (2010-10-10). GLIDA is defunct,
  and its homepage has returned HTTP 404 since at least 2025. GLIDA was one of the
  curated databases used as evidence by STITCH.
domains:
- drug discovery
- pharmacology
- chemistry and biochemistry
- cheminformatics
homepage_url: http://pharminfo.pharm.kyoto-u.ac.jp/services/glida/
id: glida
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: GLIDA
products:
- category: GraphicalInterface
  description: Former GLIDA web database for searching GPCRs and their ligands, cross-searchable
    by receptor or ligand, with a GPCR-ligand correlation map.
  format: http
  id: glida.portal
  name: GLIDA Web Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://pharminfo.pharm.kyoto-u.ac.jp/services/glida/
  warnings:
  - The site was not available when checked on 2026-10-04. The server returned HTTP
    404, and Wayback Machine captures have recorded 404 since 2025.
- category: GraphicalInterface
  description: Archived snapshot of the GLIDA homepage (version 2.04) in the Internet
    Archive Wayback Machine, the last capture before the site went offline.
  format: http
  id: glida.wayback
  name: GLIDA homepage (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://web.archive.org/web/20181108212124/http://pharminfo.pharm.kyoto-u.ac.jp:80/services/glida/
- category: DocumentationProduct
  description: GLIDA user manual (PDF), archived in the Internet Archive Wayback Machine.
  format: pdf
  id: glida.manual
  name: GLIDA Manual (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://web.archive.org/web/2007/http://pharminfo.pharm.kyoto-u.ac.jp/services/glida/data/GLIDA_MANUAL.pdf
- category: Product
  description: Web interface for searching and visualizing chemical-protein interactions
    across organisms
  format: http
  id: stitch.portal
  is_public: true
  name: STITCH Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/
- category: Product
  description: Downloadable data files containing chemical-protein interaction networks
  format: tsv
  id: stitch.downloads
  is_public: true
  name: STITCH Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/download.pl
- category: ProgrammingInterface
  description: API for programmatic access to STITCH chemical-protein interaction
    data
  format: http
  id: stitch.api
  is_public: true
  name: STITCH API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/access.pl?footer_active_subpage=apis
publications:
- authors:
  - Y. Okuno
  doi: 10.1093/nar/gkj028
  id: doi:10.1093/nar/gkj028
  journal: Nucleic Acids Research
  preferred: true
  title: 'GLIDA: GPCR-ligand database for chemical genomic drug discovery'
  year: '2006'
- authors:
  - Y. Okuno
  - A. Tamon
  - H. Yabuuchi
  - S. Niijima
  - Y. Minowa
  - K. Tonomura
  - R. Kunimoto
  - C. Feng
  doi: 10.1093/nar/gkm948
  id: doi:10.1093/nar/gkm948
  journal: Nucleic Acids Research
  title: 'GLIDA: GPCR ligand database for chemical genomics drug discovery database
    and tools update'
  year: '2007'
synonyms:
- GPCR-LIgand DAtabase
- GPCR-Ligand Database
taxon:
- NCBITaxon:9606
---
# GLIDA

GLIDA (GPCR-LIgand DAtabase) was a database of G protein-coupled receptors and their known ligands from the PharmacoInformatics Laboratory at Kyoto University (Yasushi Okuno and colleagues). It was built for researchers working on GPCR-related drug discovery, including the search for ligands of orphan GPCRs.

The database combined biological information on GPCRs with chemical information on their ligands. Users could enter by GPCR search or ligand search and move between the two, and a GPCR-ligand correlation map summarized the known pairs. The 2008 update added analysis tools for chemical genomics.

## Status

GLIDA is defunct. The last version listed on its homepage was 2.04, dated 2010-10-10. The Internet Archive holds working captures of the homepage up to 2018-11-08. Captures from 2025 onward, and a direct check on 2026-10-04, return HTTP 404. No bulk download of the data was found in the archived pages.

## Usage

GLIDA was one of the curated databases that STITCH used as an evidence source for chemical-protein interactions. For current GPCR-ligand data, see the IUPHAR/BPS Guide to Pharmacology, ChEMBL and GPCRdb.