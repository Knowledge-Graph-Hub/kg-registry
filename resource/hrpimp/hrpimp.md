---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: The Human Reference Protein Interactome Mapping Project (HRPIMP) is a
  systematic effort to map binary protein-protein interactions in human cells. The
  project produced the Human Reference Interactome (HuRI) database containing high-quality
  experimentally validated protein-protein interactions. Using systematic yeast two-hybrid
  (Y2H) screening approaches, HRPIMP produced proteome-scale human PPI datasets including
  HuRI, HI-union, and earlier CCSB interactome screens. The current HuRI portal provides
  the HuRI dataset with 52,569 interactions in TSV and PSI-MI formats, mapped to Ensembl
  identifiers for GENCODE protein-coding genes.
domains:
- proteomics
- systems biology
- biomedical
- biological systems
homepage_url: https://www.interactome-atlas.org/
id: hrpimp
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Human Reference Protein Interactome Mapping Project
products:
- category: Product
  description: Current HuRI TSV file containing 52,569 systematically mapped binary
    human protein-protein interactions, provided as interacting Ensembl gene ID pairs
  format: tsv
  id: hrpimp.data
  latest_version: HuRI
  name: HuRI Protein-Protein Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 1681536
  product_url: https://www.interactome-atlas.org/data/HuRI.tsv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: hgnc
- category: Product
  description: Current HuRI PSI-MI formatted interaction file with detailed experimental
    information and isoform-specific ORF, transcript, and protein identifiers
  format: psi_mi_mitab
  id: hrpimp.huri.psi
  latest_version: HuRI
  name: HuRI PSI-MI Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 169848924
  product_url: https://www.interactome-atlas.org/data/HuRI.psi
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
- category: GraphicalInterface
  description: Web interface for browsing and exploring the Human Reference Interactome
  format: http
  id: hrpimp.web
  name: Interactome Atlas Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_url: https://www.interactome-atlas.org/
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
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
  - "Cot\xE9 AG"
  - Daley M
  - Deimling S
  - Desbuleux A
  - Dricot A
  - Gebbia M
  - Hardy MF
  - Kishore N
  - Knapp JJ
  - "Kov\xE1cs IA"
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
  - "Ta\u015Fan M"
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
  id: doi:10.1038/s41586-020-2188-x
  journal: Nature
  preferred: true
  title: A reference map of the human binary protein interactome
  year: '2020'
repository: https://github.com/CCSB-DFCI/HuRI_paper
synonyms:
- HRPIMP
- HuRI
- Human Reference Interactome
taxon:
- NCBITaxon:9606
---
# Human Reference Protein Interactome Mapping Project

The Human Reference Protein Interactome Mapping Project (HRPIMP) is a landmark systematic effort to comprehensively map binary protein-protein interactions (PPIs) in human cells. Led by the Center for Cancer Systems Biology at Dana-Farber Cancer Institute under principal investigators Marc Vidal and Frederick P. Roth, this project has produced the Human Reference Interactome (HuRI), one of the most comprehensive and high-quality maps of human protein interactions available. The current portal provides HuRI and related CCSB interactome datasets as simple TSV files and PSI-MI files.

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