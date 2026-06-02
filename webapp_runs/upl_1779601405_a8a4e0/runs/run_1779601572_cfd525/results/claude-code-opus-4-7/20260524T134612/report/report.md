# RNA Virome of Cultivated Oysters — Data Report

## 1. Data summary

The `data/` directory contains six supplementary files associated with a Microbiome (2024) RNA-virus discovery study on bivalves (DOI prefix `40168_2024_1967`):

| File | Type | Content |
|---|---|---|
| `40168_2024_1967_MOESM1_ESM.xlsx` | Sample metadata | Sheet "This study": 16 longitudinal *Magallana gigas* (Pacific oyster) batches collected at Luchao Port, Shanghai (2016-06-22 → 2017-07-13, 7–15 individuals per batch). Sheet "Public data used": 32 public RNA-seq libraries from molluscs and Yangshan harbour seawater. |
| `40168_2024_1967_MOESM2_ESM.xlsx` | Abundance matrices | 156 putative RNA-virus contigs scored by TPM, log10TPM and covered fraction across (a) the oyster batches, (b) *Magallana hongkongensis* libraries (16 columns), (c) other Mollusca libraries (11 columns) and (d) Yangshan seawater. Includes columns "In *C. hongkongensis*?", "In other mollusks?", "In Yangshan harbor?" and a "*Dominant* (>90% coverage)" flag. |
| `40168_2024_1967_MOESM3_ESM.xlsx` | RdRp BLAST hits | 756 rows of `palmscan/HMM`-verified RdRp hits (Query_ID, Sbjct, bitscore, e-value, identity, alignment length, coordinates). |
| `40168_2024_1967_MOESM4_ESM.fa` | Protein FASTA | 154 oyster-derived RdRp ORFs labelled `>NNNNcontig\|\|k141_xxxxx_n`. |
| `40168_2024_1967_MOESM5_ESM.zip` | 9 family-level FASTAs | Phylogeny inputs for Marnaviridae (210), Durnavirales (115), Picornavirales (144), Sobelivirales (42), Fiersviridae (16), Wolframvirales (55), Tolivirales (112), Hepelivirales (12), Nodaviridae (89). Mix of `k141_*` oyster contigs and reference accessions (e.g. `YP_*`). |
| `40168_2024_1967_MOESM6_ESM.jpg` | Figure | A high-resolution figure (≈186 KB JPEG). |

## 2. Analysis

1. **Taxonomic composition of the oyster RdRp catalogue (MOESM2 sheet 1).** Of the 156 contigs, the dominant order/family groups are Marna (68), Picobirna (24), Picorna (12), Tombus (10), Noda (9), Narna (8), Wei (8), Solemo (6), Dicistro (3), Yan (2), with rarer Hepe, Fiers, Calici, Partiti (1 each). Marnaviridae alone account for ≈44 % of contigs.
2. **Cross-host / cross-environment sharing.** 75/156 contigs (48 %) are also detected in *Magallana hongkongensis*, 65/156 (42 %) in other mollusks, and 31/156 (20 %) in Yangshan harbour seawater. 40 contigs are flagged "Dominant" (>90 % covered fraction). The intersection of dominance and seawater-detection is the empirical basis for asking which viruses are persistently present versus diet/water-derived.
3. **Phylogenetic signal across nine RdRp orders.** The MOESM5 family-level FASTAs include both oyster-assembled `k141_*` ORFs and reference RdRps, so each set is laid out as a per-family alignment seed. Marnaviridae (210 seqs), Picornavirales (144) and Durnavirales (115) are the largest, indicating the primary axes along which the authors situated their novel oyster-RdRps phylogenetically.
4. **Longitudinal sampling design (MOESM1).** Sixteen batches over ~13 months at one site sample summer→winter→summer, with 7–15 individuals pooled per batch — a design that supports seasonal-prevalence analyses for the abundance matrix in MOESM2.

## 3. Reasoning

The dataset combines (i) a *time-resolved* single-site survey of one cultivated oyster species, (ii) abundance/prevalence projections of the same RdRp contigs into a second oyster species, eleven other mollusc taxa, and the surrounding seawater, and (iii) per-virus-order RdRp phylogeny inputs. The most distinctive scientific opportunity is therefore not "what viruses are present" (catalogue work, already done) but **whether specific RdRp lineages are bona fide oyster-resident infections versus environmentally/dietarily transient signal**. The covered-fraction + TPM + cross-matrix flags directly enable that test, and the per-family phylogenies allow lineage-level resolution.

## 4. Top scientific question

Which RdRp-defined RNA-virus lineages in the *Magallana gigas* virome are persistent, oyster-resident infections — distinguishable by simultaneously high covered-fraction and TPM across the 16 longitudinal Luchao batches and detection in *Magallana hongkongensis* — versus transient, environmentally acquired signals shared with Yangshan harbour seawater or with co-sampled non-oyster mollusks?

## 5. Why this question is testable on the provided dataset

Every variable needed for the test is in the supplementary files: the longitudinal batches and per-batch TPM/covered-fraction columns (MOESM2 sheets 1 + M.hongkongensis) operationalise persistence within and between oyster species; the Mollusca and Yangshan_harbor sheets supply the negative-control matrices for diet/water-borne signals; the "Dominant (>90 % coverage)" flag and pre-computed prevalence columns can be used as effect-size summaries; and MOESM5's nine per-family FASTAs allow each candidate lineage to be placed phylogenetically against known references, so the persistence/transience contrast can be reported lineage-by-lineage rather than only at the contig level. No wet-lab follow-up is required — the analysis is a direct mining of MOESM2 ± MOESM5.
