# Data Summary

The uploaded data consist of one Microsoft Word supplement, `data/43705_2022_180_MOESM1_ESM.docx`, with a 15-page document, one large accession table, and five embedded TIFF figures. Supplementary Table 1 is titled "Publicly available RNA-Sequencing datasets used in this study" and has columns for `Species`, `Scientific name`, `Animal type`, `SRA Accession`, `Country of origin`, `Tissue`, and `Sequencing platform`. The figure captions describe viral-contig discovery and phylogenetic analysis for novel reptile Bunyavirales, reptile lyssaviruses, amphibian and reptile Hepeviridae and Astroviridae, a newt influenza virus, and a newt calicivirus.

# Analysis

After excluding the footnote row, the table contains 235 accession-bearing RNA-seq entries, representing 234 unique accessions because `SRR4212883` appears twice. The accessions span 122 scientific host names and two host classes: 156 reptile entries (66.4%) and 79 amphibian entries (33.6%). Geographic metadata include 29 country or region values; the largest contributors are French Giana (40 entries), China (32), USA (28), Unknown (22), Australia (17), and Cuba (16). Tissue metadata are broad, with 26 tissue categories; liver is the dominant source (97 entries), followed by mixed viscera (38), kidney (20), nuptial pad (9), heart (8), and skin (8). Liver plus mixed viscera account for 135 of 235 entries (57.4%), indicating that many libraries sample internal organs where systemic viral RNA may be detectable. Sequencing technologies are mostly Illumina-based, with 15 platform labels; HiSeq 2000 variants, NextSeq 500, and HiSeq 2500 dominate, while 39 entries (16.6%) are starred as polyA-selected.

# Reasoning

The dataset is not just a host inventory: the captions show a complete viral discovery workflow. Viral contigs were identified by BLAST searches against NCBI viral protein databases, translated, aligned with MAFFT, and placed in RAxML phylogenies with 500 bootstrap replicates. The combination of broad amphibian/reptile host sampling, accession-level public transcriptomes, and figure evidence for multiple divergent RNA virus families points to a central scientific opportunity: using under-mined herptile transcriptomes to expand the known RNA virosphere and infer evolutionary relationships.

# Top Scientific Question

Can transcriptome mining of public amphibian and reptile RNA-seq datasets uncover novel RNA viruses in under-sampled herptile hosts and place them phylogenetically within Bunyavirales, lyssa-like rhabdoviruses, Hepeviridae, Astroviridae, influenza-like orthomyxoviruses, and Caliciviridae?

# Why This Question Is Testable On The Provided Dataset

Supplementary Table 1 provides the public accessions, host taxonomy, animal class, tissue, geography, and sequencing platform needed to retrieve and stratify transcriptome libraries. The figure captions specify the computational tests: BLAST-based viral contig detection, in silico translation, MAFFT alignment against reference viruses, and RAxML phylogenetic placement. The five figure topics also provide concrete positive targets across several RNA virus families, making the question directly answerable from the accession list and documented viral phylogenies.
