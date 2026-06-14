# Technical Report: BtCN Bat Virome Dataset Analysis

## 1. Data Summary

Five files were examined under `data/`:

| File | Description | Scale |
|---|---|---|
| `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` | FASTA of metagenomic assembly contigs from bat virome study (BtCN-Virome) | 8,176 sequences from 347 pools (≥500 bp) |
| `43059586_RdRp_motif_collection.xlsx` | Reference table of conserved RNA-dependent RNA polymerase (RdRp) motifs (A–E/G) across viral lineages | 21 rows × 8+ columns |
| `43059592_CytB-COI-ITS.tar.gz` | BLAST databases for host barcoding (chiroptera CytB/COI, arthropod COI/CytB, plant ITS) | 4 taxonomic groups |
| `45561465_Meta_data_for_ecological_modeling.zip` | Ecological metadata: per-pool total viral Shannon diversity (TVS), 9 climate variables, bat family, organ, and bat species richness | 98 pooled samples across 5 bat families, 5 organ types |
| `48306316_ML_Phylo.zip` | IQ-TREE maximum-likelihood phylogenies for BtCN virome RdRp sequences across 13 viral orders/families, with ZOVER-bat and EVRD-aa references | 13 viral clades; 139 BtCN sequences placed in 12 clades |

**Key structural features:** Pool codes encode bat family, site, organ, and year (e.g., `RSQJC08` = Rhinolophus sinicus, Qingjian site, intestine, 2008). Climate variables include near-surface temperature (`tas10`), precipitation (`pr10`), vapor pressure deficit (`vpd10`), relative humidity (`hurs10`), and others summarized over the same spatial-temporal window.

---

## 2. Analysis

### Statistic 1: Viral Shannon Diversity (TVS) by Organ Tissue
Across 98 pooled samples (5 bat families, 5 organs), TVS ranged from 0.103 to 4.631 (mean = 2.185 ± 0.964 SD). The intestine (In) had the highest mean TVS (2.664 ± 0.940, n = 27), followed by liver (Li, 2.250), kidney (Ki, 2.081), lung (Lu, 2.027), and brain (Br, 1.356 ± 0.795, n = 10). Brain samples show both the lowest mean and a near-significant depression relative to intestine (difference ≈ 1.31 Shannon units).

### Statistic 2: TVS by Bat Family
Rhinolophidae (Rh) showed the highest mean TVS (2.543 ± 0.834, n = 22), compared with Vespertilionidae (Ve, 2.196 ± 1.196, n = 40), Pteropodidae (Pt, 2.046 ± 0.665, n = 20), Emballonuridae (Eb, 2.018 ± 0.736, n = 9), and Hipposideridae (Hs, 1.607 ± 0.463, n = 7). Rhinolophidae consistently harbors the highest within-sample viral alpha diversity.

### Statistic 3: Climate–Diversity Correlations
Spearman rank correlations between TVS and climate variables were consistently weak but consistently negative for temperature-related variables: r(TVS, tas10) = −0.224, r(TVS, vpd10) = −0.158, r(TVS, pet10) = −0.149, r(TVS, pr10) = −0.067. The correlation with local bat species richness (`sp`) was negligible (r = 0.061). These patterns suggest that warmer, drier microenvironments are marginally associated with reduced within-pool viral diversity, possibly through host physiological constraints.

### Statistic 4: Virome Contig Composition
The 8,176 contigs span 500–19,176 bp (median 811 bp, mean 1,326 bp), distributed across 347 bat pool samples. BtCN sequences were placed into 12 of 13 viral clades in the ML phylogenies (absent only from the Coronaviridae analysis, which was dominated by ZOVER-bat reference sequences). The largest BtCN representation was in Picornavirales (40 sequences of 1,250 total), Mononegavirales (15), and Durnavirales (17), indicating broad RNA virus diversity spanning positive-sense, negative-sense, and dsRNA lineages.

---

## 3. Reasoning

The ecological metadata directly links within-pool viral Shannon diversity to bat family identity, organ tissue type, and a suite of 9 standardized climate covariates — a design purpose-built for ecological modelling of zoonotic risk drivers. The consistent organ-level gradient (intestine >> brain) in TVS co-occurs with matched samples from the same pools, enabling within-host compartment comparisons. The bat family effect (Rhinolophidae highest) is ecologically significant because Rhinolophus bats are the primary reservoir attributed to SARS-like coronaviruses. However, the ML phylogenies include 13 viral orders/families simultaneously reconstructed with the same BtCN virome sequences, and the RdRp motif table provides a functional scaffold for comparing polymerase conservation across these clades. The full-spectrum virome contigs tie these phylogenetic identities back to individual sampling pools documented in the metadata. Together, the multi-scale design — from RdRp motif conservation to ecological modelling — motivates a question about which host and environmental factors drive the observed variation in bat virome diversity across organs, species, and geographic sites.

---

## 4. Top Scientific Question

Does bat family identity (Rhinolophidae vs. Vespertilionidae vs. Pteropodidae) predict total viral Shannon diversity (`tvs`) independently of organ tissue type (intestine, lung, kidney, liver, brain) and climate covariates (near-surface temperature `tas10`, vapor pressure deficit `vpd10`) across the 98 pooled BtCN-Virome samples, and if so, which bat-family-by-organ combinations carry the highest broad-spectrum RNA virus diversity?

---

## 5. Testability on the Provided Dataset

This question is fully answerable using the provided data. The `Meta_data_for_ecological_modeling/total.txt` file contains `tvs` as a continuous response variable for all 98 pools, with bat `family` (5 levels: Eb, Hs, Pt, Rh, Ve), `st` (organ tissue: Br, In, Ki, Li, Lu), bat species richness (`sp`), and 9 climate covariates for each. A linear mixed model or generalised additive model with `tvs ~ family * organ + tas10 + vpd10 + (1|site)` can directly partition variance attributable to each factor. The full-spectrum contig FASTA and ML phylogenies provide independent validation by confirming which viral taxa (spanning 12 orders/families) are differentially represented across pools with extreme vs. low TVS, grounding the diversity index in concrete viral taxonomy.
