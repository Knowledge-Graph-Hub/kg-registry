---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: Sydney School of Veterinary Science, University of Sydney
    contact_details:
      - contact_type: url
        value: https://omia.org/home/
creation_date: '2026-08-12T00:00:00Z'
description: A catalogue of inherited disorders, other single-locus traits, and associated genes and variants in animals, covering 786 mostly vertebrate species.
domains:
  - organisms
  - genomics
  - phenotype
  - agriculture
homepage_url: https://omia.org/
id: omia
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
name: Online Mendelian Inheritance in Animals (OMIA)
products:
  - category: GraphicalInterface
    description: The OMIA web interface, providing browsing and search of phenes, species, genes, and likely causal variants.
    format: http
    id: omia.browser
    name: OMIA web interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omia
    product_url: https://omia.org/home/
  - category: Product
    description: A full dump of the OMIA database as MySQL SQL statements. The OMIA team asks to be contacted to discuss co-authorship arrangements for publications relying on this dump or on extended data.
    compression: gzip
    format: mysql
    id: omia.sql-dump
    name: OMIA SQL database dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omia
    product_url: https://omia.org/static/omia.sql.gz
  - category: Product
    description: A full dump of the OMIA database in XML format.
    compression: gzip
    format: xml
    id: omia.xml-dump
    name: OMIA XML database dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omia
    product_url: https://omia.org/static/omia.xml.gz
  - category: Product
    description: VCF exports of OMIA likely causal variants, given in the coordinates of the relevant species reference assemblies.
    format: vcf
    id: omia.vcf-exports
    name: OMIA variant VCF exports
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omia
    product_url: https://omia.org/download/vcf_exports/
  - category: MappingProduct
    description: A CSV mapping OMIA internal gene identifiers to NCBI Gene identifiers.
    format: csv
    id: omia.gene-mappings
    name: OMIA to NCBI Gene mappings
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omia
      - relation_type: prov:hadPrimarySource
        source: ncbigene
    product_url: https://omia.org/download/csv/genes/
synonyms:
  - OMIA
---

Online Mendelian Inheritance in Animals (OMIA) is a catalogue of inherited disorders, other single-locus traits, and associated genes and variants in animals. It is curated at the Sydney School of Veterinary Science, University of Sydney, founded by Frank Nicholas and curated by Imke Tammen.

OMIA covers 786 mostly vertebrate species, with 6,046 traits recorded in total, of which 2,120 are single-gene traits and 1,518 are single-gene diseases, alongside 1,793 known likely causal variants. Dogs account for the largest share of entries, with 1,014 traits, which makes OMIA the reference catalogue for canine inherited disease.

OMIA has been a free internet resource for over 30 years. Note that the site does not carry an explicit license statement, so no license is recorded here; the project asks users to cite OMIA, to acknowledge software support from the Sydney Informatics Hub, and to make contact to discuss co-authorship for publications that rely on the full MySQL dump or extended data.
