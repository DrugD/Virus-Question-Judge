# Technical Report: BtCN-Virome Bat Virome — Landscape Ecology Analysis

## 1. Data Summary

Five data files were examined:

| File | Description | Scale |
|---|---|---|
| `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` | Full-spectrum virome contigs (FASTA) from bat pools collected across China | 8,176 total FASTA headers; 6,640 contigs with embedded length data; mean contig length 1,326 bp, max 19,176 bp; 405 unique pool sample codes |
| `43059586_RdRp_motif_collection.xlsx` | Reference table of conserved RNA-dependent RNA polymerase (RdRp) motifs (G, F, A, B, C, D, E) for major RNA virus orders/families | 8 motif rows × 13 viral lineage columns (Permutotetraviridae, Orthomyxo, Mononega, Bunyavirales, Reovirales, +RNA, Durnavirales, etc.) |
| `43059592_CytB-COI-ITS.tar.gz` | Bat host barcode sequences: 20,505 COI sequences, 19,367 CytB sequences (from GenBank, chiroptera-only), plus combined `chiroptera_CytB_COI.fas` (3,830 sequences); arthropod COI, mollusca COI, and plant ITS references also included | Multi-kingdom reference |
| `45561465_Meta_data_for_ecological_modeling.zip` | Ecological metadata for 98 bat pool samples across 5 bat families: viral species richness (`tvs`), climate variables (temperature `tas10`, precipitation `pr10`, solar radiation `rsds10`, humidity `hurs10`, VPD `vpd10`), landscape variables (natural terrain coverage `nt`, slope `sl`, Shannon entropy `H10`), land-use pressures (cropland `gm`, built-up `bx`, shrubland `sy`, orchard `cy`, livestock density `ld`), bat species diversity index (`btsm`), and species richness (`sp`) | 98 records; tissue-specific subsets: 27 intestine, 25 lung |
| `48306316_ML_Phylo.zip` | Maximum-likelihood phylogenetic trees and aligned RdRp sequences for 13 RNA virus orders/families (Picornavirales, Reovirales, Bunyavirales, Coronaviridae, Durnavirales, etc.) reconstructed from BtCN-Virome + ZOVER-bat + EVRD-aa references | 13 viral orders/families |

Key columns in ecological metadata: `Pool_code` (bat pool ID), `tvs` (viral species richness), `family` (bat family: Hipposideridae=Hs, Rhinolophidae=Rh, Vespertilionidae=Ve, Pteropodidae=Pt, Emballonuridae=Eb), `st` (tissue: In=intestine, Lu=lung, Li=liver, Ki=kidney, Br=brain), `sp` (bat species count per pool), `sl` (terrain slope), `H10` (Shannon landscape entropy), `btsm` (co-occurring bat species diversity index).

## 2. Analysis

### Statistic 1: Viral Richness Distribution by Bat Family
Across 98 pooled samples (total.txt), mean viral species richness (`tvs`) ranges from 1.61 (Hipposideridae, n=7) to 2.54 (Rhinolophidae, n=22), with Vespertilionidae (n=40) at 2.20 and Pteropodidae (n=20) at 2.05. Overall mean tvs = 2.18 (range: 0.10–4.63). Rhinolophids host significantly higher viral richness on average, consistent with their known role as reservoirs for SARS-like coronaviruses and other zoonotic RNA viruses.

### Statistic 2: Landscape Heterogeneity and Viral Richness (Intestine Samples)
In the intestine-specific ecological model subset (n=27 pools), Pearson correlations with tvs reveal that **terrain slope (sl)** is the strongest single predictor (r = −0.598), followed by **Shannon landscape entropy (H10)** (r = +0.595), and **bat species diversity index (btsm)** (r = +0.437). The negative correlation with slope and positive correlation with landscape entropy suggest that spatially diverse, low-gradient habitats (e.g., valley/agricultural mosaics) are associated with higher intestinal viral richness. Climate variables (temperature, precipitation) show weak correlations (|r| < 0.17).

### Statistic 3: Tissue Tropism and Zero-Richness Prevalence
Comparing intestine vs. lung tissue pools: all 27 intestine pools have tvs > 0, whereas 4 of 25 lung pools (16%) have tvs = 0. This asymmetry indicates that enteric viral communities are more reliably detectable and consistently present across diverse bat hosts than respiratory ones, and that gut metagenomes carry a broader and more consistent RNA virome signal at the pool level.

### Statistic 4: Virome Contig Scale and Viral Family Breadth
The 8,176 contigs in `BtCN-Virome_full_spectrum.fna` span 405 pool sample codes, with a mean length of 1,326 bp. Phylogenetic analysis in `48306316_ML_Phylo.zip` resolves 13 RNA virus orders/families (Picornavirales, Reovirales, Bunyavirales, Coronaviridae, Durnavirales, Mononegavirales, Permutotetraviridae, and others). The `43059586_RdRp_motif_collection.xlsx` provides a cross-order RdRp motif reference (motifs G, F, A–E) enabling classification of novel sequences even at low amino acid identity.

## 3. Reasoning

The dataset uniquely combines: (i) a large-scale bat virome (metagenome-assembled contigs from 405 pools representing 5 bat families across multiple Chinese provinces and years), (ii) ecological predictors at two scales—climate and land use/landscape heterogeneity—for each pool, and (iii) host barcode sequences enabling host-specificity inference. The striking correlations between viral richness and landscape entropy (H10) and bat species diversity (btsm) point toward a dilution-effect or diversity-amplification dynamic. However, these are aggregate (pool-level) associations. The critical unresolved question is whether **habitat heterogeneity mediates viral richness through bat host diversity** (the "diversity-begets-diversity" amplification hypothesis) or whether it simply increases sampling exposure to multiple co-roosting species. The data structure—multi-host pools, landscape variables, and virome composition—is precisely suited to test whether landscape entropy and bat species co-occurrence diversity jointly predict cross-family viral richness in bat intestinal metagenomes, while controlling for climate.

## 4. Top Scientific Question

Does landscape Shannon entropy (H10), by aggregating multiple bat host species in spatially heterogeneous habitats, predict elevated intestinal RNA virome species richness (tvs) across Chinese bat communities independently of climate covariates (tas10, pr10, vpd10)?

## 5. Testability on the Provided Dataset

This question is directly answerable using the provided data. The ecological metadata (`Meta_data_for_ecological_modeling/intestine.txt`) contains both the response variable (`tv`, intestinal viral richness per pool) and all candidate predictors: `H10` (Shannon landscape entropy), `btsm` (bat co-occurrence diversity), `tas10`/`pr10`/`vpd10` (climate controls), and `family` (bat family as covariate). A multiple linear regression or partial correlation analysis of tv ~ H10 + btsm + tas10 + pr10 + vpd10 + family, using the 27 intestine pools, directly tests the hypothesis. The contrast between the strong correlations for landscape variables versus the weak climate correlations already observed provides a prior for effect size. The bat host barcode data (`chiroptera_CytB_COI.fas`) and virome contigs enable extension to test whether specific viral clades (via RdRp motif classification from `RdRp_motif_collection.xlsx`) drive the landscape entropy effect.
