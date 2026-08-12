---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: Dog10K Consortium
    contact_details:
      - contact_type: url
        value: http://www.dog10kgenomes.org/
creation_date: '2026-08-12T00:00:00Z'
description: An international consortium sequencing canine genomes across breeds, village dogs, and wild canids, producing a reference catalogue of canine genetic variation that serves as an imputation reference panel.
domains:
  - genomics
  - organisms
homepage_url: http://www.dog10kgenomes.org/
id: dog10k
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
name: Dog10K
products:
  - category: Product
    description: Variant call files and associated annotations from the Dog10K consortium, covering single nucleotide variants, copy number variants, and structural variants across sequenced canids.
    format: vcf
    id: dog10k.variants
    name: Dog10K variant files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dog10k
    product_url: https://kiddlabshare.med.umich.edu/dog10K/
  - category: Product
    description: An archived release of Dog10K variant data and annotations deposited on Zenodo.
    format: vcf
    id: dog10k.zenodo
    name: Dog10K variant data archive
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dog10k
    product_url: https://zenodo.org/record/8084059
  - category: GraphicalInterface
    description: The Dog10K database web interface, providing browsing of canine multi-omics data including variation, de novo mutations, single-cell RNA sequencing, and transcriptomic data.
    format: http
    id: dog10k.browser
    name: Dog10K database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dog10k
    product_url: https://dog10k.kiz.ac.cn/
publications:
  - id: https://doi.org/10.1186/s13059-023-03023-7
    doi: doi:10.1186/s13059-023-03023-7
    title: Genome sequencing of 2000 canids by the Dog10K consortium advances the understanding of demography, genome function and architecture
    journal: Genome Biology
    year: '2023'
    preferred: true
    authors:
      - Jennifer R. S. Meadows
      - Jeffrey M. Kidd
      - Guo-Dong Wang
      - Heidi G. Parker
      - Peter Z. Schall
      - Matteo Bianchi
      - Matthew J. Christmas
      - Katia Bougiouri
      - Reuben M. Buckley
      - Christophe Hitte
      - Anthony K. Nguyen
      - Chao Wang
      - Vidhya Jagannathan
      - Julia E. Niskanen
      - Laurent A. F. Frantz
      - Meharji Arumilli
      - Sruthi Hundi
      - Kerstin Lindblad-Toh
      - Catarina Ginja
      - Kadek Karang Agustina
      - Catherine André
      - Adam R. Boyko
      - Brian W. Davis
      - Michaela Drögemüller
      - Xin-Yao Feng
      - Konstantinos Gkagkavouzis
      - Giorgos Iliopoulos
      - Alexander C. Harris
      - Marjo K. Hytönen
      - Daniela C. Kalthoff
      - Yan-Hu Liu
      - Petros Lymberakis
      - Nikolaos Poulakakis
      - Ana Elisabete Pires
      - Fernando Racimo
      - Fabian Ramos-Almodovar
      - Peter Savolainen
      - Semina Venetsani
      - Imke Tammen
      - Alexandros Triantafyllidis
      - Bridgett vonHoldt
      - Robert K. Wayne
      - Greger Larson
      - Frank W. Nicholas
      - Hannes Lohi
      - Tosso Leeb
      - Ya-Ping Zhang
      - Elaine A. Ostrander
  - id: https://doi.org/10.1093/nar/gkae928
    doi: doi:10.1093/nar/gkae928
    title: 'Dog10K: an integrated Dog10K database summarizing canine multi-omics'
    journal: Nucleic Acids Research
    year: '2025'
    authors:
      - Tong Zhou
      - Shao-Yan Pu
      - Shao-Jie Zhang
      - Qi-Jun Zhou
      - Min Zeng
      - Jing-Sheng Lu
      - Xuemei Lu
      - Ya-Nan Wang
      - Guo-Dong Wang
taxon:
  - NCBITaxon:9615
---

Dog10K is an international consortium of canine genomics researchers formed to sequence 10,000 canids at high coverage, with the aim of uncovering the genetic basis of phenotypic diversity, disease, behavior, and domestication history in dogs.

The Dog10K.v1 release provides genome sequence data and analysis for 2,000 canids spanning hundreds of breeds, village dogs, and wild canids. The resulting variant catalogue is widely reused as a reference panel for imputing genome-wide genotypes from sparse genotyping arrays, which is the role it plays for CanVAS and, downstream of that, for the Sniff Atlas.

The Dog10K database additionally aggregates canine multi-omics data, including variation, de novo mutations from 404 trios, single-cell RNA sequencing, and transcriptomic data. Raw sequencing data are shared through the Genome Sequence Archive and the Sequence Read Archive.
