---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: finngen-info@helsinki.fi
  label: FinnGen
creation_date: '2025-06-27T00:00:00Z'
description: FinnGen is a large-scale genomics research project aimed at improving
  human health through genetic insights from the genetically unique Finnish population,
  combining genome information with digital health record data from 500,000 Finnish
  biobank participants.
domains:
- genomics
- biomedical
- precision medicine
- clinical
homepage_url: https://www.finngen.fi/en
id: finngen
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: FinnGen
products:
- category: Product
  description: Summary statistics from genome-wide association studies of various
    disease phenotypes conducted on Finnish population data, with the most recent
    release being Data Freeze 13.
  id: finngen.summary_stats
  name: FinnGen GWAS Summary Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: finngen
  product_url: https://www.finngen.fi/en/access_results
- category: GraphicalInterface
  description: A web service for browsing disease endpoints in FinnGen, including
    statistics, definitions, and relationships between diseases.
  format: http
  id: finngen.risteys
  name: Risteys
  original_source:
  - relation_type: prov:hadPrimarySource
    source: finngen
  product_url: https://risteys.finngen.fi/
- category: Product
  description: Results from meta-analysis of FinnGen data with other major biobanks,
    allowing for more powerful detection of genetic associations.
  id: finngen.meta_analysis
  name: FinnGen Meta-Analysis Results
  original_source:
  - relation_type: prov:hadPrimarySource
    source: finngen
  product_url: https://www.finngen.fi/en/access_results
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  format: http
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
- category: Product
  description: Clinical endpoint definitions and control groups for FinnGen data releases,
    including detailed documentation for each data freeze.
  id: finngen.endpoints
  name: FinnGen Clinical Endpoints
  original_source:
  - relation_type: prov:hadPrimarySource
    source: finngen
  product_url: https://www.finngen.fi/en/researchers/clinical-endpoints
publications:
- authors:
  - Sean J. Jurgens
  - "Joel T. R\xE4m\xF6"
  - Daria R. Kramarenko
  - Leonoor F. J. M. Wijdeveld
  - Jan Haas
  - Mark D. Chaffin
  - Sophie Garnier
  - Liam Gaziano
  - Lu-Chen Weng
  - Alex Lipov
  - Sean L. Zheng
  - Albert Henry
  - Jennifer E. Huffman
  - Saketh Challa
  - "Frank R\xFChle"
  - Carmen Diaz Verdugo
  - "Christian Krijger Ju\xE1rez"
  - Shinwan Kany
  - Constance A. van Orsouw
  - Kiran Biddinger
  - Edwin Poel
  - Amanda L. Elliott
  - Xin Wang
  - Catherine Francis
  - Richard Ruan
  - Satoshi Koyama
  - Leander Beekman
  - Dominic S. Zimmerman
  - "Jean-Fran\xE7ois Deleuze"
  - Eric Villard
  - "David-Alexandre Tr\xE9gou\xEBt"
  - Richard Isnard
  - Dorret I. Boomsma
  - Eco J. C. de Geus
  - Rafik Tadros
  - Yigal M. Pinto
  - Arthur A. M. Wilde
  - Jouke-Jan Hottenga
  - Juha Sinisalo
  - Teemu Niiranen
  - Roddy Walsh
  - Amand F. Schmidt
  - Seung Hoan Choi
  - Kyong-Mi Chang
  - Philip S. Tsao
  - Paul M. Matthews
  - James S. Ware
  - R. Thomas Lumbers
  - Saskia van der Crabben
  - Jari Laukkanen
  - Aarno Palotie
  - Ahmad S. Amin
  - Philippe Charron
  - Benjamin Meder
  - Patrick T. Ellinor
  - Mark Daly
  - Krishna G. Aragam
  - Connie R. Bezzina
  doi: 10.1038/s41588-024-01975-5
  id: doi:10.1038/s41588-024-01975-5
  journal: Nature Genetics
  title: Genome-wide association study reveals mechanisms underlying dilated cardiomyopathy
    and myocardial resilience
  year: '2024'
- authors:
  - Vilma Lammi
  - Tomoko Nakanishi
  - Samuel E. Jones
  - Shea J. Andrews
  - Juha Karjalainen
  - "Beatriz Cort\xE9s"
  - "Heath E. O\u2019Brien"
  - Ana Ochoa-Guzman
  - Brian E. Fulton-Howard
  - Martin Broberg
  - Hele H. Haapaniemi
  - Masahiro Kanai
  - Matti Pirinen
  - Axel Schmidt
  - Ruth E. Mitchell
  - Abdou Mousas
  - Massimo Mangino
  - Alicia Huerta-Chagoya
  - Nasa Sinnott-Armstrong
  - Elizabeth T. Cirulli
  - Marc Vaudel
  - Alex S. F. Kwong
  - Amit K. Maiti
  - Minttu M. Marttila
  - Daniel C. Posner
  - Alexis A. Rodriguez
  - Chiara Batini
  - Francesca Minnai
  - Anna R. Dearman
  - C. A. Robert Warmerdam
  - Celia B. Sequeros
  - Thomas W. Winkler
  - Daniel M. Jordan
  - "Raimonds Re\u0161cenko"
  - Lorenzo Miano
  - Jacqueline M. Lane
  - Ryan K. Chung
  - Beatriz Guillen-Guio
  - Olivia C. Leavy
  - Laura Carvajal-Silva
  - "Kevin Aguilar-Vald\xE9s"
  - Erika Frangione
  - Lindsay Guare
  - Ekaterina Vergasova
  - Eirini Marouli
  - Pasquale Striano
  - Ummu Afeera Zainulabid
  - Ashutosh Kumar
  - Hajar Fauzan Ahmad
  - Ryuya Edahiro
  - Shuhei Azekawa
  - Mari E. K. Niemi
  - Janick St-Cyr
  - Darin Adra
  - Madeleine Durand
  - David Bujold
  - Guillaume Bourque
  - Ariane Boisclair
  - Mylene Bertrand
  - Daniel Auld
  - Laetitia Laurent
  - Solomia Yanishevsky
  - G. Mark Lathrop
  - Fangyi Shi
  - Simon Rousseau
  - Jiannis Ragoussis
  - Danielle Perley
  - Vincent Mooser
  - David R. Morrison
  - Daniella Balla
  - Julia Heggemann
  - Sonja Schultz
  - Pari Behzad
  - "Markus M. N\xF6then"
  - Abigail Miller
  - Max C. Pensel
  - Carlo Maj
  - Kelly Cho
  - Tianxi Cai
  - Sudha K. Iyengar
  - Carlos A. Aguilar Salinas
  - Seung Hyuk T. Lee
  - Hortensia Moreno-Macias
  - "P\xE4ivi Pajukanta"
  - Michelle Duran-Gomez
  - Lill Trogstad
  - Daniel J. Rader
  - Marylyn D. Ritchie
  - Anurag Verma
  - Colleen M. Kripke
  - Sergi Papiol
  - Jens Wiltfang
  - Jochen Schneider
  - Thomas G. Schulze
  - Christof Winter
  - Ewa Wallin
  - Robert Frithiof
  - Fanny Senner
  - Christoph D. Spinner
  - Ulrike Protzer
  - Mattia Cordioli
  - Nikola S. Mueller
  - Andreas Dinkel
  - Janos L. Kalman
  - Tomislav Maricic
  - Kristina Adorjan
  - Miklos Lipcsey
  - Lisa Fricke
  - Ing-Marie Larsson
  - Urs Heilbronner
  - Monika Budde
  - Johanna Erber
  - Nicholas R. Harvey
  - Vince Forgetta
  - Benedict Hignell
  - Yolanda Espinosa-Parrilla
  - Juan M. Saez Hidalgo
  - Estefania Nova-Lamperti
  - "Scarlett Guti\xE9rrez-Richards"
  - Gerardo Donoso
  - Leslie C. Cerpa
  - Cesar A. Echeverria
  - Camilo Cabrera
  - Pamela Bocchieri
  - Macarena Fuentes-Guajardo
  - "Christian A. Mu\xF1oz"
  - "Karen Y. Or\xF3stica"
  - Alvaro Figueroa
  - Lissette G. Guajardo
  - Iskra A. Signore
  - "Virginia A. Monardes-Ram\xEDrez"
  - Eduardo A. Tobar-Calfucoy
  - "Luis A. Qui\xF1ones"
  - "Cristian E. Y\xE1\xF1ez"
  - Daniela Zapata-Contreras
  - "Paula Zu\xF1iga-Pacheco"
  - Romina Quiroga
  - "Mat\xEDas F. Mart\xEDnez"
  - Teresa A. Alarcon
  - Andrea X. Silva
  - Carolina S. Selman
  - Sergio Sanhueza
  - "Roc\xEDo Retamales-Ortega"
  - "Tamara V. Ar\xE9valo"
  - Eduardo Lamoza
  - "H\xE9ctor Valenzuela-Jorquera"
  - Maria Sophia Donaire
  - Sannidhi Sarvadhavabhatla
  - Sisse R. Ostrowski
  - "S\xF8ren Brunak"
  - David Westergaard
  - Bjarke Feenstra
  - Anne Sofie B. Mortensen
  - Anna L. Guyatt
  - Rafael de Cid
  - "Susana Iraola-Guzm\xE1n"
  - Gemma Moncunill
  - Alba Blasco
  - Judith Garcia-Aymerich
  - Natalia Blay
  - "Carlota Doba\xF1o"
  - Anna Carreras
  - "Xavier Farr\xE9"
  - Manolis Kogevinas
  - "Gemma Casta\xF1o-Vinyals"
  - Simone Furini
  - Chiara Fallerini
  - Kristina Zguro
  - Margherita Baldassarri
  - Francesca Colombo
  - Thompson Hannah
  - Anna Ilinskaya
  - Michil Trofimov
  - Layal Shaheen
  - Nikolay Plotnikov
  - Anna Kim
  - Dmitrii Kharitonov
  - Valery Ilinsky
  - Alexei Kamelin
  - Francisco Tanudjaja
  - Efren Sandoval
  - Nicole L. Washington
  - Simon White
  - Iva Neveux
  - Shaun Dabe
  - Alexandre Bolze
  - Kelly M. Schiabor Barrett
  - Eirini Christaki
  - Haralampos Milionis
  - Ioanna Tzoulaki
  - Angelos Liontos
  - Evangelos Evangelou
  - Evangelia Ntzani
  - Rasoul Aliannejad
  - Vahideh Zarei
  - Nastaran Soltani
  - Bahareh Sharififard
  - Hengameh Ansari Tadi
  - Ali Amirsavadkouhi
  - Ho NamKoong
  - Ryan C. Thompson
  - Alexander W. Charney
  - Laura G. Sloofman
  - Nicole W. Simons
  - Olga Vishnyakova
  - Xu Xinyi
  - Jennifer Taher
  - Lloyd T. Elliott
  - Vita Rovite
  - Peculis Raitis
  - Monta Briviba
  - "Janis Klovin\u0161"
  - Richa Saxena
  - Angus C. Burns
  - Jakob M. Cherry
  - Matthew Maher
  - Arne Kukkonen
  - Mauro Tettamanti
  - Luisa Ronzoni
  - Daniele Prati
  - Flora Peyvandi
  - Rossana Carpani
  - Antonio Muscatello
  - Sara Margarita
  - Francesco Malvestiti
  - Giuseppe Lamorte
  - Marco Mantero
  - Andre Franke
  - David Ellinghaus
  - Nathalie Iannotti
  - Nicola Montano
  - Alessandro Nobili
  - Frauke Degenhardt
  - Alessandra Bandera
  - Fabio Blandini
  - Francesco Bruno Arturo Blasi
  - Tom Hemming Karlsen
  - Shiuh-Wen Luoh
  - Christian Erikstrup
  - Ole B. V. Pedersen
  - Jordan Lerner-Ellis
  - Alicia Colombo
  - Joseph J. Grzymski
  - Makoto Ishii
  - Yukinori Okada
  - Noam D. Beckmann
  - Meena Kumari
  - Ralf Wagner
  - Iris M. Heid
  - Catherine John
  - Patrick J. Short
  - Per Magnus
  - Laura Ansone
  - Luca V. C. Valenti
  - Sulggi A. Lee
  - Louise V. Wain
  - Ricardo A. Verdugo
  - Karina Banasik
  - Frank Geller
  - Lude H. Franke
  - Alexander Rakitko
  - Emma L. Duncan
  - Alessandra Renieri
  - Konstantinos K. Tsilidis
  - Rafael de Cid
  - Ahmadreza Niavarani
  - Erik Abner
  - "Teresa Tusi\xE9-Luna"
  - Shefali S. Verma
  - George Davey Smith
  - Nicholas J. Timpson
  - Ravi K. Madduri
  - Kelly Cho
  - Mark J. Daly
  - Andrea Ganna
  - Eva C. Schulte
  - J. Brent Richards
  - Kerstin U. Ludwig
  - "Michael Marks-Hultstr\xF6m"
  - Hugo Zeberg
  - Hanna M. Ollila
  doi: 10.1038/s41588-025-02100-w
  id: doi:10.1038/s41588-025-02100-w
  journal: Nature Genetics
  title: Genome-wide association study of long COVID
  year: '2025'
taxon:
- NCBITaxon:9606
---
# FinnGen

FinnGen is a large-scale public-private partnership research project combining genome information with digital health record data from Finnish biobanks and health registries. The project aims to improve human health through genetic research and advance the development of personalized medicine.

## About FinnGen

FinnGen is one of the world's leading biobank studies, with the goal of collecting and analyzing genome and health data from 500,000 Finnish biobank participants. The unique genetic makeup of the Finnish population, characterized by genetic isolation and bottleneck effects, makes it particularly valuable for identifying rare genetic variants associated with diseases.

The project is coordinated by the University of Helsinki and includes:
- All Finnish public biobanks
- Finnish universities
- Hospital districts
- International pharmaceutical companies
- Finnish research institutes

## Key Features

### Comprehensive Health Record Data

FinnGen combines genotype data with extensive digital health record data from national health registries, covering:
- Hospital visits and diagnoses
- Medication purchases and prescriptions
- Surgical procedures
- Cancer registry data
- Death registry data

This comprehensive longitudinal data, sometimes spanning decades for individual participants, enables powerful phenotype analyses across a wide range of diseases and conditions.

### Data Freezes

FinnGen regularly releases data in "freezes" as the project progresses, with each release including more samples and updated analyses:

- **Current Release**: Data Freeze 13 (DF13) - The most recent data release includes detailed clinical endpoint definitions and comprehensive GWAS results
- **Previous Releases**: Data Freezes 2-12 - Each with varying numbers of participants, genotyped variants, and phenotype endpoints

### Clinical Endpoints

The project has developed a significant collection of meaningful clinical endpoints based on digital health record data from Finnish health registries. These endpoints are carefully defined to enable precise genetic association studies across many disease categories.

## Applications and Impact

FinnGen data has been used in hundreds of scientific publications, contributing to the understanding of:

1. **Disease Mechanisms**: Identifying genetic factors contributing to common and rare diseases
2. **Drug Target Discovery**: Finding potential therapeutic targets for various conditions
3. **Genetic Risk Prediction**: Developing and validating polygenic risk scores
4. **Population Genetics**: Understanding the genetic structure and history of Finnish populations
5. **Pharmacogenomics**: Studying how genetic variation affects drug response

## Data Access

FinnGen follows the principles of open science and makes its data accessible to the research community while respecting privacy regulations:

1. **Summary Statistics**: Publicly available GWAS summary statistics for hundreds of phenotypes
2. **Risteys**: A public web interface for browsing phenotype information and summary statistics
3. **Controlled Access**: More detailed data available for qualified researchers through application

## Related Resources

FinnGen data is frequently used in combination with other biobanks and genetic resources, including:
- UK Biobank
- Estonian Biobank
- BioBank Japan
- Million Veteran Program