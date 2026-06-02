# Scientific Question Generation — Report

## Data summary

The workspace contains 10 FASTA files spanning RNA virus sequence data, totalling ~540 KB across three categories:

1. **Seven reference-family multiple sequence alignments** (`.fas`, 9–53 KB each): Chrysoviridae, Narnaviridae, Picornavirales, Partitiviridae, Pocobirnaviridae, Reoviridae, and Totiviridae. Each file holds aligned amino-acid (and some nucleotide) sequences of the RNA-dependent RNA polymerase (RdRp) gene region, combining annotated reference accessions (e.g., NCBI GenBank entries) with novel *Hirai* metagenomic contigs (e.g., `Hirai_contig_48`, `Hirai_contig_644`).

2. **Hirai_Contigs_RdRp.fas** (250 KB): The largest file, containing ~100+ RdRp-bearing contigs from the Hirai et al. metagenomic assembly. Contig headers carry provisional family assignments: *Narna-like*, *Partiti-like*, *Toti-like*, *Chu-like*, and *Unclassified dsRNA virus*. Most are labelled `_partial`, indicating fragmented RdRp recovery.

3. **Possible_virus_contigs.fas** (63 KB) and **nuccore_reported_viral_sequences.fasta** (59 KB): The former holds ~35 *Hirai_nohit* contigs — sequences that failed to match any known viral family by similarity search. The latter contains complete or near-complete viral genomes from NCBI nuccore (metagenome accessions LC651635–LC651651) encoding RdRp, capsid, polyprotein, and hypothetical proteins.

## Analysis

**Scale and diversity.** The seven alignment files collectively span at least five distinct Baltimore-group RNA virus families (dsRNA: Chrysoviridae, Partitiviridae, Reoviridae, Totiviridae, Pocobirnaviridae; +ssRNA: Narnaviridae, Picornavirales). The Hirai contig RdRp file adds several hundred partial sequences, with *Partiti-like* and *Toti-like* being the most abundant provisional assignments.  

**Novel lineage signal.** The *Hirai_nohit* contigs (35 entries) represent sequences that could not be assigned to any existing family at detectable similarity thresholds. These contigs encode plausible RdRp motifs (identifiable GDD polymerase signatures, conserved palm-domain residues) suggesting they are genuine viral RdRps from deeply divergent or previously undescribed RNA virus lineages.

**Reference-to-novel bridging.** Each family alignment juxtaposes well-annotated reference sequences against Hirai contigs, enabling direct comparison of conserved catalytic motifs, insertion/deletion patterns, and pairwise distances. For instance, in the Totiviridae alignment, the Hirai contigs (e.g., `Hirai_contig_644`) share the canonical GDD motif with *Giardia lamblia virus* and *Leishmania RNA virus* references, while divergent nohit contigs display variant motifs.

**Sequence-length distribution.** The Hirai contigs are predominantly partial (100–500 amino acids), whereas nuccore references often span >1000 residues for polyproteins. This creates a scalable framework: well-resolved reference backbones can anchor phylogenetic placement of even short novel fragments.

## Reasoning

The dataset's architecture — curated alignments of known viral RdRp families, a large pool of classified and unclassified novel contigs, and full-length reference genomes — is purpose-built for RNA virus discovery through phylogenetic placement. The most compelling scientific opportunity is determining whether the nohit contigs constitute genuine novel RNA virus families. The data support this because: (a) the seven-family alignment set provides a robust reference phylogeny for the known RNA virome; (b) the nohit contigs encode detectable RdRp domains that can be aligned to references; and (c) phylogenetic methods can quantify the evolutionary distance between nohit sequences and established clades, distinguishing deep-branching novel lineages from artefactual or chimeric assemblies.

## Top scientific question

Do the Hirai "nohit" contigs that lack similarity to any known RNA virus family represent evolutionarily distinct, previously undescribed RNA virus lineages when placed in a phylogeny of the seven reference-family RdRp alignments?

## Why this question is testable on the provided dataset

The seven reference alignments provide the evolutionary framework (ingroup topology and branch-length calibration). The nohit contigs can be profile-aligned to each family's RdRp alignment or to a concatenated supermatrix, and phylogenetic placement algorithms (e.g., EPA, pplacer) can assign each nohit sequence to a branch, measuring its distance from known clades. Contigs falling outside all reference-family crown groups with strong support would constitute candidates for novel families. The nuccore metagenome sequences serve as additional positive controls for placement accuracy. This analysis requires only the sequence data in hand — no additional wet-lab experimentation is needed.