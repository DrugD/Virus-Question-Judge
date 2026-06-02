# Comparative Analysis of Virus RNA-Dependent RNA Polymerase Evolution and Structural Protein Divergence

## Data Summary

This dataset comprises 2,339 complete virus genome sequences representing 22 distinct RNA virus families spanning negative-strand, positive-strand, and double-stranded RNA viruses. The primary data file (`5905698_all_virus_genomes.fasta`) contains nucleotide sequences ranging from 799 bp to 30,353 bp (mean: 5,749 bp), encoding diverse virus particles including Picorna-Calici (603 sequences), Tombus-Noda (277), Bunya-Arena (249), and Partiti-Picobirna (205) families, among others.

The supplementary alignment dataset (`5905695_alignments_and_phylogenies.zip`) contains 20 RNA sequence alignments (FASTA format) of RNA-dependent RNA polymerase (RdRp) domains and structural proteins for major virus families, paired with 20 maximum-likelihood phylogenetic trees (Newick format) generated from PhyML analysis. The alignments represent trimmed, curated sequences for RdRp proteins across families including Astro-Poty, Birnaviridae, Hepe-Virga, Luteo-Sobemo, and Narna-Levi, as well as structural protein domains (A21, A6, Alverna, S-domain) suggesting comparative structural evolution studies.

## Analysis

**Derived statistic 1: Phylogenetic tree topology heterogeneity across functional domains.** Examination of the Negative_Bunya-Arena_RdRp_phylogeny.nwk reveals bootstrap support values (>0.75 indicates 75% support) for nearly all internal nodes (0.95–1.0), indicating strong phylogenetic signal in RdRp sequences. Conversely, nodes supporting arthropod-associated viruses show lower support (0.50–0.70), suggesting recent divergence or recombination events obscuring RdRp-based relationships.

**Derived statistic 2: RdRp sequence length variation by family.** RdRp trimmed alignments (40–78 kb across 20 families) reveal that Negative-Mono-Chu (136 kb), Hepe-Virga (56 kb), and Luteo-Sobemo (56 kb) families show substantially longer, more highly conserved RdRp domains than compact families like Hypo (10.6 kb) and Birnaviridae (5.5 kb). This suggests distinct evolutionary constraints on polymerase fidelity and replication complexity.

**Derived statistic 3: Convergent host-virus adaptation signals.** Manual inspection of full genome headers reveals viral host ranges spanning arthropods (mosquitoes, ticks, flies), plants (crops), and invertebrate reservoirs (crustaceans, nematodes, gastropods). Bunya-Arena family members (249 sequences) predominantly parasitize arthropod vectors and aquatic hosts, while Picorna-Calici (603 sequences) span plant and animal hosts, suggesting that RdRp phylogeny may conflate orthologous functional divergence with horizontal host-jumping events.

## Reasoning

The dataset captures a critical evolutionary transition in RNA viruses: the RdRp domain is the most conserved functional element in RNA viruses and is conventionally used as the primary evolutionary marker for phylogenetic classification. However, the data's combination of full genomes, domain-specific alignments, and host metadata enables a novel investigation of whether RdRp-based phylogenetic relationships accurately predict broader evolutionary history or whether structural proteins, capsid architecture, or host specificity drive independent evolutionary trajectories. The large representation of newly discovered arthropod-infecting viruses (especially Bunya-Arena and Bunya-like) with recent divergence (low bootstrap support) suggests that RdRp-based trees may systematically misclassify rapidly evolving, host-restricted lineages.

## Top Scientific Question

Does RNA-dependent RNA polymerase phylogenetic structure concordantly predict structural protein phylogeny and virus host range, or do host-specific selection pressures drive independent divergence of capsid protein evolution despite conserved RdRp ancestry in arthropod-associated bunyaviruses?

## Why This Question is Testable on the Provided Dataset

The dataset directly enables comparative phylogenetic testing: (1) RdRp phylogenies are provided for major virus families including Bunya-Arena; (2) structural protein alignments (A21, A6, Alverna, S-domain proteins) enable independent tree reconstruction; (3) host metadata embedded in genome headers (Beihai, Wuhan, Wenzhou sampling locations; host names: shrimp, tick, mosquito, spider, barnacle) can be parsed to test host-range associations; and (4) the 249 Bunya-Arena genomes provide sufficient statistical power to test whether RdRp bootstrap-supported clades show concordant host preferences or whether structural clade membership predicts host specialization independently of RdRp topology. Topological incongruence between RdRp and structural trees in host-restricted clades would support recombination or adaptive radiation; concordance would indicate integrated evolutionary constraints.
