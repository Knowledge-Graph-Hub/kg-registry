---
layout: schema_doc
mermaid: true
---

# Enum: DomainEnum




_A domain that a resource is relevant to. Each domain maps, where possible, to a concept in an external controlled vocabulary (Medical Subject Headings, MeSH; the NCI Thesaurus, NCIT; or EDAM) via the permissible value's `meaning`. Domains form a two-level hierarchy. A specific domain names its broader domain with `is_a`, and a resource that lists a specific domain also lists the broader one._



URI: [kgr:DomainEnum](https://w3id.org/bridge2ai/data-sheets-schema/DomainEnum)

## Permissible Values

| Value | Meaning | Is A | Description |
| --- | --- | --- | --- |
| adverse outcome pathways | MESH:D000073931 | toxicology | Adverse outcome pathways linking molecular initiating events to adverse outco... |
| aging | MESH:D000375 | biological systems | Aging and longevity, including cellular senescence |
| agriculture | MESH:D000383 |  | The agricultural and food sciences, including crop and animal production, pla... |
| air pollution | MESH:D000397 | environment | Air quality and emissions to air |
| anatomy and development | MESH:D000715 |  | The anatomy and development of organisms, including their structure, morpholo... |
| biodiversity | MESH:D044822 | organisms | The variety of life, including species occurrence, conservation status, and i... |
| biological systems | MESH:D001690 |  | The biological sciences broadly, including cellular and molecular biology and... |
| biomedical | MESH:D035843 |  | The biomedical sciences broadly, spanning the study of biological systems in ... |
| cancer | MESH:D009369 | biomedical | Cancer and other neoplasms, including tumor genomics, cancer cell lines, onco... |
| cardiovascular disease | MESH:D002318 | biomedical | Diseases of the heart and blood vessels, including hypertension |
| cell biology | MESH:D003585 | biological systems | Cells and cell types, including cell lines, cell markers, and subcellular str... |
| cheminformatics | MESH:D000080911 | chemistry and biochemistry | Computational representation, identification, and classification of chemical ... |
| chemistry and biochemistry | MESH:D002621 |  | The chemical and biochemical sciences, including the structure, properties, a... |
| climate | MESH:D002980 | environment | Climate and climate change, including climate models and drought |
| clinical | MESH:D015510 |  | The clinical sciences concerned with the care of patients, including clinical... |
| clinical coding | MESH:D059019 | clinical | Clinical terminologies and code sets for diagnoses, procedures, observations,... |
| clinical trials | MESH:D002986 | clinical | Clinical trials, including trial registries and the data standards used to re... |
| criminal justice | MESH:D003416 | public health | Crime, courts, and the justice system, including crime reporting and court re... |
| diabetes mellitus | MESH:D003920 | biomedical | Diabetes mellitus, including type 1 and type 2 diabetes and the pancreatic is... |
| disasters | MESH:D004190 | public health | Disasters and emergencies, including disaster declarations, humanitarian resp... |
| disease registries | MESH:D012042 | public health | Population-based registries of disease cases, such as cancer registries |
| domestic animals | MESH:D000829 | organisms | Domestic animals, including companion animals and livestock breeds |
| drug discovery | MESH:D055808 |  | The process of identifying and developing new candidate medications, includin... |
| drug interactions | MESH:D004347 | pharmacology | Interactions between drugs and between drugs and foods or natural products |
| drug repositioning | MESH:D058492 | drug discovery | The discovery of new indications for existing drugs, including computational ... |
| ecology | MESH:D004463 | environment | The interactions of organisms with each other and their environment, includin... |
| electronic health records | MESH:D057286 | clinical | Electronic health records and observational health data derived from them |
| environment | MESH:D004777 |  | The environment and ecosystems, including ecology and environmental health |
| environmental exposure | MESH:D004781 | environment | Exposure of people and organisms to environmental agents and the health effec... |
| enzymes | MESH:D004798 | chemistry and biochemistry | Enzymes, including their classification, reactions, and catalytic mechanisms |
| epidemiology | MESH:D004813 | public health | The distribution and determinants of disease in populations, including diseas... |
| epigenomics | MESH:D057890 | genomics | Genome-wide chromatin state and organization, including chromatin conformatio... |
| food | MESH:D005502 | nutrition | Foods, their composition, and their relationship to diet and health |
| gene expression profiling | MESH:D020869 | genomics | Measurement of gene expression across tissues, cells, and conditions, includi... |
| gene regulation | MESH:D005786 | genomics | The regulation of gene expression, including transcription factors, their bin... |
| general | None |  | A general domain, not specific to any other category. It concerns resources t... |
| genetic variation | MESH:D014644 | genomics | Germline and somatic genetic variants, including their frequencies, effects, ... |
| genome-wide association studies | MESH:D055106 | genomics | Genome-wide association studies and related statistical genetics, including Q... |
| genomics | MESH:D023281 |  | The study of genomes, including genome structure, evolution, function, mappin... |
| geographic information systems | MESH:D040362 | environment | Geospatial data, including place names, administrative boundaries, and infras... |
| glycomics | MESH:D054794 | chemistry and biochemistry | The study of glycans and glycoconjugates |
| high-throughput screening | MESH:D057166 | drug discovery | Large-scale screening of chemical or genetic perturbations, including cell li... |
| host-pathogen interactions | MESH:D054884 | microbiology | Interactions between pathogens and their hosts, including pathogen genomics a... |
| human populations | MESH:D044382 | organisms | Human population groups, including ancestry, ethnicity, and demographic groups |
| humanities and cultural heritage | MESH:D006809 |  | The humanities and the cultural heritage domain, including art history, archi... |
| immunology | MESH:D000486 |  | The study of the immune system, including its structure and function, disorde... |
| infectious disease | MESH:D003141 | biomedical | Infectious diseases, including their pathogens, transmission, epidemiology, d... |
| information technology | MESH:D000073256 |  | The information technology and informatics sciences, including software, comp... |
| insects | MESH:D007313 | organisms | Insects, including their anatomy, behavior, and genomics |
| literature | MESH:D011642 |  | The literature and publications of a domain |
| machine learning | MESH:D000069550 | information technology | Machine learning and artificial intelligence, including AI-ready data and mod... |
| medical imaging | MESH:D003952 |  | Techniques and processes for creating visual representations of the interior ... |
| mental disorders | MESH:D001523 | neuroscience | Mental and psychiatric disorders, including substance use disorders |
| metabolism | MESH:D008660 | pathways | Metabolic pathways and genome-scale metabolic network reconstructions |
| metabolomics | MESH:D055432 | chemistry and biochemistry | The large-scale study of metabolites and lipids, including mass spectrometry ... |
| metadata | MESH:D000071253 | information technology | Metadata vocabularies and standards for describing resources, datasets, and p... |
| microbiology | MESH:D008829 |  | The microbiological sciences, including the study of microbial communities (m... |
| microbiome | MESH:D064307 | microbiology | Microbial communities, including host-associated microbiomes and metagenomes |
| model organisms | edam:topic_0621 | organisms | Model organisms and the databases that serve their research communities |
| molecular evolution | MESH:D019143 | genomics | The evolution of genes and proteins, including orthology, gene families, and ... |
| natural language processing | MESH:D009323 | literature | Text mining and natural language processing of the literature, including text... |
| natural products | NCIT:C1907 | chemistry and biochemistry | Compounds derived from plants, microorganisms, or animals, including traditio... |
| neurodegenerative disease | MESH:D019636 | neuroscience | Neurodegenerative diseases, including Alzheimer disease and related dementias |
| neuroscience | MESH:D009488 |  | The scientific study of the nervous system, including brain structure, functi... |
| non-coding RNA | MESH:D022661 | genomics | RNAs that are not translated into protein, including microRNAs, long non-codi... |
| nutrition | MESH:D052756 |  | The nutritional sciences, including diet and metabolomics |
| organisms | NCIT:C14250 |  | Specific organisms or taxa |
| other | None |  | Another domain not defined here |
| pathways | MESH:D053858 |  | Biological pathways, including metabolic, signaling, and regulatory networks ... |
| pharmacogenomics | MESH:D010597 | pharmacology | The influence of genetic variation on drug response |
| pharmacology | MESH:D010600 |  | The study of how drugs interact with biological systems, including drug disco... |
| pharmacovigilance | MESH:D060735 | pharmacology | The monitoring of drug and device safety, including adverse event reports and... |
| phenotype | MESH:D010641 |  | The phenotypes of organisms |
| plants | MESH:D010944 | organisms | Plants, including crops and their anatomy, traits, and genomics |
| population genetics | MESH:D005828 | genomics | Genetic variation within and between populations, including human ancestry |
| post-translational modification | MESH:D011499 | proteomics | Post-translational modifications of proteins, such as phosphorylation |
| precision medicine | MESH:D057285 |  | An approach to disease treatment and prevention that takes into account indiv... |
| protein domains | MESH:D000072417 | proteomics | Protein families, domains, and functional sites |
| protein interactions | MESH:D060066 | proteomics | Physical interactions between proteins, including protein complexes |
| protein structure | MESH:D011487 | proteomics | The three-dimensional structure of proteins, whether determined experimentall... |
| proteomics | MESH:D040901 |  | The large-scale study of proteins, their structures, functions, and interacti... |
| public health | MESH:D011634 |  | The science of protecting and improving the health of people and their commun... |
| rare disease | MESH:D035583 | biomedical | Rare diseases, including rare Mendelian and other genetic disorders, their ph... |
| research funding | NCIT:C17090 |  | The funding and administration of research, including research projects, gran... |
| scholarly communication | MESH:D000073820 | literature | Scholarly publications and their metadata, including citations, authors, and ... |
| signal transduction | MESH:D015398 | pathways | Signaling pathways and networks that transmit signals within and between cells |
| single-cell analysis | MESH:D059010 | biological systems | Data and methods that measure molecules in individual cells, including single... |
| social determinants of health | MESH:D064890 | public health | The social and economic conditions that shape health, including housing, inco... |
| software | MESH:D012984 | information technology | Software, including package registries, software supply chains, and vulnerabi... |
| sustainability | MESH:D000076502 | environment | Sustainability and environmental, social, and governance (ESG) reporting |
| systems biology | MESH:D049490 |  | The computational and mathematical analysis of complex biological systems and... |
| taxonomy | NCIT:C17469 | organisms | The naming and classification of organisms and the relationships among taxa |
| toxicology | MESH:D014116 |  | The study of the adverse effects of chemicals on living organisms |
| transportation | MESH:D014186 |  | Transportation and transport infrastructure, including railway, road, air, an... |
| vaccines | MESH:D014612 | immunology | Vaccines and vaccination, including vaccine adverse events |
| water resources | MESH:D062066 | environment | Surface water, groundwater, drinking water, and hydrology |
| wildfires | MESH:D000075923 | environment | Wildfires and their burn severity and smoke |
| stub | None |  | This is not a domain, but rather a category for resources that are not yet ca... |




## Slots

| Name | Description |
| ---  | --- |
| [domains](domains.html) | The domain(s) that the resource is relevant to |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: DomainEnum
description: A domain that a resource is relevant to. Each domain maps, where
  possible, to a concept in an external controlled vocabulary (Medical Subject
  Headings, MeSH; the NCI Thesaurus, NCIT; or EDAM) via the permissible value's
  `meaning`. Domains form a two-level hierarchy. A specific domain names its broader
  domain with `is_a`, and a resource that lists a specific domain also lists the
  broader one.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
permissible_values:
  adverse outcome pathways:
    text: adverse outcome pathways
    description: Adverse outcome pathways linking molecular initiating events
      to adverse outcomes.
    meaning: MESH:D000073931
    is_a: toxicology
  aging:
    text: aging
    description: Aging and longevity, including cellular senescence.
    meaning: MESH:D000375
    is_a: biological systems
  agriculture:
    text: agriculture
    description: The agricultural and food sciences, including crop and animal
      production, plant science, and food production, processing, and preservation.
    meaning: MESH:D000383
  air pollution:
    text: air pollution
    description: Air quality and emissions to air.
    meaning: MESH:D000397
    is_a: environment
  anatomy and development:
    text: anatomy and development
    description: The anatomy and development of organisms, including their structure,
      morphology, and developmental biology.
    meaning: MESH:D000715
  biodiversity:
    text: biodiversity
    description: The variety of life, including species occurrence, conservation
      status, and invasive species.
    meaning: MESH:D044822
    is_a: organisms
  biological systems:
    text: biological systems
    description: The biological sciences broadly, including cellular and molecular
      biology and other biological disciplines not better described by a more
      specific domain.
    meaning: MESH:D001690
  biomedical:
    text: biomedical
    description: The biomedical sciences broadly, spanning the study of biological
      systems in the context of health and disease. Use a more specific domain
      (e.g., clinical) where one applies.
    meaning: MESH:D035843
  cancer:
    text: cancer
    description: Cancer and other neoplasms, including tumor genomics, cancer
      cell lines, oncology treatment, and cancer registries.
    meaning: MESH:D009369
    is_a: biomedical
  cardiovascular disease:
    text: cardiovascular disease
    description: Diseases of the heart and blood vessels, including hypertension.
    meaning: MESH:D002318
    is_a: biomedical
  cell biology:
    text: cell biology
    description: Cells and cell types, including cell lines, cell markers, and
      subcellular structures.
    meaning: MESH:D003585
    is_a: biological systems
  cheminformatics:
    text: cheminformatics
    description: Computational representation, identification, and classification
      of chemical structures.
    meaning: MESH:D000080911
    is_a: chemistry and biochemistry
  chemistry and biochemistry:
    text: chemistry and biochemistry
    description: The chemical and biochemical sciences, including the structure,
      properties, and reactions of chemical compounds.
    meaning: MESH:D002621
  climate:
    text: climate
    description: Climate and climate change, including climate models and drought.
    meaning: MESH:D002980
    is_a: environment
  clinical:
    text: clinical
    description: The clinical sciences concerned with the care of patients, including
      clinical trials, patient data, and diagnosis and treatment of disease.
    meaning: MESH:D015510
  clinical coding:
    text: clinical coding
    description: Clinical terminologies and code sets for diagnoses, procedures,
      observations, and medications.
    meaning: MESH:D059019
    is_a: clinical
  clinical trials:
    text: clinical trials
    description: Clinical trials, including trial registries and the data standards
      used to report them.
    meaning: MESH:D002986
    is_a: clinical
  criminal justice:
    text: criminal justice
    description: Crime, courts, and the justice system, including crime reporting
      and court records.
    meaning: MESH:D003416
    is_a: public health
  diabetes mellitus:
    text: diabetes mellitus
    description: Diabetes mellitus, including type 1 and type 2 diabetes and the
      pancreatic islet biology that underlies them.
    meaning: MESH:D003920
    is_a: biomedical
  disasters:
    text: disasters
    description: Disasters and emergencies, including disaster declarations, humanitarian
      response, and critical infrastructure.
    meaning: MESH:D004190
    is_a: public health
  disease registries:
    text: disease registries
    description: Population-based registries of disease cases, such as cancer
      registries.
    meaning: MESH:D012042
    is_a: public health
  domestic animals:
    text: domestic animals
    description: Domestic animals, including companion animals and livestock breeds.
    meaning: MESH:D000829
    is_a: organisms
  drug discovery:
    text: drug discovery
    description: The process of identifying and developing new candidate medications,
      including target identification, validation, and compound screening.
    meaning: MESH:D055808
  drug interactions:
    text: drug interactions
    description: Interactions between drugs and between drugs and foods or natural
      products.
    meaning: MESH:D004347
    is_a: pharmacology
  drug repositioning:
    text: drug repositioning
    description: The discovery of new indications for existing drugs, including
      computational repurposing methods and their benchmarks.
    meaning: MESH:D058492
    is_a: drug discovery
  ecology:
    text: ecology
    description: The interactions of organisms with each other and their environment,
      including ecological networks.
    meaning: MESH:D004463
    is_a: environment
  electronic health records:
    text: electronic health records
    description: Electronic health records and observational health data derived
      from them.
    meaning: MESH:D057286
    is_a: clinical
  environment:
    text: environment
    description: The environment and ecosystems, including ecology and environmental
      health.
    meaning: MESH:D004777
  environmental exposure:
    text: environmental exposure
    description: Exposure of people and organisms to environmental agents and
      the health effects of those exposures.
    meaning: MESH:D004781
    is_a: environment
  enzymes:
    text: enzymes
    description: Enzymes, including their classification, reactions, and catalytic
      mechanisms.
    meaning: MESH:D004798
    is_a: chemistry and biochemistry
  epidemiology:
    text: epidemiology
    description: The distribution and determinants of disease in populations,
      including disease surveillance and outbreaks.
    meaning: MESH:D004813
    is_a: public health
  epigenomics:
    text: epigenomics
    description: Genome-wide chromatin state and organization, including chromatin
      conformation and regulatory element annotation.
    meaning: MESH:D057890
    is_a: genomics
  food:
    text: food
    description: Foods, their composition, and their relationship to diet and
      health.
    meaning: MESH:D005502
    is_a: nutrition
  gene expression profiling:
    text: gene expression profiling
    description: Measurement of gene expression across tissues, cells, and conditions,
      including transcriptomic signatures.
    meaning: MESH:D020869
    is_a: genomics
  gene regulation:
    text: gene regulation
    description: The regulation of gene expression, including transcription factors,
      their binding sites, promoters, and enhancers.
    meaning: MESH:D005786
    is_a: genomics
  general:
    text: general
    description: A general domain, not specific to any other category. It concerns
      resources that are broadly applicable across multiple domains, including
      upper-level and cross-domain resources.
  genetic variation:
    text: genetic variation
    description: Germline and somatic genetic variants, including their frequencies,
      effects, and clinical interpretation.
    meaning: MESH:D014644
    is_a: genomics
  genome-wide association studies:
    text: genome-wide association studies
    description: Genome-wide association studies and related statistical genetics,
      including QTL and Mendelian randomization analyses.
    meaning: MESH:D055106
    is_a: genomics
  genomics:
    text: genomics
    description: The study of genomes, including genome structure, evolution,
      function, mapping, and editing.
    meaning: MESH:D023281
  geographic information systems:
    text: geographic information systems
    description: Geospatial data, including place names, administrative boundaries,
      and infrastructure maps.
    meaning: MESH:D040362
    is_a: environment
  glycomics:
    text: glycomics
    description: The study of glycans and glycoconjugates.
    meaning: MESH:D054794
    is_a: chemistry and biochemistry
  high-throughput screening:
    text: high-throughput screening
    description: Large-scale screening of chemical or genetic perturbations, including
      cell line sensitivity and perturbation profiling.
    meaning: MESH:D057166
    is_a: drug discovery
  host-pathogen interactions:
    text: host-pathogen interactions
    description: Interactions between pathogens and their hosts, including pathogen
      genomics and virulence.
    meaning: MESH:D054884
    is_a: microbiology
  human populations:
    text: human populations
    description: Human population groups, including ancestry, ethnicity, and demographic
      groups.
    meaning: MESH:D044382
    is_a: organisms
  humanities and cultural heritage:
    text: humanities and cultural heritage
    description: The humanities and the cultural heritage domain, including art
      history, architecture, musicology, media and performing arts, archaeology,
      and history, along with the collections, archives, and museum holdings that
      document them.
    meaning: MESH:D006809
  immunology:
    text: immunology
    description: The study of the immune system, including its structure and function,
      disorders, and therapeutic applications.
    meaning: MESH:D000486
  infectious disease:
    text: infectious disease
    description: Infectious diseases, including their pathogens, transmission,
      epidemiology, diagnosis, and treatment.
    meaning: MESH:D003141
    is_a: biomedical
  information technology:
    text: information technology
    description: The information technology and informatics sciences, including
      software, computational methods, simulation and modeling, and digital health
      technologies.
    meaning: MESH:D000073256
  insects:
    text: insects
    description: Insects, including their anatomy, behavior, and genomics.
    meaning: MESH:D007313
    is_a: organisms
  literature:
    text: literature
    description: The literature and publications of a domain.
    meaning: MESH:D011642
  machine learning:
    text: machine learning
    description: Machine learning and artificial intelligence, including AI-ready
      data and models.
    meaning: MESH:D000069550
    is_a: information technology
  medical imaging:
    text: medical imaging
    description: Techniques and processes for creating visual representations
      of the interior of a body for clinical analysis and medical intervention.
    meaning: MESH:D003952
  mental disorders:
    text: mental disorders
    description: Mental and psychiatric disorders, including substance use disorders.
    meaning: MESH:D001523
    is_a: neuroscience
  metabolism:
    text: metabolism
    description: Metabolic pathways and genome-scale metabolic network reconstructions.
    meaning: MESH:D008660
    is_a: pathways
  metabolomics:
    text: metabolomics
    description: The large-scale study of metabolites and lipids, including mass
      spectrometry and NMR data.
    meaning: MESH:D055432
    is_a: chemistry and biochemistry
  metadata:
    text: metadata
    description: Metadata vocabularies and standards for describing resources,
      datasets, and provenance.
    meaning: MESH:D000071253
    is_a: information technology
  microbiology:
    text: microbiology
    description: The microbiological sciences, including the study of microbial
      communities (microbiomes) and their influence on hosts and environments.
    meaning: MESH:D008829
  microbiome:
    text: microbiome
    description: Microbial communities, including host-associated microbiomes
      and metagenomes.
    meaning: MESH:D064307
    is_a: microbiology
  model organisms:
    text: model organisms
    description: Model organisms and the databases that serve their research communities.
    meaning: edam:topic_0621
    is_a: organisms
  molecular evolution:
    text: molecular evolution
    description: The evolution of genes and proteins, including orthology, gene
      families, and comparative analysis.
    meaning: MESH:D019143
    is_a: genomics
  natural language processing:
    text: natural language processing
    description: Text mining and natural language processing of the literature,
      including text-mined knowledge graphs and annotated corpora.
    meaning: MESH:D009323
    is_a: literature
  natural products:
    text: natural products
    description: Compounds derived from plants, microorganisms, or animals, including
      traditional medicines.
    meaning: NCIT:C1907
    is_a: chemistry and biochemistry
  neurodegenerative disease:
    text: neurodegenerative disease
    description: Neurodegenerative diseases, including Alzheimer disease and related
      dementias.
    meaning: MESH:D019636
    is_a: neuroscience
  neuroscience:
    text: neuroscience
    description: The scientific study of the nervous system, including brain structure,
      function, and disorders.
    meaning: MESH:D009488
  non-coding RNA:
    text: non-coding RNA
    description: RNAs that are not translated into protein, including microRNAs,
      long non-coding RNAs, and ribosomal and transfer RNAs.
    meaning: MESH:D022661
    is_a: genomics
  nutrition:
    text: nutrition
    description: The nutritional sciences, including diet and metabolomics.
    meaning: MESH:D052756
  organisms:
    text: organisms
    description: Specific organisms or taxa.
    meaning: NCIT:C14250
  other:
    text: other
    description: Another domain not defined here.
  pathways:
    text: pathways
    description: Biological pathways, including metabolic, signaling, and regulatory
      networks that control cellular processes.
    meaning: MESH:D053858
  pharmacogenomics:
    text: pharmacogenomics
    description: The influence of genetic variation on drug response.
    meaning: MESH:D010597
    is_a: pharmacology
  pharmacology:
    text: pharmacology
    description: The study of how drugs interact with biological systems, including
      drug discovery, development, and therapeutic uses.
    meaning: MESH:D010600
  pharmacovigilance:
    text: pharmacovigilance
    description: The monitoring of drug and device safety, including adverse event
      reports and side effects.
    meaning: MESH:D060735
    is_a: pharmacology
  phenotype:
    text: phenotype
    description: The phenotypes of organisms.
    meaning: MESH:D010641
  plants:
    text: plants
    description: Plants, including crops and their anatomy, traits, and genomics.
    meaning: MESH:D010944
    is_a: organisms
  population genetics:
    text: population genetics
    description: Genetic variation within and between populations, including human
      ancestry.
    meaning: MESH:D005828
    is_a: genomics
  post-translational modification:
    text: post-translational modification
    description: Post-translational modifications of proteins, such as phosphorylation.
    meaning: MESH:D011499
    is_a: proteomics
  precision medicine:
    text: precision medicine
    description: An approach to disease treatment and prevention that takes into
      account individual variability in genes, environment, and lifestyle.
    meaning: MESH:D057285
  protein domains:
    text: protein domains
    description: Protein families, domains, and functional sites.
    meaning: MESH:D000072417
    is_a: proteomics
  protein interactions:
    text: protein interactions
    description: Physical interactions between proteins, including protein complexes.
    meaning: MESH:D060066
    is_a: proteomics
  protein structure:
    text: protein structure
    description: The three-dimensional structure of proteins, whether determined
      experimentally or predicted.
    meaning: MESH:D011487
    is_a: proteomics
  proteomics:
    text: proteomics
    description: The large-scale study of proteins, their structures, functions,
      and interactions.
    meaning: MESH:D040901
  public health:
    text: public health
    description: The science of protecting and improving the health of people
      and their communities, including epidemiology, population health, and the
      social determinants of health.
    meaning: MESH:D011634
  rare disease:
    text: rare disease
    description: Rare diseases, including rare Mendelian and other genetic disorders,
      their phenotypes, genes, and treatments.
    meaning: MESH:D035583
    is_a: biomedical
  research funding:
    text: research funding
    description: The funding and administration of research, including research
      projects, grants and their payments, funding programmes, the organizations
      that fund or carry out research, and the outputs attributed to that funding.
    meaning: NCIT:C17090
  scholarly communication:
    text: scholarly communication
    description: Scholarly publications and their metadata, including citations,
      authors, and research contributions.
    meaning: MESH:D000073820
    is_a: literature
  signal transduction:
    text: signal transduction
    description: Signaling pathways and networks that transmit signals within
      and between cells.
    meaning: MESH:D015398
    is_a: pathways
  single-cell analysis:
    text: single-cell analysis
    description: Data and methods that measure molecules in individual cells,
      including single-cell and spatial atlases.
    meaning: MESH:D059010
    is_a: biological systems
  social determinants of health:
    text: social determinants of health
    description: The social and economic conditions that shape health, including
      housing, income, services, and rurality.
    meaning: MESH:D064890
    is_a: public health
  software:
    text: software
    description: Software, including package registries, software supply chains,
      and vulnerabilities.
    meaning: MESH:D012984
    is_a: information technology
  sustainability:
    text: sustainability
    description: Sustainability and environmental, social, and governance (ESG)
      reporting.
    meaning: MESH:D000076502
    is_a: environment
  systems biology:
    text: systems biology
    description: The computational and mathematical analysis of complex biological
      systems and their interactions.
    meaning: MESH:D049490
  taxonomy:
    text: taxonomy
    description: The naming and classification of organisms and the relationships
      among taxa.
    meaning: NCIT:C17469
    is_a: organisms
  toxicology:
    text: toxicology
    description: The study of the adverse effects of chemicals on living organisms.
    meaning: MESH:D014116
  transportation:
    text: transportation
    description: Transportation and transport infrastructure, including railway,
      road, air, and maritime networks, the assets and parameters that describe
      them, and the movement of people and goods over them.
    meaning: MESH:D014186
  vaccines:
    text: vaccines
    description: Vaccines and vaccination, including vaccine adverse events.
    meaning: MESH:D014612
    is_a: immunology
  water resources:
    text: water resources
    description: Surface water, groundwater, drinking water, and hydrology.
    meaning: MESH:D062066
    is_a: environment
  wildfires:
    text: wildfires
    description: Wildfires and their burn severity and smoke.
    meaning: MESH:D000075923
    is_a: environment
  stub:
    text: stub
    description: This is not a domain, but rather a category for resources that
      are not yet categorized and exist only as a placeholder.

```
</details>
