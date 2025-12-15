---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: The Human Reference Protein Interactome Mapping Project (HRPIMP) is a
  systematic effort to map binary protein-protein interactions in human cells. The
  project produced the Human Reference Interactome (HuRI) database containing high-quality
  experimentally validated protein-protein interactions. Using systematic yeast two-hybrid
  (Y2H) screening approaches, HRPIMP mapped interactions for 9,094 proteins, identifying
  64,006 binary protein-protein interactions. This comprehensive reference map of
  the human binary protein interactome provides essential data for understanding cellular
  mechanisms, disease pathways, and molecular networks. The data is freely available
  and has been integrated into multiple knowledge bases and research projects including
  studies of Alzheimer's Disease, cancer, and other complex diseases.
domains:
- proteomics
- systems biology
- biomedical
- biological systems
homepage_url: http://www.interactome-atlas.org/
id: hrpimp
last_modified_date: '2025-11-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Human Reference Protein Interactome Mapping Project
products:
- category: Product
  description: TSV files containing systematically mapped binary protein-protein interactions
    for 9,094 human proteins with 64,006 validated interactions
  format: tsv
  id: hrpimp.data
  name: HuRI Protein-Protein Interaction Data
  original_source:
  - hrpimp
  product_url: https://github.com/VIDallab/huri
  warnings:
  - File was not able to be retrieved when checked on 2025-12-13_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-15: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Web interface for browsing and exploring the Human Reference Interactome
  format: http
  id: hrpimp.web
  name: Interactome Atlas Web Portal
  original_source:
  - hrpimp
  product_url: http://www.interactome-atlas.org/
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Luck K
  - Kim DK
  - Lambourne L
  - Spirohn K
  - Begg BE
  - Bian W
  - Brignall R
  - Cafarelli T
  - Campos-Laborie FJ
  - Charloteaux B
  - Choi D
  - Coté AG
  - Daley M
  - Deimling S
  - Desbuleux A
  - Dricot A
  - Gebbia M
  - Hardy MF
  - Kishore N
  - Knapp JJ
  - Kovács IA
  - Lemmens I
  - Mee MW
  - Mellor JC
  - Pollis C
  - Pons C
  - Richardson AD
  - Schlabach S
  - Teeking B
  - Yadav A
  - Babor M
  - Balcha D
  - Basha O
  - Bowman-Colin C
  - Chin SF
  - Choi SG
  - Colabella C
  - Coppin G
  - D'Amata C
  - De Ridder D
  - De Rouck S
  - Duran-Frigola M
  - Ennajdaoui H
  - Goebels F
  - Goehring L
  - Gopal A
  - Haddad G
  - Hatchi E
  - Helmy M
  - Jacob Y
  - Kassa Y
  - Landini S
  - Li R
  - van Lieshout N
  - MacWilliams A
  - Markey D
  - Paulson JN
  - Rangarajan S
  - Rasla J
  - Rayhan A
  - Rolland T
  - San-Miguel A
  - Shen Y
  - Sheykhkarimli D
  - Sheynkman GM
  - Simonovsky E
  - Taşan M
  - Tejeda A
  - Tropepe V
  - Twizere JC
  - Wang Y
  - Weatheritt RJ
  - Weile J
  - Xia Y
  - Yang X
  - Yeger-Lotem E
  - Zhong Q
  - Aloy P
  - Bader GD
  - De Las Rivas J
  - Gaudet S
  - Hao T
  - Rak J
  - Tavernier J
  - Hill DE
  - Vidal M
  - Roth FP
  - Calderwood MA
  doi: 10.1038/s41586-020-2188-x
  id: PMID:32296183
  journal: Nature
  title: A reference map of the human binary protein interactome
  year: '2020'
repository: https://github.com/VIDallab/huri
synonyms:
- HRPIMP
- HuRI
- Human Reference Interactome
taxon:
- NCBITaxon:9606
- NCBITaxon:4932
---
# Human Reference Protein Interactome Mapping Project

The Human Reference Protein Interactome Mapping Project (HRPIMP) is a landmark systematic effort to comprehensively map binary protein-protein interactions (PPIs) in human cells. Led by the Center for Cancer Systems Biology at Dana-Farber Cancer Institute under principal investigators Marc Vidal and Frederick P. Roth, this project has produced the Human Reference Interactome (HuRI), one of the most comprehensive and high-quality maps of human protein interactions available.

## Key Features

- **Systematic Y2H Screening**: Uses yeast two-hybrid technology for high-throughput detection of binary protein-protein interactions
- **Comprehensive Coverage**: Maps interactions for 9,094 human proteins
- **High-Quality Data**: 64,006 experimentally validated binary protein-protein interactions
- **Open Access**: Data freely available under Creative Commons BY 4.0 license
- **Reference Standard**: Widely used reference resource for systems biology and disease research

## Applications

The HuRI database and HRPIMP data have been integrated into numerous research projects and knowledge bases, including:
- Alzheimer's Disease research (AlzKB)
- Cancer systems biology
- Drug target identification
- Disease mechanism studies
- Pathway analysis
- Network medicine

## Data Products

The project provides downloadable TSV files containing protein-protein interaction data that can be integrated into research pipelines, knowledge graphs, and systems biology analyses.