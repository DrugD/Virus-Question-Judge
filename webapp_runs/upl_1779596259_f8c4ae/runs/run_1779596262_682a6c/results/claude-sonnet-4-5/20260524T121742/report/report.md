# Technical Report: Novel Arthropod RNA Virus Dataset Analysis

## Data Summary

The dataset comprises two primary components:

1. **nuccore_reported_viral_sequences.fasta**: A multi-FASTA file containing 170 viral genome sequences (1.08 MB) from arthropod-associated RNA viruses, predominantly from China.

2. **elife-05378-supp-v1.zip**: Supplementary figures from Li et al. (2015) eLife publication on arthropod viral diversity, containing three phylogenetic tree figures showing relationships among novel and established RNA virus families.

The FASTA sequences represent 113 unique virus species/lineages collected from at least 10 arthropod host types: ticks (35 sequences, 23 unique virus types), mosquitoes (24 sequences, 17 types), flies (32 sequences, 25 types), spiders (12 sequences, 7 types), and various insects. Geographic sampling is heavily concentrated in Wuhan (59 sequences, 35%) with 12 distinct host types, followed by Shuangao (20 sequences, 5 host types) and other Chinese localities. Approximately 73.5% of sequences are novel viruses (numbered designations like "Virus 1", "Virus 2"), while 26.5% represent established reference strains.

## Analysis

**1. Sequence Completeness and Gene Distribution**: Of the 170 sequences, 138 contain complete coding sequences (CDS), 7 are complete genomes, 10 are complete segments (5.9% are from segmented viruses), and 16 are partial. Gene content analysis reveals 82 sequences encode polymerase genes, 49 encode glycoproteins, 28 encode PB1 (polymerase basic 1), and only 2 encode nucleoproteins. This distribution indicates the dataset is enriched for RNA-dependent RNA polymerase (RdRp) gene sequences, which are critical phylogenetic markers for RNA virus classification.

**2. Host-Specific Genomic Characteristics**: Mean sequence lengths vary substantially by host: tick-associated viruses average 7,471 bp, flies 7,496 bp, while mosquito (5,348 bp), insect (5,414 bp), and louse fly (5,560 bp) viruses are significantly shorter. Polymerase gene representation also differs by host: flies show 84.6% polymerase gene presence (11/13 sequences), mosquitoes 66.7% (16/24), while ticks show only 48.6% (17/35). These differences suggest either sampling biases toward particular viral families in certain hosts, or genuine biological variation in viral genome architecture across arthropod ecological niches.

**3. Geographic Host Diversity Patterns**: The Wuhan collection site exhibits exceptional host diversity (12 host types from 59 sequences), representing a geographic hotspot for arthropod-virus sampling. In contrast, specialized sites show host clustering: Wenzhou yielded only aquatic/semi-aquatic arthropods (crabs, shrimp, ticks near water), while Shuangao sampled primarily terrestrial insects (bedbugs, lacewings, flies). GC content analysis reveals substantial variation (24.65% to 59.98%, mean 41.38%), indicating diverse evolutionary histories and potential host adaptation signatures.

## Reasoning

The dataset presents a unique opportunity to investigate **cross-species viral transmission and host range determinants** in arthropod RNA viruses. Three key observations motivate this focus:

First, the geographic concentration in Wuhan (35% of sequences, 12 host types) provides spatial overlap necessary for detecting viral sharing or spillover between sympatric arthropod species. Second, the polymerase gene enrichment (82/170 sequences) offers phylogenetic resolution to distinguish true viral sharing from convergent evolution. Third, the substantial variation in sequence lengths and GC content across hosts suggests host-specific selection pressures that could illuminate barriers or enablers of cross-species transmission.

The eLife paper context indicates these viruses are ancestral to major vertebrate viral families (arenaviruses, filoviruses, paramyxoviruses), making host range evolution particularly significant for understanding emergence of human-pathogenic viruses. The dataset's combination of geographic co-occurrence, molecular phylogenetic markers, and ecological diversity creates an ideal testbed for quantifying host barriers in arthropod viral systems.

## Top Scientific Question

Do arthropod RNA viruses from the Wuhan collection site exhibit phylogenetic clustering by host taxonomic order (Diptera, Acari, Araneae) or by geographic microhabitat, and what does this pattern reveal about ecological versus phylogenetic barriers to cross-species viral transmission in arthropods?

## Why This Question is Testable

This question is directly testable using the provided dataset through the following analysis:

1. **Phylogenetic reconstruction**: Align the 82 polymerase gene sequences and construct maximum-likelihood phylogenetic trees to establish viral evolutionary relationships.

2. **Host metadata mapping**: Code each sequence by host taxonomic order (Diptera=flies/mosquitoes, Acari=ticks, Araneae=spiders) and collection microhabitat (terrestrial, aquatic, peridomestic).

3. **Phylogenetic clustering analysis**: Use Mantel tests or phylogenetic signal metrics (Blomberg's K, Pagel's λ) to quantify whether viral phylogeny correlates more strongly with host taxonomy or microhabitat.

4. **Wuhan-specific subset analysis**: Focus on the 59 Wuhan sequences with 12 host types to maximize statistical power in a spatially controlled sample, eliminating geographic distance as a confounding variable.

The expected result would distinguish between two models: (a) strong host-order clustering would indicate phylogenetic constraints (co-speciation, host-specific adaptation) limiting cross-order transmission, or (b) microhabitat clustering would suggest ecological opportunity drives viral sharing regardless of host evolutionary distance, with implications for predicting arthropod-to-vertebrate spillover risk.
