---
reference_id: DOI:10.48550/arXiv.2605.24706
title: "MetaboKG: An Analysis-centric Knowledge Graph Framework for Untargeted Metabolomics"
authors:
- "Féraud, Matthieu"
- "Boukhajou, Dina"
- "Gandon, Fabien"
- "Nothias, Louis-Félix"
journal: arXiv
year: '2026'
doi: 10.48550/arXiv.2605.24706
keywords:
- Databases (cs.DB)
- Biomolecules (q-bio.BM)
- Molecular Networks (q-bio.MN)
- "FOS: Computer and information sciences"
- "FOS: Computer and information sciences"
- "FOS: Biological sciences"
- "FOS: Biological sciences"
content_type: abstract_only
---

# MetaboKG: An Analysis-centric Knowledge Graph Framework for Untargeted Metabolomics
**Authors:** Féraud, Matthieu, Boukhajou, Dina, Gandon, Fabien, Nothias, Louis-Félix
**Journal:** arXiv (2026)
**DOI:** [10.48550/arXiv.2605.24706](https://doi.org/10.48550/arXiv.2605.24706)

## Content

Untargeted metabolomics generates large volumes of tandem mass spectrometry (MS/MS) data and computational annotations that can reveal molecular mechanisms across organisms and environments. Public reuse has improved through harmonized repository metadata and access infrastructures such as Pan-ReDU, and through metabolomics knowledge graphs such as ENPKG and METRIN-KG. Yet the analytical layer remains fragmented: spectra, features, workflow outputs, annotations, confidence evidence, and contextual metadata are still scattered across repositories and tabular artifacts. We present MetaboKG, an analysis-centric knowledge graph framework for engineering reusable metabolomics knowledge from public repositories, metadata, and GNPS molecular network results. MetaboKG contributes a transformation workflow that preserves links between repository exports, analytical files, spectra, features, and annotation results; a semantic model grounded in PROV-O and SIO and aligned with the Mass Spectrometry ontology (MS), ChEBI, NCBITaxon, ENVO, and NCIT to represent provenance, analytical evidence, metadata attributes, and controlled vocabulary terms; and a Universal Annotation Identifier strategy extending the Universal Spectrum Identifier (USI) with workflow-specific components for late binding, incremental ingestion, and post hoc linkage across analyses. We demonstrate MetaboKG at the public-repository scale on 680 GNPS molecular networking results and evaluate it through competency questions covering biochemical enrichment, environmental specificity, and cross instrument analytical variation. Results show that graph-based integration supports traceable annotation reuse and reproducible SPARQL exploration of biochemical relationships that remain fragmented across repository-native resources.