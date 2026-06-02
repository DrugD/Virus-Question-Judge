# Technical Report: BtCN-Virome Dataset Analysis

## 1. Data Summary

Five files were found under `data/`:

| File | Description | Scale |
|---|---|---|
| `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` | BtCN-Virome: full-spectrum viral metagenomic contigs from Chinese bats | 8,176 contigs, 405 distinct pool samples |
| `43059586_RdRp_motif_collection.xlsx` | Reference RdRp conserved motifs (A–E) across 13 viral orders | 22 rows × 13 columns; motifs for Permutotetra, Orthomyxo, Mononega, Bunya, Reo, +RNA |
| `43059592_CytB-COI-ITS.tar.gz` | Host barcodes: bat CytB (19,367 seqs) + COI (20,505 seqs); Arthropoda COI/CytB (515,372 seqs); Mollusca (39,050); Streptophyta ITS (106,078) | >700,000 sequences total |
| `45561465_Meta_data_for_ecological_modeling.zip` | Ecological metadata for 98 bat pool samples: viral richness (tvs), 9 climate/land variables, bat family, tissue type, pool size | 98 rows × 14 columns |
| `48306316_ML_Phylo.zip` | Maximum-likelihood RdRp phylogenies for 13 viral orders (Picorna, Corona, Bunya, Mononega, Reo, Permuto, Sobeli, Stella, Toli, Durna, Ghabri, Hepeli, Jingchu) | 99–1,250 sequences per tree; includes ZOVER-bat and EVRD-aa references |

**Ecological metadata key columns**: `tvs` = total virus species richness score (continuous, range 0.103–4.631); climate variables `srs10` (bat species richness), `H10` (landscape heterogeneity), `hurs10` (humidity), `pr10` (precipitation), `tas10` (temperature), `vpd10` (vapor pressure deficit); `family` (5 bat families: Eb, Hs, Pt, Rh, Ve); `st` (tissue: brain, intestine, kidney, liver, lung); `sp` (pool size, mean 46.6 bats, range 21–74).

---

## 2. Analysis

### 2.1 Viral richness (tvs) varies strongly by tissue type
Intestine pools show the highest mean viral richness (mean tvs = 2.664, n = 27), followed by liver (2.250), kidney (2.081), lung (2.027), and brain (1.356, n = 10). The intestine-to-brain difference suggests tissue tropism is a primary axis of bat virome diversity.

### 2.2 Landscape heterogeneity is the strongest climate predictor of tvs
Pearson correlations between tvs and nine environmental covariates:

| Variable | r |
|---|---|
| H10 (landscape heterogeneity) | **+0.228** |
| srs10 (bat species richness) | −0.130 |
| pr10 (precipitation) | −0.163 |
| tas10 (temperature) | −0.164 |
| hurs10 (humidity) | −0.106 |
| pet10 | −0.113 |
| vpd10 | −0.065 |

This association is tissue-specific: within intestine samples r(tvs, H10) = 0.595; within brain samples r = 0.827, suggesting that heterogeneous landscapes may concentrate diverse bat roost communities and facilitate viral transmission.

### 2.3 Rhinolophid bats harbor the highest mean viral richness
Mean tvs by bat family: Rhinolophidae (Rh) = **2.543** > Vespertilionidae (Ve) = 2.196 > Pteropodidae (Pt) = 2.046 > Emballonuridae (Eb) = 2.018 > Hipposideridae (Hs) = 1.607. Rhinolophids are well-known reservoirs of SARS-related betacoronaviruses; their consistently elevated tvs across 22 sampled pools suggests broader multi-order virus hosting capacity.

### 2.4 Virome contig assembly statistics
8,176 contigs (≥ 500 bp cutoff) from 405 pool samples; mean length 1,326 bp (range 500–19,176 bp). Pool-level contig counts range from 1 to 592 (mean 20.2). Correlation between pool-level contig count and tvs is r = 0.248, indicating that sequencing depth partially but not fully explains richness variation.

### 2.5 Phylogenetic breadth spans 13 viral orders with bat-derived clades in all
The ML_Phylo dataset includes reference trees for 13 orders (Picornavirales = 1,250 seqs; Mononegavirales = 422; Durnavirales = 397). ZOVER-bat sequences appear in all 13 trees alongside EVRD-aa, positioning BtCN-Virome contigs within established mammalian viral diversity. The RdRp motif reference (motifs A–E, plus G, F1/F2/F3) enables classification of novel contigs to order level.

---

## 3. Reasoning

The combination of (a) 8,176 viral contigs with sample provenance, (b) continuous viral richness scores (tvs) paired with nine ecological covariates, (c) bat family labels, and (d) tissue-type labels creates an ideal multi-variate dataset to dissect the ecological drivers of bat virome diversity. The dominant finding—that landscape heterogeneity (H10) positively predicts tvs while temperature and precipitation do not—raises a mechanistic question: does habitat fragmentation increase contact rates among bat species or among bats and their arthropod prey (the arthropod barcode sequences are also present), amplifying virus diversity? This is directly testable by modeling tvs as a function of H10, bat family, tissue type, and pool size using the 98-sample ecological dataset.

---

## 4. Top Scientific Question

Does landscape heterogeneity (H10) independently predict bat-virome viral richness (tvs) across Chinese bat populations after controlling for host phylogeny (bat family), tissue type, and pool size, and if so, does the effect operate primarily through Rhinolophidae intestinal communities?

---

## 5. Testability on the Provided Dataset

This question is fully testable using `Meta_data_for_ecological_modeling/total.txt`: tvs is the continuous response variable; H10, bat family, tissue type (st), and pool size (sp) are covariates available for all 98 rows. A mixed-effects linear model (tvs ~ H10 + family + tissue + sp + H10×family) can be fitted directly. The intestinal sub-dataset (`intestine.txt`, 27 rows) enables a focused test of the family-specific effect, where the Rhinolophidae stratum (5 intestinal pools, mean tvs = 3.163) can be compared against the other four families. No additional wet-lab experiments are required; the richness scores and all predictors are already computed and tabulated.
