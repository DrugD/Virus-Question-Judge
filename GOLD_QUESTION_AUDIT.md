# Gold Scientific Questions — Source-Paper Audit

Each `data/<paper>/gold_scientific_questions.json` was checked against the **actual published paper** (abstract / full text retrieved live via NCBI E-utilities + Europe PMC). For every paper we verified the headline figures, the central scientific claim, the primary-vs-secondary framing, question wording, and the `required_elements`.

**Date:** 2026-06-04
**Coverage:** 11/11 papers, all source-verified (`source_found: yes`).

## Summary table

| Paper | Verdict | Action needed |
|---|---|---|
| amphibian_reptile_virome_2022 | ✅ ok | none |
| arthropod_neg_sense_2015 | ⚠️ minor | fix GQ_002 framing (+ check 147.4 Gb figure) |
| bat_btcn_virome_2024 | ✅ ok | optional: anchor geography to "China"; slug year 2024→2025 |
| flavi_jingmen_jvi_2016 | ✅ ok | optional: re-verify "12 runs / 96 Gb" methods figure |
| invertebrate_rna_virosphere_2016 | ⚠️ minor | fix GQ_002 "manual curation" framing |
| oyster_rna_virome_2024 | ⚠️ minor | relax GQ_002 novel-AND-abundant coupling (indicator framing is OK) |
| rvmt_cell_2022 | ✅ ok | none (optional: name picobirna/partitiviruses) |
| tara_oceans_science_2022 | ⚠️ minor | fix scale-number labeling (44,779 ≠ species) |
| tick_metavirome_2023 | ✅ ok | optional: de-emphasize geography in GQ_002 |
| vertebrate_rna_viruses_2018 | ⚠️ minor | soften GQ_002 "codivergence" → "association" |
| zooplankton_rna_virosphere_2022 | ✅ ok | none |

**7 ok / 4 minor issues / 0 major.** No gold question is factually wrong about the paper's core finding; the issues are over-specified framings and one data-card labeling inconsistency.

---

## Priority fixes (the 4 minor-issue papers)

### 1. arthropod_neg_sense_2015 — GQ_002
Verified abstract (PMID 25633976): 70 arthropod species, 112 novel viruses, "ancestral to much of the documented genetic diversity of negative-sense RNA viruses," viruses "fall basal to major virus groups (arenaviruses, filoviruses, hantaviruses, influenza viruses, lyssaviruses, paramyxoviruses)," and "a remarkable diversity of genome structures... including a putative circular form."

- **Problem:** GQ_002's framing — "bridge phylogenetic gaps between **segmented and non-segmented** negative-sense RNA virus groups" — is **not a claim the abstract makes**. The paper frames its viruses as *basal/ancestral* to major groups, not as bridging a segmented↔non-segmented divide. Scope/centrality over-reach.
- **Suggested rewrite:**
  > "Do newly assembled arthropod viruses fall basal to and reveal the ancestral diversity of major negative-sense RNA virus groups (e.g. arenaviruses, filoviruses, hantaviruses, influenza viruses, lyssaviruses, paramyxoviruses) in RdRP/L-protein phylogenies?"
- **required_elements:** replace `"segmented and non-segmented groups"` and `"phylogenetic gaps"` with `"basal placement to major negative-sense groups"` and `"ancestral genetic diversity"`. Keep the rest.
- **Also:** the `147.4 Gb` read-volume figure is **not in the abstract** — confirm against Methods before treating it as a benchmark-defining number. (GQ_001 itself is accurate — no change.)

### 2. invertebrate_rna_virosphere_2016 — GQ_002
Shi et al. 2016, Nature 540:539–543. GQ_001 is accurate (redefining virosphere breadth / deep lineages via phylogeny — the paper's core thesis).

- **Problem:** GQ_002 asks "Which recovered invertebrate RNA viruses have genome architectures... **requiring manual curation**?" — "manual curation" is a **data-handling/bioinformatics artifact, not a scientific question the paper poses**. The paper studies genome architecture / segmentation / gene gain-loss as biology, but never frames a finding as "which viruses require curation."
- **Suggested rewrite:**
  > "Which recovered invertebrate RNA viruses exhibit unusual genome architectures or segmentation patterns (e.g. gene rearrangement, gain/loss, or segmentation/de-segmentation) that expand known RNA-virus genome organization?"
- **required_elements:** keep `genome length`, `segmentation`, `architecture`, `assembled viral genomes`; **remove `manual curation`**; consider adding `gene rearrangement` or `segmentation/de-segmentation`.

### 3. tara_oceans_science_2022 — data-card scale labeling
Verified abstract (PMID 35389782): "≈28 terabases of Global Ocean RNA sequences," "necessitate substantive revisions of taxonomy (**doubling phyla and adding >50% new classes**)," Taraviricota = "a missing link in early RNA virus evolution." Both gold questions are scientifically **ok** as written.

- **Problem:** the benchmark's scale string treats `44,779` (RdRP **contigs**) and `~5,500` (`5,504` wcANI species-rank representatives) as if interchangeable. They are different units. Anyone reading "44,779" as a species count is wrong.
- **Fix:** in the README/data card, label `44,779` explicitly as "RdRP contigs" and `5,504` as "species-rank (wcANI) representatives." No change to GQ text. (Optional: GQ_002 could mention "new phyla proposal" — the paper proposed ~5 new phyla, not just revised existing ones.)

### 4. oyster_rna_virome_2024 — GQ_002
Verified abstract (PMID 39707493): 173 *M. gigas* digestive-tissue samples, **154 viral RdRPs**, **144** putative novel species (94% <90% AA identity), and a documented **virus-sharing network** (37 / 25 oyster viruses also found in an octopus metatranscriptome / seawater virome). The "indicator" framing is **faithful** — the paper verbatim says viruses "have the potential to serve as indicators for identifying the circulation of marine RNA viruses." So keep it.

- **Problem (minor):** GQ_002 couples "novel **and** abundant" as if one virus must be both. In the paper these are *separate* sets — 144 novel species (by identity) vs 14 abundant RdRP sequences (≥1% of aligned reads). The indicator claim is made broadly, not about novel-and-abundant intersection.
- **Suggested rewrite:**
  > "Which abundant, RdRP-bearing RNA viruses identified in oyster digestive tissues — including newly described species — could serve as indicators for the circulation of marine RNA viruses?"
- **required_elements:** all five hold; just decouple novelty from abundance in the stem and mirror the paper's phrasing "circulation of marine RNA viruses."

---

## The 7 clean papers (verified, optional polish only)

- **amphibian_reptile_virome_2022** ✅ — 235 datasets / 122 species / 26 novel + 9 known all verified (abstract says "eight previously characterised," body/Table 1 says nine — benchmark's 9 follows the paper's own headline count). Both questions accurate; basal/divergent phylogeny claim directly supported (basal influenza clade, basal arenaviruses, fish–amniote intermediates).
- **bat_btcn_virome_2024** ✅ — 8,176 / 4,143 bats / 40 species / 52 locations verified exactly (PMID 39833544). "Ecological drivers" + "circulation near human settlements" (Nipah, Lloviu) is the paper's own headline → GQ_001 primary is correct. *Optional:* add "China" to GQ_001 geography (dataset is China-specific); slug year should be 2025, not 2024.
- **flavi_jingmen_jvi_2016** ✅ — 5 segmented jingmenviruses + 12 flavi-like viruses verified (PMID 26491167); NS3/NS5 shared-ancestry evidence confirmed verbatim. *Optional:* re-verify the "12 RNA-seq runs / 96 Gb" methods figure (paywalled, unconfirmed).
- **rvmt_cell_2022** ✅ — 5,150 metatranscriptomes / >2.5M contigs / >330K RdRPs / 5-fold expansion verified (PMID 36174579); CRISPR-spacer + bacteriolytic-protein host evidence for picobirna/partitiviruses confirmed. *Optional:* name those clades in GQ_002.
- **tick_metavirome_2023** ✅ — 31 species / 724 viruses / 1,801 genomes / 8,182 ticks verified (PMID 36604510); specialist/generalist reservoir framing is the paper's own. *Optional:* geography is secondary to host-range in GQ_002 — don't weight it co-equally.
- **vertebrate_rna_viruses_2018** ⚠️→effectively ok — 214 vertebrate-associated viruses verified (PMID 29618816). GQ_001 accurate. **GQ_002 minor:** "codivergence" over-weights strict cospeciation; the paper says virus branching "broadly reflected" host phylogeny *with* cross-species transmission. Soften to "deep, long-term virus-host association broadly mirroring host evolution (rather than strict one-to-one cospeciation)"; treat `codivergence` as a non-required alternative so host-switching answers aren't penalized.
- **zooplankton_rna_virosphere_2022** ✅ — 194 RdRP contigs / 189 OTUs / 21 ssRNA + 168 dsRNA verified exactly (PMID 34980753); FLDS confirmed as the dsRNA method; "no direct evidence of host species" confirms the host-association caveat. Both questions accurate.

---

*Audit method:* one domain-expert agent per paper, each retrieving the primary source live (NCBI eutils `efetch`/`esearch` + Europe PMC `resultType=core`), checking figures and claims against the abstract/full text, with explicit instruction not to invent. Papers initially blocked on WebFetch were re-run through the working curl path and all resolved to `source_found: yes`.
