# Data summary

The upload contains five data objects. `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` holds one FASTA file, `BtCN-Virome_full_spectrum.fna`, with 8,176 virome contigs from 405 pool-name prefixes. `43059586_RdRp_motif_collection.xlsx` is a 21-row RdRp motif table covering conserved polymerase motifs across RNA virus groups, including Bunya, Mononega, Reo, Picorna-like, Permutotetra, Orthomyxo, and Durna/Reovirales categories. `43059592_CytB-COI-ITS.tar.gz` contains host and diet marker references: bat COI/CytB files, a dereplicated Chiroptera CytB/COI FASTA, and large arthropod, mollusk, and streptophyte marker databases. `45561465_Meta_data_for_ecological_modeling.zip` contains `intestine.txt`, `lung.txt`, and `total.txt`; the combined table has 98 pooled observations with `tvs`, `family`, organ code `st`, `sp`, and climate predictors. `48306316_ML_Phylo.zip` contains 13 RNA virus order/family phylogeny tarballs plus a README describing full-length RdRp alignment, trimming, manual checking, and IQ-TREE reconstruction.

# Analysis

The virome contig file totals 10,612,181 bp; contig length ranges from 500 to 19,176 bp, with median 797 bp and 2,974 contigs at least 1 kb. Parsed coverage values were available for 5,447 headers, with median coverage 6.192 and 465 contigs at coverage at least 100. The marker references are broad: 515,372 arthropod COI/CytB records, 106,078 streptophyte ITS records, 39,050 mollusk COI/CytB records, 20,505 bat COI records, 19,367 bat CytB records, and 3,830 dereplicated Chiroptera CytB/COI records. In `total.txt`, family counts are Ve 40, Rh 22, Pt 20, Eb 9, and Hs 7; organ-code counts are In 27, Lu 22, Ki 22, Li 17, and Br 10. Mean `tvs` differs by organ, with intestine highest at 2.664 and brain lowest at 1.356, and by family, with Rh highest at 2.543 and Hs lowest at 1.607. The largest marginal correlations with `tvs` in the combined table are `H10` (0.228), `tas10` (-0.164), and `pr10` (-0.163). The ML phylogeny tarballs contain 4,222 original RdRp sequences and 3,205 final-alignment sequences across the 13 groups, with Picorna largest.

# Reasoning

The most complete inferential table is the ecological metadata, and it already aligns a viral-diversity response with host taxonomy, organ compartment, sample-size information, and environmental gradients. The observed organ and family differences suggest biological structure, while the climate correlations suggest environmental modulation. The sequence and phylogeny files provide virological context, but the strongest directly testable cross-sample question is an ecological model of viral richness.

# Top scientific question

How do bat family, sampled organ, and environmental gradients jointly explain variation in transformed viral species richness (`tvs`) across BtCN pooled bat virome samples?

# Why this question is testable on the provided dataset

`total.txt` supplies one row per pool with the response `tvs`, predictors `family`, `st`, `sp`, and climate variables including `H10`, `pr10`, `tas10`, `hurs10`, `pet10`, `rsds10`, `sfcwind10`, and `vpd10`. The question can be tested by fitting multivariable ecological models, comparing host, organ, and environmental terms, and checking robustness against the intestine- and lung-specific tables.
