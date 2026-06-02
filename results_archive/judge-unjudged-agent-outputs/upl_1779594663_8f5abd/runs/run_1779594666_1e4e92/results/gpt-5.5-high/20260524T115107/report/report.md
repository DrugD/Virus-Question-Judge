# Scientific Question Generation Report

## Data summary

The upload contains one agent-visible data file, `data/43705_2022_180_MOESM1_ESM.docx`, plus the schema metadata in `info.json`. The DOCX is supplementary material for a viral-discovery study. Its main structured element is "Supplementary Table 1: Publicly available RNA-Sequencing datasets used in this study", with columns for `Species`, `Scientific name`, `Animal type`, `SRA Accession`, `Country of origin`, `Tissue`, and `Sequencing platform`. After excluding the footnote row, the table lists 235 accession rows from public RNA-seq datasets. The document also contains five supplementary figure captions describing BLAST-based viral contig discovery and MAFFT/RAxML phylogenetic analyses for novel reptile Bunyavirales, reptile lyssaviruses, amphibian/reptile Hepeviridae and Astroviridae, a novel newt influenza virus, and a novel newt calicivirus.

## Analysis

The 235 accession rows span 122 scientific names, with 156 reptile rows and 79 amphibian rows. Geographic coverage is broad but uneven: 29 country/origin categories are represented, led by French Giana (40 rows), China (32), USA (28), Unknown (22), Australia (17), Cuba (16), India (11), Denmark (11), and Madagascar (10). Tissue sampling is also skewed: liver is the most common tissue with 97 rows, followed by mixed viscera (38), kidney (20), nuptial pad (9), heart (8), and skin (8), across 26 tissue labels. Sequencing platforms normalize to ten platform categories; Illumina HiSeq 2000 dominates with 119 rows, followed by NextSeq 500 (40), HiSeq 2500 (33), HiSeq 4000 (20), and Genome Analyzer II (14). Thirty-nine rows are marked with an asterisk indicating PolyA selection. The captions consistently describe a workflow of searching herptile transcriptomes against viral protein databases, translating viral genes or polyproteins in silico, aligning with MAFFT, and building RAxML trees with 500 bootstrap replicates.

## Reasoning

The strongest opportunity is not merely to summarize host metadata, but to use a taxonomically and geographically broad set of amphibian and reptile transcriptomes as a discovery panel for RNA viruses. The table supplies host, tissue, country, platform, and accession-level structure, while the figure captions identify the viral families, genes, and phylogenetic methods already aligned with the dataset. Because the captions include both genome/contig alignment and phylogenetic placement, a scientific question about novel herptile RNA virus diversity and evolutionary placement is directly motivated by the available material.

## Top scientific question

What novel RNA viruses can be detected in publicly available amphibian and reptile RNA-seq datasets, and how do their phylogenetic placements within Bunyavirales, reptile lyssaviruses, Hepeviridae, Astroviridae, influenza viruses, and caliciviruses expand known herptile virus diversity?

## Why this question is testable on the provided dataset

The SRA accession table identifies the public RNA-seq datasets to mine, and the captions specify a reproducible computational strategy: BLAST searches against NCBI viral proteins, contig translation, MAFFT alignment, and RAxML phylogenetic reconstruction. The host metadata can link detected viruses to amphibian/reptile class, species, tissue, and geography, while the supplementary figure topics define the relevant viral groups and genes for testing evolutionary placement.
