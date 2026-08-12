---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://gnomad.broadinstitute.org/policies
  label: gnomAD Project, Broad Institute
creation_date: '2026-08-12T00:00:00Z'
description: A reference catalogue of human genetic variation, aggregating and harmonizing
  exome and genome sequencing data from large-scale sequencing projects to provide
  population allele frequencies and gene-level constraint metrics.
domains:
- genomics
- biomedical
- precision medicine
homepage_url: https://gnomad.broadinstitute.org/
id: gnomad
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Genome Aggregation Database (gnomAD)
products:
- category: GraphicalInterface
  description: The gnomAD browser, providing search and display of variants, genes,
    transcripts, and regions with population allele frequencies and constraint metrics.
  format: http
  id: gnomad.browser
  name: gnomAD browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnomad
  product_url: https://gnomad.broadinstitute.org/
- category: Product
  description: Bulk downloads of gnomAD variant data, coverage, and constraint files,
    distributed as VCF and Hail Table formats. Also mirrored on the AWS Registry of
    Open Data.
  format: vcf
  id: gnomad.downloads
  latest_version: 4.1.1
  name: gnomAD data downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnomad
  product_url: https://gnomad.broadinstitute.org/downloads
- category: ProgrammingInterface
  description: A public GraphQL API for programmatic queries against gnomAD variant
    and gene data.
  format: graphql
  id: gnomad.api
  is_public: true
  name: gnomAD GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnomad
  product_url: https://gnomad.broadinstitute.org/api
- category: GraphProduct
  compatibility:
  - standard: biolink
  description: A Biolink-conformant KGX TSV node file for the Sniff cross-species
    substrate, covering dog and human genes and canine and human diseases. Part of
    the facts-only federation bundle intended for ingest into other knowledge graphs.
  format: kgx
  id: sniff.federation-nodes
  name: Sniff KGX federation export, nodes
  node_categories:
  - biolink:Gene
  - biolink:Disease
  node_count: 36915
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sniff
  product_file_size: 3726803
  product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/sniff_nodes.tsv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: omia
  - relation_type: prov:wasDerivedFrom
    source: gnomad
publications:
- authors:
  - Konrad J. Karczewski
  - Laurent C. Francioli
  - Grace Tiao
  - Beryl B. Cummings
  - "Jessica Alf\xF6ldi"
  - Qingbo Wang
  - Ryan L. Collins
  - Kristen M. Laricchia
  - Andrea Ganna
  - Daniel P. Birnbaum
  - Laura D. Gauthier
  - Harrison Brand
  - Matthew Solomonson
  - Nicholas A. Watts
  - Daniel Rhodes
  - Moriel Singer-Berk
  - Eleina M. England
  - Eleanor G. Seaby
  - Jack A. Kosmicki
  - Raymond K. Walters
  - Katherine Tashman
  - Yossi Farjoun
  - Eric Banks
  - Timothy Poterba
  - Arcturus Wang
  - Cotton Seed
  - Nicola Whiffin
  - Jessica X. Chong
  - Kaitlin E. Samocha
  - Emma Pierce-Hoffman
  - Zachary Zappala
  - "Anne H. O\u2019Donnell-Luria"
  - Eric Vallabh Minikel
  - Ben Weisburd
  - Monkol Lek
  - James S. Ware
  - Christopher Vittal
  - Irina M. Armean
  - Louis Bergelson
  - Kristian Cibulskis
  - Kristen M. Connolly
  - Miguel Covarrubias
  - Stacey Donnelly
  - Steven Ferriera
  - Stacey Gabriel
  - Jeff Gentry
  - Namrata Gupta
  - Thibault Jeandet
  - Diane Kaplan
  - Christopher Llanwarne
  - Ruchi Munshi
  - Sam Novod
  - Nikelle Petrillo
  - David Roazen
  - Valentin Ruano-Rubio
  - Andrea Saltzman
  - Molly Schleicher
  - Jose Soto
  - Kathleen Tibbetts
  - Charlotte Tolonen
  - Gordon Wade
  - Michael E. Talkowski
  - Carlos A. Aguilar Salinas
  - Tariq Ahmad
  - Christine M. Albert
  - Diego Ardissino
  - Gil Atzmon
  - John Barnard
  - Laurent Beaugerie
  - Emelia J. Benjamin
  - Michael Boehnke
  - Lori L. Bonnycastle
  - Erwin P. Bottinger
  - Donald W. Bowden
  - Matthew J. Bown
  - John C. Chambers
  - Juliana C. Chan
  - Daniel Chasman
  - Judy Cho
  - Mina K. Chung
  - Bruce Cohen
  - Adolfo Correa
  - Dana Dabelea
  - Mark J. Daly
  - Dawood Darbar
  - Ravindranath Duggirala
  - "Jos\xE9e Dupuis"
  - Patrick T. Ellinor
  - Roberto Elosua
  - Jeanette Erdmann
  - "T\xF5nu Esko"
  - "Martti F\xE4rkkil\xE4"
  - Jose Florez
  - Andre Franke
  - Gad Getz
  - Benjamin Glaser
  - Stephen J. Glatt
  - David Goldstein
  - Clicerio Gonzalez
  - Leif Groop
  - Christopher Haiman
  - Craig Hanis
  - Matthew Harms
  - Mikko Hiltunen
  - Matti M. Holi
  - Christina M. Hultman
  - Mikko Kallela
  - Jaakko Kaprio
  - Sekar Kathiresan
  - Bong-Jo Kim
  - Young Jin Kim
  - George Kirov
  - Jaspal Kooner
  - Seppo Koskinen
  - Harlan M. Krumholz
  - Subra Kugathasan
  - Soo Heon Kwak
  - Markku Laakso
  - "Terho Lehtim\xE4ki"
  - Ruth J. F. Loos
  - Steven A. Lubitz
  - Ronald C. W. Ma
  - Daniel G. MacArthur
  - Jaume Marrugat
  - Kari M. Mattila
  - Steven McCarroll
  - Mark I. McCarthy
  - Dermot McGovern
  - Ruth McPherson
  - James B. Meigs
  - Olle Melander
  - Andres Metspalu
  - Benjamin M. Neale
  - Peter M. Nilsson
  - "Michael C. O\u2019Donovan"
  - Dost Ongur
  - Lorena Orozco
  - Michael J. Owen
  - Colin N. A. Palmer
  - Aarno Palotie
  - Kyong Soo Park
  - Carlos Pato
  - Ann E. Pulver
  - Nazneen Rahman
  - Anne M. Remes
  - John D. Rioux
  - Samuli Ripatti
  - Dan M. Roden
  - Danish Saleheen
  - Veikko Salomaa
  - Nilesh J. Samani
  - Jeremiah Scharf
  - Heribert Schunkert
  - Moore B. Shoemaker
  - Pamela Sklar
  - Hilkka Soininen
  - Harry Sokol
  - Tim Spector
  - Patrick F. Sullivan
  - Jaana Suvisaari
  - E. Shyong Tai
  - Yik Ying Teo
  - Tuomi Tiinamaija
  - Ming Tsuang
  - Dan Turner
  - Teresa Tusie-Luna
  - Erkki Vartiainen
  - Marquis P. Vawter
  - James S. Ware
  - Hugh Watkins
  - Rinse K. Weersma
  - Maija Wessman
  - James G. Wilson
  - Ramnik J. Xavier
  - Benjamin M. Neale
  - Mark J. Daly
  - Daniel G. MacArthur
  doi: doi:10.1038/s41586-020-2308-7
  id: https://doi.org/10.1038/s41586-020-2308-7
  journal: Nature
  preferred: true
  title: The mutational constraint spectrum quantified from variation in 141,456 humans
  year: '2020'
synonyms:
- gnomAD
taxon:
- NCBITaxon:9606
version: 4.1.1
---
The Genome Aggregation Database (gnomAD) is a resource developed by an international coalition of investigators to aggregate and harmonize exome and genome sequencing data from a wide variety of large-scale sequencing projects. It is hosted by the Broad Institute.

The v4.1 dataset, aligned to GRCh38, spans 730,947 exome sequences and 76,215 whole-genome sequences from unrelated individuals of diverse ancestries. gnomAD is widely used as a population reference for variant interpretation, providing allele frequencies stratified by genetic ancestry group alongside gene-level constraint metrics.

Primary data from the gnomAD exomes and genomes are released free of restrictions under the Creative Commons Zero Public Domain Dedication, though the project requests attribution where possible.