# Scientific Question Report — Arthropod RNA Virosphere Dataset

## 1. Data summary

The `data/` directory contains two artifacts:

- `nuccore_reported_viral_sequences.fasta` — 170 nucleotide sequences (NCBI nuccore accessions `KM817593`–`KM817764`, all with the `KM` prefix), totalling ~1.05 Mb of nucleotide data. Sequence lengths range from 898 bp to 15,462 bp (median 6,275 bp; mean 6,169 bp). FASTA defline annotations name each isolate, its strain code, and the gene/segment encoded.
- `elife-05378-supp-v1.zip` — supplementary material from the eLife paper `e05378` (Li et al.), specifically three EPS figure-supplements for that paper's Figure 3. The zip therefore links the FASTA dump to the published study reporting these viruses.

Decoding the deflines: 27 distinct geographic prefixes (Wuhan, Shuangao, Tacheng, Wenzhou, Sanxia, Bole, Changping, Huangpi, Lishi, Yongjia, etc.) and ~113 distinct virus names. Arthropod / invertebrate hosts are explicitly stated in the names: ticks (38), flies (33), generic "insect" (27), mosquitoes (25), louse flies (16), spiders (12), water striders (7), cockroaches (6), horseflies (4), crabs (4), millipedes (3), bedbugs (3), and singletons for moth, lacewing, ant, lacewing, shrimp, crayfish, etc. Annotated coding regions are dominated by markers of negative-sense RNA viruses: 82 polymerase (L) genes, 48 nucleocapsid (N), 49 glycoprotein (G), 14 PB1 (orthomyxo-like), 13 matrix (M), 11 phosphoprotein (P), 10 segment-1 / 20 segment-2 / 9 segment-3 references, and 5 NSs.

## 2. Analysis

Three derived observations:

1. **Bimodal length distribution consistent with segmented vs. non-segmented genomes.** Bucketing the 170 lengths gives 2 (<1 kb), 55 (1–3 kb), 23 (3–6 kb), 47 (6–9 kb), 21 (9–12 kb), 22 (>12 kb). The 1–3 kb mass corresponds to N or G genes on small bunya-/phenui-like segments, while the 6–15 kb tail is dominated by L-segment / mononega-like full polymerase ORFs and complete genomes (7 sequences explicitly labelled "complete genome").
2. **Marker-gene composition implies at least three negative-sense RNA virus lineages.** N+L+G+NSs+M annotations co-occur in 108/170 entries (bunya-/phenui-/phlebo-like architecture). PB1 alone tags 14 sequences (orthomyxo-like). Phosphoprotein co-annotation in 11 sequences (with N, M, G, L) is the canonical mononegavirales gene order. Multi-segment isolates (e.g. `KM817604/KM817605` Wuchang Cockroach Virus 3 segments 1+2; `KM817740/KM817741` Shuangao Insect Virus 2 S1+S2) confirm segmented genome architecture is widespread.
3. **Host/geography crosstab is uneven and non-random.** "Wuhan" prefixes 59 isolates and "Shuangao" 20, while many provinces contribute ≤4. Tick-derived viruses (38) span six geographies (Bole, Changping, Huangpi, Tacheng, Wenzhou, Yongjia, Lihan, Dabieshan), whereas spider-derived viruses (12) cluster in only three (Lishi, Shayang, Xinzhou). This sampling structure is a confound that any host-specificity claim must address.

## 3. Reasoning

The FASTA is the public-record export of the very large RNA-virus discovery effort underlying eLife e05378. The richness of L-gene sequences (82 polymerases) makes this an unusually well-powered substrate for **RdRp-anchored phylogenetics**: the L gene is the universal marker for negative-sense RNA viruses, and 82 homologues drawn from a structured set of arthropod hosts and Chinese sampling locales is exactly the design needed to ask whether viral phylogeny tracks host taxonomy or geography. The simultaneous presence of segmented (bunya-/orthomyxo-like) and unsegmented (mononega-like) genome plans across the same arthropod orders also lets us ask whether genome architecture transitions cluster within particular host clades — a question with biomedical relevance because many arboviruses of public-health concern (Phlebovirus, Thogotovirus, Rhabdovirus) sit inside exactly these clades.

## 4. Top scientific question

**Across the 170 KM817593–KM817764 arthropod-derived RNA virus sequences, does host arthropod order (e.g. Ixodida ticks vs. Diptera flies/mosquitoes vs. Araneae spiders) explain more of the variance in RdRp (L-gene) phylogenetic placement than does Chinese sampling locality, and where do the orthomyxo-like (PB1-bearing) and bunya-/phenui-like (N+G+L) lineages place relative to known vector-borne pathogens of vertebrates?**

## 5. Why this question is testable on the provided dataset

Every ingredient is in the FASTA. (i) Host arthropod order is explicitly named in each defline (tick, fly, mosquito, spider, …), giving a categorical predictor for 170/170 sequences. (ii) Sampling locality is encoded in the virus prefix (Wuhan, Shuangao, Tacheng, …) for all entries, giving a second predictor. (iii) The 82 L-gene / RdRp sequences and 14 PB1 sequences provide the universal phylogenetic marker required to build a tree; conserved RdRp motifs let us align them to public references (Bunyavirales, Mononegavirales, Articulavirales) without any wet-lab work. (iv) A standard analysis — translate L/PB1 ORFs, align with MAFFT, build a maximum-likelihood tree with IQ-TREE, then run a Mantel test or PERMANOVA of patristic distance against host-order vs. locality labels — answers the variance-partitioning part. (v) Placement of the orthomyxo-like and bunya-like clades next to reference Thogotovirus, Phlebovirus, and Phasmaviridae genomes (linked through the e05378 supplement) addresses the public-health-relevance part. No external data beyond GenBank reference RdRps is required.
