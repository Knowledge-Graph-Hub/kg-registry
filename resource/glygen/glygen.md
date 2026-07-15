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
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: GlyGen
products:
- category: GraphicalInterface
  description: Web interface for exploring GlyGen data
  format: http
  id: glygen.site
  is_public: true
  name: GlyGen Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glygen
  product_url: https://glygen.org/
- category: ProgrammingInterface
  description: RESTful API for accessing GlyGen data
  format: http
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
  id: biomarker.bkg.nodes.biomarker
  name: BKG Biomarker Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
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
  format: txt
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
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
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
- category: GraphProduct
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  format: http
  id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: digcfdekg
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: sparc
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hubmap
- category: Product
  compression: gzip
  description: PubChem substance information in ASN.1 format
  format: xml
  id: pubchem.substances.asn
  name: PubChem Substances ASN
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/ASN/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: clinvar
  - relation_type: prov:wasInfluencedBy
    source: dbsnp
  - relation_type: prov:wasInfluencedBy
    source: dgidb
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pharmgkb
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: unichem
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
- category: Product
  compression: gzip
  description: PubChem substance information in SDF format
  format: sdf
  id: pubchem.substances.sdf
  name: PubChem Substances SDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/SDF/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: clinvar
  - relation_type: prov:wasInfluencedBy
    source: dbsnp
  - relation_type: prov:wasInfluencedBy
    source: dgidb
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pharmgkb
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: unichem
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
publications:
- authors:
  - William S York
  - Raja Mazumder
  - Rene Ranzinger
  - Nathan Edwards
  - Robel Kahsay
  - Kiyoko F Aoki-Kinoshita
  - Matthew P Campbell
  - Richard D Cummings
  - Ten Feizi
  - Maria Martin
  - Darren A Natale
  - Nicolle H Packer
  - Robert J Woods
  - Gaurav Agarwal
  - Sena Arpinar
  - Sanath Bhat
  - Judith Blake
  - Leyla Jael Garcia Castro
  - Brian Fochtman
  - Jeffrey Gildersleeve
  - Radoslav Goldman
  - Xavier Holmes
  - Vinamra Jain
  - Sujeet Kulkarni
  - Rupali Mahadik
  - Akul Mehta
  - Reza Mousavi
  - Sandeep Nakarakommula
  - Rahi Navelkar
  - Nagarajan Pattabiraman
  - Michael J Pierce
  - Karen Ross
  - Preethi Vasudev
  - Jeet Vora
  - Tatiana Williamson
  - Wenjin Zhang
  doi: 10.1093/glycob/cwz080
  id: doi:10.1093/glycob/cwz080
  journal: Glycobiology
  preferred: true
  title: 'GlyGen: Computational and Informatics Resources for Glycoscience'
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