# Report — Herptile Virome Discovery from Public RNA-Seq

## 1. Data summary

The `data/` directory contains a single Microsoft Word file,
`43705_2022_180_MOESM1_ESM.docx` (~2.25 MB), which is the
Supplementary Material of a published herptile virome study.
After XML extraction it yields ~27 KB of structured text plus five TIFF
figures (`image1.tiff` … `image5.tiff`).

The principal payload is **Supplementary Table 1** — a manifest of
**235 publicly available RNA-Sequencing libraries** (SRA / ERA / DRA
accessions, e.g. `SRR5591415`, `ERR4074563`, `DRR047251`) that the
authors mined for novel viruses. Each row has: common name, scientific
binomial, animal class (Amphibian / Reptile), accession, country of
origin, tissue, and sequencing platform. The remainder of the file is
five figure legends (Supplementary Figures 1–5) describing
phylogenies of novel viruses recovered from these transcriptomes.

## 2. Analysis (statistics derived from the manifest)

Parsed counts:

| Dimension | Value |
|---|---|
| Total libraries | 235 |
| Reptile libraries | 156 (66 %) |
| Amphibian libraries | 79 (34 %) |
| Distinct host species (approx.) | ~80 |
| Top tissue: Liver | 97 (41 %) |
| Mixed viscera | 38 |
| Kidney | 20 |
| Other tissues (Heart, Lung, Skin, Blood, Foregut, Testis, Nuptial pad, …) | <10 each |
| Top country: French Guiana | 40 |
| China | 32 |
| USA | 28 |
| Australia | 17 |
| Cuba | 16 |
| Unknown origin | 22 |
| Dominant platform | Illumina HiSeq 2000/2500 / NextSeq 500 |

Five novel-virus families are reported in the figure legends:
**Bunyavirales** (reptile), **Lyssavirus / Rhabdoviridae** (alligator-
associated rabies, anole lyssa-like), **Hepeviridae** and
**Astroviridae** (recombinant amphibian / reptile),
**Orthomyxoviridae** (newt influenza, PB1 gene), and **Caliciviridae**
(newt calicivirus, 7 390 nt polyprotein). All trees were built in
RAxML with 500 bootstraps after MAFFT alignment of in-silico
translated contigs.

Three notable distributional features:

1. **Tissue is overwhelmingly liver** (~41 % of libraries) and
   liver+kidney+mixed-viscera together account for ~66 %. Other
   compartments (gut, blood, skin, gonads, brain) are sparsely
   sampled.
2. **Geographic skew**: French Guiana caecilians (~40), Chinese
   anurans/turtles (~32) and US squamates (~28) dominate; whole
   continents (most of Africa, the Middle East, South-east Asia
   excluding China) are underrepresented or absent.
3. **Host-class imbalance**: reptiles are sampled twice as often as
   amphibians, and within reptiles squamates and chelonians dominate
   while crocodilians appear only sporadically.

## 3. Reasoning

These statistics suggest that the dataset is essentially a **natural
experiment in metatranscriptomic viral discovery** with two strong
explanatory axes — host phylogeny (amphibian vs reptile, and
sub-clades within each) and tissue tropism (liver-biased sampling).
Because the authors themselves found at least five distinct novel
virus families across this matrix, the virus-detection signal is
well above noise, which means the dataset can be re-analysed to ask
quantitative questions about *which host or tissue properties predict
viral diversity*. The presence of recombination breakpoints in the
hepeviruses/astroviruses and the recovery of a mammalian-style
*lyssavirus* in alligators further hint at host-jump and
inter-class spillover signals that the same data can directly test.

## 4. Top scientific question

**Across the 235 publicly available reptile and amphibian RNA-seq
libraries catalogued in Supplementary Table 1, does host class
(Reptilia vs Amphibia), sampled tissue (liver vs non-liver), and
geographic origin jointly predict the per-library diversity and
family-level composition of novel RNA viruses recovered by
translated-protein BLAST against herptile transcriptomes?**

## 5. Why this question is testable on the provided dataset

Every covariate the question requires is already present in
Supplementary Table 1: each row provides host class, scientific
binomial, tissue, country, and an SRA/ERA/DRA accession that points
to retrievable raw reads. The same de-novo assembly + protein-BLAST
+ MAFFT/RAxML pipeline that the authors used (and document in the
five figure legends) can be re-run on every accession to produce a
per-library count and family classification of novel viral contigs.
A regression / GLMM (Poisson or negative-binomial) of viral richness
on host class × tissue × country, with sequencing platform and read
depth as covariates, then directly answers the question, and a
PERMANOVA on a virus-family presence/absence matrix tests
compositional differences. No additional wet-lab work is required —
all data are public.
