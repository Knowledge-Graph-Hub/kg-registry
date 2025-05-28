---
layout: resource_detail
activity_status: active
id: protcid
name: ProtCID
description: The Protein Common Interface Database (ProtCID) provides comprehensive, PDB-wide structural information on protein interactions, identifying and clustering interfaces observed in multiple crystal forms of homologous proteins.
domains:
- proteomics
- structural biology
- chemistry and biochemistry
- biological systems
category: DataSource
tags:
- core
contacts:
- category: Individual
  label: "Qifang Xu"
  contact_details:
  - contact_type: email
    value: qifang.xu@fccc.edu
- category: Individual
  label: "Roland L. Dunbrack Jr"
- category: Organization
  label: "Fox Chase Cancer Center"
homepage_url: http://dunbrack2.fccc.edu/protcid/
repository: ""
license:
  id: https://dunbrack2.fccc.edu/ProtCID/About.aspx
  label: "Custom"
version: "3.0"
publications:
- id: https://doi.org/10.1038/s41467-020-14301-4
  title: "ProtCID: a data resource for structural information on protein interactions"
  authors:
  - "Qifang Xu"
  - "Roland L. Dunbrack"
  journal: "Nature Communications"
  year: "2020"
  preferred: true
- id: https://doi.org/10.1093/nar/gkq1059
  title: "The protein common interface database (ProtCID) - a comprehensive database of interactions of homologous proteins in multiple crystal forms"
  authors:
  - "Qifang Xu"
  - "Roland L. Dunbrack"
  journal: "Nucleic Acids Research"
  year: "2011"
- id: https://doi.org/10.1016/j.jmb.2008.06.002
  title: "Statistical Analysis of Interface Similarity in Crystals of Homologous Proteins"
  authors:
  - "Qifang Xu"
  - "Adrian Canutescu"
  - "Zhenyu Wang"
  - "Mu Tian"
  - "Thomas Biesiada"
  - "Roland L. Dunbrack"
  journal: "Journal of Molecular Biology"
  year: "2008"
products:
- id: protcid.database
  name: ProtCID Database
  description: "Database containing protein-protein interfaces, domain-domain interfaces, protein-peptide interfaces, and protein-ligand interactions based on structural data from the PDB."
  category: Product
- id: protcid.site
  name: ProtCID Web Interface
  description: "Web interface for searching and visualizing protein interaction data from ProtCID."
  category: GraphicalInterface
  product_url: https://dunbrack2.fccc.edu/ProtCID/Search/search.aspx
---

The Protein Common Interface Database (ProtCID) contains comprehensive, PDB-wide structural information on the interactions of proteins and individual protein domains with other molecules. The database is based on Pfam v34 and identifies common interfaces across different crystal structures.

ProtCID includes four types of interactions:
1. Chain-chain interfaces
2. Pfam domain-domain interfaces
3. Pfam-peptide interfaces
4. Pfam-ligand/nucleic acids interactions

The main goal of ProtCID is to identify and cluster homodimeric and heterodimeric interfaces observed in multiple crystal forms of homologous proteins, and interactions of peptides and ligands in homologous proteins. Such interfaces and interactions, especially of non-identical proteins or protein complexes, have been associated with biologically relevant interactions.

ProtCID provides an independent check on publicly available annotations of biological interactions for PDB entries, and can be used to identify biological protein complexes, especially weak interactions like asymmetric homodimers. The clusters of Pfam-peptide and Pfam-ligand interactions can be used to develop hypotheses for the structures of other protein families within the same superfamilies (Clans).

The database can be searched using PDB codes, PFAM IDs or accession codes, protein sequences, or UniProt IDs. It also allows browsing of Pfams, Clans, Pfam-Pfams, peptide-Pfams, and ligands in the PDB.
