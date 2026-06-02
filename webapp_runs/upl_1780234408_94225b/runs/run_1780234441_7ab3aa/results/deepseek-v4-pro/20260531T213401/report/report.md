# Report — Scientific Question Generation

## Data summary

The workspace contains a single FASTA file (`data/nuccore_reported_viral_sequences.fasta`, ~320 KB, 26 sequences) comprising complete or near-complete viral genomes retrieved from NCBI NuCCore. All sequences carry accession numbers in the KR902709–KR902740 range, consistent with a 2015–2016 deposition window. Headers include accession, viral strain name, geographic sampling code (e.g., WHXS, WHZM, SKC, BHGZ), and gene/segment annotation.

The collection spans **13 distinct viral taxa** isolated from **11 arthropod host types** (cricket, flea, insect, aphid, barnacle, fly, mosquito, spider, tick, centipede, water strider) across at least **8 sampling locations** in China (Wuhan, Shuangao, Beihai, Shayang, Gamboa, Xinzhou, Bole, Sanxia). Five viruses are multi-segmented (four with 4 segments, one with 2 segments); the remaining eight are encoded on single segments as large polyproteins. All appear to be positive-sense RNA viruses, many annotated as encoding RNA-dependent RNA polymerase (RdRp) within polyprotein open reading frames.

## Analysis

**1. Genomic architecture diversity.** Of the 13 viral species, 5 (38%) possess segmented genomes. Segment counts range from 2 (Wuhan aphid virus 2) to 4 (cricket, flea, Shuangao insect, and Wuhan aphid virus 1). The eight non-segmented genomes are all annotated as "polyprotein gene, complete cds," indicating single ORF strategies. This split enables comparative analysis of genome organization strategies within a single ecological sampling framework.

**2. Host breadth and geographic spread.** The 11 host taxa span 6 arthropod classes/orders: Insecta (cricket, aphid, fly, mosquito, water strider), Arachnida (spider, tick), Crustacea (barnacle), Chilopoda (centipede), and Siphonaptera (flea). Sampling sites span central (Wuhan, Shayang), southern (Beihai), northwestern (Xinzhou, Bole), and southwestern (Sanxia, Shuangao) China. Two aphid viruses (WHYC-1 and WHYC-2) were collected from the same host population in Wuhan, providing a natural co-infection comparison.

**3. Sequence length and compositional variation.** Segment lengths vary from ~1.2 kb (aphid virus 2 segment 2) to >10 kb (largest polyprotein genes). GC content and codon usage can be extracted directly from the nucleotide sequences and compared across host taxa. The dataset's modest size (26 sequences) is sufficient for pairwise alignment and phylogenetic reconstruction but not for large-scale metagenomic statistics.

## Reasoning

The co-occurrence of multiple novel RNA viruses across diverse arthropod hosts sampled from different Chinese ecosystems makes this dataset ideal for host–virus co-evolution questions. The presence of segmented and non-segmented genomes within the same collection allows comparison of evolutionary constraints. Critically, codon usage bias is a well-established signature of host adaptation in RNA viruses. Because these sequences span at least six arthropod orders, one can test whether viral codon preferences cluster by host taxonomy (indicating host-driven convergent evolution) or by viral phylogeny (indicating vertical inheritance). This question is non-trivial, has clear surveillance and zoonotic-risk implications, and is directly testable with the nucleotide data in hand.

## Top scientific question

Do the codon usage patterns of these 13 novel invertebrate RNA viruses cluster by host taxonomy rather than by viral phylogeny, indicating host-driven convergent evolution?

## Why this question is testable on the provided dataset

All 26 sequences are complete or near-complete coding regions available as nucleotide FASTA. Codon usage bias (e.g., relative synonymous codon usage, effective number of codons) can be computed directly from the open reading frames. Host taxonomy is explicitly stated in each sequence header (e.g., "Wuhan cricket virus," "Bole tick virus"). A correspondence analysis of codon usage frequencies, followed by hierarchical clustering or principal component analysis, would reveal whether viruses from evolutionarily distant hosts (e.g., cricket vs. tick) nevertheless share codon preferences when infecting the same host order. Phylogenetic trees built from conserved RdRp domains would serve as the viral-phylogeny baseline. If codon clusters match host rather than viral phylogeny, this constitutes evidence for host-driven convergent evolution with implications for cross-species emergence potential.
