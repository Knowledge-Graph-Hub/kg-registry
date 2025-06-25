---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: efo-users@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/spot/ontology/
  label: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)
description: The Experimental Factor Ontology (EFO) provides a systematic description
  of many experimental variables available in EBI databases, and for projects such
  as the GWAS catalog. It combines parts of several biological ontologies, such as
  UBERON anatomy, ChEBI chemical compounds, and Cell Ontology.
domains:
- biological systems
- biomedical
- health
- phenotype
homepage_url: https://www.ebi.ac.uk/efo/
id: efo
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache 2.0
name: Experimental Factor Ontology
products:
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
- category: GraphicalInterface
  description: Browse EFO with EBI's Ontology Lookup Service (OLS)
  format: http
  id: efo.ols
  name: EFO in OLS
  original_source:
  - efo
  product_url: https://www.ebi.ac.uk/ols/ontologies/efo
  secondary_source:
  - efo
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
publications:
- authors:
  - James Malone
  - Ele Holloway
  - Tomasz Adamusiak
  - Misha Kapushesky
  - Jie Zheng
  - Nikolay Kolesnikov
  - Anna Zhukova
  - Alvis Brazma
  - Helen Parkinson
  doi: doi:10.1093/bioinformatics/btq099
  id: https://doi.org/10.1093/bioinformatics/btq099
  journal: Bioinformatics
  preferred: true
  title: Modeling Sample Variables with an Experimental Factor Ontology
  year: '2010'
repository: https://github.com/EBISPOT/efo
---
# Experimental Factor Ontology

The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases and for projects such as the NHGRI-EBI GWAS catalog. It combines parts of several biological ontologies, such as UBERON anatomy, ChEBI chemical compounds, Cell Ontology, and most recently, the Monarch Disease Ontology (MONDO).

The scope of EFO is to support the annotation, analysis, and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets. EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT). 

EFO has undergone significant restructuring in version 3, particularly in the disease branch, to improve classification based on current medical understanding and alignment with existing domain ontologies. This was achieved through mapping the EFO disease and disease staging branches to the Monarch Disease Ontology (MONDO).

EFO is actively maintained with regular releases available through its GitHub repository. It is widely used in biomedical resources including:

- Open Targets platform
- Gene Expression Atlas
- ArrayExpress
- And many other EBI databases and external resources

Users can browse EFO through the EBI's Ontology Lookup Service (OLS), submit new terms through GitHub issues, and download the latest release in various formats including OWL and OBO.