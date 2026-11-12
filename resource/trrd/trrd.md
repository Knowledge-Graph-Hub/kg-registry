---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://wwwmgs.bionet.nsc.ru/mgs/gnw/trrd/contact.shtml
  label: Institute of Cytology and Genetics, Siberian Branch of the Russian Academy
    of Sciences
- category: Individual
  contact_details:
  - contact_type: email
    value: kol@bionet.nsc.ru
  label: Nikolay A. Kolchanov
creation_date: '2026-11-12T00:00:00Z'
description: The Transcription Regulatory Regions Database (TRRD) is a manually curated
  database of the structure and function of transcription regulatory regions of eukaryotic
  genes, developed at the Institute of Cytology and Genetics, Siberian Branch of the
  Russian Academy of Sciences (Novosibirsk). Each entry corresponds to a gene and
  records only experimentally confirmed data, annotated from the scientific literature,
  on promoters, enhancers, silencers and locus control regions, transcription factor
  binding sites, the transcription factors that bind them, and gene expression patterns.
  The data are split into linked libraries (TRRDGENES, TRRDUNITS, TRRDSITES, TRRDFACTORS,
  TRRDEXP, TRRDLCR, TRRDBIB and, from release 7.0, TRRDSTARTS) that are queried through
  a Sequence Retrieval System (SRS) server. The last announced release is TRRD 7.0
  (September 2005); the SRS libraries were last indexed in November 2015. The website
  and SRS server still respond but the database is no longer updated. TRRD is one of
  the curated sources of transcription factor to target gene interactions compiled
  into TFactS.
domains:
- gene regulation
- genomics
homepage_url: https://wwwmgs.bionet.nsc.ru/mgs/gnw/trrd/
id: trrd
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Transcription Regulatory Regions Database
products:
- category: GraphicalInterface
  description: TRRD website, with general information, the user's guide, database
    schema, search instructions, release history, statistics and links to the SRS
    query interface and the TRRD Viewer. The pages describe release 7.0 (September
    2005) and have not been updated since.
  format: http
  id: trrd.portal
  name: TRRD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: https://wwwmgs.bionet.nsc.ru/mgs/gnw/trrd/
  rrid: SCR_005723
  warnings:
  - The site is frozen at TRRD release 7.0 (September 2005) and is no longer maintained.
- category: GraphicalInterface
  description: Sequence Retrieval System (SRS 6) server at the Institute of Cytology
    and Genetics hosting the TRRD libraries. When checked on 2026-11-12 the libraries
    held TRRDGENES4 (2344 gene entries), TRRDUNITS4 (3490 regulatory regions), TRRDSITES4
    (10135 transcription factor binding sites), TRRDFACTORS4 (9087 transcription factor
    entries), TRRDEXP4 (14407 expression patterns), TRRDBIB4 (7609 publications),
    TRRDLCR (14 locus control regions) and TRRDSTARTS (709 transcription start sites),
    all indexed 03-Nov-2015. Gene entries link to Entrez Gene and TRANSFAC.
  format: http
  id: trrd.srs
  name: TRRD SRS Query Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: http://srs6.bionet.nsc.ru/srs6bin/cgi-bin/wgetz?-page+LibInfo+-lib+TRRDGENES4
  warnings:
  - The SRS server is served over plain HTTP only and its libraries were last indexed
    in November 2015.
- category: DocumentationProduct
  description: Description of the TRRD database schema, explaining the hierarchical
    organisation of gene, regulatory region, binding site, factor, expression and
    bibliography records.
  format: http
  id: trrd.schema
  name: TRRD Database Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: https://wwwmgs.bionet.nsc.ru/mgs/gnw/trrd/db_schema.shtml
- category: Product
  description: TFactS catalogues (version 2) as a legacy Excel workbook, recovered
    from an Internet Archive Wayback Machine snapshot of tfacts.org. The workbook
    has a sign-less sheet of about 6,800 transcription factor to target gene pairs,
    with references, species and accessions, and a sign-sensitive sheet of about 3,250
    pairs annotated as up- or down-regulation with PubMed references. Sources include
    TRED and PubMed literature.
  format: http
  id: tfacts.catalogues
  name: TFactS Catalogues (version 2, Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: pazar
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: https://web.archive.org/web/20220617202237/https://www.tfacts.org/TFactS-new/TFactS-v2/tfacts/data/Catalogues.xls
publications:
- authors:
  - Kolchanov NA
  - Ignatieva EV
  - Ananko EA
  - Podkolodnaya OA
  - Stepanenko IL
  - Merkulova TI
  - Pozdnyakov MA
  - Podkolodny NL
  - Naumochkin AN
  - Romashchenko AG
  doi: 10.1093/nar/30.1.312
  id: doi:10.1093/nar/30.1.312
  journal: Nucleic Acids Research
  preferred: true
  title: 'Transcription Regulatory Regions Database (TRRD): its status in 2002'
  year: '2002'
- authors:
  - Kolchanov NA
  - Podkolodnaya OA
  - Ananko EA
  - Ignatieva EV
  - Stepanenko IL
  - Kel-Margoulis OV
  - Kel AE
  - Merkulova TI
  - Goryachkovskaya TN
  - Busygina TV
  - Kolpakov FA
  - Podkolodny NL
  - Naumochkin AN
  - Korostishevskaya IM
  - Romashchenko AG
  - Overton GC
  doi: 10.1093/nar/28.1.298
  id: doi:10.1093/nar/28.1.298
  journal: Nucleic Acids Research
  title: 'Transcription Regulatory Regions Database (TRRD): its status in 2000'
  year: '2000'
- authors:
  - Kolchanov NA
  - Ananko EA
  - Podkolodnaya OA
  - Ignatieva EV
  - Stepanenko IL
  - Kel-Margoulis OV
  - Kel AE
  - Merkulova TI
  - Goryachkovskaya TN
  - Busygina TV
  - Kolpakov FA
  - Podkolodny NL
  - Naumochkin AN
  - Romashchenko AG
  doi: 10.1093/nar/27.1.303
  id: doi:10.1093/nar/27.1.303
  journal: Nucleic Acids Research
  title: 'Transcription Regulatory Regions Database (TRRD): its status in 1999'
  year: '1999'
rrid: SCR_005723
synonyms:
- TRRD
taxon:
- NCBITaxon:2759
version: '7.0'
---
# Transcription Regulatory Regions Database (TRRD)

TRRD is a manually curated database of eukaryotic gene transcription regulatory regions, built by Nikolay Kolchanov's group at the Institute of Cytology and Genetics (Siberian Branch of the Russian Academy of Sciences, Novosibirsk). It holds only experimentally confirmed data annotated from the literature: regulatory regions such as promoters, enhancers, silencers and locus control regions, the transcription factor binding sites within them, the binding transcription factors, and gene expression patterns. These are kept in linked libraries (TRRDGENES, TRRDUNITS, TRRDSITES, TRRDFACTORS, TRRDEXP, TRRDLCR, TRRDBIB, TRRDSTARTS) and searched through a Sequence Retrieval System (SRS) server.

The last release announced on the website is TRRD 7.0 (September 2005). The SRS libraries were last indexed in November 2015. The website and SRS server still answer queries but are no longer updated. TRRD is one of the sources of curated transcription factor to target gene interactions in TFactS.
