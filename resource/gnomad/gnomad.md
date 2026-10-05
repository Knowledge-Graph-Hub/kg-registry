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
- genetic variation
- population genetics
homepage_url: https://gnomad.broadinstitute.org/
id: gnomad
last_modified_date: '2026-09-23T00:00:00Z'
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
- category: ProgrammingInterface
  description: MyVariant.info REST API (v1) for variant query and annotation retrieval
    by HGVS id or rsid, with batch POST queries and field filtering. Returns JSON
    documents merged from the integrated sources, on hg19 and hg38.
  format: http
  id: myvariant.api
  infores_id: myvariant-info
  name: MyVariant.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myvariant
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: docm
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snpeff
  product_url: https://myvariant.info/v1/query
- category: Product
  compression: zip
  description: Academic branch of dbNSFP (v5.4a at time of curation, about 50 GB), a ZIP of
    gzipped, tab-delimited per-chromosome variant tables, the gene table, column descriptions
    and the search_dbNSFP Java program. Variant tables are also offered as a single tabix-indexed
    BGZF file per genome build (GRCh37, GRCh38) for Ensembl VEP and SnpSift. Includes all
    upstream scores that are free for academic use. Free for academic and non-commercial users
    after registration with an institutional email; download links are issued on request.
  format: tsv
  id: dbnsfp.academic
  license:
    id: https://creativecommons.org/licenses/by-nc-nd/4.0/
    label: CC BY-NC-ND 4.0
  name: dbNSFP Academic Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/download
- category: Product
  compression: zip
  description: Commercial branch of dbNSFP (v5.4c at time of curation), in the same format
    as the academic branch but excluding CADD, VEST, M-CAP, MutScore, PolyPhen-2, PrimateAI
    and RGC Million Exome data, whose authors require separate commercial licenses. Available
    to subscribers under a paid license from Genos Bioinformatics.
  format: tsv
  id: dbnsfp.commercial
  license:
    id: https://www.dbnsfp.org/license
    label: Commercial license (Genos Bioinformatics LLC)
  name: dbNSFP Commercial Branch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbnsfp
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: topmed
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: zfin
  product_url: https://www.dbnsfp.org/license
- category: Product
  compression: gzip
  description: CADD v1.7 scores for small insertions and deletions observed in gnomAD v4.0
    genomes, on GRCh38, tab-separated and bgzip-compressed with a tabix index.
  format: tsv
  id: cadd.gnomad-indels.grch38
  name: CADD v1.7 gnomAD v4.0 InDel Scores (GRCh38)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  - relation_type: prov:hadPrimarySource
    source: gnomad
  product_file_size: 1257151321
  product_url: https://krishna.gs.washington.edu/download/CADD/v1.7/GRCh38/gnomad.genomes.r4.0.indel.tsv.gz
- category: ProgrammingInterface
  connection_url: https://pavs.phenomebrowser.net/sparql
  description: Public Virtuoso SPARQL endpoint for the PAVS knowledge graph, containing Saudi
    case records, gene annotations, HPO disease annotations, HPO information content values
    and literature phenopackets as RDF named graphs.
  format: http
  id: pavs-kg.sparql
  is_public: true
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/sparql
- category: GraphicalInterface
  description: PAVS web portal with phenotype-based semantic similarity search, gene and variant
    browsers, and an HPO hierarchy explorer over the knowledge graph.
  format: http
  id: pavs-kg.portal
  name: PAVS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/
- category: ProgrammingInterface
  description: FastAPI REST API backing the PAVS portal, with OpenAPI documentation, for case
    search and SPARQL-backed queries.
  format: http
  id: pavs-kg.api
  name: PAVS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://pavs.phenomebrowser.net/api/docs
- category: Product
  description: Combined GA4GH Phenopackets v2 JSON file of all PAVS cases, with HPO phenotypes,
    variants, genes, zygosity, pathogenicity and disease diagnoses.
  format: json
  id: pavs-kg.phenopackets
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: PAVS Phenopackets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pavs-kg
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  product_url: https://raw.githubusercontent.com/bio-ontology-research-group/pavs-knowledge-graph/master/data/PAVS_phenopackets.json
publications:
- authors:
  - Konrad J. Karczewski
  - Laurent C. Francioli
  - Grace Tiao
  - Beryl B. Cummings
  - Jessica Alföldi
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
  - Anne H. O’Donnell-Luria
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
  - Josée Dupuis
  - Patrick T. Ellinor
  - Roberto Elosua
  - Jeanette Erdmann
  - Tõnu Esko
  - Martti Färkkilä
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
  - Terho Lehtimäki
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
  - Michael C. O’Donovan
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