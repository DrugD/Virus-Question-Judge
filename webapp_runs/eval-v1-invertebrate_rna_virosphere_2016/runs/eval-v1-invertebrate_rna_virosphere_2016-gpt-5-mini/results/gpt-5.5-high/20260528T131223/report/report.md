# Scientific Question Report

## Data summary

The uploaded data contain two files. `data/5905698_all_virus_genomes.fasta` is a multi-FASTA of 2,339 viral genome or genome-segment records with headers encoding a sequence/sample identifier, a broad viral group label such as `Picorna-Calici`, `Bunya-Arena`, or `New-Qinvirus`, a virus name, occasional gene/segment labels, and a terminal length field. `data/5905695_alignments_and_phylogenies.zip` contains 60 files: 30 FASTA alignments and 30 matching Newick phylogenies. Most are RdRp alignments/trees for broad RNA virus groups, while `RdRp_versus_structural/` adds paired polymerase and structural-protein alignments/trees for selected groups.

## Analysis

The genome FASTA spans 13,453,538 nucleotide characters. Sequence lengths range from 799 to 30,353 nt, with a median of 4,470 nt and mean of 5,752 nt. I parsed 22 viral group labels; the largest were `Picorna-Calici` with 603 records, `Tombus-Noda` with 277, `Bunya-Arena` with 249, `Partiti-Picobirna` with 205, and `Luteo-Sobemo` with 174. The headers resolved to 1,782 unique group-plus-virus-name labels, indicating a broad and relatively sparse virus collection rather than repeated sampling of a few taxa.

The data also contain explicit gene or segment labels: 166 `RdRp`, 63 `Capsid`, 54 `Nucleoprotein`, 36 `Glycoprotein`, and 1 `NS` record, while most records are whole or unspecified genomes. Eighty-nine virus-name groups have at least two distinct gene labels and 14 have at least three, mainly in segmented negative-sense groups such as `Bunya-Arena`. The ZIP alignments contain 2,398 aligned sequences in total; the largest RdRp alignments are `Picorna-Calici_RdRp_trimmed_alignment.fas` with 533 sequences, `Tombus-Noda_RdRp_trimmed_alignment.fas` with 294, `Narna-Levi_RdRp_trimmed_alignment.fas` with 195, and `Partiti-Picobirna_RdRp_trimmed_alignment.fas` with 185. Alignment files include both dataset sequences and named reference viruses, such as `NC_` accessions and established plant, fungal, and invertebrate virus names.

## Reasoning

The strongest scientific opportunity is not simply cataloguing genomes, but using the already prepared RdRp alignments and phylogenies to place a large invertebrate-associated virus collection into the broader RNA virus tree. The scale across many groups, the presence of novel labels such as `New-Weivirus`, `New-Qinvirus`, `New-Yanvirus`, `New-Zhaovirus`, and `New-Yuevirus`, and the inclusion of reference taxa make this dataset suited to testing whether these genomes fill evolutionary gaps between established viral families or define deep new clades. The structural-protein comparison files add a secondary route to evaluate modular evolution, but the most general and well-powered signal is RdRp phylogenetic placement across the whole dataset.

## Top scientific question

How do the 2,339 uploaded RNA virus genome records reshape RdRp-based phylogenetic relationships among established and newly named viral groups, and do they reveal invertebrate-associated lineages that bridge or expand known RNA virus diversity?

## Why this question is testable on the provided dataset.

The question can be answered directly by combining `5905698_all_virus_genomes.fasta` group and genome metadata with the 30 RdRp alignment/tree pairs in `5905695_alignments_and_phylogenies.zip`. A test would quantify clade membership, sister relationships to reference viruses, branch lengths, monophyly of newly named groups, and the distribution of uploaded sequences across established and novel phylogenetic positions.
