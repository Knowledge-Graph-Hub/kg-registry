---
activity_status: active
category: Resource
contacts:
- category: Organization
  email: helpdesk@pombase.org
  label: PomBase
description: PomBase is a comprehensive database for the fission yeast Schizosaccharomyces
  pombe, providing structural and functional annotation, literature curation and access
  to large-scale data sets.
domains:
- organisms
homepage_url: https://www.pombase.org/
id: pombase
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: PomBase
products:
- category: Product
  description: Tab-delimited file of systematic ID, primary gene name (where assigned),
    and all synonyms for each gene
  format: tsv
  id: pombase.genes
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase gene names
  original_source:
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names.tsv
  secondary_source:
  - pombase
- category: Product
  description: Tab-delimited file of systematic ID, primary gene name (where assigned),
    chromosome, product description, UniProtKB accession, all synonyms, and product
    type (protein coding, ncRNA, etc.) for each gene
  format: tsv
  id: pombase.genes-products
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase gene names and products
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Tab-delimited file with the PomBase systematic identifier for each
    protein-coding gene mapped to the corresponding UniProt accession number
  format: tsv
  id: pombase.to-uniprot
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase to UniProt map
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
  secondary_source:
  - pombase
repository: https://www.pombase.org/datasets
---
PomBase