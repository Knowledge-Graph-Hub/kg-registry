---
category: Product
compression: targz
description: Reduced tagger dictionary used by the Tagger web service, as tab-separated
  entities, names, groups, global, preferred-name, and text files. Gene/protein names
  come from the STRING alias file, chemical names from STITCH (PubChem compound identifiers),
  and other names from NCBI Taxonomy, Gene Ontology, BRENDA Tissue Ontology, Disease
  Ontology, Environment Ontology, and the Mammalian Phenotype Ontology.
format: tsv
id: tagger.dictionary
name: Tagger Dictionary
original_source:
- relation_type: prov:hadPrimarySource
  source: tagger
product_file_size: 388733075
product_url: https://download.jensenlab.org/tagger_dictionary.tar.gz
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: string
- relation_type: prov:wasDerivedFrom
  source: stitch
- relation_type: prov:wasDerivedFrom
  source: ncbitaxon
- relation_type: prov:wasDerivedFrom
  source: go
- relation_type: prov:wasDerivedFrom
  source: bto
- relation_type: prov:wasDerivedFrom
  source: doid
- relation_type: prov:wasDerivedFrom
  source: envo
- relation_type: prov:wasDerivedFrom
  source: mp
layout: product_detail
---
