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
description: PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics, maintained by the United States National Library of Medicine (NLM) at the National Institutes of Health (NIH). MEDLINE is NLM's premier bibliographic database containing more than 31 million references to journal articles indexed with Medical Subject Headings (MeSH). PubMed comprises more than 39 million citations for biomedical literature from MEDLINE, life science journals, and online books, with citations including links to full-text content from PubMed Central and publisher web sites. The database is updated daily and covers publications from the 1950s to the present.
domains:
  - biomedical
  - literature
  - health
  - clinical
homepage_url: https://pubmed.ncbi.nlm.nih.gov/
id: pubmed
infores_id: pubmed
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain (U.S. Government)
name: PubMed and MEDLINE
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing PubMed's 39+ million biomedical literature citations with advanced search, clinical queries, and MeSH database integration
    format: http
    id: pubmed.portal
    name: PubMed Web Portal
    product_url: https://pubmed.ncbi.nlm.nih.gov/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: ProgrammingInterface
    description: Entrez Programming Utilities (E-utilities) API providing programmatic access to PubMed data with eight server-side programs for querying and retrieving citations
    format: http
    id: pubmed.eutils
    name: PubMed E-utilities API
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Annual baseline set of PubMed citation records in XML format providing complete snapshot of the MEDLINE database
    format: xml
    id: pubmed.baseline
    name: PubMed Annual Baseline Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Daily update files containing new, revised, and deleted PubMed citations in XML format
    format: xml
    id: pubmed.updates
    name: PubMed Daily Update Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: MappingProduct
    compression: gzip
    description: Gene to PubMed mapping data providing literature references associated with genes
    format: tsv
    id: ncbigene.gene2pubmed
    name: Gene to PubMed Mapping
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: ncbigene
    product_file_size: 230242176
    product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz
  - category: DocumentationProduct
    description: Comprehensive PubMed help documentation including user guides, FAQs, tutorials, and search tips
    format: http
    id: pubmed.help
    name: PubMed Help Documentation
    product_url: https://pubmed.ncbi.nlm.nih.gov/help/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Advanced search builder with field-specific queries, search history, and Boolean operators for complex literature searches
    format: http
    id: pubmed.advanced.search
    name: PubMed Advanced Search
    product_url: https://pubmed.ncbi.nlm.nih.gov/advanced/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Specialized clinical queries interface with pre-defined search filters for clinical studies, systematic reviews, and medical genetics
    format: http
    id: pubmed.clinical.queries
    name: PubMed Clinical Queries
    product_url: https://pubmed.ncbi.nlm.nih.gov/clinical/
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: PubMed DTD documentation with annotations and examples for all XML elements and attributes
    format: http
    id: pubmed.dtd
    name: PubMed DTD Documentation
    product_url: https://dtd.nlm.nih.gov/ncbi/pubmed/doc/out/250101/index.html
    original_source:
      - source: pubmed
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: lincs-l1000
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: civic
      - relation_type: prov:hadPrimarySource
        source: gdsc
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: metacyc
      - relation_type: prov:hadPrimarySource
        source: bv-brc
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: pathophenodb
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: protcid
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: spoke
  - category: ProcessProduct
    description: INDRA CoGEx is a graph database integrating causal relations, ontological relations, properties, and data, assembled at scale automatically from the scientific literature and structured sources. This is the code to build the graph.
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
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: indra
  - category: Product
    description: Literature references from PubMed automatically associated with genes
    format: http
    id: genecards.literature
    name: GeneCards Literature References
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: https://www.genecards.org/
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error when accessing file'
  - category: Product
    description: Co-occurrence data from PubMed abstracts
    format: mixed
    id: omnicorp.cooccurrence
    name: OmniCorp Co-occurrence Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: omnicorp
  - category: ProgrammingInterface
    description: API access to OmniCorp co-occurrence data
    format: http
    id: omnicorp.api
    name: OmniCorp API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: omnicorp
  - category: GraphProduct
    description: Anti-tumor biomaterial knowledge graph constructed from biomedicine literature, containing structured relationships among anti-tumor entities extracted through entity recognition, sentence simplification, triple extraction, and predicate mapping.
    id: atom.kg
    name: ATOM Knowledge Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: https://doi.org/10.1109/BIBM47256.2019.8983062
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 418 error when accessing file
  - category: Product
    description: Manually curated disease-gene associations and annotations for amyloidoses and amyloid deposition-related diseases extracted from biomedical literature.
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
  - category: GraphProduct
    description: Downloadable knowledge graph dump in TAR/GZ format containing complete FORUM data
    id: forum.graph.dump
    name: FORUM Knowledge Graph Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cito
      - relation_type: prov:hadPrimarySource
        source: fabio
      - relation_type: prov:hadPrimarySource
        source: dc
      - relation_type: prov:hadPrimarySource
        source: cheminf
      - relation_type: prov:hadPrimarySource
        source: skos
      - relation_type: prov:hadPrimarySource
        source: chemont
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: forum
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ FTP error_ timed out
      - 'File was not able to be retrieved when checked on 2026-05-04: FTP error: timed out'
      - 'File was not able to be retrieved when checked on 2026-05-09: FTP error: timed out'
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
repository: https://www.ncbi.nlm.nih.gov/
synonyms:
  - PubMed
  - MEDLINE
  - MEDLINE via PubMed
  - MEDLARS
taxon:
  - NCBITaxon:9606
---
