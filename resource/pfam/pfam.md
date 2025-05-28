---
layout: resource_detail
activity_status: active
id: pfam
name: Pfam
description: Pfam is a large collection of protein families, each represented by multiple sequence alignments and hidden Markov models (HMMs), providing annotations of protein domains and functional sites.
domains:
- proteomics
- genomics
- structural biology
- biological systems
- bioinformatics
category: DataSource
contacts:
- category: Organization
  label: "European Bioinformatics Institute (EMBL-EBI)"
  contact_details:
  - contact_type: email
    value: pfam-help@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/support/pfam
homepage_url: https://www.ebi.ac.uk/interpro/entry/pfam/
repository: ""
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: "Creative Commons Zero (CC0)"
version: "37.0"
publications:
- id: https://doi.org/10.1093/nar/gkae997
  title: "The Pfam protein families database: embracing AI/ML"
  authors:
  - "T. Paysan-Lafosse"
  - "A. Andreeva"
  - "M. Blum"
  - "S. Chuguransky"
  - "T. Grego"
  - "B. Lazaro Pinto"
  - "G.A. Salazar"
  - "M.L. Bileschi"
  - "F. Llinares-López"
  - "L. Meng-Papaxanthos"
  - "L.J. Colwell"
  - "NV. Grishin"
  - "R.D. Schaeffer"
  - "D.Clementel"
  - "S.C.E Tosatto"
  - "E. Sonnhammer"
  - "V. Wood"
  - "A. Bateman"
  journal: "Nucleic Acids Research"
  year: "2024"
  preferred: true
- id: https://doi.org/10.1093/nar/gkaa913
  title: "Pfam: The protein families database in 2021"
  authors:
  - "J. Mistry"
  - "S. Chuguransky"
  - "L. Williams"
  - "M. Qureshi"
  - "G.A. Salazar"
  - "E.L.L. Sonnhammer"
  - "S.C.E. Tosatto"
  - "L. Paladin"
  - "S. Raj"
  - "L.J. Richardson"
  - "R.D. Finn"
  - "A. Bateman"
  journal: "Nucleic Acids Research"
  year: "2020"
- id: https://doi.org/10.1093/nar/gky995
  title: "The Pfam protein families database in 2019"
  authors:
  - "S. El-Gebali"
  - "J. Mistry"
  - "A. Bateman"
  - "S.R. Eddy"
  - "A. Luciani"
  - "S.C. Potter"
  - "M. Qureshi"
  - "L.J. Richardson"
  - "G.A. Salazar"
  - "A. Smart"
  - "E.L.L. Sonnhammer"
  - "L. Hirsh"
  - "L. Paladin"
  - "D. Piovesan"
  - "S.C.E. Tosatto"
  - "R.D. Finn"
  journal: "Nucleic Acids Research"
  year: "2019"
products:
- id: pfam.site
  name: Interface for the Pfam Database
  description: "The core Pfam database containing protein families, multiple sequence alignments, and hidden Markov models."
  category: GraphicalInterface
  product_url: https://www.ebi.ac.uk/interpro/entry/pfam/#table
- id: pfam.a.models
  name: Pfam-A HMM Library
  description: "The Pfam HMM library for Pfam-A families, used for searching protein sequences against Pfam."
  category: Product
  product_url: https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz
- id: pfam.a.data
  name: Pfam-A HMM data
  description: "The Pfam HMM data for Pfam-A families, used for searching protein sequences against Pfam."
  category: Product
  product_url: https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz
- id: pfam.a.seedalignment
  name: Pfam-A Seed alignment
  description: "Pfam-A Seed alignment."
  category: Product
  product_url: https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.seed.gz
- id: pfam.a.fullalignment
  name: Pfam-A Full alignment
  description: "Pfam-A Full alignment."
  category: Product
  product_url: https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.full.gz
- id: pfam.api
  name: InterPro API
  description: "REST API for programmatic access to Pfam data via the InterPro database."
  category: ProgrammingInterface
  product_url: https://www.ebi.ac.uk/interpro/api/
  format: json
funding:
- id: welcome_trust
  label: "Wellcome Trust"
- id: bbsrc
  label: "Biotechnology and Biological Sciences Research Council (BBSRC)"
- id: embl
  label: "European Molecular Biology Laboratory (EMBL)"
- id: hhmi
  label: "Howard Hughes Medical Institute (HHMI)"
---

Pfam is a large collection of protein families, each represented by multiple sequence alignments and profile hidden Markov models (HMMs). Proteins are generally composed of one or more functional regions, commonly termed domains. The presence of different domains in varying combinations in different proteins gives rise to the diverse repertoire of proteins found in nature. Identifying the domains present in a protein can provide insights into its function.

Each Pfam family, usually referred to as a Pfam-A entry, consists of a curated seed alignment containing a small set of representative members of the family, profile HMMs built from the seed alignment, and an automatically generated full alignment, which contains all detectable protein sequences belonging to the family, as defined by profile HMM searches of primary sequence databases.

Pfam entries are classified into several types:
- Family: A collection of related proteins
- Domain: A structural unit that can be found in multiple protein contexts
- Repeat: A short unit that is unstable in isolation but forms a stable structure when multiple copies are present
- Motif: A short unit found outside globular domains
- Coiled-coil: A region that forms a coiled-coil structure
- Disordered: A region that is disordered in the native state

Pfam also groups related entries into clans, which are collections of Pfam entries related by sequence, structure, or profile HMM. This is particularly useful for capturing relationships between divergent families that may have a common evolutionary origin.

Pfam version 37.0 is based on UniProt release 2023_05. The database is now maintained as part of the InterPro database at the European Bioinformatics Institute (EMBL-EBI). Pfam is powered by the HMMER3 package developed by Sean Eddy's group at HHMI/Harvard University.

The database is freely available under the Creative Commons Zero (CC0) license and can be accessed through the InterPro website or downloaded from the FTP site.
