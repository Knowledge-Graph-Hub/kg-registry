---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bioplex.hms.harvard.edu/contact.php
  label: Harper and Gygi Labs, Harvard Medical School
- category: Individual
  contact_details:
  - contact_type: url
    value: https://connects.catalyst.harvard.edu/Profiles/display/Person/20290
  label: J. Wade Harper
creation_date: '2026-10-10T00:00:00Z'
description: BioPlex is a proteome-scale map of human protein-protein interactions
  built by affinity purification-mass spectrometry (AP-MS) of tagged proteins expressed
  from the human ORFeome. It is a collaboration between the Gygi and Harper labs at
  Harvard Medical School. BioPlex 3.0 covers nearly 120,000 interactions among nearly
  15,000 proteins in HEK293T cells, and a companion network covers about 71,000 interactions
  in HCT116 cells. Interaction tables for each network version can be downloaded,
  and the networks can be explored on the web or through R and Python packages.
domains:
- protein interactions
- proteomics
- systems biology
- cell biology
- biological systems
homepage_url: https://bioplex.hms.harvard.edu/
id: bioplex
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
name: BioPlex
products:
- category: GraphicalInterface
  description: Interactive web explorer (BioPlex Display) for browsing BioPlex interactions
    with conservation, community, domain, and fitness views.
  format: http
  id: bioplex.explorer
  name: BioPlex Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_url: https://bioplex.hms.harvard.edu/explorer/
- category: GraphProduct
  description: BioPlex 3.0 human protein-protein interaction network from HEK293T
    cells (10,128 baits; nearly 120,000 interactions among nearly 15,000 proteins),
    keyed by Entrez Gene IDs and UniProt accessions with interaction probabilities.
  format: tsv
  id: bioplex.3.0-293t
  name: BioPlex 3.0 Interactions (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 12866060
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_293T_Network_10K_Dec_2019.tsv
- category: GraphProduct
  description: BioPlex human protein-protein interaction network from HCT116 cells
    (5,522 baits; about 71,000 interactions among 10,531 proteins), keyed by Entrez
    Gene IDs and UniProt accessions with interaction probabilities.
  format: tsv
  id: bioplex.3.0-hct116
  name: BioPlex 3.0 Interactions (HCT116)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 7714364
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_HCT116_Network_5.5K_Dec_2019.tsv
- category: GraphProduct
  description: BioPlex 2.0 human protein-protein interaction network from HEK293T
    cells (5,891 baits; about 57,000 interactions among about 11,000 proteins).
  format: tsv
  id: bioplex.2.0-293t
  name: BioPlex 2.0 Interactions (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 5485753
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_interactionList_v4a.tsv
- category: GraphProduct
  description: BioPlex 1.0 human protein-protein interaction network from HEK293T
    cells (2,594 baits; about 24,000 interactions among about 8,000 proteins).
  format: tsv
  id: bioplex.1.0-293t
  name: BioPlex 1.0 Interactions (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 2329777
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_interactionList_v2.tsv
- category: GraphProduct
  description: BioPlex 3.0 network (HEK293T) as directed bait-prey edges, with bait
    and prey Entrez Gene IDs and symbols.
  format: tsv
  id: bioplex.3.0-293t-directed
  name: BioPlex 3.0 Directed Edges (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 4308432
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_3.0_293T_DirectedEdges.tsv
- category: GraphProduct
  description: BioPlex 3.0 network (HCT116) as directed bait-prey edges, with bait
    and prey Entrez Gene IDs and symbols.
  format: tsv
  id: bioplex.3.0-hct116-directed
  name: BioPlex 3.0 Directed Edges (HCT116)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 2557223
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_3.0_HCT116_DirectedEdges.tsv
- category: GraphProduct
  description: BioPlex 2.0 network (HEK293T) as directed bait-prey edges, with bait
    and prey Entrez Gene IDs and symbols.
  format: tsv
  id: bioplex.2.0-293t-directed
  name: BioPlex 2.0 Directed Edges (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 1976325
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_2.0_293T_DirectedEdges.tsv
- category: GraphProduct
  description: BioPlex 1.0 network (HEK293T) as directed bait-prey edges, with bait
    and prey Entrez Gene IDs and symbols.
  format: tsv
  id: bioplex.1.0-293t-directed
  name: BioPlex 1.0 Directed Edges (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 805550
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_1.0_293T_DirectedEdges.tsv
- category: Product
  description: All candidate bait-prey pairs before background filtering, with CompPASS
    scores. The BioPlex site advises using these with caution.
  format: tsv
  id: bioplex.3.0-293t-unfiltered
  name: BioPlex 3.0 Unfiltered Bait-Prey Pairs (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 1191298612
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_BaitPreyPairs_noFilters_293T_10K_Dec_2019.tsv
- category: Product
  description: All candidate bait-prey pairs before background filtering, with CompPASS
    scores. The BioPlex site advises using these with caution.
  format: tsv
  id: bioplex.hct116-unfiltered
  name: BioPlex HCT116 Unfiltered Bait-Prey Pairs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 811749997
  product_url: https://bioplex.hms.harvard.edu/data/BioPlex_BaitPreyPairs_noFilters_HCT116_5.5K_Dec_2019.tsv
- category: Product
  description: All candidate bait-prey pairs before background filtering, with CompPASS
    scores. The BioPlex site advises using these with caution.
  format: tsv
  id: bioplex.2.0-293t-unfiltered
  name: BioPlex 2.0 Unfiltered Bait-Prey Pairs (HEK293T)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 621906318
  product_url: https://bioplex.hms.harvard.edu/data/BaitPreyPairs_noFilters_BP2a.tsv
- category: Product
  description: TMT-based protein abundance comparison between HEK293T and HCT116 cells,
    published with BioPlex 3.0.
  format: tsv
  id: bioplex.proteome-comparison
  name: HEK293T-HCT116 Proteome Comparison
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_file_size: 1771868
  product_url: https://bioplex.hms.harvard.edu/data/293T_HCT116_ProteomeComparison.tsv
- category: GraphicalInterface
  description: Web tool for downloading raw mass spectrometry data for up to 10 bait
    proteins per query.
  format: http
  id: bioplex.raw-data
  name: BioPlex Raw MS Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_url: https://bioplex.hms.harvard.edu/download.php
- category: ProcessProduct
  description: Comparative Proteomic Analysis Software Suite, the scoring method (NWD
    and Z scores) used to identify high-confidence interacting proteins in BioPlex;
    R implementation in cRomppass.
  format: r
  id: bioplex.comppass
  name: CompPASS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_url: https://github.com/dnusinow/cRomppass
- category: ProgrammingInterface
  description: Bioconductor data package giving R access to the BioPlex HEK293T and
    HCT116 networks, together with CORUM complexes and transcriptome and proteome
    data. Artistic-2.0 license.
  format: r
  id: bioplex.bioconductor
  name: BioPlex R Package (Bioconductor)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: corum
  product_url: https://bioconductor.org/packages/BioPlex/
- category: ProgrammingInterface
  description: Python package for accessing and analyzing BioPlex protein interaction
    data. MIT license.
  format: python
  id: bioplex.bioplexpy
  name: BioPlexPy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplex
  product_url: https://pypi.org/project/bioplexpy/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
publications:
- authors:
  - Huttlin EL
  - Bruckner RJ
  - Navarrete-Perea J
  - Cannon JR
  - Baltier K
  - Gebreab F
  - Gygi MP
  - Thornock A
  - Zarraga G
  - Tam S
  - Szpyt J
  - Gassaway BM
  - Panov A
  - Parzen H
  - Fu S
  - Golbazi A
  - Maenpaa E
  - Stricker K
  - Guha Thakurta S
  - Zhang T
  - Rad R
  - Pan J
  - Nusinow DP
  - Paulo JA
  - Schweppe DK
  - Vaites LP
  - Harper JW
  - Gygi SP
  doi: 10.1016/j.cell.2021.04.011
  id: PMID:33961781
  journal: Cell
  preferred: true
  title: Dual proteome-scale networks reveal cell-specific remodeling of the human
    interactome
  year: '2021'
- authors:
  - Huttlin EL
  - Bruckner RJ
  - Paulo JA
  - Cannon JR
  - Ting L
  - Baltier K
  - Colby G
  - Gebreab F
  - Gygi MP
  - Parzen H
  - Szpyt J
  - Tam S
  - Zarraga G
  - Pontano-Vaites L
  - Swarup S
  - White AE
  - Schweppe DK
  - Rad R
  - Erickson BK
  - Obar RA
  - Guruharsha KG
  - Li K
  - Artavanis-Tsakonas S
  - Gygi SP
  - Harper JW
  doi: 10.1038/nature22366
  id: PMID:28514442
  journal: Nature
  title: Architecture of the human interactome defines protein communities and disease
    networks
  year: '2017'
- authors:
  - Huttlin EL
  - Ting L
  - Bruckner RJ
  - Gebreab F
  - Gygi MP
  - Szpyt J
  - Tam S
  - Zarraga G
  - Colby G
  - Baltier K
  - Dong R
  - Guarani V
  - Vaites LP
  - Ordureau A
  - Rad R
  - Erickson BK
  - Wühr M
  - Chick J
  - Zhai B
  - Kolippakkam D
  - Mintseris J
  - Obar RA
  - Harris T
  - Artavanis-Tsakonas S
  - Sowa ME
  - De Camilli P
  - Paulo JA
  - Harper JW
  - Gygi SP
  doi: 10.1016/j.cell.2015.06.043
  id: PMID:26186194
  journal: Cell
  title: 'The BioPlex Network: A Systematic Exploration of the Human Interactome'
  year: '2015'
- authors:
  - Schweppe DK
  - Huttlin EL
  - Harper JW
  - Gygi SP
  doi: 10.1021/acs.jproteome.7b00572
  id: PMID:29054129
  journal: J Proteome Res
  title: 'BioPlex Display: An Interactive Suite for Large-Scale AP-MS Protein-Protein
    Interaction Data'
  year: '2018'
- authors:
  - Geistlinger L
  - Vargas R
  - Lee T
  - Pan J
  - Huttlin EL
  - Gentleman R
  doi: 10.1093/bioinformatics/btad091
  id: PMID:36794911
  journal: Bioinformatics
  title: 'BioPlexR and BioPlexPy: integrated data products for the analysis of human
    protein interactions'
  year: '2023'
synonyms:
- BioPlex Interactome
taxon:
- NCBITaxon:9606
---
# BioPlex

BioPlex (the BioPlex Interactome) maps human protein-protein interactions at proteome scale. Each bait protein is expressed from the human ORFeome (v8.1) with a C-terminal HA-FLAG tag, its interacting partners are captured by affinity purification and identified by mass spectrometry, and high-confidence interactions are scored with CompPASS. The project is a collaboration between the Gygi and Harper labs at Harvard Medical School, funded in part by NHGRI.

## Networks

- **BioPlex 1.0** (2015): about 24,000 interactions among about 8,000 proteins from 2,594 baits in HEK293T cells.
- **BioPlex 2.0** (2017): about 57,000 interactions among about 11,000 proteins from 5,891 baits in HEK293T cells.
- **BioPlex 3.0** (2021): nearly 120,000 interactions among nearly 15,000 proteins from 10,128 baits in HEK293T cells, plus a second network of about 71,000 interactions among 10,531 proteins from 5,522 baits in HCT116 cells.

Interaction tables identify proteins by Entrez Gene ID and UniProt accession. The site also offers unfiltered bait-prey pairs, directed bait-prey edges, bait lists, and unpublished quarterly releases for further cell lines (U2OS and RPE-1). For those unpublished releases, the site asks users not to publish large-scale analyses until the data appear in a peer-reviewed paper.

## Access and terms

The networks can be browsed in the BioPlex Explorer, downloaded as tab-separated files, or loaded with the BioPlex Bioconductor package (R) and BioPlexPy (Python), both maintained by the Center for Computational Biomedicine at Harvard Medical School. The site states no license for the published interaction data. It asks users to cite the corresponding publication for each network.