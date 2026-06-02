# Scientific Report: RNA Virus RdRp Metagenomic Dataset Analysis

## Data Summary

The workspace contains **10 FASTA files** (~560 KB total) from an RNA virus metagenomic discovery project centered on the Hirai sample set. The files fall into three categories:

1. **Seven reference-guided multiple sequence alignments** (RdRp protein) spanning established RNA virus families: Chrysoviridae (27.6 KB), Narnaviridae (8.8 KB), Picornavirales (48.5 KB), Partitiviridae (53.4 KB), Pocobirnaviridae (20.5 KB), Reoviridae (23.4 KB), and Totiviridae (15.8 KB). Each alignment includes both known NCBI reference sequences and newly assembled Hirai metagenomic contigs, enabling direct comparison.

2. **Hirai Contigs RdRp file** (`16945969_31356130_Hirai_Contigs_RdRp.fas`, 250 KB) — the largest file, containing ~30+ contigs annotated by viral family: Chu-like, Narna-like, Picorna-like, Virga-like, Solemo-like, Tombus-like, Endorna-like, Chryso-like, plus three "Unclassified_ssRNA_virus_partial" sequences. Some contigs are "complete" (e.g., contig_2_LC651642_Picorna-like_complete, contig_31_LC651635_Chryso-like_complete).

3. **Possible virus contigs** (`16958869_31373884_Possible_virus_contigs.fas`, 63 KB) — contains **17 "Hirai_nohit" contigs** that failed BLAST classification, representing candidate novel viruses.

4. **nuccore_reported_viral_sequences.fasta** (59 KB) — NCBI-deposited complete viral genomes (LC651635–LC651638) encoding RdRp, capsid, and hypothetical proteins from the same study.

## Analysis

**Taxonomic breadth:** The Hirai assembly spans at least 10 distinct RNA virus lineages across the seven reference families plus unclassified groups, indicating a diverse virome. The Partitiviridae and Picornavirales alignments are the largest (53 KB and 49 KB respectively), suggesting these families dominate the sampled community.

**Classification gap:** Of all Hirai contigs discovered, 17 (nohit1–nohit17) could not be classified into any known family. These range from ~300 bp to >3,000 bp in length and are deposited in the dedicated `Possible_virus_contigs.fas` file. This unclassified fraction represents a significant proportion of the total contig diversity.

**Complete genomes:** At least two Hirai contigs (contig_2 and contig_31) correspond to complete or near-complete genomes deposited in nuccore with protein-level annotation (RdRp + capsid + hypothetical proteins). The nuccore file provides gene-level context absent from the alignment-only files.

**Conserved motifs:** The sequences contain canonical RdRp catalytic motifs (e.g., GDD polymerase domain, SGxxxT, various Walker A/B motifs), confirming their identity as RNA-dependent RNA polymerases.

## Reasoning

The most compelling scientific opportunity lies in the 17 Hirai_nohit contigs. These sequences passed quality filters and were retained as "possible viruses" yet resisted classification into any known RNA virus family by BLAST-based methods. This pattern — classified contigs spanning 8+ families alongside a substantial pool of unclassifiable sequences — is the hallmark of novel viral diversity awaiting characterization. The availability of seven curated reference alignments makes phylogenetic placement and divergence estimation directly tractable. Furthermore, the presence of both complete (nuccore) and partial (contig) sequences from the same study enables cross-validation: a novel lineage identified among nohit contigs could potentially be corroborated by unusual genome architectures in the nuccore records.

## Top Scientific Question

Do the 17 Hirai_nohit contigs in `Possible_virus_contigs.fas` represent one or more novel RNA virus families that are phylogenetically distinct from the seven established families in the reference alignments, and can conserved RdRp domain architecture place them relative to known orders such as Picornavirales, Reoviridae, and Narnaviridae?

## Why This Question Is Testable on This Dataset

The dataset provides all necessary components: (a) 17 unclassified contigs as query sequences, (b) seven curated RdRp alignments spanning the major RNA virus families as reference databases, (c) diverse Hirai contigs already classified into those families that can serve as positive controls for phylogenetic signal, and (d) complete nuccore genomes that can provide gene-context support. The test involves: extracting conserved RdRp blocks from the alignments, aligning the nohit contigs via profile-to-sequence or hmmsearch methods, constructing maximum-likelihood phylogenies, and evaluating whether nohit sequences form monophyletic clades outside known family boundaries with sufficient bootstrap support. Pairwise amino acid identity matrices against reference sequences can quantify divergence, and RdRp motif conservation (GDD, A–F motifs) can confirm polymerase identity even when overall homology is low.
