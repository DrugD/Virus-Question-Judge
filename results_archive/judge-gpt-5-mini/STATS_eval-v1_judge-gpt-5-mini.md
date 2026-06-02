# eval-v1 系统评测 · judge=`gpt-5-mini`

qset 数：**11** · agent 数：**11** · judge：**`gpt-5-mini`**

成功格子：**111** · 失败格子：**10** · 缺数据：**0**

评分维度：`match_strength` / `required_elements_coverage` / `acceptability` / `data_grounding`（各 0–5）· Comp 0–1 = 4 维加权

⚪ = `intern-s1-mini` 用户决定不再重测，保留首轮结果


## 0 · 覆盖矩阵

| qset | cc-opus-4-7 | gpt-5.5-high | cc-sonnet-4-6 | gem-3.1-pro | ds-v4-pro | glm-5 | gem-2.5-flash | intern-s1 | intern-s1-pro | intern-s1-mini ⚪ | intern-s2-prv |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `amphibian_reptile_virome_2022` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `arthropod_neg_sense_2015` | 🟢 | 🟢 | ✅ | ✅ | ✅ | 🟢 | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `bat_btcn_virome_2024` | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | ✅ | ✅ | 🟢 | ⚪ | ✅ |
| `flavi_jingmen_jvi_2016` | ✅ | ✅ | ✅ | ✅ | 🟢 | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `invertebrate_rna_virosphere_2016` | 🟢 | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `oyster_rna_virome_2024` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `rvmt_cell_2022` | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `tara_oceans_science_2022` | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ⚪ | 🟢 |
| `tick_metavirome_2023` | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `vertebrate_rna_viruses_2018` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `zooplankton_rna_virosphere_2022` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | 🟢 | 🟢 | ✅ | ✅ | ⚪ | ✅ |
| **合计 ✅** | **11/11** | **11/11** | **11/11** | **11/11** | **11/11** | **11/11** | **11/11** | **11/11** | **11/11** | **1/11** | **11/11** |

> 🟢 = pass@1 通过 · ✅ = 跑成功但 rank-1 没过 · ❌ = 5+ 次重试都没救活 · ⚪ = `intern-s1-mini` 不再重测 · 🟨 = 缺数据

## 1 · 各 agent 跨 qset 平均分（缺/失败按 0 计入；按 Comp 排序）

| Agent | 已成功 | match | req_elem | accept | data_grnd | Comp 0–1 | Pass@1 | Pass@5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `claude-code-opus-4-7` | 11/11 | 4.82 | 4.27 | 4.82 | 4.82 | **0.892** | 0.909 | 0.727 |
| `claude-code-sonnet-4-6` | 11/11 | 4.45 | 4.18 | 4.45 | 4.91 | **0.859** | 0.636 | 0.609 |
| `gpt-5.5-high` | 11/11 | 4.27 | 3.73 | 4.55 | 4.91 | **0.778** | 0.818 | 0.527 |
| `deepseek-v4-pro` | 11/11 | 2.82 | 2.36 | 3.09 | 4.55 | **0.528** | 0.273 | 0.232 |
| `gemini-3.1-pro` | 11/11 | 2.82 | 2.00 | 2.82 | 4.18 | **0.506** | 0.273 | 0.118 |
| `glm-5` | 11/11 | 2.73 | 1.82 | 3.18 | 4.00 | **0.506** | 0.364 | 0.214 |
| `gemini-2.5-flash` | 11/11 | 2.73 | 1.73 | 2.91 | 3.73 | **0.482** | 0.182 | 0.114 |
| `intern-s1-pro` | 11/11 | 2.55 | 1.45 | 2.64 | 3.73 | **0.438** | 0.091 | 0.055 |
| `intern-s2-preview` | 11/11 | 2.36 | 1.64 | 3.00 | 4.00 | **0.431** | 0.091 | 0.082 |
| `intern-s1` | 11/11 | 1.82 | 1.18 | 2.27 | 3.45 | **0.353** | 0.000 | 0.000 |
| `intern-s1-mini` ⚪ | 1/11 | 0.00 | 0.00 | 0.09 | 0.27 | **0.009** | 0.000 | 0.000 |


---
# Part II · 每个 (qset, agent) 的 5 个候选问题 + 完整文本


## 1 · `amphibian_reptile_virome_2022`

- **raw**：1 文件: `43705_2022_180_MOESM1_ESM.docx`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.80

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 2 | 4 | 3 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Across the 235 herptile RNA-Seq libraries (156 reptile, 79 amphibian) catalogued in Supplementary Table 1, which vertebrate RNA-virus families currently attributed primarily to mammalian or avian hosts (e.g. Lyssavirus within Rhabdoviridae, Orthomyxoviridae, Caliciviridae, Hepeviridae, Astroviridae, Bunyavirales) harbour deeply branching ectothermic lineages whose phylogenetic placement and recombination pattern are consistent with herptiles being long-term ancestral reservoirs rather than recent spillover recipients?
>
> *Rationale:* The candidate precisely targets whether recovered herptile viruses in named mammal/avian-associated families form deeply branching lineages using phylogenetic and recombination evidence, covers all GQ_002 required elements, and is firmly grounded in Supplementary Table 1 and Figures 1–5.

**Rank 2** · Comp = 0.850 · ✅ pass

> Do the alligator-associated rabies lyssavirus and anole lyssa-like virus contigs identified in Supplementary Figure 2 form a monophyletic, deeply branching reptilian Lyssavirus clade sister to the canonical mammalian Lyssavirus radiation, and if so does the implied divergence time predate the mammalian crown rabies clade?
>
> *Rationale:* The candidate specifically tests whether reptile-derived lyssavirus contigs form a deeply branching sister clade to mammalian Lyssavirus and requests phylogenetic dating, directly addressing GQ_002's phylogenetic-novelty intent with concrete data pointers.

**Rank 3** · Comp = 0.510 · ❌ fail

> Is the recombination breakpoint observed between the non-structural and structural gene modules of the novel amphibian/reptile Hepeviridae and Astroviridae contigs in Supplementary Figure 3 a recurrent, conserved feature shared with their mammalian counterparts, indicating that modular recombination is a general macroevolutionary mechanism in vertebrate hepe- and astroviruses?
>
> *Rationale:* The candidate is grounded in supplied supplementary figures/tables and phylogenetic tests but shifts focus from asking whether amphibian/reptile viruses are basal/divergent to testing conserved recombination breakpoints, so it partially matches GQ_002 but omits the basal/divergent element.

**Rank 4** · Comp = 0.850 · ✅ pass

> Does the novel newt calicivirus polyprotein (7,390 nt) reported in Supplementary Figure 5 represent the first member of a previously unrecognised amphibian-specific genus within Caliciviridae, and what is its closest sister mammalian lineage as inferred from the available reference set?
>
> *Rationale:* The candidate is a specific, data-grounded phylogenetic-novelty question about a recovered amphibian calicivirus and its placement within Caliciviridae, matching GQ_002 fully with all required elements present and concrete supplemental-data citations.

**Rank 5** · Comp = 0.820 · ✅ pass

> Is virus detection rate in this 235-library herptile dataset systematically biased by tissue (97 liver vs 38 mixed-viscera vs 20 kidney vs immunological/skin glands) and by poly(A)-selection status (39 of 235 libraries flagged), such that current estimates of herptile virome richness are driven by sampling design rather than true host-virus biology?
>
> *Rationale:* The candidate is a dataset-grounded question about how tissue and poly(A) selection bias detection of herptile viromes, aligning well with GQ_001's intent to use public amphibian/reptile transcriptomes to reveal viral diversity but it omits explicit mention of discovering novel viruses.

### ✅ `gpt-5.5-high` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 2 | 3 | 4 | 3 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 3 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.940 · ✅ pass

> Do public amphibian and reptile RNA-seq datasets contain divergent RNA virus contigs whose phylogenetic placement expands known herptile virus diversity across Bunyavirales, lyssaviruses, Hepeviridae, Astroviridae, orthomyxoviruses, and caliciviruses?
>
> *Rationale:* The candidate closely matches GQ_001 by targeting public herptile RNA-seq mining for novel/divergent RNA viruses with explicit phylogenetic tests; it only omits an explicit mention that these hosts are 'under-sampled.'

**Rank 2** · Comp = 0.595 · ❌ fail

> Do amphibian and reptile astrovirus and hepevirus contigs show discordant non-structural and capsid phylogenies consistent with recombination around the common breakpoint annotated in Supplementary Figure 3?
>
> *Rationale:* The candidate matches GQ_002's phylogenetic analysis of recovered amphibian/reptile viruses and is well-grounded in the supplement, but it asks about recombination-driven discordance rather than whether the viruses occupy basal/divergent positions.

**Rank 3** · Comp = 0.850 · ✅ pass

> Are reptile rhabdovirus nucleoprotein contigs from anole and alligator transcriptomes phylogenetically close enough to recognized lyssaviruses to indicate a broader reptile-associated lyssavirus-like diversity?
>
> *Rationale:* The candidate precisely targets phylogenetic placement of reptile rhabdovirus nucleoprotein contigs (anole, alligator) against lyssaviruses and is explicitly grounded in the supplementary figure/table and SRA metadata, matching GQ_002 fully.

**Rank 4** · Comp = 0.850 · ✅ pass

> Do newt transcriptomes contain deeply divergent influenza PB1 and calicivirus polyprotein sequences that extend the known host range of orthomyxoviruses and caliciviruses into amphibians?
>
> *Rationale:* The candidate precisely targets phylogenetic novelty of amphibian-associated viruses (influenza PB1, calicivirus polyprotein) and is well grounded in the supplied supplementary figures and SRA accession, fully matching GQ_002's intent and required elements.

**Rank 5** · Comp = 1.000 · ✅ pass

> How do host class, tissue type, country of origin, and sequencing platform in Supplementary Table 1 shape the sampling power for discovering novel RNA viruses in public herptile transcriptomes?
>
> *Rationale:* The candidate directly addresses discovery of novel viruses from public amphibian/reptile transcriptomes and is tightly grounded in Supplementary Table 1 metadata (host class, tissue, country, platform), matching the gold question's intent while adding useful sampling-bias detail.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 4 | 5 | 4 | 5 | 4.400 | 0.880 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Does tissue sampling bias in publicly available herptile RNA-seq datasets — specifically the overrepresentation of liver (41% of the 234 SRA accessions in Supplementary Table 1) relative to other tissue types — systematically skew the apparent host-range and tissue-tropism distributions of novel RNA viruses discovered through transcriptome mining of amphibians and reptiles?
>
> *Rationale:* The candidate precisely probes whether liver overrepresentation (41% of 234 SRA accessions in Supplementary Table 1) in public amphibian/reptile RNA-seq biases detection of novel RNA viruses found by transcriptome mining, matching GQ_001's core intent while adding an ascertainment-bias focus.

**Rank 2** · Comp = 0.850 · ✅ pass

> Does the detection of an influenza-like orthomyxovirus (newt influenza virus) in the Japanese fire belly newt Cynops pyrrhogaster (SRR1553357) indicate that orthomyxovirus-like viruses have a deeper evolutionary origin in tetrapods than previously recognized based on bird and mammal sampling, and can the PB1 polymerase phylogeny in Supplementary Figure 4 resolve whether this newt virus represents an ancestral lineage or a host-jump from endothermic vertebrates?
>
> *Rationale:* This candidate directly addresses whether an amphibian-derived orthomyxovirus occupies a basal/divergent position using the PB1 phylogeny from Supplementary Figure 4, matching all required elements for GQ_002 and grounded in the cited supplementary files.

**Rank 3** · Comp = 0.740 · ✅ pass

> Is the co-occurrence of two highly divergent RNA viruses — an influenza-like orthomyxovirus and a calicivirus — within the single Cynops pyrrhogaster mixed-viscera transcriptome (SRR1553357) consistent with chronic multi-virus coinfection in amphibians, and does their simultaneous detection reflect a genuinely elevated per-individual viral burden in salamanders relative to other herptile orders sampled in Supplementary Table 1?
>
> *Rationale:* The candidate aligns with GQ_001 by using public amphibian transcriptomes and reporting novel viruses, but it narrows the scope to single-sample coinfection and comparative burden rather than the broader question of revealing hidden viral diversity in under-sampled hosts.

**Rank 4** · Comp = 0.850 · ✅ pass

> Do the novel reptile Bunyavirales identified through BLAST-based transcriptome mining of the herptile RNA-seq datasets in Supplementary Table 1 occupy distinct phylogenetic positions from bird- and mammal-infecting bunyaviruses in the nucleoprotein gene tree (Supplementary Figure 1), suggesting independent evolutionary radiations of bunyaviruses across vertebrate classes rather than recent cross-class transmission?
>
> *Rationale:* The candidate precisely targets GQ_002 by testing whether novel reptile Bunyavirales are basal/divergent in a nucleoprotein phylogeny using Supplementary Figure 1 and Table 1; it includes all required elements, matches acceptable variants, and is well grounded in the supplementary data.

**Rank 5** · Comp = 0.880 · ✅ pass

> Does the library preparation method — specifically poly(A) selection versus total RNA/ribo-depletion, as annotated by asterisks in Supplementary Table 1 — significantly reduce the detection rate of non-polyadenylated RNA viruses such as the novel reptile Bunyavirales and lyssaviruses in the herptile transcriptome survey?
>
> *Rationale:* The candidate is a focused, well-grounded variant of the public-transcriptome virome discovery question that tests library-prep ascertainment effects on detecting non-polyadenylated novel viruses in herptile RNA-seq data.

### ✅ `gemini-3.1-pro` — Comp=0.140 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> To what extent does the encapsulation of supplementary scientific data within a proprietary binary format like DOCX hinder automated data extraction and FAIR compliance compared to open, machine-readable formats?
>
> *Rationale:* The candidate concerns DOCX supplementary-file machine-readability and FAIR compliance, which does not address the gold question about mining amphibian/reptile RNA-seq for hidden viruses, though it is tangentially related to data-sharing practices.

**Rank 2** · Comp = 0.100 · ❌ fail

> What is the distribution of embedded media types (e.g., images, tables, equations) within the supplementary document, and how does this composition correlate with the overall file size?
>
> *Rationale:* The candidate concerns DOCX internal media composition (file 43705_2022_180_MOESM1_ESM.docx, 2.25 MB) and is unrelated to the RNA-seq virome discovery goals of GQ_001, thus matching no required elements and scoring zero on intent alignment.

**Rank 3** · Comp = 0.060 · ❌ fail

> Can natural language processing techniques successfully identify and extract specific methodological details or experimental parameters from the unstructured text within the supplementary document?
>
> *Rationale:* The candidate addresses NLP extraction from a supplementary DOCX, which does not match the virome-discovery intent of GQ_001; it does, however, concretely references one data file for testing extraction methods.

**Rank 4** · Comp = 0.140 · ❌ fail

> How accurately can the hierarchical structure of the supplementary material (e.g., sections, headings, figure legends) be reconstructed from the underlying XML representation of the DOCX file?
>
> *Rationale:* No semantic match: the candidate concerns DOCX/XML structural parsing, not viral discovery in amphibian/reptile RNA-seq; it has zero overlap with required elements but is well-grounded to the listed DOCX file.

**Rank 5** · Comp = 0.100 · ❌ fail

> What proportion of the supplementary tables contained within the document can be automatically converted into a tidy, machine-readable format without manual data cleaning?
>
> *Rationale:* The candidate concerns DOCX table extraction and tidy-data conversion, which does not match the RNA-seq virome discovery focus of GQ_001; no required elements overlap though the candidate is grounded to a specific supplementary DOCX file.

### ✅ `deepseek-v4-pro` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Does a systematic re-analysis of all tabular data in the supplementary file 43705_2022_180_MOESM1_ESM.docx using distribution-free statistical methods yield effect-size estimates that differ meaningfully from the parametric results reported in the main article?
>
> *Rationale:* The candidate concerns statistical re-analysis of a DOCX supplement, which is unrelated to mining ectotherm RNA-seq for viruses, so it scores zero on match and required-element coverage but is well-grounded to the specific supplement file.

**Rank 2** · Comp = 0.100 · ❌ fail

> Do the supplementary data tables in 43705_2022_180_MOESM1_ESM.docx contain evidence of a dose-response or exposure-response gradient across ordered experimental conditions that was not explicitly modeled in the main article?
>
> *Rationale:* The candidate concerns dose-response trend testing in a supplementary DOCX and is semantically unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viruses, though it is concretely grounded to the provided file.

**Rank 3** · Comp = 0.100 · ❌ fail

> Can stratification of the outcomes reported in the supplementary tables by pre-specified baseline covariates reveal clinically meaningful effect-modification that was not explored in the primary analysis?
>
> *Rationale:* The candidate concerns clinical subgroup stratification in supplementary DOCX tables and is semantically unrelated to virus discovery in amphibian/reptile RNA-seq, though it does reference a specific uploaded DOCX file so it has some data grounding.

**Rank 4** · Comp = 0.100 · ❌ fail

> What is the prevalence and pattern of missing data across the supplementary tables in 43705_2022_180_MOESM1_ESM.docx, and does the missingness pattern suggest informative dropout that could bias the study's primary conclusions?
>
> *Rationale:* The candidate is a missing-data audit for a DOCX supplement and does not address viral discovery or transcriptome mining; thus it fails to match GQ_001, though it is concretely grounded to the provided file.

**Rank 5** · Comp = 0.100 · ❌ fail

> When the effect-size estimates extracted from the supplementary tables in this 2022 study are pooled with prior published estimates via random-effects meta-analysis, does the updated evidence synthesis cross a clinically meaningful decision threshold that the original study alone did not?
>
> *Rationale:* The candidate is a clinical meta-analysis question about pooling effect sizes from a 2022 supplement and crossing decision thresholds, which does not address the virome/transcriptome topics or required elements of GQ_001, though it does reference the provided DOCX file.

### ✅ `glm-5` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What specific experimental datasets and statistical analyses are contained in the supplementary material that could enable independent validation or meta-analysis of the original 2022 research findings?
>
> *Rationale:* The candidate targets supplementary-material contents for reproducibility of a 2022 paper and explicitly cites a specific .docx file, which is unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viruses, so match is nil but data grounding is concrete.

**Rank 2** · Comp = 0.100 · ❌ fail

> Does the supplementary material contain sufficient methodological detail and raw data to reproduce the key findings reported in the associated 2022 research article?
>
> *Rationale:* The candidate is a reproducibility/supplementary-material question unrelated to the viral-transcriptome aims of GQ_001, so I matched it to GQ_001 (primary) as the least-worst fit: match 0, required-elements 0, acceptability 1, data grounding 3.

**Rank 3** · Comp = 0.100 · ❌ fail

> What types of biological, clinical, or experimental variables are documented in the supplementary dataset that could be integrated into cross-study comparative analyses?
>
> *Rationale:* The candidate asks about extracting and harmonizing variables from a named supplementary document for meta-analysis, which does not address amphibian/reptile RNA-seq or viral discovery in GQ_001, so it is unrelated despite concrete data grounding.

**Rank 4** · Comp = 0.100 · ❌ fail

> Are there extended statistical results or sensitivity analyses in the supplementary material that provide additional insights beyond the main publication?
>
> *Rationale:* The candidate concerns supplementary statistical/sensitivity analyses in a provided docx, which is semantically unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viral diversity, though it is grounded to the uploaded supplement file.

**Rank 5** · Comp = 0.100 · ❌ fail

> What is the completeness and quality of data documentation in the supplementary material relative to FAIR data principles?
>
> *Rationale:* The candidate assesses FAIR documentation of a specific supplementary file, which is concrete (one file) but unrelated to mining amphibian/reptile RNA-seq for hidden/novel viruses, so it matches none of GQ_001's required elements.

### ✅ `gemini-2.5-flash` — Comp=0.300 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 0 | 2 | 3 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.300 · ❌ fail

> What specific experimental methods and protocols were utilized in the study associated with this supplementary material?
>
> *Rationale:* The candidate requests methods from a specific supplementary DOCX (concrete grounding) but does not ask about mining public amphibian/reptile RNA-seq or viral diversity, so it poorly matches the gold research question.

**Rank 2** · Comp = 0.100 · ❌ fail

> Does the supplementary material contain raw data or additional statistical analyses that support the main findings of the associated publication?
>
> *Rationale:* The candidate asks about supplementary DOCX content and raw/statistical data, which does not address mining amphibian/reptile RNA-seq for hidden viruses, so it fails to match GQ_001 and contains none of its required elements despite citing a specific file.

**Rank 3** · Comp = 0.100 · ❌ fail

> Are there any additional figures, tables, or appendices in the supplementary document that provide further context or expand upon the results presented in the main paper?
>
> *Rationale:* The candidate asks about supplemental figures/tables in a DOCX and therefore does not engage with GQ_001's scientific intent concerning mining public ectotherm transcriptomes for hidden viruses; it is data-grounded but semantically unrelated.

**Rank 4** · Comp = 0.100 · ❌ fail

> What is the specific research domain or topic addressed by the study, as indicated by the content of this supplementary material?
>
> *Rationale:* The candidate is a generic question about inferring the study's research domain from a DOCX supplement and therefore is semantically unrelated to the virome-mining gold question, yielding zero coverage and low match strength.

**Rank 5** · Comp = 0.100 · ❌ fail

> Are there any specific limitations, caveats, or future research directions discussed within the supplementary material that are not prominently featured in the main publication?
>
> *Rationale:* The candidate inspects a paper's supplement for limitations/future work and does not address mining public ectotherm transcriptomes or viral discovery, so it does not match the gold question about hidden viral diversity in amphibian/reptile RNA-seq.

### ✅ `intern-s1` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What is the correlation between variable X and outcome Y as presented in the supplementary dataset?
>
> *Rationale:* The candidate is a generic correlation query about a supplementary DOCX dataset and does not address any virome/transcriptome/host elements required by the matched gold, so it is unrelated despite referencing the supplemental file.

**Rank 2** · Comp = 0.100 · ❌ fail

> How do the experimental results in the supplementary material compare to the main study's conclusions?
>
> *Rationale:* The candidate is a general supplement-vs-main comparison and does not address public ectotherm transcriptome mining or viral discovery; it is, however, concretely grounded to the provided MOESM docx file.

**Rank 3** · Comp = 0.080 · ❌ fail

> What trends are observed in the time-series data provided in the supplementary tables?
>
> *Rationale:* The candidate is a general time-series trends question about a supplementary docx and does not address any elements of public ectotherm transcriptome mining for hidden viruses, so it is a poor semantic match to GQ_001.

**Rank 4** · Comp = 0.100 · ❌ fail

> Can the supplementary data validate the hypothesis proposed in the main paper?
>
> *Rationale:* The candidate is a generic supplementary-data validation question unrelated to mining amphibian/reptile transcriptomes for viruses, so I matched it to GQ_001 with minimal coverage and low acceptability but noted it does reference the specific supplied docx file.

**Rank 5** · Comp = 0.100 · ❌ fail

> What are the statistical significances of the results reported in the supplementary figures?
>
> *Rationale:* The candidate concerns statistical annotations in a supplementary .docx and does not address public amphibian/reptile RNA-seq or viral discovery; GQ_001 is the least-bad match but intent alignment is poor.

### ✅ `intern-s1-pro` — Comp=0.220 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 2 | 3 | 0.700 | 0.140 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What is the association between baseline biomarker levels and clinical outcomes in the patient cohort described in the supplementary data?
>
> *Rationale:* The candidate is a clinical biomarker/outcomes question about a patient cohort and a supplementary docx, which is semantically unrelated to the gold question about mining ectotherm RNA‑seq for hidden viruses; it references one concrete file but matches no required elements.

**Rank 2** · Comp = 0.100 · ❌ fail

> How do demographic factors correlate with treatment response rates in the dataset provided in the supplementary material?
>
> *Rationale:* The candidate is a clinical-demographic question about treatment response in a supplementary doc, which is unrelated to the gold viromics question, so match and required-element coverage are zero while data grounding is moderate due to the explicit file reference.

**Rank 3** · Comp = 0.100 · ❌ fail

> Can the predictive model described in the supplementary data accurately stratify patients by risk of adverse events?
>
> *Rationale:* The candidate concerns clinical model validation in a supplementary docx and does not address amphibian/reptile RNA-seq, hidden viromes, or transcriptome mining, so it is unrelated to the matched gold question.

**Rank 4** · Comp = 0.220 · ❌ fail

> What are the key differences in gene expression profiles between treatment and control groups in the supplementary dataset?
>
> *Rationale:* The candidate concerns differential-expression analysis in a supplementary dataset and does not address viral discovery in amphibian/reptile transcriptomes; it shares only a broad transcriptomics domain with GQ_001, so the semantic match is weak and required viral-host elements are missing.

**Rank 5** · Comp = 0.140 · ❌ fail

> How does the temporal evolution of disease severity markers correlate with therapeutic intervention timing in the supplementary data?
>
> *Rationale:* The candidate concerns longitudinal clinical marker dynamics and treatment timing in a supplement, which does not match the gold's transcriptome-mining-for-viruses intent; it is grounded to one explicit file but lacks any amphibian/reptile or viral elements.

### ✅ `intern-s1-mini` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> How does the experimental condition represented by '43705' correlate with the measured outcome variable in the 2022 dataset?
>
> *Rationale:* The candidate is a dataset-specific correlation question tied to a DOCX file identifier and lacks any amphibian/reptile, RNA-seq, or virology elements, so it does not match the virome-mining gold question.

**Rank 2** · Comp = 0.080 · ❌ fail

> What seasonal patterns emerge in the 2022 dataset related to the MOESM1_ESM supplementary variables?
>
> *Rationale:* The candidate concerns seasonal patterns in a MOESM1_ESM supplement (2022) and does not address public amphibian/reptile RNA-seq, hidden viruses, or transcriptome mining, so it is semantically unrelated to GQ_001 with only a single-file reference as grounding.

**Rank 3** · Comp = 0.100 · ❌ fail

> How do the supplementary variables in MOESM1_ESM differ between experimental groups identified by '43705'?
>
> *Rationale:* The candidate is a dataset-specific subgroup comparison of a supplementary DOCX and does not address mining public amphibian/reptile RNA-seq or viral discovery, so GQ_001 was chosen as the least-worst match but alignment is absent.

**Rank 4** · Comp = 0.060 · ❌ fail

> What is the relationship between the dataset's size (2.25MB) and the completeness of experimental metadata in MOESM1_ESM?
>
> *Rationale:* The candidate addresses metadata completeness and file size for a single supplementary docx, which does not engage the gold question's viral-mining intent but does reference a concrete file and size.

**Rank 5** · Comp = 0.100 · ❌ fail

> How does the supplementary nature of MOESM1_ESM affect the statistical power of analyses conducted on the 2022 dataset?
>
> *Rationale:* The candidate concerns how a supplementary file (MOESM1_ESM) affects statistical power, which is unrelated to the gold question about mining ectotherm RNA-seq for hidden viral diversity, though it does concretely reference a provided file.

### ✅ `intern-s2-preview` — Comp=0.180 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.180 · ❌ fail

> What types of data (tables, figures, raw datasets, or methodological details) are most commonly contained in supplementary material documents from 2022 biomedical publications, and how does this correlate with the document size?
>
> *Rationale:* The candidate addresses supplementary .docx content and file size (specific 2.25 MB file) which is unrelated to amphibian/reptile RNA-seq virome discovery, so it is a poor semantic match to GQ_001 despite concrete file grounding.

**Rank 2** · Comp = 0.100 · ❌ fail

> Is there a relationship between the size of supplementary material documents and the complexity or volume of supporting data presented in published research articles?
>
> *Rationale:* The candidate addresses supplementary-file size vs. data complexity (concrete file and byte count) which does not match GQ_001's focus on mining amphibian/reptile RNA-seq for novel viruses, so match strength and required-element coverage are zero while data grounding is moderate.

**Rank 3** · Comp = 0.120 · ❌ fail

> What naming conventions and structural patterns are used for supplementary materials in scientific publications, and do they indicate content type or sequence?
>
> *Rationale:* The candidate is about supplement file-naming (e.g., '43705_2022_180_MOESM1_ESM.docx') and thus has no semantic overlap with the RNA-seq virome-mining gold question; it is, however, strongly grounded to specific file names.

**Rank 4** · Comp = 0.100 · ❌ fail

> How does the format of supplementary materials (e.g., .docx vs. .xlsx vs. .pdf) vary across scientific disciplines, and what implications does this have for data accessibility and reproducibility?
>
> *Rationale:* The candidate concerns supplementary file formats and reproducibility, which is semantically unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viruses; it is grounded in a specific .docx file but covers none of the gold's required virology elements.

**Rank 5** · Comp = 0.100 · ❌ fail

> What is the typical size distribution of supplementary materials in scientific publications, and how does this relate to journal policies on data sharing?
>
> *Rationale:* The candidate is about supplementary file sizes and journal data-sharing policies and thus is semantically unrelated to the gold virome question (GQ_001); it mentions one concrete file size but contains none of the gold's required virology elements.


## 2 · `arthropod_neg_sense_2015`

- **raw**：2 文件: `elife-05378-supp-v1.zip, nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 3 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 4 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Does the polymerase (L-gene) phylogeny of the 170 arthropod-derived negative-sense RNA viruses in the KM817593–KM817764 collection reveal host-class-structured clades (tick-, mosquito-, fly-, and spider-borne) that root the deep ancestry of vertebrate-infecting Bunyavirales and Mononegavirales, and do glycoprotein-vs-polymerase tree incongruences pinpoint specific candidate modular-recombination events along that backbone?
>
> *Rationale:* The candidate directly targets arthropod-derived negative-sense viruses and the L/RdRP phylogeny to relate segmented (Bunyavirales) and non-segmented (Mononegavirales) groups, adds glycoprotein-vs-polymerase incongruence analysis, and cites specific records/files, meeting all GQ_002 requirements.

**Rank 2** · Comp = 0.697 · ✅ pass

> Across the 14 hematophagous-tick strains and the 25 mosquito-borne strains in this collection, can polymerase-based phylogenetic placement and shared genome architecture (presence of N, G, M, L modules) distinguish strictly arthropod-restricted lineages from those sister to known vertebrate-pathogenic Bunyavirales such as Phenuiviridae and Nairoviridae?
>
> *Rationale:* Matches GQ_002 well via L-gene phylogenetic placement and genome-module comparison for arthropod-derived Bunyavirales, with strong accession-level grounding; missing explicit mention of non-segmented groups required by GQ_002.

**Rank 3** · Comp = 0.940 · ✅ pass

> Do the 14 PB1-gene records in this dataset (Jingshan Fly Virus 1, Wuhan Mosquito Virus 3–7, Wuhan Louse Fly Virus 3/4, etc.) form a monophyletic insect-associated sister clade to Orthomyxoviridae that supports an arthropod origin for segmented negative-sense RNA viruses with PB1 polymerases?
>
> *Rationale:* The candidate precisely targets arthropod-associated PB1 sequences to test for a basal, segmented lineage sister to Orthomyxoviridae, so it aligns strongly with GQ_001 though it references PB1 records rather than explicitly 'arthropod RNA-seq'.

**Rank 4** · Comp = 0.323 · ❌ fail

> Does the geographic sampling structure encoded in strain names (Wuhan, Tacheng, Wenzhou, Bole, Sanxia, Shuangao, Changping and others) show a latitudinal or biome-correlated stratification of viral families, such that temperate-Xinjiang collection sites preferentially harbour tick-borne phenui-/nairo-like clades while subtropical central-China sites are enriched for fly- and mosquito-associated rhabdo-/orthomyxo-like clades?
>
> *Rationale:* Matches GQ_002 only weakly: candidate deals with geographic stratification of arthropod-associated negative-sense clades (well grounded with locality counts) but omits the phylogenetic/segmentation focus (RdRP tree, bridging groups) central to GQ_002.

**Rank 5** · Comp = 0.580 · ❌ fail

> Do the multi-segment entries explicitly labelled "segment 1" and "segment 2" for Lishi Spider Virus 1, Wenzhou Crab Virus 2, Wuchang Cockroach Virus 3, and Wuhan Louse Fly Virus 6/7 exhibit segment-specific GC-content or codon-usage signatures that diverge from their host arthropods, indicating long-term virus-specific compositional evolution rather than recent host capture?
>
> *Rationale:* The candidate aligns with the gold's interest in segmentation and ancestry but is narrower (compositional analysis of named segments) and omits explicit negative-sense/ RNA-seq/basal-lineage scope, while being tightly grounded in specific accession records.

### ✅ `gpt-5.5-high` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 4 | 5 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Do the reported invertebrate-associated RNA virus polymerase sequences occupy phylogenetic positions that bridge established vertebrate, plant, and arthropod virus lineages across orthomyxo-like, bunya-like, rhabdo-like, nyami-, borna-, and chuvirus groups?
>
> *Rationale:* The candidate directly asks whether invertebrate RdRp/PB1 sequences occupy intermediate phylogenetic positions among named negative-sense virus groups, matching GQ_002's focus on bridging phylogenetic gaps and using concrete FASTA/figure evidence.

**Rank 2** · Comp = 0.544 · ❌ fail

> Are tick-, mosquito-, and fly-associated viruses enriched for distinct polymerase clades or genome organizations in the reported viral sequence collection?
>
> *Rationale:* Matched to GQ_002 because it addresses RdRP clades and genome organization across arthropod hosts; strong data grounding and partial coverage of segmentation/RdRP elements, but it omits explicit negative-sense framing, 'newly assembled' sequences, and the phylogenetic-gap bridging intent.

**Rank 3** · Comp = 0.527 · ❌ fail

> Do the segmented virus records in the dataset show consistent multi-segment recovery across the same virus strains, suggesting complete or near-complete genome assemblies for newly reported invertebrate RNA viruses?
>
> *Rationale:* The candidate aligns with GQ_002's segmentation focus and is strongly grounded in the FASTA file and named segments/strains, but it lacks explicit negative-sense/phylogenetic framing and RdRP-tree analysis required by the gold question.

**Rank 4** · Comp = 0.480 · ❌ fail

> How much novel viral diversity is represented by the 113 distinct invertebrate-associated virus names relative to the 170 reported nucleotide records and their reference placements in the supplementary phylogenies?
>
> *Rationale:* The candidate is a data-grounded question about novel virus diversity and phylogenetic placements (good grounding) but it does not target negative-sense viruses, basal lineages, or genome architecture required by GQ_001, so semantic match is partial.

**Rank 5** · Comp = 0.580 · ❌ fail

> Are glycoprotein and nucleocapsid genes recovered in the same host-associated virus groups as polymerase genes, supporting complete structural and replication module characterization across the invertebrate virome?
>
> *Rationale:* The candidate well addresses genome-module co-occurrence in arthropod-associated sequences with concrete FASTA counts and hosts, but it omits explicit reference to negative-sense viruses, basal clades, and phylogenetic ancestry required by the gold question.

### ✅ `claude-code-sonnet-4-6` — Comp=0.860 · Pass@1=0.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 3 | 5 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 5 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.374 · ❌ fail

> Do tick-associated invertebrate RNA viruses in the KM817593–KM817764 accession set exhibit significantly elevated RdRp GC content and distinct codon usage relative to viruses from other arthropod hosts (mosquitoes, flies, spiders), and do these host-class-specific nucleotide composition signatures predict host-range restriction or vertebrate zoonotic potential?
>
> *Rationale:* The candidate is well grounded in accession-level data and asks about composition and host-range prediction, but it does not address segmentation, phylogenetic bridging, or constructing an RdRp/L-protein phylogeny central to GQ_002.

**Rank 2** · Comp = 0.544 · ❌ fail

> Among the novel RNA viruses in the KM817593–KM817764 dataset, does the glycoprotein (G) gene phylogeny of rhabdovirus-like invertebrate viruses recapitulate host-arthropod phylogeny (co-divergence), or does discordance between G-gene and RdRp trees indicate past cross-host-order transmission events in Chinese arthropod populations?
>
> *Rationale:* The candidate focuses on phylogenetic congruence between G and RdRp in novel arthropod negative-sense viruses (well-grounded in KM sequences), aligning partially with GQ_002's phylogenetic intent but omitting segmentation and explicit gap-bridging elements.

**Rank 3** · Comp = 0.820 · ✅ pass

> Do the multi-ORF genome architectures observed in tick-associated viruses from the KM817593–KM817764 dataset (e.g., Tacheng Tick Virus 7 with ORF1–ORF4 plus G and L) represent evolutionarily independent acquisitions of accessory genes, and are these extra ORFs homologous to proteins in known vertebrate-infecting negative-sense RNA viruses?
>
> *Rationale:* The candidate well matches GQ_001 by interrogating arthropod-derived negative-sense virus genome architectures and evolutionary origin (with concrete accessions and ORF data), but it omits explicit discussion of 'basal lineages.'

**Rank 4** · Comp = 0.520 · ❌ fail

> Among the bisegmented RNA viruses in the KM817593–KM817764 dataset (Lishi Spider Virus 1, Wenzhou Crab Virus 2, Wuchang Cockroach Virus 3, Wuhan Louse Fly Viruses 6 and 7), are the two genomic segments more similar in GC composition and length to each other than to corresponding segments of other bisegmented invertebrate RNA viruses, consistent with stable co-packaging or recent segment reassortment?
>
> *Rationale:* The candidate well targets segmentation/genome-architecture questions using specific arthropod virus accessions, but it neglects the gold's emphasis on negative-sense viruses and ancestral/phylogenetic inference, so it is a partial match focused on reassortment/compositional analysis.

**Rank 5** · Comp = 0.860 · ✅ pass

> Do the orthomyxovirus-like invertebrate RNA viruses in the KM817593–KM817764 dataset — identified by the presence of PB1-homolog polymerase subunit genes in mosquitoes, flies, spiders, water striders, and cockroaches — form a monophyletic clade with influenza-like vertebrate orthomyxoviruses, and does their RdRp sequence diversity suggest an invertebrate origin for the vertebrate Orthomyxoviridae?
>
> *Rationale:* The candidate is a strong, data-grounded phylogenetic question about arthropod-derived orthomyxovirus PB1 sequences and vertebrate origins, matching the gold intent except for not addressing genome segmentation/architecture.

### ✅ `gemini-3.1-pro` — Comp=0.493 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.420 · ❌ fail

> What are the specific genomic signatures and phylogenetic relationships that differentiate the tick-associated viruses (e.g., Bole Tick Virus 3, Changping Tick Virus) from the spider-associated viruses (e.g., Lishi Spider Virus 1) within the provided FASTA dataset, and how do these differences reflect viral adaptation to distinct arthropod host lineages?
>
> *Rationale:* The candidate is a host-focused phylogenetic comparison grounded in a named FASTA file (high data grounding) but misses core GQ_001 requirements about negative-sense viruses, RNA-seq source, basal lineages, and genome architecture, so overall semantic match is weak.

**Rank 2** · Comp = 0.374 · ❌ fail

> How does the codon usage bias differ between the unsegmented tick viruses (e.g., Bole Tick Virus 3) and the segmented spider viruses (e.g., Lishi Spider Virus 1) present in the FASTA dataset?
>
> *Rationale:* The candidate is data-grounded and compares segmented vs unsegmented arthropod viruses but asks about codon usage (host adaptation) rather than the phylogenetic bridging and RdRP/tree-focused intent of GQ_002.

**Rank 3** · Comp = 0.240 · ❌ fail

> Are there conserved RNA secondary structure motifs within the untranslated regions (UTRs) of the Changping Tick Viruses (strains CP1-3 and CP1-4) that suggest common regulatory mechanisms?
>
> *Rationale:* The candidate is a specific structural/UTR analysis of named tick virus strains with strong file-level grounding, but it does not address the gold's phylogenetic, RNA-seq, or negative-sense virus ancestry aims.

**Rank 4** · Comp = 0.493 · ❌ fail

> What is the degree of nucleotide sequence conservation between the two segments of the Lishi Spider Virus 1 (strain LSZZ11) compared to the conservation observed among the unsegmented tick viruses in the dataset?
>
> *Rationale:* The candidate targets segmented vs unsegmented arthropod viruses using named FASTA entries, matching GQ_002's segmentation theme but omitting explicit negative-sense, phylogenetic-gap, and RdRP tree elements required for full alignment.

**Rank 5** · Comp = 0.380 · ❌ fail

> Can the open reading frames (ORFs) predicted from the Bole Tick Virus 3 and Changping Tick Virus genomes in the FASTA file be used to identify novel, uncharacterized viral proteins unique to tick-borne viruses?
>
> *Rationale:* The candidate is a concrete ORF/homology question about two tick virus genomes in a FASTA file and is grounded in specific sequences, but it does not address the gold's core evolutionary aims (RNA-seq sampling, basal clades, phylogenetic ancestry).

### ✅ `deepseek-v4-pro` — Comp=0.493 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.476 · ❌ fail

> Do the RNA-dependent RNA polymerase (RdRp/L) phylogenies of the ~150 novel arthropod viruses in nuccore_reported_viral_sequences.fasta recapitulate host taxonomic order (ticks, spiders, mosquitoes, flies, cockroaches, lacewings, crabs, water striders), indicating long-term virus–host co-divergence rather than frequent cross-order host switching?
>
> *Rationale:* Maps best to GQ_002 because it uses RdRP/L trees of novel arthropod viruses, but it shifts intent to host–virus co-divergence rather than segmentation/phylogenetic-gap bridging; two of five required elements present and dataset files are explicitly cited.

**Rank 2** · Comp = 0.493 · ❌ fail

> Do arthropod RNA viruses with segmented genomes (e.g., bunyavirus-like and reovirus-like sequences in nuccore_reported_viral_sequences.fasta) show stronger evidence of reassortment among co-infecting lineages than their non-segmented counterparts, as inferred from topological incongruence across segment trees?
>
> *Rationale:* Matches GQ_002 on segmentation and arthropod viruses but focuses on reassortment/topological incongruence rather than demonstrating phylogenetic bridging or using RdRP/L-protein trees; well grounded in specific fasta records.

**Rank 3** · Comp = 0.320 · ❌ fail

> Is there a significant association between the nucleotide composition (GC content and dinucleotide bias, especially CpG) of these arthropod RNA virus genomes and the taxonomic class of their host, reflecting host-specific innate immune pressures such as zinc-finger antiviral protein (ZAP) or Toll-like receptor recognition?
>
> *Rationale:* The candidate is a well-grounded, data-specific nucleotide-composition/host-immunity question about arthropod viruses but does not address the gold question's core phylogenetic or genome-architecture aims, so it weakly matches GQ_001.

**Rank 4** · Comp = 0.300 · ❌ fail

> Does the geographic distance between sampling locations (encoded in strain identifiers across nuccore_reported_viral_sequences.fasta) explain more variance in viral RdRp sequence divergence than host taxonomic distance, suggesting that spatial isolation dominates over host specialisation in shaping arthropod RNA virus diversity?
>
> *Rationale:* The candidate studies spatial vs host drivers of RdRp divergence in arthropod viruses (phylogeography), which is related to viral evolution but does not address basal negative-sense lineages or genome/segmentation questions central to GQ_001.

**Rank 5** · Comp = 0.400 · ❌ fail

> Can the presence of putative glycoprotein (G) gene sequences in the nuccore_reported_viral_sequences.fasta data predict host range breadth—defined as the number of arthropod orders from which related viruses have been isolated—by revealing structural features associated with receptor promiscuity versus specialisation?
>
> *Rationale:* Candidate is grounded in real files and specific accessions (high data grounding) but asks a different molecular host-range question rather than the gold's phylogenetic/genome-architecture focus, missing all required elements.

### ✅ `glm-5` — Comp=0.740 · Pass@1=1.00 · Pass@5=0.40

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 2 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 3 | 2 | 0 | 2 | 4 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 5 | 4 | 3 | 4 | 4 | 3.700 | 0.740 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.646 · ✅ pass

> What phylogenetic relationships exist among these newly discovered arthropod-associated viruses, and do they cluster by host type, geographic location, or viral genome architecture?
>
> *Rationale:* The candidate closely matches GQ_002 by asking phylogenetic relationships and clustering by genome architecture in newly discovered arthropod viruses, is well-grounded in the provided FASTA/supplement, but omits explicit 'negative-sense' and RdRP/L-protein tree specifics required by GQ_002.

**Rank 2** · Comp = 0.460 · ❌ fail

> Do the segmented genome viruses (Lishi Spider Virus, Wenzhou Crab Virus, Wuchang Cockroach Virus, Wuhan Louse Fly Virus) share conserved sequence motifs or structural features across their segments?
>
> *Rationale:* Matches GQ_001 on segmentation/genome-architecture focus (explicit segmented viruses and segment accessions) but lacks the gold's emphasis on arthropod RNA-seq, negative-sense designation, and phylogenetic/ancestral questions.

**Rank 3** · Comp = 0.272 · ❌ fail

> What is the genetic diversity and evolutionary distance between tick-associated viruses (Bole Tick Virus, Changping Tick Virus, Tacheng Tick Virus, Wuhan Tick Virus) compared to other arthropod host groups?
>
> *Rationale:* The question is a comparative phylogenetic/diversity query about tick viruses (well grounded in provided fasta accessions) but it omits the GQ_002 focus on segmentation, negative-sense viruses, and RdRP/L-protein phylogenetic bridging, so alignment is weak despite good data grounding.

**Rank 4** · Comp = 0.306 · ❌ fail

> Are there geographic patterns in virus distribution, with certain virus types or genome architectures associated with specific Chinese regions (Wuhan, Wenzhou, Tacheng, Bole, Changping)?
>
> *Rationale:* The candidate focuses on geographic clustering of virus 'genome architectures' (grounded in nuccore headers), which loosely overlaps GQ_002's architecture/segmentation theme but omits the essential arthropod, negative-sense, and RdRP phylogenetic elements required by the gold question.

**Rank 5** · Comp = 0.740 · ✅ pass

> What gene annotations and functional domains are present in the multi-gene sequences (Shayang Fly Virus, Wenzhou Crab Virus 3) and how do they compare to known negative-sense RNA virus gene organizations?
>
> *Rationale:* Aligns with GQ_001's genome-architecture goal by analyzing gene/domain organization in arthropod negative-sense virus sequences, but it lacks explicit focus on basal lineages and phylogenetic ancestry; well grounded to nuccore fasta and accessioned sequences.

### ✅ `gemini-2.5-flash` — Comp=0.360 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 4 | 0.850 | 0.170 | ❌ | GQ_002 (S) |
| 4 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.360 · ❌ fail

> What are the phylogenetic relationships among the different tick-borne viruses present in the dataset, and how do they compare to other reported viral sequences?
>
> *Rationale:* The candidate targets phylogenetic comparison of tick-borne sequences (well grounded in a fasta file) but misses the gold's focus on negative-sense viruses, basal lineages, and genome/segmentation architecture.

**Rank 2** · Comp = 0.220 · ❌ fail

> Can conserved genomic regions or specific genes be identified across different viral strains or types within the dataset, particularly those associated with pathogenicity or host interaction?
>
> *Rationale:* The candidate is about conserved genes across viral strains (data-grounded in a FASTA), which does not address the arthropod/negative-sense phylogenetic and genome-architecture focus of GQ_001; it therefore poorly matches that gold question.

**Rank 3** · Comp = 0.170 · ❌ fail

> What is the genetic diversity of specific viral species (e.g., 'Bole Tick Virus' or 'Wuchang Cockroach Virus') represented by multiple strains in the dataset?
>
> *Rationale:* The candidate focuses on within-species genetic diversity of named virus strains in a nuccore fasta (well grounded), which does not address GQ_002's phylogenetic/segmentation transition intent or required elements.

**Rank 4** · Comp = 0.220 · ❌ fail

> Are there any novel or uncharacterized viral sequences in the dataset that do not closely match known viral families or species?
>
> *Rationale:* The candidate is a general viral‑discovery question grounded in nuccore_reported_viral_sequences.fasta but omits all GQ_001 specifics (arthropod RNA‑seq, negative‑sense viruses, basal lineages, segmentation, phylogenetic analysis), so it poorly matches the gold intent.

**Rank 5** · Comp = 0.220 · ❌ fail

> What is the overall genomic composition (e.g., GC content, codon usage bias) of the viral sequences in the dataset, and does it vary significantly between different viral groups or hosts?
>
> *Rationale:* The candidate focuses on sequence composition (GC/codon usage) across viral groups/hosts using nuccore_reported_viral_sequences.fasta, but GQ_001 targets arthropod RNA-seq recovery of basal negative-sense virus clades and genome/segmentation-based phylogenetic ancestry, so intent and required elements do not align.

### ✅ `intern-s1` — Comp=0.300 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Can we identify geographical patterns in viral strain distribution using sequence metadata?
>
> *Rationale:* The candidate investigates geographic distribution using FASTA headers and a supplementary ZIP, which is data-grounded but unrelated to GQ_001's arthropod/phylogenetic/architecture focus, so it scores zero for semantic match and misses all required elements.

**Rank 2** · Comp = 0.300 · ❌ fail

> How does sequence diversity correlate with host species distribution?
>
> *Rationale:* The candidate addresses host–sequence diversity using specific files but misses the gold's focus on negative-sense viruses, basal lineages, segmentation and phylogenetic ancestry, so semantic alignment is weak despite concrete data grounding.

**Rank 3** · Comp = 0.120 · ❌ fail

> Can we detect temporal trends in viral genome sequencing efforts?
>
> *Rationale:* The candidate is about temporal trends in sequencing (accession dates) and cites specific files, but it does not address arthropod RNA-seq, negative-sense viruses, basal lineages, genome architecture, or phylogenetic ancestry required by the matched gold question.

**Rank 4** · Comp = 0.300 · ❌ fail

> What is the relationship between viral genome size and host range?
>
> *Rationale:* The candidate addresses a different scientific question (genome size vs host range) with only a loose overlap with 'genome architecture'; it is grounded in the provided FASTA and supplementary ZIP but omits key gold elements (arthropod RNA-seq, negative-sense viruses, phylogeny).

**Rank 5** · Comp = 0.220 · ❌ fail

> Can we identify conserved genomic regions across related viral strains?
>
> *Rationale:* The candidate is a generic conserved-region question about viral strains and a FASTA file, which does not address the gold's specific focus on arthropod-derived negative-sense viruses, basal lineages, or segmentation/phylogeny.

### ✅ `intern-s1-pro` — Comp=0.360 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 3 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.340 · ❌ fail

> What is the evolutionary relationship and potential for cross-species transmission among the diverse arthropod-borne viruses in this dataset, particularly those sharing geographic origins in China?
>
> *Rationale:* Candidate concerns arthropod viral evolution but is broader than GQ_001 (lacks focus on negative-sense viruses, RNA-seq, basal clades, and genome architecture); it is data-grounded and scientifically acceptable though not a close match.

**Rank 2** · Comp = 0.220 · ❌ fail

> What are the geographic distribution patterns and emergence timelines of these arthropod-borne viruses, and do they correlate with environmental or ecological factors?
>
> *Rationale:* Selected GQ_001 because both mention arthropod-associated viruses, but the candidate is epidemiological (geography/timing) not phylogenetic/genomic, so match is weak though data grounding is concrete (nuccore FASTA).

**Rank 3** · Comp = 0.360 · ❌ fail

> How do genetic variations in glycoprotein and nucleocapsid genes correlate with vector specificity and host range among these arthropod-borne viruses?
>
> *Rationale:* The candidate studies arthropod-associated viral gene variation (well grounded to a fasta file) but does not address negative-sense virus ancestry, basal clades, segmentation, or phylogenetic reconstruction required by the matched gold question.

**Rank 4** · Comp = 0.220 · ❌ fail

> What is the genetic diversity and evidence of recombination among these arthropod-borne viruses, and how does it impact viral evolution and adaptation?
>
> *Rationale:* The candidate focuses on intra-species diversity and recombination in arthropod-associated viruses and cites a specific fasta file, but it does not address negative-sense virus ancestry, basal clades, segmentation, or genome architecture required by GQ_001.

**Rank 5** · Comp = 0.220 · ❌ fail

> Can conserved regions across these viral genomes be used to develop broad-spectrum diagnostic assays for arthropod-borne viruses?
>
> *Rationale:* The candidate is an applied diagnostics question grounded in nuccore_reported_viral_sequences.fasta and does not address the evolutionary/phylogenetic requirements of GQ_001, so it has low semantic match and covers none of the gold's required elements.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 3 | 3 | 4 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 4 | 5 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 1 | 2 | 2 | 5 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 2 | 4 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 5 | 1.360 | 0.272 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.459 · ❌ fail

> What is the degree of phylogenetic congruence between arthropod hosts and their infecting viruses in this dataset, and does host taxonomic grouping predict viral genetic divergence more strongly than viral genome segmentation status?
>
> *Rationale:* The candidate is grounded in the provided FASTA and segmentation status but centers on host–virus congruence rather than testing whether arthropod viruses bridge phylogenetic gaps among negative-sense segmented vs non-segmented groups.

**Rank 2** · Comp = 0.560 · ❌ fail

> Do segmented viruses in this dataset show evidence of reassortment through incongruent phylogenetic signals between different genome segments?
>
> *Rationale:* The candidate is strongly data-grounded and addresses segmentation via segment-specific phylogenies (reassortment), but it lacks the GQ_001 emphasis on arthropod RNA-seq, negative-sense virus ancestry, and basal clade discovery.

**Rank 3** · Comp = 0.323 · ❌ fail

> What is the nucleotide composition bias (GC content) across these viral genomes, and does it correlate with host taxonomic group or genome segmentation status?
>
> *Rationale:* The candidate is well grounded in the provided FASTA and specific host labels but asks a compositional (GC content) question rather than the phylogenetic/segmentation-transition question GQ_002 targets, so semantic match is weak despite good data grounding.

**Rank 4** · Comp = 0.520 · ❌ fail

> Are there conserved functional protein domains (such as polymerase, nucleoprotein, or glycoprotein regions) identifiable across the annotated viral sequences, and what is their evolutionary conservation level?
>
> *Rationale:* The candidate focuses on conserved protein domains in annotated viral sequences (mentions specific accessions), which relates to molecular features of negative-sense viruses but omits the gold question's emphasis on arthropod RNA-seq, basal lineages, and genome segmentation.

**Rank 5** · Comp = 0.272 · ❌ fail

> What is the frequency and distribution of IUPAC ambiguity codes across these viral sequences, and do they cluster in specific genomic regions suggesting sequencing uncertainty or genuine biological variation?
>
> *Rationale:* The candidate is a sequence-quality question about IUPAC ambiguity codes in a specific FASTA (nuccore_reported_viral_sequences.fasta) and only overlaps the gold question on the single point of segmented vs non-segmented groups, so it is semantically distant from the phylogenetic/ancestry focus.


## 3 · `bat_btcn_virome_2024`

- **raw**：4 文件: `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz, 43059586_RdRp_motif_collection.xlsx, 45561465_Meta_data_for_ecological_modeling.zip, 48306316_ML_Phylo.zip`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.920 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 5 | 5 | 5 | 4.600 | 0.920 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 4 | 0 | 0 | 2 | 5 | 0.765 | 0.153 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Which combinations of climate variables (tas10, pr10, vpd10, hurs10) and land-use covariates (cy, sy, bx, btsm) most strongly predict the abundance and lineage diversity of zoonotic-prone RNA virus orders (Coronaviridae, Bunyavirales, Picornavirales) in intestinal versus pulmonary samples across the five Chinese bat families (Hipposideridae, Vespertilionidae, Rhinolophidae, Pteropodidae, Emballonuridae) profiled in the BtCN-Virome dataset?
>
> *Rationale:* The candidate precisely targets which environmental and land-use covariates predict RNA-virus richness and composition across bat families using BtCN-Virome data and explicit modeling, aligning closely with GQ_002.

**Rank 2** · Comp = 0.920 · ✅ pass

> Do bat species in the Rhinolophidae and Hipposideridae families harbour Coronaviridae lineages whose RdRp phylogenetic distance to SARS-CoV-2 (A0A6G7SLW8_SAR5) declines with increasing cropland (cy) or human-modified land-use (sy, bx) within their sampling pools?
>
> *Rationale:* The candidate is a specific, data-grounded test of ecological drivers (land-use) affecting bat coronavirus relatedness to SARS-CoV-2, matching GQ_001's core aim to link bat viromes to ecology and human exposure; it narrows scope to Coronaviridae and two bat families but retains required elements and clear data references.

**Rank 3** · Comp = 0.731 · ✅ pass

> Does intestinal viral richness (tv) in Chinese bats reflect detectable signatures of arthropod, mollusc, or plant diet (recoverable from Arthropoda_COI_CYTB.99.fna, Mollusca_COI_CYTB.99.fna, and Streptophyta_ITS.99.fna) such that dietary breadth predicts the diversity of Picornavirales and Hepelivirales contigs?
>
> *Rationale:* The candidate narrowly tests dietary covariates predicting intestinal RNA-virus richness using specific files and analyses, matching GQ_002's intent on covariates and statistical modeling, but it does not include an explicit geographic covariate requirement.

**Rank 4** · Comp = 0.153 · ❌ fail

> Are conserved RdRp catalytic motifs (motifs A, B, C in the 43059586_RdRp_motif_collection.xlsx) sufficient to assign novel BtCN-Virome contigs to the correct virus order with accuracy comparable to placement on the 13 IQ-TREE order-level phylogenies, and which motif combinations fail for the most divergent bat-derived lineages?
>
> *Rationale:* This is a methodological benchmarking question about RdRp motif vs phylogenetic placement, not an ecological-covariate or richness question, so it matches no required elements of GQ_002 but is strongly grounded in the named files.

**Rank 5** · Comp = 0.680 · ✅ pass

> Across the five surveyed bat families, do tissue-specific virome compositions (Br, In, Ki, Li, Lu in total.txt) form discrete tropism clusters, and is the brain (Br) tissue an under-recognised reservoir for Mononegavirales and Bunyavirales lineages in the BtCN-Virome RdRp phylogenies?
>
> *Rationale:* The candidate strongly targets organ-level virome composition with concrete file/sequence evidence, aligning with GQ_001's organ/metatranscriptome focus but missing ecological drivers and human-settlement circulation elements.

### ✅ `gpt-5.5-high` — Comp=0.799 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 2 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 4 | 4 | 4 | 5 | 4 | 3.570 | 0.714 | ✅ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.731 · ✅ pass

> Which host-family, tissue, climate, and landscape factors explain variation in viral richness and RdRp phylogenetic novelty across BtCN bat pools?
>
> *Rationale:* Matches the secondary ecological-modeling question: specifies host and environmental covariates, richness and phylogenetic novelty, and references modeling and concrete files; missing an explicit 'geography' mention.

**Rank 2** · Comp = 0.799 · ✅ pass

> Do intestine and lung bat samples show different ecological predictors of viral richness across the BtCN metadata and virome assemblies?
>
> *Rationale:* The candidate is a clear, dataset-grounded instance of GQ_002—it targets which covariates explain viral richness using statistical models, adds tissue stratification, and cites specific metadata and features, but does not explicitly mention geographic covariates.

**Rank 3** · Comp = 0.340 · ❌ fail

> Which RNA virus orders or families in the BtCN RdRp phylogenies contain the greatest concentration of divergent bat-associated lineages relative to ZOVER-bat and reference sequences?
>
> *Rationale:* The candidate is a phylogeny-focused question identifying where BtCN adds evolutionary novelty across viral orders; it does not ask about host/dietary/environmental/geographic covariates or statistical modeling demanded by GQ_002, but is tightly grounded in ML_Phylo files and sequence counts.

**Rank 4** · Comp = 0.714 · ✅ pass

> Can host diet markers from arthropod, mollusk, and plant reference databases explain differences in bat virome richness among host families and sample pools?
>
> *Rationale:* The candidate targets dietary covariates and virome richness with explicit data links and a testing plan, aligning well with GQ_002 (dietary predictors of viral richness) though it omits geographic covariates.

**Rank 5** · Comp = 0.320 · ❌ fail

> Are conserved RdRp motif patterns associated with viral group placement and phylogenetic diversity in the BtCN maximum-likelihood trees?
>
> *Rationale:* The candidate is a well-grounded molecular phylogenetics question about RdRp motifs and ML trees that shares RNA-virus diversity and BtCN data with GQ_001 but omits the ecological, host, and human-settlement elements central to that gold question.

### ✅ `claude-code-sonnet-4-6` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.60

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 4 | 2 | 3 | 2 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 5 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Does bat family identity (Rhinolophidae, Vespertilionidae, Hipposideridae, Pteropodidae, or Emballonuridae) predict intestinal RNA virus diversity (tv) in Chinese bat pools independently of local climate variables (tas10, pr10, vpd10) and land-use variables (nt, cy, gm)?
>
> *Rationale:* The candidate fully matches GQ_002 by specifying host family, environmental and land-use covariates, Chinese geography, an explicit viral richness metric (tv), and a clear statistical approach, all grounded in named files/columns.

**Rank 2** · Comp = 0.580 · ❌ fail

> Across the 13 RNA virus orders in the BtCN-Virome RdRp phylogenies, which orders (Picornavirales, Permutotetravirales, Durnavirales, Reovirales, Mononegavirales, Bunyavirales) show the highest proportion of VIRES sequences with no close relatives among EVRD-aa and ZOVER-bat references, indicative of the greatest undiscovered bat-specific viral diversity in China?
>
> *Rationale:* The candidate well addresses phylogenetic novelty and RNA-virus diversity using BtCN-Virome ML phylogenies and specific files, but it omits ecological-driver, human-settlement, and host-species aspects required by the matched gold question.

**Rank 3** · Comp = 0.850 · ✅ pass

> Do Chinese bat pools sampled from intestine tissue show higher RNA virus diversity (tv) than those sampled from lung tissue, and is this tissue-level difference modulated by bat family and climatic variables (tas10, hurs10, vpd10) in the ecological metadata?
>
> *Rationale:* The question asks whether tissue, bat family, and climate predict RNA-virus 'tv' in Chinese bats and specifies appropriate tests and metadata files, matching GQ_002's focus on covariates, viral richness, and statistical modeling with strong data grounding.

**Rank 4** · Comp = 0.520 · ❌ fail

> Can the conserved RdRp motifs A, B, and C (GDD catalytic triad) from the motif collection, combined with the BtCN-Virome contig sequences, be used to assign previously unclassified bat contigs to specific RNA virus orders and estimate the fraction of the Chinese bat virome that remains taxonomically unassignable by motif-based classification?
>
> *Rationale:* The candidate is a well-grounded, data-specific taxonomic classification question using RdRp motifs on BtCN contigs, which aligns with GQ_001's metatranscriptome/RNA-virus focus but omits the ecological and human-settlement aspects required by that gold question.

**Rank 5** · Comp = 0.850 · ✅ pass

> Does the geographic or climatic diversity of sampling sites across China, as measured by climatic variables (tas10, pr10, H10) in the ecological metadata, correlate with the number of BtCN-Virome contigs assembled per pool after controlling for bat family and sample size, suggesting that environmentally diverse roost sites host more virologically rich bat communities?
>
> *Rationale:* The candidate precisely targets which geographic and climatic covariates explain bat virome richness using contig counts and a clear negative-binomial model, matching the gold question's intent and fully referencing available metadata and files.

### ✅ `gemini-3.1-pro` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 5 | 5 | 4 | 3.825 | 0.765 | ✅ | GQ_002 (S) |
| 3 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 5 | 1 | 2 | 2 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> How does the phylogenetic diversity of RNA viruses correlate with the evolutionary history of their bat hosts across different ecological regions in China?
>
> *Rationale:* The candidate best matches the ecological-modeling intent by linking host phylogeny, viral phylogenetic diversity, and ecological/geographic covariates with concrete data files and co-phylogenetic methods.

**Rank 2** · Comp = 0.765 · ✅ pass

> What are the primary ecological and environmental drivers shaping the spatial distribution and richness of the bat virome in China?
>
> *Rationale:* The candidate strongly aligns with GQ_002 by targeting ecological/environmental covariates, geography, and richness and cites modelling approaches and specific metadata and contig files, though it emphasizes richness/spatial distribution rather than composition/diet explicitly.

**Rank 3** · Comp = 0.460 · ❌ fail

> Can novel, highly divergent RNA viruses be identified and classified using the provided collection of conserved RdRp motifs?
>
> *Rationale:* The candidate is a concrete, data-grounded virus-discovery question using RdRp motifs and contigs, so it partially matches GQ_001's RNA-virus focus but lacks the required ecological, host, and human-settlement elements.

**Rank 4** · Comp = 0.476 · ❌ fail

> Is there evidence of frequent cross-species transmission (host-switching) of viruses among sympatric bat species?
>
> *Rationale:* The candidate aligns with GQ_002 on host and geographic drivers but shifts focus to phylogenetic host-switching rather than modeling virus richness/composition or including dietary/environmental covariates.

**Rank 5** · Comp = 0.360 · ❌ fail

> How does the evolutionary rate and selection pressure vary across different viral families within the Chinese bat virome?
>
> *Rationale:* The candidate addresses molecular evolution (rates and selection) within the bat virome—well grounded in provided contigs/phylogenies—but it does not ask about ecological drivers, metatranscriptome sampling, human-settlement circulation, or host-species patterns central to GQ_001.

### ✅ `deepseek-v4-pro` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.80

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 5 | 5 | 3.910 | 0.782 | ✅ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.782 · ✅ pass

> Do bat species whose ecological niche breadth — inferred from COI-based dietary diversity and ITS-based fungal-associate richness — exceeds the phylogenetically expected baseline harbour a significantly greater richness and phylogenetic diversity of coronaviruses, as measured by RdRp motif clustering on assembled virome contigs?
>
> *Rationale:* Strong match to GQ_002: tests whether host/dietary/ecological covariates (COI/ITS) explain coronavirus richness using RdRp motifs and a phylogenetic model, covering all required elements though focused on coronaviruses specifically.

**Rank 2** · Comp = 0.640 · ✅ pass

> What proportion of assembled bat virome contigs in the full-spectrum contig set contain RdRp amino-acid motifs that fall outside the known coronavirus genus-level diversity represented in the curated RdRp motif collection, and do these putatively novel lineages cluster on particular host clades as defined by CytB phylogeny?
>
> *Rationale:* The candidate closely targets RNA-virus diversity and host-phylogeny mapping using provided virome contigs, matching GQ_001's core but omitting ecological drivers and explicit human-settlement circulation, and is well grounded in specific data files.

**Rank 3** · Comp = 0.493 · ❌ fail

> Can a machine-learning classifier trained on combined RdRp motif presence-absence features and host phylogenetic distance matrices predict whether a bat coronavirus lineage is restricted to a single host genus versus shared across multiple bat families, and does this classifier outperform one trained on RdRp features alone?
>
> *Rationale:* Aligns with GQ_002's ecological-modeling theme by using host traits and statistical models, but diverges in scope (predicting per-lineage host-range rather than virome richness/composition and omitting environmental/geographic covariates).

**Rank 4** · Comp = 0.850 · ✅ pass

> Does sampling-site-level coronavirus lineage richness correlate more strongly with local bat species richness estimated from CytB-COI barcoding than with anthropogenic land-use intensity variables recorded in the ecological modeling metadata, after controlling for unequal sampling effort across sites?
>
> *Rationale:* Strong, specific match to GQ_002: compares host diversity (CytB-derived richness) vs land-use predictors for coronavirus richness using explicit modeling and named datasets, covering all required elements and aligning with acceptable variants.

**Rank 5** · Comp = 0.731 · ✅ pass

> Are individual bats whose COI-inferred diet includes prey from multiple vertebrate orders significantly more likely to carry coronaviruses belonging to more than one distinct RdRp-defined lineage compared to bats with narrow, single-order diets?
>
> *Rationale:* The candidate tests a dietary covariate's effect on viral richness/composition using RdRp lineages and explicit statistical tests, aligning well with GQ_002 though it omits geographic covariates.

### ✅ `glm-5` — Comp=0.748 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 2 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 3 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 4 | 5 | 3 | 5 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 5 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.640 · ✅ pass

> What is the phylogenetic diversity and host species distribution of RNA viruses identified in Chinese bat populations, as revealed by RdRp motif analysis of virome contigs?
>
> *Rationale:* Matches GQ_001's virome/RNA-virus and host/geography focus using RdRp/contigs, but omits ecological drivers and human-settlement circulation required by the gold question.

**Rank 2** · Comp = 0.460 · ❌ fail

> How many novel RNA virus candidates can be identified from bat virome contigs that lack significant homology to known RdRp motifs in the reference collection?
>
> *Rationale:* Candidate focuses on sequence-discovery of novel RdRp-lacking contigs (well-grounded in provided files) but does not address the ecological, geographic, or human-settlement questions central to GQ_001.

**Rank 3** · Comp = 0.680 · ✅ pass

> Do specific bat host species, identified by CytB-COI-ITS barcoding, harbor distinct RNA viral communities with unique RdRp phylogenetic signatures?
>
> *Rationale:* The candidate aligns well with GQ_002 by testing host-species effects on viral composition using specified barcoding and RdRp data, but it omits dietary/environmental and geographic covariates required by the gold question.

**Rank 4** · Comp = 0.748 · ✅ pass

> Which ecological variables in the metadata most strongly predict RNA virus diversity across bat populations?
>
> *Rationale:* Strong semantic match to GQ_002 with explicit metadata and modeling grounding; covers environmental covariates, viral diversity, and statistical modeling, but omits explicit mention of host traits and geography.

**Rank 5** · Comp = 0.500 · ❌ fail

> What proportion of identified RNA viruses from bat viromes show phylogenetic proximity to known zoonotic pathogens based on RdRp and ML phylogenetic analysis?
>
> *Rationale:* The candidate is technically grounded and phylogenetically focused (good data grounding) but asks about zoonotic proximity rather than ecological drivers or human-settlement circulation, so it only partially matches GQ_001's intent.

### ✅ `gemini-2.5-flash` — Comp=0.731 · Pass@1=0.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 3 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 4 | 0 | 1 | 1 | 4 | 0.765 | 0.153 | ❌ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What is the diversity and composition of the virome in the BtCN samples, and how do identified RdRp motifs contribute to characterizing novel viral elements?
>
> *Rationale:* The candidate fits GQ_001's virome/composition focus and cites specific BtCN contigs and RdRp motif files, but it omits ecological drivers, host/geography, and human-settlement circulation required by the gold question.

**Rank 2** · Comp = 0.300 · ❌ fail

> How do the genetic markers CytB, COI, and ITS (from `43059592_CytB-COI-ITS.tar.gz`) reveal phylogenetic relationships or species boundaries among the sampled organisms?
>
> *Rationale:* The candidate is a phylogenetic/marker-based host-identification question (well grounded to the CytB/COI/ITS file) but largely unrelated to the matched gold’s focus on bat metatranscriptomes, RNA-virus diversity, and ecological drivers.

**Rank 3** · Comp = 0.731 · ✅ pass

> Can ecological factors described in the metadata (`45561465_Meta_data_for_ecological_modeling.zip`) explain variations in virome composition or host genetic diversity?
>
> *Rationale:* The candidate maps well to GQ_002 by asking if ecological metadata explain virome composition and host genetic diversity, covering most required elements and explicitly naming the relevant data files, but it fails to explicitly mention geographic covariates.

**Rank 4** · Comp = 0.153 · ❌ fail

> What machine learning approaches (implied by `48306316_ML_Phylo.zip`) are most effective for classifying or inferring phylogenetic relationships from the provided genetic marker data?
>
> *Rationale:* The candidate is about ML-driven phylogenetic inference on marker sequences and thus does not address the matched gold's ecological covariates or virus-richness focus, though it is grounded in specific provided files.

**Rank 5** · Comp = 0.680 · ✅ pass

> Are there specific associations or co-occurrence patterns between viral elements (from the virome data) and particular host organisms (identified by genetic markers) that are influenced by ecological conditions?
>
> *Rationale:* The candidate aligns well with GQ_002 by linking host genetic markers, virome contigs, and ecological metadata to study host–virus associations, but it omits explicit geographic covariates and frames the goal as co-occurrence rather than predicting richness.

### ✅ `intern-s1` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 2 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 3 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 1 | 4 | 1.105 | 0.221 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.400 · ❌ fail

> How does RdRp motif diversity correlate with viral genome complexity in the BtCN virome?
>
> *Rationale:* The question is well grounded in the provided virome and RdRp motif files but addresses molecular genome complexity rather than the gold's ecological and human-exposure intent, so it only weakly matches GQ_001.

**Rank 2** · Comp = 0.240 · ❌ fail

> What phylogenetic relationships exist among species based on CytB, COI, and ITS sequences?
>
> *Rationale:* The candidate is a phylogenetic/species-relationship question grounded in CytB/COI/ITS data but lacks the gold's focus on bat metatranscriptomes, RNA viruses, ecological drivers, and human-settlement circulation, so it poorly matches GQ_001.

**Rank 3** · Comp = 0.391 · ❌ fail

> Can ecological metadata predict species distribution patterns?
>
> *Rationale:* The candidate captures ecological-modeling methods but shifts target from RNA-virus diversity to species distributions and thus omits key required elements (host traits, geography, virus metrics) despite grounding to the Meta_data_for_ecological_modeling.zip.

**Rank 4** · Comp = 0.221 · ❌ fail

> How do machine learning methods improve phylogenetic tree accuracy compared to traditional approaches?
>
> *Rationale:* Candidate addresses ML phylogenetic methods, not ecological drivers of viral richness; only 'statistical model' element is covered, but it is well grounded to ML_Phylo.zip and sequence files.

**Rank 5** · Comp = 0.560 · ❌ fail

> Are there genetic markers in virome contigs indicating host-virus interactions?
>
> *Rationale:* The candidate is molecularly focused on host-virus markers in BtCN virome contigs and RdRp motifs, so it partially maps to GQ_001's metatranscriptome/RNA-virus scope but lacks the ecological, geographic, and human-exposure elements required by that gold question.

### ✅ `intern-s1-pro` — Comp=0.680 · Pass@1=1.00 · Pass@5=0.60

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 2 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 5 | 4 | 3 | 5 | 4 | 3.315 | 0.663 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> What is the phylogenetic relationship between RNA viruses identified through RdRp motifs and their host species, and how do environmental factors correlate with viral diversity patterns across different host lineages?
>
> *Rationale:* The candidate addresses ecological covariates and viral diversity using RdRp and host markers with modeling, aligning well with GQ_002 though it omits explicit geography and broadens to virus-host phylogenetics.

**Rank 2** · Comp = 0.374 · ❌ fail

> Can machine learning models trained on phylogenetic data accurately predict viral host range based on RdRp motif characteristics and host mitochondrial genetic markers?
>
> *Rationale:* Matches GQ_002 on using host traits and modeling (ML), but misses ecological/dietary/geographic covariates and the virus richness/composition focus required by the gold question.

**Rank 3** · Comp = 0.646 · ✅ pass

> How does viral community composition, as inferred from virome contigs, vary across different ecological niches and correlate with host genetic diversity?
>
> *Rationale:* The candidate asks whether ecological niches and host genetic diversity explain viral community composition, matching GQ_002's aim to link host/environmental covariates to virus composition but omitting explicit geography and modeling details.

**Rank 4** · Comp = 0.408 · ❌ fail

> What evolutionary rates and divergence times can be estimated for RNA viruses using RdRp motifs, and how do these correlate with host speciation events inferred from mitochondrial genes?
>
> *Rationale:* The candidate centers on molecular-clock estimation and host-virus co-divergence using RdRp and mitochondrial markers, which is phylogenetic rather than ecological-covariate modeling requested by the matched gold question.

**Rank 5** · Comp = 0.663 · ✅ pass

> To what extent can environmental variables from ecological metadata predict the presence and abundance of specific viral taxa identified in the virome contigs?
>
> *Rationale:* The candidate well matches GQ_002's ecological-modeling aim by proposing models linking environmental metadata to viral taxa abundance, but it omits host trait and geographic covariates required by the gold question.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.561 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 2 | 3 | 4 | 5 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 2 | 4 | 0.680 | 0.136 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.560 · ❌ fail

> To what extent do conserved RdRp motifs in the motif collection align with RNA viral sequences in the virome contigs, and what does this reveal about the diversity of RNA viruses in the sampled environment?
>
> *Rationale:* Mapped to GQ_001 because both concern RNA-virus diversity in virome/metatranscriptome data; scored modestly because the candidate is molecularly focused and well-grounded in files but omits ecological drivers, human-settlement context, and host/geography.

**Rank 2** · Comp = 0.510 · ❌ fail

> How do environmental variables in the ecological metadata correlate with the abundance and diversity of DNA barcoding markers (CytB, COI, ITS) across different sample sites?
>
> *Rationale:* The candidate matches the covariate→diversity modeling intent of GQ_002 and is well grounded in specific files, but it studies DNA barcodes (CytB/COI/ITS) rather than RNA viruses and omits host-trait elements.

**Rank 3** · Comp = 0.136 · ❌ fail

> What phylogenetic signal is preserved in the machine learning phylo dataset when compared to traditional marker-based phylogenies from CytB, COI, and ITS sequences?
>
> *Rationale:* The candidate concerns methodological phylogenetic congruence between ML outputs and marker-based trees (CytB/COI/ITS), which is unrelated to GQ_002's ecological-covariate question, though it is well grounded in specific provided files and concrete comparison metrics.

**Rank 4** · Comp = 0.510 · ❌ fail

> Are there specific RdRp motif patterns that are overrepresented in virome contigs from particular environmental conditions, suggesting adaptive evolution in response to ecological factors?
>
> *Rationale:* Related to ecological covariates and statistical testing but focuses on sequence motif enrichment (adaptive signals) rather than the gold's emphasis on host/geographic drivers of viral richness/composition.

**Rank 5** · Comp = 0.561 · ❌ fail

> How does the completeness of viral contig assemblies in the virome dataset correlate with the diversity of host DNA barcoding markers, and what does this imply about host-virus interaction dynamics?
>
> *Rationale:* The candidate aligns with GQ_002 by testing host-related predictors of viral diversity using specific files and assembly/marker metrics, but it omits dietary/environmental and geographic covariates required for full coverage.


## 4 · `flavi_jingmen_jvi_2016`

- **raw**：1 文件: `nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.748 · Pass@1=0.00 · Pass@5=0.35

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 5 | 3 | 5 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 5 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.580 · ❌ fail

> Does invertebrate host taxonomy (cricket, aphid, spider, tick, fly, flea, centipede, barnacle, water strider, lacewing, mosquito) predict viral genome architecture in the KR902709-KR902741 sequence set, specifically the partition between four-segment ~10 kb chuvirus/jingmenvirus-like genomes (Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid virus 1 and 2) and monopartite 16-26 kb polyprotein-encoding nido-/picorna-like genomes (Wuhan centipede virus, Gamboa mosquito virus, Bole tick virus 4, Xinzhou spider virus 2 and 3, Sanxia water strider virus 6, etc.)?
>
> *Rationale:* The candidate targets host-versus-genome-architecture for jingmenvirus-like vs monopartite viruses in a named FASTA set, matching the gold's host/genome-organization intent but missing vertebrate/transcriptome and explicit flavi-like/Flaviviridae evolution elements.

**Rank 2** · Comp = 0.748 · ✅ pass

> Within the five four-segment invertebrate viruses in this set (Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid virus 1, Wuhan aphid virus 2), is the four-segment plan with a conserved ~3 kb segment-1 (RdRp candidate) and three shorter ~1.9-2.9 kb segments a synapomorphy of a single chuvirus/jingmenvirus-like clade, or did it arise convergently in distinct lineages of arthropod RNA viruses?
>
> *Rationale:* The candidate directly tests polymerase (RdRp/NS5) phylogeny and genome architecture among five four-segment jingmenvirus-like taxa with concrete accessions, matching GQ_002's core intent but omitting explicit NS3/helicase and an explicit comparison to unsegmented flavi-like relatives.

**Rank 3** · Comp = 0.323 · ❌ fail

> Among the 13 monopartite polyprotein-encoding records (KR902729.1-KR902741.1) ranging from 9,653 nt to 26,315 nt, does genome length scale with the number and identity of conserved nidovirus/picornavirus replicase domains (RdRp, helicase, 3CL-protease, ExoN), and which records exceed the ~20 kb 'large RNA virus' threshold that signals nidovirus-like proofreading capacity?
>
> *Rationale:* Candidate is a genome-architecture question about replicase domains and ExoN with concrete accession-level grounding, but it omits the matched gold's phylogenetic focus and specific taxa (jingmenvirus/flavi-like), so it only partly aligns.

**Rank 4** · Comp = 0.320 · ❌ fail

> Do the per-record GC contents (range 34.26%-56.12%, mean 42.93%) of the 33 KR902709-KR902741 viral sequences segregate by host invertebrate class or by viral order, indicating that arthropod-host codon usage or RNA-virus replication mode imposes a measurable compositional signature on these viromes?
>
> *Rationale:* The candidate is a well-grounded compositional analysis of 33 sequences (explicit GC stats) but does not address the core GQ_001 intent about discovering jingmen/flavi-like viruses or revising Flaviviridae host-range/genome evolution.

**Rank 5** · Comp = 0.700 · ✅ pass

> Does the single non-arthropod record in the set, Wenling shark virus (KR902729.1, 9,653 nt polyprotein), branch within an arthropod-associated viral clade in an RdRp phylogeny built from all 13 monopartite KR902729-KR902741 records, suggesting an aquatic invertebrate-to-vertebrate host jump, or does it form an independent vertebrate-virus lineage?
>
> *Rationale:* The candidate well matches GQ_001's host-range/evolution focus (tests if KR902729.1 nests among invertebrate viruses), is tightly data-grounded, but omits explicit reference to flavi-like/jingmenvirus diversity and segmented genomes.

### ✅ `gpt-5.5-high` — Comp=0.493 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 4 | 5 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 4 | 2 | 0 | 2 | 5 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 5 | 2 | 0 | 2 | 5 | 1.445 | 0.289 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.476 · ❌ fail

> Do the five four-segment viruses in `data/nuccore_reported_viral_sequences.fasta` share a conserved segmented genome architecture, including segment-specific length classes, nucleotide composition, terminal sequence patterns, and ORF organization, that distinguishes them from the 13 single-record polyprotein viruses?
>
> *Rationale:* The candidate targets genome-architecture differences between multi-segment and polyprotein FASTA records, aligning with GQ_002's architectural intent but missing NS3/NS5 phylogenetic analysis and explicit jingmenvirus/flavi-like framing; it is tightly grounded in the provided FASTA metadata and sequence features.

**Rank 2** · Comp = 0.493 · ❌ fail

> Are the four segment classes in the segmented virus records conserved enough in length and terminal nucleotide composition to support assignment of homologous genome segments across Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid virus 1, and Wuhan aphid virus 2?
>
> *Rationale:* Matches the genome-architecture aspect of GQ_002 (segment homology across jingmen-like viruses) but lacks NS3/NS5 phylogenetic evidence and explicit mention of flavi-like/unsegmented genomes; strongly grounded in the provided fasta and named records.

**Rank 3** · Comp = 0.400 · ❌ fail

> Do viral sequences named for different host-associated groups in `data/nuccore_reported_viral_sequences.fasta` show systematic differences in genome size, GC content, and coding density?
>
> *Rationale:* The candidate examines host-labelled FASTA records for composition and coding-density differences, which aligns only with the gold's genome-organization/host-range aspect but lacks transcriptome focus and any mention of jingmen-/flavi-like viruses or Flaviviridae evolution.

**Rank 4** · Comp = 0.289 · ❌ fail

> Can nucleotide composition and predicted ORF structure alone separate the 13 polyprotein complete CDS records into biologically meaningful subgroups within the reported viral sequence set?
>
> *Rationale:* The candidate is well grounded in the provided fasta sequences and numeric statistics but asks a composition/ORF-clustering question that omits NS3/NS5 phylogenetic evidence and the jingmenvirus/flavi-like segmented vs unsegmented comparison required by GQ_002.

**Rank 5** · Comp = 0.289 · ❌ fail

> Are ambiguous nucleotide calls in `data/nuccore_reported_viral_sequences.fasta` rare enough to support reliable comparative genome-architecture analysis across all 33 viral records?
>
> *Rationale:* The candidate is a concrete, well-grounded QC question about ambiguous bases that supports genome-architecture work but does not address GQ_002's core phylogenetic/NS3-NS5 or jingmen/flavi-like relationship elements, so it matches only weakly as a secondary, data-quality precursor.

### ✅ `claude-code-sonnet-4-6` — Comp=0.720 · Pass@1=0.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 5 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 5 | 4 | 3 | 3 | 5 | 3.600 | 0.720 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.493 · ❌ fail

> Do the large polyprotein-encoding RNA viruses (>20 kb) in nuccore_reported_viral_sequences.fasta — including Gamboa mosquito virus (26,315 bp), Xinzhou spider virus 2 (24,521 bp), Wuhan centipede virus (23,676 bp), and Sanxia water strider virus 6 (22,879 bp) — share a monophyletic origin with vertebrate Nidovirales based on conserved RdRp domain phylogeny, supporting the hypothesis that large-genome RNA viruses evolved in invertebrates before expanding into vertebrate hosts?
>
> *Rationale:* Chose GQ_002 because both center on phylogenetic evidence linking virus groups and genome organization; the candidate is well-grounded in dataset sequences but misses the specific genes and taxa (NS3/NS5, jingmen-/flavi-like) required by GQ_002.

**Rank 2** · Comp = 0.306 · ❌ fail

> Are the conserved 5′-terminal nucleotide motifs shared across all four genome segments of Wuhan cricket virus (TATAA…), Wuhan aphid virus 1 and 2, Wuhan flea virus, and Shuangao insect virus 7 sufficient to determine whether these five arthropod-associated 4-segment viruses belong to a single new clade within Reoviridae, based on terminal sequence identity and segment-size hierarchy?
>
> *Rationale:* Candidate concerns segmented-virus clade assignment via terminal motifs and size hierarchy, which loosely matches GQ_002's genome-architecture theme but omits GQ_002's specific proteins and taxa; it is strongly data-grounded.

**Rank 3** · Comp = 0.646 · ✅ pass

> Does Wenling shark virus (KR902729.1, 9,653 bp, GC = 55.2%) represent a phylogenetic link between the small-genome arthropod viruses (~10.5 kb segmented) and the large polyprotein invertebrate viruses (>16 kb) in this dataset, based on genome size, GC content, and polyprotein organization?
>
> *Rationale:* The candidate well targets phylogenetic and genome-architecture linkage between segmented and unsegmented flavi-like viruses with strong data grounding, but omits the NS3/NS5 locus and explicit mention of jingmenvirus required by the gold question.

**Rank 4** · Comp = 0.320 · ❌ fail

> Do tick-associated RNA viruses in this dataset (Bole tick virus 4, KR902736.1, GC=56.1%; Tacheng tick virus 8, KR902741.1, GC=44.1%) show significantly elevated GC content relative to non-hematophagous arthropod-associated viruses (mean GC ~40%), and does this GC enrichment correlate with increased genome size (16.2 and 19.5 kb respectively) compared to the dataset average?
>
> *Rationale:* The candidate is a well-grounded hypothesis about GC content and genome size in tick viruses but does not ask about transcriptome mining, jingmenviruses, flavi-like viruses, or Flaviviridae evolutionary relationships, so it only weakly matches GQ_001.

**Rank 5** · Comp = 0.720 · ✅ pass

> Can coinfection of a single host species (Orthoptera: crickets) by two phylogenetically distinct RNA virus types — a 4-segment ~10.5 kb reovirus-like Wuhan cricket virus (KR902709–KR902712) and a ~21.8 kb polyprotein Xingshan cricket virus (KR902738) — be explained by differential cellular tropism or replication compartmentalization, as inferred from their contrasting genome architectures and nucleotide compositions?
>
> *Rationale:* The candidate strongly matches the segmented vs flavi-like arthropod-virus intent and is well grounded in sequence data, but it lacks the transcriptome-mining approach and vertebrate/Flaviviridae-evolution framing in GQ_001.

### ✅ `gemini-3.1-pro` — Comp=0.580 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 4 | 2 | 2 | 3 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 1 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 0.935 | 0.187 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What are the evolutionary relationships and potential reassortment events among the segmented insect-specific viruses identified in this dataset?
>
> *Rationale:* The candidate targets segment-by-segment phylogenies and reassortment among segmented insect viruses (grounded in nuccore_reported_viral_sequences.fasta), matching GQ_002's phylogenetic/genome-architecture focus but missing NS3/NS5 and explicit jingmen/flavi comparisons.

**Rank 2** · Comp = 0.580 · ❌ fail

> Are there conserved genetic motifs or secondary structures across the different segments of these insect viruses that might be involved in packaging or replication?
>
> *Rationale:* The candidate aligns with GQ_001's genome-organization/segmented-jingmenvirus intent (mentions segments and Wuhan cricket virus) but misses the transcriptome-mining and flavi-like/Flaviviridae evolutionary scope required by the gold.

**Rank 3** · Comp = 0.340 · ❌ fail

> What is the predicted coding capacity and functional annotation of the open reading frames (ORFs) within these viral segments?
>
> *Rationale:* The candidate focuses on ORF prediction/annotation within viral segments (protein-level genome analysis), so it partially matches GQ_002's genome-architecture intent but lacks specific NS3/NS5 and phylogenetic elements and resembles the unacceptable 'Do proteins have domains?'.

**Rank 4** · Comp = 0.280 · ❌ fail

> Do these insect-specific viruses exhibit distinct codon usage biases compared to their respective host organisms?
>
> *Rationale:* The candidate studies codon usage adaptation in insect viruses (specific hosts and a FASTA file) which addresses host adaptation but does not ask about transcriptome mining, jingmenviruses, flavi-like viruses, or Flaviviridae evolutionary/genome questions central to GQ_001.

**Rank 5** · Comp = 0.187 · ❌ fail

> Can we identify potential viral entry or attachment proteins by analyzing the sequence features of the predicted viral surface glycoproteins?
>
> *Rationale:* The candidate targets protein feature prediction (entry glycoproteins) not phylogenetic links or NS3/NS5, so it poorly matches GQ_002 (low match and required-element coverage), though it is grounded to one specific fasta file.

### ✅ `deepseek-v4-pro` — Comp=0.697 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 3 | 4 | 4 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 3 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.697 · ✅ pass

> Do the RNA-dependent RNA polymerase (RdRp) phylogenies of these 14 arthropod-associated viruses reveal host-switching events, and can conserved polymerase motifs distinguish segmented-genome viruses from non-segmented polyprotein-encoding viruses in this collection?
>
> *Rationale:* The candidate matches GQ_002 by using polymerase (RdRp/NS5) phylogenies to test relationships between segmented and non-segmented viruses with concrete dataset examples, but it omits explicit mention of jingmenviruses and 'flavi-like' labeling while adding host-switching and motif analyses.

**Rank 2** · Comp = 0.620 · ✅ pass

> Is there evidence of inter-segment reassortment among the multi-segment arthropod viruses, and does reassortment frequency correlate with the taxonomic breadth of their host range?
>
> *Rationale:* The candidate focuses on reassortment among segmented arthropod viruses and its relation to host-range and genome evolution, which aligns partially with GQ_001's evolutionary and host-range intent but lacks transcriptome/vertebrate sampling and explicit flavi-like framing.

**Rank 3** · Comp = 0.380 · ❌ fail

> Do codon usage bias patterns in these arthropod-associated viral genomes cluster by host taxonomic order, reflecting host-driven adaptive evolution of viral translational machinery?
>
> *Rationale:* The candidate asks a different scientific question (host-driven codon usage patterns) than GQ_001's focus on discovering jingmen/flavi-like genomes and Flaviviridae evolution, so it partially overlaps on 'arthropod/host' context but misses core elements like jingmenviruses and Flaviviridae-specific claims.

**Rank 4** · Comp = 0.240 · ❌ fail

> Are conserved RNA secondary structures identifiable in the untranslated regions (UTRs) flanking the polyprotein genes of these novel arthropod viruses, and do they resemble internal ribosome entry site (IRES) elements from known dicistrovirus or iflavirus families?
>
> *Rationale:* The candidate addresses RNA structural elements (IRES in UTRs) of arthropod viruses, which is a different, narrower mechanistic question than GQ_001's evolutionary/discovery focus and therefore a weak semantic match despite good data grounding.

**Rank 5** · Comp = 0.240 · ❌ fail

> Does the geographic distance between arthropod sampling locations in China better predict pairwise viral genome nucleotide identity than the phylogenetic distance between arthropod host species?
>
> *Rationale:* The candidate addresses viral phylogeography using arthropod samples and sequence identity, which is unrelated to the GQ_001 emphasis on mining transcriptomes for jingmen-/flavi-like viruses and revising Flaviviridae evolution; it is dataset-grounded but semantically mismatched.

### ✅ `glm-5` — Comp=0.500 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What phylogenetic relationships exist among these novel arthropod-associated segmented viruses, and do their genome architectures indicate shared evolutionary origins across diverse host taxa?
>
> *Rationale:* The candidate fits a phylogeny + genome-architecture gold question (GQ_002) but omits key specific elements (NS3/NS5, jingmenvirus vs flavi-like/unsegmented comparison); it is well grounded in the provided FASTA. Scores reflect partial semantic alignment and concrete data grounding.

**Rank 2** · Comp = 0.500 · ❌ fail

> Do the polyprotein gene sequences from barnacle, fly, mosquito, and spider viruses share conserved protein domains that suggest functional or evolutionary relationships?
>
> *Rationale:* The candidate is grounded in specific arthropod polyprotein sequences and asks about conserved domains (data-grounding strong) but omits key Flaviviridae/jingmenvirus and vertebrate-host elements required by the gold question, so it partially matches the intent.

**Rank 3** · Comp = 0.460 · ❌ fail

> Is there evidence of host-specific sequence adaptation in the viral genomes when comparing viruses from closely related host taxa versus distantly related hosts?
>
> *Rationale:* Candidate aligns with GQ_001 only on host-range comparison (hence partial match), lacks explicit mention of transcriptome mining and jingmen/flavi targets, is well grounded in the provided fasta and named viruses, and therefore scores moderate match, low required-element coverage, low acceptability, and good data grounding.

**Rank 4** · Comp = 0.120 · ❌ fail

> What geographic distribution patterns emerge from the viral sequence metadata, and do these patterns correlate with host ecology or sampling intensity?
>
> *Rationale:* The candidate addresses geographic/metadata analysis (well grounded in the FASTA headers) but does not address any required virology elements from GQ_001, so match is poor despite strong data grounding.

**Rank 5** · Comp = 0.425 · ❌ fail

> Do the segment length ratios and nucleotide composition differ significantly between the four genomic segments across segmented viruses?
>
> *Rationale:* Matches GQ_002's genome-architecture theme (segmented genomes) but omits NS3/NS5 and phylogenetic comparisons to unsegmented flavi-like viruses; well-grounded in specific fasta accessions and concrete segment analyses.

### ✅ `gemini-2.5-flash` — Comp=0.580 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 2 | 0 | 1 | 3 | 1.105 | 0.221 | ❌ | GQ_002 (S) |
| 3 | 4 | 1 | 3 | 4 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 4 | 3 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What are the phylogenetic relationships among the various insect and arthropod viruses represented in this dataset?
>
> *Rationale:* The candidate targets phylogenetic analysis of arthropod viruses (matching GQ_002's phylogeny focus) but is generic and omits the NS3/NS5 and segmented vs unsegmented jingmenvirus–flavi-like specifics required by the gold question.

**Rank 2** · Comp = 0.221 · ❌ fail

> Are there conserved genetic regions or motifs across the diverse viral sequences in this dataset, and what might be their functional significance?
>
> *Rationale:* The candidate addresses conserved motifs in viral sequences (a general protein/functional angle) but omits all specific elements (NS3/NS5, jingmenvirus, segmentation and phylogeny) required by GQ_002, so it aligns weakly and resembles an unacceptable, domain-focused variant.

**Rank 3** · Comp = 0.580 · ❌ fail

> How does the genome organization (segmented vs. polyprotein) correlate with the host range or viral family classification within this dataset?
>
> *Rationale:* The candidate targets genome-organization versus host-range correlations in the provided viral sequences, which partially matches GQ_001's intent on genome organization and host range but lacks explicit transcriptome/mining framing and mention of jingmenviruses or flavi-like/Flaviviridae context.

**Rank 4** · Comp = 0.493 · ❌ fail

> Do the different segments of segmented viruses (e.g., Wuhan cricket virus, Wuhan aphid virus) exhibit varying rates of evolution or selective pressures?
>
> *Rationale:* The candidate addresses evolutionary differences among segments of jingmenvirus-like segmented genomes (matching GQ_002's segmented/unsegmented evolution theme) but lacks explicit NS3/NS5 phylogenetic analysis and mention of flavi-like relatives, covering two of five required elements.

**Rank 5** · Comp = 0.280 · ❌ fail

> Can specific genetic markers be identified that are unique to viruses infecting particular arthropod hosts (e.g., cricket vs. aphid vs. tick)?
>
> *Rationale:* The candidate focuses on host-specific genetic markers in arthropod viruses (specific hosts and an explicit fasta file), which only partially overlaps GQ_001's host-range/evolution theme but omits key elements about jingmenviruses, flavi-like viruses, transcriptomes, and Flaviviridae evolution.

### ✅ `intern-s1` — Comp=0.425 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 2 | 3 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 2 | 3 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What is the variation in GC-content across different viral strains and segments, and how does this relate to their evolutionary relationships?
>
> *Rationale:* The candidate partially aligns with GQ_002 by addressing segments and evolutionary relationships but omits locus-specific markers (NS3/NS5) and explicit jingmenvirus/flavi-like targets; it is data-grounded to the provided FASTA.

**Rank 2** · Comp = 0.374 · ❌ fail

> How does sequence length variation correlate with viral strain differentiation across different segments?
>
> *Rationale:* The candidate addresses segment-level genome variation in the provided FASTA (grounded) but lacks the phylogenetic (NS3/NS5) and taxon-specific (jingmenvirus/flavi-like) elements central to GQ_002, so it partially matches genome-organization intent.

**Rank 3** · Comp = 0.340 · ❌ fail

> What evidence of recombination exists between different viral strains based on sequence similarity patterns?
>
> *Rationale:* The candidate addresses genome-segmentation and sequence-based recombination, which partially maps to GQ_002's genome-architecture theme, but it lacks the required NS3/NS5, phylogenetic analyses, and jingmenvirus/flavi-like taxonomic focus; it is grounded to a specific fasta file.

**Rank 4** · Comp = 0.360 · ❌ fail

> How does codon usage bias vary between different viral strains and what does this reveal about host adaptation?
>
> *Rationale:* The candidate concerns viral host adaptation via codon usage, which overlaps broadly with host-range/evolution intent but omits the gold's specific focus on transcriptome mining and jingmenvirus/flavi-like discovery.

**Rank 5** · Comp = 0.306 · ❌ fail

> What phylogenetic relationships exist between the different viral strains based on their complete genome sequences?
>
> *Rationale:* Candidate aligns with the phylogeny focus of GQ_002 but is generic and omits NS3/NS5, jingmenvirus/flavi-like context and segmented-vs-unsegmented genome framing; it does reference the provided fasta file.

### ✅ `intern-s1-pro` — Comp=0.480 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 3 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.480 · ❌ fail

> Can we determine the evolutionary relationships between Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, and Wuhan aphid viruses based on sequence alignment of their complete segments, and identify evidence of host-specific adaptation?
>
> *Rationale:* The candidate is a focused phylogenetic/host-adaptation question about insect viral segments (good partial match to GQ_001's evolution/host-range theme) but omits transcriptome-mining, jingmenvirus/flavi-like labels, and vertebrate scope, so coverage and match are limited.

**Rank 2** · Comp = 0.476 · ❌ fail

> Is there evidence of segment reassortment between different strains of Wuhan aphid virus (WHYC-1 vs WHYC-2) by comparing the phylogenetic trees of different segments?
>
> *Rationale:* Mapped to GQ_002 for its phylogenetic/segmented-virus focus; well-grounded in the provided sequences and segments but missing NS3/NS5 and explicit jingmenvirus vs flavi-like comparisons, yielding a moderate match and coverage.

**Rank 3** · Comp = 0.306 · ❌ fail

> What are the most conserved protein-coding regions across all these viral sequences, and do they correspond to known viral functional domains such as RNA-dependent RNA polymerase?
>
> *Rationale:* The candidate focuses on conserved proteins and RdRp (NS5), so it partially aligns with polymerase-related intent but lacks explicit NS3/NS5 phylogenetic analysis and the jingmenvirus vs flavi-like genome comparison required by GQ_002.

**Rank 4** · Comp = 0.100 · ❌ fail

> Do viral sequences from the same geographic location (Wuhan) cluster more closely together in phylogenetic analysis than viruses from different locations, suggesting geographic isolation?
>
> *Rationale:* The candidate addresses geographic clustering of Wuhan-labeled sequences, which is unrelated to the Flaviviridae-focused gold question; it does, however, reference a concrete fasta file, giving modest data grounding.

**Rank 5** · Comp = 0.400 · ❌ fail

> Do the viral sequences show patterns of codon usage bias that correlate with their insect hosts (cricket, flea, aphid), suggesting host-specific adaptation at the translational level?
>
> *Rationale:* Matches GQ_001 only on host-specific adaptation; it omits key Flaviviridae/jingmenvirus focus and transcriptome framing, and is grounded in one concrete fasta file.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.374 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 3 | 3 | 1 | 2 | 3 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 5 | 1 | 0 | 2 | 3 | 0.935 | 0.187 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.357 · ❌ fail

> Do segmented viral genomes exhibit consistent segment length hierarchies across different virus families, suggesting conserved packaging or replication constraints?
>
> *Rationale:* The candidate targets genome-architecture questions about segmented genomes and is data-grounded in the provided fasta, but it omits NS3/NS5 phylogenetic evidence and any jingmen-/flavi-like emphasis required by GQ_002.

**Rank 2** · Comp = 0.340 · ❌ fail

> Is there significant variation in GC content between different viral segments within the same virus, and does this correlate with segment function or position?
>
> *Rationale:* Matches GQ_002's genome-architecture theme (segmented genomes) but lacks the core phylogenetic/NS3-NS5 focus and explicit mention of jingmenviruses or flavi-like relationships; it is concretely grounded to the provided FASTA for GC analyses.

**Rank 3** · Comp = 0.374 · ❌ fail

> Do polyprotein-encoding viruses (Beihai barnacle virus, Shayang fly virus, Gamboa mosquito virus) exhibit different nucleotide composition patterns compared to segmented viruses, reflecting different genome organization strategies?
>
> *Rationale:* Matches the genome-architecture theme of GQ_002 (segmented vs unsegmented) but lacks the core NS3/NS5 phylogenetic and flavivirus-specific elements; it is well grounded to the provided fasta sequences.

**Rank 4** · Comp = 0.306 · ❌ fail

> Are there conserved sequence motifs or regions across different segments of the same virus family that might indicate functional importance or common regulatory elements?
>
> *Rationale:* The candidate focuses on conserved motifs across segments (a genome-organization aspect) but lacks the phylogenetic/NS3-NS5 framing and explicit links to jingmenviruses or flavi-like unsegmented relatives, so it only partially aligns with GQ_002.

**Rank 5** · Comp = 0.187 · ❌ fail

> What is the distribution of ambiguous nucleotide codes (e.g., R, Y, N) across the viral sequences, and do they cluster in specific regions or segments suggesting sequencing uncertainty or biological variation?
>
> *Rationale:* The candidate addresses sequence-quality patterns in a viral FASTA (well grounded) but does not engage phylogenetic, NS3/NS5, or jingmenvirus/flavi-like evolutionary questions required by GQ_002, so semantic match is weak.


## 5 · `invertebrate_rna_virosphere_2016`

- **raw**：2 文件: `5905695_alignments_and_phylogenies.zip, 5905698_all_virus_genomes.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> Across the 22 invertebrate RNA-virus clades represented in 5905698_all_virus_genomes.fasta, do RdRp-based phylogenies (e.g. Hepe-Virga_RdRp_phylogeny.nwk, Luteo-Sobemo_RdRp_phylogeny.nwk) and matched structural-protein phylogenies in RdRp_versus_structural/ (capsid S-domain, jelly-roll A6/A21/Alverna) exhibit topological incongruence indicative of widespread modular recombination between replication and structural genes during the diversification of the invertebrate RNA virosphere?
>
> *Rationale:* The candidate aligns with GQ_001's evolutionary scope but narrows to detecting modular recombination via RdRp vs structural-tree incongruence; it is well-grounded in provided FASTA and Newick files but omits explicit mention of transcriptomes, breadth, and deep-lineage redefinition.

**Rank 2** · Comp = 0.940 · ✅ pass

> Within the five 'New-' putative virus phyla (New-Qinvirus, New-Weivirus, New-Yanvirus, New-Yuevirus, New-Zhaovirus) recovered in the FASTA, does the RdRp phylogenetic position of each lineage relative to the established Narna-Levi / Tombus-Noda / Partiti-Picobirna clades support their proposal as bona fide phylum-rank lineages rather than divergent members of existing groups?
>
> *Rationale:* Highly aligned: the candidate concretely tests deep-lineage/phylum claims using RdRp phylogenies and provided files; it only omits explicit mention of 'invertebrate transcriptomes' from the question text.

**Rank 3** · Comp = 0.544 · ❌ fail

> Among the negative-sense and segmented RNA-virus clades in the dataset (Bunya-Arena, Mono-Chu, Orthomyxo, Reo, Partiti-Picobirna), how often do RdRp, glycoprotein, nucleoprotein and capsid segments from the same metatranscriptome library co-segregate phylogenetically, and is segment reassortment between co-circulating viruses detectable from the matched per-segment trees?
>
> *Rationale:* The candidate closely targets segmentation and segment-level phylogenies (central to GQ_002) and is strongly data-grounded, but it asks about reassortment detection rather than explicitly about manual curation or genome length.

**Rank 4** · Comp = 0.640 · ✅ pass

> Does invertebrate host group, encoded by FASTA library prefixes (spider, tick, mosHB, arthropodmix, BHJJX hermit-crab, BHNXC sipunculid worm), predict clade membership in the per-clade RdRp phylogenies, indicating phylogenetically structured host association rather than free host-switching across the invertebrate RNA virosphere?
>
> *Rationale:* The candidate aligns with GQ_001's phylogenetic analysis of invertebrate-associated viruses and is well grounded in specific FASTA and tree files, but it focuses on host-structure rather than testing breadth or uncovering deep lineages.

**Rank 5** · Comp = 0.527 · ❌ fail

> Do nucleotide-level genome length distributions across the 22 clades in 5905698_all_virus_genomes.fasta (median 4,454 nt, max 30,353 nt) reveal clade-specific upper limits consistent with replication-fidelity ceilings, and does the ratio of long (>15 kb) to short genomes systematically distinguish nidovirus-like from other positive-sense RNA clades in this invertebrate sample?
>
> *Rationale:* The candidate is best matched to GQ_002 because it interrogates genome-level patterns in assembled viral genomes using specific FASTA headers and phylogenies, but it omits segmentation and explicit manual-curation requirements demanded by GQ_002.

### ✅ `gpt-5.5-high` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 5 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.940 · ✅ pass

> How do the 2,339 uploaded RNA virus genome records reshape RdRp-based phylogenetic relationships among established and newly named viral groups, and do they reveal invertebrate-associated lineages that bridge or expand known RNA virus diversity?
>
> *Rationale:* The candidate fully targets phylogenetic placement of many assembled viral genomes and discovery of deep invertebrate-associated clades, but omits the explicit phrase 'invertebrate transcriptomes' while grounding the question in specific provided files and trees.

**Rank 2** · Comp = 0.408 · ❌ fail

> Do RdRp and structural-protein phylogenies show incongruent relationships among the uploaded RNA viruses, indicating modular genome evolution or recombination between polymerase and capsid/structural genes?
>
> *Rationale:* Related to genome-architecture analysis but focuses on phylogenetic incongruence/recombination rather than segmentation, length, or explicit manual curation needs; well grounded in provided RdRp/structural alignment files.

**Rank 3** · Comp = 0.646 · ✅ pass

> Which viral groups in the uploaded genomes show evidence of segmented genome organization, and how are RdRp, glycoprotein, nucleoprotein, capsid, and NS segments distributed across their phylogenetic lineages?
>
> *Rationale:* Matches GQ_002 well by interrogating segmentation and segment distribution across phylogenies with concrete file/FASTA evidence; however it omits genome length metrics and explicit mention of manual curation. Data grounding is strong via filenames and numeric header counts.

**Rank 4** · Comp = 0.820 · ✅ pass

> Are the newly named groups New-Qinvirus, New-Weivirus, New-Yanvirus, New-Zhaovirus, and New-Yuevirus phylogenetically coherent lineages with genome sizes and RdRp placements distinct from established RNA virus groups?
>
> *Rationale:* Candidate aligns well with GQ_001 by testing monophyly and distinctness of new groups using assembled genomes and RdRp trees (strong data grounding), but omits explicit mention of 'invertebrate transcriptomes' required by the gold.

**Rank 5** · Comp = 0.697 · ✅ pass

> How does genome length and gene architecture vary across the 22 viral group labels in the uploaded FASTA, and are these architectural differences reflected in the available RdRp phylogenies?
>
> *Rationale:* Good semantic match to GQ_002 on genome architecture, segmentation and assembled FASTA + RdRp phylogenies; covers four of five required elements but omits explicit 'manual curation' focus despite strong data grounding in specific FASTA and RdRp files.

### ✅ `claude-code-sonnet-4-6` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 3 | 5 | 3.600 | 0.720 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 3 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 4 | 2 | 4 | 4 | 5 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.720 · ✅ pass

> Do the RNA-dependent RNA polymerase (RdRp) and structural protein (S-domain, A6-fold, A21-fold, Alverna-fold) phylogenies of invertebrate RNA viruses in the Tombus-Noda, Hepe-Virga, and Narna-Levi supergroups show statistically significant topological incongruence, providing evidence that capsid genes were independently acquired rather than co-inherited with the replication module during the deep evolution of positive-sense RNA viruses?
>
> *Rationale:* The candidate matches GQ_001's phylogenetic/deep‑lineage intent and is strongly data‑grounded, but it narrows scope to gene‑tree incongruence (RdRp vs capsid) and omits explicit mention of transcriptome mining or assembled genomes.

**Rank 2** · Comp = 0.680 · ✅ pass

> Across the 22 RNA virus supergroups represented in the 2,339-sequence invertebrate RNA virosphere dataset, do viruses infecting phylogenetically distant invertebrate host taxa (e.g., arthropods vs. nematodes vs. molluscs) cluster by host phylum or by viral family in RdRp-based phylogenies, and does the degree of host-phylogeny congruence differ significantly between supergroups with broad versus narrow host ranges?
>
> *Rationale:* Candidate aligns with GQ_001's phylogenetic exploration of invertebrate RNA-virus diversity and is well grounded in provided FASTA and phylogeny files, but it pivots to host-clustering questions and omits explicit mention of transcriptome mining and 'deep lineages.'

**Rank 3** · Comp = 0.940 · ✅ pass

> Do the five putative novel RNA virus families (New-Weivirus, New-Qinvirus, New-Yanvirus, New-Zhaovirus, New-Yuevirus) represented by 56 sequences in 5905698_all_virus_genomes.fasta occupy phylogenetically isolated positions in all available RdRp trees, or do their RdRp sequences place them within or sister to established families, indicating that these lineages represent deeply divergent members of known supergroups rather than entirely new RNA virus phyla?
>
> *Rationale:* The candidate precisely targets phylogenetic placement of five novel family-level groups using RdRp trees and named files, aligning tightly with GQ_001's focus on deep-lineage discovery, but it omits an explicit mention of invertebrate transcriptomes.

**Rank 4** · Comp = 0.561 · ❌ fail

> Among the 46 Flavi-group sequences in 5905698_all_virus_genomes.fasta, which include both monopartite (e.g., Beihai barnacle virus 1, len=18,719 nt; Xinzhou spider virus 2, len=24,521 nt) and multi-segmented Jingmen-like viruses (4 RNA segments encoding NS5-like, NS3-like, glycoprotein, and nucleoprotein functions), do the NS5-like (RdRp) and NS3-like (helicase) segments yield congruent phylogenies supporting a single origin of genome segmentation, or do incongruent topologies indicate that segmentation arose independently in multiple Flavivirus-like lineages?
>
> *Rationale:* Candidate aligns with GQ_002 on segmentation and genome architecture and is strongly data-grounded, but it reframes the question toward phylogenetic origins of segmentation rather than identifying genomes that need manual curation.

**Rank 5** · Comp = 0.760 · ✅ pass

> Do the 11 invertebrate RNA viruses from the Tombus-Noda and Hepe-Virga groups annotated with ciliate codon usage (ciliate_coding / Ciliate_coding in 5905698_all_virus_genomes.fasta) form distinct monophyletic clades within the RdRp-based and structural-protein-based phylogenies, consistent with long-term stable associations with ciliate protist hosts rather than transient infection of invertebrate animals?
>
> *Rationale:* The candidate aligns well with GQ_001's phylogenetic intent using assembled invertebrate genomes and specific phylogeny files, but is narrower—testing ciliate-host signatures rather than surveying overall virosphere breadth or deep lineage diversity.

### ✅ `gemini-3.1-pro` — Comp=0.640 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 2 | 2 | 2 | 4 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.640 · ✅ pass

> What are the evolutionary relationships and potential recombination events between established plant Potyviruses and the newly identified astro-like and poty-like viruses, and do these relationships suggest a shared ancestral host or cross-kingdom host-jumping events?
>
> *Rationale:* The candidate aligns with GQ_001's phylogenetic/deep-lineage intent and is well grounded in the provided FASTA/phylogeny files, but it omits the invertebrate-transcriptome scope and broad RNA-virosphere framing required by the gold question.

**Rank 2** · Comp = 0.561 · ❌ fail

> How do the genome lengths and gene contents of the 'astro-like' and 'poty-like' viruses compare to established Potyviruses, and what does this variation indicate about their evolutionary adaptation?
>
> *Rationale:* The candidate is a genomics-focused comparison grounded in the provided FASTA (specific lengths) and matches GQ_002's architecture theme, but it omits segmentation analysis and any explicit manual curation question, so it only partially fulfills the gold intent.

**Rank 3** · Comp = 0.300 · ❌ fail

> Are there specific conserved sequence motifs or structural elements shared between Astroviridae and Potyviridae that justify their grouping in this dataset?
>
> *Rationale:* The candidate is a different, narrower molecular-motif question tied to a specific 'Astro-Poty' grouping and genome FASTA, so it is grounded in provided files but does not address the gold's core themes of invertebrate transcriptomes or deep-lineage phylogenetics.

**Rank 4** · Comp = 0.560 · ❌ fail

> What is the phylogenetic diversity and geographic distribution of the 'poty-like' and 'astro-like' viruses based on the provided sequence data?
>
> *Rationale:* Candidate aligns partially with GQ_001 via phylogenetic analysis and assembled genomes but is narrower (specific clades + geography) and omits invertebrate-transcriptome scope and deep-lineage framing; it is well-grounded in the provided files/headers.

**Rank 5** · Comp = 0.440 · ❌ fail

> Can the sequence divergence within the 'Astro-Poty' group be used to estimate the time of their most recent common ancestor?
>
> *Rationale:* The candidate centers on molecular-clock dating (MRCA) for a specific virus group using provided alignments/genomes, matching GQ_001's phylogenetic angle but missing the transcriptome-driven diversity/redefinition focus.

### ✅ `deepseek-v4-pro` — Comp=0.740 · Pass@1=0.00 · Pass@5=0.20

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 2 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 4 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 4 | 2 | 2 | 2 | 3 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.540 · ❌ fail

> Do the phylogenetic relationships among the novel Astro-Poty RNA virus genomes support host-switching between arthropod and plant hosts as the dominant mode of diversification, as opposed to vertical co-divergence with host lineages?
>
> *Rationale:* The candidate aligns with GQ_001 on using phylogenies of assembled viral genomes but shifts focus to host-switching vs co-divergence and omits the gold's emphasis on invertebrate transcriptome mining and broad/deep virosphere redefinition.

**Rank 2** · Comp = 0.527 · ❌ fail

> Is there evidence of reassortment among the segmented Bunya-Arena viruses based on topological incongruence between the RdRp, Glycoprotein, and Nucleoprotein gene trees?
>
> *Rationale:* The candidate fits GQ_002's segmentation/architecture theme and is well grounded in supplied FASTA/alignments, but it addresses reassortment via phylogenetic incongruence rather than genome-length metrics or explicit manual curation needs.

**Rank 3** · Comp = 0.740 · ✅ pass

> Does the 'Astro-Poty' group of viruses, whose members share features of both Astroviridae and Potyviridae, form a monophyletic lineage that bridges these two recognized families, and what are the implications for RNA virus taxonomy?
>
> *Rationale:* The candidate focuses on phylogenetic placement and taxonomic consequences of a specific putative lineage (Astro-Poty), matching GQ_001's deep-lineage/phylogeny intent but lacking explicit invertebrate-transcriptome framing and a broader survey of RNA virosphere breadth.

**Rank 4** · Comp = 0.357 · ❌ fail

> Are segmented viral genomes (Bunya-Arena, Birna) associated with broader host ranges across the sampled hosts compared to non-segmented genomes (Astro-Poty, Picorna-Calici, Toti-Chryso) among these novel viruses?
>
> *Rationale:* Matched to the genome-architecture gold (GQ_002) because it centers on segmentation, but it diverges from GQ_002's curation focus by asking about ecological host-range correlations; it is grounded to the FASTA file but misses curation and length/architecture elements.

**Rank 5** · Comp = 0.580 · ❌ fail

> Do the RdRp-based phylogenies from the alignments reveal geographic clustering of viral lineages among the four sampled Chinese locations (Beihai, Hubei, Wuhan, and Changjiang), suggesting local diversification rather than widespread dispersal?
>
> *Rationale:* The candidate leverages provided RdRp alignments/trees and FASTA headers to test geographic clustering (strong data grounding) but diverges from GQ_001's focus on invertebrate-transcriptome-driven breadth and deep-lineage discovery.

### ✅ `glm-5` — Comp=0.680 · Pass@1=0.00 · Pass@5=0.20

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 1 | 2 | 2 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.580 · ❌ fail

> What phylogenetic relationships exist among the Astro-Poty, Birna, and Bunya-Arena virus families across the Hubei, Beihai, Wuhan, and Changjiang geographic regions, and do geographic location or host species explain the observed clustering patterns?
>
> *Rationale:* Aligns with GQ_001 on using assembled genomes and trees for phylogenetic analysis, but focuses on geographic/host clustering and omits invertebrate-transcriptome scope and explicit deep-lineage/repertoire questions.

**Rank 2** · Comp = 0.480 · ❌ fail

> Do Bunya-Arena viruses exhibit higher host diversity compared to Astro-Poty and Birna viruses, and what ecological factors might explain this difference?
>
> *Rationale:* The candidate is a data-grounded host-diversity comparison using assembled virus FASTA headers, so it partially aligns with GQ_001's virosphere/breadth theme but omits the transcriptome source and phylogenetic/deep-lineage framing.

**Rank 3** · Comp = 0.680 · ✅ pass

> Are genome length distributions significantly different among Astro-Poty, Birna, and Bunya-Arena virus families, and do these differences reflect distinct genome architectures?
>
> *Rationale:* This question aligns with GQ_002 by examining genome length and segmentation using assembled FASTA records (covers 4/5 required elements), but it fails to address manual curation, so it is a strong but not complete match.

**Rank 4** · Comp = 0.360 · ❌ fail

> Do geographic regions (Hubei vs. Beihai vs. Wuhan) harbor distinct virus family compositions, suggesting regional ecological filtering?
>
> *Rationale:* Candidate concerns regional virus-family composition using assembled genomes (FASTA), aligning weakly to the gold focus on invertebrate-transcriptome-driven discovery and deep-lineage phylogenetics; well grounded to a specific FASTA file but missing key required elements.

**Rank 5** · Comp = 0.360 · ❌ fail

> Are the Astro-Poty Zucchini yellow mosaic virus and Bean yellow mosaic virus sequences phylogenetically distinct from the astro-like and poty-like viruses, indicating potential cross-family recombination?
>
> *Rationale:* Candidate is about plant-virus phylogenetics and recombination, not invertebrate-transcriptome-driven expansion of deep RNA-virus lineages; it only matches phylogeny and assembled genomes elements and is well grounded in the provided FASTA/alignments files.

### ✅ `gemini-2.5-flash` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 2 | 1 | 3 | 3 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 2 | 2 | 2 | 3 | 1.785 | 0.357 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.459 · ❌ fail

> What is the genomic diversity and average genome length of the viruses present in the `all_virus_genomes.fasta` dataset?
>
> *Rationale:* Matched to GQ_002 because it targets genome lengths in an assembled-virus FASTA; it captures some required elements but omits segmentation, architecture, and the manual curation focus, so it's a partial but concrete match grounded in the specific FASTA file.

**Rank 2** · Comp = 0.560 · ❌ fail

> How do the phylogenetic relationships inferred from the `alignments_and_phylogenies.zip` data correlate with the taxonomic classifications observed in the `all_virus_genomes.fasta` headers?
>
> *Rationale:* The candidate matches GQ_001's phylogenetic-analysis intent but omits the invertebrate and deep-lineage scope; it is well grounded in the provided files yet only partially covers required elements.

**Rank 3** · Comp = 0.400 · ❌ fail

> What are the most prevalent viral families or groups represented in the `all_virus_genomes.fasta` dataset based on the information in the sequence headers?
>
> *Rationale:* Matched to GQ_001 because the candidate concerns dataset-level viral diversity, but it only uses FASTA header annotations and omits the gold's required invertebrate/phylogenetic elements.

**Rank 4** · Comp = 0.360 · ❌ fail

> Can conserved sequence motifs or functional domains be identified across different viral genomes within the `all_virus_genomes.fasta` dataset, potentially indicating shared evolutionary origins or functional constraints?
>
> *Rationale:* The candidate centers on motif/domain discovery in a named fasta, which relates to viral evolution but misses the invertebrate-transcriptome scope, virosphere breadth, deep-lineage discovery, and phylogenetic analyses required by GQ_001.

**Rank 5** · Comp = 0.357 · ❌ fail

> Is there a significant variation in GC content among the viral genomes in `all_virus_genomes.fasta`, and does this variation correlate with specific viral groups or genome lengths?
>
> *Rationale:* The candidate uses the provided viral genome FASTA and genome lengths but asks about GC content rather than segmentation/architecture or curation, so it partially overlaps with GQ_002 but misses its main intent.

### ✅ `intern-s1` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 3 | 2 | 2 | 4 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What is the nucleotide diversity (π) across different virus families represented in the genome collection?
>
> *Rationale:* The candidate aligns with GQ_001 on studying viral diversity but is narrower—measuring within-family nucleotide diversity—covers assembled genomes and alignments, omits invertebrate-transcriptome and deep-lineage framing, and is concretely grounded in the two uploaded files.

**Rank 2** · Comp = 0.520 · ❌ fail

> How do phylogenetic relationships correlate with geographic distribution patterns of these viruses?
>
> *Rationale:* The candidate is a phylogeographic question grounded in the provided FASTA and tree files, matching GQ_001's phylogenetic element but missing key required elements about invertebrate transcriptomes and deep virosphere breadth.

**Rank 3** · Comp = 0.560 · ❌ fail

> What evidence exists for recombination events between different virus lineages?
>
> *Rationale:* Asks a phylogenetics-centered question (recombination) grounded in provided genomes/alignments, but lacks the gold's invertebrate-transcriptome and virosphere breadth emphasis, making it a partial match.

**Rank 4** · Comp = 0.323 · ❌ fail

> Which genomic regions show the highest conservation across all virus families?
>
> *Rationale:* The candidate is a genome-level conservation question and thus only partially overlaps GQ_002 (assembled genomes present) but misses core elements about segmentation and manual curation; it is grounded in the provided FASTA and alignment files.

**Rank 5** · Comp = 0.380 · ❌ fail

> How do substitution rates vary between different virus families in this collection?
>
> *Rationale:* Selected GQ_001 as the closest evolutionary/phylogenetic match despite different intent; candidate is about substitution rates, not about broad invertebrate-driven discovery of RNA-virus diversity, and only covers phylogenetic analysis with good file-level grounding.

### ✅ `intern-s1-pro` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 5 | 2 | 2 | 2 | 4 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What are the evolutionary relationships and divergence times among the Astro-Poty virus strains represented in the dataset, and which clades show evidence of recent rapid diversification?
>
> *Rationale:* The candidate aligns with the phylogenetic component of GQ_001 (assembled genomes and trees) but misses the core invertebrate-transcriptome and broad/deep virosphere framing required by the gold question.

**Rank 2** · Comp = 0.408 · ❌ fail

> Do the Astro-Poty virus genomes in this dataset show evidence of recombination events, and if so, what are the major recombination breakpoints and parental lineages?
>
> *Rationale:* Matches GQ_002 only loosely: it concerns assembled virus genomes and lengths but asks about recombination rather than segmentation/architecture/manual curation, though it is well grounded in the provided FASTA and alignment files.

**Rank 3** · Comp = 0.340 · ❌ fail

> Which functional domains and conserved motifs are present across the Astro-Poty virus genomes, and how do variations in these domains correlate with host range or pathogenicity?
>
> *Rationale:* The candidate asks about domain/motif variation across Astro-Poty genomes and correlations with host/pathogenicity, which is about functional analysis of assembled genomes but does not address segmentation, genome-length, architecture, or manual curation required by GQ_002.

**Rank 4** · Comp = 0.306 · ❌ fail

> What is the nucleotide composition bias (GC content, codon usage) across the Astro-Poty virus genomes, and does this bias correlate with geographic origin or host species?
>
> *Rationale:* Selected GQ_002 because both address genome-level questions using assembled viral FASTA data; candidate diverges by focusing on composition and host/geography correlations rather than segmentation, architecture, or curation, so coverage and intent alignment are limited.

**Rank 5** · Comp = 0.440 · ❌ fail

> How do the evolutionary rates and selective pressures (dN/dS ratios) vary across different regions of the Astro-Poty virus genomes, and which regions are under positive selection?
>
> *Rationale:* Selected GQ_001 as the best fit because the candidate is evolutionary in scope; however it targets per-gene selection (dN/dS) within Astro-Poty genomes rather than transcriptome-wide diversity, deep lineages, or redefinition of the RNA virosphere.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.680 · Pass@1=0.00 · Pass@5=0.25

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 2 | 4 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 3 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 3 | 3 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.440 · ❌ fail

> What is the phylogenetic relationship and evolutionary divergence between potyviruses (Astro-Poty) and bunyaviruses (Bunya-Arena) based on conserved RdRp gene sequences, and does geographic origin correlate with genetic clustering?
>
> *Rationale:* The candidate centers on RdRp phylogenetics and geography across two virus families, matching the phylogenetic theme of GQ_001 but missing key elements (invertebrate transcriptomes, assembled genomes, breadth/deep-lineage focus), so it's only a partial semantic match despite good file-level grounding.

**Rank 2** · Comp = 0.680 · ✅ pass

> How do genome lengths vary across different virus families (Astro-Poty, Birna, Bunya-Arena) and what does this reveal about their genomic organization and segment structure?
>
> *Rationale:* The candidate aligns well with GQ_002 by targeting genome length, segmentation and architecture using FASTA header lengths and annotated segments, covering 4 of 5 required elements; it omits explicit manual curation, so it's close to acceptable phrasing but risks resembling an overly simple 'Are viruses long or short?' question.

**Rank 3** · Comp = 0.480 · ❌ fail

> What is the geographic distribution pattern of bunyaviruses in the dataset, and are there distinct genetic clusters associated with specific host types (mosquito, insect, shrimp)?
>
> *Rationale:* The candidate is a focused, data-grounded phylogenetic question about bunyaviruses and host/geography clustering, but it does not address transcriptome-wide discovery, the breadth of the RNA virosphere, or deep-lineage redefinition required by GQ_001.

**Rank 4** · Comp = 0.272 · ❌ fail

> To what extent are conserved functional domains (RdRp, Glycoprotein, Nucleoprotein) preserved across different bunyavirus sequences, and what sequence motifs indicate functional conservation?
>
> *Rationale:* The candidate is sequence-focused and grounded to the provided genome FASTA but addresses protein-domain conservation rather than GQ_002's required elements (segmentation, architecture, manual curation), so it only partially aligns.

**Rank 5** · Comp = 0.527 · ❌ fail

> What evidence of recombination or reassortment exists among the segmented bunyavirus sequences, and how do different genome segments co-evolve within the same viral isolates?
>
> *Rationale:* The candidate aligns well with GQ_002 on segmentation and segment-level analyses using assembled fasta records but omits genome length and the explicit question of which genomes require manual curation.


## 6 · `oyster_rna_virome_2024`

- **raw**：6 文件: `40168_2024_1967_MOESM1_ESM.xlsx, 40168_2024_1967_MOESM2_ESM.xlsx, 40168_2024_1967_MOESM3_ESM.xlsx, 40168_2024_1967_MOESM4_ESM.fa...`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.940 · ✅ pass

> Which RNA virus contigs in the cultured-oyster virome — particularly Marnaviridae-like RdRps such as k141_94377, k141_179532 and k141_240998 — are simultaneously detectable at high coverage in Magallana gigas, in geographically distant M. hongkongensis populations, in unrelated freshwater and marine mollusc viromes, and in Yangshan-harbour seawater, indicating water-borne dispersal rather than host-specific replication?
>
> *Rationale:* The candidate tightly matches GQ_001 by focusing on RdRP contigs shared across oysters, other mollusks and seawater with mapped-coverage evidence and is grounded in multiple MOESM files, but it emphasizes specific Marnaviridae-like lineages rather than asking about overall virome diversity.

**Rank 2** · Comp = 0.646 · ✅ pass

> Do the 40 high-coverage 'dominant' RNA virus contigs in cultured oysters cluster into a small number of palmprint-RdRp lineages closely related to Beihai mollusk viruses, suggesting a stable core RNA virome maintained in Magallana populations across China?
>
> *Rationale:* The candidate strongly aligns with GQ_002 by focusing on abundant RdRP-bearing contigs and their geographic persistence, and is well grounded in supplied MOESM files, but it omits explicit novelty assessment and formal indicator evaluation.

**Rank 3** · Comp = 0.580 · ❌ fail

> Does the abundance and richness of Picobirnaviridae-like dsRNA contigs in oyster digestive tissue correlate with sampling season across the 16 Luchao-Port Magallana gigas batches collected between June 2016 and July 2017?
>
> *Rationale:* The candidate aligns with GQ_001's oyster metatranscriptome and read-mapping evidence but is a focused seasonality test of Picobirnaviridae and omits RdRP, broad virome diversity, and seawater-sharing elements.

**Rank 4** · Comp = 0.680 · ✅ pass

> Are the bimodal coverage distributions seen in the M. hongkongensis and seawater violins of Fig. S6 explained by replicating versus passively-filtered viral lineages, identifiable as distinct RdRp clades within the Marnaviridae and Picornavirales alignments?
>
> *Rationale:* The candidate examines RdRp clades and host–seawater sharing with concrete MOESM files, matching GQ_001's RdRp and sharing focus but diverging by using M. hongkongensis and testing replication vs passive filtering rather than the oyster-centered diverse virome question.

**Rank 5** · Comp = 0.493 · ❌ fail

> How many of the 154 RdRp ORFs in MOESM4 represent novel viral species (best BLAST identity <90% over >=80% of the query) and to which RNA viral orders do these candidate novel species disproportionately belong?
>
> *Rationale:* The candidate solidly addresses RdRP novelty using MOESM files and BLAST thresholds (strong data grounding) but misses abundance, indicator value, and marine-circulation framing required for full match to GQ_002.

### ✅ `gpt-5.5-high` — Comp=0.760 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 2 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 4 | 4 | 2 | 3 | 5 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.731 · ✅ pass

> Do the abundant RdRP-supported RNA viruses discovered in Magallana gigas, particularly Marna and Picobirna contigs, recur across M. hongkongensis, other mollusks, and Yangshan Harbor seawater in patterns consistent with broad host range and environmental circulation?
>
> *Rationale:* Matches GQ_002 well by probing abundant RdRP-bearing oyster viruses' recurrence across hosts and seawater and their indicator potential; strongly data-grounded in multiple supplemental files but fails to explicitly address novelty (novel species).

**Rank 2** · Comp = 0.527 · ❌ fail

> Which oyster RNA-virus lineages dominate the Magallana gigas virome, and are dominant contigs also the ones with near-complete genome coverage and repeated detection in M. hongkongensis libraries?
>
> *Rationale:* The candidate targets abundance and cross-host recurrence (matches GQ_002 intent partially) and is strongly grounded in specific spreadsheet columns, but omits explicit RdRP and novelty/indicator wording.

**Rank 3** · Comp = 0.760 · ✅ pass

> Are oyster RNA-virus contigs shared with other mollusks or seawater more abundant and more completely covered than contigs detected only in the Magallana gigas dataset?
>
> *Rationale:* Candidate strongly matches GQ_001's sharing and read-mapping intent, explicitly compares shared vs private contigs using TPM and coverage, but omits explicit RdRP/palm-domain and broader 'diverse virome' phrasing.

**Rank 4** · Comp = 0.660 · ✅ pass

> How much novel RNA-virus diversity in oysters is supported by RdRP motif-containing proteins and phylogenetic placement across established RNA-virus orders and families?
>
> *Rationale:* Matches GQ_001's RdRP/diversity focus and is well grounded in the ESM files and motif counts, but omits explicit digestive-tissue metatranscriptome framing, sharing/network evidence, and read-mapping support.

**Rank 5** · Comp = 0.760 · ✅ pass

> Do viral coverage profiles differ among M. hongkongensis, other mollusk, and seawater datasets in a way that distinguishes likely host-associated infections from environmental detections?
>
> *Rationale:* Aligns well with GQ_001 by using metatranscriptome coverage across M. hongkongensis, other mollusks, and seawater to infer host association (read-mapping present), but omits RdRP/palm-domain evidence and explicit 'diverse RNA virome' framing.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 4 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 5 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Do Marna-like RNA viruses shared between Magallana oyster tissue and ambient Yangshan Harbor seawater (k141_94377, k141_179532, k141_59248, k141_480947) exhibit higher per-individual TPM and covered fraction in M. hongkongensis sampled from geographically proximate coastal sites, implicating seawater as the primary transmission route for the dominant bivalve RNA virome?
>
> *Rationale:* The candidate precisely targets cross-compartment RNA viruses revealed by oyster metatranscriptomes, cites RdRP evidence and read-mapping TPMs, and proposes a geographic correlation test to evaluate seawater-driven transmission.

**Rank 2** · Comp = 0.940 · ✅ pass

> Are the two universally prevalent Picobirna-like (k141_147375) and Marna-like (k141_94377) RNA viruses detected in all 17 individual M. hongkongensis across five geographically distinct coastal South China sites associated with persistent endogenous viral elements or represent horizontally circulating infections, as evidenced by the extremely high and geographically variable per-individual TPM (ranging from 64 to 894,639)?
>
> *Rationale:* The candidate precisely tests whether two prevalent RdRP contigs reflect horizontal circulation vs endogenous elements using per-sample TPM, geographic sampling, BLASTP identities, and cross-host detection—matching GQ_001's metatranscriptome + sharing focus but not addressing overall virome diversity.

**Rank 3** · Comp = 0.731 · ✅ pass

> Do the 42 oyster RNA viral contigs with <50% RdRP amino-acid identity to any known virus (from MOESM3 BLASTP results) represent novel species within established families (Marna, Picobirna, Noda, Tombus) that are host-restricted to Magallana oysters rather than shared with other mollusks or seawater, suggesting these marine bivalves harbor a substantial undescribed private RNA virome?
>
> *Rationale:* Strong semantic match to GQ_002: explicit RdRP novelty and host-restriction testing with concrete MOESM2/MOESM3 evidence; misses explicit framing of indicator use but is well grounded and acceptable.

**Rank 4** · Comp = 0.520 · ❌ fail

> Does the RNA virome composition of temporally replicated Magallana gigas (16 batches sampled Jun 2016–Jul 2017, n=173 individuals, Luchao Port) differ seasonally in viral family richness or Marna-to-Picobirna abundance ratio, suggesting that temperature or reproductive stage drives shifts in the dominant oyster RNA virome community?
>
> *Rationale:* Matched to GQ_001 because both target oyster RNA viromes; the candidate robustly tests seasonal shifts in family richness and Marna:Picobirna ratios and is well-grounded in MOESM1/MOESM2, but it omits RdRP/palm-domain, tissue-specific metatranscriptome framing, and sharing/network evidence required by GQ_001.

**Rank 5** · Comp = 0.680 · ✅ pass

> Do the dominant Marna-like RNA viruses detected across M. hongkongensis, other mollusks (Bivalva, Gastropoda, Octopodidae), and seawater show phylogenetic clustering by host class rather than by geographic origin, indicating host-specific evolutionary pressures that constrain cross-class transmission despite their presence in shared coastal marine environments?
>
> *Rationale:* The candidate is a well-grounded, RdRP-focused test of host vs geographic phylogenetic signal that fits GQ_001's sharing/network intent but narrows scope (phylogeny over broad virome diversity) and omits explicit 'digestive-tissue' wording.

### ✅ `gemini-3.1-pro` — Comp=0.323 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 2 | 3 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What novel functional domains or metabolic pathways can be identified from the predicted protein sequences in the assembled contigs, and how do they contribute to the ecological adaptation of the sampled community?
>
> *Rationale:* GQ_001 was chosen as the closest gold, but the candidate targets general functional annotation of predicted proteins (FASTA) and ecological adaptation rather than oyster metatranscriptome RdRPs, virus-sharing, or read-mapping evidence, so it fails to cover required elements despite being grounded in a specific file.

**Rank 2** · Comp = 0.180 · ❌ fail

> Are there specific protein families or domains within the assembled contigs that are significantly enriched or unique to this dataset compared to known reference databases?
>
> *Rationale:* The candidate is a general protein-domain enrichment question (references a FASTA file) and lacks any mention of oysters, RdRP/viral markers, virome diversity, or sharing/read-mapping evidence, so it does not match the gold virome/sharing question.

**Rank 3** · Comp = 0.220 · ❌ fail

> What is the taxonomic origin and diversity of the organisms contributing to the protein sequences found in the assembled contigs?
>
> *Rationale:* The candidate is a general taxonomic-profiling question about contig-derived proteins (MOESM4.fa) and does not address oyster RNA viromes, RdRP detection, or host–seawater sharing, so it poorly matches the gold virome/network question.

**Rank 4** · Comp = 0.140 · ❌ fail

> Can we identify potential antimicrobial resistance (AMR) genes or virulence factors among the predicted protein sequences in the dataset?
>
> *Rationale:* The candidate is about AMR/virulence screening of predicted proteins in a .fa file and does not address any of the oyster-RdRP-seawater virome elements in GQ_001; it is concrete about the file but semantically unrelated.

**Rank 5** · Comp = 0.323 · ❌ fail

> Do the supplementary Excel files provide metadata or quantitative data that correlates with the presence or abundance of specific protein sequences found in the FASTA file?
>
> *Rationale:* The candidate is a file-level data-integration question that addresses abundance in FASTA-linked proteins (weakly overlapping GQ_002's abundance element) but omits RdRP, novelty, indicator value, and marine-circulation context, so alignment is low.

### ✅ `deepseek-v4-pro` — Comp=0.460 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.460 · ❌ fail

> Do RNA virus clades in sample k141 exhibit statistically significant co-abundance patterns with specific DNA bacteriophage groups, and can these associations be linked to predicted bacterial host phyla using the host-prediction data in MOESM3?
>
> *Rationale:* Candidate fits the network/read-mapping aspect and references RdRp and MOESM files, but it lacks the oyster/mollusk context and explicit claim of a diverse oyster RNA virome, so it only partially matches GQ_001.

**Rank 2** · Comp = 0.408 · ❌ fail

> What proportion of the RNA-dependent RNA polymerase (RdRp) sequences recovered from sample k141 represent novel clades that cannot be assigned to established orthornaviran families, and do these unassigned sequences carry unique structural motifs absent from reference genomes?
>
> *Rationale:* Candidate fits GQ_002's novelty+RdRP theme but omits abundance/indicator/marine-circulation elements; it is well grounded in MOESM4/MOESM1/MOESM5 and closest to the acceptable novel-RdRP variant while also resembling the unacceptable generic 'Are there many novel viruses?'.

**Rank 3** · Comp = 0.120 · ❌ fail

> Are bacteriophage-encoded auxiliary metabolic genes (AMGs) in sample k141 preferentially associated with specific bacterial host phyla, and does AMG abundance correlate with predicted host metabolic pathway completeness as inferred from MOESM3?
>
> *Rationale:* The candidate studies bacteriophage AMGs and host phyla using MOESM2–4 files (k141), which is semantically unrelated to GQ_001's focus on oyster digestive-tissue RNA viromes, RdRP evidence, and mollusk–seawater sharing; none of GQ_001's required elements are present.

**Rank 4** · Comp = 0.300 · ❌ fail

> Does the genome length distribution of assembled viral contigs in sample k141 differ significantly between RNA virus and DNA bacteriophage populations, and is RNA virus genome recovery completeness systematically lower as suggested by truncated polyproteins in MOESM4?
>
> *Rationale:* The candidate is a different, assembly-completeness question grounded in MOESM files and RNA vs phage contigs; it only overlaps the gold via 'RNA virome' and lacks oyster/RdRP/sharing elements, so it scores low on semantic match but high on data grounding.

**Rank 5** · Comp = 0.380 · ❌ fail

> Can the viral populations in sample k141 be partitioned into distinct ecological modules based on tetranucleotide frequency and codon usage patterns of their assembled contigs, and do these modules correspond to different host-derived niches as annotated in MOESM3?
>
> *Rationale:* The candidate addresses viral composition and host-assignment clustering (MOESM3/MOESM4) which overlaps the virome/host-sharing theme, but it omits oyster-specific samples, RdRP-based viral evidence, and seawater-sharing/read-mapping network elements required by GQ_001.

### ✅ `glm-5` — Comp=0.357 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.240 · ❌ fail

> What is the functional diversity and taxonomic distribution of protein-coding genes across the metagenomic contigs, and how do specific protein families correlate with ecological niches?
>
> *Rationale:* The candidate addresses metagenomic functional/taxonomic profiling (well grounded in MOESM files) but does not target oysters, RNA viromes, RdRP sequences, or host–seawater sharing required by the matched gold, so semantic alignment is minimal.

**Rank 2** · Comp = 0.120 · ❌ fail

> Which metabolic pathways are most abundantly represented in the metagenomic dataset, and do specific pathways show enrichment in particular contig clusters?
>
> *Rationale:* The candidate addresses metabolic pathway abundance/enrichment in metagenomic contigs (FASTA + Excel) which is unrelated to GQ_001's oyster RNA-virome and RdRP/shared-virus focus; data grounding is specific but virology-required elements are absent.

**Rank 3** · Comp = 0.357 · ❌ fail

> What proportion of the metagenomic proteins represent novel sequences with low homology to known protein families, and how does this vary across different contig assemblies?
>
> *Rationale:* The candidate focuses on novelty of proteins across contig assemblies (overlapping GQ_002's novelty theme) but omits RdRP, abundance, indicator value and marine-circulation context, though it is grounded to specific provided files.

**Rank 4** · Comp = 0.120 · ❌ fail

> How does the protein sequence length distribution and domain architecture vary across different functional categories in the metagenomic dataset?
>
> *Rationale:* The candidate concerns protein length/domain distributions in a FASTA/Excel, which is unrelated to oyster RNA‑virome/RdRP questions; it does, however, reference specific available files.

**Rank 5** · Comp = 0.120 · ❌ fail

> Are there distinct clusters of co-occurring protein families that suggest functional modules or metabolic networks within the microbial community?
>
> *Rationale:* The candidate addresses protein-family co-occurrence and metabolic modules using FASTA/Excel files, not oyster RNA viromes, RdRP sequences, or host–seawater virus sharing; it has strong data-file grounding but none of the gold's required virology elements.

### ✅ `gemini-2.5-flash` — Comp=0.380 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 2 | 0.800 | 0.160 | ❌ | GQ_001 (P) |
| 4 | 2 | 0 | 2 | 4 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 2 | 0.800 | 0.160 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.240 · ❌ fail

> What are the functional annotations and evolutionary relationships of the sequences provided in the FASTA file, and how do these relate to the experimental data in the spreadsheets?
>
> *Rationale:* The candidate is a generic sequence-analysis question grounded in specific files but omits all GQ_001-specific elements (oysters, RdRPs, virome sharing), so it poorly matches the gold intent despite good data grounding.

**Rank 2** · Comp = 0.380 · ❌ fail

> Do the quantitative data in the Excel spreadsheets reveal significant differences or patterns across experimental conditions or sample groups, and how do these patterns relate to the identified sequences?
>
> *Rationale:* The candidate is a general statistical question about spreadsheets and sequences that is grounded in specific files but misses key GQ_001 elements (oysters, RdRP, virome diversity, mollusk–seawater sharing), yielding low match and required-element coverage but strong data grounding.

**Rank 3** · Comp = 0.160 · ❌ fail

> What is the overall genomic or transcriptomic landscape represented by the sequences in the FASTA file, and what insights can be gained about the organism or system under study?
>
> *Rationale:* The candidate is a generic assembly/landscape question about a FASTA file and lacks the virome-, RdRP-, oyster- and seawater-specific elements required by GQ_001, though it does reference the specific FASTA file.

**Rank 4** · Comp = 0.320 · ❌ fail

> Can the image file (`.jpg`) provide visual evidence or context that supports or contradicts the findings from the sequence and spreadsheet data?
>
> *Rationale:* The candidate asks about whether an included .jpg can corroborate sequence/spreadsheet results, which is a data-integration question grounded in specific files but misses all virology-specific elements (oyster metatranscriptomes, RdRPs, sharing/network evidence) central to GQ_001.

**Rank 5** · Comp = 0.160 · ❌ fail

> What additional information or raw data might be contained within the compressed archive (`.zip`) that could further enhance the understanding of the study presented by the other files?
>
> *Rationale:* The candidate is a dataset/metadata query about a ZIP archive (40168_2024_1967_MOESM5_ESM.zip) and does not address the virome/RdRP/sharing scientific questions in GQ_001, so alignment and required-element coverage are minimal.

### ✅ `intern-s1` — Comp=0.200 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.200 · ❌ fail

> What conserved protein motifs are present in the FASTA sequences, and how do they correlate with functional annotations in the Excel datasets?
>
> *Rationale:* The candidate concerns motif discovery in provided FASTA/Excel files (sequence→annotation correlation) and does not address the oyster RNA-virome, RdRP identification, or host–seawater sharing required by GQ_001, so semantic alignment is minimal.

**Rank 2** · Comp = 0.120 · ❌ fail

> Do protein sequences show differential expression patterns across experimental conditions in the Excel datasets?
>
> *Rationale:* The candidate asks about protein differential expression in Excel files, which is unrelated to GQ_001's oyster metatranscriptome and RNA virome focus; it does, however, cite two specific Excel files from the provided dataset.

**Rank 3** · Comp = 0.120 · ❌ fail

> Is there a correlation between protein sequence length and expression level in the datasets?
>
> *Rationale:* The candidate poses an unrelated analysis (sequence length vs expression) that is well grounded in provided files but does not address any of the oyster/RdRP/virus-sharing requirements of the matched gold question.

**Rank 4** · Comp = 0.120 · ❌ fail

> Are specific functional categories overrepresented in the protein sequences compared to background datasets?
>
> *Rationale:* The candidate asks an orthogonal question (GO enrichment of protein sequences) and cites specific files, so it is well grounded in data but has no semantic overlap with the oyster RNA‑virome focus of the matched gold question.

**Rank 5** · Comp = 0.100 · ❌ fail

> Do the protein sequences show evolutionary conservation with homologs in other species?
>
> *Rationale:* The candidate concerns general protein homology from a FASTA file and BLASTP, which does not address oyster metatranscriptomes, RNA virus RdRPs, abundance/indicator value, or virus-sharing networks, so it is unrelated to GQ_001.

### ✅ `intern-s1-pro` — Comp=0.460 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.460 · ❌ fail

> What novel viral lineages and functional protein families can be identified from the metagenomic assembly, and how do their domain architectures and sequence conservation patterns inform their evolutionary relationships and potential host interactions?
>
> *Rationale:* The candidate addresses viral lineage discovery and domain-based evolutionary inference but omits oyster/metatranscriptome context, RdRP focus, and sharing/network evidence, so it partially matches GQ_001's intent while being data-grounded in supplied FASTA/XLSX files.

**Rank 2** · Comp = 0.240 · ❌ fail

> How do the transmembrane domain distributions and membrane protein topologies in these contigs correlate with their predicted subcellular localization and potential roles in host membrane remodeling during viral infection?
>
> *Rationale:* The candidate is focused on membrane-protein features in contigs (TM domains, topology) with concrete file references, which is biologically relevant but semantically divergent from GQ_001's virome/diversity and RdRP/sharing network focus, so it scores low on intent match and misses all required elements.

**Rank 3** · Comp = 0.120 · ❌ fail

> What ATP-binding and enzymatic motifs are present across these protein sequences, and how do they suggest novel enzymatic activities or metabolic pathways that could be exploited for biotechnological applications?
>
> *Rationale:* The candidate is about ATP-binding/enzymatic motifs and biotech potential in protein sequences, which does not address the oyster-RNA-virome/RdRP sharing intent of the matched gold question.

**Rank 4** · Comp = 0.240 · ❌ fail

> To what extent do the protein sequences from this metagenomic assembly share homology with known viral proteins in public databases, and what does this reveal about the geographic distribution and host range of these viral communities?
>
> *Rationale:* Candidate addresses viral sequence homology and biogeography but omits the oyster-specific metatranscriptome focus, RdRP markers, and network/read-mapping evidence required by GQ_001.

**Rank 5** · Comp = 0.240 · ❌ fail

> How do the GC content and codon usage patterns across these contigs reflect their evolutionary adaptation to specific host organisms and environmental conditions?
>
> *Rationale:* The candidate addresses sequence composition (GC/codon usage) of contigs and is grounded in specific FASTA/XLS files, but it does not ask about oysters, RNA virome, RdRP, sharing, or mapping required by GQ_001.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.153 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 3 | 0 | 1 | 1 | 3 | 0.680 | 0.136 | ❌ | GQ_002 (S) |
| 4 | 0 | 1 | 1 | 4 | 0.765 | 0.153 | ❌ | GQ_002 (S) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What is the diversity and phylogenetic distribution of ABC transporter nucleotide-binding domains in this metagenomic protein assembly, and what does this reveal about the community's capacity for active transport?
>
> *Rationale:* The candidate is about ABC transporter domains in a metagenomic assembly (no viruses, oysters, or RdRPs), so it does not match GQ_001's virome/network intent despite grounding to MOESM4_ESM.fa.

**Rank 2** · Comp = 0.060 · ❌ fail

> How many complete ABC transporter systems (with both nucleotide-binding and transmembrane domains) are present in this assembly, and what substrates might they transport based on domain architecture?
>
> *Rationale:* The candidate concerns ABC transporters in an assembly and substrate prediction, which does not match any virus/metatranscriptome gold intents; it is nonetheless grounded in a listed FASTA file.

**Rank 3** · Comp = 0.136 · ❌ fail

> What is the relative abundance and distribution of different ABC transporter subfamilies (e.g., importers vs exporters) in this metagenomic assembly?
>
> *Rationale:* The question concerns ABC transporter subfamily abundance in a metagenomic assembly and is unrelated to RdRP-bearing oyster viruses; it only overlaps the gold question on the single concept of 'abundance' and references one supplied FASTA file.

**Rank 4** · Comp = 0.153 · ❌ fail

> Are there novel or divergent ABC transporter variants in this assembly that differ from known transporter families in reference databases?
>
> *Rationale:* The candidate concerns novel ABC transporter variants in an assembly (not RdRP viruses), so it fails to match the marine RdRP/indicator intent of GQ_002; it only overlaps on 'novelty' but is otherwise unaligned though grounded to a specific FASTA file.

**Rank 5** · Comp = 0.100 · ❌ fail

> How do the identified protein sequences in this assembly compare to known metabolic pathways, and what functional capabilities do they suggest for the microbial community?
>
> *Rationale:* The candidate addresses protein functional annotation and metabolic pathways from an assembly/FASTA, which is unrelated to the gold question's focus on oyster RNA viromes, RdRP sequences, and host–seawater virus sharing; it shows concrete grounding in one provided FASTA file but covers none of the required virome elements.


## 7 · `rvmt_cell_2022`

- **raw**：1 文件: `RVMT_Zenodo_V4.zip.remote.json`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.800 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 3 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 3 | 2 | 2 | 4 | 2.600 | 0.520 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.800 · ✅ pass

> Across the RVMT V4 global RNA virome catalogue, do the newly recovered RdRp-defined Orthornavirae phylum-level lineages exhibit habitat-specific (e.g., marine, soil, gut, freshwater) host-range and genome-architecture signatures that predict their eukaryotic host taxa, and which previously unrecognized lineages constitute candidate zoonotic or agricultural reservoirs?
>
> *Rationale:* Matches GQ_001 on global RdRp-based discovery and host association but diverges by focusing on eukaryotic host prediction and zoonotic/agricultural reservoirs rather than RNA bacteriophage clades.

**Rank 2** · Comp = 0.760 · ✅ pass

> Within the RVMT V4 catalogue, how does RNA-dependent RNA polymerase (RdRp) sequence and structural diversity scale with sampling effort across biomes, and at what point does rarefaction indicate saturation of Earth's detectable RNA-virus phylum-level diversity?
>
> *Rationale:* The candidate closely matches the gold's RdRp-driven global diversity intent and is well grounded in the RVMT V4 data, but it omits phage-clade discovery and host-association evidence required by the gold question.

**Rank 3** · Comp = 0.425 · ❌ fail

> Do RNA viruses in the RVMT V4 catalogue show systematic, clade-specific differences in genome segmentation, ORF architecture, and codon-usage bias that correlate with predicted host kingdom (animal, plant, fungal, protist) and could be used as machine-learning features for automated host assignment of unclassified contigs?
>
> *Rationale:* Mapped to GQ_002 because both ask whether sequence/gene signals can support host assignments; the candidate focuses on kingdom-level ML features (ORF/codon/segmentation) and is grounded in RVMT V4 data but omits CRISPR and prokaryotic/RNA-phage-specific evidence.

**Rank 4** · Comp = 0.560 · ❌ fail

> Which RVMT V4 RdRp lineages show evidence of recombination or horizontal gene transfer between divergent phyla (e.g., Lenarviricota, Pisuviricota, Kitrinoviricota), and does the rate of such inter-phylum exchange differ between aquatic and terrestrial biomes?
>
> *Rationale:* The candidate aligns with RdRp-driven, metatranscriptome-centered virome analysis (GQ_001) but shifts focus to recombination/HGT and biome differences instead of asking about virome expansion or RNA phage discovery.

**Rank 5** · Comp = 0.520 · ❌ fail

> Do RVMT V4 contigs assigned to Lenarviricota-like and other novel phylum-level lineages carry auxiliary metabolic genes (AMGs) suggestive of viral manipulation of host carbon or nitrogen cycling, and is AMG content enriched in marine versus host-associated metatranscriptomes?
>
> *Rationale:* The candidate is related to discovery in RVMT metatranscriptomes (novel lineages) but shifts focus to AMGs and biome enrichment rather than RdRP-driven expansion or explicit RNA-phage host evidence, so it partially matches GQ_001 but misses core required elements.

### ✅ `gpt-5.5-high` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.80

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 4 | 5 | 4 | 4.200 | 0.840 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 4 | 3 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 4 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Do the RVMT metatranscriptomic contigs reveal previously unrecognized prokaryote-infecting RNA virus lineages, including bacteriophage-like picobirnaviruses and partitiviruses, when RdRP phylogeny, CRISPR spacer matches, and bacteriolytic protein domains are analyzed together?
>
> *Rationale:* The candidate precisely targets host association for candidate RNA-phage clades using CRISPR spacers and gene-content (bacteriolytic domains), is grounded in RVMT data/files, and thus maps strongly to GQ_002.

**Rank 2** · Comp = 0.840 · ✅ pass

> How does adding more than 330,000 RVMT RdRP sequences from 5,150 metatranscriptomes change the inferred deep taxonomy of Riboviria, including support for two putative additional bacteriophage phyla?
>
> *Rationale:* Strong match to GQ_001: RdRP-centered, large-scale metatranscriptome expansion and bacteriophage phyla focus with concrete dataset counts; missing explicit host-association (CRISPR/gene-content) evidence.

**Rank 3** · Comp = 0.493 · ❌ fail

> Which protein-domain innovations in RVMT RNA virus ORFs are most strongly associated with inferred virus-host interactions across the expanded global RNA virome?
>
> *Rationale:* The candidate asks about gene-content (protein-domain) signals linked to host interactions, which aligns with GQ_002's focus on gene-content host-association evidence but omits CRISPR and explicit prokaryotic-host framing.

**Rank 4** · Comp = 0.800 · ✅ pass

> Does the greatly expanded RVMT sampling show that Lenarviricota dominates RNA virus diversity across metatranscriptomes, and which RdRP or gene-content features distinguish its bacterial and eukaryotic-associated members?
>
> *Rationale:* The candidate closely aligns with GQ_001 by using RdRP and gene-content evidence to evaluate host-associated RNA-phage lineages (focused on Lenarviricota), but it omits asking about a broad multi-fold expansion of the global RNA virome.

**Rank 5** · Comp = 0.760 · ✅ pass

> How much previously hidden RNA virus diversity is recovered per metatranscriptome in the RVMT archive, and does novelty concentrate in particular RdRP clades or annotated functional groups?
>
> *Rationale:* The candidate matches GQ_001's virome-expansion and RdRP-focused intent with strong data grounding and per-sample yield emphasis, but it omits explicit RNA-phage and host-association elements required by the gold question.

### ✅ `claude-code-sonnet-4-6` — Comp=0.580 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 3 | 2 | 3 | 2 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 4 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.460 · ❌ fail

> Does RNA-dependent RNA polymerase (RdRp) sequence divergence within recognized RNA virus genera in the RVMT V4 dataset predict cross-habitat host-range breadth, such that genera with higher within-genus amino-acid identity variance span more distinct ecological biomes?
>
> *Rationale:* The candidate shares dataset and RdRp-methodology with GQ_001 but addresses a different scientific aim (ecological breadth vs. virome expansion/RNA-phage discovery), hence a partial semantic match with strong dataset grounding.

**Rank 2** · Comp = 0.460 · ❌ fail

> Are RNA viruses recovered from geographically under-sampled regions (Africa, South America, Southeast Asia) in the RVMT V4 dataset disproportionately unclassified at the family level, indicating that current RNA virome diversity estimates are geographically biased?
>
> *Rationale:* Mapped to GQ_001 because it concerns global metatranscriptome-derived RNA-virus diversity, but it targets geographic classification bias rather than RdRP mining, phage discovery, or host-evidence; strong dataset grounding but only partial required-element coverage.

**Rank 3** · Comp = 0.520 · ❌ fail

> Do RNA viruses in the RVMT V4 dataset that infect invertebrate hosts show significantly higher rates of cross-kingdom host-range overlap (also detected in plant or fungal metagenomes) compared to RNA viruses restricted to vertebrate hosts, consistent with invertebrates serving as evolutionary bridges for inter-kingdom viral transfer?
>
> *Rationale:* The candidate aligns with GQ_001's dataset/RdRP/host-association context but focuses on cross-kingdom host-range and an invertebrate-bridge hypothesis rather than on demonstrating a multi-fold expansion of diversity or discovering RNA bacteriophage clades, so it is a partial semantic match.

**Rank 4** · Comp = 0.380 · ❌ fail

> Does the RVMT V4 dataset reveal a latitudinal diversity gradient in RNA virus richness across environmental metagenomes, analogous to the patterns documented for macro-organisms, with peak diversity in tropical biomes?
>
> *Rationale:* The candidate addresses biogeographic patterns in the RVMT V4 metatranscriptomes (matching the global-metatranscriptome theme of GQ_001) but does not pursue RdRP mining, virome expansion, or RNA phage/host discovery, so semantic alignment is weak despite strong dataset grounding.

**Rank 5** · Comp = 0.580 · ❌ fail

> Can the completeness scores and RdRp phylogenetic placement of RVMT V4 sequences be used to identify RNA virus clades with disproportionately large genomic dark matter (incomplete, phylogenetically isolated sequences), indicating lineages most likely to harbor undiscovered replication strategies?
>
> *Rationale:* The candidate aligns with GQ_001 via RdRp-based analysis of a metatranscriptome dataset (RVMT V4) but lacks explicit questions about overall virome expansion, RNA phage clades, and host-association evidence.

### ✅ `gemini-3.1-pro` — Comp=0.540 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 3 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.540 · ❌ fail

> What are the universal genomic signatures of host adaptation across diverse RNA virus families represented in the RVMT dataset?
>
> *Rationale:* The candidate focuses on host-adaptation signatures in the RVMT metatranscriptome dataset, so it aligns partially with GQ_001's host-association aim but omits RdRP-based mining and RNA-phage discovery required by that gold question.

**Rank 2** · Comp = 0.180 · ❌ fail

> How do mutation rates vary across different viral taxonomic groups within the RVMT dataset?
>
> *Rationale:* The candidate concerns evolutionary rate comparisons within the RVMT data, which is related to viral genomics but does not address metatranscriptome RdRP mining, RNA-phage discovery, or host-association evidence required by GQ_001.

**Rank 3** · Comp = 0.280 · ❌ fail

> Are there specific structural constraints on RNA viral genomes that limit their evolutionary trajectories?
>
> *Rationale:* The candidate concerns RNA genome structural constraints and uses the RVMT dataset, which relates broadly to RNA virome research but omits core elements of GQ_001 (metatranscriptome mining, RdRPs, phage/host evidence), so the semantic match is low.

**Rank 4** · Comp = 0.180 · ❌ fail

> What is the frequency and distribution of recombination events among the RNA viruses in this dataset?
>
> *Rationale:* The candidate addresses recombination in RNA viruses (a different, narrower evolutionary question) and is grounded to a specific RVMT_Zenodo_V4 file, but it fails to include any required elements of the matched gold question about metatranscriptome-wide RdRP mining and RNA phage discovery.

**Rank 5** · Comp = 0.280 · ❌ fail

> Can the metadata in the RVMT dataset be used to predict the emergence of novel viral lineages with pandemic potential?
>
> *Rationale:* The candidate concerns predictive epidemiology using RVMT metadata rather than RdRP-based discovery or RNA-phage host evidence; it references the RVMT file but omits most GQ_001 required elements and differs substantially in scientific intent.

### ✅ `deepseek-v4-pro` — Comp=0.280 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What climatological and anthropogenic land-use variables best predict the spatial expansion rate of Rift Valley fever virus lineages across East Africa between 2000 and 2023, as inferred from the RVMT genomic and metadata archive?
>
> *Rationale:* The candidate addresses RVF phylogeography and environmental drivers using the RVMT archive (2000–2023), which is semantically unrelated to GQ_001's RdRP-driven global metatranscriptome RNA-virome expansion and RNA-phage discovery; it has no required elements but is grounded to the named RVMT file.

**Rank 2** · Comp = 0.280 · ❌ fail

> Do Rift Valley fever virus lineages circulating in livestock populations exhibit distinct nucleotide substitution rates compared to those sampled from human clinical cases, and does this difference correlate with host immune pressure?
>
> *Rationale:* The candidate focuses on host-specific evolutionary rates for RVFV using the RVMT archive, which touches the dataset domain of GQ_001 but does not address RNA‑virome expansion, RdRP mining, or RNA phage discovery.

**Rank 3** · Comp = 0.100 · ❌ fail

> Can periods of intense RVFV circulation in livestock be detected retrospectively from the shape of the viral phylogeny's lineage-through-time curve before human outbreak reports appear?
>
> *Rationale:* The candidate is a focused RVFV phylodynamics/surveillance question tied to a specific RVMT file and LTT changepoint detection, which is semantically unrelated to the gold's metatranscriptome/RdRP-driven RNA virome expansion goals.

**Rank 4** · Comp = 0.100 · ❌ fail

> What is the contribution of wind-borne mosquito dispersal versus livestock trade networks to the long-distance dissemination of Rift Valley fever virus genotypes across the African continent?
>
> *Rationale:* The candidate addresses RVFV phylogeography and transmission drivers, which is a different epidemiological question and does not meet any of GQ_001's required elements, though it does reference a specific dataset file.

**Rank 5** · Comp = 0.180 · ❌ fail

> Does the genetic diversity of Rift Valley fever virus within a single outbreak locality predict the probability of that locality serving as a source for subsequent regional spread in the following transmission season?
>
> *Rationale:* The candidate concerns RVFV outbreak genetic diversity predicting seasonal source status—an epidemiological phylodynamic question—whereas the matched gold is about global metatranscriptome RdRP mining for RNA-virus and RNA-phage discovery, so semantic overlap is minimal.

### ✅ `glm-5` — Comp=0.240 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What temporal patterns and trends can be identified across the four versions of the RVMT dataset, and how do they reflect changes in data collection methodology or underlying phenomena?
>
> *Rationale:* The candidate is a dataset-version and methodology-trends question grounded to RVMT_Zenodo_V4, but it does not address RdRP mining, RNA-virus diversity expansion, RNA phage clades, or host-association evidence required by GQ_001, so semantic match is nil despite concrete file grounding.

**Rank 2** · Comp = 0.120 · ❌ fail

> What is the scientific domain and primary research application of the RVMT dataset based on its naming convention, size, and repository metadata?
>
> *Rationale:* The candidate is a metadata/domain-identification question about an RVMT Zenodo dataset and does not address GQ_001's scientific intent about mining metatranscriptomes and discovering RNA phages.

**Rank 3** · Comp = 0.240 · ❌ fail

> How does the data volume and structure of RVMT_Zenodo_V4.zip compare to typical datasets in its scientific domain, and what does this indicate about its comprehensiveness?
>
> *Rationale:* The candidate is a dataset-comprehensiveness question about a specific 9.4 GB archive and does not address RdRP mining, RNA-virus diversity expansion, RNA phage clades, or host-association evidence required by the matched gold question.

**Rank 4** · Comp = 0.120 · ❌ fail

> What quality assurance indicators are embedded in the RVMT dataset versioning history, and how do they support reproducible scientific research?
>
> *Rationale:* The candidate is about dataset QA/versioning and reproducibility for RVMT Zenodo V4 (checksums, changelog), which does not address GQ_001's virome discovery, RdRP mining, or host-evidence requirements.

**Rank 5** · Comp = 0.120 · ❌ fail

> What machine learning or statistical analysis opportunities does the RVMT dataset's scale and structure enable for predictive modeling applications?
>
> *Rationale:* The candidate addresses dataset-scale ML opportunities for RVMT and not the core scientific question of RdRP-driven metatranscriptome mining or RNA-phage host evidence, so it is a poor semantic match despite concrete dataset grounding.

### ✅ `gemini-2.5-flash` — Comp=0.260 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 2 | 2 | 1.300 | 0.260 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 2 | 1.000 | 0.200 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.260 · ❌ fail

> What are the primary data types and their statistical distributions within the RVMT dataset, and do these distributions reveal any initial insights into the underlying phenomena?
>
> *Rationale:* The candidate is a generic dataset-characterization question that only marginally aligns with GQ_001 via the RVMT metatranscriptome archive; it omits core scientific aims (RdRP mining, RNA-phage discovery, host-evidence) and cites one specific file but no detailed data features.

**Rank 2** · Comp = 0.200 · ❌ fail

> Are there discernible relationships or correlations between different variables or data components present in the RVMT archive that could suggest underlying scientific principles?
>
> *Rationale:* The candidate is a generic data-relationships question grounded to one archive file, not addressing the specific RNA-virus/RdRP/host-association aims of the matched gold, so it poorly matches GQ_001's intent.

**Rank 3** · Comp = 0.100 · ❌ fail

> Does the RVMT dataset contain temporal or spatial information, and if so, do these dimensions reveal any significant patterns, trends, or anomalies?
>
> *Rationale:* The candidate concerns temporal/spatial metadata in a specific RVMT Zenodo JSON file, which is unrelated to the GQ_001 focus on RdRP-driven RNA-virus discovery and RNA phage host evidence.

**Rank 4** · Comp = 0.240 · ❌ fail

> Can the data within the RVMT archive be utilized to develop a predictive model for a specific outcome or classification task, and what is the potential accuracy of such a model?
>
> *Rationale:* The candidate asks about ML on the RVMT archive rather than RNA‑virome discovery via RdRP mining; it only covers the dataset element ('global metatranscriptomes'), so it aligns poorly with GQ_001's intent and is closer to unacceptable generic variants.

**Rank 5** · Comp = 0.060 · ❌ fail

> What is the internal structure and organization of the `RVMT_Zenodo_V4.zip` archive, including file formats, directory hierarchy, and metadata conventions?
>
> *Rationale:* The candidate is a metadata/data-organization query unrelated to the virome-discovery aims of GQ_001; it has no required scientific elements, though it is grounded in the specific provided file.

### ✅ `intern-s1` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 1 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 1 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> How does vehicle speed correlate with fuel efficiency under different load conditions?
>
> *Rationale:* The candidate addresses vehicle speed and fuel efficiency, which is unrelated to RNA virome mining; it contains no virology-specific elements and only a generic dataset mention, so it does not match the gold question.

**Rank 2** · Comp = 0.060 · ❌ fail

> What is the impact of engine temperature on emission levels during urban driving cycles?
>
> *Rationale:* The candidate concerns engine temperature and urban emissions, a domain wholly unrelated to the RNA virome/CRISPR gold questions, so it matches none of the required elements and has minimal grounding in the provided dataset.

**Rank 3** · Comp = 0.080 · ❌ fail

> How do different driving styles (aggressive vs. eco-driving) affect overall energy consumption?
>
> *Rationale:* The candidate question is about driving styles and energy usage, unrelated to RNA virome mining; it contains no required virology elements, references one dataset file generically, and therefore scores zero on match and required-elements coverage with low acceptability and modest data grounding.

**Rank 4** · Comp = 0.060 · ❌ fail

> Can predictive maintenance alerts be optimized using real-time sensor data patterns?
>
> *Rationale:* The candidate concerns predictive maintenance on sensor data, which is unrelated to RNA virome mining; no required viromics elements are present, grounding is only a vague file reference, and framing is not aligned with acceptable variants.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the relationship between ambient temperature and battery performance in hybrid vehicles?
>
> *Rationale:* The candidate is unrelated to the matched gold (RNA virome) and contains none of the required virology elements; it mentions concrete sensor measures and a file but lacks confirmation those fields exist in the provided dataset.

### ✅ `intern-s1-pro` — Comp=0.323 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 4 | 2 | 1 | 1 | 3 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.300 · ❌ fail

> What is the geographic distribution and evolutionary trajectory of RVMT viral strains across different host species and environmental reservoirs based on genomic sequence variation?
>
> *Rationale:* Candidate addresses phylogeography and evolution of RVMT strains (host/geography/sequence) but does not engage the gold's metatranscriptome/RdRP-driven discovery or RNA-phage focus, so match is low though data grounding is specific.

**Rank 2** · Comp = 0.323 · ❌ fail

> How does genetic diversity of RVMT correlate with host species specificity and transmission efficiency in different ecological zones?
>
> *Rationale:* The candidate concerns host-associated genetic signals but lacks GQ_002's required CRISPR/gene-content evidence and explicit focus on prokaryotic RNA-phage clades, though it is well grounded in the named RVMT dataset and metadata.

**Rank 3** · Comp = 0.240 · ❌ fail

> What are the recombination patterns and reassortment events in RVMT populations, and how do they contribute to viral evolution and emergence?
>
> *Rationale:* The candidate addresses recombination in a specific RVMT dataset, which is a different scientific question than GQ_001's focus on global metatranscriptome RdRP mining and RNA-phage discovery, so match is weak though data grounding is specific.

**Rank 4** · Comp = 0.320 · ❌ fail

> Can environmental factors predict the presence and abundance of RVMT in different geographic regions based on metagenomic surveillance data?
>
> *Rationale:* Matched to GQ_001 because of shared viral surveillance/metatranscriptome topic; however the candidate focuses on environmental predictors not RdRP-based discovery or RNA-phage clade evidence, so coverage of required elements is minimal and acceptability is low.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the temporal evolution of RVMT antigenic sites, and how does this relate to immune escape and vaccine efficacy?
>
> *Rationale:* The candidate addresses antigenic evolution and vaccine efficacy, which is semantically unrelated to GQ_001's metatranscriptome/RdRP-focused discovery question; it only references the available RVMT_Zenodo_V4.zip file but lacks any required elements from the gold question.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.220 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> How do seasonal temperature variations correlate with the timing and magnitude of respiratory virus outbreak peaks across different geographic regions in the RVMT dataset?
>
> *Rationale:* The candidate is an epidemiological question about seasonality and temperature correlations in respiratory virus outbreaks using RVMT data, which is semantically unrelated to the gold question on RdRP-based metatranscriptome mining and RNA phage discovery; required elements are absent.

**Rank 2** · Comp = 0.080 · ❌ fail

> What is the relative prevalence and temporal succession of different respiratory virus strains within the RVMT surveillance network over multi-year periods?
>
> *Rationale:* The candidate is a surveillance time-series question about respiratory strain prevalence in RVMT V4 and does not address GQ_001's metatranscriptome/RdRP-driven RNA virome expansion or RNA phage discovery, though it is well grounded to the named RVMT file and time-stamped strain records.

**Rank 3** · Comp = 0.100 · ❌ fail

> How does the spatial clustering of respiratory virus detections vary by season and what does this reveal about local transmission dynamics in the RVMT dataset?
>
> *Rationale:* The candidate addresses spatial/seasonal epidemiology in the RVMT dataset, which is semantically unrelated to GQ_001's global metatranscriptome RdRP-driven RNA-virus and RNA-phage discovery goals; it contains no required elements but is moderately grounded to the named RVMT file.

**Rank 4** · Comp = 0.120 · ❌ fail

> Are there detectable inter-annual trends in the timing of respiratory virus onset in the RVMT dataset, and if so, how do they relate to climate variability indices?
>
> *Rationale:* The candidate addresses respiratory-virus seasonality and climate using the RVMT surveillance dataset, which does not align with GQ_001's focus on RdRP-based discovery of RNA virome expansion and RNA bacteriophages; it is well grounded in the provided RVMT file but semantically mismatched.

**Rank 5** · Comp = 0.220 · ❌ fail

> What is the co-circulation pattern of multiple respiratory virus types within the RVMT dataset, and does evidence of viral interference exist between competing strains?
>
> *Rationale:* The candidate addresses respiratory-virus co-circulation and interference in a specific RVMT dataset, which is epidemiological and time-series focused and thus semantically different from the gold question about RdRP-driven global RNA virome expansion and RNA phage discovery.


## 8 · `tara_oceans_science_2022`

- **raw**：7 文件: `44779_RdRP_contigs.fna.gz, 5504_wcANI_based_clusters_90_80.fna.gz, RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz, RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent.fasta.gz...`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 3 | 4 | 4 | 5 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 3 | 2 | 2 | 2 | 5 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Across the 5,504 marine RNA-virus vOTUs, do RdRP phylogenetic clades — particularly the novel megataxa Taraviricota, Arctiviricota, Pomiviricota, Paraxenoviricota and Wamoviricota — possess statistically distinct accessory-gene repertoires (capsid, methyltransferase, helicase, protease families annotated in functional-annotation-table.tsv), and does the presence of specific capsid families (e.g., Calici_coat, CRPV_capsid, Waikav_capsid_1, Birna-class) co-segregate with RdRP clade membership rather than crossing clade boundaries through horizontal gene transfer?
>
> *Rationale:* The candidate directly tests whether marine RdRP-based clades (megataxa) are supported by accessory-gene congruence, mapping closely to GQ_002's aim to evaluate high-level phylogenetic/taxonomic revision using RdRP data and associated annotations.

**Rank 2** · Comp = 0.629 · ✅ pass

> What fraction of the 5,504 marine RNA-virus vOTUs encode an identifiable capsid protein, and does this capsid-detection rate differ between known RdRP supergroups and the five novel megataxa, indicating that the latter use structurally divergent or as-yet-uncharacterised virion architectures?
>
> *Rationale:* The candidate investigates RdRP-defined clade-level differences (capsid detection across known supergroups vs five novel megataxa), aligning with GQ_002's taxonomy-focus though it emphasizes structural annotation rather than explicit tree-based phylogenetic revision; it is well grounded in the provided files and counts.

**Rank 3** · Comp = 0.391 · ❌ fail

> Do Arctic versus non-Arctic Tara Oceans sampling stations harbour systematically different RdRP clade compositions in the 44,779-contig RdRP set, and which RdRP families (RdRP_1, RdRP_3, Mitovir_RNA_pol, Birna_RdRp, Bunya_RdRp, Mononeg_RNA_pol) are enriched or depleted in polar waters?
>
> *Rationale:* The candidate is a well‑grounded, specific biogeography/composition question using the RdRP contig set, but it does not seek phylogenetic reclassification at phylum/class levels required by the matched gold.

**Rank 4** · Comp = 0.850 · ✅ pass

> How many distinct RdRP lineages remain unrepresented in GenBank yet are recovered as near-complete centroids in this dataset, and what is their phylogenetic placement relative to the five new megataxa once 160,167 reference RdRPs are co-aligned with the 6,238 near-complete Tara centroids?
>
> *Rationale:* The candidate precisely targets high-level RNA-virus phylogeny revision using Tara RdRP centroids and specific reference sets, fully matching GQ_002's required elements and is tightly grounded in the listed RdRp footprint/centroid files.

**Rank 5** · Comp = 0.493 · ❌ fail

> Are RdRP-encoding contigs that also carry mitochondrial RdRP signatures (Mitovir_RNA_pol, 811 hits) preferentially recovered from eukaryote-enriched (>0.22–3 µm) Tara Oceans size fractions and DCM depths, suggesting that mitoviruses constitute a major and depth-stratified component of the marine RNA virome?
>
> *Rationale:* Matches GQ_002 because it uses marine RdRP contigs and Tara data but focuses on prevalence/depth patterns of mitoviruses rather than conducting phylogenetic or taxonomy-level revisions, so partial alignment with required elements.

### ✅ `gpt-5.5-high` — Comp=0.800 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 5 | 5 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 3 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.800 · ✅ pass

> Do Tara Oceans RdRp-containing vOTUs define previously undersampled marine RNA virus lineages that disproportionately expand 50%-identity RdRp diversity relative to GenBank and Wolf2020 references?
>
> *Rationale:* The candidate targets Tara RdRp sequences and quantifies centroid enrichment—well aligned with discovery of novel marine RdRPs—but lacks explicit claims about deeply divergent basal lineages or reshaping early RNA-virus evolutionary structure.

**Rank 2** · Comp = 0.578 · ❌ fail

> Which Tara Oceans vOTU clusters encode near-complete RdRp proteins with additional capsid or helicase annotations, and do these genomes mark candidate RNA virus groups with more complete evolutionary context?
>
> *Rationale:* The candidate aligns with GQ_002 by using Tara RdRP centroids to propose candidate virus groups, but it lacks explicit phylogenetic analysis and explicit phylum/class-level reclassification required for full alignment.

**Rank 3** · Comp = 0.408 · ❌ fail

> Are high-abundance Tara RdRp contigs, as estimated by multi values in nucleotide FASTA headers, concentrated in specific 90/80 wcANI vOTU representatives and RdRp annotation classes?
>
> *Rationale:* The candidate concerns Tara RdRP contigs and wcANI clusters (matching GQ_002's data domain) but asks about abundance vs. cluster/annotation distribution rather than high-level phylogenetic/taxonomic revision, covers two of five required elements, and is well grounded in specific files/headers.

**Rank 4** · Comp = 0.340 · ❌ fail

> How do strand orientation and domain-coordinate distributions of annotated vOTUs vary among polymerase, capsid, helicase, and hypothetical protein annotations in the functional table?
>
> *Rationale:* The candidate targets functional-annotation distributions (strand, domain coords) in the functional table and is well grounded in file columns and counts, but it does not pursue RdRP-based phylogenetic or taxonomic revision required by GQ_002.

**Rank 5** · Comp = 0.527 · ❌ fail

> Does the near-complete 50%-identity RdRp centroid set retain the same Tara-versus-reference diversity balance as the full centroid set, or does completeness filtering preferentially remove Tara marine sequences?
>
> *Rationale:* The candidate is a well-grounded, dataset-specific question about bias introduced by completeness filtering in RdRp centroid sets that affects phylogenetic interpretation, but it does not explicitly ask for phylum/class-level phylogenetic revision.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.60

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 4 | 3 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 3 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 4 | 2 | 3 | 3 | 5 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.700 · ✅ pass

> Do depth-layer (surface, DCM, mesopelagic) and polar vs. non-polar biogeography jointly predict the compositional turnover of RNA virus vOTU assemblages across Tara Oceans and Tara Oceans Polar Circle stations, as measured by RdRp-based diversity and the prevalence of novel-megataxon lineages in the 5504 vOTU catalogue?
>
> *Rationale:* Candidate aligns with GQ_001's discovery and RdRp focus and is well grounded in provided files, but it shifts emphasis to ecological turnover rather than addressing early evolutionary structure, so it partially matches the gold intent.

**Rank 2** · Comp = 0.578 · ❌ fail

> What fraction of the 5,504 marine RNA vOTUs from the Tara Oceans metatranscriptomes encode near-complete genome architectures (co-occurring RdRp, capsid, and auxiliary domains in the functional-annotation-table.tsv), and does genome completeness correlate with vOTU taxonomic novelty as inferred from RdRp phylogenetic distance to reference sequences?
>
> *Rationale:* The candidate aligns with GQ_002 by using Tara RdRP data and phylogenetic distance to infer taxonomic novelty, adds strong file-level grounding and a genome-completeness angle, but stops short of explicit phylum/class-level reclassification.

**Rank 3** · Comp = 0.800 · ✅ pass

> Do the five novel RNA virus megataxa identified in the Tara Oceans dataset (Arctiviricota, Paraxenoviricota, Pomiviricota, Taraviricota, Wamoviricota) show non-random geographic or depth-layer distribution across the 121 sampling stations, suggesting ecological niche partitioning among deep-branching RNA virus lineages?
>
> *Rationale:* The candidate aligns well with GQ_001 by interrogating Tara-derived deep-branching RdRP megataxa and evolutionary implications, covers most required elements and is grounded in specific files/metadata; it omits an explicit mention of 'uncultivated' diversity and emphasizes ecology over tree reshaping.

**Rank 4** · Comp = 0.560 · ❌ fail

> Is the per-sample RdRp-sequence richness of marine RNA viruses in the Tara Oceans dataset correlated with sampling depth layer, such that mesopelagic samples harbor systematically different RdRp diversity indices compared to surface and deep chlorophyll maximum samples, after controlling for sequencing effort reflected in contig counts?
>
> *Rationale:* Methodologically aligned to GQ_001 via Tara RdRP mining and diversity assessment, but semantically focused on depth-related richness rather than discovering deeply divergent lineages or reshaping early RNA-virus evolution.

**Rank 5** · Comp = 1.000 · ✅ pass

> Does the RdRp amino-acid sequence similarity between Tara Oceans marine RNA viruses and reference sequences from GenBank and Wolf et al. 2020 follow a bimodal distribution indicative of two distinct discovery regimes — recovered known diversity vs. genuinely novel deep-branching lineages — within the 13,109 fifty-percent-identity cluster representatives?
>
> *Rationale:* The candidate precisely tests RdRp divergence among Tara centroids to detect distinct known vs deep-branching novel lineages, matching GQ_001's intent and using specific files, counts, and statistical tests to ground the question.

### ✅ `gemini-3.1-pro` — Comp=0.700 · Pass@1=1.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 3 | 4 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 2 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 3 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 4 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 5 | 1 | 2 | 2 | 3 | 1.445 | 0.289 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.700 · ✅ pass

> How does the structural diversity of RNA-dependent RNA polymerases (RdRPs) in novel marine viral megataxa correlate with their functional adaptations and evolutionary divergence from known RNA viruses?
>
> *Rationale:* The candidate targets RdRP-based discovery of divergent marine viral lineages and their evolutionary divergence, matching GQ_001's intent, but it omits explicit global/metatranscriptome sampling and emphasis on reshaping early RNA‑virome structure while grounding itself in two specific dataset files.

**Rank 2** · Comp = 0.360 · ❌ fail

> What are the co-occurrence patterns of RNA-dependent RNA polymerases (RdRPs) and viral helicases across different marine sampling sites, and what do they reveal about viral replication strategies?
>
> *Rationale:* The candidate is about functional co-occurrence of RdRPs and helicases in marine contigs (data-grounded) but does not pursue the gold's evolutionary/discovery goal of finding deeply divergent RNA-virus lineages in global metatranscriptomes.

**Rank 3** · Comp = 0.460 · ❌ fail

> Can the diversity of viral capsid proteins identified in the metatranscriptomes be used to predict the host range of these novel marine RNA viruses?
>
> *Rationale:* The candidate is about host-range inference from capsid proteins in metatranscriptomes and is thematically related to GQ_001's marine metatranscriptome focus but lacks the RdRP- and evolution-centered intent required for a strong match.

**Rank 4** · Comp = 0.629 · ✅ pass

> How do the RdRP footprint sequences from the Tara Oceans expeditions compare to those from Genbank and previous studies in terms of sequence identity and phylogenetic placement?
>
> *Rationale:* The candidate aligns well with GQ_002 by comparing Tara RdRP footprints to GenBank for sequence identity and phylogenetic placement (file names cited), but it does not explicitly target phylum/class-level reclassification or state a taxonomy revision goal.

**Rank 5** · Comp = 0.289 · ❌ fail

> What is the prevalence and functional significance of methyltransferase domains in the assembled marine viral contigs?
>
> *Rationale:* Candidate asks about methyltransferase domain prevalence/function (a functional genomics question) not phylogenetic/taxonomic revision; it overlaps only on 'marine contigs' and RdRP proximity and cites functional-annotation-table.tsv, so it scores low-to-mid for match and grounding.

### ✅ `deepseek-v4-pro` — Comp=0.748 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 4 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 2 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 4 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.748 · ✅ pass

> Do the five newly discovered marine RNA virus phyla (Arctiviricota, Paraxenoviricota, Pomiviricota, Taraviricota, and Wamiviricota) possess distinct RdRP domain architectures and accessory-protein linkages that differentiate them from established orthornaviran phyla, and are these architectural differences consistent with their proposed deep-branching phylogenetic positions?
>
> *Rationale:* Well-aligned with GQ_002: uses RdRP contigs/footprints and phylum-level comparisons to evaluate taxonomy, strongly grounded in specific files and annotations; more focused on domain-architecture as mechanistic evidence than the gold's broader phylogenetic framing.

**Rank 2** · Comp = 0.374 · ❌ fail

> How does the taxonomic composition and diversity of RNA virus RdRP types vary across ocean depth layers (surface SRF, deep chlorophyll maximum DCM, and mesopelagic MES) in the Tara Oceans dataset, and do depth-associated community shifts correlate with known ecological partitioning of host organisms?
>
> *Rationale:* Matches marine RdRP data focus (Tara, RdRP domains) but asks about ecological depth-stratified diversity rather than performing phylogenetic analyses or proposing phylum/class-level taxonomy revisions; well grounded in specific files.

**Rank 3** · Comp = 0.544 · ❌ fail

> Which accessory protein domains (e.g., helicases, methyltransferases, peptidases, capsid proteins) are most strongly and consistently associated with each major class of RNA virus RdRP in marine metatranscriptomes, and do these domain co-occurrence patterns recapitulate known RNA virus genome organisations or reveal previously undescribed modular arrangements?
>
> *Rationale:* The candidate is well grounded in the provided RdRP/domain files and targets class-level RdRP associations, but it does not perform or claim phylogenetic analyses or propose taxonomy revision required by GQ_002.

**Rank 4** · Comp = 0.740 · ✅ pass

> Do the RNA virus communities recovered from eukaryotic-fraction versus prokaryotic-fraction metatranscriptomes in the Tara Oceans dataset differ in their RdRP type composition, and does the prokaryotic fraction reveal a previously underestimated diversity of RNA bacteriophages in marine surface waters?
>
> *Rationale:* Aligns with GQ_001's RdRP-driven discovery of cryptic marine RNA viruses (uses Tara data and RdRP contigs) but specializes on prokaryotic vs eukaryotic fractions and RNA bacteriophages, omitting explicit claims about deep divergence or reshaping early virome evolution.

**Rank 5** · Comp = 0.646 · ✅ pass

> Are the 50%-identity RdRP footprint centroids that are classified as 'near-complete' associated with specific RNA virus phyla or genome architectures, and does genome completeness correlate with higher confidence in domain annotation and predicted 3D structure quality across the novel marine megataxa?
>
> *Rationale:* The candidate aligns well with GQ_002 by using RdRP footprints to ask about phylum-level associations in marine RNA viruses, but it emphasizes completeness and annotation confidence rather than performing explicit phylogenetic analyses or proposing taxonomy revisions.

### ✅ `glm-5` — Comp=0.820 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 5 | 2 | 2 | 3 | 5 | 2.125 | 0.425 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.820 · ✅ pass

> How do the five newly discovered RNA virus megataxa (Arctiviricota, Paraxenoviricota, Pomiviricota, Taraviricota, Wamoviricota) distribute across ocean ecological zones (deep chlorophyll maximum, surface, mesopelagic) and what functional protein domains characterize their genomes beyond RdRp?
>
> *Rationale:* Strong semantic match to primary discovery intent (novel, divergent Tara RdRPs) with concrete file/field grounding; loses one required element by not asking about evolutionary origins/early RNA‑virome structure.

**Rank 2** · Comp = 0.760 · ✅ pass

> What proportion of the 44,779 RdRp contigs represent novel RNA virus lineages versus known viral families, and how does this ratio vary across different ocean depth zones?
>
> *Rationale:* Maps well to the primary discovery intent (RdRP-based marine viral novelty) with strong dataset grounding, but lacks explicit emphasis on deep divergence and implications for early RNA-virus evolutionary structure.

**Rank 3** · Comp = 0.408 · ❌ fail

> What viral protein domains co-occur with RdRp in marine RNA virus genomes, and do specific domain combinations correlate with particular ecological zones or viral lineages?
>
> *Rationale:* The candidate is closest to GQ_002 because it centers on RdRp-containing marine contigs and lineage correlations, but it lacks the phylogenetic/taxonomic revision focus required by GQ_002 while being well grounded in specific files and annotations.

**Rank 4** · Comp = 0.476 · ❌ fail

> Are Arctic marine RNA viruses (stations 100-150) distinct from non-Arctic viruses in terms of RdRp diversity, viral family composition, and functional protein domain representation?
>
> *Rationale:* The candidate is a well-grounded, data-specific geographic comparison of marine RdRp diversity and functional domains but lacks the high-level phylogenetic/taxonomic revision focus required by GQ_002.

**Rank 5** · Comp = 0.425 · ❌ fail

> How many of the 44,779 RdRp contigs represent near-complete viral genomes based on the presence of multiple essential viral proteins (RdRp, capsid, helicase) versus partial genome fragments?
>
> *Rationale:* The candidate strongly targets contig-level completeness using specific RdRP files (high data grounding) but does not address phylogenetic or taxonomic revision, so it only partially matches GQ_002's intent.

### ✅ `gemini-2.5-flash` — Comp=0.740 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 3 | 4 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 3 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 4 | 3.700 | 0.740 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.640 · ✅ pass

> What is the diversity and distribution of RNA-dependent RNA polymerase (RdRP) types across different marine environments sampled during the Tara Oceans expeditions?
>
> *Rationale:* The candidate aligns with the global RdRP discovery theme (Tara Oceans, RdRP types) and is well grounded in provided files, but it omits explicit focus on deep divergence and evolutionary reconfiguration required by GQ_001.

**Rank 2** · Comp = 0.680 · ✅ pass

> Are there specific RdRP domain architectures or accessory protein domains that are uniquely associated with particular marine viral megataxa identified in the Tara Oceans dataset?
>
> *Rationale:* The candidate is a strong match to GQ_002 because it links RdRP features in Tara Oceans data to high-level viral groups and cites concrete files, but it stops short of requesting explicit phylogenetic analyses or a taxonomy revision.

**Rank 3** · Comp = 0.357 · ❌ fail

> How do the sequence characteristics (e.g., length, e-value, probability) of identified RdRP domains vary across different viral groups or environmental samples?
>
> *Rationale:* The candidate is an RdRP-focused, data-grounded descriptive question (functional-annotation fields) but does not pursue the phylogenetic/taxonomic revision central to the matched gold question.

**Rank 4** · Comp = 0.560 · ❌ fail

> What is the relative abundance of different RdRP types within the overall viral community across the Tara Oceans samples?
>
> *Rationale:* The candidate aligns with the primary gold on RdRP abundance in Tara Oceans and cites specific files, but it omits the gold's key goals of finding divergent lineages and addressing evolutionary/novel diversity.

**Rank 5** · Comp = 0.740 · ✅ pass

> Are there novel or uncharacterized RdRP domains present in the Tara Oceans dataset that warrant further investigation for their evolutionary or functional significance?
>
> *Rationale:* The candidate aligns well with GQ_001 by querying novel RdRPs in Tara metatranscriptomes and citing specific files, but it omits explicit claims about deeply divergent, abundant, or large uncultivated diversity, so it partially but not fully covers the gold question.

### ✅ `intern-s1` — Comp=0.480 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 2 | 3 | 1.190 | 0.238 | ❌ | GQ_002 (S) |
| 4 | 2 | 2 | 2 | 3 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.480 · ❌ fail

> What is the relative abundance of different RdRp domain types across marine metagenomic samples?
>
> *Rationale:* The candidate addresses RdRP abundance in marine samples (matching part of GQ_001) and is grounded in functional-annotation-table.tsv, but it omits global metatranscriptome scope and evolutionary/divergence claims required by the gold.

**Rank 2** · Comp = 0.306 · ❌ fail

> Do specific RdRp domain types co-occur within the same genomic contigs?
>
> *Rationale:* The candidate focuses narrowly on RdRp domain co-occurrence in contigs (grounded in functional-annotation-table.tsv) but omits the phylogenetic/taxonomic revision and marine scope central to GQ_002.

**Rank 3** · Comp = 0.238 · ❌ fail

> Is there a correlation between annotation confidence scores and RdRp domain types?
>
> *Rationale:* Matched to GQ_002 because of shared RdRP focus, but the candidate targets annotation-confidence correlations (with specific file/columns) rather than phylogeny or taxonomy, so semantic alignment and required-element coverage are low despite concrete data grounding.

**Rank 4** · Comp = 0.357 · ❌ fail

> Do RdRp domains show strand orientation bias in marine viral genomes?
>
> *Rationale:* The candidate is an RdRP-focused, data-grounded question about strand orientation bias (uses functional-annotation-table.tsv) but does not address the phylogenetic or taxonomic revision aims central to GQ_002.

**Rank 5** · Comp = 0.306 · ❌ fail

> How do RdRp domain lengths vary between different domain types?
>
> *Rationale:* The candidate uses concrete RdRp domain columns in functional-annotation-table.tsv but asks a descriptive length-comparison, not the phylogeny/taxonomy revision central to GQ_002, so it only weakly matches the gold.

### ✅ `intern-s1-pro` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 5 | 2.210 | 0.442 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 2 | 4 | 2.210 | 0.442 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.442 · ❌ fail

> What is the distribution of RdRP domain types (RdRP_1, RdRP_2, RdRP_3, RdRP_4) across the 5,504 ANI-based viral clusters, and does this distribution correlate with sequence similarity thresholds?
>
> *Rationale:* The candidate is a cluster-focused, data-grounded question about RdRP domain distributions that aligns partially with GQ_002's clustered-RdRP intent but omits explicit phylogenetic methods, high-level taxonomic (phylum/class) claims, and marine framing, so it is moderately aligned but incomplete.

**Rank 2** · Comp = 0.560 · ❌ fail

> How does the diversity of RdRP domain architectures correlate with sampling depth and geographic location across the Tara Oceans expedition sites?
>
> *Rationale:* The candidate aligns with the Tara+RdRP scope but shifts to ecological biogeography of RdRP domain architectures rather than the gold's core aim of finding deeply divergent, evolutionarily informative RNA-virus lineages; it is well grounded in specific files and sample codes.

**Rank 3** · Comp = 0.442 · ❌ fail

> What proportion of marine RNA viruses encode additional functional domains (e.g., helicases, methyltransferases) alongside RdRP, and how does this multi-domain architecture vary across viral clusters?
>
> *Rationale:* Matches GQ_002 on RdRP and clusters but misses the phylogenetic, phylum/class-level, and taxonomy-revision focus; well grounded in specific functional-annotation and cluster files.

**Rank 4** · Comp = 0.560 · ❌ fail

> Are there novel RdRP domain architectures or combinations not previously described in GenBank or Wolf et al. (2020), and what is their prevalence in marine environments?
>
> *Rationale:* The candidate aligns with GQ_001's discovery focus using Tara RdRP data but shifts to domain-architecture novelty and prevalence rather than deep divergence or evolutionary reclassification; it is grounded in named files but misses key evolutionary elements.

**Rank 5** · Comp = 0.323 · ❌ fail

> How does the confidence of RdRP domain assignments (prob, e-value, score) vary across different domain types and viral clusters, and does this reflect biological reality or technical artifacts?
>
> *Rationale:* Candidate is about annotation-confidence of RdRP domains (well grounded in files/columns) but does not pursue GQ_002's phylogenetic/taxonomic revision questions, so semantic match is weak despite good data grounding.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.680 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 4 | 3.000 | 0.600 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 4 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.600 · ✅ pass

> What is the diversity and relative abundance of RdRP domain types across Tara Oceans sampling sites, and how does this reflect the global distribution of marine RNA viruses?
>
> *Rationale:* Good semantic match on Tara/RdRP and biogeography but misses the discovery/evolution emphasis (deeply divergent lineages, early virome structure, uncultivated diversity); well grounded in specific files/columns.

**Rank 2** · Comp = 0.560 · ❌ fail

> How do RdRP domain compositions differ between Arctic and non-Arctic Tara Oceans samples, and what does this reveal about polar versus temperate marine RNA viromes?
>
> *Rationale:* Matched to GQ_001 because of RdRP and Tara/metatranscriptome focus; captures geographic composition but misses discovery of deeply divergent lineages and evolutionary-structure aims; covers 2/5 required elements and is grounded in multiple listed files.

**Rank 3** · Comp = 0.629 · ✅ pass

> What proportion of identified RdRP domains in the Tara Oceans dataset are near-complete versus partial, and how does completeness affect phylogenetic placement and taxonomic assignment?
>
> *Rationale:* The question fits GQ_002 by focusing on Tara RdRP data and phylogenetic/taxonomic outcomes, but it emphasizes sequence completeness and does not explicitly target phylum/class-level revision of taxonomy.

**Rank 4** · Comp = 0.680 · ✅ pass

> How do the Tara Oceans RdRP sequences cluster with known RdRP sequences from Genbank and Wolf et al. 2020, and what novel lineages emerge from this comparison?
>
> *Rationale:* The candidate is well-aligned with GQ_002 by focusing on Tara RdRP footprints versus reference RdRPs and identifying novel lineages via phylogenetic clustering, but it omits explicit phylum/class-level claims and formal taxonomy revision.

**Rank 5** · Comp = 0.560 · ❌ fail

> What functional domains co-occur with RdRP domains in Tara Oceans viral contigs, and what does this reveal about viral genome organization and replication strategies?
>
> *Rationale:* The candidate aligns with GQ_001 by using RdRP and Tara Oceans data but shifts focus to domain co-occurrence and genome architecture rather than discovering deeply divergent lineages or revising early RNA-virus evolutionary structure; it is well grounded in provided annotation files.


## 9 · `tick_metavirome_2023`

- **raw**：1 文件: `nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Across the 1,801 TIGMIC metagenome-assembled viral genomes from Chinese tick samples, do the mycovirus-typical families (Narnaviridae, Mitoviridae, Botourmiaviridae, Totiviridae, Partitiviridae) — including the 89 sequences explicitly annotated as Erysiphe necator-associated and Plasmopara viticola lesion-associated — represent genuine tick-resident RNA viromes that co-vary geographically with classical tick-borne arbovirus families (Phenuiviridae, Nairoviridae, Flaviviridae, Orthomyxoviridae), and what does that co-variation imply about cross-kingdom virus traffic in tick microbiomes?
>
> *Rationale:* The candidate precisely targets tick-derived RNA genomes, specialist vs generalist reservoirs and geographic co-variation, is tightly grounded in FASTA headers/accessions and sampling tags, and thus fully matches GQ_001 with high acceptability and data grounding.

**Rank 2** · Comp = 0.578 · ❌ fail

> Within the TIGMIC tick metagenome, do the Phenuiviridae, Nairoviridae and Flaviviridae assemblies (including Brown dog tick phlebovirus 1/2, Sara tick phlebovirus, Dabieshan Tick Virus, Wuhan tick virus 2, Lihan tick virus, and named Henan/Shanxi/Yanbian tick viruses) form province-level RdRp phylogeographic clades that mirror the known dispersal of medically important bunyaviruses such as SFTSV and Crimean-Congo-like nairoviruses across China?
>
> *Rationale:* Matches GQ_002 on phylogeography and lineage distribution across provinces with strong FASTA-grounded evidence, but fails to include tick-species and host-range elements required by the gold question.

**Rank 3** · Comp = 0.760 · ✅ pass

> Do the Orthomyxoviridae assemblies in this dataset (n=37, predominantly ~2.36 kb single-segment contigs) represent novel tick-borne quaranja-like or thogoto-like influenza-relatives whose segment-level diversity and sequence completeness suggest stable enzootic circulation in Chinese ticks rather than incidental detection?
>
> *Rationale:* Good semantic match to GQ_001: specific genome-discovery + reservoir question focused on Orthomyxoviridae and enzootic circulation, well grounded in dataset counts/lengths, but lacks explicit mention of metatranscriptomic sampling breadth (31 species).

**Rank 4** · Comp = 0.850 · ✅ pass

> Given the prominent Rhabdoviridae (n=72, median ~11.3 kb) and Chuviridae (n=20, median ~11.2 kb) signal in this tick metagenome alongside named Rhipicephalus-associated rhabdo-like viruses, do these full-length negative-sense RNA virus assemblies show evidence of co-divergence with their tick host genus rather than free arthropod-to-arthropod horizontal transmission?
>
> *Rationale:* The candidate precisely targets phylogenetic congruence of virus lineages with tick genus, includes geographic and abundance/genome-size evidence, and proposes explicit phylogenetic tests, directly matching GQ_002's intent.

**Rank 5** · Comp = 0.620 · ✅ pass

> Across the family-stratified length distributions in the TIGMIC FASTA — for example the >9 kb arbovirus-like assemblies in Flaviviridae, Nairoviridae and Chuviridae versus the 1.6–3.4 kb single-ORF assemblies in Narnaviridae, Mitoviridae and Botourmiaviridae — does sequence completeness (annotated 'complete genome' versus 'partial' or 'UNVERIFIED') systematically bias which viral families are reported as 'novel' in tick metagenomic surveys, and how does that bias distort estimates of tick virome diversity?
>
> *Rationale:* The candidate is a methodological question tightly grounded in the provided FASTA metadata and addresses bias in building an RNA-virus genome compendium from tick metagenomes, but it omits host-range/reservoir and broad-sampling elements required by GQ_001.

### ✅ `gpt-5.5-high` — Comp=0.561 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 2 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 3 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.493 · ❌ fail

> How is viral diversity structured across TIGMIC tick metagenomic isolates, and do genome completeness, genome size, and sequence composition distinguish major tick-associated RNA virus lineages?
>
> *Rationale:* The candidate aligns best with GQ_002 by examining lineage-level structure and genome distribution across tick-associated isolates, but it omits explicit tick species, geography, and host-range elements required by the gold question.

**Rank 2** · Comp = 0.561 · ❌ fail

> Do repeated TIGMIC isolate IDs contain multi-lineage viral assemblages that indicate co-occurrence of tick-borne, fungal-associated, and unclassified RNA viruses within the same metagenomic isolate?
>
> *Rationale:* The candidate probes viral clade host-range and within-isolate distribution (matching GQ_002's lineage and host-range intent) but omits tick-species and geographic variation; it is well grounded to the nuccore FASTA and TIGMIC isolate headers.

**Rank 3** · Comp = 0.500 · ❌ fail

> Which dominant viral lineages in the FASTA, including Totiviridae, Botourmiaviridae, Dabieshan Tick Virus, Rhabdoviridae, Flaviviridae, and Nairoviridae, provide enough complete genomes for comparative phylogenetic reconstruction?
>
> *Rationale:* The candidate targets which viral lineages in the uploaded FASTA yield enough complete genomes for phylogenetic work, aligning with GQ_001's genome-compendium focus but missing explicit metatranscriptome, multi-species, and reservoir/host-range elements.

**Rank 4** · Comp = 0.140 · ❌ fail

> Are MAG UNVERIFIED viral records concentrated in particular organism labels or sequence descriptors and are they shorter or compositionally different than verified MAG records?
>
> *Rationale:* The candidate is about MAG verification and sequence composition in a fasta file and therefore does not address the tick-focused genome-discovery/reservoir questions of GQ_001; it is data-grounded but semantically mismatched.

**Rank 5** · Comp = 0.380 · ❌ fail

> Do the TIGMIC viral MAG sequences show genome architecture differences among complete genomes, cRNA sequences, genomic sequences, and RdRP or PB1 coding records that separate RNA virus families?
>
> *Rationale:* The candidate centers on RNA-virus genome architecture (matches GQ_001's genome focus) but fails to include tick metatranscriptome sampling, host-range/reservoir framing, and the broad tick-species scope required by GQ_001; it is well grounded in the provided FASTA file.

### ✅ `claude-code-sonnet-4-6` — Comp=0.697 · Pass@1=0.00 · Pass@5=0.35

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.578 · ❌ fail

> Does within-pool viral species richness in metagenome-assembled tick viromes (119 TIGMIC pools) correlate with co-occurrence of medically important RNA virus families (Phenuiviridae, Nairoviridae, Flaviviridae) across geographically distinct Chinese collection sites, and do co-detected mycovirus-like sequences (Totiviridae, Botourmiaviridae, Narnaviridae) statistically predict co-presence of pathogen-family viruses in the same tick pool?
>
> *Rationale:* The candidate well addresses geography, host-range categories, and pool-level viral abundance/co-occurrence with strong dataset grounding, but it omits tick-species and phylogenetic-lineage analyses required by the matched gold question.

**Rank 2** · Comp = 0.646 · ✅ pass

> Do the metagenome-assembled Phenuiviridae and Nairoviridae sequences in the TIGMIC tick dataset form phylogenetically distinct lineages relative to known human-pathogenic tick-borne phleboviruses (SFTS virus) and nairoviruses (CCHF virus), and does geographic clustering in Chinese provinces predict phylogenetic clustering in these two medically important families?
>
> *Rationale:* The candidate closely matches GQ_002 by testing phylogenetic vs geographic structure and host-range relevance (human pathogens), but it omits explicit tick-species stratification and measures of abundance/genome distribution.

**Rank 3** · Comp = 0.527 · ❌ fail

> Does the geographic collection site of tick pools in the TIGMIC dataset predict the composition of the associated RNA virome, specifically whether tropical/subtropical sites (Nanning, Zhangzhou, Dali) harbor significantly higher Flaviviridae and Phenuiviridae richness compared to temperate/boreal sites (Hulunbuir, Tonghua, Yanbian)?
>
> *Rationale:* Best match is GQ_002 because the candidate tests geographic differences in virome composition with concrete counts and sites; it fails to address tick-species, host-range, and phylogenetic lineage required by the gold question.

**Rank 4** · Comp = 0.578 · ❌ fail

> Are the 945 unclassified (sp.) metagenome-assembled viral sequences in the TIGMIC tick virome dataset distributed non-randomly across the 17 represented RNA virus families, and does the proportion of unclassified sequences within each family correlate with the total family richness sampled, suggesting systematic under-characterization of specific tick-borne virus lineages in China?
>
> *Rationale:* The candidate aligns with GQ_002's lineage-and-geography focus (family-level distribution in China) but omits tick-species and host-range elements; it is highly data-grounded and framed acceptably.

**Rank 5** · Comp = 0.697 · ✅ pass

> Do the Rhipicephalus-associated and Brown dog tick (Rhipicephalus sanguineus)-associated phlebovirus sequences in the TIGMIC dataset exhibit evidence of geographic population structure (sequence divergence correlated with collection site distance) consistent with co-evolutionary isolation, or do they show signatures of recent geographic spread across the sampled Chinese sites?
>
> *Rationale:* The candidate targets geographic and phylogenetic variation of Rhipicephalus-associated phleboviruses with specific sequence counts and city labels, matching GQ_002's core intent but omitting explicit viral abundance/genome distribution metrics.

### ✅ `gemini-3.1-pro` — Comp=0.480 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 2 | 3 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.459 · ❌ fail

> How does the genetic diversity of Botou tick virus isolates correlate with their geographic distribution across different regions in China?
>
> *Rationale:* The candidate best matches GQ_002 by asking a phylogeographic question about a tick virus (geography + lineage) and is grounded in the provided FASTA and named isolates, but it omits required elements on tick species, host-range, and abundance/genome distribution.

**Rank 2** · Comp = 0.480 · ❌ fail

> What are the most highly conserved genomic regions among the different species of tick-borne viruses in this dataset?
>
> *Rationale:* Matches GQ_001 on RNA-virus genome analysis grounded in the provided FASTA, but focuses narrowly on conserved regions rather than broad tick sampling, host-range, or reservoir structure, so required-element coverage is low.

**Rank 3** · Comp = 0.374 · ❌ fail

> Is there evidence of genetic recombination between different isolates of Botou tick virus 1?
>
> *Rationale:* The candidate is a specific recombination question for Botou tick virus 1 and only partially aligns with GQ_002's intent (covers genomes and locations) but omits tick-species, host-range and explicit lineage comparisons; it is grounded in the provided fasta sequences.

**Rank 4** · Comp = 0.440 · ❌ fail

> What is the variation in GC content across the genomes of the different tick viruses reported?
>
> *Rationale:* The candidate is genome-focused and grounded in the provided FASTA but addresses GC composition rather than the gold's emphasis on broad metatranscriptomic sampling, reservoir structure, and host-range (specialist/generalist) discovery.

**Rank 5** · Comp = 0.340 · ❌ fail

> Can specific genetic markers differentiate between Botou tick virus 1 and Botou tick virus 2?
>
> *Rationale:* Candidate is a narrow, data-grounded comparative genetics question about two viruses; it partially matches GQ_002's lineage focus but omits key distributional elements (species, geography, host-range, abundance), so scores low-to-mid on coverage and match.

### ✅ `deepseek-v4-pro` — Comp=0.578 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 3 | 2 | 3 | 3 | 4 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 3 | 3 | 4 | 3 | 2.720 | 0.544 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.578 · ❌ fail

> Do the metagenome-assembled tick virus genomes in this dataset exhibit stronger phylogenetic clustering by geographic location than by viral genus, indicating that local tick populations harbor distinctive, co-diverged viral communities shaped by ecological isolation?
>
> *Rationale:* The candidate tightly tests geography versus taxonomy using MAG genomes (strong data grounding) and matches GQ_002 on geography and phylogeny but omits explicit tick-species and host-range elements, so it is a partial but well-specified match.

**Rank 2** · Comp = 0.420 · ❌ fail

> Do the tick virus genomes labeled as 'cRNA sequence' represent a distinct genome segment or replication intermediate, as evidenced by systematic differences in sequence length, ORF content, and terminal repeat structures compared to those labeled as 'genomic sequence'?
>
> *Rationale:* The candidate is a concrete, data-grounded genome-structure question about tick viral fasta entries and labels, so it partially aligns with GQ_001's genome-discovery theme but lacks the required metatranscriptomic sampling, host-range, and reservoir elements; scores reflect strong data grounding but low coverage of required elements.

**Rank 3** · Comp = 0.459 · ❌ fail

> Is there evidence of inter-genus recombination among co-circulating tick viruses, as detectable by discordant phylogenetic signals across different genomic regions in viruses sampled from the same geographic location?
>
> *Rationale:* Candidate is topically aligned to GQ_002 through geography and phylogenetic analysis but asks a different specific question (recombination across genera) and omits tick-species and host-range elements; it is well grounded in provided sequence data and sample locations.

**Rank 4** · Comp = 0.480 · ❌ fail

> Can conserved RNA-dependent RNA polymerase (RdRp) motifs identified across all six tick virus genera in this dataset serve as universal qPCR or sequencing targets for pan-tick-virus surveillance?
>
> *Rationale:* The candidate addresses RNA-virus genome-based surveillance using conserved RdRp motifs (aligning partially with GQ_001) but omits required elements like broad metatranscriptomic sampling, species breadth, and reservoir/host-specialist comparisons.

**Rank 5** · Comp = 0.544 · ❌ fail

> Does codon usage bias in these tick-associated viral genomes correlate with the inferred host tick species, and can it be used to predict the arthropod vector from viral sequence alone?
>
> *Rationale:* The candidate aligns with GQ_002 on tick-species and host-range questions and is grounded to the provided viral sequences, but it omits phylogenetic lineage and abundance/genome-distribution elements required by GQ_002.

### ✅ `glm-5` — Comp=0.580 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 4 | 3 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 5 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.561 · ❌ fail

> How does geographic location influence the phylogenetic clustering and genetic divergence of tick-borne viral genomes across different viral families in China?
>
> *Rationale:* Matches GQ_002 on geography and phylogenetics using sequence headers with city labels and complete genomes, but omits required tick-species and host-range framing; well grounded in nuccore_reported_viral_sequences.fasta.

**Rank 2** · Comp = 0.510 · ❌ fail

> What patterns of viral family diversity and richness emerge across different geographic sampling locations in Chinese tick populations?
>
> *Rationale:* The candidate aligns with GQ_002 on geographic variation in viral composition and is grounded in sequence-header metadata, but it misses required elements about tick species, host-range categories, and phylogenetic lineage.

**Rank 3** · Comp = 0.280 · ❌ fail

> Which genomic regions show the highest conservation versus variability across tick-borne viral families, potentially indicating functional constraints or adaptive evolution?
>
> *Rationale:* The candidate is a comparative genomics question about conserved regions in tick-borne virus genomes, which only overlaps GQ_001's genome aspect and lacks the metatranscriptomic, sampling, and reservoir/host-range elements required by the gold.

**Rank 4** · Comp = 0.580 · ❌ fail

> Do tick-borne viruses in this dataset exhibit genomic signatures associated with known zoonotic potential or host-switching capability?
>
> *Rationale:* Partial match to GQ_001: targets host-range/zoonotic genomic signatures and cites the viral FASTA, but lacks metatranscriptome framing, broad tick-species sampling, and reservoir-scale analysis.

**Rank 5** · Comp = 0.527 · ❌ fail

> What evolutionary relationships exist between Botou tick virus variants from different geographic locations, suggesting patterns of viral dispersal or local adaptation?
>
> *Rationale:* The candidate aligns well with GQ_002's focus on phylogenetic/geographic variation of viral lineages (explicit locale list and genomes) but omits required dimensions of tick species and host-range, so it partially matches the gold intent.

### ✅ `gemini-2.5-flash` — Comp=0.561 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 3 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 3 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.510 · ❌ fail

> What is the phylogenetic relationship and geographical distribution of different Botou tick virus types (1, 2, 3, 4, 5) across the reported isolates from various Chinese locations (Nanning, Tonghua, Zhangzhou, Maanshan, Lianyungang, Hulunbuir)?
>
> *Rationale:* Addresses phylogeny and geography for Botou tick viruses grounded in the provided fasta, aligning partially with GQ_002 but missing tick-species and host-range elements.

**Rank 2** · Comp = 0.510 · ❌ fail

> Are there specific genetic markers or conserved regions within the Botou tick virus genomes that differentiate the various types or geographical isolates?
>
> *Rationale:* The question aligns partially with GQ_002 by targeting geographic and genomic differentiation of viral lineages using provided fasta sequences, but it omits tick-species and host-range considerations required by the gold question.

**Rank 3** · Comp = 0.306 · ❌ fail

> Do recombination events play a significant role in the genetic diversity and evolution of Botou tick viruses across the sampled isolates?
>
> *Rationale:* The candidate is about viral evolution via recombination and thus only loosely matches GQ_002's focus on lineage variation; it omits species, geography, and host-range details but is concretely tied to a named sequence file for analysis.

**Rank 4** · Comp = 0.561 · ❌ fail

> What is the extent of genetic diversity within each Botou tick virus type, and how does this diversity vary across different geographical regions?
>
> *Rationale:* The candidate aligns well with GQ_002 on geographic variation and within-lineage diversity and is grounded in the provided FASTA, but it omits tick-species and host-range elements required by the gold question.

**Rank 5** · Comp = 0.340 · ❌ fail

> Can specific genomic features or mutations be correlated with potential differences in virulence or host adaptation among the Botou tick virus isolates?
>
> *Rationale:* The candidate focuses on mutation-level correlates of virulence/host adaptation in Botou isolates, which overlaps GQ_002's host-range intent but misses species, geography and lineage/distribution elements and only references a single fasta data source.

### ✅ `intern-s1` — Comp=0.544 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 2 | 2 | 2 | 3 | 3 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 3 | 2 | 2 | 3 | 3 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 3 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.306 · ❌ fail

> Which Botou tick virus subtype is most prevalent in the dataset?
>
> *Rationale:* Matched to GQ_002 because both touch viral abundance, but the candidate is a narrow prevalence/count question lacking species, geography, host-range, and phylogenetic comparisons; it is grounded in a specific FASTA file and headers.

**Rank 2** · Comp = 0.391 · ❌ fail

> What is the geographic distribution of Botou tick virus isolates across different locations?
>
> *Rationale:* The candidate aligns with GQ_002's geographic aspect and references concrete header metadata, but it focuses on a single virus and locations only, missing species-level, host-range, and phylogenetic lineage elements required by the gold question.

**Rank 3** · Comp = 0.391 · ❌ fail

> How many distinct isolates exist per Botou tick virus subtype?
>
> *Rationale:* The candidate aligns with GQ_002's lineage/abundance aspects by counting isolates per subtype but misses required axes (species, geography, host-range), so it's a narrower, data-grounded query rather than a full match.

**Rank 4** · Comp = 0.544 · ❌ fail

> What is the genetic diversity of Botou tick virus isolates within and between geographic regions?
>
> *Rationale:* Matches GQ_002 on geography and lineage (phylogenetic diversity) but is narrower (single virus) and omits tick-species and host-range elements; uses a specific fasta file for grounding.

**Rank 5** · Comp = 0.459 · ❌ fail

> Is there a correlation between geographic distance and genetic divergence in Botou tick virus isolates?
>
> *Rationale:* Matches GQ_002 on geography and phylogenetic divergence but is narrower (single virus, no tick-species or host-range elements) and grounded to one fasta file; suitable as a focused subquestion of GQ_002.

### ✅ `intern-s1-pro` — Comp=0.476 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 3 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 3 | 3 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.476 · ❌ fail

> What is the nucleotide diversity and phylogenetic relationship among Botou tick virus isolates from different geographic locations in China?
>
> *Rationale:* The candidate matches GQ_002's phylogenetic and geographic intent using concrete FASTA headers, but it omits tick-species and host-range elements and does not address abundance/genome-distribution, so alignment is partial.

**Rank 2** · Comp = 0.360 · ❌ fail

> Are there conserved genomic regions or motifs across all Botou tick virus isolates that could indicate essential functional elements?
>
> *Rationale:* The candidate is a genome-focused conserved-motif question that aligns weakly with GQ_001's genome theme but lacks the required broad metatranscriptomic sampling and reservoir/host-range elements.

**Rank 3** · Comp = 0.391 · ❌ fail

> How do the genomic lengths and GC content vary among different Botou tick virus isolates, and is there a geographic correlation?
>
> *Rationale:* The candidate focuses on genome-length/GC variation and geography for Botou tick virus isolates, aligning weakly with GQ_002's geographic variation element but missing species, host-range, and phylogenetic lineage requirements.

**Rank 4** · Comp = 0.306 · ❌ fail

> Can we detect evidence of recombination events between different Botou tick virus strains based on sequence alignment patterns?
>
> *Rationale:* The candidate aligns weakly with GQ_002 by addressing phylogenetic signal in viral sequences but omits key comparative elements (species, geography, host-range, abundance); it is well grounded in the provided fasta file and sequence-analysis methods.

**Rank 5** · Comp = 0.400 · ❌ fail

> What is the distribution of open reading frames (ORFs) and potential protein-coding regions across the Botou tick virus genomes?
>
> *Rationale:* The candidate is a valid genome-annotation question tied to the provided FASTA, so it matches the 'RNA-virus genomes' aspect of GQ_001 but fails to address the required broad metatranscriptomic sampling and reservoir/host-range intent.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.527 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 2 | 0 | 1 | 1 | 4 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 3 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.527 · ❌ fail

> What is the genetic diversity and phylogenetic relationship among Botou tick virus isolates from different geographic locations in China?
>
> *Rationale:* The candidate well addresses geographic variation and phylogeny using specific fasta accessions, aligning partially with GQ_002, but misses tick-species and host-range/abundance elements required for full alignment.

**Rank 2** · Comp = 0.180 · ❌ fail

> How do the complete genome sequences of Wuhan mivirus isolates (TIGMIC_41, TIGMIC_43, TIGMIC_44, TIGMIC_45) compare in terms of sequence identity and structural features?
>
> *Rationale:* The candidate targets isolate-level genome comparison for Wuhan mivirus accessions in the provided FASTA, which only matches the 'RNA-virus genomes' element of GQ_001 and does not address tick sampling, host-range, or reservoir questions.

**Rank 3** · Comp = 0.360 · ❌ fail

> What nucleotide composition biases (GC content, codon usage) characterize these reported viral genomes and how do they vary between virus types?
>
> *Rationale:* The candidate aligns weakly with GQ_001 via RNA-virus genomes and is grounded in the provided FASTA, but it omits tick-focused sampling, host-range/reservoir aims, and thus captures only a small part of the gold intent.

**Rank 4** · Comp = 0.280 · ❌ fail

> Are there evidence of recombination events or shared genomic segments among the closely related Wuhan mivirus cRNA and complete genome sequences?
>
> *Rationale:* The candidate is a specific recombination/genomics question about Wuhan mivirus sequences and is only tangentially related to the gold's RNA-virus genome theme; it omits all tick- and reservoir-related elements required by GQ_001.

**Rank 5** · Comp = 0.500 · ❌ fail

> What functional domains or conserved protein-coding regions can be identified in these viral genomes through open reading frame analysis?
>
> *Rationale:* Matches GQ_001 on genome-focused analysis but misses tick-sampling and reservoir/host-range elements; well grounded to the provided fasta sequences and suitable as a genomic characterization sub-question.


## 10 · `vertebrate_rna_viruses_2018`

- **raw**：3 文件: `41586_2018_12_MOESM1_ESM.pdf, 41586_2018_12_MOESM2_ESM.xlsx, 41586_2018_12_MOESM3_ESM.xlsx`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 4 | 2 | 3 | 3 | 5 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.697 · ✅ pass

> To what extent have major vertebrate RNA-virus families (Astroviridae, Picornaviridae, Caliciviridae, Hepeviridae, Flaviviridae/Hepacivirus, Arenaviridae, Filoviridae, Hantaviridae, Orthomyxoviridae and Reoviridae) co-diverged with their chordate hosts across the ~525-million-year span from jawless fish to reptiles, rather than being recent mammalian/avian acquisitions?
>
> *Rationale:* Strong semantic match to GQ_002: explicit co-phylogenetic tests, concrete data files and methods are present, but the question fails to mention endogenous viral elements, a required component of the gold question.

**Rank 2** · Comp = 1.000 · ✅ pass

> Which vertebrate host orders sampled here harbour previously unrecognised ancestral lineages of human-pathogen viral families (Filoviridae, Arenaviridae, Hantaviridae, Hepacivirus and Influenza-like Orthomyxoviridae), and what does their phylogenetic placement imply about the non-mammalian origins of these emerging zoonoses?
>
> *Rationale:* The candidate fully aligns with GQ_001: it uses MOESM3 metatranscriptomic records across vertebrate orders to test whether newly found sequences in non-mammalian hosts form ancestral lineages of key RNA-virus families, implicating deep virus–host associations and ancient origins.

**Rank 3** · Comp = 1.000 · ✅ pass

> Does host tissue tropism (gut vs gill vs liver vs lung) structure the recovered RNA virosphere across vertebrate classes, such that specific viral families show consistent organ-of-replication signatures conserved from fish gills to reptilian lungs?
>
> *Rationale:* The candidate is a focused, data-grounded instantiation of GQ_001: it uses the provided metatranscriptome tables to test cross-class tissue tropism and phylogenetic conservation of RNA-virus families, addressing deep virus–host associations and origins.

**Rank 4** · Comp = 0.560 · ❌ fail

> Are the segmented negative-sense RNA viruses recovered from fish and reptiles (Orthomyxoviridae, Hantaviridae, Arenaviridae) undergoing detectable reassortment within shared hosts, as evidenced by phylogenetic incongruence among co-occurring genome segments?
>
> *Rationale:* The candidate is a specific, well-grounded question about reassortment in segmented RNA viruses using MOESM3 segment-level metatranscriptomic data; it aligns with GQ_001's theme of vertebrate RNA viruses but omits broad phylogenetic sampling and ancient-origins framing.

**Rank 5** · Comp = 0.760 · ✅ pass

> How does sequencing depth per library (Data bp in MOESM2) and viral abundance (% reads, Coverage in MOESM3) jointly govern the rarefaction of viral-family discovery across vertebrate classes, and what does the saturation curve predict for the residual unsampled vertebrate virosphere?
>
> *Rationale:* The candidate targets metatranscriptomic sampling and cross-vertebrate viral-family discovery using MOESM2/3 and rarefaction modeling, matching GQ_001's sampling/discovery intent but lacking explicit mention of RNA-virus families and ancient origins.

### ✅ `gpt-5.5-high` — Comp=0.820 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 4 | 4 | 3 | 5 | 3.900 | 0.780 | ✅ | GQ_001 (P) |
| 5 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.731 · ✅ pass

> Do the RNA virus lineages discovered across 185 chordate host species show host-class and host-order phylogenetic structure consistent with long-term vertebrate virus-host co-divergence rather than random host switching?
>
> *Rationale:* The candidate strongly matches GQ_002 by testing virus versus host phylogenetic structure and co-divergence with concrete dataset columns and samples, but it omits mention of endogenous viral elements required by the gold question.

**Rank 2** · Comp = 0.580 · ❌ fail

> How much previously uncharacterized RNA-virus diversity is revealed by non-mammalian chordate sampling when novelty is measured by low BLASTx amino-acid identity, divergent-virus notes, and broad virus-family representation?
>
> *Rationale:* The candidate quantifies novel RNA-virus diversity in non-mammalian chordates with concrete BLASTx evidence, matching GQ_001's discovery goal but only partially covering broad vertebrate sampling and omitting virus-host association and ancient-origin questions.

**Rank 3** · Comp = 0.820 · ✅ pass

> Are RNA-virus family assemblages non-randomly distributed among chordate host classes after accounting for library number, sequenced base pairs, tissue type, and location?
>
> *Rationale:* The candidate strongly matches GQ_001's intent to test vertebrate virus-host associations using metatranscriptomic data and sampling covariates, but it does not address ancient origins or deep-time implications.

**Rank 4** · Comp = 0.780 · ✅ pass

> Do gut, gill, liver, and lung libraries differ in the RNA-virus families and viral abundances they recover across aquatic and terrestrial chordate hosts?
>
> *Rationale:* The candidate aligns well with GQ_001 on metatranscriptomic detection of RNA-virus families across vertebrate hosts and tissue-specific associations, but it does not address ancient origins or deep evolutionary history required by GQ_001.

**Rank 5** · Comp = 0.800 · ✅ pass

> Which viral families detected in basal chordate lineages such as Agnatha, Chondrichthyes, and Sarcopterygii provide the strongest evidence for ancient origins of vertebrate-specific RNA viruses?
>
> *Rationale:* Candidate focuses on basal vertebrate clades and specific viral families to test ancient origins, matching the gold intent of uncovering deep virus-host associations across vertebrate phylogeny, but omits explicit mention of metatranscriptomic sampling.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 5 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.731 · ✅ pass

> Do the hepaciviruses discovered across Chondrichthyes, Actinopterygii, Sarcopterygii, and Reptilia exhibit a phylogenetic history consistent with virus-host co-divergence, or do discordances in the hepacivirus tree relative to the vertebrate host phylogeny indicate ancient cross-class host-switching events that shaped the evolutionary origin of hepatitis C virus?
>
> *Rationale:* Strong semantic match to GQ_002: compares virus and host trees to test co-divergence vs host-switching with concrete dataset citations, but it fails to include endogenous viral elements.

**Rank 2** · Comp = 1.000 · ✅ pass

> Do influenza viruses recovered from jawless fish (Agnatha: hagfish Eptatretus burgeri), ray-finned fish (Actinopterygii: spiny eel Mastacembelus aculeatus), and amphibians (Amphibia: Asiatic toad Bufo gargarizans) form a clade ancestral to avian and mammalian influenza viruses, indicating that the Orthomyxoviridae originated in aquatic non-tetrapod vertebrates rather than in birds?
>
> *Rationale:* The candidate explicitly uses MOESM3 metatranscriptomic influenza entries from divergent vertebrates to test whether these viruses are basal to avian/mammalian lineages, directly matching GQ_001's scope on ancient RNA-virus origins from broad vertebrate sampling.

**Rank 3** · Comp = 0.820 · ✅ pass

> Is tissue tropism conserved within each RNA virus family across phylogenetically disparate vertebrate host classes in this dataset, and does the degree of tropism conservation correlate with virus family age as inferred from the depth of host-class divergence spanned by each family?
>
> *Rationale:* The candidate aligns well with GQ_001 by testing deep virus–host associations and family age across vertebrate classes using MOESM3 tissue and host data, missing only an explicit mention of metatranscriptomic sampling.

**Rank 4** · Comp = 1.000 · ✅ pass

> Do hantaviruses (Bunyavirales: Hantaviridae) recovered from Actinopterygii (batfish Halieutaea stellata, goosefish Lophius litulon, spikefish Triacanthodes anomalus) and Agnatha (hagfish Eptatretus burgeri) represent an independent aquatic origin of this family that predates the rodent-associated hantaviruses, as evidenced by basal placement of the fish/jawless-fish sequences on the hantavirus phylogeny?
>
> *Rationale:* The candidate is a focused, well-grounded instantiation of GQ_001: it uses MOESM3 metatranscriptomic entries from multiple vertebrate classes to test whether Hantaviridae show an ancient aquatic origin via basal phylogenetic placement.

**Rank 5** · Comp = 0.640 · ✅ pass

> Does virus species richness (number of distinct virus families per host class) in this vertebrate virome survey scale with the phylogenetic diversity or sampling depth of each host class, and are Actinopterygii disproportionately virus-rich relative to their sequencing library count compared to Chondrichthyes and Amphibia?
>
> *Rationale:* The candidate aligns with GQ_001's sampling and host-association goals (uses MOESM2/MOESM3 counts and library depth) but does not address ancient origins or explicitly restrict to RNA-virus families, so it partially matches the gold intent.

### ✅ `gemini-3.1-pro` — Comp=0.260 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 5 | 1.300 | 0.260 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.020 | 0.204 | ❌ | GQ_002 (S) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Can the quantitative data provided in the Excel spreadsheets (MOESM2 and MOESM3) be used to independently reproduce the key findings or figures presented in the supplementary PDF (MOESM1)?
>
> *Rationale:* The candidate is a reproducibility/data-validation question about supplementary files and does not address the scientific intent of GQ_001 (vertebrate RNA-virus evolution), so it is unrelated despite concrete file grounding.

**Rank 2** · Comp = 0.260 · ❌ fail

> What specific variables or metrics are detailed in the larger Excel file (MOESM3) compared to the smaller one (MOESM2), and how do they relate to the overall study described in the PDF?
>
> *Rationale:* This is a well-grounded file-comparison question tied to specific supplementary files (high data grounding) but it does not address the scientific intent of GQ_001 (phylogeny, metatranscriptomics, virus-host evolutionary inference), so the semantic match is low.

**Rank 3** · Comp = 0.120 · ❌ fail

> Are there any discrepancies or missing data points between the datasets in the Excel files and the summarized results in the PDF?
>
> *Rationale:* The candidate is a data-integrity/audit question about supplementary Excel and PDF files and does not engage the scientific aims of GQ_001 (vertebrate RNA-virus evolution), though it is well-grounded in specific files.

**Rank 4** · Comp = 0.204 · ❌ fail

> What statistical methods are required to analyze the data in MOESM2 and MOESM3 to reach the conclusions presented in MOESM1?
>
> *Rationale:* The candidate is a methodological question about which stats to apply to specific supplemental files and thus is grounded in the data files but does not engage the scientific content (phylogenies, EVEs, codivergence) required by GQ_002.

**Rank 5** · Comp = 0.120 · ❌ fail

> Does the supplementary PDF (MOESM1) provide sufficient context and metadata to fully understand and utilize the datasets in the Excel files (MOESM2 and MOESM3)?
>
> *Rationale:* The candidate is a data-documentation question about specific supplement files and does not address the scientific intent of GQ_001 regarding vertebrate metatranscriptomic sampling or ancient RNA-virus evolution.

### ✅ `deepseek-v4-pro` — Comp=0.140 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.140 · ❌ fail

> Do somatic mutations in NOTCH1 exhibit a significantly greater increase in clone size with donor age compared to mutations in TP53 across histologically normal esophageal biopsies, as measured by variant allele frequency?
>
> *Rationale:* The candidate is a well-grounded, data-specific somatic-mutation question about NOTCH1/TP53 in human esophagus but is semantically unrelated to the selected gold question on vertebrate RNA-virus evolutionary associations.

**Rank 2** · Comp = 0.140 · ❌ fail

> Is the overall burden of non-synonymous somatic mutations per esophageal biopsy positively correlated with donor age, and does this correlation remain significant after controlling for biopsy-level sequencing depth?
>
> *Rationale:* The candidate addresses somatic mutation burden and age in human esophageal biopsies, which does not match the viral-evolution focus of GQ_001; however it is well grounded in the supplied MOESM2/MOESM3 files and statistical testing details.

**Rank 3** · Comp = 0.100 · ❌ fail

> Does the ratio of non-synonymous to synonymous mutations (dN/dS) in NOTCH1 exceed the genome-wide background dN/dS ratio across all esophageal biopsies, indicating positive selection acting specifically on NOTCH1 in normal tissue?
>
> *Rationale:* The candidate concerns somatic dN/dS in NOTCH1 from MOESM3 esophageal biopsies (somatic selection), which is unrelated to the matched gold question about vertebrate RNA-virus origins and so scores zero for intent alignment.

**Rank 4** · Comp = 0.120 · ❌ fail

> How does the spatial distribution of TP53-mutant clones across multiple biopsies from the same donor compare with that of NOTCH1-mutant clones, and does TP53 clonal spread show greater inter-biopsy dispersion suggesting earlier mutational timing?
>
> *Rationale:* The candidate is a somatic genomics question about TP53/NOTCH1 clonal spread in human biopsies and thus does not match the vertebrate RNA-virus intent of GQ_001, though it is well grounded in the listed MOESM2/MOESM3 files.

**Rank 5** · Comp = 0.140 · ❌ fail

> Do NOTCH1 mutations in normal esophageal biopsies display a mutational signature distinct from the background mutational spectrum of the same biopsies, and is the signature enriched for specific trinucleotide-context substitutions associated with oxidative damage?
>
> *Rationale:* The candidate asks about NOTCH1 mutational signatures in human esophagus, not vertebrate RNA-virus evolution, so it doesn't match GQ_001; however it is strongly grounded in the provided MOESM3 Excel file and trinucleotide-context data.

### ✅ `glm-5` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> What is the quantitative relationship between the two experimental datasets in MOESM2 and MOESM3, and does it reveal statistically significant differences between experimental conditions?
>
> *Rationale:* The candidate is a data-comparison/statistics question about two supplementary Excel files and does not address any elements of vertebrate RNA-virus evolutionary questions in GQ_001, though it is well grounded in the named files.

**Rank 2** · Comp = 0.120 · ❌ fail

> Do the numerical measurements in the supplementary Excel files demonstrate a dose-dependent or time-dependent response pattern?
>
> *Rationale:* The candidate is about dose/time patterns in Excel supplements and thus semantically unrelated to the gold question on vertebrate RNA-virus evolutionary history; it has strong grounding in specific supplementary files but contains none of the gold's required elements.

**Rank 3** · Comp = 0.100 · ❌ fail

> What is the correlation structure among variables in the larger dataset (MOESM3), and which variables show the strongest associations?
>
> *Rationale:* The candidate is a dataset-focused correlation question about MOESM3 and does not address any of the virology-evolution elements required by GQ_001, so it is unrelated though grounded to a specific file.

**Rank 4** · Comp = 0.120 · ❌ fail

> Are there outlier samples or measurements in the experimental data that deviate significantly from the overall distribution?
>
> *Rationale:* The candidate is a data-quality/outlier-detection question grounded in two Excel files and is semantically unrelated to the gold question about vertebrate RNA-virus evolution, so it matches none of the required elements.

**Rank 5** · Comp = 0.120 · ❌ fail

> What is the sample size and statistical power of the experimental design based on the data in the supplementary files?
>
> *Rationale:* The candidate is a methodological question about sample size/power and does not address the scientific intent of GQ_001 (ancient vertebrate RNA-virus associations), though it does concretely reference named supplementary Excel files.

### ✅ `gemini-2.5-flash` — Comp=0.200 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Can the quantitative relationships between experimental variables be determined from the provided supplementary Excel datasets?
>
> *Rationale:* The candidate is a dataset-analysis question focused on two Excel supplements and does not address vertebrate phylogeny, metatranscriptomics, or RNA-virus evolutionary questions posed by the gold.

**Rank 2** · Comp = 0.120 · ❌ fail

> Do the supplementary materials, including the PDF and Excel files, provide comprehensive data and methods necessary for independent replication of the study's results?
>
> *Rationale:* The candidate concerns reproducibility of provided supplementary PDF/XLSX files and thus does not capture the scientific intent of GQ_001 about vertebrate RNA-virus evolution; it contains no required elements but is well grounded in specific supplementary filenames.

**Rank 3** · Comp = 0.120 · ❌ fail

> What specific types of data (e.g., biological measurements, chemical properties, clinical outcomes) are organized within each of the two supplementary Excel spreadsheets?
>
> *Rationale:* The candidate is a metadata/content inspection question about two Excel files and is semantically unrelated to the gold question about broad vertebrate RNA-virus evolution; it contains no required evolutionary elements but is well grounded to the specific supplementary files.

**Rank 4** · Comp = 0.100 · ❌ fail

> Does the supplementary PDF document contain visual representations of data, such as figures or graphs, that support or extend the findings presented in the main article?
>
> *Rationale:* The candidate is unrelated to the gold question about vertebrate RNA-virus evolution; it instead asks about figures in a supplementary PDF and is grounded to a specific uploaded file (41586_2018_12_MOESM1_ESM.pdf).

**Rank 5** · Comp = 0.200 · ❌ fail

> Are there any overlapping or cross-referenced datasets between the two supplementary Excel files, and if so, how do they relate to each other?
>
> *Rationale:* The candidate is a file-level data-integration question, not about vertebrate phylogeny or ancient RNA-virus origins, so it has minimal semantic match to GQ_001 but is well grounded in the two supplementary Excel files.

### ✅ `intern-s1` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Is there a significant difference in gene expression levels between treated and untreated samples?
>
> *Rationale:* The candidate addresses gene-expression treatment effects, which does not match the viral-phylogeny and ancient virus-host association intent of GQ_001; it does, however, reference specific supplementary Excel files.

**Rank 2** · Comp = 0.100 · ❌ fail

> Can the results of the study be replicated using the same dataset?
>
> *Rationale:* The candidate asks about reproducibility using the same dataset, which is a different methodological question than GQ_001's evolutionary aim; it lacks all required thematic elements though it does reference a specific PDF file for grounding.

**Rank 3** · Comp = 0.080 · ❌ fail

> Is there a correlation between pollutant levels and health outcomes in the studied population?
>
> *Rationale:* The candidate addresses environmental pollutant–health correlations and cites two Excel files, which is specific data grounding but entirely unrelated to GQ_001's vertebrate RNA-virus/phylogeny focus; therefore match strength and required-element coverage are zero.

**Rank 4** · Comp = 0.120 · ❌ fail

> Are the observed effects statistically significant when controlling for confounding variables?
>
> *Rationale:* The candidate is a generic statistical-significance question about controlling confounders and references two supplemental xlsx files, but it does not address any core elements of the matched gold question about vertebrate metatranscriptomic viral evolution.

**Rank 5** · Comp = 0.120 · ❌ fail

> Does the drug significantly reduce symptoms compared to a placebo?
>
> *Rationale:* The candidate is a clinical trial efficacy question unrelated to vertebrate viral evolution; it references specific supplement files (good grounding) but contains none of the required elements of GQ_001 and thus matches very weakly.

### ✅ `intern-s1-pro` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What is the correlation between gene expression levels and protein abundance across different tissue samples in the supplementary dataset?
>
> *Rationale:* The candidate is about gene expression–protein abundance correlations in supplement files (good data grounding) but is unrelated to the viral-evolution intent of GQ_001, so match and required-element coverage are zero and it aligns more with generic unacceptable variants.

**Rank 2** · Comp = 0.120 · ❌ fail

> How does treatment duration affect cellular response metrics in the experimental time-course data?
>
> *Rationale:* The candidate is about treatment-duration effects in experimental time-course data and is unrelated to vertebrate RNA-virus evolution, so it matches no required elements though it is well grounded in the listed Excel/PDF files.

**Rank 3** · Comp = 0.120 · ❌ fail

> Are there significant differences in metabolic pathway activity between control and experimental groups as shown in the supplementary tables?
>
> *Rationale:* The candidate concerns metabolic pathway comparisons in supplementary Excel/PDF files and does not address vertebrate metatranscriptomics, virus phylogeny, EVEs, or ancient RNA-virus origins; GQ_001 was chosen as the least-worst match but intent and required elements are entirely unmet.

**Rank 4** · Comp = 0.120 · ❌ fail

> What environmental factors most strongly predict observed biological responses in the longitudinal dataset?
>
> *Rationale:* The candidate is semantically unrelated to the virus-evolution gold: it lacks all required virology elements (hence match_strength and coverage 0) but does reference specific provided files, so data grounding scores high.

**Rank 5** · Comp = 0.120 · ❌ fail

> How do the experimental conditions in the supplementary data support the proposed mechanism of cellular differentiation?
>
> *Rationale:* The candidate asks about validating a cellular-differentiation mechanism using supplemental Excel/PDF data, which does not address virus evolution or phylogeny required by GQ_001, though it is well grounded in the listed supplementary files.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.240 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.020 | 0.204 | ❌ | GQ_002 (S) |
| 5 | 1 | 0 | 2 | 4 | 1.020 | 0.204 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.240 · ❌ fail

> What are the key quantitative findings and statistical relationships documented in the supplementary data tables of Nature article 41586 (December 2018), and how do they support the main conclusions of the study?
>
> *Rationale:* The candidate is a general request to summarize supplementary quantitative results (well grounded in specific files) but does not ask about the core scientific topic of GQ_001 (vertebrate RNA-virus evolution and ancient host associations).

**Rank 2** · Comp = 0.120 · ❌ fail

> How do the sample sizes and experimental conditions documented in the supplementary Excel tables vary across different experimental groups in the study?
>
> *Rationale:* The candidate is a study-design/metadata question about Excel tables and sample sizes, not about vertebrate RNA-virus evolution or codivergence, though it is well grounded to the provided supplementary Excel files.

**Rank 3** · Comp = 0.120 · ❌ fail

> What temporal or spatial patterns are evident in the time-series or spatial data presented in the supplementary materials of this Nature study?
>
> *Rationale:* <<The candidate asks a generic temporal/spatial data-pattern question grounded to specific supplementary files but is unrelated to the matched gold question about vertebrate RNA-virus origins, so it covers none of the required elements.>>

**Rank 4** · Comp = 0.204 · ❌ fail

> What correlations or covariates are reported in the supplementary data tables, and which variables show the strongest associations with the primary outcome measures?
>
> *Rationale:* The candidate is a generic correlation request grounded in specific supplementary Excel files but lacks the phylogenetic/EVE elements central to GQ_002, so it only weakly matches the gold intent (association concept) while strongly grounding in data files.

**Rank 5** · Comp = 0.204 · ❌ fail

> What methodological details and parameter values are documented in the supplementary PDF and Excel files that would enable replication of the study's experimental procedures and data analysis?
>
> *Rationale:* The candidate is a methods/reproducibility question and does not address phylogenetic or EVE-based hypotheses in GQ_002, so it scores low on match and required-element coverage but is well grounded in the supplementary files.


## 11 · `zooplankton_rna_virosphere_2022`

- **raw**：10 文件: `16945363_31352431_chrysoviridae_alignment.fas, 16945399_31352560_Narnaviridae_alignment.fas, 16945423_31352587_Picornavirales_alignment.fas, 16945426_31352578_Partitiviridae_alignment.fas...`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.820 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 3 | 2 | 4 | 4 | 3.000 | 0.600 | ✅ | GQ_001 (P) |
| 5 | 5 | 3 | 4 | 4 | 4.100 | 0.820 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.620 · ✅ pass

> What is the family-level taxonomic composition and proportion of phylogenetically novel RdRp lineages among the 194 Hirai RNA-virus contigs, and which viral families (Partitiviridae, Totiviridae, Picobirnaviridae, Narnaviridae, Reoviridae, Chrysoviridae or Picornavirales) host the largest share of previously unreported diversity?
>
> *Rationale:* The candidate focuses tightly on RdRp contigs, family-level composition, and phylogenetic novelty (well grounded in specific files and counts), matching the gold's discovery intent but omitting FLDS/metatranscriptome, explicit zooplankton context, and host-association caveats.

**Rank 2** · Comp = 0.646 · ✅ pass

> Do the 37 Hirai_nohit contigs in 16958869_31373884_Possible_virus_contigs.fas form one or more deeply branching RdRp clades that fall outside the seven reference families represented in the alignment files, indicating candidate new RNA-virus families in this metagenome?
>
> *Rationale:* The candidate aligns well with GQ_002 by using RdRp contigs and multiple family alignment files to test classification into (or outside) reference families, but it omits explicit mention of ssRNA/dsRNA partitioning and 'bulk zooplankton' context while being strongly grounded in specific files.

**Rank 3** · Comp = 0.646 · ✅ pass

> Are the 12 contigs flagged 'complete' in 16945969_31356130_Hirai_Contigs_RdRp.fas, together with the 17 LC651635-LC651651 nuccore-reported genomes, sufficient to reconstruct full RdRp ORFs that recover the same family-level phylogenetic placements as the partial contigs they correspond to (e.g. contig_31_LC651635 Chryso-like, contig_2_LC651642 Picorna-like, contig_43_LC651648 Hypo-like)?
>
> *Rationale:* The candidate matches GQ_002's focus on RdRp-based family-level classification and is tightly grounded in specific files/IDs, but it omits explicit ssRNA/dsRNA phrasing and the 'bulk zooplankton' term.

**Rank 4** · Comp = 0.600 · ✅ pass

> Within the Pocobirnaviridae alignment, do the Hirai contigs and the GBH-prefixed Jam/St sample sequences form sample-specific monophyletic clades, suggesting picobirnavirus lineages stratified by host or sampling site?
>
> *Rationale:* The candidate targets host-association within a Pocobirnaviridae alignment (good semantic overlap with GQ_001's host-association aim) but is narrower and omits dataset-wide FLDS/metatranscriptome and virome-diversity framing.

**Rank 5** · Comp = 0.820 · ✅ pass

> Across the seven family RdRp alignments, do the Hirai contigs preferentially cluster with fungal- and protist-associated reference viruses (e.g. Aspergillus, Penicillium, Saccharomyces, Giardia, Leishmania, Trichomonas, Helminthosporium) rather than with arthropod- or vertebrate-host references, indicating that the source sample's RNA virome is dominated by viruses of microbial eukaryotic hosts?
>
> *Rationale:* The candidate strongly matches the gold's host-association intent and is well grounded in specific RdRp family alignments and Hirai contigs, but it omits explicit mention of FLDS/metatranscriptome methods, the zooplankton-community label, and a broad 'diversity' framing.

### ✅ `gpt-5.5-high` — Comp=0.680 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> Which Hirai viral RdRp contigs represent novel RNA virus lineages, and how are those lineages phylogenetically distributed across Partiti-like, Toti-like, Picobirna-like, Narna-like, Reo-like, Chryso-like, and Picorna-like reference groups?
>
> *Rationale:* The candidate targets RdRp contigs and family-level phylogenetic placement (matching GQ_002's classification aim), is tightly grounded in the listed alignment and Hirai contig files, but omits explicit ssRNA/dsRNA framing and the 'bulk zooplankton' sample context.

**Rank 2** · Comp = 0.646 · ✅ pass

> Are the numerous Hirai Partiti-like RdRp contigs a single expanded partitivirus-like clade or multiple independent lineages relative to the Partitiviridae reference alignment?
>
> *Rationale:* The candidate well matches GQ_002's focus on RdRp-based, family-level classification using the Partitiviridae alignment and is strongly data-grounded, but it omits explicit ssRNA/dsRNA comparison and the 'bulk zooplankton' phrasing.

**Rank 3** · Comp = 0.520 · ❌ fail

> Do the complete LC651635-LC651651 viral metagenome records define multi-segment viral genomes that can be linked to the RdRp-classified Hirai contigs?
>
> *Rationale:* Matches the RdRP-centric virome intent but misses the required zooplankton/FLDS framing and broader diversity/host-association elements; very well grounded in specific files and accessions.

**Rank 4** · Comp = 0.620 · ✅ pass

> Are the 37 Hirai possible-virus contigs additional unclassified viral segments related to the RdRp-defined Hirai virome based on length, GC content, coding potential, and matches to reported viral sequences?
>
> *Rationale:* The candidate aligns well with GQ_001's virome-discovery and RdRP focus and is strongly data-grounded, but it omits explicit FLDS/zooplankton context and any host-association caveat, so it partially matches the gold intent.

**Rank 5** · Comp = 0.527 · ❌ fail

> Do Hirai Reo-like and Narna-like RdRp sequences show stronger divergence from known references than the Chryso-like and Picorna-like Hirai sequences?
>
> *Rationale:* Matches GQ_002: candidate uses family alignments and compares divergence across Hirai RdRp families (Reo/Narna vs Chryso/Picornavirales), addressing family-level separation but omitting OTU clustering and bulk-zooplankton context; strongly grounded in specific alignment files and contig identity values.

### ✅ `claude-code-sonnet-4-6` — Comp=0.800 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 2 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.700 · ✅ pass

> Do the 75 Partitiviridae-like RNA virus contigs recovered from the Hirai 2021 metagenomic sample represent a monophyletic arthropod-infecting clade or multiple independent host-switching events from fungal/plant partitivirus lineages, as determinable by RdRp-based maximum-likelihood phylogenetic analysis of the 16945426_31352578_Partitiviridae_alignment.fas dataset?
>
> *Rationale:* The candidate well matches the gold's host-association intent using RdRp phylogenetics and is tightly grounded in specific alignment and contig files, but it omits explicit mention of FLDS/metatranscriptome protocols and does not state 'zooplankton community' nor broader RNA-virosphere-level scope.

**Rank 2** · Comp = 0.700 · ✅ pass

> Do the 10 Totiviridae-like Hirai contigs that cluster with protozoan RNA viruses (Giardia lamblia virus, Leishmania RNA virus 1-1, Trichomonas vaginalis virus 1) in the 16945477_31352614_Totiviridae_alignment.fas phylogeny represent a novel clade of protozoan-infecting totiviruses in the Hirai metagenome source, or alternatively a distinct arthropod-infecting lineage convergently resembling protozoan totivirus RdRps?
>
> *Rationale:* Mapped to GQ_001 because the candidate is a concrete RdRp-based host-association question grounded in specific Totiviridae alignments, but it omits the original's FLDS/metatranscriptome and zooplankton-community scope and broader virosphere-diversity framing.

**Rank 3** · Comp = 0.800 · ✅ pass

> Can the 35 nucleotide sequences in 16958869_31373884_Possible_virus_contigs.fas that lack detectable homology to any known virus (nohit sequences) be assigned to novel virus families through iterative profile-based RdRp domain searches, and do the co-occurring putative capsid and hypothetical protein sequences in the same file indicate a complete bipartite or tripartite genome organization for at least one novel virus?
>
> *Rationale:* The candidate is a focused discovery question matching GQ_001's intent (RdRp-driven novel virome discovery) and is well grounded in specific files, but it omits the host-association caveat required by the gold question.

**Rank 4** · Comp = 0.560 · ❌ fail

> Does the single Hirai contig placed within the Reoviridae alignment (16945462_31352605_Reoviridae_alignment.fas) represent a segment of a multi-segmented reovirus genome, and if so, can additional genomic segments be identified among the 14 Reo-like partial contigs in 16945969_31356130_Hirai_Contigs_RdRp.fas through sequence co-abundance and cross-clustering analysis?
>
> *Rationale:* Candidate examines RdRP contigs and host association (matches GQ_001 focus) and is well grounded in specific alignment and contig files, but it omits FLDS/metatranscriptome and explicit zooplankton-community and broad virosphere diversity elements.

**Rank 5** · Comp = 0.697 · ✅ pass

> Across the seven Hirai 2021 viral family-specific RdRp phylogenetic alignments (Chrysoviridae, Narnaviridae, Picornavirales, Partitiviridae, Pocobirnaviridae, Reoviridae, Totiviridae), is there a significant enrichment of novel Hirai contigs in dsRNA virus families (Partitiviridae, Totiviridae, Pocobirnaviridae, Reoviridae) compared to positive-sense ssRNA families (Picornavirales), consistent with the known dominance of dsRNA viruses in invertebrate-associated mycovirus-rich environments?
>
> *Rationale:* The candidate aligns well with GQ_002 by using family-level RdRp alignments to compare dsRNA vs ssRNA diversity and is strongly grounded in the provided alignment files and contig counts, but it omits explicit mention of a bulk zooplankton sample context.

### ✅ `gemini-3.1-pro` — Comp=0.561 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 2 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.510 · ❌ fail

> Where do the newly assembled viral contigs place within the established phylogeny of known RNA virus families?
>
> *Rationale:* The candidate matches GQ_002's family-level phylogenetic classification intent and is well grounded in specific RdRp and family alignment files, but it lacks explicit OTU-clustering, ssRNA/dsRNA distinction, and the bulk zooplankton sample context.

**Rank 2** · Comp = 0.561 · ❌ fail

> What is the diversity and relative abundance of different viral families within the sampled metagenome?
>
> *Rationale:* The candidate aligns with GQ_002's family-level classification intent (references RdRP contigs and alignment files) but omits OTU-clustering, explicit ssRNA/dsRNA separation, and the zooplankton sample context, so it's a partial match grounded in specific files.

**Rank 3** · Comp = 0.476 · ❌ fail

> Are there novel, deeply branching viral lineages present in the contig datasets that do not cluster with any of the provided reference families?
>
> *Rationale:* The candidate targets novel deep-branching contig clades vs reference families (family-level classification) and is grounded in specific RdRp contig files, but omits OTU clustering, ssRNA/dsRNA partitioning, and the bulk zooplankton context required by GQ_002.

**Rank 4** · Comp = 0.425 · ❌ fail

> What are the conserved sequence motifs within the RdRp genes across the different viral families represented in the dataset?
>
> *Rationale:* Uses family-level RdRp alignments in the dataset (matching GQ_002's alignment focus) but lacks OTU clustering, ssRNA/dsRNA distinction, and bulk zooplankton/classification framing; well grounded in specific alignment files.

**Rank 5** · Comp = 0.380 · ❌ fail

> Do the 'Possible_virus_contigs' represent complete viral genomes or only partial fragments, and how does this compare to the reported viral sequences?
>
> *Rationale:* The candidate deals with viral contigs in the provided files and genome completeness (not virome diversity or host links), so it partially overlaps GQ_001's domain but misses most required elements while being well grounded in specific files.

### ✅ `deepseek-v4-pro` — Comp=0.700 · Pass@1=0.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 3 | 4 | 2 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 4 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.578 · ❌ fail

> Do the unclassified dsRNA virus contigs and 'Hirai_nohit' sequences in this dataset form monophyletic clades that represent previously undescribed RNA virus families distinct from the seven known families represented in the curated alignments?
>
> *Rationale:* The candidate aligns well with GQ_002's methods (RdRp phylogeny and family MSAs) and is grounded in specific files and contigs, but it narrows scope to dsRNA and lacks the explicit bulk-zooplankton / ssRNA vs dsRNA comparison required by GQ_002.

**Rank 2** · Comp = 0.700 · ✅ pass

> What is the host-range breadth of the novel Picorna-like and Narna-like contigs in this dataset, as inferred by phylogenetic proximity to reference sequences with known host associations?
>
> *Rationale:* Candidate matches GQ_001's host-association aim via RdRP phylogenies (files cited) but is narrower (host-range for Picorna/Narna) and omits explicit mention of FLDS/metatranscriptome, zooplankton community, and broad virosphere diversity.

**Rank 3** · Comp = 0.680 · ✅ pass

> Do the Partitiviridae and Totiviridae alignments reveal evidence of recent horizontal virus transfer between fungal and invertebrate hosts, based on incongruence between virus phylogeny and host taxonomy?
>
> *Rationale:* The candidate well targets GQ_001's host-association aim using specific RdRp alignments and files, but omits explicit FLDS/metatranscriptome provenance, a stated zooplankton community, and the broader virosphere diversity framing.

**Rank 4** · Comp = 0.374 · ❌ fail

> Are the evolutionary rates of RdRp significantly different between dsRNA virus families (Reoviridae, Chrysoviridae, Partitiviridae, Totiviridae, Pocobirnaviridae) and (+)ssRNA lineages (Picornavirales, Narnaviridae) in this dataset, and does rate variation correlate with genome segmentation strategy?
>
> *Rationale:* Mapped to GQ_002 because it shares family alignments and ssRNA/dsRNA contrast but asks about evolutionary rates and segmentation rather than OTU clustering/classification; covers 2/5 required elements and is grounded in multiple family alignment files.

**Rank 5** · Comp = 0.420 · ❌ fail

> Can the 'Hirai_virus_capsid' sequence in the Possible_virus_contigs file be linked to a specific RdRp-bearing contig through paired genomic termini or conserved intergenic signals, enabling complete or near-complete genome reconstruction for a novel virus?
>
> *Rationale:* The candidate is a focused genome-reconstruction question tied to specific contigs (good data grounding) but does not address the gold's broader community-level diversity and host-association aims, so it only partially matches the primary gold intent.

### ✅ `glm-5` — Comp=0.680 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 3 | 5 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 2 | 4 | 2 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 5 | 2 | 3 | 3 | 5 | 2.380 | 0.476 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.660 · ✅ pass

> What proportion of the novel RNA virus contigs discovered in this metagenomic dataset represent previously uncharacterized viral lineages, and how does their taxonomic distribution across established virus families inform our understanding of RNA virus diversity and evolution?
>
> *Rationale:* The candidate captures virome-discovery and novelty assessment using RdRP contigs and family alignments (well grounded in specific files) but omits key context required by GQ_001: FLDS/metatranscriptome methods, explicit zooplankton sampling, and host-association cautions.

**Rank 2** · Comp = 0.680 · ✅ pass

> How do the phylogenetic relationships between the novel viral contigs and reference sequences in the alignment files reveal patterns of RNA virus evolution and potential host associations?
>
> *Rationale:* The candidate matches the gold's focus on using RdRp/alignments to infer host associations and evolutionary patterns but omits explicit FLDS/metatranscriptome and zooplankton-community framing, and only implies diversity rather than stating it.

**Rank 3** · Comp = 0.560 · ❌ fail

> What genomic and sequence characteristics distinguish the 'Hirai_nohit' viral contigs from classified sequences, and do these features suggest they represent novel virus taxa or highly divergent lineages?
>
> *Rationale:* The candidate focuses on novel/divergent RdRP-bearing contigs and is grounded in specific files, matching the discovery intent of GQ_001 but missing FLDS/metatranscriptome, zooplankton context, and host-association considerations.

**Rank 4** · Comp = 0.500 · ❌ fail

> How does the diversity of RNA virus families represented in this dataset compare to known viral diversity patterns, and what ecological or environmental factors might explain the observed taxonomic distribution?
>
> *Rationale:* The candidate addresses RNA virus family diversity and ecological explanations (matching the gold's diversity intent) but omits key dataset/context requirements (zooplankton, FLDS/metatranscriptome, RdRP), so it is partially aligned and well-grounded in specific alignment files.

**Rank 5** · Comp = 0.476 · ❌ fail

> What evolutionary relationships exist between the novel RNA virus contigs and the reference sequences from NCBI's nucleotide database, and do these relationships suggest recent divergence events or ancient evolutionary lineages?
>
> *Rationale:* The candidate aligns with GQ_002's phylogenetic/classification theme (uses RdRp and family alignments) but diverges by focusing on divergence timing and omitting OTU clustering, ssRNA/dsRNA separation, and explicit bulk zooplankton context.

### ✅ `gemini-2.5-flash` — Comp=0.629 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 2 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 4 | 1.275 | 0.255 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.629 · ✅ pass

> How do the newly identified viral contigs, particularly those containing RdRp sequences, relate phylogenetically to known viral families represented in the provided alignment files?
>
> *Rationale:* Asks about phylogenetic classification of RdRp contigs using provided family alignments (aligns with GQ_002), but omits explicit bulk-zooplankton context, ssRNA/dsRNA distinction, and OTU-clustering phrasing.

**Rank 2** · Comp = 0.408 · ❌ fail

> What is the degree of sequence conservation within the RdRp gene across the different viral families represented in the dataset?
>
> *Rationale:* The candidate fits the RdRp/family-alignment theme (uses many alignment files) but asks about sequence conservation rather than OTU clustering, ssRNA/dsRNA separation, or classification, so it partially matches GQ_002.

**Rank 3** · Comp = 0.560 · ❌ fail

> Does the `nuccore_reported_viral_sequences.fasta` file contain sequences that represent novel viral species or significant variants of known viruses, particularly those related to the families in the alignment files?
>
> *Rationale:* Candidate aligns with virome discovery via RdRp/family comparisons (GQ_001 intent) but omits the zooplankton/FLDS context and host-association caution required by the gold question.

**Rank 4** · Comp = 0.425 · ❌ fail

> Are there significant differences in the predicted protein length or domain architecture of the RdRp genes among the various viral families and novel contigs?
>
> *Rationale:* Matched to GQ_002 (secondary). The candidate targets RdRp length/domain differences across viral families and contigs with concrete alignment files, but it omits OTU clustering, ssRNA/dsRNA distinction, bulk zooplankton context, and explicit classification intent.

**Rank 5** · Comp = 0.255 · ❌ fail

> Are there indications of recombination events within the RdRp genes of the novel contigs or sequences from `nuccore_reported_viral_sequences.fasta` when compared to known viral RdRp sequences?
>
> *Rationale:* The candidate concerns recombination in RdRp sequences—it references dataset files and RdRp contigs but does not ask about OTU clustering, family alignments, ssRNA/dsRNA separation, bulk zooplankton, or classification, so it poorly matches GQ_002.

### ✅ `intern-s1` — Comp=0.510 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 5 | 0 | 1 | 2 | 4 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.510 · ❌ fail

> How do RdRp gene phylogenies reflect evolutionary relationships among the identified viral families in the dataset?
>
> *Rationale:* The candidate targets RdRp-based phylogenetic classification (aligns with GQ_002 family-level intent) and cites specific RdRp files, but it omits OTU clustering, ssRNA/dsRNA distinction, and explicit bulk zooplankton context, reducing full alignment with the gold question.

**Rank 2** · Comp = 0.323 · ❌ fail

> What is the distribution of partial vs. complete viral genomes across different virus families in the dataset?
>
> *Rationale:* The candidate is about genome completeness by viral family so it only aligns to GQ_002's family-alignment aspect (hence low match and required-element coverage), but it lacks RdRP/OTU, ssRNA/dsRNA, and zooplankton classification; it is well grounded in specific alignment files.

**Rank 3** · Comp = 0.323 · ❌ fail

> Are there conserved nucleotide motifs across different viral families that suggest horizontal gene transfer?
>
> *Rationale:* Selected GQ_002 because of family-level alignment overlap; candidate diverges by focusing on conserved motifs/HGT rather than RdRP OTU clustering or ssRNA/dsRNA classification, covering only the alignment element but grounded in specific alignment files.

**Rank 4** · Comp = 0.357 · ❌ fail

> How do nucleotide composition biases (e.g., GC content) vary between viral families in the dataset?
>
> *Rationale:* Matches GQ_002 only on family-level alignments (files cited) but diverges substantially by focusing on nucleotide composition rather than RdRP clustering, ssRNA/dsRNA separation, bulk zooplankton, or classification.

**Rank 5** · Comp = 0.220 · ❌ fail

> Can viral genome completeness predict the presence of host interaction-related genes?
>
> *Rationale:* The candidate concerns genome completeness and host-interaction genes, which only matches GQ_001's host-association element; it lacks FLDS/metatranscriptome, zooplankton, RdRP, and virome diversity focus, though it is grounded to specific files.

### ✅ `intern-s1-pro` — Comp=0.578 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 3 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 4 | 4 | 2 | 4 | 4 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.561 · ❌ fail

> What novel viral lineages or recombination events can be identified from the unclassified RdRp-containing contigs when compared against the established viral family alignments?
>
> *Rationale:* The candidate aligns with GQ_002 by using RdRp contigs and family alignments for phylogenetic classification, adds recombination/novel-lineage aims, but omits explicit ssRNA/dsRNA partitioning and bulk zooplankton framing.

**Rank 2** · Comp = 0.425 · ❌ fail

> What are the evolutionary relationships and potential cross-family recombination patterns between the different viral families represented in the alignment datasets?
>
> *Rationale:* The candidate aligns with family-level alignment analysis (GQ_002) but shifts to phylogenetic and recombination questions and omits OTU clustering, ssRNA/dsRNA partitioning, and the bulk zooplankton classification focus.

**Rank 3** · Comp = 0.425 · ❌ fail

> How conserved are the RdRp domains across different viral families, and what does this conservation reveal about functional constraints and evolutionary rates?
>
> *Rationale:* The candidate aligns with GQ_002 on RdRp and family alignments but pivots to conservation and evolutionary-rate questions, missing OTU clustering, ssRNA/dsRNA separation, zooplankton context, and classification; it is well grounded in specific provided alignment files.

**Rank 4** · Comp = 0.578 · ❌ fail

> Can the unclassified viral contigs be taxonomically assigned to specific viral families based on phylogenetic analysis of their RdRp sequences?
>
> *Rationale:* The candidate well matches GQ_002's family-level RdRp classification aim and cites specific alignment files, but it omits OTU-clustering, the zooplankton sample context, and explicit ssRNA/dsRNA separation.

**Rank 5** · Comp = 0.560 · ❌ fail

> What is the diversity and distribution pattern of viral sequences across different host-associated environments represented in the dataset?
>
> *Rationale:* The candidate aligns with GQ_001's focus on virosphere diversity and host associations but generalizes beyond zooplankton and omits explicit mention of FLDS/metatranscriptome and RdRP contigs; it is grounded in several specific alignment/contig files.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.561 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 2 | 3 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 5 | 5 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.561 · ❌ fail

> What is the phylogenetic relationship between novel viral metagenomic contigs and established virus families based on RdRp sequence conservation?
>
> *Rationale:* The candidate aligns with GQ_002's classification/phylogeny focus using RdRp and family alignments (files cited) but lacks the explicit bulk-zooplankton context and the ssRNA/dsRNA partitioning emphasis required by the gold.

**Rank 2** · Comp = 0.374 · ❌ fail

> Which amino acid residues in the chrysovirus RdRp alignment are most conserved across the 18 chrysovirus species, and what functional roles might they play?
>
> *Rationale:* The candidate matches GQ_002 only in using a family RdRp alignment (Chrysoviridae) but diverges by asking about residue conservation and function rather than OTU clustering, ssRNA/dsRNA separation, or zooplankton-based classification; it is grounded to a specific alignment file.

**Rank 3** · Comp = 0.561 · ❌ fail

> How do the putative classifications of Hirai contigs (e.g., 'Picorna-like', 'Tombus-like') compare to their actual sequence similarity to reference alignments of those virus families?
>
> *Rationale:* The candidate is best matched to GQ_002 because it aims to validate contig classifications via family alignments with strong file-level grounding, but it lacks OTU-clustering, explicit ssRNA/dsRNA framing, and explicit bulk-zooplankton context.

**Rank 4** · Comp = 0.360 · ❌ fail

> What is the diversity of gene types (RdRp, capsid, polyprotein, hypothetical) represented in the reported viral metagenome sequences, and what does this reveal about viral metagenomic sampling bias?
>
> *Rationale:* The candidate addresses viral gene-type composition and sampling bias with concrete reference to nuccore_reported_viral_sequences.fasta and RdRp, but it lacks the zooplankton/FLDS context and host-association focus central to GQ_001.

**Rank 5** · Comp = 0.357 · ❌ fail

> Are there conserved structural motifs shared across multiple virus families (e.g., Chrysoviridae, Narnaviridae, Picornavirales) that suggest common evolutionary origins or convergent evolution?
>
> *Rationale:* The candidate leverages family-level alignments (matching available files) to ask about cross-family conserved motifs and evolution, but it omits RdRP OTU clustering, the ssRNA/dsRNA partitioning goal, bulk zooplankton context, and explicit classification aims from GQ_002.
