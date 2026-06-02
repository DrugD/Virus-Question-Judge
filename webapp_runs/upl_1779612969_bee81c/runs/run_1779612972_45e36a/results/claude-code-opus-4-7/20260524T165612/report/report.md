# BtCN-Virome: Scientific Question Generation Report

## 1. Data summary

The upload comprises five archives describing a large bat-associated RNA virome (BtCN-Virome) survey paired with host genetic markers, virus marker motifs, ecological covariates and phylogenetic reconstructions:

- `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` → `BtCN-Virome_full_spectrum.fna`: a single nucleotide FASTA containing **8,176 assembled viral contigs** (mean length ≈ 810 bp, longest several kb) from **388 distinct sample-pool identifiers** such as `ASYGC15_17`, `HABJF22`, `MSWZN17`, `PPYCG16`, etc. Pool codes embed location, organ/tissue letter (C, F, G, H, N, P, S) and year.
- `43059586_RdRp_motif_collection.xlsx` (1 sheet, 22×13): a curated table of **conserved RdRp motifs (G, F, A, B, C, D, E)** across virus groups — All viruses, Permutotetraviridae, Orthomyxo, "−RNA", Mononega, Bunya, Reo, Reovirales, +RNA, Durnavirales, with consensus residues such as `GDD`, `SGxxxTxxxN`, `DxxxxD`, `SxG`, `KxR`.
- `43059592_CytB-COI-ITS.tar.gz`: host barcode reference databases — `Bats/COI.fasta`, `Bats/CYTB.fasta` plus a BLAST-formatted Chiroptera CytB+COI database (`chiroptera_CytB_COI.*`), and 99 %-clustered references for `Arthropoda_COI_CYTB.99.fna`, `Mollusca_COI_CYTB.99.fna`, `Streptophyta_ITS.99.fna` (i.e., insect/mollusc prey and plant diet markers).
- `45561465_Meta_data_for_ecological_modeling.zip`: `total.txt` (98 pool×organ rows), `intestine.txt` (27), `lung.txt` (25). Columns: `Pool_code, tvs, srs10, H10, hurs10, pet10, pr10, rsds10, sfcwind10, tas10, vpd10, family, st, sp` plus, in organ files, soil/landcover and `sample size`. `tvs` is the per-organ total-virome score; climate fields are 10-year means of solar radiation, humidity, evapotranspiration, precipitation, surface wind, temperature and vapour-pressure deficit.
- `48306316_ML_Phylo.zip`: 14 viral order-/family-level phylogenetic packages (`Bunya, Corona, Durna, Ghabri, Hepeli, Jingchu, Mononega, Permuto, Picorna, Reo, Sobeli, Stella, Toli`). Each tarball ships an unaligned `*.faa`, MAFFT alignment, trimAl-trimmed alignment, manually-checked alignment, and IQ-TREE outputs (`.treefile`, `.contree`, `.iqtree`, `.mldist`, `.splits.nex`, model files). The Corona package, for example, contains 68 RdRp sequences from BtCN-Virome (`VIRES|`), ZOVER-bat references (52) and EVRD references.

## 2. Analysis

Three quick derived statistics:

1. **Virome scale.** 8,176 contigs across 388 sample pools = ≈ 21 contigs / pool on average; metadata covers 98 pool×organ rows spanning **5 organs** (Br=10, In=27, Ki=22, Li=17, Lu=22) and **5 bat families** (Vespertilionidae=40, Rhinolophidae=22, Pteropodidae=20, Hipposideridae=7, Emballonuridae=9 in `total.txt`).
2. **Climate gradient.** Within `total.txt`, mean annual precipitation `pr10` ranges from < 1,000 to > 60,000 (units arbitrary in source) and `tas10` (mean 10-yr temperature) clusters 2,840–3,020 — capturing tropical/temperate East-Asian sites such as ASY, HAB, MSW, PPY, PPX, with covarying `vpd10` and `hurs10`. The `tvs` virome score within these rows ranges roughly from 0.10 (PPXSS17) to 4.23 (PPUQC17), giving > 40-fold variance in apparent viral richness across pools.
3. **Phylogenetic breadth.** Of 14 viral orders, the largest IQ-TREE inputs are Picorna (10.5 MB), Mononega (1.6 MB), Toli (1.85 MB), Hepeli (1.4 MB), Ghabri/Bunya/Stella ≈ 1 MB; the smallest is Permuto (0.24 MB) and Corona (0.14 MB, 68 taxa). All packages share a uniform `mafft → trimAl → IQ-TREE (1,000 ultrafast bootstraps, ModelFinder)` pipeline, with both automatic and manually-curated trees retained — enabling consistent cross-order comparison of branch lengths, divergence and host clustering.

## 3. Reasoning

The dataset is unusual because it links **(a)** a deeply sampled bat metaviromic catalogue, **(b)** matched host barcoding markers (CytB/COI) and prey/plant ITS markers from the same pools, **(c)** quantitative ecological covariates (climate, land cover, soil, sample size) per pool and organ, and **(d)** family-resolved RdRp phylogenies aligned to global references. This combination is precisely what is needed to ask whether observable **bioclimatic and host-ecological drivers predict the abundance and phylogenetic placement of bat-borne RNA viruses** — a central question for spillover surveillance. The presence of `intestine.txt` and `lung.txt` further enables organ-stratified inference, separating gut-tropic (likely diet/Picorna-rich) from respiratory-tropic (Corona/Paramyxo-rich) signatures. The RdRp-motif sheet anchors taxonomic placement of newly-assembled contigs, and the per-order ML phylogenies supply the reference scaffold to test whether new BtCN-Virome lineages cluster with mammalian-tropic clades versus invertebrate/plant-tropic clades — a direct proxy for zoonotic potential.

## 4. Top scientific question

**To what extent do site-level bioclimatic variables (`tas10`, `pr10`, `vpd10`, `hurs10`, `pet10`, `rsds10`, `sfcwind10`, `srs10`, `H10`) and bat host family (Vespertilionidae, Rhinolophidae, Pteropodidae, Hipposideridae, Emballonuridae) jointly predict organ-stratified RNA virome richness (`tvs` in lung versus intestine) and the phylogenetic affinity of BtCN-Virome RdRp contigs to mammalian-tropic versus invertebrate/plant-tropic clades within the 14 ML order-level reference trees?**

## 5. Why this question is testable on the provided dataset

Every component required is on disk:

- The response variables — per-pool/organ `tvs` and per-organ contig counts derivable from `BtCN-Virome_full_spectrum.fna` headers — are present in `Meta_data_for_ecological_modeling/{total,intestine,lung}.txt`.
- The bioclimatic predictors and the bat `family` factor are columns in those same TSVs (98 rows total).
- Phylogenetic affinity can be assessed by placing `VIRES|...` BtCN-Virome RdRp tips on the supplied IQ-TREE `*.treefile` / `*.contree` files for each of the 14 viral orders and labelling the nearest reference clade with mammalian/invertebrate/plant host metadata already present in the EVRD/ZOVER reference headers (e.g., `…Coronaviridae…Hypsugo_bat_coronavirus_HKU25`).
- Host identity per pool is verifiable through `Bats/CYTB.fasta` / `COI.fasta` and the Chiroptera BLAST DB; diet/parasite contamination can be screened against `Arthropoda_COI_CYTB.99.fna`, `Mollusca_COI_CYTB.99.fna`, `Streptophyta_ITS.99.fna`.
- Newly-assembled contigs can be assigned to viral orders by RdRp motif matching using the curated motif consensus in `RdRp_motif_collection.xlsx`.

A mixed-effects model (climate fixed + bat family random) on `tvs` per organ, combined with phylogenetic-placement counts per order, produces a falsifiable answer using only the supplied files.
