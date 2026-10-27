---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/protein/
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-27T00:00:00Z'
description: The NCBI Protein database is a collection of protein sequence records
  from several sources, including translations of annotated coding regions in GenBank
  and RefSeq, as well as records from UniProtKB/Swiss-Prot, PIR, PRF, and PDB. It
  is searchable through Entrez and linked to related NCBI resources such as Gene,
  Nucleotide, Structure, and Conserved Domains. On 2026-10-26 it held about 1.66
  billion records.
domains:
- proteomics
- genomics
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/protein/
id: ncbi-protein
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI usage policies
name: NCBI Protein
products:
- category: GraphicalInterface
  description: Entrez search interface for NCBI Protein sequence records, with links
    to Gene, Nucleotide, Structure, and Conserved Domains.
  format: http
  id: ncbi-protein.web
  name: NCBI Protein Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://www.ncbi.nlm.nih.gov/protein/
synonyms:
- Protein
- Entrez Protein
---
# NCBI Protein

## Overview

The NCBI Protein database collects protein sequence records from several sources: translations of annotated coding regions in GenBank and RefSeq, and records from UniProtKB/Swiss-Prot, PIR, PRF, and PDB. Entrez queries on 2026-10-27 counted about 811 million GenBank, 511 million RefSeq, 1.1 million PDB, 576,000 Swiss-Prot, 22,000 PIR, and 12,000 PRF records, out of 1.66 billion in total.

## Access

- Entrez Protein search on the NCBI website.
- Programmatic access through the E-utilities (`db=protein`).

PRF (Protein Research Foundation, Japan) records are included, but PRF has no registry entry.
