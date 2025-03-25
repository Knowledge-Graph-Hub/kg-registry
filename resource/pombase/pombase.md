---
layout: resource_detail
id: pombase
name: PomBase
contacts:
- category: Organization
  email: helpdesk@pombase.org
  label: PomBase
description: PomBase is a comprehensive database for the fission yeast Schizosaccharomyces pombe, providing structural and functional annotation, literature curation and access to large-scale data sets.
domain: organisms
homepage_url: https://www.pombase.org/
license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
products:
- id: pombase.genes
  description: Tab-delimited file of systematic ID, primary gene name (where assigned), and all synonyms for each gene
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names.tsv
  name: PomBase gene names
  category: Product
  format: tsv
  secondary_source:
  - pombase
  original_source:
  - pombase
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
- id: pombase.genes-products
  description: Tab-delimited file of systematic ID, primary gene name (where assigned), chromosome, product description, UniProtKB accession, all synonyms, and product type (protein coding, ncRNA, etc.) for each gene
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
  name: PomBase gene names and products
  category: Product
  format: tsv
  secondary_source:
  - pombase
  original_source:
  - uniprot
  - pombase
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
- id: pombase.to-uniprot
  description: Tab-delimited file with the PomBase systematic identifier for each protein-coding gene mapped to the corresponding UniProt accession number
  product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
  name: PomBase to UniProt map
  category: MappingProduct
  format: tsv
  secondary_source:
  - pombase
  original_source:
  - uniprot
  - pombase
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
repository: https://www.pombase.org/datasets
activity_status: active
category: Resource
---

PomBase
