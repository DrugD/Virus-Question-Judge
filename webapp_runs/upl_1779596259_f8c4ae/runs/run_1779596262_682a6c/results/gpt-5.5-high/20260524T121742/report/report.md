# Data summary

The visible dataset contains two uploaded files under `data/`: `nuccore_reported_viral_sequences.fasta` and `elife-05378-supp-v1.zip`. The FASTA has 170 nucleotide records, spanning accessions KM817593.1 through KM817764.1, with headers that name virus, strain, gene or segment, and completeness. The archive contains three EPS figure supplements: `elife_poa_e05378_Figure_3_Figure_Supplement_1.eps`, `..._Supplement_2.eps`, and `..._Supplement_3.eps`. Text extracted from the EPS files shows phylogenetic trees containing the uploaded invertebrate-associated viruses alongside reference groups including Quaranjavirus/Influenza virus, Phlebovirus, Arenavirus, Nairovirus, Phasmavirus, Hantavirus, Tospovirus, Orthobunyavirus, Rhabdovirus, Bornavirus, Nyamivirus, and Chuvirus.

# Analysis

The FASTA records total 1,048,737 nucleotides. Sequence lengths range from 898 to 15,462 nt, with a median length of 6,275.5 nt and mean length of 6,169.0 nt; the overall GC content is 41.21%. Header-derived annotation counts show 82 polymerase-related records, including RNA-dependent RNA polymerase, L polymerase, and PB1 labels; 49 glycoprotein records; and 48 nucleocapsid records. Completeness labels are dominated by 138 complete CDS entries, with 16 partial CDS entries, 7 complete genomes, and 10 segment-labeled records.

Parsing virus names gives 113 unique virus names. Host-associated cues are broad but uneven: record counts include 38 tick-associated, 25 mosquito-associated, 21 fly-associated plus 16 louse-fly-associated, 27 generic insect-associated, 12 spider-associated, 7 water-strider-associated, 5 shrimp-associated, 4 crab-associated, and smaller counts for bedbug, millipede, cockroach, lacewing, and ant names. Marker coverage is substantial enough for comparative work: 31 virus names have polymerase, glycoprotein, and nucleocapsid markers, and 60 have at least two of those major marker categories.

# Reasoning

The strongest scientific signal is not just that many viruses are present, but that many are annotated with conserved polymerase markers and are explicitly placed in phylogenetic context against known negative-sense RNA virus groups. The data span numerous invertebrate host cues and include both single-gene and multi-marker viral records, making it possible to ask whether these invertebrate sequences form novel host-associated clades or occupy positions that expand recognized viral families. Because RNA-dependent RNA polymerase is the principal deep phylogenetic marker for these viruses, it is the most defensible anchor for a high-impact evolutionary question.

# Top scientific question

Do the reported invertebrate viral RNA-dependent RNA polymerase sequences reveal host-associated lineages that bridge or expand established negative-sense RNA virus families?

# Why this question is testable on the provided dataset

The FASTA supplies the viral nucleotide sequences and header annotations needed to identify RdRp/L/PB1 records, host-associated virus names, and marker completeness. The EPS supplements supply the reference phylogenetic framing and named viral groups against which these records were interpreted. A direct test would extract polymerase sequences, align them with the reference taxa named in the figures, infer phylogenies, and evaluate whether the invertebrate viruses form distinct host-associated clades or branch near the boundaries of established negative-sense RNA virus families.
