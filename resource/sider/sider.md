---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: michael.kuhn@gmail.com
  label: Michael Kuhn
- category: Organization
  label: European Molecular Biology Laboratory (EMBL)
description: SIDER (Side Effect Resource) contains information on marketed medicines
  and their recorded adverse drug reactions. The information is extracted from public
  documents and package inserts, including side effect frequency, drug and side effect
  classifications, and links to further information.
domains:
- biomedical
- pharmacology
- drug discovery
- health
homepage_url: http://sideeffects.embl.de/
id: sider
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC-BY-NC-4.0
name: SIDER
products:
- category: GraphicalInterface
  description: Web interface that allows searching and browsing drugs and their side
    effects.
  id: sider.web
  name: SIDER Web Interface
  product_url: http://sideeffects.embl.de/
- category: Product
  description: Tab-separated file mapping drugs to their names and synonyms.
  format: tsv
  id: sider.drug_names
  name: SIDER Drug Names
  product_url: http://sideeffects.embl.de/media/download/drug_names.tsv
- category: MappingProduct
  description: Tab-separated file mapping drugs to their ATC codes.
  format: tsv
  id: sider.drug_atc
  name: SIDER Drug ATC Codes
  product_url: http://sideeffects.embl.de/media/download/drug_atc.tsv
- category: Product
  compression: gzip
  description: Tab-separated file containing all drug indications extracted from drug
    labels using MedDRA terminology.
  format: tsv
  id: sider.meddra_all_indications
  name: SIDER MedDRA All Indications
  product_url: http://sideeffects.embl.de/media/download/meddra_all_indications.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated file containing all side effects extracted from drug
    labels using MedDRA terminology.
  format: tsv
  id: sider.meddra_all_se
  name: SIDER MedDRA All Side Effects
  product_url: http://sideeffects.embl.de/media/download/meddra_all_se.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated file containing side effect frequency information extracted
    from drug labels using MedDRA terminology.
  format: tsv
  id: sider.meddra_freq
  name: SIDER MedDRA Frequency
  product_url: http://sideeffects.embl.de/media/download/meddra_freq.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated file containing all original label indications extracted
    from drug labels using MedDRA terminology.
  format: tsv
  id: sider.meddra_all_label_indications
  name: SIDER MedDRA All Label Indications
  product_url: http://sideeffects.embl.de/media/download/meddra_all_label_indications.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated file containing all original label side effects extracted
    from drug labels using MedDRA terminology.
  format: tsv
  id: sider.meddra_all_label_se
  name: SIDER MedDRA All Label Side Effects
  product_url: http://sideeffects.embl.de/media/download/meddra_all_label_se.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated file mapping MedDRA terms to their concept ID.
  format: tsv
  id: sider.meddra
  name: SIDER MedDRA Dictionary
  product_url: http://sideeffects.embl.de/media/download/meddra.tsv.gz
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Kuhn M
  - Letunic I
  - Jensen LJ
  - Bork P
  doi: doi:10.1093/nar/gkv1075
  id: https://doi.org/10.1093/nar/gkv1075
  journal: Nucleic Acids Research
  preferred: true
  title: The SIDER database of drugs and side effects
  year: '2016'
- authors:
  - Kuhn M
  - Campillos M
  - Letunic I
  - Jensen LJ
  - Bork P
  doi: doi:10.1038/msb.2009.98
  id: https://doi.org/10.1038/msb.2009.98
  journal: Molecular Systems Biology
  title: A side effect resource to capture phenotypic effects of drugs
  year: '2010'
warnings:
- The last release for this resource was on October 21, 2015.
---
SIDER (Side Effect Resource) is a database of drugs and their side effects, which was developed at the European Molecular Biology Laboratory (EMBL). The database contains information extracted from public documents and package inserts, providing valuable data on marketed medicines and their recorded adverse drug reactions.

SIDER 4.1, released on October 21, 2015, contains information on 1,430 drugs and 5,868 side effects, totaling 139,756 drug-side effect pairs. The database uses the MedDRA dictionary (version 16.1) to standardize side effect terminology and provides access to both preferred terms and lower-level terms.

The database includes:
- Drug information (names, ATC codes)
- Side effect information (MedDRA terms)
- Frequency information for side effects
- Indications for drugs
- Classifications of drugs and side effects
- Links to further information (e.g., drug-target relations)

SIDER is linked to other databases like STITCH and PubChem through compound identifiers, allowing for integration with other biomedical resources.

The project is no longer actively maintained or updated as it lacks funding for further development. The most recent data is from 2015 and is therefore considered out of date. However, the resource remains valuable for historical research and as a reference for drug side effect data.