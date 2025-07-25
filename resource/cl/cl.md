---
activity_status: active
category: DataModel
description: The Cell Ontology (CL) is a structured controlled vocabulary for cell types in animals. It serves as a comprehensive resource for model organism and bioinformatics databases, with over 2,700 cell type classes and rich integration with other biomedical ontologies.
domains:
- anatomy and development
- biomedical
- cellular biology
- bioinformatics
homepage_url: https://cell-ontology.github.io/
repository: https://github.com/obophenotype/cell-ontology
id: cl
layout: resource_detail
name: Cell Ontology
creation_date: '2025-07-22T00:00:00Z'
last_modified_date: '2025-07-22T00:00:00Z'
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contacts:
- category: Individual
  label: Alexander D. Diehl
  orcid: 0000-0001-9990-8331
  contact_details:
  - contact_type: email
    value: addiehl@buffalo.edu
  - contact_type: github
    value: addiehl
- category: Organization
  label: OBO Foundry
  contact_details:
  - contact_type: url
    value: https://obofoundry.org/
  - contact_type: github
    value: obophenotype
products:
- category: DataModelProduct
  description: The latest release of CL in OWL format with full imports and reasoning
  format: owl
  id: cl.owl
  name: CL OWL
  product_url: http://purl.obolibrary.org/obo/cl.owl
  license:
    id: http://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
- category: DataModelProduct
  description: The latest release of CL in OBO format with imports merged in
  format: obo
  id: cl.obo
  name: CL OBO
  product_url: http://purl.obolibrary.org/obo/cl.obo
  license:
    id: http://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
- category: DataModelProduct
  description: The latest release of CL in OBOGraph-JSON format with imports merged in
  format: json
  id: cl.json
  name: CL JSON
  product_url: http://purl.obolibrary.org/obo/cl.json
  license:
    id: http://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
- category: DataModelProduct
  description: Basic version of CL with no inter-ontology axioms (OWL format)
  format: owl
  id: cl.basic.owl
  name: CL Basic OWL
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.owl
  license:
    id: http://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
- category: DataModelProduct
  description: Basic version of CL with no inter-ontology axioms (OBO format)
  format: obo
  id: cl.basic.obo
  name: CL Basic OBO
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.obo
  license:
    id: http://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
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
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - do
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
publications:
- id: doi:10.1186/s13326-016-0088-7
  title: The Cell Ontology 2016 - enhanced content, modularization, and ontology interoperability
  authors:
  - Alexander D Diehl
  - Terrence F Meehan
  - Yvonne M Bradford
  - Matthew H Brush
  - Wasila M Dahdul
  - David S Dougall
  - Yongqun He
  - David Osumi-Sutherland
  - Bjoern Peters
  - Alan Ruttenberg
  - Sirarat Sarntivijai
  - Christian J Stoeckert Jr
  - Melissa A Haendel
  - Christopher J Mungall
  doi: 10.1186/s13326-016-0088-7
  journal: Journal of Biomedical Semantics
  year: 2016
  preferred: true
- id: doi:10.1186/1471-2105-12-6
  title: Logical development of the cell ontology
  authors:
  - Terrence F Meehan
  - Anna Maria Masci
  - Amina Abdulla
  - Lindsay G Cowell
  - Judith A Blake
  - Christopher J Mungall
  - Alexander D Diehl
  doi: 10.1186/1471-2105-12-6
  journal: BMC Bioinformatics
  year: 2011
- id: doi:10.1186/gb-2005-6-2-r21
  title: An ontology for cell types
  authors:
  - Jonathan Bard
  - Seung Y Rhee
  - Michael Ashburner
  doi: 10.1186/gb-2005-6-2-r21
  journal: Genome Biology
  year: 2005
---

# Cell Ontology (CL)

The Cell Ontology (CL) is a structured controlled vocabulary for cell types in animals. Created in 2004 and maintained as a core OBO Foundry ontology, it serves as a comprehensive resource for model organism and bioinformatics databases, with over 2,700 cell type classes and rich integration with other biomedical ontologies.

## Overview

CL provides a standardized classification of cell types across multiple species, focusing on animal cell types but offering high-level cell type classes that serve as mapping points for cell types in ontologies representing other species, such as plants. The ontology is designed to support annotation, data integration, and knowledge discovery in biomedical research.

## Integration with Other Ontologies

The Cell Ontology is tightly integrated with other biomedical ontologies:

- **Uberon**: Cell types in CL are linked to anatomical structures via part-of relationships
- **Gene Ontology (GO)**: Cell types are linked to biological processes via capable-of relationships
- **Other ontologies**: CL integrates with CHEBI, PR, PATO, and other ontologies in the OBO ecosystem

This integration enables rich cross-domain queries and annotations, making CL a central component in many biomedical knowledge representation systems.

## Applications and Adoption

The Cell Ontology has been widely adopted by major biomedical research initiatives and databases:

- **HuBMAP (Human BioMolecular Atlas Program)**: Uses CL for cell type annotation in human reference atlases
- **Human Cell Atlas (HCA)**: Uses CL to annotate cells in reference maps
- **CZ CELLxGENE**: Annotates all cell types according to CL in their single-cell transcriptomics platform
- **BRAIN Initiative Cell Census Network (BICCN)**: Uses CL as a foundation for the Brain Data Standards Ontology
- **Single Cell Expression Atlas**: Links cell types to CL terms
- **ENCODE (Encyclopedia of DNA Elements)**: Uses CL for sample annotation
- **FANTOM5**: Uses CL and Uberon to annotate samples for transcriptome analyses

## Technical Details

The Cell Ontology is distributed in multiple standard formats:
- OWL (RDF/XML)
- OBO format
- JSON (OBOGraphs)

It comes in multiple variants including:
- Full (all imports merged in, classified using a reasoner)
- Base (not pre-reasoned, only axioms belonging to the ontology)
- Simple (pre-reasoned, only CL classes)

All downloads are versioned with resolvable IRIs for persistent reference and access.

## Community and Development

CL is developed through an active community process with editors from multiple projects embedded in the team. The development follows FAIR principles (Findable, Accessible, Interoperable, Reusable) and is governed by OBO Foundry best practices.

Contributors can engage through the GitHub issue tracker, Slack channel, or mailing list. The ontology is continuously updated to meet the evolving needs of the biomedical research community.