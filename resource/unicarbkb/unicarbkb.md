---
activity_status: active
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: UniCarbKB is a glycomics and glycoproteomics knowledge platform that
  curates glycan structures of glycoproteins, biological source context, experimental
  methods, literature evidence, and protein links for glycobiology research.
domains:
- chemistry and biochemistry
- proteomics
- biomedical
- biological systems
homepage_url: https://www.unicarbkb.org
id: unicarbkb
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: UniCarbKB
products:
- category: GraphicalInterface
  description: UniCarbKB web portal for browsing curated glycoprotein glycan structures,
    biological source information, experimental methods, literature references, and
    linked protein records.
  format: http
  id: unicarbkb.portal
  name: UniCarbKB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unicarbkb
  product_url: https://www.unicarbkb.org
- category: DocumentationProduct
  description: Nucleic Acids Research article describing UniCarbKB as a curated knowledge
    platform for glycoproteomics and glycomics research.
  format: http
  id: unicarbkb.article
  name: UniCarbKB Knowledge Platform Article
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unicarbkb
  product_url: https://doi.org/10.1093/nar/gkt1128
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 403 error
    when accessing file'
- category: Product
  description: Sample RDF data files demonstrating GlycoCoO usage with examples from
    UniCarbKB, GlyConnect, and GlycoNAVI
  format: http
  id: glycocoo.rdf-samples
  name: GlycoCoO RDF Sample Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  product_url: https://github.com/glycoinfo/GlycoCoO/tree/master/RDF_Sample
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: glycordf
  - relation_type: prov:wasInformedBy
    source: unicarbkb
  - relation_type: prov:wasInformedBy
    source: glyconnect
  - relation_type: prov:wasInformedBy
    source: glyconavi
publications:
- authors:
  - Matthew P Campbell
  - Robyn Peterson
  - Julien Mariethoz
  - Elisabeth Gasteiger
  - Yukie Akune
  - Kiyoko F Aoki-Kinoshita
  - Frederique Lisacek
  - Nicolle H Packer
  doi: 10.1093/nar/gkt1128
  id: doi:10.1093/nar/gkt1128
  journal: Nucleic Acids Research
  preferred: true
  title: 'UniCarbKB: building a knowledge platform for glycoproteomics'
  year: '2014'
- doi: 10.1002/pmic.201100302
  id: doi:10.1002/pmic.201100302
  journal: Proteomics
  title: 'UniCarbKB: putting the pieces together for glycomics research'
  year: '2011'
synonyms:
- UniCarb KnowledgeBase
---
# UniCarbKB

UniCarbKB is a curated glycomics and glycoproteomics knowledge platform. It
links glycan structures on glycoproteins to biological source context,
experimental methods, protein records, and literature evidence.