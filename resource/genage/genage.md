---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: jp@senescence.info
  label: Genomics of Ageing and Rejuvenation Lab
creation_date: '2025-10-30T00:00:00Z'
description: GenAge is a curated database of genes related to ageing and longevity,
  part of the Human Ageing Genomic Resources (HAGR). It includes genes directly related
  to human ageing plus candidate genes from model organisms (yeast, worms, flies,
  mice), manually curated by experts to ensure high-quality content.
domains:
- genomics
- health
homepage_url: http://genomics.senescence.info/genes/
id: genage
infores_id: genage
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
name: GenAge Database of Ageing-Related Genes
products:
- category: Product
  compression: zip
  description: Tab-delimited file containing all human ageing-related genes with extensive
    annotations
  format: tsv
  id: genage.human
  name: GenAge Human Genes Dataset
  original_source:
  - genage
  product_file_size: 9465
  product_url: https://genomics.senescence.info/genes/human_genes.zip
- category: Product
  compression: zip
  description: Tab-delimited file containing genes associated with longevity and ageing
    in model organisms (yeast, worms, flies, mice)
  format: tsv
  id: genage.models
  name: GenAge Model Organisms Dataset
  original_source:
  - genage
  product_file_size: 48796
  product_url: https://genomics.senescence.info/genes/models_genes.zip
- category: GraphicalInterface
  description: Web interface for searching and browsing human ageing-related genes
  format: http
  id: genage.human.search
  name: GenAge Human Genes Search
  original_source:
  - genage
  product_url: https://genomics.senescence.info/genes/human.html
- category: GraphicalInterface
  description: Web interface for searching and browsing model organism ageing genes
  format: http
  id: genage.models.search
  name: GenAge Model Organisms Search
  original_source:
  - genage
  product_url: https://genomics.senescence.info/genes/models.html
publications:
- authors:
  - de Magalhaes JP
  - et al
  doi: 10.1093/nar/gkad927
  id: doi:10.1093/nar/gkad927
  journal: Nucleic Acids Research
  preferred: true
  title: 'Human Ageing Genomic Resources: updates on key databases in ageing research'
  year: '2024'
- authors:
  - de Magalhaes JP
  - Toussaint O
  doi: 10.1016/j.febslet.2004.06.080
  id: doi:10.1016/j.febslet.2004.06.080
  journal: FEBS Letters
  title: 'GenAge: a genomic and proteomic network map of human ageing'
  year: '2004'
- authors:
  - Fernandes M
  - et al
  doi: 10.1093/hmg/ddw307
  id: doi:10.1093/hmg/ddw307
  journal: Human Molecular Genetics
  title: Systematic analysis of the gerontome reveals links between aging and age-related
    diseases
  year: '2016'
synonyms:
- GenAge
- The Aging Gene Database
---
# GenAge Database of Ageing-Related Genes

## Overview

GenAge is the benchmark database of genes related to ageing and longevity, a core component of the Human Ageing Genomic Resources (HAGR) maintained by the Genomics of Ageing and Rejuvenation Lab at the University of Birmingham. The database is divided into two main sections: human ageing-related genes and genes associated with longevity/ageing in model organisms (yeast, worms, flies, mice, and others).

GenAge is manually curated by experts in the field of biogerontology to ensure high-quality, reliable content. The human genes section includes both genes directly related to ageing in humans and the best candidate genes obtained from model organism research, with considerably better annotation and more comprehensive information.

## Data Content

### Human Ageing-Related Genes
The human genes dataset includes:
- **Direct human ageing genes**: Few genes directly proven to affect human ageing
- **Candidate genes**: Best candidate genes from model organism research
- **Extensive annotations**: Detailed descriptions, evidence, and functional information
- **Literature support**: Links to supporting publications and evidence
- **Cross-references**: Connections to other databases and resources

### Model Organism Genes
The model organisms dataset covers:
- **Yeast** (Saccharomyces cerevisiae)
- **Nematodes** (Caenorhabditis elegans)
- **Fruit flies** (Drosophila melanogaster)
- **Mice** (Mus musculus)
- **Other model systems**: Various organisms used in ageing research

### Gene Classifications
Genes are categorized by:
- **Longevity effects**: Impact on lifespan when manipulated
- **Ageing phenotypes**: Effects on age-related changes
- **Evolutionary conservation**: Conservation across species
- **Functional groups**: Biological pathways and processes
- **Evidence quality**: Strength of experimental support

## Key Features

- **Expert curation**: Manual curation by biogerontology experts
- **Comprehensive coverage**: Genes from humans and multiple model organisms
- **Detailed annotations**: Rich functional and experimental information
- **Regular updates**: Ongoing maintenance and new gene additions
- **High quality**: Rigorous standards for inclusion and annotation
- **Web interfaces**: Searchable, browsable online interfaces
- **Downloadable data**: Complete datasets in tab-delimited format
- **Cross-referenced**: Linked to other aging and genomic databases

## Access Methods

1. **Interactive Web Search**: Browse and search genes through web interfaces
2. **Direct Downloads**: Download complete datasets as zipped TSV files
3. **API Access**: (Check website for programmatic access options)
4. **Integration**: Part of broader HAGR ecosystem with complementary databases

## Related HAGR Databases

GenAge is part of a comprehensive suite of aging research databases:
- **AnAge**: Animal longevity and life history database
- **GenDR**: Dietary restriction genes database
- **LongevityMap**: Human genetic variants associated with longevity
- **CellAge**: Cellular senescence genes database
- **DrugAge**: Compounds that modulate longevity
- **Digital Ageing Atlas**: Ageing changes across biological levels

## Use Cases

1. **Ageing Research**: Identify and study genes involved in ageing processes
2. **Longevity Studies**: Investigate genetic factors influencing lifespan
3. **Comparative Biology**: Compare ageing mechanisms across species
4. **Systems Biology**: Analyze networks and pathways in ageing
5. **Translational Research**: Identify targets for anti-ageing interventions
6. **Evolutionary Studies**: Understand evolution of ageing and longevity
7. **Education**: Teaching resource for biogerontology
8. **Drug Discovery**: Identify potential therapeutic targets

## Network Analyses

GenAge has been used for pioneering systems biology analyses:
- **Protein network of human ageing**: First comprehensive network analysis (2004)
- **System-level interpretation**: Holistic view of ageing processes
- **Machine learning applications**: Predictive modeling of ageing genes
- **Evolutionary analyses**: Cross-species comparisons
- **Disease connections**: Links between ageing and age-related diseases

## Recognition

GenAge has been highlighted in major scientific publications:
- **Nature Reviews Genetics** (5:1362) - Web Watch feature
- **Science** (307:187) - NetWatch feature
- **BioTechniques** (39:21) - WebWatch feature
- Cited in hundreds of scientific publications
- Core resource for biogerontology community

## Management

Maintained by the Genomics of Ageing and Rejuvenation Lab, led by Dr. João Pedro de Magalhães at the University of Birmingham. The lab is supported by the Wellcome Trust and BBSRC (Biotechnology and Biological Sciences Research Council).

## Data Quality

- **Manual curation**: Expert review of all entries
- **Evidence-based**: All genes supported by experimental evidence
- **Regular updates**: Ongoing incorporation of new findings
- **Quality control**: Rigorous standards for inclusion
- **Peer-reviewed**: Associated publications in top journals

## License and Usage

GenAge may be freely used for all purposes under HAGR's terms and conditions. Users are asked to cite the appropriate publications when using the database in research.

## Community

- **HAGR-news mailing list**: Notifications of new releases and updates
- **Feedback mechanism**: User submissions for new genes or corrections
- **Publications database**: Tracking of GenAge citations and applications
- **Educational resources**: Documentation and help materials

## Related Resources

- [AnAge](anage): Animal species longevity database (if available in registry)
- [CellAge](cellage): Cellular senescence database (if available)
- [DrugAge](drugage): Longevity-modulating compounds (if available)

## Last Update

Database build: 2024 (check website for specific build number and date)
Latest HAGR description: de Magalhães et al. (2024) Nucleic Acids Research