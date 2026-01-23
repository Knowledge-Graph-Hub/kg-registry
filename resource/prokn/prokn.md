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
  label: Chuming Chen
creation_date: '2026-01-23T00:00:00Z'
description: The Protein Knowledge Network (ProKN) integrates protein-centric data with Common Fund Data Ecosystem resources to link proteins, variants, pathways, and phenotypes for functional genomics and systems-level insights.
domains:
- proteomics
- genomics
- biomedical
- systems biology
products:
- category: GraphProduct
  description: GlyGen amino acid nodes used in ProKN
  format: csv
  id: prokn.glygen.aminoacid.nodes
  name: ProKN GlyGen AminoAcid Nodes
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.AminoAcid.nodes.csv
- category: GraphProduct
  description: GTEx expression anatomy nodes (GTEXEXP) used in ProKN
  format: csv
  id: prokn.gtexexp.anatomy.nodes
  name: ProKN GTEx Anatomy Nodes
  original_source:
  - gtex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GTEXEXP.Anatomy.nodes.csv
- category: GraphProduct
  description: HMAZ anatomy nodes used in ProKN
  format: csv
  id: prokn.hmaz.anatomy.nodes
  name: ProKN HMAZ Anatomy Nodes
  original_source:
  - hmaz
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HMAZ.Anatomy.nodes.csv
- category: GraphProduct
  description: IMEx complex nodes used in ProKN
  format: csv
  id: prokn.imex.complex.nodes
  name: ProKN IMEx Complex Nodes
  original_source:
  - imex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Complex.nodes.csv
- category: GraphProduct
  description: IDG compound-protein nodes (IDGP) used in ProKN
  format: csv
  id: prokn.idgp.compound.nodes
  name: ProKN IDGP Compound Nodes
  original_source:
  - idgp
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IDGP.Compound.nodes.csv
- category: GraphProduct
  description: IDG compound-disease nodes (IDGD) used in ProKN
  format: csv
  id: prokn.idgd.compound.nodes
  name: ProKN IDGD Compound Nodes
  original_source:
  - idgd
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IDGD.Compound.nodes.csv
- category: GraphProduct
  description: HMAZ anatomy to heart marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_heart.gene.edges
  name: ProKN HMAZ Heart Marker Edges
  original_source:
  - hmaz
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HMAZ.Anatomy.HAS_MARKER_GENE_IN_HEART.Gene.edges.csv
- category: GraphProduct
  description: HMAZ anatomy to kidney marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_kidney.gene.edges
  name: ProKN HMAZ Kidney Marker Edges
  original_source:
  - hmaz
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HMAZ.Anatomy.HAS_MARKER_GENE_IN_KIDNEY.Gene.edges.csv
- category: GraphProduct
  description: HMAZ anatomy to liver marker gene edges
  format: csv
  id: prokn.hmaz.anatomy.has_marker_gene_in_liver.gene.edges
  name: ProKN HMAZ Liver Marker Edges
  original_source:
  - hmaz
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HMAZ.Anatomy.HAS_MARKER_GENE_IN_LIVER.Gene.edges.csv
- category: GraphProduct
  description: IDGP compound bioactivity to protein edges
  format: csv
  id: prokn.idgp.compound.bioactivity.protein.edges
  name: ProKN IDGP Bioactivity Edges
  original_source:
  - idgp
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IDGP.Compound.BIOACTIVITY.Protein.edges.csv
- category: GraphProduct
  description: LINCS compound similarity edges
  format: csv
  id: prokn.lincs.compound.in_similarity_relationship_with.compound.edges
  name: ProKN LINCS Compound Similarity Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS.Compound.IN_SIMILARITY_RELATIONSHIP_WITH.Compound.edges.csv
- category: GraphProduct
  description: IDGD compound indication edges to disease/phenotype
  format: csv
  id: prokn.idgd.compound.indication.diseaseorphenotype.edges
  name: ProKN IDGD Indication Edges
  original_source:
  - idgd
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IDGD.Compound.INDICATION.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: LINCS compound negatively regulates gene edges
  format: csv
  id: prokn.lincs.compound.negatively_regulates.gene.edges
  name: ProKN LINCS Negative Regulation Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS.Compound.NEGATIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: LINCS compound positively regulates gene edges
  format: csv
  id: prokn.lincs.compound.positively_regulates.gene.edges
  name: ProKN LINCS Positive Regulation Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS.Compound.POSITIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: PIR compound targets protein edges
  format: csv
  id: prokn.pir.compound.targets.protein.edges
  name: ProKN PIR Compound Targets Edges
  original_source:
  - pir
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Compound.TARGETS.Protein.edges.csv
- category: GraphProduct
  description: PIR disease exact match to disease/phenotype edges
  format: csv
  id: prokn.pir.disease.skos_exact_match.diseaseorphenotype.edges
  name: ProKN PIR Disease Exact Match Edges
  original_source:
  - pir
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Disease.SKOS_EXACT_MATCH.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: InterPro domain is_a domain edges
  format: csv
  id: prokn.interpro.domain.is_a.domain.edges
  name: ProKN InterPro Domain Hierarchy Edges
  original_source:
  - interpro
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/InterPro.Domain.IS_A.Domain.edges.csv
- category: GraphProduct
  description: HGNCHPO gene associated with disease/phenotype edges
  format: csv
  id: prokn.hgnchpo.gene.associated_with.diseaseorphenotype.edges
  name: ProKN HGNCHPO Association Edges
  original_source:
  - hgnchpo
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HGNCHPO.Gene.ASSOCIATED_WITH.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: GTEx gene expressed in anatomy edges
  format: csv
  id: prokn.gtexexp.gene.expressed_in.anatomy.edges
  name: ProKN GTEx Gene Expression Edges
  original_source:
  - gtex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GTEXEXP.Gene.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: ClinVar gene associated with disease/phenotype edges
  format: csv
  id: prokn.clinvar.gene.associated_with.diseaseorphenotype.edges
  name: ProKN ClinVar Association Edges
  original_source:
  - clinvar
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/CLINVAR.Gene.GENE_ASSOCIATED_WITH_DISEASE_OR_PHENOTYPE.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: HGNC to UniProt gene is_protein edges
  format: csv
  id: prokn.hgncuniprot.gene.is_protein.protein.edges
  name: ProKN HGNC UniProt Gene-Protein Edges
  original_source:
  - hgnc
  - uniprot
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/HGNCUNIPROT.Gene.IS_PROTEIN.Protein.edges.csv
- category: GraphProduct
  description: PIR gene exact match to IMPC human gene edges
  format: csv
  id: prokn.pir.gene.skos_exact_match.impc_gene.edges
  name: ProKN PIR Gene Exact Match Edges
  original_source:
  - pir
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.Gene.SKOS_EXACT_MATCH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein glycosylated site edges
  format: csv
  id: prokn.glygen.glycoprotein.glycosylated_at.glycosylationsite.edges
  name: ProKN GlyGen Glycosylated Site Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycoprotein.GLYCOSYLATED_AT.GlycosylationSite.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein evidence edges
  format: csv
  id: prokn.glygen.glycoprotein.has_evidence.glycoproteinevidence.edges
  name: ProKN GlyGen Evidence Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycoprotein.HAS_EVIDENCE.GlycoproteinEvidence.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein PRO entry edges
  format: csv
  id: prokn.glygen.glycoprotein.has_pro_entry.gpid2pro.edges
  name: ProKN GlyGen PRO Entry Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycoprotein.HAS_PRO_ENTRY.GPID2PRO.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein isoform sequence edges
  format: csv
  id: prokn.glygen.glycoprotein.sequence.isoform.edges
  name: ProKN GlyGen Isoform Sequence Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycoprotein.SEQUENCE.Isoform.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein protein sequence edges
  format: csv
  id: prokn.glygen.glycoprotein.sequence.protein.edges
  name: ProKN GlyGen Protein Sequence Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycoprotein.SEQUENCE.Protein.edges.csv
- category: GraphProduct
  description: GlyGen glycoprotein evidence citation edges
  format: csv
  id: prokn.glygen.glycoproteinevidence.citation.glycoproteincitation.edges
  name: ProKN GlyGen Evidence Citation Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlycoproteinEvidence.CITATION.GlycoproteinCitation.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation enzyme protein edges
  format: csv
  id: prokn.glygen.glycosylation.has_enzyme_protein.protein.edges
  name: ProKN GlyGen Enzyme Protein Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glycosylation.HAS_ENZYME_PROTEIN.Protein.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation site saccharide edges
  format: csv
  id: prokn.glygen.glycosylationsite.has_saccharide.glytoucan.edges
  name: ProKN GlyGen Saccharide Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlycosylationSite.HAS_SACCHARIDE.Glytoucan.edges.csv
- category: GraphProduct
  description: GlyGen glycosylation site location edges
  format: csv
  id: prokn.glygen.glycosylationsite.location.glygenlocation.edges
  name: ProKN GlyGen Site Location Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlycosylationSite.LOCATION.GlyGenLocation.edges.csv
- category: GraphProduct
  description: GlyGen glycosyltransferase reaction enzyme edges
  format: csv
  id: prokn.glygen.glycosyltransferasereaction.has_enzyme_protein_gr.protein.edges
  name: ProKN GlyGen Reaction Enzyme Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlycosyltransferaseReaction.HAS_ENZYME_PROTEIN_GR.Protein.edges.csv
- category: GraphProduct
  description: GlyGen location amino acid edges
  format: csv
  id: prokn.glygen.glygenlocation.has_amino_acid.aminoacid.edges
  name: ProKN GlyGen Location Amino Acid Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlyGenLocation.HAS_AMINO_ACID.AminoAcid.edges.csv
- category: GraphProduct
  description: GlyGen residue attached by glycosylation edges
  format: csv
  id: prokn.glygen.glygenresidue.attached_by.glycosylation.edges
  name: ProKN GlyGen Residue Attachment Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlyGenResidue.ATTACHED_BY.Glycosylation.edges.csv
- category: GraphProduct
  description: GlyGen residue parent edges
  format: csv
  id: prokn.glygen.glygenresidue.has_parent.glygenresidue.edges
  name: ProKN GlyGen Residue Parent Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.GlyGenResidue.HAS_PARENT.GlyGenResidue.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan canonical residue edges
  format: csv
  id: prokn.glygen.glytoucan.has_canonical_residue.glygenresidue.edges
  name: ProKN GlyGen Canonical Residue Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glytoucan.HAS_CANONICAL_RESIDUE.GlyGenResidue.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan glyco-sequence edges
  format: csv
  id: prokn.glygen.glytoucan.has_glycosequence.gyglycosequence.edges
  name: ProKN GlyGen Glycosequence Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glytoucan.HAS_GLYCOSEQUENCE.GlyGenGlycosequence.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan motif edges
  format: csv
  id: prokn.glygen.glytoucan.has_motif.glycanmotif.edges
  name: ProKN GlyGen Motif Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glytoucan.HAS_MOTIF.GlycanMotif.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan source edges
  format: csv
  id: prokn.glygen.glytoucan.is_from_source.glygensrc.edges
  name: ProKN GlyGen Source Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glytoucan.IS_FROM_SOURCE.GlyGenSrc.edges.csv
- category: GraphProduct
  description: GlyGen glytoucan synthesized by reaction edges
  format: csv
  id: prokn.glygen.glytoucan.synthesized_by.glycosyltransferasereaction.edges
  name: ProKN GlyGen Synthesized By Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Glytoucan.SYNTHESIZED_BY.GlycosyltransferaseReaction.edges.csv
- category: GraphProduct
  description: GO term hierarchy edges
  format: csv
  id: prokn.go.goterm.is_a.goterm.edges
  name: ProKN GO Term Hierarchy Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.GOTerm.IS_A.GOTerm.edges.csv
- category: GraphProduct
  description: GTEx expression to anatomy edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.anatomy.edges
  name: ProKN GTExEXP Anatomy Expression Edges
  original_source:
  - gtex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GTEXEXP.GTExEXP.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: GTEx expression to gene edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.gene.edges
  name: ProKN GTExEXP Gene Expression Edges
  original_source:
  - gtex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GTEXEXP.GTExEXP.EXPRESSED_IN.Gene.edges.csv
- category: GraphProduct
  description: GTEx expression to expression bins edges
  format: csv
  id: prokn.gtexexp.gtexexp.has_expression.expbins.edges
  name: ProKN GTExEXP Expression Bin Edges
  original_source:
  - gtex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GTEXEXP.GTExEXP.HAS_EXPRESSION.EXPBINS.edges.csv
- category: GraphProduct
  description: IMPC allele to mouse gene edges
  format: csv
  id: prokn.impc.impcallele.impc_ensembl_id.impcmousegene.edges
  name: ProKN IMPC Allele to Mouse Gene Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcAllele.IMPC_ENSEMBL_ID.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with human gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impchumangene.edges
  name: ProKN IMPC Human-Human Interaction Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC human gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Human-Mouse Interaction Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC human gene orthologous to mouse gene edges
  format: csv
  id: prokn.impc.impchumangene.orthologous_to.impcmousegene.edges
  name: ProKN IMPC Ortholog Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: PIR IMPC human gene orthologous to protein edges
  format: csv
  id: prokn.pir.impchumangene.orthologous_to.protein.edges
  name: ProKN PIR Human Gene to Protein Ortholog Edges
  original_source:
  - pir
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcHumanGene.BIOLINK_ORTHOLOGOUS_TO.Protein.edges.csv
- category: GraphProduct
  description: PIR IMPC mouse gene has gene product protein edges
  format: csv
  id: prokn.pir.impcmousegene.has_gene_product.protein.edges
  name: ProKN PIR Mouse Gene Product Edges
  original_source:
  - pir
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/PIR.ImpcMouseGene.BIOLINK_HAS_GENE_PRODUCT.Protein.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with human gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impchumangene.edges
  name: ProKN IMPC Mouse-Human Interaction Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene interacts with mouse gene edges
  format: csv
  id: prokn.impc.impcmousegene.interacts_with.impcmousegene.edges
  name: ProKN IMPC Mouse-Mouse Interaction Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.BIOLINK_INTERACTS_WITH.ImpcMouseGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene orthologous to human gene edges
  format: csv
  id: prokn.impc.impcmousegene.orthologous_to.impchumangene.edges
  name: ProKN IMPC Mouse-Human Ortholog Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_HUMAN_GENE_ORTHOLOGUES.ImpcHumanGene.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele ID edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_allele_id.impcallele.edges
  name: ProKN IMPC Mouse Allele ID Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELE_ID.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC mouse gene allele membership edges
  format: csv
  id: prokn.impc.impcmousegene.impc_mouse_alleles.impcallele.edges
  name: ProKN IMPC Mouse Alleles Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcMouseGene.IMPC_MOUSE_ALLELES.ImpcAllele.edges.csv
- category: GraphProduct
  description: IMPC publication allele edges
  format: csv
  id: prokn.impc.imppublication.impc_alleles.impcallele.edges
  name: ProKN IMPC Publication Allele Edges
  original_source:
  - impc
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMPC.ImpcPublication.IMPC_ALLELES.ImpcAllele.edges.csv
- category: GraphProduct
  description: MSIGDB chromosome band contains gene edges
  format: csv
  id: prokn.msigdb.msigdb.chr_band_contains_gene.gene.edges
  name: ProKN MSIGDB Chromosome Band Edges
  original_source:
  - msigdb
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/MSIGDB.MSigDB.CHR_BAND_CONTAINS_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB marker gene edges
  format: csv
  id: prokn.msigdb.msigdb.has_marker_gene.gene.edges
  name: ProKN MSIGDB Marker Gene Edges
  original_source:
  - msigdb
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/MSIGDB.MSigDB.HAS_MARKER_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB signature gene edges
  format: csv
  id: prokn.msigdb.msigdb.has_signature_gene.gene.edges
  name: ProKN MSIGDB Signature Gene Edges
  original_source:
  - msigdb
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/MSIGDB.MSigDB.HAS_SIGNATURE_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB pathway associated with gene edges
  format: csv
  id: prokn.msigdb.msigdb.pathway_associated_with_gene.gene.edges
  name: ProKN MSIGDB Pathway Gene Edges
  original_source:
  - msigdb
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/MSIGDB.MSigDB.PATHWAY_ASSOCIATED_WITH_GENE.Gene.edges.csv
- category: GraphProduct
  description: MSIGDB targets expression of gene edges
  format: csv
  id: prokn.msigdb.msigdb.targets_expression_of_gene.gene.edges
  name: ProKN MSIGDB Targets Expression Edges
  original_source:
  - msigdb
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/MSIGDB.MSigDB.TARGETS_EXPRESSION_OF_GENE.Gene.edges.csv
- category: GraphProduct
  description: Reactome pathway event hierarchy edges
  format: csv
  id: prokn.reactome.pathway.event_of.pathway.edges
  name: ProKN Reactome Pathway Event Edges
  original_source:
  - reactome
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Pathway.PATHWAY_EVENT_OF.Pathway.edges.csv
- category: GraphProduct
  description: LINCS P100 perturbagen experiment edges
  format: csv
  id: prokn.lincs_p100.perturbagen.is_used_in.experiment.edges
  name: ProKN LINCS P100 Perturbagen Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Perturbagen.IS_USED_IN.Experiment.edges.csv
- category: GraphProduct
  description: LINCS P100 phosphosite down-regulated edges
  format: csv
  id: prokn.lincs_p100.phosphosite.down_regulated.experiment.edges
  name: ProKN LINCS P100 Down Regulated Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Phosphosite.DOWN_REGULATED.Experiment.edges.csv
- category: GraphProduct
  description: LINCS P100 phosphosite site-of protein edges
  format: csv
  id: prokn.lincs_p100.phosphosite.is_site_of.protein.edges
  name: ProKN LINCS P100 Site Of Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Phosphosite.IS_SITE_OF.Protein.edges.csv
- category: GraphProduct
  description: LINCS P100 phosphosite unregulated edges
  format: csv
  id: prokn.lincs_p100.phosphosite.unregulated.experiment.edges
  name: ProKN LINCS P100 Unregulated Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Phosphosite.UNREGULATED.Experiment.edges.csv
- category: GraphProduct
  description: LINCS P100 phosphosite up-regulated edges
  format: csv
  id: prokn.lincs_p100.phosphosite.up_regulated.experiment.edges
  name: ProKN LINCS P100 Up Regulated Edges
  original_source:
  - lincs
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Phosphosite.UP_REGULATED.Experiment.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of GO term edges
  format: csv
  id: prokn.go.protein.acts_upstream_of.goterm.edges
  name: ProKN GO Acts Upstream Of Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Negative Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Acts Upstream Or Within Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Negative Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Positive Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Positive Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.colocalizes_with.goterm.edges
  name: ProKN GO Colocalizes Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein contributes to GO term edges
  format: csv
  id: prokn.go.protein.contributes_to.goterm.edges
  name: ProKN GO Contributes To Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein enables GO term edges
  format: csv
  id: prokn.go.protein.enables.goterm.edges
  name: ProKN GO Enables Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: InterPro protein has domain edges
  format: csv
  id: prokn.interpro.protein.has_domain.domain.edges
  name: ProKN InterPro Domain Edges
  original_source:
  - interpro
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/InterPro.Protein.HAS_DOMAIN.Domain.edges.csv
- category: GraphProduct
  description: GlyGen protein isoform edges
  format: csv
  id: prokn.glygen.protein.has_isoform.isoform.edges
  name: ProKN GlyGen Protein Isoform Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Protein.HAS_ISOFORM.Isoform.edges.csv
- category: GraphProduct
  description: iPTMnet protein isoform edges
  format: csv
  id: prokn.iptmnet.protein.has_isoform.protein.edges
  name: ProKN iPTMnet Protein Isoform Edges
  original_source:
  - iptmnet
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.Protein.HAS_ISOFORM.Protein.edges.csv
- category: GraphProduct
  description: GlyGen protein isoform protein edges
  format: csv
  id: prokn.glygen.protein.has_isoform.protein.edges
  name: ProKN GlyGen Protein Isoform Protein Edges
  original_source:
  - glygen
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GlyGen.Protein.HAS_ISOFORM.Protein.edges.csv
- category: GraphProduct
  description: UniProtKB protein PTM edges
  format: csv
  id: prokn.uniprotkb.protein.has_ptm.ptm.edges
  name: ProKN UniProtKB PTM Edges
  original_source:
  - uniprot
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/UniProtKB.Protein.HAS_PTM.PTM.edges.csv
- category: GraphProduct
  description: UniProtKB protein variant edges
  format: csv
  id: prokn.uniprotkb.protein.has_variant.variant.edges
  name: ProKN UniProtKB Variant Edges
  original_source:
  - uniprot
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/UniProtKB.Protein.HAS_VARIANT.Variant.edges.csv
- category: GraphProduct
  description: eMIND protein variant edges
  format: csv
  id: prokn.emind.protein.has_variant.variant.edges
  name: ProKN eMIND Variant Edges
  original_source:
  - emind
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Protein.HAS_VARIANT.Variant.edges.csv
- category: GraphProduct
  description: IMEx protein interacts with protein edges
  format: csv
  id: prokn.imex.protein.interacts_with.protein.edges
  name: ProKN IMEx Protein Interaction Edges
  original_source:
  - imex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.INTERACTS_WITH.Protein.edges.csv
- category: GraphProduct
  description: GO protein involved in GO term edges
  format: csv
  id: prokn.go.protein.involved_in.goterm.edges
  name: ProKN GO Involved In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein active in GO term edges
  format: csv
  id: prokn.go.protein.is_active_in.goterm.edges
  name: ProKN GO Active In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein located in GO term edges
  format: csv
  id: prokn.go.protein.located_in.goterm.edges
  name: ProKN GO Located In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Not Acts Upstream Or Within Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Not Acts Upstream Negative Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.not_colocalizes_with.goterm.edges
  name: ProKN GO Not Colocalizes Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not contributes to GO term edges
  format: csv
  id: prokn.go.protein.not_contributes_to.goterm.edges
  name: ProKN GO Not Contributes Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not enables GO term edges
  format: csv
  id: prokn.go.protein.not_enables.goterm.edges
  name: ProKN GO Not Enables Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not involved in GO term edges
  format: csv
  id: prokn.go.protein.not_involved_in.goterm.edges
  name: ProKN GO Not Involved In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not active in GO term edges
  format: csv
  id: prokn.go.protein.not_is_active_in.goterm.edges
  name: ProKN GO Not Active In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not located in GO term edges
  format: csv
  id: prokn.go.protein.not_located_in.goterm.edges
  name: ProKN GO Not Located In Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not part of GO term edges
  format: csv
  id: prokn.go.protein.not_part_of.goterm.edges
  name: ProKN GO Not Part Of Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_PART_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein part of GO term edges
  format: csv
  id: prokn.go.protein.part_of.goterm.edges
  name: ProKN GO Part Of Edges
  original_source:
  - go
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.PART_OF.GOTerm.edges.csv
- category: GraphProduct
  description: IMEx protein participates in complex edges
  format: csv
  id: prokn.imex.protein.participates_in.complex.edges
  name: ProKN IMEx Protein Participates In Complex Edges
  original_source:
  - imex
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/IMEx.Protein.PARTICIPATES_IN.Complex.edges.csv
- category: GraphProduct
  description: Reactome protein participates in pathway edges
  format: csv
  id: prokn.reactome.protein.participates_in.pathway.edges
  name: ProKN Reactome Protein Pathway Edges
  original_source:
  - reactome
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/Reactome.Protein.PARTICIPATES_IN.Pathway.edges.csv
- category: GraphProduct
  description: iPTMnet PTM targets protein edges
  format: csv
  id: prokn.iptmnet.ptm.targets.protein.edges
  name: ProKN iPTMnet PTM Targets Edges
  original_source:
  - iptmnet
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.PTM.TARGETS.Protein.edges.csv
- category: GraphProduct
  description: eMIND variant associated with disease edges
  format: csv
  id: prokn.emind.variant.associated_with.disease.edges
  name: ProKN eMIND Variant Disease Edges
  original_source:
  - emind
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.ASSOCIATED_WITH.Disease.edges.csv
- category: GraphProduct
  description: eMIND variant impact on disease edges
  format: csv
  id: prokn.emind.variant.impact.disease.edges
  name: ProKN eMIND Variant Impact Disease Edges
  original_source:
  - emind
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.IMPACT.Disease.edges.csv
- category: GraphProduct
  description: eMIND variant impact on protein edges
  format: csv
  id: prokn.emind.variant.impact.protein.edges
  name: ProKN eMIND Variant Impact Protein Edges
  original_source:
  - emind
  - prokn
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/eMIND.Variant.IMPACT.Protein.edges.csv
- category: GraphicalInterface
  description: Web explorer for the Protein Knowledge Network with interactive graph browsing
  format: http
  id: prokn.explorer
  name: Protein Knowledge Network Explorer
  original_source:
  - prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/explorer
- category: ProgrammingInterface
  description: REST API for the Protein Knowledge Network
  format: http
  id: prokn.api
  name: Protein Knowledge Network REST API
  original_source:
  - prokn
  product_url: https://research.bioinformatics.udel.edu/ProKN/restapi

---
Protein Knowledge Network

## Automated Evaluation

- View the automated evaluation: [prokn automated evaluation](prokn_eval_automated.html)
