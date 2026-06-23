---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: chenc@udel.edu
  - contact_type: github
    value: chenchuming
  label: Chuming Chen
creation_date: '2026-01-23T00:00:00Z'
description: The Protein Knowledge Network (ProKN) integrates protein-centric data
  with the genomic-centric datasets of the Common Fund Data Ecosystem (CFDE), spanning
  heterogeneous biological data types across multiple domains to foster CFDE re-use
  and collaboration through enhanced connectivity and data integration, enabling new
  capabilities for functional genomics and systems-level understanding of disease
  mechanisms.
domains:
- proteomics
- genomics
- biomedical
- systems biology
homepage_url: https://research.bioinformatics.udel.edu/ProKN/
id: prokn
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: Protein Knowledge Network
products:
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
  description: GTEx expression anatomy nodes (GTEXEXP) used in ProKN
  format: csv
  id: prokn.gtexexp.anatomy.nodes
  name: ProKN GTEx Anatomy Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 6993
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.Anatomy.nodes.csv
- category: GraphProduct
  description: HuBMAP Azimuth anatomy nodes used in ProKN
  format: csv
  id: prokn.hmaz.anatomy.nodes
  name: ProKN HuBMAP Azimuth Anatomy Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 12730
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.nodes.csv
- category: GraphProduct
  description: IMEx complex nodes used in ProKN
  format: csv
  id: prokn.imex.complex.nodes
  name: ProKN IMEx Complex Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1381676
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Complex.nodes.csv
- category: GraphProduct
  description: IDG/TCRD compound-protein nodes used in ProKN
  format: csv
  id: prokn.idgp.compound.nodes
  name: ProKN TCRD Compound-Protein Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 83991029
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.nodes.csv
- category: GraphProduct
  description: IDG/TCRD compound-disease nodes used in ProKN
  format: csv
  id: prokn.idgd.compound.nodes
  name: ProKN TCRD Compound-Disease Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 105796
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.nodes.csv
- category: GraphProduct
  description: HuBMAP Azimuth anatomy to heart marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_heart.gene.edges
  name: ProKN HuBMAP Azimuth Heart Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 48364
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_HEART.Gene.edges.csv
- category: GraphProduct
  description: HuBMAP Azimuth anatomy to kidney marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_kidney.gene.edges
  name: ProKN HuBMAP Azimuth Kidney Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 126963
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_KIDNEY.Gene.edges.csv
- category: GraphProduct
  description: HuBMAP Azimuth anatomy to liver marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_liver.gene.edges
  name: ProKN HuBMAP Azimuth Liver Marker Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hubmap.azimuth
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 56732
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HMAZ.Anatomy.HAS_MARKER_GENE_IN_LIVER.Gene.edges.csv
- category: GraphProduct
  description: TCRD compound bioactivity to protein edges
  format: csv
  id: prokn.idgp.compound.bioactivity.protein.edges
  name: ProKN TCRD Compound-Protein Bioactivity Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 128158013
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.BIOACTIVITY.Protein.edges.csv
- category: GraphProduct
  description: LINCS compound similarity edges
  format: csv
  id: prokn.lincs.compound.in_similarity_relationship_with.compound.edges
  name: ProKN LINCS Compound Similarity Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 6193189
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.IN_SIMILARITY_RELATIONSHIP_WITH.Compound.edges.csv
- category: GraphProduct
  description: TCRD compound indication edges to disease and phenotype terms
  format: csv
  id: prokn.idgd.compound.indication.diseaseorphenotype.edges
  name: ProKN TCRD Compound-Disease Indication Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1686928
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.INDICATION.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: LINCS compound negatively regulates gene edges
  format: csv
  id: prokn.lincs.compound.negatively_regulates.gene.edges
  name: ProKN LINCS Negative Regulation Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 28342168
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.NEGATIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: LINCS compound positively regulates gene edges
  format: csv
  id: prokn.lincs.compound.positively_regulates.gene.edges
  name: ProKN LINCS Positive Regulation Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 28223124
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.POSITIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: PIR compound exact match edges
  format: csv
  id: prokn.pir.compound.skos_exact_match.compound.edges
  name: ProKN PIR Compound Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 100170454
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Compound.SKOS_EXACT_MATCH.Compound.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impchumangene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: InterPro domain is_a domain edges
  format: csv
  id: prokn.interpro.domain.is_a.domain.edges
  name: ProKN InterPro Domain Hierarchy Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 171040
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/InterPro.Domain.IS_A.Domain.edges.csv
- category: GraphProduct
  description: HPO gene-to-phenotype association edges
  format: csv
  id: prokn.hgnchpo.gene.associated_with.diseaseorphenotype.edges
  name: ProKN HPO Gene-to-Phenotype Association Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hp.genes_to_phenotype.txt
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 155778514
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HGNCHPO.Gene.ASSOCIATED_WITH.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: GTEx gene expressed in anatomy edges
  format: csv
  id: prokn.gtexexp.gene.expressed_in.anatomy.edges
  name: ProKN GTEx Gene Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 341113044
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.Gene.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: ClinVar gene associated with disease/phenotype edges
  format: csv
  id: prokn.clinvar.gene.associated_with.diseaseorphenotype.edges
  name: ProKN ClinVar Association Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 16911644
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_CLINVAR.Gene.GENE_ASSOCIATED_WITH_DISEASE_OR_PHENOTYPE.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: HGNC to UniProt gene is_protein edges
  format: csv
  id: prokn.hgncuniprot.gene.is_protein.protein.edges
  name: ProKN HGNC UniProt Gene-Protein Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1750609
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_HGNCUNIPROT.Gene.IS_PROTEIN.Protein.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impc_gene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4832630
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
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
  description: GO term hierarchy edges
  format: csv
  id: prokn.go.goterm.is_a.goterm.edges
  name: ProKN GO Term Hierarchy Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 11917762
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.GOTerm.IS_A.GOTerm.edges.csv
- category: GraphProduct
  description: GTEx expression to anatomy edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.anatomy.edges
  name: ProKN GTExEXP Anatomy Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 406384547
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: GTEx expression to gene edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.gene.edges
  name: ProKN GTExEXP Gene Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 386708211
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.EXPRESSED_IN.Gene.edges.csv
- category: GraphProduct
  description: GTEx expression to expression bins edges
  format: csv
  id: prokn.gtexexp.gtexexp.has_expression.expbins.edges
  name: ProKN GTExEXP Expression Bin Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 413542626
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.HAS_EXPRESSION.EXPBINS.edges.csv
- category: GraphProduct
  description: IMPC allele to mouse gene edges
  format: csv
  id: prokn.impc.impcallele.impc_ensembl_id.impcmousegene.edges
  name: ProKN IMPC Allele to Mouse Gene Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 30886543
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcAllele.IMPC_ENSEMBL_ID.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with human gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impchumangene.edges
  name: ProKN IMPC Human-Human Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1268784667
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Human-Mouse Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 8283231
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene orthologous to mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.orthologous_to.impcmousegene.edges
  name: ProKN IMPC Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 16772307
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: PIR IMPC human gene orthologous to protein edges
  format: csv
  id: prokn.pir.impchumangene.orthologous_to.protein.edges
  name: ProKN PIR Human Gene to Protein Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18025933
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.Protein.edges.csv
- category: GraphProduct
  description: PIR IMPC mouse gene has gene product protein edges
  format: csv
  id: prokn.pir.impcmousegene.has_gene_product.protein.edges
  name: ProKN PIR Mouse Gene Product Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 19465205
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcMouseGene.BIOLINK_HAS_GENE_PRODUCT.Protein.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with human gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impchumangene.edges
  name: ProKN IMPC Mouse-Human Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 26416649
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Mouse-Mouse Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 354264338
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene orthologous to human gene edges
  format: csv
  id: prokn.impc.impcmousegene.orthologous_to.impchumangene.edges
  name: ProKN IMPC Mouse-Human Ortholog Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 5761243
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_HUMAN_GENE_ORTHOLOGUES.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele ID edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_allele_id.impcallele.edges
  name: ProKN IMPC Mouse Allele ID Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 2428378
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELE_ID.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele membership edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_alleles.impcallele.edges
  name: ProKN IMPC Mouse Alleles Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 29340516
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELES.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC publication allele edges
  format: csv
  id: prokn.impc.imppublication.impc_alleles.impcallele.edges
  name: ProKN IMPC Publication Allele Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4211083
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcPublication.IMPC_ALLELES.ImpcAllele.edges.csv
- category: GraphProduct
  description: MSIGDB chromosome band contains gene edges
  format: csv
  id: prokn.msigdb.msigdb.chr_band_contains_gene.gene.edges
  name: ProKN MSIGDB Chromosome Band Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 5090569
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_MSIGDB.MSigDB.CHR_BAND_CONTAINS_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB marker gene edges
  format: csv
  id: prokn.msigdb.msigdb.has_marker_gene.gene.edges
  name: ProKN MSIGDB Marker Gene Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 24846141
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_MSIGDB.MSigDB.HAS_MARKER_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB signature gene edges
  format: csv
  id: prokn.msigdb.msigdb.has_signature_gene.gene.edges
  name: ProKN MSIGDB Signature Gene Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1690507
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_MSIGDB.MSigDB.HAS_SIGNATURE_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB pathway associated with gene edges
  format: csv
  id: prokn.msigdb.msigdb.pathway_associated_with_gene.gene.edges
  name: ProKN MSIGDB Pathway Gene Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 125939588
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_MSIGDB.MSigDB.PATHWAY_ASSOCIATED_WITH_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB targets expression of gene edges
  format: csv
  id: prokn.msigdb.msigdb.targets_expression_of_gene.gene.edges
  name: ProKN MSIGDB Targets Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 156490605
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_MSIGDB.MSigDB.TARGETS_EXPRESSION_OF_GENE.Gene.edges.csv
- category: GraphProduct
  description: Reactome pathway event hierarchy edges
  format: csv
  id: prokn.reactome.pathway.event_of.pathway.edges
  name: ProKN Reactome Pathway Event Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1088495
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Pathway.PATHWAY_EVENT_OF.Pathway.edges.csv
- category: GraphProduct
  description: LINCS P100 perturbagen experiment edges
  format: csv
  id: prokn.lincs_p100.perturbagen.is_used_in.experiment.edges
  name: ProKN LINCS P100 Perturbagen Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 541848
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Perturbagen.IS_USED_IN.Experiment.edges.csv
- category: GraphProduct
  description: LINCS P100 experiment perturbation effect on PTM site edges
  format: csv
  id: prokn.lincs_p100.experiment.perturbation_effect.ptmsite.edges
  name: ProKN LINCS P100 Perturbation Effect Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 52555993
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Experiment.PERTURBATION_EFFECT.PTMSite.edges.csv
- category: GraphProduct
  description: LINCS P100 PTM site is site of site edges
  format: csv
  id: prokn.lincs_p100.ptmsite.is_site.site.edges
  name: ProKN LINCS P100 PTM Site Mapping Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 980
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.PTMSite.IS_SITE.Site.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of GO term edges
  format: csv
  id: prokn.go.protein.acts_upstream_of.goterm.edges
  name: ProKN GO Acts Upstream Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 158931
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 10441
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Acts Upstream Or Within Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 714349
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4257
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Positive Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 13894
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Positive Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 32541
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.colocalizes_with.goterm.edges
  name: ProKN GO Colocalizes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 261555
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein contributes to GO term edges
  format: csv
  id: prokn.go.protein.contributes_to.goterm.edges
  name: ProKN GO Contributes To Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 310541
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein enables GO term edges
  format: csv
  id: prokn.go.protein.enables.goterm.edges
  name: ProKN GO Enables Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 53141599
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: InterPro protein has domain edges
  format: csv
  id: prokn.interpro.protein.has_domain.domain.edges
  name: ProKN InterPro Domain Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4696849
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/InterPro.Protein.HAS_DOMAIN.Domain.edges.csv
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
  description: iPTMnet protein has site edges
  format: csv
  id: prokn.iptmnet.protein.has_site.site.edges
  name: ProKN iPTMnet Protein Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 34132692
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.Protein.HAS_SITE.Site.edges.csv
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
  description: UniProtKB protein has site edges
  format: csv
  id: prokn.uniprotkb.protein.has_site.site.edges
  name: ProKN UniProtKB Protein Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 26846810
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/UniProtKB.Protein.HAS_SITE.Site.edges.csv
- category: GraphProduct
  description: UniProtKB protein variant edges
  format: csv
  id: prokn.uniprotkb.protein.has_variant.variant.edges
  name: ProKN UniProtKB Variant Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 19744738
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/UniProtKB.Protein.HAS_VARIANT.Variant.edges.csv
- category: GraphProduct
  description: eMIND protein variant edges
  format: csv
  id: prokn.emind.protein.has_variant.variant.edges
  name: ProKN eMIND Variant Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 60076
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Protein.HAS_VARIANT.Variant.edges.csv
- category: GraphProduct
  description: IMEx protein interacts with protein edges
  format: csv
  id: prokn.imex.protein.interacts_with.protein.edges
  name: ProKN IMEx Protein Interaction Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 363360000
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.INTERACTS_WITH.Protein.edges.csv
- category: GraphProduct
  description: GO protein involved in GO term edges
  format: csv
  id: prokn.go.protein.involved_in.goterm.edges
  name: ProKN GO Involved In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 43447452
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein active in GO term edges
  format: csv
  id: prokn.go.protein.is_active_in.goterm.edges
  name: ProKN GO Active In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1630623
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein located in GO term edges
  format: csv
  id: prokn.go.protein.located_in.goterm.edges
  name: ProKN GO Located In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 50784436
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Not Acts Upstream Or Within Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1796
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Not Acts Upstream Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 455
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.not_colocalizes_with.goterm.edges
  name: ProKN GO Not Colocalizes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3336
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not contributes to GO term edges
  format: csv
  id: prokn.go.protein.not_contributes_to.goterm.edges
  name: ProKN GO Not Contributes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3198
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not enables GO term edges
  format: csv
  id: prokn.go.protein.not_enables.goterm.edges
  name: ProKN GO Not Enables Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 129748
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not involved in GO term edges
  format: csv
  id: prokn.go.protein.not_involved_in.goterm.edges
  name: ProKN GO Not Involved In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 143198
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not active in GO term edges
  format: csv
  id: prokn.go.protein.not_is_active_in.goterm.edges
  name: ProKN GO Not Active In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 893
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not located in GO term edges
  format: csv
  id: prokn.go.protein.not_located_in.goterm.edges
  name: ProKN GO Not Located In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 52743
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not part of GO term edges
  format: csv
  id: prokn.go.protein.not_part_of.goterm.edges
  name: ProKN GO Not Part Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4731
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_PART_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein part of GO term edges
  format: csv
  id: prokn.go.protein.part_of.goterm.edges
  name: ProKN GO Part Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3629548
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.PART_OF.GOTerm.edges.csv
- category: GraphProduct
  description: IMEx protein participates in complex edges
  format: csv
  id: prokn.imex.protein.participates_in.complex.edges
  name: ProKN IMEx Protein Participates In Complex Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 18774312
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.PARTICIPATES_IN.Complex.edges.csv
- category: GraphProduct
  description: Reactome protein participates in pathway edges
  format: csv
  id: prokn.reactome.protein.participates_in.pathway.edges
  name: ProKN Reactome Protein Pathway Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 17112000
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Protein.PARTICIPATES_IN.Pathway.edges.csv
- category: GraphProduct
  description: iPTMnet protein catalyzes PTM site edges
  format: csv
  id: prokn.iptmnet.protein.catalyzes.ptmsite.edges
  name: ProKN iPTMnet Protein Catalyzes PTM Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4049194
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.Protein.CATALYZES.PTMSite.edges.csv
- category: GraphProduct
  description: eMIND variant associated with disease edges
  format: csv
  id: prokn.emind.variant.associated_with.disease.edges
  name: ProKN eMIND Variant Disease Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1665
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.ASSOCIATED_WITH.Disease.edges.csv
- category: GraphProduct
  description: eMIND variant impact on disease edges
  format: csv
  id: prokn.emind.variant.impact.disease.edges
  name: ProKN eMIND Variant Impact Disease Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 69659
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.IMPACT.Disease.edges.csv
- category: GraphProduct
  description: eMIND variant impact on protein edges
  format: csv
  id: prokn.emind.variant.impact.protein.edges
  name: ProKN eMIND Variant Impact Protein Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: emind
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1371
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.IMPACT.Protein.edges.csv
- category: GraphicalInterface
  description: Web explorer for the Protein Knowledge Network with interactive graph
    browsing
  format: http
  id: prokn.explorer
  name: Protein Knowledge Network Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/explorer
- category: Product
  description: Bulk downloads page listing current ProKN node and edge CSV exports
    with file sizes and update timestamps
  format: http
  id: prokn.downloads
  name: Protein Knowledge Network Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/downloads
- category: ProgrammingInterface
  description: REST API for the Protein Knowledge Network
  format: http
  id: prokn.api
  name: Protein Knowledge Network REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/restapi
- category: ProgrammingInterface
  description: Hosted Model Context Protocol endpoint for MCP-compatible clients accessing
    ProKN
  format: http
  id: prokn.mcp
  name: ProKN MCP Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/mcp
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for Protein Knowledge Network
  format: http
  id: prokn.tpf
  name: Protein Knowledge Network TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://apps.okn.us/ldf/prokn
- category: ProgrammingInterface
  description: SPARQL endpoint for Protein Knowledge Network
  format: http
  id: prokn.sparql
  name: Protein Knowledge Network SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_url: https://apps.okn.us/prokn/sparql
---
# Protein Knowledge Network

Protein Knowledge Network (ProKN) is a protein-centric knowledge graph that links CFDE datasets with curated biomedical resources spanning protein function, post-translational modification, pathway biology, gene expression, genotype-phenotype associations, and chemical perturbation data. The graph is designed to support cross-domain exploration of functional genomics and systems-level responses to perturbations.

The current public ProKN site exposes several complementary access paths. The network explorer supports interactive browsing, the REST API publishes resource-specific endpoints plus graph search operations, and the FRINK Triple Pattern Fragments endpoint provides linked-data access for graph-pattern queries. Bulk node and edge exports are indexed from the downloads page, which is the current authoritative landing page for public CSV exports.

Recent ProKN infrastructure also includes an MCP server implementation for AI clients. The MCP server source is published separately from the main website and documents both local deployment and the hosted MCP entry point used by compatible clients.

## Access Points

- Web explorer: [ProKN Explorer](https://research.bioinformatics.udel.edu/ProKN/explorer)
- Downloads catalog: [ProKN Downloads](https://research.bioinformatics.udel.edu/ProKN/downloads)
- REST API: [ProKN API docs](https://research.bioinformatics.udel.edu/ProKN/restapi)
- Triple Pattern Fragments: [FRINK ProKN TPF](https://frink.apps.renci.org/ldf/prokn)
- MCP endpoint: [ProKN MCP](https://research.bioinformatics.udel.edu/ProKN/mcp)

## Automated Evaluation

- View the automated evaluation: [prokn automated evaluation](prokn_eval_automated.html)