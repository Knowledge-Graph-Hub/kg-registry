---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://dbarchive.biosciencedbc.jp/en/open-tggates/desc.html
  label: Toxicogenomics Informatics Project, National Institutes of Biomedical Innovation,
    Health and Nutrition (NIBIOHN)
creation_date: '2026-10-05T00:00:00Z'
description: Open TG-GATEs is the public release of the toxicogenomics database built
  by the Japanese Toxicogenomics Project (TGP, 2002-2007) and Toxicogenomics Informatics
  Project (TGP2, 2007-2012), collaborations of the National Institute of Biomedical
  Innovation, the National Institute of Health Sciences and Japanese pharmaceutical
  companies. It covers 170 compounds, with Affymetrix microarray gene expression data
  (CEL files) from rat liver and kidney in vivo (single and repeated dosing) and from
  rat and human primary hepatocytes in vitro, linked to pathology, hematology, blood
  biochemistry, organ and body weight, and cell viability data. The original site is
  offline; the data were last updated in 2012 and are preserved in the NBDC LSDB Archive
  and in ArrayExpress.
domains:
- toxicology
- pharmacology
- genomics
- gene expression profiling
homepage_url: https://dbarchive.biosciencedbc.jp/en/open-tggates/desc.html
id: open-tggates
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/2.1/jp/
  label: CC BY-SA 2.1 JP
name: Open TG-GATEs
products:
- category: GraphicalInterface
  description: NBDC LSDB Archive page for Open TG-GATEs, with the database description,
    license terms, update history and links to the downloadable files and TogoDB simple
    search tables.
  format: http
  id: open-tggates.archive
  name: Open TG-GATEs LSDB Archive Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_url: https://dbarchive.biosciencedbc.jp/en/open-tggates/download.html
- category: Product
  description: Download directory of the archived Open TG-GATEs release (2012), containing
    the README, zipped CSV/TSV attribute tables and per-compound zip archives of CEL
    files organized by species, in vivo or in vitro, organ and dosing regimen.
  format: mixed
  id: open-tggates.download
  name: Open TG-GATEs Download Directory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/
- category: Product
  compression: zip
  description: Affymetrix GeneChip CEL files (Rat Genome 230 2.0 and Human Genome U133
    Plus 2.0 arrays) from rat liver and kidney in vivo and rat and human hepatocytes
    in vitro, packaged as one zip archive per compound and study design (about 12 GB
    for the rat data alone).
  format: mixed
  id: open-tggates.cel-files
  name: Open TG-GATEs Gene Expression Data (CEL Files)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/Rat/
- category: Product
  compression: zip
  description: Combined attribute table for all CEL files, with compound, dose, time
    point, sample and toxicological measurements for each array, as a single TSV file.
  format: tsv
  id: open-tggates.all-attributes
  name: Open TG-GATEs CEL File Attachments (All Attributes)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_file_size: 1801847
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/Open-tggates_AllAttribute.zip
- category: Product
  compression: zip
  description: List of the 170 Open TG-GATEs compounds with abbreviations, compound
    numbers and links to the CEL file archives for each study design, as a CSV file.
  format: csv
  id: open-tggates.compounds
  name: Open TG-GATEs Compound List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_file_size: 6589
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/open_tggates_main.zip
- category: Product
  compression: zip
  description: Histopathological findings for liver and kidney samples from the rat
    in vivo studies, with finding type, topography and severity grade, as a CSV file.
  format: csv
  id: open-tggates.pathology
  name: Open TG-GATEs Pathological Items
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_file_size: 91525
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/open_tggates_pathology.zip
- category: Product
  compression: zip
  description: Blood biochemistry measurements for the rat in vivo studies, as a CSV
    file.
  format: csv
  id: open-tggates.biochemistry
  name: Open TG-GATEs Biochemistry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_file_size: 682051
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/open_tggates_biochemistry.zip
- category: Product
  compression: zip
  description: Hematology measurements for the rat in vivo studies, as a CSV file.
  format: csv
  id: open-tggates.hematology
  name: Open TG-GATEs Hematology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_file_size: 651798
  product_url: https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/open_tggates_hematology.zip
- category: GraphicalInterface
  description: TogoDB table view of the Open TG-GATEs compound list, one of the simple
    search and download interfaces the NBDC provides for each archived Open TG-GATEs
    table.
  format: http
  id: open-tggates.togodb
  name: Open TG-GATEs TogoDB Simple Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_url: http://togodb.biosciencedbc.jp/togodb/view/open_tggates_main
- category: Product
  description: ArrayExpress record E-MTAB-797, Open TG-GATEs gene expression data from
    rat primary hepatocytes treated in vitro (Affymetrix Rat Genome 230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-in-vitro
  name: Open TG-GATEs in ArrayExpress (Rat In Vitro)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-797
- category: Product
  description: ArrayExpress record E-MTAB-798, Open TG-GATEs gene expression data from
    human primary hepatocytes treated in vitro (Affymetrix Human Genome U133 Plus 2.0).
  format: http
  id: open-tggates.arrayexpress-human-in-vitro
  name: Open TG-GATEs in ArrayExpress (Human In Vitro)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-798
- category: Product
  description: ArrayExpress record E-MTAB-799, Open TG-GATEs gene expression data from
    rat liver and kidney after single-dose in vivo exposure (Affymetrix Rat Genome
    230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-single-dose
  name: Open TG-GATEs in ArrayExpress (Rat In Vivo Single Dose)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-799
- category: Product
  description: ArrayExpress record E-MTAB-800, Open TG-GATEs gene expression data from
    rat liver and kidney after repeated-dose in vivo exposure (Affymetrix Rat Genome
    230 2.0).
  format: http
  id: open-tggates.arrayexpress-rat-repeat-dose
  name: Open TG-GATEs in ArrayExpress (Rat In Vivo Repeated Dose)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-800
- category: Product
  description: BioImage Archive study S-BIAD501 (released 2022), Open TG-GATEs rat
    liver and kidney histopathology slide images, each linked to its histopathology
    finding with mapped ontology terms and severity grade as recorded in ChEMBL.
  format: http
  id: open-tggates.histopathology-images
  license:
    id: https://creativecommons.org/licenses/by-sa/2.1/jp/
    label: CC BY-SA 2.1 JP
  name: Open TG-GATEs Histopathology Images
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:wasInfluencedBy
    source: chembl
  product_url: https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD501
- category: GraphicalInterface
  description: Original Open TG-GATEs web site of the Toxicogenomics Informatics Project,
    which offered search by compound name or pathological finding and CEL file download.
  format: http
  id: open-tggates.original-site
  name: Open TG-GATEs Original Web Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  product_url: http://toxico.nibiohn.go.jp/
  warnings:
  - Could not be retrieved when checked on 2026-10-05 because the host name toxico.nibiohn.go.jp
    no longer resolves. The data are available from the NBDC LSDB Archive.
publications:
- authors:
  - Yoshinobu Igarashi
  - Noriyuki Nakatsu
  - Tomoya Yamashita
  - Atsushi Ono
  - Yasuo Ohno
  - Tetsuro Urushidani
  - Hiroshi Yamada
  doi: 10.1093/nar/gku955
  id: doi:10.1093/nar/gku955
  journal: Nucleic Acids Research
  preferred: true
  title: 'Open TG-GATEs: a large-scale toxicogenomics database'
  year: '2015'
synonyms:
- TG-GATEs
- Toxicogenomics Project-Genomics Assisted Toxicity Evaluation System
taxon:
- NCBITaxon:10116
- NCBITaxon:9606
---
# Open TG-GATEs

Open TG-GATEs (Toxicogenomics Project-Genomics Assisted Toxicity Evaluation system) is the public part of TG-GATEs, the toxicogenomics database of the Japanese Toxicogenomics Project (TGP, 2002-2007) and its successor, the Toxicogenomics Informatics Project (TGP2, 2007-2012). In these projects, compounds (mostly drugs) were given to rats or applied to rat and human primary hepatocytes, and gene expression was measured with Affymetrix GeneChips alongside conventional toxicology endpoints.

## Contents

The release covers 170 compounds across six study designs: human hepatocytes in vitro, rat hepatocytes in vitro, and rat liver and kidney in vivo after single or repeated dosing. For each study the database provides:

- Gene expression data as CEL files (Rat Genome 230 2.0 and Human Genome U133 Plus 2.0 arrays)
- Histopathological findings with severity grades
- Hematology, blood biochemistry, body weight, organ weight and food consumption
- Cell viability data for the in vitro studies

## Availability

The original site at toxico.nibiohn.go.jp went live in 2011 and was last updated in January 2012. It is offline as of 2026-10-05. The full release is preserved in the NBDC LSDB Archive (DOI [10.18908/lsdba.nbdc00954-01-000](https://doi.org/10.18908/lsdba.nbdc00954-01-000)) as zipped CSV/TSV tables and per-compound CEL file archives, with TogoDB views for simple search. The expression data are also in ArrayExpress (E-MTAB-797, E-MTAB-798, E-MTAB-799 and E-MTAB-800), and the histopathology slide images are in the BioImage Archive (S-BIAD501).

The data are licensed under CC BY-SA 2.1 Japan, with an additional license that requires derived works to carry these license terms and requires publications to cite the database by name and URL.
