---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pubmedinfo@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://support.nlm.nih.gov/
  id: ncbi
  label: NCBI PubMed Help Desk
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/
  id: ncbi
  label: National Library of Medicine
creation_date: '2025-10-31T00:00:00Z'
description: PubMed is a free search engine accessing primarily the MEDLINE database
  of references and abstracts on life sciences and biomedical topics, maintained by
  the United States National Library of Medicine (NLM) at the National Institutes
  of Health (NIH). MEDLINE is NLM's premier bibliographic database containing more
  than 31 million references to journal articles indexed with Medical Subject Headings
  (MeSH). PubMed comprises more than 39 million citations for biomedical literature
  from MEDLINE, life science journals, and online books, with citations including
  links to full-text content from PubMed Central and publisher web sites. The database
  is updated daily and covers publications from the 1950s to the present.
domains:
- biomedical
- literature
- clinical
homepage_url: https://pubmed.ncbi.nlm.nih.gov/
id: pubmed
infores_id: pubmed
last_modified_date: '2026-06-22T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain (U.S. Government)
name: PubMed and MEDLINE
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing PubMed's 39+ million biomedical
    literature citations with advanced search, clinical queries, and MeSH database
    integration
  format: http
  id: pubmed.portal
  name: PubMed Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://pubmed.ncbi.nlm.nih.gov/
- category: ProgrammingInterface
  description: Entrez Programming Utilities (E-utilities) API providing programmatic
    access to PubMed data with eight server-side programs for querying and retrieving
    citations
  format: http
  id: pubmed.eutils
  name: PubMed E-utilities API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- category: Product
  description: Annual baseline set of PubMed citation records in XML format providing
    complete snapshot of the MEDLINE database
  format: xml
  id: pubmed.baseline
  name: PubMed Annual Baseline Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/
- category: Product
  description: Daily update files containing new, revised, and deleted PubMed citations
    in XML format
  format: xml
  id: pubmed.updates
  name: PubMed Daily Update Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/
- category: MappingProduct
  compression: gzip
  description: Gene to PubMed mapping data providing literature references associated
    with genes
  format: tsv
  id: ncbigene.gene2pubmed
  name: Gene to PubMed Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 267368408
  product_url: https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2pubmed.gz
- category: DocumentationProduct
  description: Comprehensive PubMed help documentation including user guides, FAQs,
    tutorials, and search tips
  format: http
  id: pubmed.help
  name: PubMed Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://pubmed.ncbi.nlm.nih.gov/help/
- category: GraphicalInterface
  description: Advanced search builder with field-specific queries, search history,
    and Boolean operators for complex literature searches
  format: http
  id: pubmed.advanced.search
  name: PubMed Advanced Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://pubmed.ncbi.nlm.nih.gov/advanced/
- category: GraphicalInterface
  description: Specialized clinical queries interface with pre-defined search filters
    for clinical studies, systematic reviews, and medical genetics
  format: http
  id: pubmed.clinical.queries
  name: PubMed Clinical Queries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://pubmed.ncbi.nlm.nih.gov/clinical/
- category: DocumentationProduct
  description: PubMed DTD documentation with annotations and examples for all XML
    elements and attributes
  format: http
  id: pubmed.dtd
  name: PubMed DTD Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://dtd.nlm.nih.gov/ncbi/pubmed/doc/out/250101/index.html
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: Product
  description: Literature references from PubMed automatically associated with genes
  format: http
  id: genecards.literature
  name: GeneCards Literature References
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  description: Co-occurrence database generated from public PubMed abstracts with
    entity normalization for Biolink-relevant biomedical concepts
  format: mixed
  id: omnicorp.cooccurrence
  name: OmniCorp Co-occurrence Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
  secondary_source:
  - relation_type: prov:used
    source: biolink
- category: ProgrammingInterface
  description: API behavior documented for adding co-occurrence counts and literature
    co-occurrence edges to TRAPI messages
  format: http
  id: omnicorp.api
  name: OmniCorp API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
  secondary_source:
  - relation_type: prov:used
    source: biolink
  warnings:
  - The registry points to the Translator wiki documentation; checked RENCI OmniCorp
    service URLs were unavailable or had certificate issues on 2026-06-02.
- category: GraphProduct
  description: Anti-tumor biomaterial knowledge graph constructed from biomedicine
    literature, containing structured relationships among anti-tumor entities extracted
    through entity recognition, sentence simplification, triple extraction, and predicate
    mapping.
  format: mixed
  id: atom.kg
  name: ATOM Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atom
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://doi.org/10.1109/BIBM47256.2019.8983062
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 418 error when
    accessing file
- category: Product
  description: Manually curated disease-gene associations and annotations for amyloidoses
    and amyloid deposition-related diseases extracted from biomedical literature.
  id: amyco.annotations
  name: AmyCo Curated Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: amyco
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: diseases
- category: Product
  compression: gzip
  description: Links between MedGen concepts and PubMed articles with gzip compression
  format: txt
  id: medgen.pubmed-links
  name: MedGen PubMed Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 239947326
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/medgen_pubmed_lnk.txt.gz
- category: ProcessProduct
  description: Natural language processing pipeline for constructing anti-tumor biomaterial
    knowledge graphs from unstructured biomedicine literature, implementing entity
    recognition, sentence simplification, triple extraction, and predicate mapping
    processes.
  format: mixed
  id: atom.pipeline
  name: ATOM Construction Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atom
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://doi.org/10.1109/BIBM47256.2019.8983062
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 418 error when
    accessing file
- category: GraphicalInterface
  description: FORUM web application interface for semantic metabolomics exploration
  format: http
  id: forum.webapp
  name: FORUM Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://forum-webapp.semantic-metabolomics.fr/
- category: ProgrammingInterface
  description: FORUM REST API for programmatic access to chemical-disease associations
  format: http
  id: forum.api
  name: FORUM API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://forum-webapp.semantic-metabolomics.fr/#/openapi-documentation
- category: DocumentationProduct
  description: FORUM VoID (Vocabulary of Interlinked Datasets) metadata describing
    the knowledge graph structure
  format: ttl
  id: forum.void
  name: FORUM VoID Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 96461
  product_url: https://forum.semantic-metabolomics.fr/.well-known/void
- category: GraphProduct
  description: Text-mined biomedical knowledge graph of gene–disease–drug relationships
    (semantic themes)
  format: http
  id: gnbr.graph
  name: GNBR graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://zenodo.org/records/3459420
- category: Product
  description: Version 6 JSON file containing literature metadata for the HALD corpus.
  format: json
  id: hald.literature-info.json
  latest_version: v6
  name: HALD Literature Info
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 854292307
  product_url: https://ndownloader.figshare.com/files/43612512
- category: Product
  description: Version 6 JSON file containing entity-level metadata extracted for
    HALD.
  format: json
  id: hald.entity-info.json
  latest_version: v6
  name: HALD Entity Info
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 296732271
  product_url: https://ndownloader.figshare.com/files/43612509
- category: GraphProduct
  description: Version 6 JSON file containing relation triples extracted for HALD.
  format: json
  id: hald.relation-info.json
  latest_version: v6
  name: HALD Relation Info
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 98203237
  product_url: https://ndownloader.figshare.com/files/43612506
- category: Product
  description: Version 6 JSON file containing aging biomarker records from HALD.
  format: json
  id: hald.aging-biomarkers.json
  latest_version: v6
  name: HALD Aging Biomarkers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 1199321
  product_url: https://ndownloader.figshare.com/files/43612503
- category: Product
  description: Version 6 JSON file containing longevity biomarker records from HALD.
  format: json
  id: hald.longevity-biomarkers.json
  latest_version: v6
  name: HALD Longevity Biomarkers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 339386
  product_url: https://ndownloader.figshare.com/files/43612497
- category: Product
  description: Version 6 CSV file containing entity rows for loading HALD into Neo4j.
  format: csv
  id: hald.entities.csv
  latest_version: v6
  name: HALD Neo4j Entities
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 239792
  product_url: https://ndownloader.figshare.com/files/43612494
- category: Product
  description: Version 6 CSV file containing relationship rows for loading HALD into
    Neo4j.
  format: csv
  id: hald.roles.csv
  latest_version: v6
  name: HALD Neo4j Roles
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 5077672
  product_url: https://ndownloader.figshare.com/files/43612500
- category: GraphicalInterface
  description: Interactive web interface for searching, browsing, and exploring HALD.
  format: http
  id: hald.browser
  name: HALD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hald
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://bis.zju.edu.cn/hald
- category: GraphicalInterface
  description: Biomedical Knowledge Discovery Engine. Interface for iKraph with search,
    visualization, and exploration capabilities.
  format: http
  id: ikraph.site
  name: BioKDE
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ikraph
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://biokde.insilicom.com/
- category: ProcessProduct
  description: Code for named entity recognition, relation extraction, and drug repurposing
    in assembly and analysis of iKraph
  format: mixed
  id: ikraph.code
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.en.html
    label: GPL-3
  name: iKraph Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ikraph
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/myinsilicom/iKraph
  repository: https://github.com/myinsilicom/iKraph
- category: GraphProduct
  compression: targz
  description: Graph metadata for iKraph, including a list of relations, entity type-specific
    metadata, data sources, and drug repurposing predictions.
  format: json
  id: ikraph.graph
  name: iKraph graph metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ikraph
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 61183533
  product_url: https://zenodo.org/records/14851275/files/data.tar.gz?download=1
- category: GraphProduct
  compression: targz
  description: Complete graph data for iKraph with all entities and relations extracted
    from PubMed abstracts
  format: mixed
  id: ikraph.graphdata
  name: iKraph graph data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ikraph
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 1440676039
  product_url: https://zenodo.org/records/14851275/files/iKraph_full.tar.gz?download=1
- category: GraphicalInterface
  description: Graphical interface for MedKG
  format: http
  id: medkb.site
  name: MedKG Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: http://pitools.niper.ac.in/medkg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: medkg
- category: GraphicalInterface
  description: Public web interface for querying and exploring ReproTox-KG relationships.
  format: http
  id: reprotox-kg.portal
  name: ReproTox-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://maayanlab.cloud/reprotox-kg
- category: Product
  description: Data and content assets published with ReproTox-KG (markdown and supporting
    materials).
  format: http
  id: reprotox-kg.data
  name: ReproTox-KG Data Assets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://github.com/MaayanLab/Reprotox-KG/tree/main/markdown
- category: DocumentationProduct
  description: Translator wiki page describing SuppKG scope and example supplement-disease
    relationships.
  format: http
  id: suppkg.docs
  name: SuppKG Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
- category: ProcessProduct
  description: Source data directory used for SuppKG in the SemRep_DS repository.
  format: http
  id: suppkg.source-data
  name: SuppKG Source Data Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG
- category: GraphProduct
  description: Weighted heterogeneous knowledge graph extracted from MEDLINE corpus
    containing 1,179 tumors, 2,550 biomarkers, 1,806 drugs, and 756 ADRs with 139,254
    relationship edges (Tumor-Biomarker, Tumor-Drug, Tumor-ADR, Drug-Biomarker, Drug-ADR,
    Biomarker-ADR). Includes correlation weights calculated using naive Bayesian model.
  format: mixed
  id: tbkg.data
  name: TBKG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tbkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
- category: Product
  description: Clinical validation dataset with calculated ADRs for osimertinib ranked
    by importance, biomarker pathways explaining drug-ADR relationships, and clinical
    data from 8 lung adenocarcinoma patients. Model achieved Kappa=0.68 concordance
    with official manual and 0.81 three-fold cross-validation accuracy.
  format: mixed
  id: tbkg.osimertinib_case_study
  name: TBKG Osimertinib ADR Case Study Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tbkg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://www.frontiersin.org/articles/10.3389/fgene.2020.625659/full#supplementary-material
- category: Product
  description: Raw format target information including all TTD target data
  format: txt
  id: ttd.targets-raw
  name: TTD Targets Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-01-TTD_target_download.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Drug to disease mapping with ICD identifiers
  format: txt
  id: ttd.drug-disease
  name: Drug-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-05-Drug_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to disease mapping with ICD identifiers
  format: txt
  id: ttd.target-disease
  name: Target-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-06-Target_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to drug mapping with mode of action information
  format: csv
  id: ttd.target-drug
  name: Target-Drug Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-07-Drug-TargetMapping.xlsx
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Biomarker to disease mapping with ICD identifiers
  format: txt
  id: ttd.biomarker-disease
  name: Biomarker-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-08-Biomarker_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to compound mapping with experimental activity data
  format: txt
  id: ttd.target-compound
  name: Target-Compound Activity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-09-Target_compound_activity.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: GraphicalInterface
  description: Graphical interface for GLKB
  format: http
  id: glkb.site
  name: GLKB Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glkb
  product_url: https://glkb.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: pubmed
- category: ProgrammingInterface
  connection_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  description: E-utilities API for programmatic access to Entrez databases
  format: json
  id: entrez.eutils
  name: Entrez E-utilities
  original_source:
  - relation_type: prov:hadPrimarySource
    source: entrez
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: ncbigene
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
- category: Product
  description: Downloadable dataset of dietary restriction-related genes
  format: csv
  id: gendr.data
  latest_version: Build 4
  name: GenDR Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gendr
  product_file_size: 8209
  product_url: https://hagr.ageing-map.org/diet/dataset.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: ncbigene
- category: Product
  description: Excel spreadsheet of dietary-restriction gene expression signatures
    from the HAGR meta-analysis of dietary restriction in mammals
  format: http
  id: gendr.expression-signatures
  name: GenDR Dietary Restriction Expression Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gendr
  product_file_size: 49152
  product_url: https://hagr.ageing-map.org/diet/TableS2.xls
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubmed
- category: GraphicalInterface
  description: Web interface for searching and retrieving variant information from
    35+ million PubMed articles with autocomplete, filtering, and entity highlighting
  format: http
  id: litvar.web_interface
  name: LitVar Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to variant summaries, publications,
    search, and gene-level variant queries
  format: http
  id: litvar.api
  name: LitVar API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2-api/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  format: mixed
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: Product
  description: dbPTM downloads for experimental and putative PTM sites, benchmark
    datasets, and cancer proteomics datasets, with PTM records mapped to UniProtKB
    protein entries and linked to literature evidence.
  format: tsv
  id: dbptm.downloads
  name: dbPTM Download Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbptm
  product_url: https://biomics.lab.nycu.edu.tw/dbPTM/download.php
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: Product
  description: Tab-delimited dbSNO 3.0 S-nitrosylation dataset containing UniProt
    identifiers, organisms, positions, and sequence context for manually curated and
    experimentally identified S-nitrosylated peptides.
  format: tsv
  id: dbsno.downloads
  name: dbSNO Download Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbsno
  product_url: https://biomics.lab.nycu.edu.tw/dbSNO/download.php
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-18: HTTP 500 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-22: HTTP 500 error
    when accessing file'
- category: Product
  description: Phospho.ELM version 9.0 dataset request page for phosphorylation instances
    with accessions, sequences, residue positions, phosphorylated residues, PubMed
    identifiers, upstream kinases, evidence source class, species, and entry dates.
  format: mixed
  id: phosphoelm.dataset
  license:
    id: http://phospho.elm.eu.org/dumps/Phospho.Elm_AcademicLicense.pdf
    label: Phospho.ELM Academic License
  name: Phospho.ELM Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphoelm
  product_url: http://phospho.elm.eu.org/dataset.html
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  warnings: []
- category: GraphicalInterface
  description: RLIMS-P web portal for searching phosphorylation information by keywords,
    organisms, date range, and PubMed identifiers, with extracted kinase, substrate,
    site, evidence text, and downloadable results.
  format: http
  id: rlims-p.portal
  name: RLIMS-P Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rlims-p
  product_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
  secondary_source:
  - relation_type: prov:used
    source: pubmed
- category: ProcessProduct
  description: Rule-based text-mining service for extracting protein phosphorylation
    events, including kinase, substrate, phosphorylation site, and textual evidence,
    from PubMed abstracts and selected literature corpora.
  format: http
  id: rlims-p.text-mining-service
  name: RLIMS-P Text-Mining Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rlims-p
  product_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
  secondary_source:
  - relation_type: prov:used
    source: pubmed
- category: GraphProduct
  description: Source CSV tables for AcuKG, including acupoint therapeutic actions,
    indications, anatomy relationships, clinical trial links, and PubMed links.
  edge_count: 11527
  format: csv
  id: acukg.csv
  name: AcuKG CSV tables
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG
- category: GraphProduct
  description: RDF Turtle representation of AcuKG relationship tables.
  edge_count: 11527
  format: ttl
  id: acukg.rdf
  name: AcuKG RDF Turtle files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_RDF
- category: GraphProduct
  description: JSON representation of AcuKG relationship tables.
  edge_count: 11527
  format: json
  id: acukg.json
  name: AcuKG JSON files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_json
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and exploring food compounds
    and their properties.
  format: http
  id: foodb.web
  name: FooDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_url: https://foodb.ca/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database in CSV format
  format: csv
  id: foodb.data.csv
  name: FooDB CSV Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 998314299
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_csv.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database in XML format
  format: xml
  id: foodb.data.xml
  name: FooDB XML Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 6731854848
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_xml.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: zip
  description: Complete FooDB database in JSON format
  format: json
  id: foodb.data.json
  name: FooDB JSON Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 90852659
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_04_07_json.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database as MySQL dump
  format: mysql
  id: foodb.data.mysql
  name: FooDB MySQL Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 180900659
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_mysql.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: GraphProduct
  description: Immune cell type-specific node and relationship CSV files for ICKG,
    including T cell, NK cell, and B cell graph exports.
  format: csv
  id: ickg.graph-data
  name: ICKG graph data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ickg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://github.com/KChen-lab/immune-knowledgegraph.github.io/tree/main/data
- category: GraphProduct
  description: Multilayer epilepsy knowledge graph generated by the myAURA data processing
    workflow from biomedical, clinical, literature, and patient-centered data sources.
  format: mixed
  id: myaura.graph
  name: myAURA epilepsy knowledge graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myaura
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://github.com/cns-iu/myaura
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
publications:
- authors:
  - Eric W Sayers
  - Jeff Beck
  - Evan E Bolton
  - J Rodney Brister
  - Jessica Chan
  - Donald C Comeau
  - Kim D Pruitt
  - Stephen T Sherry
  doi: 10.1093/nar/gkad1044
  id: doi:10.1093/nar/gkad1044
  journal: Nucleic Acids Research
  title: Database resources of the National Center for Biotechnology Information
  year: '2024'
- authors:
  - Nicolas Fiorini
  - Kathi Canese
  - Grisha Starchenko
  - Evgeny Kireev
  - Won Kim
  - Vadim Miller
  - Maxim Osipov
  - Michael Kholodov
  - Rafis Ismagilov
  - Sunil Mohan
  - James Ostell
  - Zhiyong Lu
  doi: 10.1371/journal.pbio.2005343
  id: doi:10.1371/journal.pbio.2005343
  journal: PLOS Biology
  title: 'Best Match: New relevance search for PubMed'
  year: '2018'
repository: https://www.ncbi.nlm.nih.gov/
synonyms:
- PubMed
- MEDLINE
- MEDLINE via PubMed
- MEDLARS
taxon:
- NCBITaxon:9606
---
