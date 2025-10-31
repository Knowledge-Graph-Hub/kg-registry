---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "pubmedinfo@ncbi.nlm.nih.gov"
      - contact_type: url
        value: "https://support.nlm.nih.gov/"
    label: NCBI PubMed Help Desk
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.nlm.nih.gov/"
    label: National Library of Medicine
creation_date: '2025-10-31T00:00:00Z'
description: "PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics, maintained by the United States National Library of Medicine (NLM) at the National Institutes of Health (NIH). MEDLINE is NLM's premier bibliographic database containing more than 31 million references to journal articles indexed with Medical Subject Headings (MeSH). PubMed comprises more than 39 million citations for biomedical literature from MEDLINE, life science journals, and online books, with citations including links to full-text content from PubMed Central and publisher web sites. The database is updated daily and covers publications from the 1950s to the present."
domains:
  - biomedical
  - literature
  - health
  - clinical
homepage_url: https://pubmed.ncbi.nlm.nih.gov/
id: "pubmed"
infores_id: "pubmed"
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: "https://www.ncbi.nlm.nih.gov/home/about/policies/"
  label: Public Domain (U.S. Government)
name: PubMed and MEDLINE
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing PubMed's 39+ million biomedical literature citations with advanced search, clinical queries, and MeSH database integration
    format: http
    id: "pubmed.portal"
    name: PubMed Web Portal
    product_url: https://pubmed.ncbi.nlm.nih.gov/
  - category: ProgrammingInterface
    description: Entrez Programming Utilities (E-utilities) API providing programmatic access to PubMed data with eight server-side programs for querying and retrieving citations
    format: http
    id: "pubmed.eutils"
    name: PubMed E-utilities API
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
  - category: Product
    description: Annual baseline set of PubMed citation records in XML format providing complete snapshot of the MEDLINE database
    format: xml
    id: "pubmed.baseline"
    name: PubMed Annual Baseline Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/
  - category: Product
    description: Daily update files containing new, revised, and deleted PubMed citations in XML format
    format: xml
    id: "pubmed.updates"
    name: PubMed Daily Update Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/
  - category: MappingProduct
    compression: gzip
    description: Mapping file linking NCBI Gene IDs to PubMed citation IDs, providing literature references associated with genes
    format: tsv
    id: "ncbigene.gene2pubmed"
    name: Gene to PubMed Mapping
    original_source:
      - pubmed
      - ncbigene
    product_file_size: 230242176
    product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz
  - category: DocumentationProduct
    description: Comprehensive PubMed help documentation including user guides, FAQs, tutorials, and search tips
    format: http
    id: "pubmed.help"
    name: PubMed Help Documentation
    product_url: https://pubmed.ncbi.nlm.nih.gov/help/
  - category: GraphicalInterface
    description: Advanced search builder with field-specific queries, search history, and Boolean operators for complex literature searches
    format: http
    id: "pubmed.advanced.search"
    name: PubMed Advanced Search
    product_url: https://pubmed.ncbi.nlm.nih.gov/advanced/
  - category: GraphicalInterface
    description: Specialized clinical queries interface with pre-defined search filters for clinical studies, systematic reviews, and medical genetics
    format: http
    id: "pubmed.clinical.queries"
    name: PubMed Clinical Queries
    product_url: https://pubmed.ncbi.nlm.nih.gov/clinical/
  - category: DocumentationProduct
    description: PubMed DTD documentation with annotations and examples for all XML elements and attributes
    format: http
    id: "pubmed.dtd"
    name: PubMed DTD Documentation
    product_url: https://dtd.nlm.nih.gov/ncbi/pubmed/doc/out/250101/index.html
repository: https://www.ncbi.nlm.nih.gov/
synonyms:
  - PubMed
  - MEDLINE
  - MEDLINE via PubMed
  - MEDLARS
---
