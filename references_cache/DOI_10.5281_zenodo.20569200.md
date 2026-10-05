---
reference_id: DOI:10.5281/zenodo.20569200
title: "Sugi Atlas: A Comprehensive, Deterministic Biomedical Catalog from a Knowledge Graph for Humans and AI Agents"
authors:
- "Tamer, Gür"
journal: Zenodo
year: '2026'
doi: 10.5281/zenodo.20569200
content_type: abstract_only
supplementary_files:
  - filename: main.pdf
    download_url: "https://zenodo.org/api/records/20569200/files/main.pdf/content"
    size_bytes: 561046
    checksum: md5:2b29a0d1cfda507eaeec8893325c1b65
---

# Sugi Atlas: A Comprehensive, Deterministic Biomedical Catalog from a Knowledge Graph for Humans and AI Agents
**Authors:** Tamer, Gür
**Journal:** Zenodo (2026)
**DOI:** [10.5281/zenodo.20569200](https://doi.org/10.5281/zenodo.20569200)

## Content

Biomedical knowledge is spread across hundreds of specialized databases, each with its own identifiers, formats, and update cycles. Each is authoritative within its domain, yet most research needs a connected view across them, so assembling a consolidated, current, and trustworthy picture of any single gene, drug, or disease still takes considerable manual effort. Such reference content is increasingly consumed not only by researchers but by AI agents, raising the bar on how correct and how current it must be. Large language models can write it, but doing so at the scale of an entire catalog is costly and carries a hallucination surface; and even when grounded against authoritative data through a protocol such as MCP, the path a model takes through a large graph varies between runs and models and is hard to reproduce. We present Sugi Atlas, a comprehensive catalog of genes (together with their protein products), drugs, and diseases built by deterministically mining BioBTree, a graph that unifies around seventy primary databases into billions of cross-references. Rather than let a model explore the graph at query time, Sugi Atlas traverses it along fixed query plans, hundreds to thousands of chained graph queries per page, so the catalog is built the same way on each run: every entity is covered at uniform breadth, every value comes straight from the source data, and, for a given BioBTree snapshot, the whole corpus is reproducible. A curated cross-entity mesh links the three corpora into one connected resource, so a relationship recorded for a gene is navigable from the drug or disease it implicates. By consolidating otherwise scattered data into one openly published, refreshable place, with a stable page structure and schema.org records that ease programmatic use, Sugi Atlas offers researchers and AI agents alike a grounded, current reference. Sugi Atlas comprises more than 52,000 pages and is openly available at https://sugi.bio/atlas/.