# Scientific Question Report

## Data summary

The `data/` directory contains ten FASTA files describing a Hirai viral metagenome and comparative viral alignments. Seven files are amino-acid multiple sequence alignments for viral RdRp or polymerase-like regions: Chrysoviridae, Narnaviridae, Picornavirales, Partitiviridae, Pocobirnaviridae, Reoviridae, and Totiviridae. These alignments mix Hirai contigs with reference viral sequences whose headers encode accession-like identifiers and virus names. `16945969_31356130_Hirai_Contigs_RdRp.fas` contains nucleotide sequences for 194 Hirai RdRp contigs with headers encoding contig ID, virus-like classification, and complete/partial status. `16958869_31373884_Possible_virus_contigs.fas` contains 37 additional Hirai no-hit possible viral contigs. `nuccore_reported_viral_sequences.fasta` contains 17 reported complete CDS records named LC651635.1-LC651651.1 with gene annotations such as RdRp, polyprotein, capsid, and hypothetical protein.

## Analysis

Across all FASTA files there are 486 records, of which 264 are Hirai-like records. The seven family-level alignments contain 238 total amino-acid records and 33 Hirai entries; the Partitiviridae alignment has the most Hirai representatives (11), followed by Totiviridae (10), Pocobirnaviridae (7), Narnaviridae (2), and one each in Chrysoviridae, Picornavirales, and Reoviridae. The 194 RdRp contigs are dominated by dsRNA-associated groups: 82 Partiti-like, 37 Toti-like, 23 Picobirna-like, 14 Reo-like, 10 Narna-like, 7 Endorna-like, and smaller counts of Hypo-like, Virga-like, unclassified ssRNA/dsRNA, Picorna-like, Megabirna-like, Chu-like, Solemo-like, Tombus-like, and Chryso-like labels. Only 12 of the 194 RdRp contigs are marked complete; 182 are partial. The 37 no-hit possible viral contigs range from 744 to 3440 nt, with a mean length of about 1690 nt. Nearest-reference amino-acid identity varies sharply by alignment: Hirai Picornavirales and Chrysoviridae representatives are close to known references (92.0% and 90.5%), while Reoviridae, Narnaviridae, Partitiviridae, and Totiviridae Hirai sequences include much more divergent placements, with nearest-reference identities around 22.2%, 40.7%, 46.6% mean, and 46.3% mean, respectively.

## Reasoning

The data are not just a list of assembled contigs; they already contain marker annotations, complete reported sequences, no-hit candidates, and comparative alignments spanning several RNA virus families. The strongest scientific opportunity is therefore to ask how broad and novel the Hirai RNA virome is, especially because the RdRp inventory is large, dominated by partiti-like/toti-like/picobirna-like/reo-like groups, and includes both close matches and highly divergent sequences. The alignments make this testable by comparing Hirai contigs to known viral references, while the contig inventory can quantify family composition and completeness.

## Top scientific question

What is the diversity, novelty, and phylogenetic placement of RdRp-bearing RNA viruses recovered from the Hirai viral metagenome across the partiti-like, toti-like, picobirna-like, reo-like, narna-like, picorna-like, and related viral groups?

## Why this question is testable on the provided dataset

The question can be answered directly from the provided FASTA files by parsing RdRp contig classifications, summarizing complete versus partial viral sequences, aligning Hirai entries against the supplied family-level reference alignments, estimating nearest-reference similarity, and reconstructing family-specific phylogenetic trees or distance matrices. The `nuccore_reported_viral_sequences.fasta` records provide complete CDS examples for validation, while the no-hit contigs can be screened as possible additional divergent viral sequences.
