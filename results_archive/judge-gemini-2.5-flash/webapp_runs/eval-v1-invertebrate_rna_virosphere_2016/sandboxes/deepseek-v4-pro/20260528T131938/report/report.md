# Scientific Question Generation Report

## Data summary

The workspace contains two files under `data/`:

1. **`5905698_all_virus_genomes.fasta`** (13.6 MB) — A multi-FASTA file containing viral genome and gene-segment sequences. Sequence headers follow the pattern `<accession>_<family-group>_<virus_name>_len<length>`, encoding strain identifiers, family-level grouping, descriptive virus name, and nucleotide length. Four major family-groups are represented: **Astro-Poty** (astro-/potyvirus-like), **Bunya-Arena** (bunya-/arenavirus-like), **Birna** (birnavirus-like), and **Toti-Chryso** (totivirus-/chrysovirus-like). Some entries also encode specific gene products (RdRp, Glycoprotein, Nucleoprotein, Capsid, Protease). Host and geographic associations are embedded in virus names (e.g., Beihai, Wuhan, Hubei, Wenzhou, Wenling; mosquito, insect, shrimp, crab, barnacle, sipunculid worm, plant).

2. **`5905695_alignments_and_phylogenies.zip`** (516 KB) — A compressed archive containing pre-computed sequence alignments and phylogenetic trees derived from the FASTA data.

## Analysis

Three derived observations from the data:

1. **Taxonomic breadth and host diversity**: Across the sampled sequences, viral families span at least four distinct RNA virus lineages (Bunya-Arena, Astro-Poty, Toti-Chryso, Birna), associated with arthropod vectors (mosquitoes, insects, crabs, shrimp, barnacles), marine invertebrates (sipunculid worms, hermit crabs), and plants (zucchini, bean). This creates a multi-host, multi-family matrix suitable for cross-family host-association analysis.

2. **RdRp as a universal phylogenetic marker**: Multiple Bunya-Arena and Toti-Chryso entries explicitly encode the RNA-dependent RNA polymerase (RdRp). RdRp is the only universally conserved gene across RNA viruses and is routinely used for deep phylogenetics. Its presence across families makes the dataset amenable to superfamily-level evolutionary inference.

3. **Genome length variation across families**: Sequence lengths (from headers) range from ~1.4 kb (nucleoprotein segments) to ~11.7 kb (complete RdRp-containing genomes). Astro-Poty genomes range ~5.8–9.6 kb, Bunya-Arena ~1.4–11.7 kb (segmented), and Toti-Chryso ~2.6–8.7 kb. This size heterogeneity reflects differing genome architectures (segmented vs. monopartite) and gene content.

## Reasoning

The co-occurrence of multiple viral families sampled from overlapping geographic regions and host taxa provides a rare opportunity to disentangle co-evolutionary signals (virus-host codivergence) from ecological signals (host switching, vector sharing). Specifically, the presence of RdRp sequences across all families, combined with the alignments and phylogenies in the companion ZIP, enables formal phylogenetic testing of whether host range boundaries are conserved within viral clades or are routinely crossed over evolutionary time. The Bunya-Arena group, with its documented capacity to infect both arthropods and vertebrates, and the Astro-Poty group spanning plant and arthropod hosts, are ideal model systems for this question.

## Top scientific question

Does the RdRp phylogeny of the Astro-Poty and Bunya-Arena virus families in this dataset reveal statistically supported host-switching events between arthropod and plant (or vertebrate) hosts, consistent with vector-borne cross-kingdom transmission?

## Why this question is testable on the provided dataset

The FASTA file supplies nucleotide/amino-acid sequences for RdRp across multiple virus families and host-assigned isolates. The companion ZIP provides pre-built alignments and trees that can be directly interrogated for host-switching signatures. Ancestral-state reconstruction of host type on the RdRp tree, combined with bootstrap support for inter-host clade placements, can formally test whether cross-kingdom jumps are rare (strong host-phylogeny congruence) or recurrent (multiple independent jumps). The geographic metadata (Beihai, Wuhan, Hubei) further allows the question to be refined by testing whether host jumps correlate with sympatric sampling locations.
