---
reference_id: DOI:10.5281/zenodo.20566358
title: "Sniff Atlas v1.0.1: an open, breed-stratified catalogue of common canine coding variants with calibrated protein-language-model pathogenicity and an evidence-graded knowledge graph"
authors:
- "Gehring, Matt"
journal: Zenodo
year: '2026'
doi: 10.5281/zenodo.20566358
keywords:
- canine genomics
- dog
- CanFam4
- allele frequency
- breed
- pathogenicity prediction
- ESM2
- knowledge graph
- gnomAD
- variant catalogue
- Biolink
- Canis Familiaris
content_type: abstract_only
supplementary_files:
  - filename: sniff_atlas.sites.vcf.gz
    download_url: "https://zenodo.org/api/records/20572692/files/sniff_atlas.sites.vcf.gz/content"
    size_bytes: 189117079
    checksum: md5:8b0c4f02ce6653f158eb0c64278e3471
  - filename: sniff_atlas.sites.vcf.gz.tbi
    download_url: "https://zenodo.org/api/records/20572692/files/sniff_atlas.sites.vcf.gz.tbi/content"
    size_bytes: 1384822
    checksum: md5:710e9a76de5df6d8b157bc403120634e
  - filename: README.md
    download_url: "https://zenodo.org/api/records/20572692/files/README.md/content"
    size_bytes: 6212
    checksum: md5:155ed8c1eb3340ac7af2ec09dc729e75
  - filename: sniff-atlas-v1.0.1.tar.gz
    download_url: "https://zenodo.org/api/records/20572692/files/sniff-atlas-v1.0.1.tar.gz/content"
    size_bytes: 1753039854
    checksum: md5:bb4ca86f3461028b3a1763d9fcd7307b
---

# Sniff Atlas v1.0.1: an open, breed-stratified catalogue of common canine coding variants with calibrated protein-language-model pathogenicity and an evidence-graded knowledge graph
**Authors:** Gehring, Matt
**Journal:** Zenodo (2026)
**DOI:** [10.5281/zenodo.20566358](https://doi.org/10.5281/zenodo.20566358)

## Content

An open, breed-stratified catalogue of the common and low-frequency coding-variant landscape of the domestic dog across 188 breeds: allele frequencies for 9,667,790 imputed variants (14,478 dogs, CanFam4) — ~6.7M common (MAF >= 5%) plus ~3.0M lower-frequency (MAF 1-5%) — with SnpEff annotation and three complementary deleteriousness layers (ESM2, Pangolin, Zoonomia 241-way phyloP; ESM2 calibrated at AUC 0.935 vs OMIA), an evidence-graded Biolink knowledge graph, and a bcftools-queryable sites VCF. Scope: MAF >= 1% (the CanVAS imputation floor; sub-1% variants are out of scope). Independently validated against the NHGRI (National Human Genome Research Institute) 722 directly-sequenced whole-genome catalogue (Plassais et al. 2019). Derived from CanVAS (doi:10.5281/zenodo.19186944, Brundage 2026); raw genotypes not redistributed. See README/VALIDATION/CITATIONS inside the archive. Aggregate data only (no individual dog identifiers); OMIA-derived clinical layer held for v1.1.
Erratum (2026-06-07): In the bundled knowledge_graph/, ten known-disease-variant nodes (tag-SNP proxies and unshipped sentinel entries) were assigned mismapped CanFam4 coordinates and must not be used as authoritative disease-variant positions. This affects only those knowledge-graph variant coordinates; the core breed-stratified allele-frequency atlas, the pathogenicity scores, and the sites VCF are CanFam4-native and unaffected. Corrected in the source repository and in the forthcoming v1.1. In v1.0.x, treat knowledge_graph variant positions as advisory only.