# BtCN-Virome Dataset — Technical Report

## 1. Data Summary

Five files constitute this dataset, totalling ~145 MB:

| File | Contents | Scale |
|---|---|---|
| `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` | Full-spectrum viral contigs assembled from Chinese bat metagenomes | 8,176 contigs, 405 sampling pools |
| `43059586_RdRp_motif_collection.xlsx` | Cross-order RdRp conserved-motif reference table (motifs A–F) | 22 rows × 13 columns covering 7 viral orders |
| `43059592_CytB-COI-ITS.tar.gz` | Barcode sequences for host (bats, arthropods, molluscs, plants) used as BLAST databases | 4 subdirectories: Bats/COI+CytB, Arthropoda, Mollusca, Streptophyta |
| `45561465_Meta_data_for_ecological_modeling.zip` | Pool-level viral-species richness + 12 climate/landscape predictors | 98 pools (total), 27 intestine-only, 25 lung-only records |
| `48306316_ML_Phylo.zip` | IQ-TREE maximum-likelihood phylogenetic data for 13 viral orders/families | 13 viral order tar-balls, each with aligned FAA, trimmed FAA, and 13 tree/log files |

The BtCN-Virome contigs span five bat families: Rhinolophidae (~1,845 contigs), Hipposideridae (~1,674), Scotophilidae (~893), Miniopteridae/Vespertilionidae, and Pteropodidae. Contig lengths range from 500 to 19,176 bp (mean 1,326 bp; 2,478 contigs ≥ 1 kb, 206 contigs ≥ 5 kb).

## 2. Analysis

**Viral species richness (tvs) distribution.** Across 98 pool samples the rarefied viral species richness ranges from 0.10 to 4.63 (mean 2.19 ± 0.96 SD). Rhinolophidae pools show the highest mean richness (2.54, n=22), while Hipposideridae show the lowest (1.61, n=7). Intestinal samples have markedly higher mean richness (2.66) than brain samples (1.36), with lung intermediate (2.03).

**Climate–virome correlations.** Pearson correlations between pool-level tvs and the 10-year climate variables are modest: host-species diversity H10 shows the strongest positive relationship (r = 0.23), while temperature (tas10, r = −0.16) and precipitation (pr10, r = −0.16) show weak negative associations. Species pool size (srs10) is negatively correlated (r = −0.13), suggesting that larger geographic ranges do not predict higher within-pool richness.

**Phylogenetic scope of BtCN-Virome.** The ML_Phylo dataset covers 13 viral orders/families (Bunyavirales, Coronaviridae, Durnavirales, Ghabrivirales, Hepelivirales, Jingchuvirales, Mononegavirales, Permutotetraviridae, Picornavirales [1,250 reference sequences], Reovirales, Sobelivirales, Stellavirales, Tolivirales). RdRp phylogenies were built against global references (EVRD, ZOVER) to place BtCN-Virome viruses within each order.

## 3. Reasoning

The richest predictive signal comes from the combination of (a) pool-level viral species richness data linked to bat family identity and climate/landscape predictors, (b) the host barcode databases enabling dietary/ectoparasite-linked transmission inference, and (c) the multi-order RdRp phylogenies that could reveal whether ecological context predicts clade membership. The observed positive correlation between local host-species diversity (H10) and viral richness, contrasted with weak climate effects, raises a specific ecological hypothesis about whether bat dietary diversity (inferable from COI/CytB prey barcoding) mediates viral community composition more strongly than abiotic climate variables.

## 4. Top Scientific Question

Does local host-species diversity (H10), mediated by bat dietary prey diversity inferred from COI/CytB barcodes, predict bat pool-level RNA viral species richness (tvs) more strongly than abiotic climate variables (tas10, pr10, vpd10) across five bat families sampled in the BtCN-Virome dataset?

## 5. Why This Question Is Testable on the Provided Dataset

The dataset directly contains all required inputs: (i) pool-level tvs values and H10 diversity indices from `45561465_Meta_data_for_ecological_modeling`, (ii) COI/CytB barcode references in `43059592_CytB-COI-ITS` for dietary reconstruction or host assignment, (iii) climate variables (tas10, pr10, vpd10, hurs10) in the same metadata file, and (iv) bat family labels enabling multi-level modelling. A regression or random-forest model with tvs as response and H10, dietary diversity proxy, and climate variables as predictors can be directly fitted to the 98-pool dataset.
