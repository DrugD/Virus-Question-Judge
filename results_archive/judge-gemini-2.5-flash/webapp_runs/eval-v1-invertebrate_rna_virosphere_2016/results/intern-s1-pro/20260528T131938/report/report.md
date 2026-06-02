# Scientific Questions from Virus Genome Data

## Data Summary
The workspace contains two key datasets:
- `5905698_all_virus_genomes.fasta` (13.6 MB): A FASTA file with multiple virus genome sequences, primarily from the Astro-Poty group (Astrovirus and Potyvirus families). Headers indicate virus names, lengths (5,795–9,557 bp), and host associations.
- `5905695_alignments_and_phylogenies.zip` (516 KB): A compressed archive containing alignments and phylogenetic trees, presumably for the viruses in the FASTA file.

## Analysis
The FASTA file reveals 7+ complete virus genomes with diverse hosts (e.g., Beihai astro-like virus, Zucchini yellow mosaic virus, Hubei poty-like viruses). The .zip file's name suggests it contains multiple alignment files and phylogenetic trees, enabling comparative evolutionary analysis. The combination of raw sequences and pre-computed alignments/trees allows for both de novo and reference-based analyses of viral evolution, recombination, and functional conservation.

## Reasoning
The strongest scientific question (rank 1) focuses on phylogenetic relationships because the dataset explicitly includes phylogenies, making this directly testable. Questions 2–5 progressively explore sequence-level patterns, selection pressures, and functional implications that can be derived from alignments and trees. All questions are distinct and address different aspects of viral evolution and genomics.

## Top Scientific Question
**What is the phylogenetic relationship among the Astro-Poty virus genomes, and how does it correlate with host specificity?**

## Why Testable on This Dataset
The dataset provides both raw genome sequences (for de novo tree construction) and a dedicated phylogenies archive. Host information is embedded in sequence headers. By reconstructing or analyzing the provided phylogenies and mapping host data, we can directly test correlations between evolutionary relatedness and host range.