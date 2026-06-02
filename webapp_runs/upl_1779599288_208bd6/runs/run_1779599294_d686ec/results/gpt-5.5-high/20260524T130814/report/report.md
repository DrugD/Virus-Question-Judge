# Scientific Question Report

## Data summary

The uploaded data consist of one FASTA file, `data/nuccore_reported_viral_sequences.fasta`, with 33 NCBI-style nucleotide records totaling 313,499 bases. Each header contains an accession, virus name, strain label, and either a segment annotation or a polyprotein CDS annotation. Twenty records are complete genomic segments from five named four-segment viruses: Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid virus 1, and Wuhan aphid virus 2. The remaining 13 records are long `polyprotein gene, complete cds` entries from viruses named after diverse hosts such as shark, spider, barnacle, fly, mosquito, lacewing, tick, centipede, cricket, and water strider.

## Analysis

The dataset has a strongly bimodal length distribution. The 20 segmented records are short, with a mean length of 2,687 nt and range of 1,845-3,170 nt, whereas the 13 polyprotein CDS records have a mean length of 19,981.5 nt and range of 9,653-26,315 nt. The five segmented viruses all have exactly four records, and their total assembled segment lengths are similar: 10,406-10,992 nt. Segment-length profiles are also ordered similarly across viruses, with segment 1 near 3.0-3.2 kb, segment 2 near 1.8-2.2 kb, and segments 3 and 4 near 2.7-2.9 kb.

Base composition provides another comparison. Across all records, GC content ranges from 34.26% in Sanxia water strider virus 6 to 56.12% in Bole tick virus 4. Segmented records are narrower in GC content, spanning 38.43-47.15% with virus-level means of 40.29-45.89%, while polyprotein records span 34.26-56.12%. Sequence ambiguity is minimal: only 15 non-ACGT bases occur in the full FASTA, concentrated in Wuhan aphid virus 1 segment 2, Shuangao lacewing virus 2, and Tacheng tick virus 8.

## Reasoning

The most scientifically informative contrast is not simply that the dataset contains viral sequences, but that it juxtaposes complete multi-segment arthropod-virus genomes with much longer unsegmented polyprotein CDS records. The five four-segment viruses show a repeated genome architecture despite coming from different named hosts, while the polyprotein records show far broader genome length and GC variation. This suggests the dataset can be used to test whether conserved segmentation patterns distinguish one coherent viral genome strategy from the diverse long-polyprotein viruses.

## Top scientific question

Do the complete four-segment arthropod viral genomes in `nuccore_reported_viral_sequences.fasta` share a conserved segment-length and nucleotide-composition architecture that distinguishes them from the long polyprotein CDS viruses?

## Why this question is testable on the provided dataset

The FASTA headers directly label segment numbers and polyprotein CDS records, allowing records to be grouped without external metadata. The nucleotide sequences allow segment lengths, total genome sizes, GC content, ambiguous-base counts, and terminal sequence patterns to be computed for every record. These features are sufficient to compare within-virus segment architecture, between-virus conservation among the five segmented genomes, and the contrast between segmented complete sequences and long polyprotein CDS entries.
