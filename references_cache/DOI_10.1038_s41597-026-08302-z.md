---
reference_id: DOI:10.1038/s41597-026-08302-z
title: Unifying biomedical knowledge in a modern multimodal graph
authors:
- Lucas Vittor
- Ayush Noori
- Iñaki Arango
- Joaquín Polonuer
- Sam Rodriques
- Andrew White
- David A. Clifton
- Marinka Zitnik
journal: Scientific Data
year: '2026'
doi: 10.1038/s41597-026-08302-z
content_type: abstract_only
---

# Unifying biomedical knowledge in a modern multimodal graph
**Authors:** Lucas Vittor, Ayush Noori, Iñaki Arango, Joaquín Polonuer, Sam Rodriques, Andrew White, David A. Clifton, Marinka Zitnik
**Journal:** Scientific Data (2026)
**DOI:** [10.1038/s41597-026-08302-z](https://doi.org/10.1038/s41597-026-08302-z)

## Content

Abstract

                    Biomedical knowledge graphs (KGs) are widely used in the life sciences, yet many are derived from unstructured documents and therefore lack schema-level constraints, whereas graphs assembled from structured resources are difficult to harmonize into a unified representation. We present O
                    ptimus
                    KG, a multimodal biomedical labeled property graph (LPG) built from structured and semi-structured resources to preserve factual, type-specific metadata across molecular, anatomical, clinical, and environmental domains. O
                    ptimus
                    KG contains 190,939 nodes across 10 entity types, 21,818,752 edges across 27 edge types, and 67,070,490 property instances encoding 109,665,797 values across 145 distinct property keys, derived from 18 ontologies and controlled vocabularies. The graph enforces a top-level schema for nodes and edges and retains granular, type-specific properties, cross-references, and provenance. We assessed the validity of O
                    ptimus
                    KG by evaluating whether graph relationships are supported by evidence from the scientific literature using a multimodal agent, PaperQA3. PaperQA3 identified supporting evidence for 70.0% of sampled edges, whereas 83.4% of sampled false edges received no supporting evidence. Edges without literature support were concentrated in associations derived from experimental and functional genomics resources, suggesting that O
                    ptimus
                    KG captures biomedical knowledge that may precede synthesis in the scientific literature. O
                    ptimus
                    KG is distributed as Apache Parquet files, providing a standardized resource for graph-based machine learning, knowledge-grounded retrieval with large language models, and biomedical discovery use cases such as hypothesis generation.