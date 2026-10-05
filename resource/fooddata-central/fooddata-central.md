---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://fdc.nal.usda.gov/contact/
  label: USDA Agricultural Research Service, Beltsville Human Nutrition Research Center
creation_date: '2026-10-04T00:00:00Z'
description: FoodData Central is the U.S. Department of Agriculture's integrated food
  composition data system, run by the Agricultural Research Service (Beltsville Human
  Nutrition Research Center) and hosted by the National Agricultural Library. It provides
  nutrient and food component profiles for five data types (Foundation Foods, SR Legacy,
  the Food and Nutrient Database for Dietary Studies (FNDDS), Branded Foods and Experimental
  Foods), with a search interface, a REST API and bulk CSV and JSON downloads. The
  data are in the public domain under CC0 1.0.
domains:
- nutrition
- food
- agriculture
homepage_url: https://fdc.nal.usda.gov/
id: fooddata-central
infores_id: fooddata-central
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: FoodData Central
products:
- category: GraphicalInterface
  description: FoodData Central food search interface for browsing nutrient profiles
    across all five data types.
  format: http
  id: fooddata-central.portal
  name: FoodData Central Food Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_url: https://fdc.nal.usda.gov/food-search
- category: ProgrammingInterface
  description: FoodData Central REST API (v1) for food search, food details and food
    lists, returning JSON. Requires a free data.gov API key; DEMO_KEY works for light
    testing.
  format: http
  id: fooddata-central.api
  name: FoodData Central API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_url: https://api.nal.usda.gov/fdc/v1/
  warnings:
  - As of 2026-10-04 the base URL returns HTTP 403 without an API key; keyed requests
    (for example with DEMO_KEY) return 200.
- category: DocumentationProduct
  description: API guide for the FoodData Central REST API, with key signup, endpoints
    and the OpenAPI specification.
  format: http
  id: fooddata-central.api-docs
  name: FoodData Central API Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_url: https://fdc.nal.usda.gov/api-guide
- category: Product
  compression: zip
  description: Full FoodData Central download with all data types as CSV files, April
    2026 release (about 480 MB compressed).
  format: csv
  id: fooddata-central.full.csv
  latest_version: '2026-04-30'
  name: FoodData Central Full Download (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 481517495
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2026-04-30.zip
- category: Product
  compression: zip
  description: Foundation Foods data as CSV, April 2026 release. Foundation Foods
    carry analytical nutrient values with extensive metadata on samples and methods.
  format: csv
  id: fooddata-central.foundation.csv
  latest_version: '2026-04-30'
  name: FoodData Central Foundation Foods (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 3825741
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2026-04-30.zip
- category: Product
  compression: zip
  description: Foundation Foods data as JSON, April 2026 release.
  format: json
  id: fooddata-central.foundation.json
  latest_version: '2026-04-30'
  name: FoodData Central Foundation Foods (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 469303
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_json_2026-04-30.zip
- category: Product
  compression: zip
  description: Branded Foods data as CSV, April 2026 release. Branded Foods hold label
    nutrient data for commercial products submitted by industry through the Global
    Branded Food Products Database partnership.
  format: csv
  id: fooddata-central.branded.csv
  latest_version: '2026-04-30'
  name: FoodData Central Branded Foods (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 448767220
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_csv_2026-04-30.zip
- category: Product
  compression: zip
  description: Branded Foods data as JSON, April 2026 release.
  format: json
  id: fooddata-central.branded.json
  latest_version: '2026-04-30'
  name: FoodData Central Branded Foods (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 204270542
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_json_2026-04-30.zip
- category: Product
  compression: zip
  description: Survey Foods (FNDDS) data as CSV, October 2024 release. FNDDS gives
    nutrient values for foods and beverages reported in What We Eat in America, the
    dietary intake component of NHANES.
  format: csv
  id: fooddata-central.survey.csv
  latest_version: '2024-10-31'
  name: FoodData Central Survey Foods FNDDS (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 3325692
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_survey_food_csv_2024-10-31.zip
- category: Product
  compression: zip
  description: Survey Foods (FNDDS) data as JSON, October 2024 release.
  format: json
  id: fooddata-central.survey.json
  latest_version: '2024-10-31'
  name: FoodData Central Survey Foods FNDDS (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 3835292
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_survey_food_json_2024-10-31.zip
- category: Product
  compression: zip
  description: SR Legacy data as CSV. This is the final April 2018 release of the
    USDA National Nutrient Database for Standard Reference, which is no longer updated.
  format: csv
  id: fooddata-central.sr-legacy.csv
  latest_version: 2018-04
  name: FoodData Central SR Legacy (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 6074592
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
- category: Product
  compression: zip
  description: SR Legacy data as JSON, final April 2018 release.
  format: json
  id: fooddata-central.sr-legacy.json
  latest_version: 2018-04
  name: FoodData Central SR Legacy (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_file_size: 13456312
  product_url: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_json_2018-04.zip
- category: DocumentationProduct
  description: Download page listing current and past releases of every FoodData Central
    dataset, with documentation and field descriptions.
  format: http
  id: fooddata-central.downloads
  name: FoodData Central Download Datasets Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  product_url: https://fdc.nal.usda.gov/download-datasets
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
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
publications:
- authors:
  - Naomi K Fukagawa
  - Kyle McKillop
  - Pamela R Pehrsson
  - Alanna Moshfegh
  - James Harnly
  - John Finley
  doi: 10.1093/ajcn/nqab397
  id: doi:10.1093/ajcn/nqab397
  journal: The American Journal of Clinical Nutrition
  preferred: true
  title: 'USDA’s FoodData Central: what is it and why is it needed today?'
  year: '2022'
synonyms:
- FDC
- USDA FoodData Central
---
# FoodData Central

FoodData Central (FDC) is the USDA's food composition data system. The Agricultural Research Service's Beltsville Human Nutrition Research Center maintains it, and the National Agricultural Library hosts it.

## Data types

- **Foundation Foods**: analytical nutrient values for commodity and minimally processed foods, with sample and method metadata.
- **SR Legacy**: the final (April 2018) release of the USDA National Nutrient Database for Standard Reference. It is no longer updated.
- **Survey Foods (FNDDS)**: the Food and Nutrient Database for Dietary Studies, used to code foods reported in What We Eat in America / NHANES.
- **Branded Foods**: label data for commercial products from the Global Branded Food Products Database partnership.
- **Experimental Foods**: research data linked to agricultural studies. It is searchable in the portal but has no separate bulk file on the download page.

## Access

Bulk CSV and JSON files are released about twice a year. File names carry the release date, and no stable "latest" link exists, so the product URLs here point at the newest release listed on 2026-10-04 (2026-04-30 for full, Foundation and Branded; 2024-10-31 for FNDDS; 2018-04 for SR Legacy).

The REST API needs a free data.gov key. The NCATS Translator Service Provider also serves FoodData Central through a BioThings API at `https://biothings.transltr.io/fooddata` (infores `biothings-fooddata-central`, build 2024-01-18).

## License

FDC data are in the public domain and published under CC0 1.0. USDA asks users to cite: U.S. Department of Agriculture, Agricultural Research Service, Beltsville Human Nutrition Research Center. FoodData Central. Available from https://fdc.nal.usda.gov/.