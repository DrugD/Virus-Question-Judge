# Scientific Report: Viral Metagenomic Sequences from Tick Isolates

## Data summary

The dataset consists of a single multi-FASTA file (`data/nuccore_reported_viral_sequences.fasta`, ~11.9 MB) containing metagenome-assembled genomes (MAGs) of viral sequences submitted to NCBI Nucleotide. Each sequence header follows the pattern `>Accession MAG: [Location] [Virus name] isolate TIGMIC_[n] [genomic sequence / complete genome]`. The isolates span numerous geographic locations across China, including Nanning, Tonghua, Zhangzhou, Maanshan, Lianyungang, Luoyang, Hulunbuir, Tianjin, Suizhou, Huanggang, Linzhi, Lhasa, and Chuzhou. Viral taxa represented include multiple Botou tick virus variants (numbered 1–8), Dabieshan Tick Virus, Phenuiviridae sp., Hulunbuir tick virus, Chuzhou tick virus, and Iflav tick viruses — all derived from ticks. Sequence lengths vary from a few hundred bases to complete genomes exceeding 10,000 bp, consistent with diverse RNA and DNA viral genome architectures. All entries are marked as MAGs, indicating computational assembly from metagenomic sequencing rather than isolate culture.

## Analysis

1. **Taxonomic breadth**: At least 8 distinct Botou tick virus types (1–8), plus Dabieshan Tick Virus, Phenuiviridae sp., and multiple Iflav tick viruses were identified from header parsing, indicating a multi-family survey of the tick virome.

2. **Geographic coverage**: Sequences originate from at least 13 distinct Chinese cities spanning from the northeast (Hulunbuir, Tonghua) to the south (Nanning, Zhangzhou) and the Tibetan plateau (Linzhi, Lhasa), covering substantial climatic and ecological gradients.

3. **Genome completeness variation**: Headers labelled "complete genome" versus "genomic sequence" suggest varying assembly quality, with some MAGs representing full viral genomes and others partial contigs, enabling assessment of genome recovery efficiency across different viral taxa and sampling sites.

4. **Sequence composition**: Observed nucleotide composition and repeat structures (e.g., homopolymer runs of A/T in Iflav sequences) differ markedly across viral families, suggesting family-specific genomic signatures amenable to comparative analysis.

## Reasoning

The co-occurrence of multiple viral species from the same tick metagenomes (same TIGMIC isolate numbering scheme), combined with broad geographic sampling, creates a unique opportunity to investigate whether viral co-infection patterns in ticks are structured by geography, tick species, or viral phylogeny. The presence of both segmented (Phenuiviridae) and non-segmented viruses across the same isolates makes this dataset especially powerful for addressing questions about viral community assembly in arthropod vectors.

## Top scientific question

Do tick-associated viral communities assembled from metagenomes across different Chinese geographic regions exhibit phylogenetically clustered co-occurrence patterns that correlate with the geographic distance between sampling locations?

## Why this question is testable on the provided dataset

The dataset provides (a) precise geographic labels in every sequence header, (b) multiple viral taxa co-occurring under shared TIGMIC isolate identifiers, (c) full or near-full genome sequences suitable for phylogenetic reconstruction, and (d) sufficient sample breadth (13+ cities across China's latitudinal and altitudinal gradients) to compute geographic distance matrices. One can extract co-occurrence networks by pooling sequences sharing isolate prefixes, reconstruct phylogenies for each viral family, and test for phylogenetic signal in co-infection patterns against geographic and climatic distance using Mantel tests or joint species distribution modelling — all without any wet-lab follow-up.
