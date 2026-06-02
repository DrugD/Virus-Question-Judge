# Technical Report: RNA Virome of *Magallana gigas* (Pacific Oyster) — Luchao Port, Shanghai

## 1. Data Summary

Six supplementary files from a study on the oyster RNA virome were analyzed:

| File | Description | Key Contents |
|---|---|---|
| `MOESM1_ESM.xlsx` | Sampling metadata | 16 collection batches (June 2016 – July 2017), 173 individual *M. gigas* from Luchao Port, Shanghai; plus 32 public mollusk/seawater libraries |
| `MOESM2_ESM.xlsx` | Viral abundance tables | 4 sheets: (1) 156 viral RNA contigs with TPM and taxonomy in *M. gigas* metatranscriptomes; (2) per-individual TPM × 17 samples; (3) TPM across 11 other mollusk libraries; (4) TPM in Yangshan harbor seawater RNA virome |
| `MOESM3_ESM.xlsx` | RdRp BLAST results | 756 BLAST hits for 146 oyster contigs against reference RdRp sequences |
| `MOESM4_ESM.fa` | RdRp amino-acid sequences | 154 predicted RdRp sequences (median 742 aa, range 206–3215 aa) |
| `MOESM5_ESM.zip` | Phylogenetic alignment FASTAs | 9 FASTAs for 9 RNA virus orders/families; 147 oyster sequences placed among reference taxa |
| `MOESM6_ESM.jpg` | Supplementary figure | Visual summary (not analyzed numerically) |

**Scale:** 156 viral RNA contigs, 173 oyster individuals, 13-month time series, 9 RNA virus orders, 11 additional mollusk host libraries, 1 adjacent seawater virome.

---

## 2. Analysis

### 2.1 Taxonomic Composition and Dominance

Of the 156 viral RNA contigs detected in *M. gigas*, **Marnaviridae** dominates overwhelmingly: 68 contigs (44%) account for **60.9% of total normalized expression (TPM)**, followed by Picobirnaviridae with 24 contigs (15%) contributing **28.2% of TPM**. Together, just two families account for ~89% of viral RNA abundance. The remaining 64 contigs span 12 additional groups including Picornavirales, Tombusviridae, Nodaviridae, Narnaviridae, Weiviridae, Sobelivirales, Dicistroviridae, Yanvirus, Hepelivirales, Fiersviridae, Caliviridae, and Partiviridae. Nine RNA-virus orders/families are represented in the phylogenetic alignment FASTAs (MOESM5).

### 2.2 Viral Novelty Assessed via RdRp BLAST

BLAST searches of 146 confirmed RdRp sequences against known references (MOESM3) yielded a **median best amino-acid identity of 0.64**. Only 33/146 contigs (23%) had a best hit ≥90% identity; 39 contigs (27%) had best-hit identity <50%, indicating highly divergent or potentially novel virus species. Mean best-hit identity was 0.660 ± 0.165, placing the majority of oyster viruses in the "divergent but assignable" range.

### 2.3 Within-Host Prevalence and Individual Variation

Across 17 individual *M. gigas* metatranscriptomic libraries (MOESM2, sheet "M.hongkongensis"), two contigs — **k141_147375 (Picobirna) and k141_94377 (Marna)** — were detected in **all 17 individuals** (prevalence = 17/17). Mean TPM for k141_147375 was 256,903 (CV = 1.45) and for k141_94377 was 125,843 (CV = 2.42). An additional 4 contigs appeared in ≥11/17 individuals, while 25 contigs were found in only 1–2 individuals, indicating a bimodal structure of core persistent and sporadic accessory viruses.

### 2.4 Cross-Environment Sharing with Seawater

Of the 156 oyster-associated viral contigs, **31 (20%) were also detected in the Yangshan harbor seawater RNA virome** (MOESM2, sheet "Yangshan_harbor"). The 57 seawater-positive contigs had a mean TPM of 17,544. The top five shared viruses by oyster TPM are all Marna family (k141_94377, k141_179532, k141_40569, k141_53240, k141_112007). Viruses shared with seawater had a substantially higher mean TPM in oysters (9,774 vs. 5,667 for seawater-absent viruses), suggesting that highly active oyster viruses are also shed or transmitted via the water column.

---

## 3. Reasoning

The dataset uniquely combines (a) a 13-month longitudinal sampling series across 16 collection batches with 173 individual oysters, (b) individual-level metatranscriptomic resolution across 17 libraries, (c) host-range cross-referencing across 11 other mollusk species, and (d) paired seawater virome data from the same harbor. The presence of two core Picobirna and Marna viruses in every sampled individual across all seasons, combined with the detection of 31 oyster viruses in adjacent seawater, creates a tractable system to ask whether environmental transmission from seawater determines the persistent core RNA virome of *M. gigas* across seasons. This question is scientifically non-trivial because filter-feeding bivalves constantly process large water volumes and the direction of viral flow (seawater → oyster uptake vs. oyster shedding → seawater) is unresolved in natural populations. It also has aquaculture biosecurity and seafood safety significance. The data provide TPM in both compartments, prevalence across individuals, and a 13-month time axis, making quantitative modeling feasible.

---

## 4. Top Scientific Question

**Do the high-abundance Marnaviridae and Picobirnaviridae RNA viruses detected in Yangshan harbor seawater serve as the environmental reservoir driving persistent, near-universal infection of *Magallana gigas* at Luchao Port across 13 months of seasonal sampling?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The dataset directly supports this question through four complementary analyses: (1) the Yangshan harbor seawater RNA virome (MOESM2, "Yangshan_harbor" sheet) provides TPM and covered-fraction for 57 oyster-associated contigs in water, establishing environmental presence; (2) the 17-individual *M. gigas* metatranscriptomic libraries (MOESM2, "M.hongkongensis" sheet) provide prevalence and TPM for the same contigs within hosts; (3) the 16-batch longitudinal sampling spanning June 2016–July 2017 (MOESM1) enables seasonal trend analysis; and (4) the MOESM2 "Abundance_of_oyster_RNA_virus" sheet explicitly flags each contig as detected/not-detected in seawater, in *C. hongkongensis*, and in other mollusks, allowing stratified comparison. Correlation between seawater TPM and within-host prevalence/abundance, combined with seasonal co-variation, would quantitatively address whether seawater is the transmission source for the two universally prevalent core viruses (k141_147375 and k141_94377).
