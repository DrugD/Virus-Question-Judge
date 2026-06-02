# BtCN-Virome Scientific Question Report

## 1. Data summary

The upload bundles five resources that together describe a bat-centred virome study in China (the "BtCN-Virome") plus the reference data used to place its sequences phylogenetically and ecologically.

| File | Content (verified) |
|---|---|
| `data/43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` → `BtCN-Virome_full_spectrum.fna` | 8,176 nucleotide contigs from **405 distinct sample pools** (e.g. `MSJDC22`, `RPGXC15-17`, `HABSC17`); contig length 500–19,176 bp (median 811, mean 1,326); 2,478 ≥1 kb, 206 ≥5 kb, 58 ≥10 kb. |
| `data/43059586_RdRp_motif_collection.xlsx` | Single sheet, 21 rows × 13 columns of canonical RdRp catalytic motifs (G, F1/F2/F3, A, B, C, D, E) curated across 12 viral lineage groupings (Permutotetra, Orthomyxo, Mononega, Bunya, Reovirales, Durnavirales, Picorna, etc.). |
| `data/43059592_CytB-COI-ITS.tar.gz` | Host/eukaryote barcode references: `Bats/COI.fasta` (20,505 seqs) and `CYTB.fasta` (19,367 seqs) for Chiroptera, plus `Arthropoda_COI_CYTB.99.fna` (515,372), `Mollusca_COI_CYTB.99.fna` (39,050), `Streptophyta_ITS.99.fna` (106,078) — clearly intended for host / dietary-item / arthropod-vector identification of contigs. |
| `data/45561465_Meta_data_for_ecological_modeling.zip` | Three TSVs (`total.txt` 98 rows, `lung.txt` 25, `intestine.txt` 27) with `Pool_code`, viral-richness response (`tvs`/`tv`), 10-yr climatic variables (`tas10`, `pr10`, `hurs10`, `vpd10`, `pet10`, `sfcwind10`, `rsds10`, `srs10`, `H10`), land-cover variables (`nt`, `sl`, `gm`, `cy`, `sy`, `bx`, `ld`, `btsm`, `sd`), bat family (`Hs`, `Ve`, `Rh`, `Pt`, `Eb`) and tissue (`In`, `Lu`, `Li`, `Ki`, `Br`). |
| `data/48306316_ML_Phylo.zip` | 13 RdRp maximum-likelihood phylogenies (one per viral order/group) with `.faa`, mafft alignments, trimmed alignments, IQ-TREE `.contree`, `.treefile`, `.iqtree`, `.bionj`, `.mldist`, `.splits.nex`, `.model.gz`. |

## 2. Analysis (derived)

1. **Sampling effort vs. contig yield (FASTA + meta join).** Among 405 pool IDs in the contig FASTA, the top 10 pools (`MSJDC22` 592, `RPGXC15-17` 388, `JTYGC13_16` 186 …) account for ~26% of all contigs, indicating a strongly right-skewed per-pool yield.
2. **Host-family imbalance (`total.txt`).** Of 98 ecological-modeling rows: Vespertilionidae (`Ve`) = 40, Rhinolophidae (`Rh`) = 22, Pteropodidae (`Pt`) = 20, Hipposideridae (`Hs`) = 7, Emballonuridae (`Eb`) = 9. Tissues: intestine 27, kidney 22, lung 22, liver 17, brain 10 — i.e. gut and kidney are the most deeply sampled compartments.
3. **Phylogenetic novelty (`ML_Phylo`).** Counting the proportion of non-`GenBank_REF` (i.e., novel BtCN-Virome) tips in the final trimmed alignments shows a high novelty rate per RdRp-defined order: Picornavirales 741/911 (81%), Toli 267/344 (78%), Mononega 236/313 (75%), Bunya 169/256 (66%), Stella 158/158 (100%), Hepeli 160/160, Durna 255/255, Permuto 62/66; Coronaviridae shows only 68 sequences and far fewer novel relative to other orders.
4. **RdRp motif framework.** The xlsx catalogues the seven canonical motifs (G, F1–F3, A, B, C[GDD], D, E) and their lineage-specific variants (e.g. SDD vs. GDD; DxxKWN/DxxKWS for Mononega/Bunya), enabling order-level RdRp authentication of any contig.

## 3. Reasoning

The dataset is a complete, end-to-end resource: novel bat-derived RNA-virus contigs (output), an RdRp motif rulebook (validation), reference phylogenies in 13 RdRp lineages (placement), barcode references for hosts, arthropod vectors and plants (host/diet attribution), and georeferenced climate & land-cover covariates per pool (ecological modeling). The combination is unusual — most bat-virome studies stop at discovery and a single phylogeny. Here, the joint presence of (a) per-pool climatic/land-use covariates with a `tvs`/`tv` viral-richness response, (b) per-tissue stratification, and (c) host barcodes that include arthropod and plant references invites a question that bridges discovery and predictive ecology rather than a routine taxonomic-novelty count.

## 4. Top scientific question

**Which combination of long-term climatic variables (e.g., `tas10`, `pr10`, `hurs10`, `vpd10`, `pet10`) and land-use variables (e.g., `nt`, `sl`, `gm`, `cy`, `bx`) at the bat-roost scale most strongly predicts pool-level RNA virome richness (`tvs`) across Chinese bat families and tissue compartments, and does this climate–richness relationship differ for zoonotically relevant RdRp lineages (Coronaviridae, Bunyavirales, Mononegavirales) versus arthropod-/plant-borne lineages (Picornavirales, Stellavirales)?**

## 5. Why this question is testable on the provided dataset

- **Response variable** is already engineered: `tvs`/`tv` columns in `total.txt`, `lung.txt`, `intestine.txt` quantify virome richness per pool, with tissue stratification.
- **Predictors** are aligned to the same `Pool_code` keys: `tas10`, `pr10`, `hurs10`, `vpd10`, `pet10`, `sfcwind10`, `rsds10` (climate) and `nt`, `sl`, `gm`, `cy`, `sy`, `bx`, `ld`, `btsm`, `sd` (land cover/use), plus host `family` and tissue `st`.
- **Lineage stratification of richness** can be computed by mapping the 8,176 contigs to the 13 RdRp ML phylogenies in `ML_Phylo.zip` (e.g., by placing each VIRES-prefixed sequence on the `*.mafft.trimmed.80.mc.faa` alignments and the `*.contree`/`.treefile` trees) and aggregating per pool/order, with the `RdRp_motif_collection.xlsx` motifs serving as an order-level QC filter.
- **Statistical test**: GLMM/zero-inflated negative-binomial regression of order-specific contig counts on standardized climatic + land-use covariates with bat family and tissue as random effects; permutation tests or random-forest variable-importance to compare zoonotic vs. arthropod-/plant-borne lineage groups.
- All required inputs are on disk; no external wet-lab data are needed.
