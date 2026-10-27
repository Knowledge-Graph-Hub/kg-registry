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
- organisms
- model organisms
homepage_url: https://www.mousephenotype.org/
id: impc
last_modified_date: '2026-09-23T00:00:00Z'
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
    source: gene-expression-omnibus
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
    source: gene-expression-omnibus
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
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  format: http
  id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: digcfdekg
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: sparc
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hubmap
- category: Product
  description: Downloadable Enrichr gene set libraries (more than 200 libraries across
    transcription, pathways, ontologies, diseases/drugs, cell types, crowd-contributed,
    and legacy categories), each retrievable as a GMT-style tab-delimited text file
    via the geneSetLibrary endpoint (e.g. geneSetLibrary?mode=text&libraryName=KEGG_2021_Human).
    Libraries are compiled from external databases including GO, KEGG, Reactome, WikiPathways,
    MSigDB, ChEA/ENCODE, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, OMIM, GWAS Catalog,
    HPO, MGI, CellMarker, and others.
  format: txt
  id: enrichr.libraries
  name: Enrichr Gene Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://maayanlab.cloud/Enrichr/#libraries
- category: GraphicalInterface
  description: OxO2 web interface for searching and browsing ontology cross-references
    and SSSOM mappings, including asserted mappings from OLS ontologies and curated
    mapping sets, plus inferred cross-set mappings
  format: http
  id: oxo.portal
  name: OxO Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/spot/oxo/api/v2
  description: OxO2 REST API (OpenAPI 3) for querying mappings, mapping sets, and
    ontologies; supports SSSOM-shaped JSON and SSSOM TSV export of mapping search
    results. Also exposes legacy OxO v1-compatible endpoints.
  format: http
  id: oxo.api
  is_public: true
  name: OxO2 REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: biomappings
  - relation_type: prov:hadPrimarySource
    source: semra
  product_url: https://www.ebi.ac.uk/spot/oxo/swagger-ui.html
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing protein target
    information with advanced filtering, visualizations, and data export capabilities
    across the druggable genome
  format: http
  id: pharos.portal
  name: Pharos Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/
- category: Product
  description: Target Central Resource Database (TCRD) downloadable database files
    containing comprehensive protein target information including druggability classifications,
    expression data, disease associations, and chemical probe information
  format: http
  id: pharos.tcrd.download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://opendata.ncats.nih.gov/public/pharos/
  warnings:
  - The Pharos footer still links the historical Juniper TCRD download host, but the
    about page points Pharos data downloads to NCATS OpenData; the registry uses the
    NCATS OpenData URL.
- category: ProgrammingInterface
  connection_url: https://pharos-api.ncats.io/graphql
  description: GraphQL API for programmatic access to Pharos and TCRD data enabling
    custom queries and integrations. The pharos.nih.gov/graphql page is the in-browser
    explorer; queries are served by the pharos-api.ncats.io/graphql endpoint used
    by the Pharos frontend.
  format: graphql
  id: pharos.api
  name: Pharos GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/graphql
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
rrid: SCR_006158
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