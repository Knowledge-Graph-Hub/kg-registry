---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mousephenotype.org/
  label: International Mouse Phenotyping Consortium
creation_date: '2026-05-20T00:00:00Z'
description: The International Mouse Phenotyping Consortium (IMPC) is a global functional
  genomics program that generates and phenotypes knockout mouse lines at scale to
  identify the functions of protein-coding genes and connect mouse phenotypes to human
  biology and disease.
domains:
- genomics
- biomedical
- phenotype
homepage_url: https://www.mousephenotype.org/
id: impc
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: International Mouse Phenotyping Consortium
products:
- category: GraphicalInterface
  description: Official IMPC portal for searching genes, alleles, phenotypes, disease
    associations, and phenotyping results.
  format: http
  id: impc.portal
  name: IMPC Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  product_url: https://www.mousephenotype.org/
- category: GraphProduct
  description: IMPC allele to mouse gene edges
  format: csv
  id: prokn.impc.impcallele.impc_ensembl_id.impcmousegene.edges
  name: ProKN IMPC Allele to Mouse Gene Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 30886543
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcAllele.IMPC_ENSEMBL_ID.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with human gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impchumangene.edges
  name: ProKN IMPC Human-Human Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1268784667
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Human-Mouse Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 8283231
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene orthologous to mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.orthologous_to.impcmousegene.edges
  name: ProKN IMPC Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 16772307
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: PIR IMPC human gene orthologous to protein edges
  format: csv
  id: prokn.pir.impchumangene.orthologous_to.protein.edges
  name: ProKN PIR Human Gene to Protein Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18025933
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.Protein.edges.csv
- category: GraphProduct
  description: PIR IMPC mouse gene has gene product protein edges
  format: csv
  id: prokn.pir.impcmousegene.has_gene_product.protein.edges
  name: ProKN PIR Mouse Gene Product Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 19465205
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcMouseGene.BIOLINK_HAS_GENE_PRODUCT.Protein.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with human gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impchumangene.edges
  name: ProKN IMPC Mouse-Human Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 26416649
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Mouse-Mouse Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 354264338
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene orthologous to human gene edges
  format: csv
  id: prokn.impc.impcmousegene.orthologous_to.impchumangene.edges
  name: ProKN IMPC Mouse-Human Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 5761243
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_HUMAN_GENE_ORTHOLOGUES.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele ID edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_allele_id.impcallele.edges
  name: ProKN IMPC Mouse Allele ID Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 2428378
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELE_ID.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele membership edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_alleles.impcallele.edges
  name: ProKN IMPC Mouse Alleles Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 29340516
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELES.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC publication allele edges
  format: csv
  id: prokn.impc.imppublication.impc_alleles.impcallele.edges
  name: ProKN IMPC Publication Allele Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4211083
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcPublication.IMPC_ALLELES.ImpcAllele.edges.csv
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
publications:
- authors:
  - Groza T
  - Gomez FL
  - Mashhadi HH
  - Muñoz-Fuentes V
  - Gunes O
  - Wilson R
  - Cacheiro P
  - Frost A
  - Keskivali-Bond P
  - Vardal B
  - McCoy A
  - Cheng TK
  - Santos L
  - Wells S
  - Smedley D
  - Mallon AM
  - Parkinson H
  doi: 10.1093/nar/gkac972
  id: https://www.ncbi.nlm.nih.gov/pubmed/36305825
  journal: Nucleic Acids Res
  preferred: true
  title: 'The International Mouse Phenotyping Consortium: comprehensive knockout phenotyping
    underpinning the study of human disease'
  year: '2023'
taxon:
- NCBITaxon:10090
- NCBITaxon:9606
---
# International Mouse Phenotyping Consortium

IMPC coordinates large-scale generation and phenotyping of knockout mouse lines across
multiple international centers. Its portal provides standardized genotype, allele,
phenotype, viability, imaging, and orthology data that support functional characterization
of mouse genes and translation of those findings to human disease biology.

The ProKN products on this page represent downstream graph extractions built from IMPC
allele, orthology, and phenotype-oriented integration outputs. They preserve IMPC as a
primary provenance source while exposing derived graph structures for computational use.