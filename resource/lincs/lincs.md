---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ilincs@googlegroups.com
  label: BD2K-LINCS Data Coordination and Integration Center
- category: Organization
  label: National Institutes of Health (NIH) Common Fund
description: The Library of Integrated Network-based Cellular Signatures (LINCS) is
  a comprehensive collection of data that catalogs how human cells globally respond
  to chemical, genetic, and disease perturbations. It aims to better understand human
  disease and advance the development of new therapies by assembling an integrated
  picture of the range of responses of human cells exposed to many perturbations.
domains:
- biomedical
- drug discovery
- systems biology
- genomics
- proteomics
- precision medicine
homepage_url: https://lincsportal.ccs.miami.edu/signatures/home
id: lincs
layout: resource_detail
name: LINCS
products:
- category: GraphicalInterface
  description: Web interface that allows users to explore, analyze, and visualize
    LINCS signatures and datasets.
  id: lincs.portal
  name: LINCS Data Portal 2.0
  product_url: https://lincsportal.ccs.miami.edu/signatures/home
- category: ProgrammingInterface
  description: API for programmatic access to LINCS data and signatures.
  id: lincs.api
  is_public: true
  name: LINCS API
  product_url: https://lincsportal.ccs.miami.edu/sigc-api/swagger-ui.html#/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- authors:
  - Keenan AB
  - Jenkins SL
  - Jagodnik KM
  - Koplev S
  - He E
  - Torre D
  - Wang Z
  - Dohlman AB
  - Silverstein MC
  - Lachmann A
  - Kuleshov MV
  - Ma'ayan A
  - Stathias V
  - Terryn R
  - Cooper D
  - Forlin M
  - Koleti A
  - Vidovic D
  - Chung C
  - "Sch\xFCrer SC"
  - Vasiliauskas J
  - Pilarczyk M
  - Shamsaei B
  - Fazel M
  - Ren Y
  - Niu W
  - Clark NA
  - White S
  - Mahi N
  - Zhang L
  - Kouril M
  - Reichard JF
  - Sivaganesan S
  - Medvedovic M
  - Meller J
  - Koch RJ
  - Birtwistle MR
  - Iyengar R
  - Sobie EA
  - Azeloglu EU
  - Kaye J
  - Osterloh J
  - Haston K
  - Kalra J
  - Finkbiener S
  - Li J
  - Milani P
  - Adam M
  - Escalante-Chong R
  - Sachs K
  - Lenail A
  - Ramamoorthy D
  - Fraenkel E
  - Daigle G
  - Hussain U
  - Coye A
  - Rothstein J
  - Sareen D
  - Ornelas L
  - Banuelos M
  - Mandefro B
  - Ho R
  - Svendsen CN
  - Lim RG
  - Stocksdale J
  - Casale MS
  - Thompson TG
  - Wu J
  - Thompson LM
  - Dardov V
  - Venkatraman V
  - Matlock A
  - Van Eyk JE
  - Jaffe JD
  - Papanastasiou M
  - Subramanian A
  - Golub TR
  - Erickson SD
  - Fallahi-Sichani M
  - Hafner M
  - Gray NS
  - Lin JR
  - Mills CE
  - Muhlich JL
  - Niepel M
  - Shamu CE
  - Williams EH
  - Wrobel D
  - Sorger PK
  - Heiser LM
  - Gray JW
  - Korkola JE
  - Mills GB
  - LaBarge M
  - Feiler HS
  - Dane MA
  - Bucher E
  - Nederlof M
  - Sudar D
  - Gross S
  - Kilburn DF
  - Smith R
  - Devlin K
  - Margolis R
  - Derr L
  - Lee A
  - Pillai A
  doi: doi:10.1016/j.cels.2017.11.001
  id: https://doi.org/10.1016/j.cels.2017.11.001
  journal: Cell Systems
  preferred: true
  title: The Library of Integrated Network-Based Cellular Signatures NIH Program -
    System-Level Cataloging of Human Cells Response to Perturbations
  year: '2018'
- authors:
  - Koleti A
  - Terryn R
  - Stathias V
  - Chung C
  - Cooper DJ
  - Turner JP
  - Vidovic D
  - Forlin M
  - Kelley TT
  - D'Urso A
  - Allen BK
  - Torre D
  - Jagodnik KM
  - Wang L
  - Jenkins SL
  - Mader C
  - Niu W
  - Fazel M
  - Mahi N
  - Pilarczyk M
  - Clark N
  - Shamsaei B
  - Meller J
  - Vasiliauskas J
  - Reichard J
  - Medvedovic M
  - Ma'ayan A
  - Pillai A
  - "Sch\xFCrer SC"
  doi: doi:10.1093/nar/gkx1063
  id: https://doi.org/10.1093/nar/gkx1063
  journal: Nucleic Acids Research
  title: Data Portal for the Library of Integrated Network-based Cellular Signatures
    (LINCS) program - integrated access to diverse large-scale cellular perturbation
    response data
  year: '2018'
- authors:
  - Shen JP
  - Ozerov IV
  - Zhavoronkov A
  - Keenan AB
  - Koplev S
  - Jenkins SL
  - Jagodnik KM
  - Hallen A
  - Ma'ayan A
  doi: doi:10.1038/s41467-022-32205-3
  id: https://doi.org/10.1038/s41467-022-32205-3
  journal: Nature Communications
  title: Connecting omics signatures of diseases, drugs, and mechanisms of actions
    with iLINCS
  year: '2022'
---
The Library of Integrated Network-based Cellular Signatures (LINCS) is an NIH Common Fund program that catalogs how human cells globally respond to chemical, genetic, and disease perturbations. By assembling an integrated picture of the range of responses of human cells exposed to many perturbations, the LINCS program aims to better understand human disease and to advance the development of new therapies.

LINCS contains data on cellular responses to thousands of perturbagens (including drugs, genetic perturbations, tissue micro-environments, antibodies, and disease-causing mutations) across multiple cell types. These responses are measured using various high-throughput technologies including:

1. **L1000 Technology**: A cost-effective method to measure the expression of ~1,000 landmark genes that can be used to infer the expression of the rest of the transcriptome
2. **P100 Assay**: A targeted mass spectrometry-based proteomics approach that measures ~100 key phosphorylation sites
3. **Cell Painting**: A high-content imaging method that uses multiple fluorescent dyes to label different cellular components
4. **Other Assays**: Including RNA-seq, proteomics, epigenomics, and other cellular measurements

The program focuses on cellular physiology shared among tissues and cell types relevant to an array of diseases, including cancer, heart disease, and neurodegenerative disorders. The data generated by LINCS is freely available to the research community through various portals and tools, with iLINCS being one of the primary access points.

LINCS data has led to important research discoveries, including new tools for enhancing drug discovery and predicting adverse health events. Although the NIH Common Fund supported the LINCS program from 2011 to 2020, the data and resources continue to be available for researchers worldwide.