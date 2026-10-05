---
activity_status: inactive
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://developers.google.com/freebase
  label: Google
creation_date: '2026-10-04T00:00:00Z'
description: Freebase was a large collaborative knowledge base of structured general
  knowledge, started by Metaweb Technologies in 2007 and acquired by Google in 2010.
  Its graph of topics, types and properties (about 1.9 billion triples in the final
  RDF dump) was used as a source for the Google Knowledge Graph and for many linked
  data and NLP projects. Freebase was shut down in 2016 and much of its content migrated
  to Wikidata. Google still documents the final data dumps, but the download links
  denied anonymous access when checked on 2026-10-04.
domains:
- general
homepage_url: https://developers.google.com/freebase
id: freebase
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/2.5/
  label: CC BY 2.5
name: Freebase
products:
- category: GraphProduct
  compression: gzip
  description: Final Freebase RDF dump with every fact in Freebase at shutdown, about
    1.9 billion triples serialized as N-Triples (about 22 GB compressed, 250 GB uncompressed).
  format: ntriples
  id: freebase.rdf
  name: Freebase Triples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: freebase
  product_url: https://commondatastorage.googleapis.com/freebase-public/rdf/freebase-rdf-latest.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-10-04. Google Cloud Storage
    returned HTTP 403 AccessDenied for anonymous requests.
- category: Product
  compression: targz
  description: One-time dump of about 63 million triples deleted from Freebase through
    March 2013, in a CSV-like format split across 20 files (about 2 GB compressed).
  format: csv
  id: freebase.deleted-triples
  name: Freebase Deleted Triples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: freebase
  product_url: https://storage.googleapis.com/freebase-public/deleted_freebase.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-10-04. Google Cloud Storage
    returned HTTP 403 AccessDenied for anonymous requests.
- category: MappingProduct
  compression: gzip
  description: About 2.1 million owl sameAs links between Freebase MIDs and Wikidata
    items, built from the Wikidata dump of 2013-10-28 using shared Wikipedia links,
    released under CC0.
  format: ntriples
  id: freebase.wikidata-mappings
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: Freebase/Wikidata Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: freebase
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://storage.googleapis.com/freebase-public/fb2w.nt.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-10-04. Google Cloud Storage
    returned HTTP 403 AccessDenied for anonymous requests.
- category: DocumentationProduct
  description: Google Developers page describing the Freebase data dumps, their formats
    and license terms, and how to cite them.
  format: http
  id: freebase.docs
  name: Freebase Data Dumps Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: freebase
  product_url: https://developers.google.com/freebase
- category: DocumentationProduct
  description: PDF specification of PROTON 3.0 Beta, describing the System, Top, Extent
    and Knowledge Management modules and their classes and properties.
  format: pdf
  id: proton.ontology
  is_public: true
  name: PROTON 3.0 Beta Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: freebase
  - relation_type: prov:wasInfluencedBy
    source: wordnet
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
publications:
- authors:
  - Kurt Bollacker
  - Colin Evans
  - Praveen Paritosh
  - Tim Sturge
  - Jamie Taylor
  doi: 10.1145/1376616.1376746
  id: doi:10.1145/1376616.1376746
  journal: Proceedings of the 2008 ACM SIGMOD international conference on Management
    of data
  preferred: true
  title: Freebase
  year: '2008'
synonyms:
- Metaweb Freebase
---
# Freebase

Freebase was a collaboratively edited knowledge base of structured general knowledge. Metaweb Technologies launched it in 2007, and Google acquired it in 2010. Data was organized as a graph of topics, identified by machine IDs (MIDs such as `/m/012rkqx`), with types and properties defined in a community-maintained schema.

Google announced Freebase's closure in December 2014, made it read-only in 2015 and shut down the API in 2016. Much of its content was migrated to [Wikidata](https://www.wikidata.org/), so Wikidata is the maintained alternative for most uses.

## Data Dumps

Google's Freebase page documents three final data releases:

- **Freebase Triples**: every fact in Freebase at shutdown, about 1.9 billion triples in N-Triples format (CC BY).
- **Freebase Deleted Triples**: about 63 million triples deleted through March 2013 (CC BY).
- **Freebase/Wikidata Mappings**: about 2.1 million `owl:sameAs` links from Freebase MIDs to Wikidata items (CC0).

When checked on 2026-10-04, all three download links on Google Cloud Storage returned HTTP 403 (AccessDenied) for anonymous requests, even though the documentation page still lists them. Copies may exist in third-party archives.

## Usage

Freebase was widely used as a benchmark and source dataset, for example for knowledge base completion (FB15k and FB15k-237), entity linking and question answering. It was also mapped to other ontologies, such as the PROTON upper-level ontology's Linked Open Data extension.