# Report — Viral discovery from herptile RNA-Seq metadata

## 1. Data summary

The `data/` directory contains a single Microsoft Word file,
`43705_2022_180_MOESM1_ESM.docx` (~2.25 MB), authored by Emma Harding and last
modified 2022-06-17. It is the **supplementary material of a published
viral-discovery study on amphibians and reptiles ("herptiles")**. The document
contains:

* **Supplementary Table 1** — an inventory of the publicly available
  RNA-Sequencing datasets selected for viral mining. Columns are
  *common name, scientific name, animal type (Amphibian/Reptile),
  SRA/ERR/DRR accession, country of origin, tissue, sequencing platform*,
  with an asterisk flag for libraries prepared with poly(A) selection.
* **Supplementary Figures 1–5** (5 embedded TIFF images and figure legends)
  describing five novel virus discoveries: novel reptile *Bunyavirales*,
  reptile lyssaviruses (including alligator-associated rabies lyssavirus and
  anole lyssa-like virus), novel amphibian/reptile *Hepeviridae* and
  *Astroviridae* (with a recombination breakpoint highlighted), a novel newt
  influenza virus (PB1 phylogeny), and a novel newt calicivirus
  (7,390-nt polyprotein).

## 2. Analysis

I extracted the table text and computed several derived statistics:

* **Sample inventory.** 234 unique SRA/ERR/DRR accessions are tabulated.
  By animal type the split is **156 reptile** vs **79 amphibian** libraries
  (≈2:1). Forty entries (≈17 %) carry the poly(A) flag, meaning host-mRNA
  enrichment that strongly biases against detecting most non-poly-adenylated
  RNA viruses (e.g. *Bunyavirales*, *Rhabdoviridae*).
* **Tissue and platform composition.** Liver dominates (97 libraries),
  followed by *Mixed viscera* (38), Kidney (20), Nuptial pad (9), Heart (8),
  Skin (8), Blood (6), Small intestine (6), Lung (5), Mixed tadpole viscera
  (5), and a long tail of glandular tissues (mental, femoral, pectoral,
  axillary). Sequencing was performed on at least 11 distinct Illumina/454
  platforms (HiSeq 2000 dominant, plus NextSeq 500, HiSeq 2500/4000, GAIIx,
  HiSeq X Ten, 454 GS FLX/Junior), introducing systematic differences in read
  length and depth.
* **Geography.** Samples span ≥27 countries / regions, with the largest
  contributions from French Guiana (40 — almost all caecilian tissues),
  China (32), USA (28), Australia (17), Cuba (16), Madagascar (11),
  India (11) and Denmark (11). Five new viruses are reported as supplementary
  figures, all with phylogenetic placement among existing families.

## 3. Reasoning

Three observations drive the scientific question I propose. First, the
metadata is unusually rich along three orthogonal axes — host clade
(amphibian vs reptile, plus species), tissue, and library chemistry
(poly(A) vs total-RNA). Second, the supplementary figures show that several
novel viruses (e.g. lyssaviruses, *Bunyavirales*) are being recovered from
libraries that include poly(A)-selected datasets, which should in principle
deplete negative-sense RNA virus genomes. Third, liver and "mixed viscera"
overwhelmingly dominate the sampled tissues, so any tissue-level inferences
about virome composition are highly confounded with host clade and origin.
Together these structural features make the dataset particularly well suited
to a question about **how the technical and biological design of public
RNA-Seq libraries determines which viruses are discoverable in herptile
hosts**, with direct relevance for zoonotic-spillover surveillance of
reptile rabies-like lyssaviruses and amphibian orthomyxoviruses.

## 4. Top scientific question

> Across the 234 publicly archived herptile RNA-Seq libraries catalogued in
> Supplementary Table 1, do library chemistry (poly(A) vs total-RNA),
> tissue type, and host clade (Amphibia vs Reptilia) jointly bias the
> recoverable viral family spectrum — particularly the detection of
> negative-sense RNA viruses such as *Bunyavirales* and *Rhabdoviridae*
> (e.g. the alligator-associated rabies lyssavirus shown in
> Supplementary Figure 2)?

## 5. Why this question is testable on the provided dataset

Supplementary Table 1 already provides the exact covariates needed:
animal type, tissue, sequencing platform, country, and a poly(A) flag.
Supplementary Figures 1–5 enumerate the viral families recovered. A
straightforward re-analysis pulls each accession from SRA, runs a uniform
viral-contig assembly + BLASTx pipeline (as the original study did against
NCBI protein references), and treats each library as an observation with
covariates (chemistry, tissue, host class). Logistic / multinomial models
of "virus family detected ~ chemistry + tissue + host" then directly
quantify whether the bias toward poly(A) liver libraries causes specific
viral families — most importantly the negative-sense RNA viruses with
zoonotic relevance — to be systematically under-recovered.
