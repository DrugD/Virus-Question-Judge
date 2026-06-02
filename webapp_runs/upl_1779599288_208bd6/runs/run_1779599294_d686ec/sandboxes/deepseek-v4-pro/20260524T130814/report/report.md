# Scientific Question Report

## Data Summary

The dataset is a multi-FASTA file (`nuccore_reported_viral_sequences.fasta`, ~320 KB) containing complete or near-complete coding sequences of novel RNA viruses deposited in NCBI's Nucleotide database. At least 13 distinct viral taxa are represented, spanning ~30 individual sequence records (segmented genomes contribute multiple entries per virus). The viruses were discovered via metagenomic sequencing from diverse arthropod hosts collected across multiple Chinese provinces. Host taxa include crickets, fleas, aphids, flies, mosquitoes, spiders, ticks, centipedes, barnacles, and water striders. Sampling locations include Wuhan, Shuangao, Beihai, Shayang, Gamboa, Xinzhou, Bole, and Sanxia. Two genome architectures are present: (a) segmented genomes with 4 (occasionally 2) segments, encoding putative RdRp, capsid, and structural proteins on separate molecules; (b) unsegmented genomes encoding a single large polyprotein. All sequences are annotated as "complete cds" or "complete sequence."

## Analysis

Three key observations emerged from inspecting sequence headers, genome organization, and host/locality metadata:

1. **Host breadth and phylogenetic span**: The 13 viral taxa infect arthropod hosts spanning at least six orders (Orthoptera, Siphonaptera, Hemiptera, Diptera, Araneae, Ixodida) plus a crustacean (barnacle). This broad host range, combined with the fact that many of these viruses belong to poorly characterized clades, makes the dataset ideal for examining host-virus co-divergence versus cross-order host switching.

2. **Co-occurrence of segmented and unsegmented genomes**: Several viruses (Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid viruses) possess 4-segmented genomes reminiscent of the order *Ghabrivirales* or related dsRNA viral groups, while others (Beihai barnacle virus 1, Shayang fly virus 4, Gamboa mosquito virus, Bole tick virus 4, etc.) encode a single large polyprotein typical of positive-sense ssRNA viruses such as flaviviruses, chuviruses, or picorna-like viruses. This dichotomy allows comparative analysis of genome architecture evolution.

3. **Geographic clustering with host diversity**: Several viruses were sampled from the same region (e.g., Wuhan yielded cricket, flea, aphid, and centipede viruses; Shayang yielded fly and spider viruses). This permits investigation of whether viral phylogenetic relatedness is better explained by host taxonomy or by geographic proximity (indicative of local cross-species transmission).

## Reasoning

The above observations converge on a central evolutionary question: are these novel arthropod RNA viruses primarily host-restricted (vertically co-evolving with their arthropod hosts) or do they frequently jump between distantly related hosts within shared ecosystems? The dataset's combination of diverse hosts, multiple geographic sites, and two distinct genome architectures provides a natural experiment: phylogenetic trees built from the RNA-dependent RNA polymerase (RdRp) domain — conserved across all these viruses — can be compared against host phylogeny and geographic origin to infer evolutionary processes. This question is non-trivial, has clear implications for understanding arbovirus emergence and zoonotic risk, and is directly testable with the sequence data provided.

## Top Scientific Question

Do the RNA-dependent RNA polymerase (RdRp) phylogenies of these novel arthropod viruses reveal host-order-level clustering consistent with long-term co-divergence, or do they show interleaving of viruses from different arthropod orders indicative of frequent cross-order host switching?

## Why This Question Is Testable on This Dataset

The dataset provides complete coding sequences for the RdRp gene (either as a dedicated segment or within the polyprotein) for each virus, alongside precise host taxonomic identification to the species or genus level. RdRp amino acid sequences can be extracted, aligned using established tools (MAFFT, MUSCLE), and subjected to maximum-likelihood phylogenetic reconstruction (IQ-TREE, RAxML). The resulting tree topology can be formally compared against host phylogeny using tests such as BaTS (Bayesian Tip-association Significance), ParaFit, or event-based cophylogenetic reconciliation (Jane, CoRe-PA). Geographic signal can be assessed by mapping collection location onto the viral phylogeny and testing for phylogeographic clustering. The combination of multi-segment and single-polyprotein genomes further allows the question to be stratified by genome architecture.
