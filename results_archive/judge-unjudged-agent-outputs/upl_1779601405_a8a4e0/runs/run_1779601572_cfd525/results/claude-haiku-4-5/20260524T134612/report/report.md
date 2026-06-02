# Analysis Report: Viral RNA Diversity in Mollusk Host Populations

## Data Summary

The dataset comprises a multi-faceted study of RNA viruses infecting mollusk species, with a focus on Pacific oyster (*Magallana gigas*). The uploaded supplementary materials include:

- **40168_2024_1967_MOESM1_ESM.xlsx**: Sample metadata documenting 16 oyster sampling batches (173 individuals total) collected across 4+ months (June–October 2016) from Luchao Port, Shanghai, and public transcriptomic datasets from 13 additional mollusk species and environments.
- **40168_2024_1967_MOESM2_ESM.xlsx**: Abundance quantification with transcripts per million (TPM), sequence coverage, and prevalence data for 157 unique viral contigs across 17 *Magallana hongkongensis* specimens and cross-host/cross-environment distribution patterns.
- **40168_2024_1967_MOESM3_ESM.xlsx**: 756 homology hits for RNA-dependent RNA polymerase (RdRp) sequences, bridging 146 unique query contigs to annotated viral proteins and enabling taxonomy assignment.
- **40168_2024_1967_MOESM4_ESM.fa**: 154 protein sequences representing translated viral open reading frames.
- **40168_2024_1967_MOESM5_ESM.zip**: Phylogenetic alignments across 9 viral taxa (Marnaviridae, Durnavirales, Picornavirales, Sobelivirales, Fiersviridae, Wolframvirales, Tolivirales, Hepelivirales, Nodaviridae).
- **40168_2024_1967_MOESM6_ESM.jpg**: Distribution of genome sequence coverage across three host categories.

## Analysis

### Derived Statistic 1: Viral Composition and Taxonomy Distribution
The 157 identified RNA viral contigs classify into 14 distinct taxa, with Marnaviridae (68 contigs, 43%), Picobirnaviruses (24 contigs, 15%), and Picornavirales (12 contigs, 8%) dominating. Forty contigs exhibit >90% genomic coverage (complete or near-complete genomes), indicating high-quality viral detection. This biased distribution toward positive-sense RNA viruses suggests either strong selective pressures favoring these groups in mollusk microbiota or biased detection in transcriptomic surveys.

### Derived Statistic 2: Temporal and Spatial Prevalence Heterogeneity
Analysis of 17 *M. hongkongensis* specimens across multiple timepoints and collection sites reveals striking variation in RdRp abundance (TPM ranges: 0 to 894,638 across samples). Individual contigs show prevalence patterns from single-sample detection to presence in 17/17 hosts, with median prevalence ~11 samples. In contrast, identical viral taxa appear in distinct mollusk species (oysters, gastropods, bivalves) and seawater, indicating cross-species transmission or environmental persistence at landscape scales.

### Derived Statistic 3: RdRp Homology Signature and Evolutionary Distance
The 756 BLAST/HMMER hits mapping 146 query contigs to reference RdRp sequences yield E-values ranging from e-160 to e-3 and identity scores from 46% to 98%. High-identity (>90%), full-length matches (>1500 bp) suggest recently acquired or co-evolving viral lineages (e.g., Beihai mollusks virus 2), while lower-identity, partial-length hits (300–600 bp) indicate divergent, recently-diversified viral strains (e.g., Picobirnavirus sp.). This heterogeneity in sequence divergence predicts structured host-adaptation within mollusk virome.

## Reasoning

The dataset combines temporal/spatial mollusk sampling, quantitative transcriptomics, and molecular phylogenetics to characterize a **previously unknown or poorly characterized viral landscape**. Three observations motivate a central scientific question:

1. **Ecological distribution**: Viruses are found across phylogenetically distant host species (oysters, gastropods, bivalves) and environmental reservoirs, yet individual contigs show strong prevalence heterogeneity—suggesting either recent, variable transmission events or niche-specific adaptation.

2. **Molecular diversity**: RdRp sequences exhibit both high-fidelity matches to named viral species and divergent, unnamed clades, indicating ongoing evolution and possible emergence of novel viral lineages within mollusk populations.

3. **High-prevalence dominance**: A small subset of viral contigs (40/157 = 25%) achieve near-complete genome coverage in *M. hongkongensis*, contrasting with many low-abundance variants, suggesting potential adaptive success or host-virus coevolution in this species.

## Top Scientific Question

**Do distinct RNA virus lineages (as defined by RdRp phylogeny and sequence identity) exhibit species-specific host tropism and prevalence patterns in sympatric mollusk populations, and do highly prevalent viruses in Pacific oyster (*Magallana* species) show evidence of recent horizontal transmission from environmental reservoirs?**

## Why This Question Is Testable on the Provided Dataset

1. **Host tropism analysis**: Cross-reference viral contigs in Sheet "Abundance_of_oyster_RNA_virus" (columns: In *C. hongkongensis?*, In other mollusks?, In Yangshan harbor seawater?) to define three tropism categories; test for non-random distribution across phylogenetic clusters in ZIP FASTA files.

2. **RdRp phylogeny**: Construct maximum-likelihood trees using ZIP files (e.g., Marnaviridae, Picornavirales) and classify query contigs into monophyletic groups; measure pairwise amino-acid identity using Sheet "oyster_hmm_palm_verified_rdrp_v" (columns: Identity, Evalue, Query_cover).

3. **Prevalence correlation**: Compute prevalence scores (Sheet "M.hongkongensis": count non-zero TPM across 17 samples) and cross-correlate with (i) coverage fraction, (ii) RdRp identity to reference, and (iii) host-range (presence in >3 species).

4. **Recent transmission signature**: Low-identity, high-coverage sequences suggest divergent recent acquisition; stratify by temporal batches (Sheet "This study": dates) to identify temporal emergence patterns in *M. gigas*.
