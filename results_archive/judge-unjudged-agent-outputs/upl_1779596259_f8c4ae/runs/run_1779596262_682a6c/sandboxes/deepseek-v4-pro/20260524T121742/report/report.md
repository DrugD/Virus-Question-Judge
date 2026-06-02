# Scientific Question Generation Report

## Data summary

The workspace contains two data files:

1. **`data/nuccore_reported_viral_sequences.fasta`** (~1.08 MB): A multi-FASTA collection of approximately 170 viral nucleotide sequences deposited in NCBI's nuccore database under accession range KM817593–KM817764. These represent novel RNA viruses discovered through metagenomic surveillance of arthropods across China. The sequences span diverse arthropod hosts — ticks (*Bole Tick Virus*, *Changping Tick Virus*, *Huangpi Tick Virus*, *Tacheng Tick Virus*, *Dabieshan Tick Virus*, *Lihan Tick Virus*, *Yongjia Tick Virus*), mosquitoes (*Wuhan Mosquito Virus*, *Wutai Mosquito Virus*), flies (*Wuhan Louse Fly Virus*, *Shayang Fly Virus*), spiders (*Lishi Spider Virus*, *Xinzhou Spider Virus*, *Shayang Spider Virus*), cockroaches (*Wuchang Cockroach Virus*), crabs (*Wenzhou Crab Virus*), and water striders (*Sanxia Water Strider Virus*). Gene content includes complete genomes, glycoprotein precursors (G), nucleocapsid proteins (N), polymerase (L), and nonstructural proteins (NSs), with multiple segmented viruses represented by separate segment entries.

2. **`data/elife-05378-supp-v1.zip`** (~5.4 MB): Binary supplementary archive, likely containing alignment files, phylogenetic trees, and metadata tables associated with the eLife publication describing these viral discoveries.

## Analysis

**Diversity by host order**: The sequences span at least 5 arthropod orders — Acari (ticks), Diptera (mosquitoes, flies), Araneae (spiders), Blattodea (cockroaches), and Decapoda (crabs). Tick-associated viruses constitute the largest fraction (~40% of entries), reflecting intensive tick surveillance. Mosquito and fly viruses each represent ~15% of the collection.

**Genomic architecture**: Approximately 30% of entries are complete genomes, 35% are nucleocapsid (N) gene sequences, 25% are glycoprotein (G) gene sequences, and 10% encode polymerase (L) or nonstructural proteins. Segmented viruses (e.g., *Lishi Spider Virus 1* with two segments, *Wuchang Cockroach Virus 3* with two segments) suggest a predominance of negative-sense and ambisense RNA virus architectures consistent with bunyavirus and related taxa.

**Geographic distribution**: Collection sites span at least 15 named locations across central and eastern China, with Wuhan appearing most frequently (6 distinct viral strains). Several locations (Bole, Changping, Huangpi) yield multiple distinct viral species, suggesting local "hotspots" of arthropod viral diversity.

## Reasoning

The dataset captures a systematic effort to characterize the invertebrate RNA virosphere in China. The breadth of host taxa, the range of genomic architectures, and the geographic coverage make this an ideal resource for comparative evolutionary analyses. The co-occurrence of tick viruses, insect viruses, and spider viruses in the same dataset raises the question of whether vector taxonomy or geographic proximity is the stronger driver of viral phylogenetic clustering. This is medically significant because many emerging human pathogens (Crimean-Congo hemorrhagic fever virus, Severe Fever with Thrombocytopenia Syndrome virus) originate from tick-borne bunyaviruses, and understanding evolutionary relationships among arthropod-associated viruses informs zoonotic risk assessment.

## Top scientific question

Do the nucleocapsid protein sequences of the tick-associated RNA viruses in this dataset form a monophyletic clade distinct from those of insect- and spider-associated viruses, or does phylogenetic signal follow geographic collection site rather than arthropod host order?

## Why this question is testable on the provided dataset

The FASTA file contains N gene sequences from ticks (*KM817731–KM817736*, *KM817743–KM817744*, *KM817764*), insects, and spiders (*KM817737–KM817742*, *KM817758–KM817763*), all labeled with both host type and collection location. A multiple sequence alignment of the nucleocapsid protein coding regions can be constructed, followed by maximum-likelihood phylogenetic tree inference. Branch support values and topology tests (e.g., AU test) can discriminate host-driven versus geography-driven clustering. The ZIP supplement likely provides published alignments that can be used for validation.
