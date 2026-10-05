---
activity_status: inactive
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://foodkg.github.io/contact.html
  - contact_type: github
    value: foodkg
  label: Tetherless World Constellation, Rensselaer Polytechnic Institute
creation_date: '2026-10-04T00:00:00Z'
description: FoodKG is a food knowledge graph built at Rensselaer Polytechnic Institute
  as part of the HEALS project with IBM Research. It links about one million recipes
  from the Recipe1M dataset, their ingredients, USDA nutrient data and the FoodOn
  food ontology, with provenance for each statement, to support food recommendation
  and question answering. The project releases its build scripts, mapping files and
  supporting ontologies rather than full RDF dumps; the full graph (about 67 million
  triples) is generated locally or queried through a public SPARQL endpoint, which
  returned HTTP 502 when checked on 2026-10-04.
domains:
- food
- nutrition
homepage_url: https://foodkg.github.io/
id: foodkg
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0
name: FoodKG
products:
- category: DocumentationProduct
  description: FoodKG project website, describing the knowledge graph, its construction
    process, the public SPARQL endpoint and related applications (WhatToMake, question
    answering over FoodKG and ingredient substitution).
  format: http
  id: foodkg.site
  name: FoodKG Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  product_url: https://foodkg.github.io/
- category: ProcessProduct
  description: Python scripts that build FoodKG from the Recipe1M recipe dataset (layer1.json
    and det_ingrs.json, acquired manually), USDA nutrient data and FoodOn (downloaded
    automatically). Outputs are three TriG files, usda-links.trig (about 4.1 million
    triples), foodon-links.trig (about 30 thousand triples) and foodkg-core.trig (about
    63 million triples), intended for loading into Blazegraph.
  format: python
  id: foodkg.build-scripts
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: FoodKG Construction Scripts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:wasDerivedFrom
    source: fooddata-central
  product_url: https://github.com/foodkg/foodkg.github.io/tree/master/src
- category: ProgrammingInterface
  description: Public Blazegraph SPARQL endpoint for querying FoodKG recipes, ingredients
    and nutrition data (namespace kb).
  format: http
  id: foodkg.sparql
  name: FoodKG SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  - relation_type: prov:hadPrimarySource
    source: foodon
  product_url: https://inciteprojects.idea.rpi.edu/foodkg/namespace/kb/sparql
  warnings:
  - Endpoint was not able to be reached when checked on 2026-10-04. The server returned
    HTTP 502 Bad Gateway for the endpoint and its landing page.
- category: GraphProduct
  description: Sample of FoodKG containing the USDA nutrient data mappings, generated
    with the Semantic Data Dictionary process (usda.rdf, hosted on Google Drive).
  format: rdfxml
  id: foodkg.usda-sample
  name: FoodKG USDA Mappings Sample
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:wasDerivedFrom
    source: fooddata-central
  product_url: https://drive.google.com/open?id=1hkitCcxnM_7R6OYuvC5zakWojlN2Xuog
- category: MappingProduct
  description: Semantic Data Dictionary mapping file specifying how USDA nutrient
    data columns are linked to external ontologies such as FoodOn and the Units of
    Measurement Ontology when building FoodKG.
  format: csv
  id: foodkg.sdd-dictionary
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: FoodKG USDA Semantic Data Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:wasDerivedFrom
    source: fooddata-central
  product_file_size: 1066
  product_url: https://foodkg.github.io/sdd/usdaDM.csv
- category: OntologyProduct
  description: Food component of the WhatToMake ontology, containing the base classes
    (food, ingredient, recipe, characteristic, user, course, meal) used to find recipes
    from ingredients at hand while accounting for allergies and dietary restrictions.
  format: rdfxml
  id: foodkg.whattomake
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: WhatToMake Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  product_file_size: 6542
  product_url: http://purl.org/heals/food
- category: OntologyProduct
  description: FoodOn component of the WhatToMake ontology, containing the classes
    imported from FoodOn.
  format: rdfxml
  id: foodkg.whattomake-foodon
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: WhatToMake FoodOn Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  - relation_type: prov:hadPrimarySource
    source: foodon
  product_file_size: 15252
  product_url: http://purl.org/heals/foodon
- category: GraphProduct
  description: Ingredient component of the WhatToMake ontology, containing the individuals
    that represent recipes and ingredients.
  format: rdfxml
  id: foodkg.whattomake-individuals
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: WhatToMake Individuals
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  product_file_size: 14373
  product_url: http://purl.org/heals/ingredient
- category: OntologyProduct
  description: Dietary Guideline Ontology (heals-guidelines), an OWL ontology modeling
    dietary guidelines, published alongside FoodKG.
  format: ttl
  id: foodkg.dgo
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: Dietary Guideline Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodkg
  product_file_size: 3687
  product_url: https://foodkg.github.io/ontologies/dgo.owl
publications:
- authors:
  - Steven Haussmann
  - Oshani Seneviratne
  - Yu Chen
  - Yarden Ne'eman
  - James Codella
  - Ching-Hua Chen
  - Deborah L. McGuinness
  - Mohammed J. Zaki
  doi: 10.1007/978-3-030-30796-7_10
  id: doi:10.1007/978-3-030-30796-7_10
  journal: Lecture Notes in Computer Science
  preferred: true
  title: 'FoodKG: A Semantics-Driven Knowledge Graph for Food Recommendation'
  year: '2019'
synonyms:
- Food Knowledge Graph
---
# FoodKG

FoodKG is a food knowledge graph developed by the Tetherless World Constellation at Rensselaer Polytechnic Institute, with IBM Research, as part of the Health Empowerment by Analytics, Learning and Semantics (HEALS) project. It was presented at ISWC 2019 as a resource for consumer-oriented food recommendation.

## Contents

FoodKG combines three kinds of data, keeping provenance for each statement:

- **Recipes**: about one million recipes and their ingredients from the Recipe1M dataset (Im2Recipe project, MIT CSAIL).
- **Nutrients**: USDA nutrient data, converted to RDF with the Semantic Data Dictionary approach and linked to FoodOn and the Units of Measurement Ontology. The USDA data is now distributed through FoodData Central.
- **Food knowledge**: links from ingredients to [FoodOn](https://foodon.org) classes.

## Access

The project publishes construction scripts rather than full RDF dumps. Users obtain the Recipe1M files themselves and run the scripts to produce `usda-links.trig`, `foodon-links.trig` and `foodkg-core.trig` (about 67 million triples in total), which can be loaded into Blazegraph. A sample of the USDA mappings is available as RDF/XML, and the site documents a public SPARQL endpoint, which returned HTTP 502 when checked on 2026-10-04.

The site also hosts the WhatToMake ontology, the Dietary Guideline Ontology, and related work on question answering and ingredient substitution over FoodKG. The repository was last updated in November 2024.