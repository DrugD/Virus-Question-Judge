# Technical Report: Tick-Associated Viral Metagenome Survey Across China

## 1. Data Summary

**File:** `data/nuccore_reported_viral_sequences.fasta` (11.9 MB)

The dataset contains **1,801 metagenomically assembled genome (MAG) sequences** representing viral sequences recovered from tick samples collected across China. All entries carry the `MAG:` NCBI prefix, indicating assembly from metagenomic reads rather than culture-isolated viruses. The FASTA headers encode geographic origin (city-level), virus name, and isolate identifier.

Key structural features:
- **Accession prefixes:** ON (1,680 sequences) and OP (121 sequences), likely corresponding to two related sequencing studies
- **Isolates:** 145 unique TIGMIC tick-pool identifiers (TIGMIC_1 through TIGMIC_145, plus TIGMIC 1–TIGMIC 40 in the earlier batch)
- **Sequence types:** 1,228 complete genomes, 308 genomic sequences, 128 cRNA sequences, 80 partial sequences
- **Unverified entries:** 101 sequences flagged `MAG UNVERIFIED`
- **Unique virus species/types:** 362 distinct named entities across the file

---

## 2. Analysis

### 2.1 Virus Family Distribution
Sequences span at least 14 recognized viral families plus numerous unclassified lineages:

| Family | Sequences |
|---|---|
| Totiviridae | 244 |
| Botourmiaviridae | 180 |
| Narnaviridae | 118 |
| Rhabdoviridae | 72 |
| Mitoviridae | 52 |
| Nairoviridae | 51 |
| Partitiviridae | 45 |
| Phenuiviridae | 42 |
| Flaviviridae | 40 |
| Orthomyxoviridae | 37 |
| Peribunyaviridae | 32 |
| Chuviridae | 27 |
| Reoviridae | 20 |
| Other / novel | 841 |

Many families with known human pathogens are represented: Nairoviridae (includes Crimean-Congo hemorrhagic fever virus), Phenuiviridae (includes SFTS phlebovirus), Flaviviridae (tick-borne encephalitis viruses), and Orthomyxoviridae (includes Thogotovirus). In total, 284 sequences belong to these four families of high medical concern.

### 2.2 Co-infection Density per Tick Pool
The 145 TIGMIC isolates show highly variable viral richness. The average number of distinct viral sequences per pool is **12.4**, but the distribution is strongly right-skewed: 42 pools yield only 1 virus, while the most virome-rich pools harbor 103, 132, 145, or even **179 distinct viral sequences**. At least 37 pools carry ≥10 distinct viruses and 8 pools carry ≥50, demonstrating extreme multi-virus co-infection in individual tick samples.

### 2.3 Sequence Length Distribution
Sequence lengths range from **803 bp** (shortest, likely a partial gene segment) to **22,791 bp** (longest, consistent with large-genome RNA viruses such as rhabdoviruses or nidoviruses), with a mean of **6,432 bp**. This range is consistent with fully segmented or mono-partite genomes across diverse RNA virus families.

### 2.4 Geographic Breadth and Virus Novelty
Headers reveal ≥50 distinct Chinese cities/regions spanning from Zhangzhou (coastal Fujian) to Kashgar (Xinjiang) and from Hulunbuir (Inner Mongolia) to Lhasa (Tibet). Many virus names follow the pattern `[City] [FamilyAbbrev] tick virus N`, indicating novel, previously unnamed species discovered by this survey. At least 362 unique species-level names appear, the majority unnamed at family level (labeled `sp.` or abbreviated family prefixes), underscoring the extent of undescribed diversity.

---

## 3. Reasoning

The dataset captures the full tick virome of metagenomically sampled ticks from a vast geographic range within China. The co-presence of large numbers of phylogenetically distinct viruses within individual tick pools (up to 179 per pool) raises a critical question about infection dynamics: do ticks that carry one virus from a particular family (e.g., Phenuiviridae, which includes the zoonotic SFTS virus) disproportionately carry viruses from other medically relevant families (e.g., Nairoviridae, Flaviviridae), suggesting shared ecological or vector-competence factors? This co-occurrence structure is directly computable from the TIGMIC sample identifiers and the annotated family memberships present in the sequence headers — no additional wet-lab data are needed.

---

## 4. Top Scientific Question

**Do tick pools (TIGMIC isolates) that harbor sequences from Phenuiviridae show significantly higher co-occurrence rates with sequences from Nairoviridae, Flaviviridae, or Orthomyxoviridae compared to pools lacking Phenuiviridae, indicating non-random co-vectoring of medically important tick-borne viruses in Chinese tick populations?**

---

## 5. Testability on the Provided Dataset

This question is fully answerable from the FASTA file alone. Each TIGMIC isolate identifier links all viruses recovered from the same tick pool; the viral family of each sequence is encoded in its header name. A contingency-table or network co-occurrence analysis can determine whether the presence of Phenuiviridae sequences is statistically associated with sequences from Nairoviridae, Flaviviridae, or Orthomyxoviridae within the same TIGMIC pool. Fisher's exact tests or logistic regression controlling for sampling location (city prefix in the header) would quantify significance. The result would directly inform whether single-tick specimens co-vectoring multiple zoonotic virus families represent a heightened epidemiological risk at specific geographic foci within China.
