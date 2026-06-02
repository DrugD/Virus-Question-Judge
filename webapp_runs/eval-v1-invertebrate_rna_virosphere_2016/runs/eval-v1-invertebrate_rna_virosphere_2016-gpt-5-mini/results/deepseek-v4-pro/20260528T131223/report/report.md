# Scientific Report: Novel RNA Virus Discovery Metagenomics Dataset

## Data Summary

The dataset comprises two files under `data/`:

1. **`5905698_all_virus_genomes.fasta`** (13.6 MB) — A multi-FASTA file containing complete or near-complete virus genome sequences. Sequence headers follow the pattern `<accession>_<family-group>_<virus_name>_len<length>`, encoding a rich set of metadata: viral family/group assignment, descriptive virus name (often including host or location), and genome length.

2. **`5905695_alignments_and_phylogenies.zip`** (516 KB) — A compressed archive of pre-computed multiple sequence alignments and phylogenetic trees, presumably derived from the FASTA genomes.

From header analysis, five major virus groups are represented: **Astro-Poty** (astro-like and poty-like viruses), **Bunya-Arena** (bunya/arena-like, including segmented genomes with RdRp, Glycoprotein, and Nucleoprotein segments), **Birna** (birna-like viruses), **Picorna-Calici** (picorna-like and calici-like viruses), and **Toti-Chryso** (toti-like and chryso-like viruses). Host associations span arthropods (mosquitoes, insects, shrimp), plants (zucchini, bean), and annelids (leeches). Geographic origins cluster in China: Beihai, Hubei, Wuhan, and Changjiang.

## Analysis

**Genome architecture diversity**: The dataset includes both non-segmented (Astro-Poty, Picorna-Calici, Toti-Chryso) and segmented genomes (Bunya-Arena with 2–3 segments; Birna). For several Bunya-Arena viruses, separate segment sequences (RdRp, Glycoprotein, Nucleoprotein) are present, enabling reassortment analysis.

**Host range breadth**: Viruses span at least four host phyla: Arthropoda (mosquitoes, insects, shrimp), Plantae (zucchini, bean), Annelida (leeches), and Mollusca (potential shrimp-associated). The Astro-Poty group alone bridges plant-infecting (Zucchini yellow mosaic virus, Bean yellow mosaic virus) and arthropod-infecting (Beihai astro-like virus) members.

**Genome size distribution**: Genome lengths range from ~1,971 nt (Hubei toti-like virus 3) to ~10,960 nt (Beihai shrimp virus 3 RdRp), reflecting substantial variation in gene content and genome organization across groups.

**Geographic clustering**: All samples derive from four Chinese locations. Multiple virus groups are present at each site, with Hubei and Beihai showing the greatest diversity, suggesting these are biodiversity hotspots for RNA virus discovery.

**Phylogenetic resources**: The zip file provides ready-made alignments and trees, enabling immediate cross-validation of evolutionary hypotheses without recomputing alignments from scratch.

## Reasoning

The most compelling scientific question emerging from these observations concerns the evolutionary drivers of RNA virus diversification across host kingdoms. The co-occurrence of related viruses in arthropods, plants, and aquatic animals — particularly within the Astro-Poty group, where plant and arthropod viruses cluster together — raises the hypothesis that host-switching, rather than strict co-divergence, has shaped the evolution of these viral lineages. This dataset is uniquely suited to test this because it contains (a) genome sequences from multiple viral families, (b) host metadata embedded in virus names, (c) pre-computed alignments and phylogenies, and (d) both segmented and non-segmented genomes allowing comparison of evolutionary constraints.

## Top Scientific Question

Do the phylogenetic relationships among the novel Astro-Poty RNA virus genomes support host-switching between arthropod and plant hosts as the dominant mode of diversification, as opposed to vertical co-divergence with host lineages?

## Why This Question Is Testable on the Provided Dataset

The FASTA file provides full genome sequences for multiple Astro-Poty viruses from arthropod (e.g., Beihai astro-like virus, Hubei poty-like virus 1, Wuhan poty-like virus 1) and plant hosts (e.g., Zucchini yellow mosaic virus, Bean yellow mosaic virus). The companion zip file contains pre-computed alignments and phylogenetic trees that can be directly inspected for topology. By mapping host type onto the phylogenetic tree and comparing tree topology against known host phylogenies, one can statistically test for host-switching (incongruent topologies) versus co-divergence (congruent topologies). The presence of RdRp sequences — the conserved RNA-dependent RNA polymerase — across all genomes provides a universal phylogenetic marker for robust tree reconstruction and hypothesis testing.
