---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://glygen.org/contact-us/
  label: GlyGen Team
creation_date: '2025-05-04T00:00:00Z'
description: GlyGen is an integrated, data-driven resource for glycoproteins, glycans,
  and carbohydrate-active enzymes, providing researchers with comprehensive, high-quality
  data on glycobiology.
domains:
- chemistry and biochemistry
- biological systems
homepage_url: https://glygen.org/
id: glygen
last_modified_date: '2025-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: GlyGen
products:
- category: GraphicalInterface
  description: Web interface for exploring GlyGen data
  id: glygen.site
  is_public: true
  name: GlyGen Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  product_url: https://glygen.org/
- category: ProgrammingInterface
  description: RESTful API for accessing GlyGen data
  id: glygen.api
  is_public: true
  name: GlyGen API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  product_url: https://api.glygen.org/
- category: GraphicalInterface
  description: Interface for searching GlyGen protein and glycan data
  format: csv
  id: glygen.data.site
  name: GlyGen Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  product_url: https://data.glygen.org/
- category: GraphProduct
  compression: zip
  description: Nodes from GlyGen Biomarker Database
  format: csv
  id: biomarkerkg.nodes.biomarker
  name: BKG Biomarker Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarkerkg
  - relation_type: prov:hadPrimarySource
    source: glygen
  product_file_size: 1252064
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Biomarker.nodes.zip
- category: GraphProduct
  description: GlyGen amino acid nodes used in ProKN
  format: csv
  id: prokn.glygen.aminoacid.nodes
  name: ProKN GlyGen AminoAcid Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 853
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.AminoAcid.nodes.csv
- category: GraphProduct
  description: GlyGen glycoprotein glycosylated site edges
  format: csv
  id: prokn.glygen.glycoprotein.glycosylated_at.glycosylationsite.edges
  name: ProKN GlyGen Glycosylated Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 14046942
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Glycoprotein.GLYCOSYLATED_AT.GlycosylationSite.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein evidence edges
  format: csv
  id: prokn.glygen.glycoprotein.has_evidence.glycoproteinevidence.edges
  name: ProKN GlyGen Evidence Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 33863751
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Glycoprotein.HAS_EVIDENCE.GlycoproteinEvidence.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein PRO entry edges
  format: csv
  id: prokn.glygen.glycoprotein.has_pro_entry.gpid2pro.edges
  name: ProKN GlyGen PRO Entry Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 15557656
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Glycoprotein.HAS_PRO_ENTRY.GPID2PRO.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein isoform sequence edges
  format: csv
  id: prokn.glygen.glycoprotein.sequence.isoform.edges
  name: ProKN GlyGen Isoform Sequence Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 7097575
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Glycoprotein.SEQUENCE.Isoform.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein protein sequence edges
  format: csv
  id: prokn.glygen.glycoprotein.sequence.protein.edges
  name: ProKN GlyGen Protein Sequence Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 7773165
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Glycoprotein.SEQUENCE.Protein.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein evidence citation edges
  format: csv
  id: prokn.glygen.glycoproteinevidence.citation.glycoproteincitation.edges
  name: ProKN GlyGen Evidence Citation Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 571669
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.GlycoproteinEvidence.CITATION.GlycoproteinCitation.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation enzyme protein edges
  format: csv
  id: prokn.glygen.glycosylation.has_enzyme_protein.protein.edges
  name: ProKN GlyGen Enzyme Protein Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 23734
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glycosylation.HAS_ENZYME_PROTEIN.Protein.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation site saccharide edges
  format: csv
  id: prokn.glygen.glycosylationsite.has_saccharide.glytoucan.edges
  name: ProKN GlyGen Saccharide Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 11352916
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.GlycosylationSite.HAS_SACCHARIDE.Glytoucan.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation site location edges
  format: csv
  id: prokn.glygen.glycosylationsite.location.glygenlocation.edges
  name: ProKN GlyGen Site Location Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 12742560
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.GlycosylationSite.LOCATION.GlyGenLocation.edges.csv
- category: GraphProduct
  description: GlyGen glycosyltransferase reaction enzyme edges
  format: csv
  id: prokn.glygen.glycosyltransferasereaction.has_enzyme_protein_gr.protein.edges
  name: ProKN GlyGen Reaction Enzyme Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 25008
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.GlycosyltransferaseReaction.HAS_ENZYME_PROTEIN_GR.Protein.edges.csv
- category: GraphProduct
  description: GlyGen location amino acid edges
  format: csv
  id: prokn.glygen.glygenlocation.has_amino_acid.aminoacid.edges
  name: ProKN GlyGen Location Amino Acid Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 12480310
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.GlyGenLocation.HAS_AMINO_ACID.AminoAcid.edges.csv
- category: GraphProduct
  description: GlyGen residue attached by glycosylation edges
  format: csv
  id: prokn.glygen.glygenresidue.attached_by.glycosylation.edges
  name: ProKN GlyGen Residue Attachment Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 87915
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.GlyGenResidue.ATTACHED_BY.Glycosylation.edges.csv
- category: GraphProduct
  description: GlyGen residue parent edges
  format: csv
  id: prokn.glygen.glygenresidue.has_parent.glygenresidue.edges
  name: ProKN GlyGen Residue Parent Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18592
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.GlyGenResidue.HAS_PARENT.GlyGenResidue.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan canonical residue edges
  format: csv
  id: prokn.glygen.glytoucan.has_canonical_residue.glygenresidue.edges
  name: ProKN GlyGen Canonical Residue Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 21661105
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glytoucan.HAS_CANONICAL_RESIDUE.GlyGenResidue.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan glyco-sequence edges
  format: csv
  id: prokn.glygen.glytoucan.has_glycosequence.gyglycosequence.edges
  name: ProKN GlyGen Glycosequence Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 31816753
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glytoucan.HAS_GLYCOSEQUENCE.GlyGenGlycosequence.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan motif edges
  format: csv
  id: prokn.glygen.glytoucan.has_motif.glycanmotif.edges
  name: ProKN GlyGen Motif Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4403891
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glytoucan.HAS_MOTIF.GlycanMotif.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan source edges
  format: csv
  id: prokn.glygen.glytoucan.is_from_source.glygensrc.edges
  name: ProKN GlyGen Source Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 7768294
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glytoucan.IS_FROM_SOURCE.GlyGenSrc.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan synthesized by reaction edges
  format: csv
  id: prokn.glygen.glytoucan.synthesized_by.glycosyltransferasereaction.edges
  name: ProKN GlyGen Synthesized By Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 54721397
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GLYCANS.Glytoucan.SYNTHESIZED_BY.GlycosyltransferaseReaction.edges.csv
- category: GraphProduct
  description: GlyGen protein isoform edges
  format: csv
  id: prokn.glygen.protein.has_isoform.isoform.edges
  name: ProKN GlyGen Protein Isoform Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1357770
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Protein.HAS_ISOFORM.Isoform.edges.csv
- category: GraphProduct
  description: GlyGen protein isoform protein edges
  format: csv
  id: prokn.glygen.protein.has_isoform.protein.edges
  name: ProKN GlyGen Protein Isoform Protein Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 653113
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_PROTEOFORM.Protein.HAS_ISOFORM.Protein.edges.csv
- category: GraphProduct
  description: Neo4j knowledge graph containing integrated gene sets from multiple
    Common Fund programs with cross-references
  dump_format: neo4j
  format: neo4j
  id: cfde-gse.graph
  name: CFDE-GSE Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
- category: Product
  description: Standardized gene set collections from Common Fund programs in GMT
    format
  id: cfde-gse.genesets
  name: CFDE Gene Set Collections
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://gse.cfde.cloud/downloads/
- category: GraphProduct
  description: A comprehensive multi-omics biomedical knowledge graph connecting genomic,
    transcriptomic, proteomic, and clinical data. Contains over 32 million nodes and
    118 million relationships.
  dump_format: neo4j
  edge_count: 118000000
  id: petagraph.graph
  name: Petagraph Knowledge Graph (Neo4J)
  node_count: 32000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: petagraph
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_url: https://ubkg-downloads.xconsortia.org/
publications:
- authors:
  - Kahsay R
  - Vora J
  - Navelkar R
  - Mousavi R
  - Bittremieux W
  - Bakker H
  - Moremen K
  - Ten F
  - Abrahams D
  - Campbell M
  - Glushka J
  - Ranzinger R
  - York W
  - Haslam S
  - Dell A
  - Packer N
  - Bourne P
  - Azadi P
  - Aoki-Kinoshita K
  - Lisacek F
  - Tiemeyer M
  - Neelamegham S
  doi: doi:10.1093/glycob/cwaa085
  id: doi:10.1093/glycob/cwaa085
  preferred: true
  title: GlyGen - Computational and informatics resources for glycoscience
  year: '2020'
repository: https://github.com/glygener/glygen-backend-api
---
GlyGen is a data integration and dissemination project for carbohydrate and glycoconjugate related data. It provides researchers with a comprehensive, integrated, and unified resource for glycan and glycoprotein information, bringing together data from multiple international data sources and partners.

The database integrates information from multiple sources, including:
- Protein sequences and associated data from UniProt
- Glycan structures from GlyTouCan
- Protein-glycan associations from UniCarbKB
- Glycan binding information from UniLectin
- Carbohydrate enzyme data from CAZy

GlyGen provides both a web interface for human users and programmatic access via a RESTful API for computational applications. The resource supports complex queries across multiple data types and provides visualization tools for glycan structures and protein-glycan interactions.

GlyGen is a collaborative effort between the University of Georgia, George Washington University, and international partners, funded by the National Institutes of Health (NIH) through the National Institute of General Medical Sciences (NIGMS).