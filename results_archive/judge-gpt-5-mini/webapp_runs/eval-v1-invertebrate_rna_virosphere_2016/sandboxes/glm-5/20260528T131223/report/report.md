# Data Summary

The dataset comprises virus genome sequences from a metagenomic survey, stored in `data/5905698_all_virus_genomes.fasta` (13.6 MB). The FASTA file contains 50+ complete or partial genome sequences spanning three major virus families: Astrovirus-Potyvirus-like (Astro-Poty), Birnavirus-like (Birna), and Bunyavirus-Arenavirus-like (Bunya-Arena). A supplementary archive `data/5905695_alignments_and_phylogenies.zip` (515 KB) contains pre-computed alignments and phylogenetic trees.

Sequence headers encode rich metadata including virus family, geographic origin (Hubei, Beihai, Wuhan, Changjiang, Zhee), host species (mosquitoes, shrimp, spiders, insects, barnacles, hermit crabs), and genome length. Genome sizes vary substantially: Astro-Poty sequences range 4,779–9,557 bp, Birna sequences 2,895–3,293 bp, and Bunya-Arena sequences 1,380–10,960 bp. Many Bunya-Arena entries represent segmented genomes with separate RdRp, glycoprotein, and nucleoprotein components.

# Analysis

Three key observations emerge from the data:

1. **Geographic clustering**: Viruses from the same family cluster by location. For example, multiple Astro-Poty variants (Hubei astro-like virus, Hubei poty-like virus) originate from Hubei province, while Beihai hosts diverse Bunya-Arena variants (Beihai shrimp virus 3, Beihai bunya-like virus 1–4, Beihai barnacle virus, Beihai hermit crab virus).

2. **Host diversity**: Bunya-Arena viruses infect diverse hosts including mosquitoes (Wuhan mosquito virus, Zhee mosquito virus), crustaceans (shrimp, barnacle, hermit crab), and insects. Astro-Poty viruses appear associated with plants (Zucchini yellow mosaic virus, Bean yellow mosaic virus) and invertebrates (leech virus).

3. **Genome architecture**: Bunya-Arena viruses exhibit tri-segmented genomes typical of bunyaviruses, with distinct RdRp (RNA-dependent RNA polymerase), glycoprotein, and nucleoprotein genes encoded separately. Astro-Poty viruses show monopartite genomes, while Birna viruses have bipartite genomes characteristic of birnaviruses.

# Reasoning

The co-occurrence of multiple virus families across shared geographic regions and hosts suggests potential ecological interactions and cross-species transmission dynamics. The presence of pre-computed alignments and phylogenies indicates prior phylogenetic analysis, making evolutionary relationship questions particularly tractable. The geographic and host metadata embedded in sequence headers enables systematic analysis of distribution patterns without requiring external databases.

# Top Scientific Question

What phylogenetic relationships exist among the Astro-Poty, Birna, and Bunya-Arena virus families across the Hubei, Beihai, Wuhan, and Changjiang geographic regions, and do geographic location or host species explain the observed clustering patterns?

# Why This Question Is Testable

This question is directly testable using the provided data. The FASTA file contains complete genome sequences with embedded geographic and host metadata in each header. The alignments_and_phylogenies.zip archive provides pre-computed alignments and phylogenetic trees that can be analyzed for clustering patterns. Phylogenetic analysis can reveal whether viruses cluster by family, geography, or host, and statistical tests (e.g., Mantel test, phylogenetic signal analysis) can quantify the explanatory power of geographic distance versus host similarity. The genome sequences themselves enable independent phylogenetic reconstruction if needed.