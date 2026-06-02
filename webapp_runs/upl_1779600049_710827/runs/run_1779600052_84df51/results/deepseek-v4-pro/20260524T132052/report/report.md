# Scientific Question Generation Report

## Data Summary

The uploaded workspace contains two files under `data/`:

1. **`5905698_all_virus_genomes.fasta`** (13.6 MB) — A multi-FASTA file containing complete RNA virus genome sequences. Each header follows the pattern `<SampleID>_<Group>_<VirusName>_len<Length>`. The viruses span at least four major taxonomic groupings: **Astro-Poty** (astro-like + poty-like), **Birna** (birna-like), **Bunya-Arena** (bunya-like + arena-like), and **Toti-Chryso** (toti-like + chryso-like). Host sources identifiable from headers include mosquitoes, insects, shrimp, hermit crabs, barnacles, sipunculid worms, and spiders. Geographic sampling spans multiple Chinese locations: Beihai, Hubei (including Wuhan), and Wenling.

2. **`5905695_alignments_and_phylogenies.zip`** (516 KB) — A compressed archive containing pre-computed sequence alignments and phylogenetic trees derived from the genome sequences above.

The dataset is consistent with large-scale meta-transcriptomic virus discovery efforts (e.g., Shi et al. 2016, *Nature*), which aimed to characterize the invertebrate RNA virosphere.

## Analysis

Several derived observations were made by inspecting the FASTA headers and sequence content:

1. **Taxonomic breadth**: At least four distinct virus family-level groups are represented (Astro-Poty, Birna, Bunya-Arena, Toti-Chryso). The hyphenated group names (e.g., "Astro-Poty") suggest these viruses exhibit phylogenetic affinities that bridge two previously distinct families — a hallmark of the dataset's significance in redefining viral taxonomy.

2. **Host diversity**: Headers reference arthropod hosts (mosquitoes, insects, spiders, shrimp, crabs, barnacles) and at least one non-arthropod invertebrate (sipunculid worms), indicating broad host sampling across invertebrate phyla.

3. **Genome size variation**: Genome lengths extracted from headers range from ~1,600 bp (nucleoprotein segments) to >11,700 bp (full-length RdRp-containing segments), reflecting both segmented and non-segmented genome architectures as well as partial versus complete coding sequences.

4. **Geographic signal**: Sampling localities (Beihai, Hubei, Wuhan, Wenling) are embedded in sample IDs, enabling phylogeographic analyses in conjunction with host information.

## Reasoning

The hyphenated group names (Astro-Poty, Bunya-Arena, Toti-Chryso) are not conventional ICTV taxa — they denote viruses discovered through this meta-transcriptomic survey that blur the boundaries between established families within the *Picornavirales* and *Bunyavirales*. The presence of both genome alignments and phylogenies in the zip archive provides the essential data infrastructure to test whether these groupings reflect genuine evolutionary intermediates or artifacts of incomplete lineage sorting. The diversity of hosts and locations further enables testing whether phylogenetic patterns are driven by host association or geography. The most compelling question targets the core evolutionary claim of the dataset: that invertebrate virome sampling reveals continuous phylogenetic space between previously discrete viral families.

## Top Scientific Question

Do the chimeric invertebrate RNA virus groups Astro-Poty, Bunya-Arena, and Toti-Chryso represent genuine phylogenetic intermediates blurring established family boundaries, as evidenced by the RdRp-based maximum-likelihood phylogenies and codon-aligned genome alignments provided?

## Why This Question Is Testable on the Provided Dataset

The question is directly answerable because: (i) the FASTA file provides full-length RdRp coding sequences for each virus, identifiable by the segment annotations in headers (e.g., "RdRp," "Glycoprotein," "Nucleoprotein"); (ii) the zip file contains pre-computed alignments and phylogenies that can be inspected for topological support of intermediate placements; (iii) the group labels in the headers allow viruses to be partitioned by their proposed chimeric affiliation; and (iv) phylogenetic incongruence tests (e.g., AU test, concatenation vs. single-gene tree comparison) can be applied using the alignment data to statistically evaluate whether these taxa genuinely occupy intermediate phylogenetic positions.
