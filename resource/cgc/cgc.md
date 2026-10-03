---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: cgc@umn.edu
  - contact_type: url
    value: https://cgc.umn.edu/
  label: Caenorhabditis Genetics Center
creation_date: '2026-10-03T00:00:00Z'
description: The Caenorhabditis Genetics Center (CGC) collects, maintains and distributes
  genetic stocks (strains) of the nematode Caenorhabditis elegans and related species,
  aiming to hold a null mutation for every C. elegans gene along with strains that
  serve as genetic and molecular tools, such as chromosome rearrangements, endogenously
  tagged loci and expression tools. Each strain record gives the genotype, description,
  mutagen, outcrossing and provenance. The CGC is based at the University of Minnesota
  and funded by the NIH Office of Research Infrastructure Programs.
domains:
- model organisms
- organisms
- genetic variation
- genomics
- phenotype
homepage_url: https://cgc.umn.edu/
id: cgc
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
name: Caenorhabditis Genetics Center
products:
- category: Product
  description: Plain-text dump of all CGC strain records in a key/value record layout,
    with fields for strain, species, genotype, description, mutagen, outcrossed, made
    by and received.
  format: txt
  id: cgc.strain-list
  name: CGC Strain List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgc
  product_file_size: 18535807
  product_url: https://cgc.umn.edu/static/cgc-strains.txt
- category: GraphicalInterface
  description: Web search over CGC strains by genotype, description, mutagen and maker,
    with strain pages and CSV export of full search results.
  format: http
  id: cgc.strain-search
  name: CGC Strain Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgc
  product_url: https://cgc.umn.edu/strain/search
publications:
- authors:
  - Victor R Ambros
  - Martin Chalfie
  - Aric L Daul
  - Andrew Z Fire
  - David H Hall
  - H Robert Horvitz
  - Craig C Mello
  - Gary Ruvkun
  - Nathan E Schroeder
  - Paul W Sternberg
  - Ann E Rougvie
  doi: 10.1073/pnas.2522808122
  id: doi:10.1073/pnas.2522808122
  journal: Proceedings of the National Academy of Sciences
  preferred: true
  title: 'From nematode to Nobel: How community-shared resources fueled the rise of
    Caenorhabditis elegans as a research organism'
  year: '2025'
synonyms:
- CGC
taxon:
- NCBITaxon:6237
---
# Caenorhabditis Genetics Center (CGC)

The Caenorhabditis Genetics Center collects, maintains and distributes genetic stocks
of the nematode *Caenorhabditis elegans* and related species. Its goal is to hold a
null mutation for every *C. elegans* gene, along with strains that serve as genetic
and molecular tools: chromosome rearrangements, endogenously tagged loci, protein
depletion strains and expression tools. It also distributes wild isolates of
*Caenorhabditis* and other nematodes (RRID:SCR_007341).

The downloadable strain list held 26,321 strain records as of its 2026-01-22 update.
Most are *C. elegans*; others include *C. briggsae*, *C. remanei* and *E. coli* food
strains.

## History and Funding

Stock center operations began at the University of Missouri in 1979 under a National
Institute on Aging contract, and the CGC moved to the University of Minnesota, Twin
Cities, in 1992. It is funded by the NIH Office of Research Infrastructure Programs
(P40 OD010440). A complete frozen copy of the collection is kept off-site at the
National Animal Germplasm Program in Fort Collins, Colorado.

## Data Access

- Strain search: https://cgc.umn.edu/strain/search (searches by genotype,
  description, mutagen and maker; the CSV button returns the full result set)
- Full strain list (plain text): https://cgc.umn.edu/static/cgc-strains.txt
- Curated lists of recently added strains, endogenously tagged loci, protein
  depletion strains and wild isolates are linked from the homepage.

Each strain page links to the matching WormBase strain record, and the CGC is an
upstream source of strain data for WormBase.

## Terms of Use

No license is stated for the strain data. The CGC Conditions of Use
(https://cgc.umn.edu/conditions-of-use) cover the physical stocks: they may not be
redistributed outside the recipient's organization without written consent, and
stocks with patented or exclusively licensed components may be used for nonprofit
research only.

## People

Ann Rougvie is the CGC director and Aric Daul is its curator.
