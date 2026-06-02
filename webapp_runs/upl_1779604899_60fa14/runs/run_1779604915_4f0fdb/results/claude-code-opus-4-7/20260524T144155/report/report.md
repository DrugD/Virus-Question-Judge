# Report — Marine RNA Virome (Tara Oceans RdRp Catalog)

## 1. Data summary

The `data/` directory contains seven files associated with the manuscript *"Cryptic and abundant marine viruses at the evolutionary origins of Earth's RNA virome"* (a Tara Oceans / Tara Oceans Polar Circle metatranscriptome-derived RNA-virus catalog):

- `44779_RdRP_contigs.fna.gz` — 44,779 RNA-virus contigs identified by RdRp signal (mean length ≈1,191 nt, range 300–25,584 nt). Headers encode 567 distinct sample/station labels embedding depth-zone codes (SUR=12,031 contigs, DCM=14,685, MES=3,666, MIX=445, ZZZ=1,136); ~19,443 contigs carry a `TARA_` prefix.
- `5504_wcANI_based_clusters_90_80.fna.gz` — 5,504 viral OTU representatives clustered at 90% whole-contig ANI / 80% AAI (mean ≈2,714 nt, max 25.6 kb), the operational species units.
- `RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz` — 209,588 RdRp protein "footprint" sequences merging 160,167 GenBank reference entries (`REF_*`), 44,779 Tara entries (`Tara_*`), 4,593 Wolf-et-al-2018 ORFs (`orf.*`) and 49 additional sequences.
- `RdRp_footprints_..._centroids_50_percent.fasta.gz` — 13,109 centroids at 50% AA identity (the genus-/family-scale dereplicated set).
- `..._centroids_50_percent_near_complete.faa.gz` — 6,238 near-complete centroids (length-filtered for full RdRp domain).
- `functional-annotation-table.tsv` — 20,578 HMM/Diamond hits over 5,122 distinct vOTU-encoded proteins, with columns `qseqid, strand, dom_start, dom_end, desc, prob, evalue, score, database`.

## 2. Analysis (derived statistics)

1. **Database mix and viral-marker yield in the annotation table**: 8,004 hits from `hhblits-Wolf-et-al-2018`, 7,291 from `hhblits-pfam`, 5,283 from `diamond`. 5,028 of 20,578 annotations are explicitly tagged as viral (`|vir` suffix); 7,428 are pure RdRP signatures and 8,122 are other functions.
2. **RdRp family composition (top descriptors)**: 7,625 generic `RdRP` hits, 1,302 `RdRP_1`, 811 `Mitovir_RNA_pol`, 785 `RdRP_3`, 337 `Birna_RdRp`, 305 `RdRP_2`, 224 `RdRP_4`, 112 `Bunya_RdRp`, 109 `Mononeg_RNA_pol`. This co-occurrence of dsRNA (Birna), +ssRNA (RdRP_1–4), -ssRNA (Bunya, Mononeg), and Narnaviridae-like (Mitovir) signatures within one ocean catalog is striking.
3. **Auxiliary virus-protein signal beyond RdRp**: capsid markers from picorna-like lineages dominate (Calici_coat 333, CRPV_capsid 270, Waikav_capsid 349, Dicistro_VP4 204) alongside helicase (`RNA_helicase` 183, `ViralHelicase1` 132) and methyltransferase (`Vmethyltransf` 100, `Methyltrans_Mon` 88) hits — i.e., long contigs encode multi-gene cassettes, not just the RdRp anchor.
4. **Spatial coverage**: 567 sampling labels; depth-zone breakdown SUR ≈ 12,031, DCM ≈ 14,685 (the largest), MES ≈ 3,666 — clear oversampling of euphotic/DCM relative to mesopelagic.
5. **Clustering compression**: 209,588 footprints → 13,109 centroids (≈16-fold compression at 50% AAI), suggesting deep within-clade radiation; only 6,238/13,109 (47.6%) centroids are "near-complete," meaning roughly half of the diversity is currently RdRp-fragmentary.
6. **Length tail**: vOTUs span 1,001–25,584 nt; the upper tail (>15 kb) is the candidate territory for the proposed novel marine megataxa (Taraviricota, Pomiviricota, Paraxenoviricota, Wamoviricota, Arctiviricota named in `cyverse_readme.txt`).

## 3. Reasoning

The dataset is uniquely structured to support evolutionary and ecological inference at scale: every contig has (a) a station/depth tag embedded in its name, (b) a paired RdRp protein footprint, (c) a hierarchical clustering (90%/80% nucleotide vOTU → 50% AAI centroid → near-complete centroid), and (d) functional annotations across multiple viral RdRp Pfams plus capsid markers. Because depth zone (SUR/DCM/MES) is recoverable from the FASTA headers, and because RdRp family identity is recoverable from `functional-annotation-table.tsv`, depth-stratified family enrichment can be tested directly. The strong representation of Mitovir, Birnavirus, Bunyavirus and Mononegavirus RdRps alongside picorna-like capsids — in seawater — challenges the textbook view that those clades are mostly fungal/animal-host-restricted, and makes the strongest single-question opportunity a depth-stratified test of which RdRp super-groups expand in cryptic marine clades.

## 4. Top scientific question

**Which RNA-virus RdRp super-groups (Pfam classes RdRP_1–4, Mitovir_RNA_pol, Birna_RdRp, Bunya_RdRp, Mononeg_RNA_pol) are differentially enriched between surface (SUR), deep chlorophyll maximum (DCM), and mesopelagic (MES) Tara Oceans metatranscriptomes, and do the depth-enriched super-groups correspond to the near-complete RdRp centroids that fall outside known phyla (i.e., the proposed Taraviricota / Pomiviricota / Paraxenoviricota / Wamoviricota / Arctiviricota megataxa)?**

## 5. Why this question is testable on the provided dataset

Each of the 44,779 RdRP contigs carries a station/depth code in its FASTA header (SUR / DCM / MES, plus MIX/ZZZ), so every contig can be assigned a depth class without external metadata. The same contig identifiers join to `functional-annotation-table.tsv`, which provides the RdRp Pfam class for 5,122 vOTUs across `hhblits-pfam`, `hhblits-Wolf-et-al-2018` and `diamond` databases — yielding a contig × depth × RdRp-family contingency table testable by χ² / Fisher tests with FDR control. The 50%-AAI near-complete centroid set (6,238 sequences) lets a phylogenetic placement step identify which depth-enriched contigs sit on long branches outside Riboviria's classical phyla, directly mapping enrichment to the manuscript's candidate megataxa. The existence of 90/80 wcANI vOTUs additionally controls for redundancy so that depth comparisons reflect community composition rather than per-strain abundance.
