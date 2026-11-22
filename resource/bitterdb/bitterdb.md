---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: nivlab@agri.huji.ac.il
  - contact_type: url
    value: https://bitterdb.agri.huji.ac.il/dbbitter.php
  label: BitterDB - The Hebrew University of Jerusalem
- category: Individual
  contact_details:
  - contact_type: url
    value: https://biochem-food-nutrition.agri.huji.ac.il/mashaniv
  label: Masha Y. Niv
  orcid: 0000-0001-8275-8795
creation_date: '2026-06-17T00:00:00Z'
description: BitterDB is a database of bitter-tasting compounds and their associated
  bitter taste receptors (TAS2Rs), maintained by the Niv lab at the Hebrew University
  of Jerusalem. The 2024 release holds over 2,200 bitter molecules, close to 1,800
  ligand-TAS2R associations, and receptors from 66 species, with links to receptor
  structures, mutation and SNP data, and machine-learning bitterness classifiers,
  supporting research in chemoreception and ligand-receptor pharmacology.
domains:
- chemistry and biochemistry
- cheminformatics
- pharmacology
- nutrition
- food
funding:
- Israel Science Foundation (ISF) (494/16)
- Israel Science Foundation (ISF) and National Natural Science Foundation of China
  (NSFC) (2463/16)
- Ministry of Innovation
- Ministry of Agriculture
- Good Food Israel
- Hebrew University of Jerusalem
homepage_url: https://bitterdb.agri.huji.ac.il/dbbitter.php
id: bitterdb
last_modified_date: '2026-11-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-nd/4.0/
  label: CC BY-NC-ND 4.0
name: BitterDB
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching bitter compounds and bitter
    taste receptors.
  format: http
  id: bitterdb.site
  is_public: true
  name: BitterDB Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://bitterdb.agri.huji.ac.il/dbbitter.php
- category: Product
  description: BitterDB 2024 compound table with one row per bitter molecule, giving
    structure (SMILES, InChIKey, formula), PubChem identifier, CAS number, physicochemical
    properties, natural-product flag, and sensory threshold and toxicity values where
    known.
  format: csv
  id: bitterdb.downloads.compounds
  name: BitterDB 2024 Bitter Compound Properties
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=BitterCompoundsPropA_2024.csv
- category: Product
  description: BitterDB 2024 ligand-receptor association table linking bitter compounds
    to the bitter taste receptors (TAS2Rs) they activate, with literature references,
    threshold, EC50 and efficacy values, and the receptor sequence variant tested.
  format: csv
  id: bitterdb.downloads.ligand_receptors
  name: BitterDB 2024 Ligand-Receptor Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=ligandReceptorsA_2024.csv
- category: Product
  description: BitterDB 2024 receptor table with one row per bitter taste receptor
    (TAS2R) across species, giving sequence, organism, UniProt accession, gene and
    protein names, number of known ligands, and links to GeneCards, GPCRdb, the Human
    Protein Atlas, the IUPHAR/BPS Guide to Pharmacology and AlphaFold models.
  format: csv
  id: bitterdb.downloads.receptors
  name: BitterDB 2024 Bitter Taste Receptors
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: genecards
  - relation_type: prov:wasInfluencedBy
    source: gpcrdb
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: gtopdb
  - relation_type: prov:wasInfluencedBy
    source: alphafold
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=ReceptorSearchA_2024.csv
- category: Product
  description: BitterDB 2024 table of the sources reporting each compound as bitter
    (handbooks, literature and databases), with bitterness classification, sensory
    test concentration, EC50, threshold, citation and organism.
  format: csv
  id: bitterdb.downloads.compound_sources
  name: BitterDB 2024 Compound Bitterness Sources
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=cbitterresourceA_2024.csv
- category: Product
  description: BitterDB 2024 table of TAS2R residues studied by site-directed mutagenesis,
    giving receptor, transmembrane location, Ballesteros-Weinstein number, residue
    and literature references.
  format: csv
  id: bitterdb.downloads.mutations
  name: BitterDB 2024 Receptor Mutation Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=mutationData_2024.csv
- category: Product
  description: BitterDB 2024 table of TAS2R single-nucleotide polymorphisms, giving
    receptor, location, Ballesteros-Weinstein number, residue change, minor allele
    frequency and dbSNP identifier.
  format: csv
  id: bitterdb.downloads.snps
  name: BitterDB 2024 Receptor SNP Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=snpData_2024.csv
- category: MappingProduct
  description: BitterDB 2024 mapping of BitterDB compound IDs to ZINC database identifiers.
  format: csv
  id: bitterdb.downloads.zinc_mapping
  name: BitterDB 2024 Compound to ZINC Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: zinc
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=compzinclinksA_2024.csv
- category: MappingProduct
  description: BitterDB 2024 mapping of BitterDB compound IDs to identical and similar
    DrugBank drugs.
  format: csv
  id: bitterdb.downloads.drugbank_mapping
  name: BitterDB 2024 Compound to DrugBank Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=drugbankcidA_2024.csv
- category: MappingProduct
  description: BitterDB 2024 mapping of BitterDB compound IDs to IUPHAR/BPS Guide
    to Pharmacology ligand IDs.
  format: csv
  id: bitterdb.downloads.gtopdb_mapping
  name: BitterDB 2024 Compound to Guide to Pharmacology Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  product_url: https://bitterdb.agri.huji.ac.il/downloads/2024/?file=IUPHAR_cidA_2024.csv
- category: ProcessProduct
  description: MATLAB code for BitterPredict, a machine-learning classifier that predicts
    whether a molecule tastes bitter from its chemical structure, trained on BitterDB
    compounds and offered as a BitterDB classifier.
  format: mixed
  id: bitterdb.bitterpredict
  name: BitterPredict
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://github.com/Niv-Lab/BitterPredict1
  repository: https://github.com/Niv-Lab/BitterPredict1
- category: ProcessProduct
  description: BitterMatch, a recommendation-system algorithm for predicting which
    bitter taste receptors a molecule activates, trained on BitterDB ligand-receptor
    associations and offered as a BitterDB classifier.
  format: python
  id: bitterdb.bittermatch
  name: BitterMatch
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  product_url: https://github.com/YuliSl/BitterMatch
  repository: https://github.com/YuliSl/BitterMatch
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
publications:
- authors:
  - Evgenii Ziaikin
  - Moran David
  - Sofya Uspenskaya
  - Masha Y Niv
  doi: 10.1093/nar/gkae1044
  id: https://doi.org/10.1093/nar/gkae1044
  journal: Nucleic Acids Research
  preferred: true
  title: 'BitterDB: 2024 update on bitter ligands and taste receptors'
  year: '2025'
- authors:
  - Ayana Dagan-Wiener
  - "Antonella Di\_Pizio"
  - Ido Nissim
  - Malkeet S Bahia
  - Nitzan Dubovski
  - Eitan Margulis
  - Masha Y Niv
  doi: 10.1093/nar/gky974
  id: https://doi.org/10.1093/nar/gky974
  journal: Nucleic Acids Research
  title: 'BitterDB: taste ligands and receptors database in 2019'
  year: '2019'
- authors:
  - Ayana Wiener
  - Marina Shudler
  - Anat Levit
  - Masha Y. Niv
  doi: 10.1093/nar/gkr755
  id: https://doi.org/10.1093/nar/gkr755
  journal: Nucleic Acids Research
  title: 'BitterDB: a database of bitter compounds'
  year: '2012'
rrid: SCR_006977
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:9031
- NCBITaxon:9685
- NCBITaxon:9615
- NCBITaxon:9913
- NCBITaxon:9258
---
# BitterDB

BitterDB is a database of bitter-tasting molecules and the bitter taste receptors (T2Rs
or TAS2Rs) they activate. Maintained by the Niv lab at the Institute of Biochemistry,
Food Science and Nutrition, Hebrew University of Jerusalem, it serves as a reference
for studies of bitter taste, chemoreception, and the pharmacology of taste receptors.
It was introduced in 2012 and updated in 2019 and 2024; the database was last updated
on 18 October 2024.

Content includes:

- Over 2,200 bitter compounds curated from the literature, handbooks and other databases,
  with structures, physicochemical properties and links to PubChem, ZINC, DrugBank and
  the IUPHAR/BPS Guide to Pharmacology
- Bitter taste receptors from 66 species, including all 26 functional human TAS2Rs,
  with sequences, alignments, mutation and SNP data, and links to available structures
- Close to 1,800 ligand-receptor associations
- Bitterness classifiers (BitterPredict, BitterToxic, BitterIntense, BitterMatch and
  BitterMasS)

All source tables are downloadable as CSV files from the Download tab, under a Creative
Commons Attribution-NonCommercial-NoDerivatives 4.0 license. GeneCards integrates bitter
taste receptor information from BitterDB.