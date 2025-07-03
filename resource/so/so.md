---
activity_status: active
category: DataModel
contacts:
- category: Individual
  orcid: 0000-0002-0831-6427
  contact_details:
  - contact_type: email
    value: keilbeck@genetics.utah.edu
  - contact_type: github
    value: keilbeck
  label: Karen Eilbeck
description: The Sequence Ontology (SO) is a structured controlled vocabulary for
  the features and attributes of biological sequences. SO provides a common set of
  terms and definitions that facilitate the exchange, analysis, and management of
  genomic data.
domains:
- biomedical
- chemistry and biochemistry
- genomics
homepage_url: http://www.sequenceontology.org/
id: so
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Sequence Ontology
products:
- category: DataModelProduct
  description: Main SO release in OWL Format
  format: owl
  id: so.owl
  name: SO OWL
  product_url: http://purl.obolibrary.org/obo/so.owl
- category: DataModelProduct
  description: Main SO release in OBO Format
  format: obo
  id: so.obo
  name: SO OBO
  product_url: http://purl.obolibrary.org/obo/so.obo
- category: DataModelProduct
  description: Sequence Ontology Feature Annotation (SOFA) subset in OWL format. This
    subset includes only locatable sequence features and is designed for use in such
    outputs as GFF3.
  format: owl
  id: sofa.owl
  name: SOFA OWL
  product_url: http://purl.obolibrary.org/obo/so/subsets/SOFA.owl
- category: DataModelProduct
  description: Sequence Ontology Feature Annotation (SOFA) subset in OBO format. This
    subset includes only locatable sequence features and is designed for use in such
    outputs as GFF3.
  format: obo
  id: sofa.obo
  name: SOFA OBO
  product_url: http://purl.obolibrary.org/obo/so/subsets/SOFA.obo
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
publications:
- authors:
  - Eilbeck K
  - Lewis SE
  - Mungall CJ
  - Yandell M
  - Stein L
  - Durbin R
  - Ashburner M
  doi: 10.1186/gb-2005-6-5-r44
  id: doi:10.1186/gb-2005-6-5-r44
  journal: Genome Biology
  preferred: true
  title: 'The Sequence Ontology: a tool for the unification of genome annotations'
  year: '2005'
- authors:
  - Mungall CJ
  - Batchelor C
  - Eilbeck K
  doi: 10.1016/j.jbi.2010.03.002
  id: doi:10.1016/j.jbi.2010.03.002
  journal: Journal of Biomedical Informatics
  title: Evolution of the Sequence Ontology terms and relationships
  year: '2010'
repository: https://github.com/The-Sequence-Ontology/SO-Ontologies
---
# Sequence Ontology

The Sequence Ontology (SO) is a structured controlled vocabulary for the features and attributes of biological sequences. It was initially developed by the [Gene Ontology Consortium](http://www.geneontology.org/) and has since evolved with contributions from the [GMOD](http://www.gmod.org/) community, model organism database groups, and research institutes.

## Overview

SO provides a common set of terms and definitions that facilitate the exchange, analysis, and management of genomic data. It includes different kinds of features which can be located on biological sequences:

- **Biological features**: Defined by their disposition to be involved in a biological process (e.g., binding_site, exon)
- **Biomaterial features**: Intended for use in experiments (e.g., aptamer, PCR_product)
- **Experimental features**: Results of experiments

The ontology also provides a rich set of attributes to describe these features, such as "polycistronic" and "maternally imprinted."

## Applications

The Sequence Ontology serves several key purposes:

1. **Structured controlled vocabulary** for describing primary annotations of nucleic acid sequences, including annotations shared by DAS servers or encoded by GFF3
2. **Structured representation of annotations within databases**, enabling cross-database queries for specific genomic features
3. **Standardized description of mutations** at both sequence and more general levels in genomic databases

## Integration with Other Resources

The Sequence Ontology is part of the [OBO Foundry](http://www.obofoundry.org/) and has close links to other ontology projects such as:
- The RNA Ontology Consortium ([RNAO](http://roc.bgsu.edu/))
- Biosapiens polypeptide features

## Access and Development

SO is available in both OWL and OBO formats, with the main ontology and the Sequence Ontology Feature Annotation (SOFA) subset which includes only locatable sequence features designed for use in outputs like GFF3.

For new term suggestions, users can submit requests through the [Term Tracker](https://github.com/The-Sequence-Ontology/SO-Ontologies/issues) on GitHub.