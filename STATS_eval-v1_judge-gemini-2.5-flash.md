# eval-v1 系统评测 · judge=`gemini-2.5-flash`

qset 数：**11** · agent 数：**11** · judge：**`gemini-2.5-flash`**

成功格子：**89** · 失败格子：**32** · 缺数据：**0**

评分维度：`match_strength` / `required_elements_coverage` / `acceptability` / `data_grounding`（各 0–5）· Comp 0–1 = 4 维加权

⚪ = `intern-s1-mini` 用户决定不再重测，保留首轮结果


## 0 · 覆盖矩阵

| qset | cc-opus-4-7 | gpt-5.5-high | cc-sonnet-4-6 | gem-3.1-pro | ds-v4-pro | glm-5 | gem-2.5-flash | intern-s1 | intern-s1-pro | intern-s1-mini ⚪ | intern-s2-prv |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `amphibian_reptile_virome_2022` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `arthropod_neg_sense_2015` | 🟢 | ✅ | 🟢 | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ⚪ | ❌ |
| `bat_btcn_virome_2024` | 🟢 | ❌ | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ |
| `flavi_jingmen_jvi_2016` | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `invertebrate_rna_virosphere_2016` | ✅ | 🟢 | 🟢 | 🟢 | 🟢 | ✅ | 🟢 | 🟢 | ✅ | ⚪ | ✅ |
| `oyster_rna_virome_2024` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `rvmt_cell_2022` | ❌ | 🟢 | ✅ | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `tara_oceans_science_2022` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ⚪ | ❌ |
| `tick_metavirome_2023` | 🟢 | ✅ | 🟢 | ✅ | 🟢 | 🟢 | 🟢 | ✅ | 🟢 | ⚪ | 🟢 |
| `vertebrate_rna_viruses_2018` | 🟢 | 🟢 | 🟢 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚪ | ✅ |
| `zooplankton_rna_virosphere_2022` | ❌ | ❌ | ❌ | 🟢 | ❌ | ❌ | ❌ | ✅ | ✅ | ⚪ | ❌ |
| **合计 ✅** | **7/11** | **8/11** | **10/11** | **10/11** | **7/11** | **7/11** | **10/11** | **10/11** | **10/11** | **2/11** | **8/11** |

> 🟢 = pass@1 通过 · ✅ = 跑成功但 rank-1 没过 · ❌ = 5+ 次重试都没救活 · ⚪ = `intern-s1-mini` 不再重测 · 🟨 = 缺数据

## 1 · 各 agent 跨 qset 平均分（缺/失败按 0 计入；按 Comp 排序）

| Agent | 已成功 | match | req_elem | accept | data_grnd | Comp 0–1 | Pass@1 | Pass@5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `claude-code-sonnet-4-6` | 10/11 | 4.18 | 3.91 | 4.27 | 4.45 | **0.793** | 0.636 | 0.618 |
| `claude-code-opus-4-7` | 7/11 | 3.00 | 3.09 | 3.09 | 3.18 | **0.572** | 0.545 | 0.436 |
| `gpt-5.5-high` | 8/11 | 3.09 | 2.64 | 3.18 | 3.64 | **0.563** | 0.455 | 0.418 |
| `gemini-3.1-pro` | 10/11 | 2.45 | 1.82 | 2.64 | 4.09 | **0.442** | 0.364 | 0.209 |
| `gemini-2.5-flash` | 10/11 | 1.73 | 1.64 | 2.27 | 3.64 | **0.362** | 0.273 | 0.177 |
| `intern-s1-pro` | 10/11 | 1.73 | 1.18 | 2.00 | 3.73 | **0.336** | 0.091 | 0.068 |
| `deepseek-v4-pro` | 7/11 | 1.36 | 1.55 | 1.82 | 2.82 | **0.301** | 0.273 | 0.200 |
| `intern-s1` | 10/11 | 1.45 | 1.00 | 2.09 | 3.45 | **0.300** | 0.182 | 0.073 |
| `intern-s2-preview` | 8/11 | 1.27 | 1.09 | 1.45 | 3.09 | **0.259** | 0.091 | 0.068 |
| `glm-5` | 7/11 | 1.18 | 0.91 | 1.18 | 2.73 | **0.229** | 0.182 | 0.109 |
| `intern-s1-mini` ⚪ | 2/11 | 0.36 | 0.18 | 0.27 | 0.64 | **0.055** | 0.000 | 0.000 |


---
# Part II · 每个 (qset, agent) 的 5 个候选问题 + 完整文本


## 1 · `amphibian_reptile_virome_2022`

- **raw**：1 文件: `43705_2022_180_MOESM1_ESM.docx`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 2 | 3 | 4 | 5 | 3.000 | 0.600 | ✅ | GQ_001 (P) |
| 3 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 2 | 3 | 3 | 4 | 2.295 | 0.459 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Do amphibians and reptiles harbour RNA viruses phylogenetically nested within or sister to vertebrate-pathogenic families (Rhabdoviridae/Lyssavirus, Orthomyxoviridae, Hepeviridae, Caliciviridae, Astroviridae, Bunyavirales), and does the host taxonomy, geography and tissue distribution recoverable from the 234 public RNA-Seq libraries indicate that herptiles constitute a previously underappreciated reservoir for relatives of mammalian/avian zoonotic viruses?
>
> *Rationale:* The candidate question is an excellent, highly detailed match for GQ_002, focusing on the phylogenetic placement of amphibian/reptile RNA viruses relative to known pathogenic families and their potential as zoonotic reservoirs, with strong data grounding.

**Rank 2** · Comp = 0.600 · ✅ pass

> How does host tissue type and poly(A) library-selection status, as recorded across the 234 RNA-Seq libraries in Supplementary Table 1, bias the recovery of negative-sense versus positive-sense RNA viruses (e.g. Bunyavirales and Lyssaviruses versus Astro-, Hepe- and Caliciviridae) in herptile meta-transcriptomic surveys?
>
> *Rationale:* The candidate question addresses methodological bias in viral recovery from herptile RNA-seq, a related but distinct intent from the gold's focus on revealing hidden diversity. It is well-grounded in data and well-phrased, but doesn't fully align with the gold's core elements.

**Rank 3** · Comp = 0.340 · ❌ fail

> Is the recombination breakpoint observed between the non-structural and structural gene blocks of the novel herptile Hepeviridae and Astroviridae (Supplementary Figure 3) a recurrent evolutionary feature shared with reference astro-/hepeviruses, and does it correlate with host-class jumps between amphibians and reptiles?
>
> *Rationale:* The candidate asks a highly specific mechanistic question about recombination breakpoints and host-jump correlation in Astroviridae/Hepeviridae. While it falls under the broad category of viral evolution in herptiles, it misses the core intent of GQ_002 regarding the phylogenetic placement and novelty of recovered viruses relative to known families.

**Rank 4** · Comp = 0.850 · ✅ pass

> Does the presence of an alligator-associated rabies-like lyssavirus and an anole lyssa-like virus, together with the tuatara, crocodilian, snake and turtle libraries in Supplementary Table 1, support a deep evolutionary origin of Lyssavirus or Lyssavirus-like rhabdoviruses in non-avian sauropsids predating the mammalian radiation?
>
> *Rationale:* The candidate effectively asks whether specific reptile-associated lyssa-like viruses occupy positions that suggest a deeper evolutionary history than previously thought, grounding the inquiry in concrete host and phylogenetic data from the provided supplementary materials.

**Rank 5** · Comp = 0.459 · ❌ fail

> Given that French Guianan caecilians (40 libraries), Cuban anoles (16), Chinese reptiles (32) and Australian herptiles (17) form the largest geographic clusters in Supplementary Table 1, are the novel virus lineages described in Supplementary Figures 1–5 geographically structured — i.e. do biogeographic boundaries shape the herptile RNA virome at the level of viral family and species?
>
> *Rationale:* The candidate question investigates the biogeographic structure of novel herptile viruses, aligning with GQ_002's focus on analyzing characteristics of recovered viruses in herptiles and viral families. However, it diverges on the specific characteristic (geographical structure vs. phylogenetic novelty). It is well-grounded in specific data features.

### ✅ `gpt-5.5-high` — Comp=0.850 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 3 | 3.900 | 0.780 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 4 | 4.165 | 0.833 | ✅ | GQ_002 (S) |
| 3 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.780 · ✅ pass

> Do publicly available amphibian and reptile RNA-seq datasets reveal divergent RNA viruses that expand the known host range and phylogenetic diversity of major vertebrate virus families?
>
> *Rationale:* The candidate effectively targets the discovery of novel viral diversity in amphibian and reptile transcriptomes. It is scientifically sound, well-grounded in the provided supplementary document list, and aligns closely with the goals of public transcriptome mining for virome discovery.

**Rank 2** · Comp = 0.833 · ✅ pass

> Do reptile transcriptomes contain lyssavirus-like rhabdoviruses related to rabies lyssavirus, indicating that lyssavirus diversity extends beyond its better-known mammalian reservoirs?
>
> *Rationale:* The candidate question strongly matches GQ_002 by focusing on whether reptile-derived lyssaviruses represent an extension of diversity beyond known mammalian reservoirs, directly implying a phylogenetic assessment of their position within viral families. All required elements are covered, and it is highly specific and well-grounded in data.

**Rank 3** · Comp = 0.850 · ✅ pass

> Do newt RNA-seq data contain divergent viruses from multiple RNA virus families, including influenza-like, hepevirus, and calicivirus lineages?
>
> *Rationale:* The candidate question precisely asks about divergent viruses within specific RNA virus families in newt RNA-seq data, directly matching the phylogenetic novelty intent of GQ_002. It is well-grounded with specific data features.

**Rank 4** · Comp = 0.850 · ✅ pass

> Do reptile RNA-seq datasets uncover novel Bunyavirales lineages that clarify the evolutionary placement of reptile-associated arenaviruses, hantaviruses, and related viruses?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, focusing on the phylogenetic placement of novel reptile viruses within known families. It covers all required elements, is highly acceptable, and is well-grounded in specific data features.

**Rank 5** · Comp = 0.850 · ✅ pass

> Do amphibian and reptile hepevirus and astrovirus contigs show gene-level phylogenetic patterns consistent with deep divergence or recombination near structural and non-structural genome regions?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, focusing on phylogenetic patterns and deep divergence for specific amphibian/reptile viruses. It covers all required elements, is highly specific, and is well-grounded in the provided data features, referencing specific figures and viral examples.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 4 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 2 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 3 | 4 | 5 | 4 | 4 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 4 | 5 | 5 | 5 | 4 | 4.165 | 0.833 | ✅ | GQ_002 (S) |
| 5 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.748 · ✅ pass

> Does host phylogenetic distance from mammalian lyssavirus reservoirs predict nucleoprotein N-gene divergence of novel herptile lyssaviruses, supporting pre-mammalian evolutionary origin?
>
> *Rationale:* The candidate question effectively addresses the phylogenetic novelty of herptile lyssaviruses, aligning well with GQ_002. It covers all required elements, is highly specific, and demonstrates strong data grounding by referencing specific genes, figures, and SRA accessions.

**Rank 2** · Comp = 0.740 · ✅ pass

> Does poly-A library selection bias in RNA-Seq samples from Supplementary Table 1 systematically inflate discovery rates of positive-sense ssRNA viruses such as Hepeviridae and Astroviridae relative to negative-sense RNA viruses in herptile transcriptomes?
>
> *Rationale:* The candidate question addresses a specific methodological bias in the discovery of viral diversity in herptile RNA-seq data, aligning with the broader theme of GQ_001. It is highly specific, well-grounded in data, and scientifically rigorous, though it frames a critique of the discovery process rather than a direct discovery question.

**Rank 3** · Comp = 0.860 · ✅ pass

> Does the sampled tissue type in Supplementary Table 1 predict the probability of discovering novel RNA viruses in herptile transcriptomes, with liver-derived samples exhibiting lower novel virus detection than mixed-viscera samples?
>
> *Rationale:* The candidate question closely aligns with the gold's intent of discovering novel viruses in herptile transcriptomes, specifically investigating the impact of tissue type. It covers most required elements and is well-grounded in specific data features, demonstrating high scientific quality.

**Rank 4** · Comp = 0.833 · ✅ pass

> Does the PB1 polymerase phylogeny of the novel newt influenza virus from Cynops pyrrhogaster SRR1553357 indicate an independent host-jump from birds into Urodela, or does it represent basal divergence predating the avian influenza radiation?
>
> *Rationale:* The candidate question precisely addresses the phylogenetic placement of a newt influenza virus, asking if its PB1 polymerase phylogeny indicates a host-jump or basal divergence, directly matching GQ_002's focus on basal/divergent positions within viral families.

**Rank 5** · Comp = 1.000 · ✅ pass

> Are caecilians (order Gymnophiona, approximately 40 RNA-Seq runs in Supplementary Table 1) disproportionately under-represented in novel virus discovery relative to their sampling depth compared to anurans and reptiles, suggesting a genuine virome gap in this understudied amphibian order?
>
> *Rationale:* The candidate question precisely targets the discovery of hidden viral diversity in an under-sampled amphibian group (caecilians) using RNA-seq data, aligning perfectly with the gold's intent and covering all required elements with strong data grounding.

### ✅ `gemini-3.1-pro` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | unknown (U) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | unknown (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> How effectively can automated data extraction pipelines recover structured, machine-readable experimental results and methodological parameters from the 2.25 MB of unstructured text and embedded assets in the electronic supplementary material (43705_2022_180_MOESM1_ESM.docx) to facilitate independent reproducibility of the 2022 study?
>
> *Rationale:* The candidate question is about automated data extraction from an unstructured document for reproducibility, which is entirely unrelated to the matched gold question's focus on discovering viral diversity from RNA-seq data. Consequently, all match-based scores are zero, though data grounding is strong.

**Rank 2** · Comp = 0.080 · ❌ fail

> To what extent does the encapsulation of supplementary research data within the unstructured 2.25 MB 43705_2022_180_MOESM1_ESM.docx file hinder the Findability, Accessibility, Interoperability, and Reusability (FAIR) of the underlying scientific findings compared to machine-readable formats?
>
> *Rationale:* The candidate question is entirely unrelated to the gold questions, focusing on FAIR principles rather than virology. Consequently, it scores 0 on match strength, required elements coverage, and acceptability. However, it demonstrates strong data grounding by referencing a specific file.

**Rank 3** · Comp = 0.080 · ❌ fail

> What is the relative distribution of scientific information across different modalities (text, tables, embedded images) within the 2.25 MB supplementary document, and how does this distribution affect the automated retrieval of key experimental variables?
>
> *Rationale:* The candidate question is entirely unrelated to the scientific domain of the provided gold questions, focusing instead on document structure and information retrieval from a Word file. Consequently, it scores zero on match strength, required elements coverage, and acceptability, but scores well on data grounding due to specific file and feature references.

**Rank 4** · Comp = 0.060 · ❌ fail

> Can natural language processing models fine-tuned on scientific literature accurately identify and extract specific experimental conditions and methodological parameters from the unstructured text of the 43705_2022_180_MOESM1_ESM.docx supplementary file?
>
> *Rationale:* The candidate question is about NLP for extracting experimental conditions from a DOCX file, which is entirely unrelated to the virology and bioinformatics topics of the provided gold questions. It does, however, ground itself in a specific data file.

**Rank 5** · Comp = 0.060 · ❌ fail

> What hidden metadata, revision histories, or embedded annotations exist within the binary structure of the 43705_2022_180_MOESM1_ESM.docx file, and do they reveal undisclosed methodological changes or potential data leakage from the peer review process?
>
> *Rationale:* The candidate question is completely unrelated to the scientific domain of the provided gold questions, which focus on virology and RNA-seq. While it is a well-formed question in its own right, it does not align with the rubric's scope.

### ✅ `deepseek-v4-pro` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | unknown (U) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |

**Rank 1** · Comp = 0.100 · ❌ fail

> Does the structured tabular data contained within the 2.25 MB MOESM1 supplementary document for Springer Nature manuscript 43705 (article 180, 2022) allow an independent computational re-analysis that reproduces the study's primary reported effect sizes and their associated confidence intervals?
>
> *Rationale:* The candidate question focuses on reproducibility of effect sizes from a specific supplementary document, which is entirely unrelated to the provided gold questions about viral diversity and phylogeny in amphibians/reptiles. It exhibits excellent data grounding but no match to the given gold standards.

**Rank 2** · Comp = 0.060 · ❌ fail

> Can the multiple experimental conditions or sub-group analyses reported across distinct tables within the 2.25 MB MOESM1 file (manuscript 43705, 2022) be harmonised into a single meta-analytic framework to estimate a pooled effect and quantify within-study heterogeneity using I² and τ² statistics?
>
> *Rationale:* The candidate question is about meta-analysis of experimental conditions within a supplementary document, which is completely unrelated to the topic of viral diversity in amphibians and reptiles from RNA-seq data, as described in the gold questions.

**Rank 3** · Comp = 0.080 · ❌ fail

> Do the sample-size and event-count summaries distributed across the supplementary tables of MOESM1 (manuscript 43705, 2022) satisfy the data-consistency constraints implied by the study design, or do they reveal internal discrepancies such as non-monotonic count progressions, impossible subgroup totals, or digit-distribution anomalies?
>
> *Rationale:* The candidate question is about data integrity auditing of supplementary tables, which is completely unrelated to any of the provided gold questions concerning viral diversity or phylogeny. Therefore, it scores 0 on match strength, required elements, and acceptability, but scores well on data grounding due to specific file references.

**Rank 4** · Comp = 0.060 · ❌ fail

> What is the minimum detectable effect size at 80% statistical power for the primary endpoint, given the sample sizes recoverable from the MOESM1 supplementary tables of manuscript 43705 (2022), and does the study's central claim remain supported after adjusting for the multiplicity of endpoints and subgroup tests evident in the 2.25 MB document?
>
> *Rationale:* The candidate question is entirely out of scope for the provided gold questions. While it is well-grounded in a specific supplementary data file, it addresses statistical power and multiplicity correction in a clinical context rather than virological discovery or transcriptomics.

**Rank 5** · Comp = 0.060 · ❌ fail

> Using the file-naming metadata encoded in '43705_2022_180_MOESM1_ESM.docx', can the published main text of this 2022 Springer Nature article be retrieved from the public record and its key quantitative claims systematically compared against the corresponding values in the supplementary document to quantify the rate and direction of main-text-to-supplement reporting discrepancies?
>
> *Rationale:* The candidate question focuses on research integrity, metadata mining, and discrepancy auditing of a scientific article, which is entirely unrelated to the virology and phylogenetic analysis topics of the provided gold questions.

### ✅ `glm-5` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.060 · ❌ fail

> Does the supplementary material contain sufficient methodological detail and raw data to enable independent replication of the study's primary findings?
>
> *Rationale:* The candidate question is about research reproducibility and data transparency, specifically regarding a supplementary document. This topic is entirely unrelated to the virology and RNA-seq mining focus of the provided gold questions.

**Rank 2** · Comp = 0.060 · ❌ fail

> What types of supplementary data (tables, figures, datasets, protocols) are included in the electronic supplementary material?
>
> *Rationale:* The candidate question is about the content of a supplementary document, which is entirely unrelated to the scientific intent of either gold question concerning viral diversity or phylogeny in amphibians/reptiles.

**Rank 3** · Comp = 0.080 · ❌ fail

> Is the supplementary material file size (2.2 MB) consistent with comprehensive data sharing practices in the 2022 publication?
>
> *Rationale:* The candidate question about file size and data sharing is unrelated to the gold questions about viral diversity. It scores 0 for match strength, required elements, and acceptability, but high for data grounding due to specific file reference.

**Rank 4** · Comp = 0.060 · ❌ fail

> Does the naming convention of the supplementary material file follow standard journal guidelines for electronic supplementary materials?
>
> *Rationale:* The candidate question is about file naming conventions, which is completely unrelated to the scientific questions about viral discovery or phylogeny in the gold set. It grounds in a specific filename but fails on all other scientific dimensions.

**Rank 5** · Comp = 0.060 · ❌ fail

> What research domain or field is indicated by the article identifier and supplementary material designation?
>
> *Rationale:* The candidate question focuses on identifying the research domain of an article based on its identifier and supplementary material, which is entirely unrelated to the scientific inquiry of finding hidden viral diversity in amphibian/reptile RNA-seq data.

### ✅ `gemini-2.5-flash` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (U) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What are the key experimental findings or datasets presented in the supplementary material that support the main conclusions of the associated publication?
>
> *Rationale:* The candidate question is a generic request to parse a file rather than a scientific hypothesis-driven question. It lacks any semantic alignment with the research topics of viral discovery in amphibian/reptile transcriptomes defined in the gold set.

**Rank 2** · Comp = 0.060 · ❌ fail

> What specific methodologies or protocols are detailed within the supplementary document that were not fully elaborated in the main research article?
>
> *Rationale:* The candidate question is a generic document analysis task, unrelated to the scientific questions about viral diversity or phylogeny in amphibians/reptiles posed by the gold questions. It does, however, ground itself in a specific data file.

**Rank 3** · Comp = 0.080 · ❌ fail

> Does the supplementary material include any extended data figures or tables that provide additional context or less critical results related to the primary research?
>
> *Rationale:* The candidate question is about finding figures/tables in supplementary material, which is unrelated to the gold questions' scientific focus on viral diversity in amphibians/reptiles. It scores 0 for match strength, required elements, and acceptability due to this complete thematic mismatch, but scores well for data grounding by referencing a specific file and content types.

**Rank 4** · Comp = 0.060 · ❌ fail

> Are there any specific software tools, scripts, or computational models described or provided in the supplementary material that were used for data analysis or simulation?
>
> *Rationale:* The candidate question is a methodological inquiry about software tools, completely unrelated to the scientific discovery of viral diversity in amphibians and reptiles, leading to zero scores for match strength, required elements, and acceptability. It does, however, ground itself to a specific supplementary document.

**Rank 5** · Comp = 0.060 · ❌ fail

> What is the overall scope and focus of the supplementary information, and how does it complement the main research article it is associated with?
>
> *Rationale:* The candidate question is a meta-question about document structure and purpose, not a scientific inquiry into biological phenomena. It is completely unrelated to the specific virology and RNA-seq research questions in the gold standards.

### ✅ `intern-s1` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 1 | 0.100 | 0.020 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.060 · ❌ fail

> What is the relationship between temperature variation and plant growth rates in the dataset?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, which focus on viral diversity in amphibians/reptiles. It does, however, ground its query in specific data features it expects to find in the provided document.

**Rank 2** · Comp = 0.080 · ❌ fail

> How does soil pH correlate with plant health indicators in the study?
>
> *Rationale:* The candidate question is completely unrelated to the provided gold questions, focusing on plant health and soil pH rather than viral diversity in amphibians/reptiles. It scores well on data grounding by referencing specific features and a file.

**Rank 3** · Comp = 0.060 · ❌ fail

> Does fertilizer application show a significant effect on crop yield in the dataset?
>
> *Rationale:* The candidate question is about agricultural science, specifically fertilizer effects on crop yield, which is completely outside the scope of the provided gold questions focused on viral diversity in amphibians and reptiles.

**Rank 4** · Comp = 0.020 · ❌ fail

> What seasonal patterns are observed in plant development metrics?
>
> *Rationale:* The candidate question is about plant development and seasonality, which is entirely unrelated to the virology-focused gold questions provided. Consequently, it scores very low across all dimensions related to matching the gold questions.

**Rank 5** · Comp = 0.000 · ❌ fail

> How do different light exposure durations affect photosynthesis efficiency?
>
> *Rationale:* The candidate question is about plant physiology, specifically light exposure and photosynthesis, which is completely unrelated to the gold question's focus on viral diversity in amphibians and reptiles using RNA-seq data.

### ✅ `intern-s1-pro` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 2 | 0 | 0 | 1 | 1 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 2 | 0.200 | 0.040 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What experimental parameters and statistical methods were used to generate the primary results, and can they be replicated using the detailed protocols provided in the supplementary material?
>
> *Rationale:* The candidate question is a generic query about experimental parameters, statistical methods, and reproducibility from supplementary material, which is entirely unrelated to the specific scientific goals of discovering viral diversity or analyzing viral phylogeny in amphibians and reptiles as defined by the gold questions.

**Rank 2** · Comp = 0.060 · ❌ fail

> What are the key quantitative findings and statistical significance levels reported in the supplementary data tables, and how do they support the main conclusions of the study?
>
> *Rationale:* The candidate question is a generic meta-inquiry about statistical significance in a supplementary file. It lacks any scientific connection to the provided gold questions concerning virome discovery in ectotherm hosts, failing to address the specific biological domain or required technical elements.

**Rank 3** · Comp = 0.000 · ❌ fail

> What experimental variables, controls, and measurement techniques were employed in the study, and how were potential confounding factors addressed in the methodology?
>
> *Rationale:* The candidate question is a generic meta-inquiry about experimental design that lacks any scientific connection to the specific domain of viral discovery in transcriptomic data required by the gold questions.

**Rank 4** · Comp = 0.040 · ❌ fail

> How do the supplementary findings compare with previously published results in the field, and what novel contributions do they make to existing scientific knowledge?
>
> *Rationale:* The candidate question is a generic meta-question about scientific novelty and comparison to existing literature, which is entirely unrelated to the specific biological and methodological focus of the gold questions concerning viral diversity in amphibians/reptiles from RNA-seq data.

**Rank 5** · Comp = 0.060 · ❌ fail

> What additional hypotheses or research questions are suggested by the supplementary data and analyses that were not addressed in the main study?
>
> *Rationale:* The candidate question is a generic query about hypothesis generation from supplementary data, bearing no specific scientific resemblance to the gold questions about viral diversity in amphibians/reptiles. It lacks any specific biological or methodological elements of the gold questions.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 5 | 0 | 0 | 0 | 2 | 0.200 | 0.040 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.060 · ❌ fail

> What specific experimental methods, raw data tables, or supplementary figures are contained in the MOESM1 supplementary document associated with article 43705 (2022), and how do these materials enable validation or extension of the primary study's findings?
>
> *Rationale:* The candidate question is about extracting and analyzing the contents of a supplementary document to validate a primary study. This intent is unrelated to the provided gold questions, which focus on discovering and characterizing viral diversity in amphibians and reptiles using RNA-seq data.

**Rank 2** · Comp = 0.100 · ❌ fail

> Does the 2.25 MB supplementary document contain quantitative data tables that could be extracted and re-analyzed to verify statistical claims in the associated 2022 publication?
>
> *Rationale:* The candidate question focuses on extracting and re-analyzing quantitative data from a supplementary document to verify statistical claims, which is entirely unrelated to the biological and virological scope of the provided gold questions.

**Rank 3** · Comp = 0.080 · ❌ fail

> What is the structural composition of the MOESM1 supplementary document—does it contain primarily textual methods descriptions, embedded figures, or tabular data, and how does this composition reflect standard practices for supplementary materials in the relevant scientific field?
>
> *Rationale:* The candidate question is about document structure, not scientific content related to viral diversity or phylogeny. It is completely unrelated to the gold questions, hence low scores for match strength, coverage, and acceptability, despite good data grounding.

**Rank 4** · Comp = 0.060 · ❌ fail

> Can the supplementary document be linked to its primary publication (article ID 43705, 2022) to identify the research domain and specific study questions that the supplementary materials were designed to address?
>
> *Rationale:* The candidate question focuses on bibliometric linkage of a supplementary document to its primary publication for contextual understanding, which is completely unrelated to the scientific domain of discovering viral diversity from RNA-seq data in amphibians and reptiles.

**Rank 5** · Comp = 0.040 · ❌ fail

> What are the potential challenges and limitations in extracting and analyzing content from this binary .docx supplementary document, and how might these limitations affect the reliability of any scientific conclusions drawn from it?
>
> *Rationale:* The candidate question is off-topic. It addresses the technical challenge of parsing a supplementary .docx file rather than the biological research question of mining public RNA-seq data for novel viruses in ectothermic vertebrates.


## 2 · `arthropod_neg_sense_2015`

- **raw**：2 文件: `elife-05378-supp-v1.zip, nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.740 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 1 | 5 | 1.400 | 0.280 | ❌ | GQ_001 (U) |
| 5 | 2 | 2 | 2 | 5 | 1.955 | 0.391 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.740 · ✅ pass

> Does the RNA-dependent RNA polymerase phylogeny of the 170 arthropod-derived negative-sense RNA virus sequences in nuccore_reported_viral_sequences.fasta (KM817593–KM817764) recover host-arthropod-order-specific clades (Acari, Diptera, Araneae, Hemiptera, Decapoda, Blattodea), and is the inferred host-association signal congruent with the independent N- and G-gene phylogenies built from the same strain panel?
>
> *Rationale:* The candidate question is a highly specific and well-grounded inquiry into host-association and multi-gene phylogenetic congruence of arthropod negative-sense RNA viruses. While it touches on ancestry and lineages, its specific framing differs from `GQ_001`'s broader intent regarding genome architecture.

**Rank 2** · Comp = 0.493 · ❌ fail

> Among the 170 KM817593–KM817764 arthropod-virus sequences, does each segmented orthomyxo-like genome (the multi-`segment N` entries with PB1, glycoprotein and nucleoprotein modules) preserve a stable cassette gene order, and can reassortment be detected by topological incongruence between the PB1 tree and the segment-1/segment-2 trees of the same strains?
>
> *Rationale:* The candidate shifts focus from broad macro-evolutionary phylogenetic gaps (GQ_002) to mechanistic reassortment detection in specific orthomyxo-like segments. It is highly grounded in the provided file metadata but moves beyond the core intent of bridging global viral lineages toward focused strain-level topological incongruence analysis.

**Rank 3** · Comp = 0.580 · ❌ fail

> Within the negative-sense RNA virus catalogue spanning seven `complete genome` entries (898–15,462 nt), is genome length and ORF count systematically associated with arthropod host class — i.e. are mononegavirus-like genomes longer in chelicerate hosts (ticks, spiders) than in dipteran hosts (mosquitoes, flies)?
>
> *Rationale:* The candidate partially matches GQ_001 by focusing on genome architecture in negative-sense RNA viruses, but it lacks the emphasis on basal lineages and RNA-seq. Data grounding is excellent, citing specific files and entries. Acceptability is moderate as it's a good question but doesn't align with the gold's specific acceptable variants.

**Rank 4** · Comp = 0.280 · ❌ fail

> Does GC content and codon-usage bias of the L (RdRp) coding sequences within nuccore_reported_viral_sequences.fasta cluster by arthropod host order rather than by viral family, indicating compositional adaptation to host translational machinery in invertebrate-infecting negative-sense RNA viruses?
>
> *Rationale:* The candidate proposes a sophisticated analysis of codon usage bias and compositional adaptation to host machinery in negative-sense RNA viruses. While scientifically rigorous and well-grounded in the provided FASTA data, it asks a fundamentally different evolutionary question than the gold items, which target phylogenetic ancestry, lineage discovery, and genome architecture/segmentation.

**Rank 5** · Comp = 0.391 · ❌ fail

> Among the tick-derived virus subset (38 sequences spanning Bole, Changping, Tacheng, Huangpi, Dabieshan, Lihan, Wenzhou, Yongjia, Wuhan, and Taishun tick viruses), how many phylogenetically distinct negative-sense RNA virus lineages are co-circulating in Chinese tick populations, and do any cluster with known human-pathogenic phenuiviruses (e.g. SFTSV, Heartland, Bhanja) at the L or N gene?
>
> *Rationale:* The candidate question is a highly granular epidemiological and surveillance query regarding specific tick-borne viruses. It lacks the focus on evolutionary genome architecture transitions (segmentation) defined in the gold set, though it uses the correct data sources.

### ✅ `gpt-5.5-high` — Comp=0.578 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 1 | 4 | 1.300 | 0.260 | ❌ | GQ_001 (P) |
| 3 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 5 | 2 | 2 | 1 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.493 · ❌ fail

> To what extent do invertebrate host groups structure the evolutionary diversity of newly reported negative-sense RNA viruses across the orthomyxovirus-, bunyavirus-, mononegavirus-, and chuvirus-related clades represented in the FASTA sequences and Figure 3 supplement phylogenies?
>
> *Rationale:* The candidate explores the relationship between invertebrate hosts and viral evolution across major clades. While it effectively utilizes the data to propose a robust evolutionary analysis, it focuses on host-structured diversity rather than the specific mechanistic question of genome segmentation and phylogenetic gaps between segmented and non-segmented groups defined in GQ_002.

**Rank 2** · Comp = 0.260 · ❌ fail

> Which invertebrate host categories contribute the greatest breadth of reported negative-sense RNA virus diversity and genome completeness in the provided sequences?
>
> *Rationale:* The candidate shifts the research question from evolutionary phylogenetic analysis to descriptive host-diversity and genome completeness statistics. While it utilizes the provided data files effectively, it ignores the core objective of understanding the ancestry and evolutionary architecture of arthropod-associated negative-sense RNA viruses.

**Rank 3** · Comp = 0.578 · ❌ fail

> Do polymerase-bearing sequences in the FASTA recover the same major virus-family relationships shown in the orthomyxovirus, bunyavirus, mononegavirus, and chuvirus Figure 3 supplement trees?
>
> *Rationale:* The candidate tests if polymerase sequences from the FASTA can reproduce known phylogenetic relationships of specific negative-sense RNA virus families shown in provided figures. It aligns with GQ_002's focus on phylogenetic connections between these groups, though it emphasizes concordance rather than bridging gaps or new assembly. It is strongly data-grounded.

**Rank 4** · Comp = 0.476 · ❌ fail

> Are segmented genome architectures concentrated in particular invertebrate hosts or phylogenetic groups among the reported viral sequences?
>
> *Rationale:* The candidate investigates the distribution of genome segmentation in arthropod viruses. While it successfully grounds its analysis in provided sequence data and host information, it misses the core evolutionary focus of the gold questions regarding phylogenetic bridging and the negative-sense viral classification.

**Rank 5** · Comp = 0.400 · ❌ fail

> How often are glycoprotein and nucleocapsid genes recovered together with polymerase genes in the reported invertebrate viruses, and does that co-recovery vary by host category?
>
> *Rationale:* The candidate question focuses on gene recovery completeness and host-related biases, which is distinct from the gold's evolutionary and deep phylogenetic intent. It implicitly touches on genome content but misses core elements like ancestry and specific data types.

### ✅ `claude-code-sonnet-4-6` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.80

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 5 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 4 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.860 · ✅ pass

> Do the RNA-dependent RNA polymerase (L gene) phylogenies of the 82 arthropod-infecting negative-sense RNA viruses from Chinese arthropod surveillance (KM817593–KM817764) reveal that tick-borne phlebo/bunya-like viruses (Bole, Changping, Tacheng, Huangpi, and Yongjia Tick Viruses) form a monophyletic clade evolutionarily derived from non-hematophagous arthropod lineages (spider, cockroach, and water-strider viruses), implying that acquisition of hematophagy is the primary driver of tick-borne RNA virus emergence?
>
> *Rationale:* The candidate question is a highly specific, hypothesis-driven inquiry into the phylogenetic ancestry and evolutionary drivers (hematophagy) of specific negative-sense RNA viruses in arthropods, aligning well with the core intent of GQ_001 despite its narrower scope and omission of genome architecture.

**Rank 2** · Comp = 0.940 · ✅ pass

> Do the 14 PB1-containing orthomyxo-like arthropod viruses (Jingshan Fly Virus 1, Jiujie Fly Virus, Sanxia Water Strider Virus 3, Shayang Spider Virus 3, Wuhan Louse Fly Viruses 3 and 4, Wuhan Mosquito Viruses 3–7, and Wuchang Cockroach Virus 2) from Chinese invertebrates constitute a monophyletic sister clade to the vertebrate-infecting influenza-like orthomyxoviruses, indicating that the influenza virus lineage originated in arthropod hosts before expanding to vertebrates?
>
> *Rationale:* The candidate question precisely investigates the arthropod origin and ancestry of a specific negative-sense RNA virus lineage (Orthomyxoviridae), aligning perfectly with the gold question's focus on basal lineages and ancestry. It is highly specific, well-grounded in data, and avoids vague phrasing.

**Rank 3** · Comp = 0.360 · ❌ fail

> Do viruses from aquatic or semi-aquatic arthropods (Wenzhou Crab Viruses 1–3, Whenzhou Shrimp Viruses 1–2, Sanxia Water Strider Viruses 1–5) share more recent common ancestors with each other than with terrestrial arthropod viruses in L-gene phylogenies derived from the sequences in nuccore_reported_viral_sequences.fasta, suggesting that aquatic habitat is a stronger predictor of RNA virus clade membership than host taxonomic order?
>
> *Rationale:* The candidate investigates ecological vs. taxonomic drivers of RNA virus clade membership using L-gene phylogenies from specific arthropod viruses. It weakly aligns with GQ_001's broad theme of phylogenetic ancestry but diverges in its specific focus and lacks elements like basal lineages or genome architecture.

**Rank 4** · Comp = 0.860 · ✅ pass

> Do the multi-gene genomic architectures of the 15 fully characterized phlebo/bunyavirus-like arthropod viruses in nuccore_reported_viral_sequences.fasta (possessing complete N, G, and L coding sequences) show evidence of inter-species reassortment between tick-borne and mosquito-borne lineages, as inferred by incongruent topologies between N-gene and L-gene phylogenies?
>
> *Rationale:* The candidate question is a highly specific and well-grounded inquiry into the genome architecture and ancestry of arthropod-borne negative-sense RNA viruses, focusing on reassortment. It aligns well with the matched gold's intent, covering most required elements with excellent data grounding, despite its specific framing.

**Rank 5** · Comp = 0.760 · ✅ pass

> Is genome size (measured as total coding sequence length per virus) in the arthropod RNA virus collection from KM817593–KM817764 positively correlated with host taxonomic diversity (number of distinct arthropod orders sampled per virus clade in the L-gene phylogeny), consistent with a model in which broader host-range RNA viruses evolve larger, more complex genomes to accommodate diverse cellular environments?
>
> *Rationale:* The candidate question aligns well with GQ_001 by focusing on genome architecture and its evolutionary implications in arthropod RNA viruses, specifically linking genome size/complexity to host diversity. It is highly specific and well-grounded in data, though it omits the "negative-sense" aspect and "basal lineages" from the gold question's requirements.

### ✅ `gemini-3.1-pro` — Comp=0.527 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 3 | 1.190 | 0.238 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.476 · ❌ fail

> How do the evolutionary relationships of the newly discovered arthropod viruses (e.g., Bole Tick Virus, Lishi Spider Virus) reshape our understanding of viral phylogeny and host-virus co-evolution?
>
> *Rationale:* The question aligns with using new arthropod viruses for viral phylogeny but lacks specificity on negative-sense RNA viruses and segmentation. It grounds well in data features but misses core elements of the gold question's specific scientific inquiry.

**Rank 2** · Comp = 0.527 · ❌ fail

> What are the unique genomic architectures and gene arrangements of the novel segmented and unsegmented arthropod viruses identified in this dataset?
>
> *Rationale:* The candidate question describes the genomic architecture of novel segmented and unsegmented arthropod viruses, which is a foundational step for GQ_002's phylogenetic inquiry. It grounds well in data but omits the phylogenetic and negative-sense RNA virus aspects.

**Rank 3** · Comp = 0.476 · ❌ fail

> Are there conserved functional domains within the putative polymerase and glycoprotein sequences of these diverse invertebrate viruses?
>
> *Rationale:* The candidate question focuses on conserved functional domains in viral proteins, which is a method to infer phylogenetic relationships. It partially aligns with GQ_002's intent of understanding phylogenetic connections and uses specific protein types (polymerase). However, it misses the explicit framing of 'phylogenetic gaps' and 'segmentation transitions' central to GQ_002.

**Rank 4** · Comp = 0.200 · ❌ fail

> What is the extent of viral diversity and abundance within the sampled arthropod populations as indicated by the supplementary data?
>
> *Rationale:* The candidate question is a general inquiry into viral diversity and abundance in arthropods, lacking the specific evolutionary and genomic focus of the matched gold question. It fails to cover any of the gold's required elements and is closer to an unacceptable, generic question.

**Rank 5** · Comp = 0.238 · ❌ fail

> Do the codon usage patterns of these novel arthropod viruses reflect adaptation to their specific tick, spider, or fly hosts?
>
> *Rationale:* The candidate question addresses host adaptation via codon usage in novel arthropod viruses, which is a different scientific intent from the matched gold question's focus on phylogenetic gaps and genome segmentation. It covers few required elements and is not close to any acceptable or unacceptable variants.

### ❌ `deepseek-v4-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `glm-5` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ✅ `gemini-2.5-flash` — Comp=0.320 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 3 | 4 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 2 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 3 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 0 | 3 | 0.595 | 0.119 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 1 | 3 | 1.200 | 0.240 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.280 · ❌ fail

> How do the codon usage patterns in the Bole Tick Virus 3 genome compare to those of other identified viral sequences in the dataset, and what does this suggest about its host adaptation?
>
> *Rationale:* The candidate question about codon usage and host adaptation of Bole Tick Virus 3 is not aligned with the gold's focus on negative-sense RNA virus evolution, basal lineages, or genome architecture. It lacks coverage of key required elements, despite being a well-grounded question.

**Rank 2** · Comp = 0.240 · ❌ fail

> What are the phylogenetic relationships among the viral sequences in the dataset, and do these relationships correlate with known host specificities or geographical origins?
>
> *Rationale:* The candidate asks a generic phylogenetic question about viral sequences in a dataset. It lacks the specific evolutionary context regarding arthropod hosts, negative-sense RNA virus classification, and genome structure required to match the intent of the gold questions.

**Rank 3** · Comp = 0.320 · ❌ fail

> Are there highly conserved genomic regions or specific sequence motifs present across different viral families or strains within the dataset, suggesting common functional elements?
>
> *Rationale:* The candidate question focuses on general viral sequence conservation and functional elements, which is semantically distinct from the matched gold's intent regarding negative-sense RNA virus ancestry and genome architecture from arthropod RNA-seq. It only vaguely touches upon genome structure.

**Rank 4** · Comp = 0.119 · ❌ fail

> What is the range of genome sizes and nucleotide compositions (e.g., GC content) among the viral sequences, and do these variations correlate with viral classification or replication strategies?
>
> *Rationale:* The candidate question is a general descriptive query about viral genome properties (size, composition) and their correlation with classification, which is fundamentally different from the specific evolutionary and phylogenetic hypothesis of GQ_002. It closely resembles an unacceptable variant of GQ_002.

**Rank 5** · Comp = 0.240 · ❌ fail

> Can specific genes or regulatory elements, known to be associated with virulence or host interaction, be identified and characterized across the diverse viral sequences in the dataset?
>
> *Rationale:* The candidate question focuses on functional gene annotation (virulence factors) rather than the evolutionary and phylogenetic investigation of arthropod-associated negative-sense RNA viruses required by the gold standards.

### ✅ `intern-s1` — Comp=0.340 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 0 | 3 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.340 · ❌ fail

> How does genetic diversity of Bole Tick Virus 3 correlate with geographic sampling locations?
>
> *Rationale:* The candidate question focuses on the phylogeography and genetic diversity of a specific virus, which differs significantly from GQ_001's intent to explore the broad ancestry and genome architecture of negative-sense RNA viruses using arthropod RNA-seq data.

**Rank 2** · Comp = 0.100 · ❌ fail

> What temporal trends exist in viral sequence submissions to GenBank for this dataset?
>
> *Rationale:* The candidate question is about temporal trends in GenBank submissions, which is completely unrelated to the gold question's focus on viral evolution, ancestry, and genome architecture from arthropod RNA-seq data. It covers none of the gold's required elements but has excellent data grounding.

**Rank 3** · Comp = 0.140 · ❌ fail

> Are there conserved genomic regions across different strains that could serve as diagnostic targets?
>
> *Rationale:* The candidate question is about finding conserved genomic regions for diagnostic targets, which is unrelated to the evolutionary and phylogenetic focus of the gold questions. It lacks any specific elements of the gold questions but does ground itself in a specific FASTA file.

**Rank 4** · Comp = 0.240 · ❌ fail

> How do sequence variations in the viral genome correlate with host species metadata?
>
> *Rationale:* The candidate question focuses on general viral sequence variation and host correlation, which is distinct from the gold's specific intent regarding negative-sense RNA virus ancestry and genome architecture in arthropods. It lacks the required elements and specificity.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the relationship between viral genome length and pathogenicity indicators in the metadata?
>
> *Rationale:* The candidate question is entirely unrelated to the evolutionary and architectural focus of GQ_001, leading to low scores across most dimensions. It does, however, demonstrate strong data grounding by referencing specific files and features.

### ✅ `intern-s1-pro` — Comp=0.400 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 3 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 3 | 3 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (U) |
| 4 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (U) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.200 · ❌ fail

> What is the GC content distribution across the reported viral genomes, and does it differ significantly between viruses infecting ticks, spiders, and flies?
>
> *Rationale:* The candidate question about GC content and host differences is unrelated to the gold's focus on viral evolution and genome architecture. It lacks all required elements of the gold question but is well-grounded in data.

**Rank 2** · Comp = 0.400 · ❌ fail

> What is the pairwise nucleotide sequence identity among the viral genomes, and can a phylogenetic tree be constructed to infer evolutionary relationships?
>
> *Rationale:* The candidate question is a generic inquiry about viral phylogeny, broadly touching on evolutionary relationships. It misses the specific context of arthropod RNA-seq, negative-sense RNA viruses, basal lineages, and genome architecture central to the matched gold question. It grounds in the provided FASTA file but lacks specificity.

**Rank 3** · Comp = 0.180 · ❌ fail

> Are there conserved non-coding regulatory motifs (e.g., promoter-like sequences) present in the intergenic regions of these viral genomes?
>
> *Rationale:* The candidate question focuses on the technical identification of regulatory motifs within viral genomes. It is unrelated to the evolutionary or phylogenetic goals defined in the gold set, which center on arthropod host associations and the ancestry of negative-sense RNA virus architectures.

**Rank 4** · Comp = 0.180 · ❌ fail

> What is the length variation of the viral genomes, and is there a correlation between genome length and host type?
>
> *Rationale:* The candidate question focuses on viral genome length and host correlations, which is a descriptive statistical query. It lacks the evolutionary, lineage-based, or phylogenetic framing required by the gold questions regarding the ancestry and architecture of negative-sense RNA viruses.

**Rank 5** · Comp = 0.220 · ❌ fail

> Can recombination events be detected among the viral sequences using nucleotide alignment and recombination detection methods?
>
> *Rationale:* The candidate question about detecting recombination in viral sequences is broadly related to viral evolution but completely misses the specific focus of GQ_001 on arthropod negative-sense RNA virus ancestry and genome architecture. It lacks all specific required elements.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ❌ `intern-s2-preview` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`


## 3 · `bat_btcn_virome_2024`

- **raw**：4 文件: `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz, 43059586_RdRp_motif_collection.xlsx, 45561465_Meta_data_for_ecological_modeling.zip, 48306316_ML_Phylo.zip`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 4 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 5 | 0 | 2 | 1 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Which environmental, land-use and host-diet covariates best predict the per-pool RNA-virus richness (tv) and the cross-order composition of bat viromes across the five Chinese bat families and five sampled tissues represented in the BtCN-Virome dataset?
>
> *Rationale:* The candidate question perfectly matches the gold's intent to identify covariates explaining bat RNA-virus richness and composition. It covers all required elements, is highly acceptable, and demonstrates strong data grounding by referencing specific files and features for all components.

**Rank 2** · Comp = 0.646 · ✅ pass

> Does intestinal-tissue sampling recover systematically higher and compositionally distinct RNA-virus diversity than lung-tissue sampling within the same bat individuals/pools, and which viral orders drive this tissue tropism?
>
> *Rationale:* The candidate question investigates tissue type as a covariate explaining RNA-virus diversity and composition, aligning with GQ_002's focus on covariates. It covers host traits, virus diversity, and statistical modeling, with strong data grounding using specific files and numerical details.

**Rank 3** · Comp = 0.400 · ❌ fail

> How does the phylogenetic placement of BtCN-Virome contigs within each of the 14 order-level RdRp trees reveal previously uncharacterised viral clades that fall outside known reference diversity, particularly within the small Coronaviridae reference set?
>
> *Rationale:* The candidate question focuses on phylogenetic placement to discover novel viral clades, particularly within Coronaviridae, using specific data files. It poorly matches GQ_001, which is about ecological drivers and human circulation of bat RNA-virus diversity, missing most of its core elements.

**Rank 4** · Comp = 0.799 · ✅ pass

> To what extent does the ingested arthropod, mollusc, and plant DNA recoverable from BtCN-Virome reads (matched against Arthropoda, Mollusca and Streptophyta barcode references) explain bat-virome composition beyond what is predicted by host bat species identity alone?
>
> *Rationale:* The candidate question precisely identifies dietary and host covariates to explain bat-virome composition, directly matching GQ_002. It is highly specific, well-grounded in data features, and proposes a clear analytical approach, though it omits geographic covariates.

**Rank 5** · Comp = 0.240 · ❌ fail

> Are the conserved RdRp motifs catalogued in 43059586_RdRp_motif_collection.xlsx sufficient to classify BtCN-Virome contigs to the correct viral order, and which order-level motif signatures provide the highest classification accuracy compared to phylogeny-based assignment?
>
> *Rationale:* The candidate question focuses on benchmarking viral classification methods using RdRp motifs against phylogenetic assignments, which is fundamentally different from the ecological drivers and human circulation intent of the matched gold question. It does, however, reference specific data files for its proposed analysis.

### ❌ `gpt-5.5-high` — 失败 `FileNotFoundError: gpt-5.5-high did not write /private/tmp/codex-sandboxes/gpt-5.5-high/20260531T171859/agent_questions.`

### ✅ `claude-code-sonnet-4-6` — Comp=0.850 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 5 | 3 | 5 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 3 | 5 | 3 | 5 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 5 | 3 | 4 | 4 | 5 | 3.145 | 0.629 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Do site-level elevation (H10) and shrubland cover (sl) independently predict RNA-virus Shannon diversity in bat intestinal viromes across Chinese Rhinolophidae and Vespertilionidae populations, and does the direction of these landscape effects differ between intestinal and pulmonary tissue compartments?

**Rank 2** · Comp = 0.748 · ✅ pass

> Do Rhinolophidae bat pools consistently harbour higher RNA-virus Shannon diversity than Vespertilionidae, Pteropodidae, and Hipposideridae pools across all five sampled tissue types (intestine, lung, kidney, liver, brain), and is the Rhinolophidae excess driven by phylogenetically broader viral lineage representation as evidenced by the ML RdRp phylogenies?
>
> *Rationale:* The candidate question precisely asks about specific host factors (bat family, tissue type) influencing RNA-virus diversity and composition, aligning well with GQ_002. It is highly data-grounded and well-structured, though it doesn't cover all covariate types listed in the gold's broad scope.

**Rank 3** · Comp = 0.748 · ✅ pass

> Can a machine-learning model trained on the nine climatic variables (srs10, H10, hurs10, pet10, pr10, rsds10, sfcwind10, tas10, vpd10) and nine land-use variables from the BtCN-Virome ecological metadata predict bat intestinal RNA-virus Shannon diversity with cross-validated R² > 0.5 at the sampling-pool level?
>
> *Rationale:* The candidate question is an excellent, highly specific instance of GQ_002, detailing the covariates (climatic, land-use), the outcome (Shannon diversity), and the method (ML model). It is well-grounded in data features, though it doesn't explicitly include host traits or geography as covariates.

**Rank 4** · Comp = 0.646 · ✅ pass

> Among the 8,176 BtCN-Virome full-spectrum contigs, what proportion carry intact conserved RdRp motifs C (GDD) and B (SGxxxTxxxN) as defined in the RdRp motif collection, and do contigs from Rhinolophidae bat pools show a higher frequency of multi-family RdRp motif variants compared to contigs from Vespertilionidae pools?
>
> *Rationale:* The question investigates RdRp motif frequency in viral contigs, comparing it between bat families, directly addressing how host traits relate to viral composition. It is well-grounded in specific data features and files, though it doesn't cover all ecological covariates.

**Rank 5** · Comp = 0.629 · ✅ pass

> Do bat viromes sampled from kidney and liver pools show lower RNA-virus Shannon diversity than intestinal pools when controlling for bat family and geographic site, consistent with tissue-tropism constraints predicted by the gut-associated virome reservoir hypothesis?
>
> *Rationale:* The candidate shifts the focus from broad ecological covariates to specific tissue-based tropism as a driver of virome diversity. It is well-grounded in the provided metadata files and uses appropriate statistical phrasing for a secondary-level ecological modeling question, though it narrows the scope compared to the broader gold requirement.

### ✅ `gemini-3.1-pro` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 4 | 4.165 | 0.833 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 4 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 5 | 3 | 4 | 4 | 4 | 3.060 | 0.612 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.833 · ✅ pass

> How do host genetic divergence, inferred from CytB, COI, and ITS barcoding markers, and environmental variables interact to shape the phylogenetic diversity and geographic distribution of RNA viruses within the Chinese bat virome?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, comprehensively covering all required elements by asking how host genetics, environmental variables, and geographic distribution explain RNA virus phylogenetic diversity. It is highly specific and well-grounded in available data features.

**Rank 2** · Comp = 0.850 · ✅ pass

> Can ecological niche modeling, integrating host occurrence data from DNA barcoding and viral detection from virome contigs, accurately predict geographic hotspots for the presence of specific RNA viral clades?
>
> *Rationale:* The candidate question is an excellent, highly specific formulation of GQ_002, focusing on ecological niche modeling to predict viral geographic hotspots. It fully covers all required elements and is strongly grounded in the available data, demonstrating a clear and actionable scientific inquiry.

**Rank 3** · Comp = 0.850 · ✅ pass

> Is the phylogenetic structure of the bat RNA virome more strongly constrained by host species boundaries or by geographic and climatic barriers?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, precisely identifying drivers of bat RNA virome structure using specific covariates. It covers all required elements, is highly acceptable, and is well-grounded in the provided data features.

**Rank 4** · Comp = 0.527 · ❌ fail

> Do specific amino acid variations within the highly conserved RdRp motifs correlate with distinct host species or ecological niches, indicating adaptive evolution of the viral replication machinery?
>
> *Rationale:* The candidate question links host/ecological factors to viral features, aligning with GQ_002's intent to explain viral characteristics. However, it focuses on molecular variations rather than overall richness/composition, leading to partial coverage of required elements and a mid-range match.

**Rank 5** · Comp = 0.612 · ✅ pass

> What is the frequency and ecological context of cross-species viral transmission events among sympatric bat populations, as evidenced by incongruences between viral and host phylogenies?
>
> *Rationale:* The candidate question aligns with the gold's intent to explain viral patterns using ecological factors, but focuses on cross-species transmission via phylogenies rather than richness/composition. It grounds well in data and is a well-formed scientific question, though it doesn't perfectly match an acceptable variant.

### ✅ `deepseek-v4-pro` — Comp=0.833 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 4 | 4.165 | 0.833 | ✅ | GQ_002 (S) |
| 2 | 1 | 2 | 2 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 3 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 4 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 5 | 1 | 1 | 3 | 5 | 1.800 | 0.360 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.833 · ✅ pass

> How does bat host community phylogenetic composition — resolved via CytB, COI, and ITS barcodes — shape the richness and novelty of coronaviruses detected in full-spectrum virome contigs across different ecological contexts?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, directly asking how specific host and environmental covariates (phylogenetic composition, ecological contexts) explain viral diversity (coronavirus richness/novelty). It explicitly grounds in multiple data features and covers all required elements with high specificity, aligning well with acceptable variants.

**Rank 2** · Comp = 0.360 · ❌ fail

> Do RdRp motif-based detection methods recover a significantly broader diversity of bat coronaviruses than contig-assembly-based approaches when applied to the same full-spectrum virome data?
>
> *Rationale:* The candidate question is methodological, comparing virus detection techniques, which fundamentally differs from the ecological/epidemiological intent of the gold question. While it mentions bat viruses and virome data, its core focus is on method benchmarking, not ecological drivers or circulation near human settlements.

**Rank 3** · Comp = 0.799 · ✅ pass

> Are bat coronavirus prevalence and diversity significantly higher in sampling sites characterised by anthropogenic disturbance, as inferred from the ecological metadata, after controlling for host species richness from barcode data?
>
> *Rationale:* The candidate question is an excellent match for GQ_002, directly addressing how specific host and environmental covariates explain viral diversity. It is well-grounded in data and highly acceptable, though it omits 'geography' as a distinct covariate.

**Rank 4** · Comp = 0.697 · ✅ pass

> Can machine-learning models trained on host phylogenetic features and ecological covariates, as provided in the ML/Phylo archive, predict which bat species are most likely to harbour novel coronaviruses not yet detected in the virome contigs?
>
> *Rationale:* The candidate question aligns well with predicting viral presence/composition using host and ecological covariates via machine learning, a specific application of GQ_002. It grounds well in multiple data features but omits explicit mention of geography.

**Rank 5** · Comp = 0.360 · ❌ fail

> Does the phylogenetic clustering of bat coronavirus RdRp sequences mirror the phylogenetic structure of their bat hosts inferred from CytB, suggesting long-term codiversification rather than recent host switching?
>
> *Rationale:* The candidate question focuses on cophylogeny and evolutionary patterns of bat coronaviruses and hosts, which is a distinct scientific intent from the matched gold's focus on ecological drivers of RNA-virus diversity and human settlement circulation. Data grounding is excellent, but coverage of the gold's specific required elements is minimal.

### ✅ `glm-5` — Comp=0.748 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 3 | 5 | 3 | 5 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 4 | 1.275 | 0.255 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 4 | 1.275 | 0.255 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> How does bat host phylogeny, as resolved by CytB-COI-ITS barcoding, correlate with the taxonomic composition and diversity of RNA viruses detected in virome contigs, and can this relationship predict zoonotic spillover risk?
>
> *Rationale:* The candidate effectively links host phylogeny (via CytB-COI-ITS) to RNA-virus composition and diversity within the context of the provided dataset, aligning well with GQ_002's focus on ecological and biological predictors of viral diversity.

**Rank 2** · Comp = 0.620 · ✅ pass

> What is the phylogenetic diversity and host range of RNA viruses identified through RdRp motif analysis in the bat virome contigs?
>
> *Rationale:* The candidate question partially aligns with GQ_001 by focusing on bat RNA virus diversity and host range, but it omits the ecological drivers and human settlement aspects. It is a specific scientific question, well-grounded in data, but doesn't fully match the intent or acceptable variants of the gold question.

**Rank 3** · Comp = 0.748 · ✅ pass

> Do ecological factors recorded in the metadata explain variation in viral community composition across bat species identified by CytB-COI-ITS barcoding?
>
> *Rationale:* The candidate question strongly aligns with GQ_002, asking how ecological factors explain viral community composition in bats, and is well-grounded in specific data files. It covers most required elements, though it could be more explicit about geography and the statistical approach.

**Rank 4** · Comp = 0.255 · ❌ fail

> What is the concordance between host phylogeny reconstructed from mitochondrial genes (CytB, COI) versus nuclear ribosomal DNA (ITS) in the bat samples?
>
> *Rationale:* The candidate question focuses on bat host phylogeny, which is distinct from the gold question's intent of explaining RNA-virus richness. While well-grounded in data, it misses the core viral and ecological aspects of the matched gold question.

**Rank 5** · Comp = 0.255 · ❌ fail

> Can machine learning approaches applied to the phylogenetic data predict novel virus-host associations in the bat virome dataset?
>
> *Rationale:* The candidate question focuses on predicting host-virus associations using ML, which differs significantly from the gold question's focus on ecological drivers and covariates of viral richness. While it demonstrates strong data grounding by citing specific files, it misses the thematic core of the relevant gold questions.

### ✅ `gemini-2.5-flash` — Comp=0.799 · Pass@1=1.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 2 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 1 | 2 | 2 | 4 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 4 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 5 | 3 | 1 | 3 | 3 | 2.040 | 0.408 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.799 · ✅ pass

> How do ecological factors influence the diversity and composition of the viral community identified in the BtCN virome?
>
> *Rationale:* The candidate question strongly aligns with the gold question's intent to explore ecological drivers of viral diversity and composition, explicitly referencing the BtCN virome and relevant data files. It covers most required elements, missing only the explicit mention of a statistical model.

**Rank 2** · Comp = 0.400 · ❌ fail

> Can novel RNA viruses be identified within the BtCN virome by leveraging known RdRp motifs, and what are their phylogenetic relationships?
>
> *Rationale:* The candidate question focuses on identifying novel RNA viruses and their phylogenetic relationships using specific data files. While it touches on viral diversity and metatranscriptomes, it fundamentally misses the core intent of the matched gold question, which is about ecological drivers and human settlement circulation, resulting in a low match strength.

**Rank 3** · Comp = 0.306 · ❌ fail

> What are the phylogenetic relationships among the organisms represented by the CytB, COI, and ITS markers, and how do these relate to the broader ecological context?
>
> *Rationale:* The candidate question focuses on host phylogeny and its ecological context, which differs significantly from the gold's focus on RNA-virus diversity and its ecological drivers. While some elements like 'host traits' and 'ecological context' are present, the core subject of viruses is entirely missing, leading to a low match.

**Rank 4** · Comp = 0.680 · ✅ pass

> Can machine learning approaches be applied to the combined genetic datasets (virome, host markers) to predict specific ecological outcomes or host-virus associations?
>
> *Rationale:* The candidate question aligns well with GQ_002 by focusing on predicting ecological outcomes/host-virus associations using genetic and ecological data, similar to explaining virus patterns with covariates. It grounds in multiple data files, covering most required elements, though 'geography' is missing. It's similar to an acceptable variant.

**Rank 5** · Comp = 0.408 · ❌ fail

> What is the overall genetic diversity and taxonomic breadth of the BtCN virome, and how does it compare to other known viromes?
>
> *Rationale:* The candidate question describes the genetic diversity and taxonomic breadth of the BtCN virome, aligning with the 'virus richness or composition' element of GQ_002. However, it misses GQ_002's core intent of explaining this diversity using ecological covariates, resulting in a partial match.

### ✅ `intern-s1` — Comp=0.629 · Pass@1=1.00 · Pass@5=0.40

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 2 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.629 · ✅ pass

> How does the diversity and functional potential of viruses in the BtCN virome correlate with environmental factors from the ecological metadata?
>
> *Rationale:* The candidate asks how viral diversity in the BtCN-Virome correlates with environmental metadata. It matches the intent of GQ_002 by focusing on explanatory covariates for viral patterns, grounding the inquiry in specific dataset files while missing some of the broader host and geographic requirements.

**Rank 2** · Comp = 0.300 · ❌ fail

> What is the phylogenetic relationship between the identified viral contigs and known viral taxa using machine learning approaches?
>
> *Rationale:* The candidate question is about viral phylogeny and classification using ML, which is a distinct scientific question from `GQ_001`'s focus on ecological drivers of bat RNA-virus diversity and circulation. It covers few required elements but is well-grounded in data.

**Rank 3** · Comp = 0.560 · ❌ fail

> Can the CytB-COI-ITS genetic markers identify potential host species for the detected viruses?
>
> *Rationale:* The candidate question focuses on identifying host species for detected viruses using genetic markers. This is a foundational step for understanding virus ecology, partially aligning with GQ_001's intent but missing its broader scope of ecological drivers and human settlement circulation. It covers some required elements and is well-grounded in data.

**Rank 4** · Comp = 0.400 · ❌ fail

> How do RdRp motif variations in the virome dataset reflect viral replication strategies?
>
> *Rationale:* The candidate question focuses on molecular mechanisms of viral replication, which is distinct from the ecological and epidemiological intent of the matched gold question. It grounds well in data but misses most of the gold's required elements, resulting in a low match strength.

**Rank 5** · Comp = 0.629 · ✅ pass

> What are the temporal or spatial patterns in viral community composition based on the ecological metadata?
>
> *Rationale:* The candidate question effectively seeks to identify ecological factors (temporal/spatial patterns) influencing viral community composition, aligning with the gold's intent to explain viral diversity using covariates from ecological metadata. It grounds well in available data but omits some specific covariate types and the explicit mention of a statistical model.

### ✅ `intern-s1-pro` — Comp=0.629 · Pass@1=0.00 · Pass@5=0.20

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 1 | 4 | 1.105 | 0.221 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 4 | 1.275 | 0.255 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 4 | 1.275 | 0.255 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.323 · ❌ fail

> How do RdRp motif patterns correlate with the diversity and abundance of viral contigs in the BtCN virome dataset?
>
> *Rationale:* The candidate question focuses on viral sequence motifs rather than ecological modeling. While well-grounded in the provided data files, it fails to address the host traits, dietary/environmental covariates, or geography required to explain RNA-virus diversity in an ecological context, making it a poor fit for the requested ecological modeling gold standard.

**Rank 2** · Comp = 0.221 · ❌ fail

> What phylogenetic relationships can be inferred from CytB, COI, and ITS sequences across different species in the dataset?
>
> *Rationale:* The candidate question focuses on inferring phylogenetic relationships from host genetic markers, whereas the gold questions concern the ecological drivers and modeling of RNA-virus diversity. While the candidate is scientifically valid and well-grounded in the provided data files, it fails to address the specific scientific inquiry regarding virome composition and ecological covariates.

**Rank 3** · Comp = 0.629 · ✅ pass

> How do environmental variables in the ecological metadata correlate with viral community composition?
>
> *Rationale:* The candidate question effectively seeks to correlate environmental metadata with viral community composition using specific datasets. While it lacks explicit mention of host traits or geographic factors required by the gold standard, it maintains a strong scientific focus on ecological modeling.

**Rank 4** · Comp = 0.255 · ❌ fail

> Can machine learning models trained on phylogenetic features accurately classify viral sequences from the virome dataset?
>
> *Rationale:* The candidate question focuses on ML classification of viral sequences, a methodological task, which differs significantly from GQ_002's ecological explanatory intent. Only the 'statistical model' element is covered, and the question's specific framing does not align with any acceptable variants for GQ_002.

**Rank 5** · Comp = 0.255 · ❌ fail

> What is the relationship between viral contig length distribution and the presence of RdRp motifs in the virome dataset?
>
> *Rationale:* The candidate question is about sequence features (contig length, RdRp motifs) which is a different scientific question from the matched gold's focus on ecological drivers of virus diversity. While well-grounded in data, it misses most required elements and does not align with the gold's acceptable framing.

### ✅ `intern-s1-mini` — Comp=0.527 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 2 | 3 | 1.190 | 0.238 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_002 (U) |
| 4 | 4 | 2 | 3 | 3 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 5 | 1 | 2 | 2 | 3 | 1.700 | 0.340 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.476 · ❌ fail

> How do environmental factors correlate with viral contig abundance in metagenomic datasets?
>
> *Rationale:* The candidate asks a valid ecological question regarding environmental drivers of viral abundance. It identifies relevant data files but lacks the comprehensive scope of host and geographic variables required by the gold standard for full modeling.

**Rank 2** · Comp = 0.238 · ❌ fail

> What genetic diversity patterns emerge from CytB-COI-ITS marker sequences across taxonomic groups?
>
> *Rationale:* The candidate question focuses on host genetic diversity patterns using specific markers, which fundamentally differs from GQ_002's intent to explain viral diversity with covariates. It only covers one required element and is far from acceptable variants.

**Rank 3** · Comp = 0.100 · ❌ fail

> How do machine learning models compare to traditional methods in phylogenetic reconstruction?
>
> *Rationale:* The candidate question focuses on the technical performance of phylogenetic algorithms rather than the ecological drivers of bat viral diversity. It is unrelated to the provided gold questions, which prioritize virome-host ecology and environmental metadata over computational method benchmarking.

**Rank 4** · Comp = 0.527 · ❌ fail

> What ecological factors drive species coexistence patterns in the provided metadata?
>
> *Rationale:* The candidate question aligns with GQ_002's intent to find ecological drivers of biological patterns, but it is more general, lacking the specific focus on 'RNA-virus richness and composition in bats'. It grounds well in the provided metadata file.

**Rank 5** · Comp = 0.340 · ❌ fail

> How might RdRp motif patterns inform viral host range predictions?
>
> *Rationale:* The candidate question is about predicting viral host range using genetic motifs, which is distinct from the gold's focus on ecological drivers of bat RNA-virus diversity and circulation. It covers few required elements and is not close to any acceptable variants.

### ✅ `intern-s2-preview` — Comp=0.731 · Pass@1=0.00 · Pass@5=0.35

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 2 | 4 | 5 | 4 | 4 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 3 | 1 | 0 | 3 | 4 | 1.400 | 0.280 | ❌ | GQ_001 (U) |
| 4 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 5 | 5 | 2 | 4 | 5 | 3.315 | 0.663 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.400 · ❌ fail

> Can novel viral lineages be identified by matching RdRp motifs from the motif collection against full-spectrum virome contigs?
>
> *Rationale:* The candidate question is about viral discovery methodology, which differs significantly from the gold's focus on ecological drivers and circulation. While it references specific data, its intent is not aligned with the gold's core scientific question.

**Rank 2** · Comp = 0.731 · ✅ pass

> How does viral community composition inferred from contig abundance correlate with ecological metadata parameters?
>
> *Rationale:* The candidate question closely matches GQ_002's intent to link viral community composition to ecological metadata, covering all required elements and referencing specific data. It is slightly less specific on host and virus type than the gold question.

**Rank 3** · Comp = 0.280 · ❌ fail

> Do machine learning phylogenetic methods produce more accurate viral classifications than traditional motif-based approaches?
>
> *Rationale:* The candidate question focuses on comparing viral classification methodologies, which is distinct from the ecological and epidemiological scope of the provided gold questions. It is a valid question but does not align with the specific intents of the gold standards.

**Rank 4** · Comp = 0.400 · ❌ fail

> What is the diversity and distribution of RdRp motifs across different viral families in the virome dataset?
>
> *Rationale:* The candidate question focuses on molecular diversity of viral motifs, which differs significantly from GQ_001's intent regarding ecological drivers and human settlement circulation. It covers few required elements but is a well-grounded, specific question, though not aligned with the gold's core purpose.

**Rank 5** · Comp = 0.663 · ✅ pass

> Can host-virus interaction patterns be inferred from the combined virome and ecological metadata datasets?
>
> *Rationale:* The candidate question strongly aligns with the gold's intent to use ecological data to explain viral patterns. It grounds well in data but misses explicit mention of geography, specific viral outcomes (richness/composition), and the statistical modeling aspect in its core framing.


## 4 · `flavi_jingmen_jvi_2016`

- **raw**：1 文件: `nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ❌ `claude-code-opus-4-7` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 15 column 4 (char 1180)`

### ✅ `gpt-5.5-high` — Comp=0.476 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 2 | 3 | 1 | 4 | 5 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 3 | 1 | 0 | 3 | 4 | 1.400 | 0.280 | ❌ | GQ_001 (U) |
| 4 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.320 · ❌ fail

> Do the 33 reported complete viral sequences exhibit host-associated evolutionary structure across their named source groups, as reflected in genome architecture, predicted ORF organization, GC content, codon usage, and within-dataset sequence similarity?
>
> *Rationale:* The candidate question is too general, focusing on broad host-associated viral evolution and genomic features for generic viral sequences, missing the specific Flaviviridae-related viruses, segmentation, and transcriptome data central to the matched gold question.

**Rank 2** · Comp = 0.476 · ❌ fail

> Do the five four-segment virus genomes share conserved segment-size hierarchy, terminal motifs, and coding organization consistent with a common segmented insect-virus lineage?
>
> *Rationale:* The candidate question aligns with GQ_002's focus on genome architecture for inferring relationships, though it lacks specificity regarding NS3/NS5 and flavi-like viruses. It is well-grounded in specific data features and is a high-quality question.

**Rank 3** · Comp = 0.280 · ❌ fail

> Are the thirteen complete polyprotein CDS viruses separable into compositionally distinct genome classes by length, GC content, codon usage, and predicted polyprotein ORF coverage?
>
> *Rationale:* The candidate question is about compositional classification of polyprotein CDS viruses, which is a very weak match to GQ_001's specific focus on Flaviviridae-related viruses and transcriptomes. It lacks all required elements but is a well-formed question with strong data grounding.

**Rank 4** · Comp = 0.320 · ❌ fail

> Is genome size among the complete polyprotein CDS records associated with nucleotide composition and named source organism, suggesting different evolutionary constraints across shark, tick, mosquito, spider, centipede, water strider, fly, lacewing, and barnacle viruses?
>
> *Rationale:* The candidate question is about general viral genome characteristics and evolutionary constraints across diverse hosts, which is largely unrelated to the specific Flaviviridae/jingmenvirus/flavi-like focus of the matched gold question. While well-grounded in data, it misses most of the gold's required elements and specific intent.

**Rank 5** · Comp = 0.240 · ❌ fail

> Do related source and naming groups, especially Wuhan aphid virus 1 versus Wuhan aphid virus 2 and Xinzhou spider virus 2 versus Xinzhou spider virus 3, show parallel or divergent genome signatures that could indicate source-specific virus diversification?
>
> *Rationale:* The candidate question focuses on intra-group diversification of specific named viruses using genome signatures, which is fundamentally different from the gold question's intent to discover segmented jingmenviruses and flavi-like viruses from transcriptomes to revise Flaviviridae evolution.

### ✅ `claude-code-sonnet-4-6` — Comp=0.578 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 2 | 5 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 5 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 3 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 4 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 5 | 0.935 | 0.187 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.272 · ❌ fail

> Do invertebrate-infecting RNA viruses with large polyprotein genomes (>15 kb) in this dataset (KR902730–KR902741) exhibit significantly higher CpG dinucleotide obs/exp ratios compared to the four-segment arthropod viruses (KR902709–KR902728), indicating that genome architecture rather than arthropod host taxon is the primary determinant of nucleotide composition bias across this novel invertebrate RNA virosphere?
>
> *Rationale:* The candidate question investigates CpG bias based on genome architecture in invertebrate RNA viruses, citing specific accession numbers. It does not align with the gold's focus on NS3/NS5 phylogenies or relationships between jingmenviruses and flavi-like viruses, despite mentioning genome architecture.

**Rank 2** · Comp = 0.306 · ❌ fail

> Is there a significant positive correlation between polyprotein genome length and GC content across the 13 unsegmented RNA viruses (KR902729–KR902741) infecting diverse invertebrate and one vertebrate host, suggesting that larger RNA virus genomes tolerate or require higher GC content to maintain RNA secondary structure stability?
>
> *Rationale:* The candidate question investigates genome length and GC content correlation in unsegmented RNA viruses, hypothesizing about RNA secondary structure stability. It poorly matches GQ_002, which focuses on phylogenetic relationships and genome architectures of specific flavi-like and jingmenviruses, missing most required elements despite strong data grounding.

**Rank 3** · Comp = 0.578 · ❌ fail

> Do the five four-segment RNA viruses (Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, Wuhan aphid virus 1, Wuhan aphid virus 2; KR902709–KR902728) share a conserved segment-size hierarchy (segment 1 largest, segment 2 smallest) that is consistent across all five viruses and reflects conserved RNA-dependent RNA polymerase gene placement, supporting a common evolutionary origin for this arthropod-infecting segmented RNA virus clade?
>
> *Rationale:* The candidate question aligns with GQ_002 by using genome architecture (segment size, RdRp placement) to infer evolutionary relationships for segmented RNA viruses. It is highly data-grounded but misses specific virus types (jingmenvirus, flavi-like) and explicit NS3/NS5 focus from the gold question.

**Rank 4** · Comp = 0.100 · ❌ fail

> Does the Wenling shark virus (KR902729), the sole vertebrate-hosted virus in this dataset, exhibit measurably distinct nucleotide composition (GC content 55.2%, CpG obs/exp 0.759) compared to the 32 invertebrate-hosted viruses (GC range 34.3–56.1%, CpG obs/exp range 0.426–1.025), and does this divergence indicate early host-driven compositional adaptation occurring even for viruses newly discovered by metagenomics?
>
> *Rationale:* The candidate question is about host-driven nucleotide compositional adaptation of the Wenling shark virus, which is unrelated to the Flaviviridae-specific evolutionary questions in the gold set. Despite the poor match, it demonstrates excellent data grounding with specific numerical evidence.

**Rank 5** · Comp = 0.187 · ❌ fail

> Among the 20 genome segments from the five four-segment arthropod RNA viruses (KR902709–KR902728), does GC content vary systematically by segment number (i.e., is segment 2, the smallest and most conserved, consistently the most or least GC-rich within each virus), suggesting segment-specific nucleotide composition constraints linked to encoded protein function or RNA structure?
>
> *Rationale:* The candidate asks a specific bioinformatic question about GC content patterns across segments of arthropod viruses. While highly grounded in specific accession data, it misses the thematic scope of the provided gold questions, which center on evolutionary links and broader genome architecture, and thus does not satisfy the required elements.

### ✅ `gemini-3.1-pro` — Comp=0.510 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 3 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 1 | 3 | 1.020 | 0.204 | ❌ | GQ_002 (S) |
| 5 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.510 · ❌ fail

> How conserved is the segment organization and sequence homology across the different insect-associated viruses (cricket, flea, aphid) identified in this dataset?
>
> *Rationale:* The candidate question aligns with GQ_002's focus on genome architecture and sequence relationships among segmented viruses, but it lacks specificity regarding NS3/NS5, jingmenviruses, and flavi-like viruses. It is well-grounded in the provided data.

**Rank 2** · Comp = 0.408 · ❌ fail

> What are the phylogenetic relationships among the newly identified Wuhan insect viruses based on their segment sequences?
>
> *Rationale:* The candidate question partially aligns with the gold's intent to explore phylogenetic relationships of segmented viruses but lacks specificity regarding protein markers and virus types. It covers few required elements and is generic compared to acceptable variants, though it grounds in data.

**Rank 3** · Comp = 0.476 · ❌ fail

> Is there evidence of segment reassortment among these segmented insect viruses?
>
> *Rationale:* The candidate partially matches GQ_002 by focusing on phylogenetic analysis of segmented genomes for reassortment, but it lacks the specific protein and virus family context. It covers some required elements and shows good data grounding by referencing specific segments and a file.

**Rank 4** · Comp = 0.204 · ❌ fail

> Are there conserved non-coding regulatory elements at the termini of the viral segments across different species?
>
> *Rationale:* The candidate question is a generic inquiry about regulatory elements in segmented viral genomes, broadly relating to genome architecture but lacking the specific virus types, phylogenetic context, and protein markers central to the matched gold question. It grounds in the provided FASTA file for terminal sequence analysis.

**Rank 5** · Comp = 0.400 · ❌ fail

> Can we identify host-specific sequence signatures or adaptations in the viral genomes corresponding to their insect hosts (cricket, flea, aphid)?
>
> *Rationale:* The candidate question is a poor match for GQ_001, focusing on general host adaptation rather than specific Flaviviridae-related viruses and their evolution. It covers few required elements and is not close to any acceptable variant, though it is more specific than the unacceptable ones. Data grounding is strong, referencing specific viral genomes and hosts.

### ❌ `deepseek-v4-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `glm-5` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ✅ `gemini-2.5-flash` — Comp=0.320 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 1 | 3 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 3 | 1.600 | 0.320 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.272 · ❌ fail

> What is the phylogenetic relationship and genetic diversity among the reported viral sequences in the dataset?
>
> *Rationale:* The candidate question is too generic, only broadly touching on phylogeny without the specific viral types, genes, or genomic features of the matched gold question. It covers only one required element and is closer to an unacceptable variant due to its lack of specificity.

**Rank 2** · Comp = 0.320 · ❌ fail

> How do the reported viral sequences vary in terms of their host organisms and geographical origins?
>
> *Rationale:* The candidate question is a general descriptive query about host and geographical origin of viral sequences. It does not align with the specific intent of GQ_001, which focuses on discovering specific virus types from transcriptomes to revise Flaviviridae evolution and host range. Only the broad concept of 'host' is shared.

**Rank 3** · Comp = 0.180 · ❌ fail

> Are there common conserved genetic motifs or functional domains present across different viral sequences in the dataset?
>
> *Rationale:* The candidate question is too generic, focusing on general conserved motifs in viral sequences rather than the specific Flaviviridae-related viruses, data sources, and evolutionary context of the gold question. It misses all specific required elements and is far from acceptable variants.

**Rank 4** · Comp = 0.280 · ❌ fail

> What is the distribution of sequence lengths for the reported viral segments or complete genomes within the dataset?
>
> *Rationale:* The candidate question is a generic descriptive query about sequence length distribution, which is fundamentally different from the gold's specific, hypothesis-driven inquiry into Flaviviridae evolution and novel virus discovery. It covers very few required elements and lacks the specificity of acceptable variants.

**Rank 5** · Comp = 0.060 · ❌ fail

> What is the prevalence of different viral strains or species within the reported sequences, and how are they represented in the dataset?
>
> *Rationale:* The candidate question is a generic data inventory query about viral prevalence, completely lacking the specific focus on Flaviviridae, jingmenviruses, flavi-like viruses, transcriptomes, evolution, or genome organization central to the gold question.

### ✅ `intern-s1` — Comp=0.357 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 3 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 1 | 1 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 4 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.357 · ❌ fail

> Can we determine the evolutionary relationships between different virus strains based on their sequences?
>
> *Rationale:* The candidate broadly asks about viral evolutionary relationships, aligning with the phylogenetic aspect of GQ_002 but missing its specific viral and genomic context. It is a generic question, well-grounded in the provided data features.

**Rank 2** · Comp = 0.272 · ❌ fail

> How does genetic diversity vary between different segments of the same virus strain?
>
> *Rationale:* The candidate question is a generic inquiry into genetic diversity across viral segments, broadly touching on genome architecture but lacking the specific virus types, phylogenetic focus, and comparative intent of the matched gold question (GQ_002). It covers few required elements and is not close to any specific acceptable or unacceptable variants.

**Rank 3** · Comp = 0.060 · ❌ fail

> Are there conserved regions across different virus strains that could serve as diagnostic targets?
>
> *Rationale:* The candidate question is off-topic, focusing on broad diagnostic development rather than the specific evolutionary study of segmented jingmenviruses and flavi-like viruses required by the gold standard.

**Rank 4** · Comp = 0.180 · ❌ fail

> Is there evidence of recombination between different virus strains?
>
> *Rationale:* The candidate question is about general viral recombination, which is semantically distant from the specific Flaviviridae-focused evolution and discovery intent of the matched gold question. It lacks coverage of all specific required elements and is generic in nature, though not identical to, the unacceptable variants. It does, however, ground in a specific data file with some concrete framing.

**Rank 5** · Comp = 0.280 · ❌ fail

> Do different virus strains exhibit codon usage bias correlated with their host organisms?
>
> *Rationale:* The candidate question is a general inquiry about codon usage bias and host correlation in viruses, which is a different scientific question from the gold's specific focus on Flaviviridae, jingmenviruses, and flavi-like viruses from transcriptomes. It covers only one required element and is not close to any acceptable or unacceptable variants.

### ✅ `intern-s1-pro` — Comp=0.425 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 1 | 2 | 1.275 | 0.255 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 1 | 2 | 3 | 3 | 1.615 | 0.323 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What is the phylogenetic relationship between Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7, and Wuhan aphid viruses based on nucleotide sequence similarity across their complete genomic segments?
>
> *Rationale:* The candidate asks about phylogenetic relationships of specific insect viruses using genomic segments. It aligns with GQ_002's focus on phylogenies and genome architecture but misses the specific virus groups and protein markers, resulting in partial coverage of required elements.

**Rank 2** · Comp = 0.255 · ❌ fail

> Do the segmented viruses in this dataset show evidence of inter-segment recombination events that could indicate reassortment between different viral strains?
>
> *Rationale:* The candidate addresses recombination and reassortment in segmented viruses but lacks the specific focus on Flaviviridae-related evolution, Jingmenviruses, or the phylogenetic evidence required by the gold standards.

**Rank 3** · Comp = 0.120 · ❌ fail

> Are there host-specific nucleotide sequence patterns or motifs that distinguish viruses infecting crickets, fleas, and aphids in this dataset?
>
> *Rationale:* The candidate question is unrelated to the gold question's specific focus on Flaviviridae evolution and specific virus types. It lacks coverage of all required elements and does not align with the specificity of acceptable variants, though it is well-grounded in data.

**Rank 4** · Comp = 0.060 · ❌ fail

> What are the most conserved genomic regions across all viral segments in this dataset, and could these represent functional elements or potential targets for antiviral interventions?
>
> *Rationale:* The candidate question is a general genomics inquiry about conserved regions and functional elements, which is fundamentally different from the specific evolutionary and host range questions about Flaviviridae, jingmenviruses, and flavi-like viruses posed by the gold question.

**Rank 5** · Comp = 0.323 · ❌ fail

> How do nucleotide substitution rates vary between different viral segments and strains in this dataset, and what does this suggest about their evolutionary pressures?
>
> *Rationale:* The candidate question is a general molecular evolution query about substitution rates and evolutionary pressures in viral segments. It poorly matches the specific intent of GQ_002, which focuses on NS3/NS5 phylogenies and genome architectures of specific virus groups.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.357 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 1 | 3 | 1.360 | 0.272 | ❌ | GQ_002 (S) |
| 3 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 4 | 1 | 0 | 2 | 3 | 0.935 | 0.187 | ❌ | GQ_002 (S) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |

**Rank 1** · Comp = 0.200 · ❌ fail

> Do segmented viral genomes show consistent nucleotide composition biases across their multiple segments, suggesting shared evolutionary constraints or replication mechanisms?
>
> *Rationale:* The candidate question investigates general nucleotide composition biases in segmented viral genomes and their evolutionary implications. It does not align with the matched gold question's specific focus on discovering Flaviviridae-related jingmenviruses and flavi-like viruses from transcriptomes. While well-grounded in data, it misses all specific required elements.

**Rank 2** · Comp = 0.272 · ❌ fail

> Is there a correlation between segment length and coding potential in segmented viral genomes, with longer segments encoding more or larger proteins?
>
> *Rationale:* The candidate question is a general inquiry into segmented viral genome organization, specifically segment length and coding potential. It weakly matches GQ_002's theme of genome architecture but misses the specific focus on jingmenviruses, flavi-like viruses, and their relationships, making it too generic compared to the gold's intent and acceptable variants.

**Rank 3** · Comp = 0.357 · ❌ fail

> Do polyprotein-containing viruses exhibit different nucleotide composition patterns compared to segmented viruses, reflecting distinct replication strategies?
>
> *Rationale:* The candidate question broadly touches on genome architecture comparison but lacks the specificity of the gold question regarding virus types and analytical methods. It covers few required elements and is not close to any specific acceptable or unacceptable variants.

**Rank 4** · Comp = 0.187 · ❌ fail

> Are there conserved nucleotide motifs at segment boundaries in multi-segment viral genomes that could serve as replication or packaging signals?
>
> *Rationale:* The candidate question is too general, focusing on universal features of segmented viral genomes rather than the specific Flaviviridae-related viruses and phylogenetic analyses central to the matched gold question. It misses all specific required elements.

**Rank 5** · Comp = 0.060 · ❌ fail

> What is the GC content distribution across different viral segments and how does it vary between virus families, indicating lineage-specific compositional constraints?
>
> *Rationale:* The candidate question about GC content distribution in viral segments and families is entirely unrelated to the specific topics of Flaviviridae, jingmenviruses, flavi-like viruses, or NS3/NS5 phylogenies covered by the gold questions. It therefore matches none of the gold questions.


## 5 · `invertebrate_rna_virosphere_2016`

- **raw**：2 文件: `5905695_alignments_and_phylogenies.zip, 5905698_all_virus_genomes.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=1.000 · Pass@1=0.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 3 | 2 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 4 | 3 | 5 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 5 | 4 | 5 | 5 | 5 | 4.600 | 0.920 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.520 · ❌ fail

> Across the six RNA virus supergroups (hepe, luteo, narna, permutotetra, tombus, weivirus) for which paired RdRp and structural-protein alignments and phylogenies are provided, do the replicase (RdRp) and virion-structural (capsid S-domain / A6 / A21 / Alverna) trees show statistically significant topological incongruence indicative of widespread modular horizontal gene transfer of replicase versus virion modules during invertebrate RNA-virus evolution?
>
> *Rationale:* The candidate question is a sophisticated evolutionary query about HGT via tree incongruence in invertebrate RNA viruses. While it shares the broad topic of RNA virus evolution with GQ_001, its specific intent differs from redefining breadth/deep lineages. It demonstrates excellent data grounding but does not align with GQ_001's specific acceptable variants.

**Rank 2** · Comp = 1.000 · ✅ pass

> Within the >2,300 invertebrate-derived RNA virus sequences, do viral RdRp phylogenies recover stronger clustering by invertebrate host taxon (insect, spider, tick, crab, shrimp, worm) or by Chinese sampling location (Beihai, Hubei, Wuhan, Wenzhou, Shahe, Changjiang), and does the relative strength of host-versus-geography signal differ systematically between segmented and monolithic-genome supergroups?
>
> *Rationale:* The candidate question is a highly specific and well-grounded phylogenetic analysis that directly contributes to understanding the diversity and evolution of the RNA virosphere from invertebrate sources, covering all required elements with strong data references.

**Rank 3** · Comp = 1.000 · ✅ pass

> Does the position of basal invertebrate-virus lineages on the per-supergroup RdRp phylogenies (e.g. the deep Beihai picorna-like virus clades in the Picorna-Calici tree, novel Wei/Qin/Zhao/Yan-virus lineages, and Hepe-Virga long branches) statistically support invertebrates as the ancestral host reservoir from which plant, fungal and vertebrate RNA virus families were derived?
>
> *Rationale:* The candidate question strongly aligns with GQ_001 by investigating the evolutionary origins of RNA viruses using phylogenetic evidence from invertebrate lineages. It covers all required elements, is highly specific, and is well-grounded in the provided data, asking if invertebrates are the ancestral host reservoir.

**Rank 4** · Comp = 0.680 · ✅ pass

> How does genome architecture — specifically the number of recoverable segments and the overall genome length — vary across the 22 RdRp-defined RNA-virus supergroups in this dataset, and is segment number a phylogenetically conserved trait or one that has evolved repeatedly within supergroups?
>
> *Rationale:* The candidate question closely aligns with GQ_002's focus on genome architecture, segmentation, and length, but shifts the goal from 'manual curation' to understanding variation and evolutionary patterns. It is a well-grounded and specific scientific inquiry.

**Rank 5** · Comp = 0.920 · ✅ pass

> Do branch-length distributions and within-supergroup nucleotide diversity in the trimmed RdRp alignments differ significantly between negative-sense (Bunya-Arena, Mono-Chu, Orthomyxo) and positive-sense / dsRNA (Picorna-Calici, Tombus-Noda, Reo, Partiti-Picobirna) supergroups, suggesting different long-term substitution-rate or selective regimes among invertebrate RNA viruses?
>
> *Rationale:* The candidate question strongly aligns with the gold's intent to understand the evolutionary dynamics of RNA viruses from invertebrates, specifically focusing on how substitution rates and selective regimes contribute to their diversity and deep lineages. It covers all required elements, is highly specific, and demonstrates excellent data grounding.

### ✅ `gpt-5.5-high` — Comp=0.820 · Pass@1=1.00 · Pass@5=0.85

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 3 | 3 | 4 | 4 | 5 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.760 · ✅ pass

> Do discordances between RdRp phylogenies and structural-protein phylogenies in the provided RNA virus genomes reveal modular evolution and interclade structural gene exchange among Hepe-Virga, Luteo-Sobemo, Narna-Levi, Permutotetra, Tombus-Noda, and New-Weivirus-like viruses?
>
> *Rationale:* The candidate question aligns with GQ_001's focus on RNA virus evolution and deep lineages through phylogenetic analysis, specifically investigating modular evolution and gene exchange. It covers assembled genomes, deep lineages, and phylogenetic analysis, but omits invertebrate origin and broad virosphere redefinition. The question is highly specific and well-grounded in provided data files.

**Rank 2** · Comp = 0.820 · ✅ pass

> Do the RdRp alignments and phylogenies support New-Qinvirus, New-Weivirus, New-Yanvirus, and New-Zhaovirus as distinct RNA virus lineages relative to established RdRp-defined groups?
>
> *Rationale:* The candidate question effectively addresses the identification of new deep RNA virus lineages using phylogenetic analysis, aligning well with the gold question's intent. It is highly specific and well-grounded in the provided data, though it omits explicit mention of invertebrate transcriptomes as the source.

**Rank 3** · Comp = 0.629 · ✅ pass

> How is genome architecture, including segmentation and encoded RdRp, capsid, nucleoprotein, and glycoprotein components, associated with the 22 virus group labels in the genome FASTA?
>
> *Rationale:* The candidate question aligns well with GQ_002's focus on genome architecture and segmentation, though it shifts the purpose from manual curation to association with group labels. It demonstrates strong data grounding by referencing specific FASTA features and components.

**Rank 4** · Comp = 0.578 · ❌ fail

> Do genome length and nucleotide composition differ systematically among the major RNA virus groups represented in the 2,339 genome FASTA records?
>
> *Rationale:* The candidate question explores systematic differences in genome length and nucleotide composition among RNA virus groups from FASTA records. It aligns with GQ_002's focus on genome characteristics but misses the specific intent of identifying features for manual curation or segmentation patterns. Data grounding is excellent with specific numerical evidence.

**Rank 5** · Comp = 0.620 · ✅ pass

> Are sampling-location labels embedded in genome names, such as Hubei, Beihai, Wuhan, and Wenzhou, associated with different RNA virus group diversity and RdRp phylogenetic representation?
>
> *Rationale:* The candidate question explores how sampling locations relate to RNA virus diversity and phylogeny, aligning with GQ_001's goal of understanding viral breadth and lineages. It covers several required elements and is well-grounded in specific data features, but lacks explicit mention of invertebrate transcriptomes or the ambition to 'redefine' the virosphere.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 5 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Do the RdRp-based and structural-protein-based phylogenies of the invertebrate RNA viruses in the RdRp_versus_structural alignments show statistically congruent topologies across the Hepe-Virga, Luteo-Sobemo, Narna-Levi, Permutotetra, Tombus-Noda, and New-Weivirus lineages, or do systematic topological incongruences implicate modular capsid evolution and inter-lineage structural gene exchange as drivers of RNA virome diversification in invertebrates?
>
> *Rationale:* This question precisely investigates the evolutionary drivers of RNA virome diversification in invertebrates using detailed phylogenetic congruence analysis. It is highly specific, well-grounded in data, and directly addresses the mechanisms shaping deep lineages and breadth of the RNA virosphere.

**Rank 2** · Comp = 1.000 · ✅ pass

> Do the five entirely new RNA virus superfamilies (New-Weivirus, New-Qinvirus, New-Zhaovirus, New-Yanvirus, New-Yuevirus) discovered in the Chinese invertebrate metatranscriptome form monophyletic lineages in the 20 RdRp-based PhyML phylogenies, and can their genomic and phylogenetic signatures reveal which established RNA virus superfamily each is most closely related to?
>
> *Rationale:* The candidate question precisely addresses the phylogenetic placement of novel RNA virus superfamilies from invertebrate metatranscriptomes, directly aligning with the goal of understanding deep lineages and the breadth of the RNA virosphere. It is highly specific and well-grounded in the provided data.

**Rank 3** · Comp = 0.820 · ✅ pass

> Do invertebrate-associated Nidovirales in 5905698_all_virus_genomes.fasta encode large genomes (>20 kb) comparable to vertebrate coronaviruses, and does their placement in the Nido_RdRp_phylogeny.nwk indicate that large-genome RNA complexity evolved before the emergence of vertebrate nidoviruses?
>
> *Rationale:* The candidate question aligns well with GQ_001's focus on deep lineages and evolutionary understanding within the RNA virosphere, specifically through phylogenetic analysis of invertebrate-associated assembled virus genomes. It is highly data-grounded and well-framed, resembling acceptable variants.

**Rank 4** · Comp = 0.620 · ✅ pass

> Do the 249 Bunya-Arena group viruses in 5905698_all_virus_genomes.fasta, which span arthropod, crustacean, and marine invertebrate hosts across multiple Chinese sampling sites, show evidence of host-associated genome segment reassortment — specifically, do RdRp, Glycoprotein, and Nucleoprotein segments from the same putative virus co-cluster in Negative_Bunya-Arena_RdRp_phylogeny.nwk, or does phylogenetic incongruence among segments indicate frequent reassortment events?
>
> *Rationale:* The candidate question is a specific, well-grounded scientific inquiry into viral reassortment in invertebrates, aligning with the general domain of GQ_001 but missing its broader scope of redefining virosphere breadth and deep lineages. It scores well on data grounding and acceptability.

**Rank 5** · Comp = 0.940 · ✅ pass

> Do the 603 Picorna-Calici group virus genomes from diverse Chinese invertebrate hosts in 5905698_all_virus_genomes.fasta form host-specific phylogenetic clusters in the Picorna-Calici_RdRp_phylogeny.nwk, indicating host-driven diversification, or do viruses from phylogenetically distant invertebrate hosts (arthropods vs. molluscs vs. crustaceans) intermix across the tree, supporting cross-phylum host-switching as the primary driver of picorna-like virus diversity?
>
> *Rationale:* The candidate question is an excellent, highly specific instance of GQ_001, focusing on phylogenetic analysis of deep lineages and diversification drivers within a specific viral group from invertebrate hosts. It is well-grounded in data and aligns perfectly with the scientific rigor of acceptable variants.

### ✅ `gemini-3.1-pro` — Comp=0.640 · Pass@1=1.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 5 | 1 | 2 | 3 | 5 | 2.100 | 0.420 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.640 · ✅ pass

> What are the evolutionary relationships and genomic architectural differences between the plant-infecting potyviruses and the diverse astro-like viruses within the provided "Astro-Poty" dataset?
>
> *Rationale:* The candidate question asks about evolutionary relationships and genomic architectural differences between specific virus groups. It aligns with GQ_001's focus on deep lineages and phylogenetic analysis but diverges in host specificity and the broad goal of redefining the RNA virosphere breadth. It is well-grounded in the provided data.

**Rank 2** · Comp = 0.544 · ❌ fail

> Does the genome length of the viruses in the "Astro-Poty" dataset correlate with their specific viral lineage or host type (e.g., plant vs. other)?
>
> *Rationale:* The question investigates genome length correlation with lineage/host, partially aligning with the gold's focus on genome architecture. It covers key elements like genome length and assembled genomes, but misses segmentation and manual curation. Data grounding is excellent, citing specific file features and examples.

**Rank 3** · Comp = 0.560 · ❌ fail

> Are there specific conserved nucleotide motifs or regions that are shared across all diverse members of the "Astro-Poty" group, despite their different origins and genome lengths?
>
> *Rationale:* The candidate question partially aligns with understanding viral evolution and grouping through conserved motifs, but it lacks the broader scope and specific host context of the gold question. It is well-grounded in the provided data files.

**Rank 4** · Comp = 0.620 · ✅ pass

> How does the nucleotide composition (e.g., GC content) vary among the different viral species within the provided FASTA dataset, and does it reflect their evolutionary divergence?
>
> *Rationale:* The candidate question partially aligns with GQ_001 by focusing on evolutionary divergence and phylogenetic analysis of viral genomes, but it lacks the specific context of invertebrate transcriptomes and redefining the RNA virosphere's breadth. It grounds well in data but is a generic scientific question.

**Rank 5** · Comp = 0.420 · ❌ fail

> Can the geographic origin of the astro-like viruses (e.g., Beihai, Changjiang, Hubei) be correlated with specific phylogenetic clades within the "Astro-Poty" dataset?
>
> *Rationale:* The candidate question asks about phylogeography of specific astro-like viruses, which is a different intent from GQ_001's focus on broad RNA virosphere discovery from invertebrate transcriptomes. While it uses phylogenetic analysis, it misses core elements of the gold question, though it is well-grounded in data.

### ✅ `deepseek-v4-pro` — Comp=0.680 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 2 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 4 | 3 | 3 | 4 | 4 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 5 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> Does the RdRp phylogeny of the Astro-Poty and Bunya-Arena virus families in this dataset reveal statistically supported host-switching events between arthropod and plant hosts, consistent with vector-borne cross-kingdom transmission?
>
> *Rationale:* The candidate question aligns with the evolutionary aspect of GQ_001, focusing on host-switching via RdRp phylogeny. It's a well-grounded, specific scientific question, though it doesn't aim to redefine the entire virosphere's breadth or deep lineages.

**Rank 2** · Comp = 0.374 · ❌ fail

> Is there a significant correlation between viral genome length and host taxonomic breadth across the four RNA virus family-groups (Astro-Poty, Bunya-Arena, Birna, Toti-Chryso) represented in this dataset?
>
> *Rationale:* The candidate shifts from the gold standard's emphasis on structural curation and metadata quality to an ecological investigation of virus genome size relative to host diversity. While technically grounded in the provided FASTA file structure, it diverges significantly from the clinical/bioinformatic focus of GQ_002 on viral genome assembly properties.

**Rank 3** · Comp = 0.680 · ✅ pass

> Do the Bunya-Arena virus sequences in this dataset cluster by host phylum (Arthropoda, Mollusca, Annelida) rather than by geographic sampling location, supporting host-driven rather than geography-driven diversification?
>
> *Rationale:* The candidate partially aligns with GQ_001's intent on invertebrate viral evolution and deep lineages, but is narrower in scope. It covers most relevant required elements and is a high-quality, data-grounded question, though not directly matching any specific acceptable variant.

**Rank 4** · Comp = 0.660 · ✅ pass

> Within the Toti-Chryso family-group from this dataset, does the phylogeny inferred from the capsid protein gene recapitulate the same host-association topology as the RdRp gene tree, or is there evidence of reassortment or recombination between arthropod-infecting lineages?
>
> *Rationale:* The candidate asks about phylogenetic incongruence between viral genes (capsid, RdRp) in Toti-Chryso viruses to detect reassortment/recombination, implying viral evolution. It aligns with GQ_001's use of phylogenetic analysis for viral evolution but differs in scope, focusing on specific events rather than broad diversity. It is well-grounded and scientifically rigorous.

**Rank 5** · Comp = 0.408 · ❌ fail

> Are there conserved RNA secondary structure elements in the untranslated regions of Astro-Poty virus genomes from this dataset that can be predicted to form internal ribosome entry sites (IRES), and do these structures correlate with host type?
>
> *Rationale:* The candidate question investigates specific RNA secondary structures (IRES) in Astro-Poty virus UTRs and their host correlation. It aligns with GQ_002's focus on genome architecture but lacks the broader scope of segmentation and manual curation. It is well-grounded in the provided FASTA data, referencing specific virus types and hosts.

### ✅ `glm-5` — Comp=0.800 · Pass@1=0.00 · Pass@5=0.15

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 1 | 2 | 2 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 3 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 4 | 4 | 4 | 4 | 4 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What phylogenetic relationships exist among these novel viruses across different host taxa and geographic regions, and do specific virus families show evidence of host-specific adaptation or cross-species transmission?
>
> *Rationale:* The candidate question partially aligns with GQ_001 by focusing on phylogenetic analysis of novel assembled virus genomes from diverse hosts. However, it misses the specific framing of 'invertebrate transcriptomes' and the broader goal of 'redefining the breadth and deep lineages of the RNA virosphere'. It is a well-grounded scientific question.

**Rank 2** · Comp = 0.360 · ❌ fail

> Do virus isolates from different geographic regions (Beihai, Hubei, Wuhan, Changjiang, Zhee, Wenling) show distinct phylogenetic clustering patterns that suggest geographic structuring of virus populations?
>
> *Rationale:* The candidate question addresses phylogeographic structuring of virus populations, which is a different intent from the matched gold's focus on RNA virosphere breadth and deep lineages. It grounds well in data but covers few of the gold's specific required elements.

**Rank 3** · Comp = 0.544 · ❌ fail

> What evolutionary patterns characterize genome size variation across virus families, and do genome length differences correlate with host type or virus family classification?
>
> *Rationale:* The candidate question investigates evolutionary patterns and correlations of genome length, aligning with the gold's focus on genome features. It explicitly grounds in FASTA file headers for length data but misses the gold's specific emphasis on segmentation and manual curation, leading to a partial match in intent and coverage.

**Rank 4** · Comp = 0.800 · ✅ pass

> Are these viruses novel taxa distinct from known virus families, or do they represent divergent lineages within established virus families based on phylogenetic analysis?
>
> *Rationale:* The candidate question strongly aligns with GQ_001's intent to understand the novelty and taxonomic placement of discovered viruses through phylogenetic analysis, covering most required elements and grounding well in data, though it omits the explicit source context of "invertebrate transcriptomes".

**Rank 5** · Comp = 0.560 · ❌ fail

> Do specific virus families demonstrate restricted host ranges (specialists) versus broad host ranges (generalists) based on host association patterns across the dataset?
>
> *Rationale:* The candidate question explores host range patterns, a facet of viral diversity, aligning broadly with GQ_001's domain. However, it misses GQ_001's specific focus on redefining virosphere breadth and deep lineages. It is a well-grounded, specific question, but not a close match to the gold's specific intent or acceptable variants.

### ✅ `gemini-2.5-flash` — Comp=0.620 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.620 · ✅ pass

> What are the primary evolutionary drivers and phylogenetic relationships among the diverse viral lineages represented in this dataset?
>
> *Rationale:* The candidate partially aligns with GQ_001 by focusing on phylogenetic relationships and diverse viral lineages, but it lacks the specific context of 'invertebrate transcriptomes' and 'redefining the RNA virosphere breadth'. It covers some required elements and is well-grounded in data but is generic compared to acceptable variants.

**Rank 2** · Comp = 0.620 · ✅ pass

> How does the genetic diversity within specific viral families or genera correlate with their geographic distribution or host range?
>
> *Rationale:* The candidate question explores genetic diversity and its correlation with geographic/host distribution, aligning partially with GQ_001's evolutionary scope. However, it lacks the specific focus on invertebrate transcriptomes and redefining the RNA virosphere, making it a more general evolutionary question.

**Rank 3** · Comp = 0.560 · ❌ fail

> Are there specific genomic regions or genes that exhibit higher rates of evolutionary change or evidence of positive selection across these viral genomes?
>
> *Rationale:* The candidate question focuses on identifying genomic regions under positive selection, aligning with GQ_001's use of assembled viral genomes and phylogenetic analysis, but misses the broader scope of redefining virosphere breadth and deep lineages. It explicitly grounds in provided data files.

**Rank 4** · Comp = 0.480 · ❌ fail

> What is the prevalence and impact of recombination events on the evolution and diversification of these viral genomes?
>
> *Rationale:* The candidate question addresses viral evolution but misses the specific framing of GQ_001 regarding redefining RNA virosphere breadth and deep lineages from invertebrate transcriptomes. It covers some required elements and grounds well in data but doesn't align with the gold's specific acceptable variants.

**Rank 5** · Comp = 0.560 · ❌ fail

> Can novel viral species or clades be identified within this dataset based on phylogenetic clustering and sequence divergence thresholds?
>
> *Rationale:* The candidate proposes a methodology for identifying novel viral taxa using provided phylogenetic and sequence data. While it captures the analytical intent of exploring viral diversity, it omits the crucial context of invertebrate transcriptomes that defines the gold question's focus on the host-associated virosphere.

### ✅ `intern-s1` — Comp=0.700 · Pass@1=1.00 · Pass@5=0.40

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 4 | 3 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (U) |
| 5 | 3 | 4 | 3 | 4 | 3.400 | 0.680 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.700 · ✅ pass

> How does genetic diversity correlate with host specificity across different virus families?
>
> *Rationale:* The candidate question broadly aligns with GQ_001's focus on viral diversity and evolution, covering genetic diversity, deep lineages, and phylogenetic analysis. However, it misses the specific data source (invertebrate transcriptomes) and the "redefining" aspect of the gold question. It is well-grounded in the provided data features.

**Rank 2** · Comp = 0.480 · ❌ fail

> What evidence exists for recombination events shaping virus genome evolution?
>
> *Rationale:* The candidate question addresses recombination in viral evolution, which is related to the broader theme of GQ_001 but misses its specific focus on invertebrate transcriptomes and redefining RNA virosphere diversity. It covers some required elements and grounds well in the provided data files.

**Rank 3** · Comp = 0.500 · ❌ fail

> Which viral genes show evidence of positive selection pressure?
>
> *Rationale:* The candidate question is a valid scientific inquiry into viral evolution but diverges significantly from the matched gold's specific focus on invertebrate transcriptomes and redefining viral diversity/lineages. It grounds well in data but lacks coverage of the gold's core elements.

**Rank 4** · Comp = 0.300 · ❌ fail

> How does geographic distribution correlate with viral phylogenetic clustering?
>
> *Rationale:* The candidate question focuses on spatial autocorrelation and phylogeography, which is distinct from the gold question's focus on defining the breadth and deep lineages of the RNA virosphere through invertebrate-associated transcriptomes. While it utilizes the provided data, it fails to address the specific scientific scope defined by the gold questions.

**Rank 5** · Comp = 0.680 · ✅ pass

> What conserved genomic regions exist across different virus families?
>
> *Rationale:* The candidate question partially aligns with GQ_001 by focusing on viral genome analysis across families to understand relationships, covering most required elements except the specific host. It is well-grounded in the provided data but lacks the specific framing of the gold's acceptable variants.

### ✅ `intern-s1-pro` — Comp=0.560 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 1 | 2 | 3 | 4 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 1 | 3 | 0.765 | 0.153 | ❌ | GQ_001 (S) |
| 5 | 1 | 1 | 1 | 3 | 1.020 | 0.204 | ❌ | GQ_001 (S) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What is the phylogenetic relationship among the Astro-Poty virus genomes, and how does it correlate with host specificity?
>
> *Rationale:* The candidate asks a specific phylogenetic question about Astro-Poty viruses and host specificity. It aligns with the general theme of viral evolution in GQ_001 but misses the broader scope of 'RNA virosphere breadth' and the specific data source 'invertebrate transcriptomes' central to GQ_001. It is well-grounded in data.

**Rank 2** · Comp = 0.400 · ❌ fail

> Which genomic regions show the highest sequence conservation across Astro-Poty viruses, and what functional domains do they correspond to?
>
> *Rationale:* The candidate question is a well-formed comparative genomics question about sequence conservation and functional domains in Astro-Poty viruses. It poorly matches GQ_001, which focuses on broader RNA virosphere diversity and deep lineages from invertebrate transcriptomes. It covers few of GQ_001's specific required elements but grounds well in data.

**Rank 3** · Comp = 0.480 · ❌ fail

> Do Astro-Poty viruses exhibit evidence of positive selection in specific genes, and which codon sites are under selection?
>
> *Rationale:* The candidate question addresses viral evolution through positive selection, aligning broadly with the evolutionary aspect of GQ_001, but its scope is much narrower, focusing on specific genes and viruses rather than virosphere breadth or deep lineages. It grounds well in the provided data.

**Rank 4** · Comp = 0.153 · ❌ fail

> How do recombination events shape the genomic diversity of Astro-Poty viruses, and which regions are hotspots?
>
> *Rationale:* The candidate question focuses on recombination hotspots in specific viral taxa. It lacks alignment with the core intent of the provided gold questions, which center on broad-scale evolutionary discovery and viral genome curation from invertebrate transcriptomes. It is scientifically valid but unrelated to the established rubric topics.

**Rank 5** · Comp = 0.204 · ❌ fail

> What is the evolutionary rate (substitutions per site per year) of Astro-Poty viruses, and how does it vary across lineages?
>
> *Rationale:* The candidate addresses a specific evolutionary rate analysis (molecular clock) rather than the broad phylogenetic scope and diversity mapping represented by the gold questions.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.600 · Pass@1=0.00 · Pass@5=0.10

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 3 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (U) |
| 4 | 1 | 1 | 1 | 4 | 1.105 | 0.221 | ❌ | GQ_001 (S) |
| 5 | 3 | 3 | 3 | 3 | 3.000 | 0.600 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.580 · ❌ fail

> What phylogenetic relationships and evolutionary patterns can be inferred from the Astro-Poty virus genome sequences and their associated alignments, and how do these relationships reflect geographic and host-specific diversification?
>
> *Rationale:* The candidate question explores phylogenetic relationships and evolutionary patterns of Astro-Poty viruses, aligning with the general intent of GQ_001 for viral evolution. It is well-grounded in specific data features but misses the broader scope of RNA virosphere breadth and invertebrate transcriptomes central to GQ_001.

**Rank 2** · Comp = 0.500 · ❌ fail

> What are the nucleotide diversity and substitution rate metrics across the Astro-Poty virus genomes, and how do these vary between different viral lineages identified in the phylogeny?
>
> *Rationale:* The candidate question is about quantifying molecular evolution metrics within specific viral lineages, which differs from the gold's intent of redefining the RNA virosphere's breadth using transcriptomes. It covers some required elements and is well-grounded in data, but its intent and specific framing do not align closely with the matched gold's acceptable variants.

**Rank 3** · Comp = 0.480 · ❌ fail

> Do geographic patterns emerge in the phylogenetic tree of these viruses, suggesting localized evolutionary trajectories or dispersal patterns from source populations?
>
> *Rationale:* The candidate question explores phylogeographic patterns, which is a distinct scientific question from the matched gold's focus on broad RNA virosphere diversity from invertebrate transcriptomes. While it uses phylogenetic analysis and references data well, it misses core elements of the gold's intent and specific framing.

**Rank 4** · Comp = 0.221 · ❌ fail

> What evidence exists for recombination or horizontal gene transfer events among the Astro-Poty virus genomes based on incongruences between local gene trees and the overall phylogeny?
>
> *Rationale:* The candidate question investigates mechanisms of viral evolution (recombination) via phylogenetic incongruence, which is distinct from the gold question's goal of mapping the breadth and deep phylogeny of the invertebrate-associated RNA virosphere.

**Rank 5** · Comp = 0.600 · ✅ pass

> How do genomic features such as gene content, structural variations, and codon usage bias correlate with phylogenetic clustering among the virus isolates?
>
> *Rationale:* The candidate question aligns with GQ_001 by investigating the correlation between genomic features and phylogenetic clustering, contributing to understanding viral evolution. However, it lacks the specific context of invertebrate transcriptomes and the broader goal of redefining the RNA virosphere's breadth. It is well-grounded in data.


## 6 · `oyster_rna_virome_2024`

- **raw**：6 文件: `40168_2024_1967_MOESM1_ESM.xlsx, 40168_2024_1967_MOESM2_ESM.xlsx, 40168_2024_1967_MOESM3_ESM.xlsx, 40168_2024_1967_MOESM4_ESM.fa...`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.65

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 3 | 4 | 2 | 4 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 3 | 5 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> What fraction of the Magallana gigas RNA virome — and which Marnaviridae- and Picobirnaviridae-dominated lineages in particular — represent transient seawater-acquired viruses versus a temporally stable oyster-resident core, when contig TPM trajectories across the 16 longitudinal Luchao-Port batches are jointly modelled with co-located Yangshan-harbor seawater abundance and prevalence in M. hongkongensis libraries?
>
> *Rationale:* The candidate question perfectly captures the intent of identifying the oyster RNA virome and its sharing with seawater and other mollusks. It is highly specific, well-grounded in data, and covers all required elements by detailing the methodology to distinguish transient seawater-acquired viruses from a stable oyster-resident core using longitudinal TPM data.

**Rank 2** · Comp = 0.740 · ✅ pass

> Do the 68 oyster-derived Marnaviridae RdRp contigs co-vary in TPM with co-located Yangshan-harbor seawater abundances in a way consistent with diatom/protist-mediated trophic transfer rather than oyster-cell replication?
>
> *Rationale:* The candidate question is a specific, mechanistic inquiry into virus sharing between oysters and seawater, focusing on Marnaviridae and trophic transfer. It aligns with the 'sharing network' aspect of GQ_001 but is more detailed and specific, missing the broader 'diverse RNA virome' scope.

**Rank 3** · Comp = 0.595 · ❌ fail

> How many of the 146 RdRp contigs whose best RefSeq match is below 60% amino-acid identity (e.g. against Beihai mollusks virus 1/2 and Beihai picorna-like virus 14/15/35) represent novel virus species or higher-rank taxa within Picornavirales/Sobelivirales/Durnavirales, and where do they place in the order-level phylogenies provided?
>
> *Rationale:* The candidate question effectively addresses the identification and phylogenetic placement of novel RdRp viruses, aligning with GQ_002's focus on novel RdRP-bearing species. It is highly data-grounded but omits aspects of abundance and indicator value.

**Rank 4** · Comp = 0.374 · ❌ fail

> Across the 16 monthly Magallana gigas sampling batches at Luchao Port (June 2016 to July 2017), do oyster RNA-virus community composition and per-family TPM exhibit reproducible seasonal turnover, and do Marnaviridae and Picobirnaviridae follow opposite temperature-driven phenologies?
>
> *Rationale:* The candidate shifts the scientific focus from identifying novel RdRP-bearing indicator viruses (GQ_002) to characterizing seasonal community turnover of specific viral families. While highly grounded in the provided datasets and methodologically precise, it does not address the core intent of discovering indicator species for viral circulation.

**Rank 5** · Comp = 0.620 · ✅ pass

> Are the 40 'dominant' RNA-virus contigs (>90% genome coverage in at least one library) phylogenetically clustered within specific Picornavirales/Durnavirales sub-clades, indicating that genome-completeness signals true oyster infection rather than fragmentary environmental DNA?
>
> *Rationale:* The candidate partially aligns with GQ_001 by focusing on characterizing oyster RNA viruses, but misses the broader scope of virome diversity and sharing networks. It is a well-framed, specific question with excellent data grounding, but only covers a subset of the gold's required elements.

### ✅ `gpt-5.5-high` — Comp=0.940 · Pass@1=1.00 · Pass@5=0.60

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 2 | 3 | 1 | 3 | 5 | 2.210 | 0.442 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.940 · ✅ pass

> Are high-abundance oyster-associated RNA viruses, especially Marna and Picobirna contigs, broadly shared across oyster batches, other mollusk hosts, and Yangshan harbor seawater in a pattern consistent with environmental transmission or a multi-host reservoir?
>
> *Rationale:* The candidate question strongly aligns with GQ_001's focus on virus sharing between mollusks and seawater, providing specific virus types and data grounding. It covers most required elements, missing only the explicit mention of RdRP/palm-domain sequences.

**Rank 2** · Comp = 0.442 · ❌ fail

> Do the oyster prevalence and coverage matrices identify a core RNA virome made up of recurrent high-coverage contigs across the 17 oyster libraries?
>
> *Rationale:* The candidate partially matches GQ_002 by focusing on the abundance and prevalence of a 'core RNA virome' within oysters. It covers the 'abundance' element but misses other key aspects like novelty, RdRP specificity, and indicator value for marine circulation. Data grounding is excellent, referencing specific files, columns, and numerical evidence.

**Rank 3** · Comp = 0.646 · ✅ pass

> Which proposed RNA virus taxa are most responsible for dominant greater-than-90-percent coverage detections in oysters, other mollusks, and seawater?
>
> *Rationale:* The candidate question effectively targets the identification of dominant RNA virus taxa and their distribution across marine hosts and seawater, aligning well with GQ_002's focus on abundance and circulation. It provides strong data grounding but could be improved by explicitly mentioning novelty or RdRP-bearing viruses.

**Rank 4** · Comp = 0.493 · ❌ fail

> Do RdRp similarity hits and taxon-specific phylogenetic FASTA alignments place the oyster RNA virus contigs within known regional mollusk virus lineages such as Beihai and Wenzhou viruses?
>
> *Rationale:* The candidate investigates the phylogenetic relationship between identified oyster virus contigs and known regional virus lineages (Beihai/Wenzhou). While grounded in the provided data, it prioritizes taxonomic characterization over the goal of using viral abundance as a marine circulation indicator.

**Rank 5** · Comp = 0.820 · ✅ pass

> Is the Yangshan harbor seawater RNA virome best explained as a subset of oyster and mollusk-associated contigs or as a distinct assemblage with separate high-TPM viruses?
>
> *Rationale:* The candidate question effectively probes the nature of virus sharing between seawater and mollusks, aligning well with GQ_001's focus on a virus-sharing network. It demonstrates strong data grounding with specific references and covers most required elements, though it omits explicit mention of RdRP sequences.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 5 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Do the RNA viruses shared between Magallana gigas and Magallana hongkongensis represent a taxonomically non-random, phylogenetically conserved core virome shaped by host genetic relatedness rather than geographic proximity or seawater-mediated environmental transmission?
>
> *Rationale:* The candidate question precisely investigates the nature of RNA virus sharing between specific oyster species, contrasting host genetic relatedness with environmental transmission. It fully aligns with the gold's intent of exploring a virome and sharing network, covering all required elements and demonstrating exceptional data grounding with specific file and column references.

**Rank 2** · Comp = 0.850 · ✅ pass

> Are Marnaviridae the dominant RNA virus family in the Pacific oyster Magallana gigas virome in terms of both genomic diversity and transcriptional abundance, and does their high TPM expression correlate with broader cross-host detection range across co-sampled mollusk species?
>
> *Rationale:* The candidate question precisely asks if Marnaviridae, due to their dominance in diversity and abundance, serve as indicators of marine RNA-virus circulation through cross-host detection. This directly aligns with the gold question's intent to identify novel, abundant viruses as indicators. All required elements are covered with strong data grounding.

**Rank 3** · Comp = 0.820 · ✅ pass

> Do the RNA viruses detected in the Yangshan deep-water harbor seawater virome at high TPM represent genuine aquatic reservoir populations of oyster-associated RNA viruses, distinguishable from passive shedding by their genome coverage distribution and taxonomic composition?
>
> *Rationale:* The candidate question closely aligns with GQ_001's intent of understanding virus sharing between oysters and seawater, specifically probing if seawater viruses are reservoirs or shedding. It provides strong data grounding with specific files, columns, and numerical examples, but omits explicit mention of RdRP sequences.

**Rank 4** · Comp = 0.544 · ❌ fail

> Do Picobirnavirus sequences in the Magallana gigas metatranscriptome exhibit the highest per-contig transcriptional abundance among all RNA virus families, and does this reflect a distinct ecological role as opportunistic or persistent infectors of oyster intestinal epithelium?
>
> *Rationale:* The candidate question aligns with GQ_002's focus on abundance and ecological role, though it's more specific to Picobirnavirus and less on broad marine circulation indicators or novelty. It is well-grounded in specific data features and avoids unacceptable generic phrasing.

**Rank 5** · Comp = 0.500 · ❌ fail

> Does the seasonal sampling of Magallana gigas at Luchao Port over 16 monthly batches spanning June 2016 to July 2017 reveal temporal variation in the RNA virome composition that correlates with host population size or environmental season?
>
> *Rationale:* The candidate question focuses on temporal variation and environmental correlations of the oyster RNA virome, which differs significantly from GQ_001's intent of revealing a diverse virome and a virus-sharing network. While specific and well-grounded in data, it covers only two of GQ_001's five required elements.

### ✅ `gemini-3.1-pro` — Comp=0.200 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 3 | 1 | 0 | 1 | 3 | 0.765 | 0.153 | ❌ | GQ_002 (S) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.060 · ❌ fail

> What are the predicted functional roles of the diverse protein sequences identified in the assembled contigs, and how do these functions contribute to the metabolic capabilities or ecological dynamics of the sampled biological system?
>
> *Rationale:* The candidate question is a general functional annotation query, completely unrelated to the specific viral virome and sharing network focus of the gold questions. Consequently, it scores zero on match strength, required elements, and acceptability, despite having concrete data grounding for its own unrelated scope.

**Rank 2** · Comp = 0.060 · ❌ fail

> How does the distribution of protein sequence lengths in the assembled contigs reflect the completeness and quality of the underlying genomic or metagenomic assembly?
>
> *Rationale:* The candidate question focuses on assembly quality metrics, which is entirely different from the biological questions posed by the gold standards regarding oyster viromes and virus circulation.

**Rank 3** · Comp = 0.153 · ❌ fail

> Are there specific protein families or domains that are significantly overrepresented in this dataset, and what does this suggest about the selective pressures or environmental adaptations of the sampled organisms?
>
> *Rationale:* The candidate asks about generic protein domain enrichment and evolutionary pressures. It is fundamentally different from the gold questions, which specifically target RdRP-bearing viral diversity, abundance, and their role as indicators in marine circulation networks.

**Rank 4** · Comp = 0.060 · ❌ fail

> Can the protein sequences in the FASTA file be used to reconstruct the phylogenetic diversity of the sampled community, and how does this diversity compare to known microbial ecosystems?
>
> *Rationale:* The candidate question is about general microbial phylogenetic diversity, which is entirely unrelated to the specific oyster virome and virus-sharing network focus of the gold questions. Consequently, it scores very low on match strength, required elements, and acceptability, despite good data grounding.

**Rank 5** · Comp = 0.200 · ❌ fail

> What is the relationship between the protein sequences identified in the FASTA file and the quantitative data likely contained in the accompanying Excel spreadsheets?
>
> *Rationale:* The candidate question focuses on the technical integration of provided files rather than the specific scientific inquiry defined in the gold set. While it demonstrates strong data grounding by referencing specific files, it misses the biological scope of the gold questions entirely.

### ✅ `deepseek-v4-pro` — Comp=0.340 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 5 | 1 | 2 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What is the phylogenetic diversity and taxonomic novelty of bacteriophage genomes recovered from the human gut metagenome represented by the k141 contig collection, and how do their encoded protein domain architectures relate to known crAss-like and other gut phage lineages?
>
> *Rationale:* The candidate question is about bacteriophages in the human gut, which is completely unrelated to the provided gold questions concerning oyster RNA viruses in marine environments. Therefore, no gold question could be matched.

**Rank 2** · Comp = 0.080 · ❌ fail

> Can the protein domain architectures encoded by the k141 bacteriophage contigs be used to predict host bacterial ranges, and do specific domain combinations correlate with particular gut bacterial phyla?
>
> *Rationale:* The candidate question about bacteriophage host prediction is entirely unrelated to the gold question concerning oyster RNA viromes and virus sharing, leading to very low scores across most dimensions. However, it demonstrates strong data grounding by referencing specific files and their potential content.

**Rank 3** · Comp = 0.080 · ❌ fail

> Do the replication-associated proteins (ATPases, helicases, DNA polymerases) across the k141 phage contigs exhibit signatures of purifying selection consistent with long-term co-evolution with their gut bacterial hosts?
>
> *Rationale:* The candidate question focuses on phage evolution and purifying selection of replication proteins, which is unrelated to the provided gold questions about oyster RNA viromes and marine virus sharing networks.

**Rank 4** · Comp = 0.060 · ❌ fail

> What proportion of the k141 bacteriophage contigs encode auxiliary metabolic genes or bacteria-derived domains that may modulate gut bacterial metabolism, and are these enriched in specific phage lineages?
>
> *Rationale:* The candidate question is entirely unrelated to any of the provided gold questions, focusing on bacteriophage AMGs and gut metabolism rather than oyster RNA viromes. Consequently, all match-related scores are zero, though it does ground to a specific data file.

**Rank 5** · Comp = 0.340 · ❌ fail

> Does the relative abundance of different phage protein families in the k141 dataset correlate with sample-associated metadata variables, and can phage protein profiles serve as biomarkers for gut ecosystem states?
>
> *Rationale:* The candidate question is about phage biomarkers in gut ecosystems, which is a poor match for the gold question's focus on oyster RNA viruses. While it covers 'abundance' and 'indicators', the core subject matter is different. It is a well-grounded question for the provided data.

### ✅ `glm-5` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What functional gene categories are most abundant across the assembled metagenomic contigs, and do these abundance patterns suggest specific ecological adaptations or metabolic capabilities?
>
> *Rationale:* The candidate question is about general metagenomic functional gene abundance and ecological adaptations, completely unrelated to the gold question's focus on oyster RNA viromes and virus sharing networks. Data grounding is strong for the candidate's own intent, but irrelevant to the gold.

**Rank 2** · Comp = 0.080 · ❌ fail

> How does protein sequence length distribution vary across different contigs, and does this variation correlate with functional gene categories or assembly quality metrics?
>
> *Rationale:* The candidate question is a generic bioinformatics query about sequence length and assembly quality, completely unrelated to the specific virology and marine biology focus of the gold question. It lacks any mention of viruses, oysters, or sharing networks, resulting in a very low match.

**Rank 3** · Comp = 0.080 · ❌ fail

> Are there distinct clusters of protein sequences based on sequence similarity, and do these clusters correspond to specific functional protein families or taxonomic origins?
>
> *Rationale:* The candidate question is a generic bioinformatics query about protein sequence clustering and annotation, completely unrelated to the specific marine virome and host-sharing network focus of the gold questions. It lacks any specific biological context of the gold questions.

**Rank 4** · Comp = 0.080 · ❌ fail

> What proportion of assembled protein sequences contain transmembrane domains or membrane-associated motifs, and how does this compare to expected distributions for different environmental or organismal sources?
>
> *Rationale:* The candidate question is completely unrelated to the matched gold question, focusing on general protein features rather than oyster viromes. Consequently, it covers none of the required elements and does not align with any acceptable or unacceptable variants. Data grounding is strong for its own topic.

**Rank 5** · Comp = 0.080 · ❌ fail

> Can the assembled protein sequences be mapped to known metabolic pathways, and which pathways show the highest representation suggesting dominant metabolic processes in the sampled environment?
>
> *Rationale:* The candidate question focuses on metabolic pathways and protein sequences, which is completely unrelated to the gold question's topic of oyster RNA viromes and virus sharing. Consequently, all match-related scores are zero, though data grounding is strong.

### ✅ `gemini-2.5-flash` — Comp=0.306 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 2 | 2 | 4 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 2 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.306 · ❌ fail

> What novel genes or functional elements are encoded within the provided contig sequences, and how do their expression levels or associated quantitative metrics, as detailed in the supplementary spreadsheets, vary across different experimental conditions or sample types?
>
> *Rationale:* The candidate question is generic, focusing on novel genes/elements and their expression from contigs. It lacks the specific biological context (oysters, viruses, marine environment) of the gold question, resulting in a low match strength and coverage of required elements, despite good data grounding.

**Rank 2** · Comp = 0.220 · ❌ fail

> What is the taxonomic origin and predicted functional annotation of the contig sequences present in `40168_2024_1967_MOESM4_ESM.fa`?
>
> *Rationale:* The candidate question is a generic request for sequence characterization of contigs from a file. It does not align with the specific intent of GQ_001, which focuses on revealing a diverse RNA virome and virus-sharing network from oyster metatranscriptomes, missing all required elements.

**Rank 3** · Comp = 0.080 · ❌ fail

> Are there statistically significant differences or correlations in the quantitative measurements provided in the Excel spreadsheets across different experimental groups or time points?
>
> *Rationale:* The candidate question is a generic statistical query about quantitative data in Excel files, completely unrelated to the specific marine virology context of the gold questions. It grounds well in the data features but fails on all other rubric dimensions due to lack of thematic alignment.

**Rank 4** · Comp = 0.080 · ❌ fail

> Does the visual evidence presented in `40168_2024_1967_MOESM6_ESM.jpg` provide qualitative support or illustrate key findings derived from the quantitative and sequence data?
>
> *Rationale:* The candidate question is entirely unrelated to the scientific intent of any gold question, focusing instead on the interpretation of visual data. It covers none of the gold's required elements but does ground itself well in the provided data files.

**Rank 5** · Comp = 0.080 · ❌ fail

> Can the combined multi-omics data, including genetic sequences and quantitative measurements, reveal novel biological pathways or regulatory networks active under specific experimental conditions?
>
> *Rationale:* The candidate question is a generic multi-omics inquiry, completely unrelated to the specific marine oyster virome topic of the gold questions. It lacks any domain-specific elements from the gold questions.

### ✅ `intern-s1` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | unknown (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |

**Rank 1** · Comp = 0.080 · ❌ fail

> How do genetic variations in contig sequences (MOESM4) correlate with phenotypic traits in MOESM1?
>
> *Rationale:* The candidate question addresses general genotype-phenotype correlation, which is unrelated to the gold question's specific focus on oyster RNA viromes and virus-sharing networks. While data grounding is strong, the scientific intent is completely different.

**Rank 2** · Comp = 0.080 · ❌ fail

> What is the relationship between environmental variables in MOESM2 and gene expression levels in MOESM3?
>
> *Rationale:* The candidate question is unrelated to the specific virome and virus-sharing topics of the gold questions, resulting in low scores for match strength, required elements, and acceptability. However, it demonstrates strong data grounding by explicitly referencing two specific data files.

**Rank 3** · Comp = 0.080 · ❌ fail

> Do temporal trends in MOESM1 data align with seasonal patterns in MOESM2?
>
> *Rationale:* The candidate question is entirely unrelated to the scientific domain of the gold questions, focusing instead on generic temporal and seasonal data alignment between two specified files. Consequently, it covers none of the gold's specific scientific elements or framing.

**Rank 4** · Comp = 0.120 · ❌ fail

> Can phylogenetic relationships inferred from MOESM4 sequences explain functional diversity in MOESM3?
>
> *Rationale:* The candidate question is completely unrelated to the gold question's topic of oyster viromes and virus sharing. It fails to cover any required elements, but it does ground itself well in specific data files.

**Rank 5** · Comp = 0.080 · ❌ fail

> Are there significant differences in data distributions between MOESM1 and MOESM2?
>
> *Rationale:* The candidate question is a generic data quality check, asking about statistical differences between two files. It is completely unrelated to the specific scientific questions about marine viromes, oysters, or virus sharing networks posed by the gold questions.

### ✅ `intern-s1-pro` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | unknown (U) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What protein domains and functional annotations can be identified in the predicted proteome, and how do they relate to known protein families and metabolic pathways?
>
> *Rationale:* The candidate question is unrelated to the provided gold questions, focusing on general protein domain identification and functional annotation rather than marine viromes. It demonstrates strong data grounding by referencing specific FASTA and Excel files.

**Rank 2** · Comp = 0.120 · ❌ fail

> What evolutionary relationships and phylogenetic patterns can be inferred from the comparative analysis of protein sequences across different contigs in the dataset?
>
> *Rationale:* The candidate question is a general bioinformatics query about phylogenetics from protein sequences, completely unrelated to the specific marine virology focus of the gold questions. It lacks any mention of oysters, viruses, or marine environments, resulting in a very low match.

**Rank 3** · Comp = 0.080 · ❌ fail

> Can metabolic pathways be reconstructed from the annotated protein functions, and what key metabolic capabilities do these pathways reveal about the organism(s) in the dataset?
>
> *Rationale:* The candidate question is about metabolic pathways and protein functions, which is completely unrelated to the provided gold questions concerning oyster viromes and marine virus circulation.

**Rank 4** · Comp = 0.080 · ❌ fail

> Are there patterns of gene co-expression or regulatory elements that can be identified from the sequence data and supplementary tables, suggesting coordinated gene regulation?
>
> *Rationale:* The candidate question about gene co-expression and regulation is completely unrelated to the gold question's focus on oyster viromes and virus sharing. Consequently, it covers none of the required elements and does not align with any acceptable or unacceptable variants, despite good data grounding.

**Rank 5** · Comp = 0.060 · ❌ fail

> What structural features and functional properties can be predicted for the encoded proteins, and how do these predictions correlate with their annotated functions?
>
> *Rationale:* The candidate question addresses generic bioinformatics protein structure prediction and functional annotation. It fails to match the scientific intent of the provided gold questions, which are specifically focused on marine RNA virome discovery and virus-sharing networks in oyster hosts.

### ✅ `intern-s1-mini` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 2 | 0.200 | 0.040 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.000 · ❌ fail

> How do particulate matter (PM2.5) levels correlate with respiratory hospital admissions across different age groups in the dataset?
>
> *Rationale:* The candidate question is entirely unrelated to the provided gold questions, which focus on oyster viromes and marine virus circulation. It addresses a completely different scientific domain (environmental health).

**Rank 2** · Comp = 0.080 · ❌ fail

> What genetic markers in the FASTA file are associated with higher diabetes prevalence in the Excel dataset?
>
> *Rationale:* The candidate question is completely unrelated to the gold questions, focusing on human genetics and diabetes rather than marine viromes. It scores 0 for match-related dimensions but high for data grounding due to specific file references.

**Rank 3** · Comp = 0.060 · ❌ fail

> Does smoking status significantly influence lung cancer risk in individuals aged 50-70 based on the Excel dataset?
>
> *Rationale:* The candidate question on human lung cancer and smoking is completely unrelated to the provided gold questions about oyster viromes. Consequently, it scores zero on most dimensions, except for data grounding, where it references specific features in an Excel file.

**Rank 4** · Comp = 0.040 · ❌ fail

> Are there temporal trends in PM2.5 levels over time in the Excel dataset?
>
> *Rationale:* The candidate question is entirely unrelated to the marine virology topics of the gold questions, scoring zero for match strength, required elements, and acceptability. It generically references 'the Excel dataset' for data grounding.

**Rank 5** · Comp = 0.080 · ❌ fail

> How does geographical location correlate with asthma prevalence in the dataset?
>
> *Rationale:* The candidate question about asthma prevalence is completely unrelated to the marine virome topic of the gold questions, resulting in zero scores for match strength, coverage, and acceptability. However, it does make a concrete attempt to ground itself in specific data files.

### ✅ `intern-s2-preview` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | null (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |

**Rank 1** · Comp = 0.080 · ❌ fail

> Given the multiple ABC transporter nucleotide-binding domains identified in the contig sequences, what is the phylogenetic relationship and functional divergence among these transporter proteins in this organism?
>
> *Rationale:* The candidate question is about ABC transporters and phylogenetic analysis, which is completely unrelated to the marine virome topics of the gold questions. Therefore, it does not match any gold question, resulting in low scores for match strength, required elements, and acceptability. However, it is well-grounded in specific data features.

**Rank 2** · Comp = 0.060 · ❌ fail

> What proportion of the assembled protein sequences contain predicted transmembrane domains, and what does this reveal about the membrane proteome composition of this organism?
>
> *Rationale:* The candidate question focuses on protein transmembrane domains, which is entirely unrelated to the viral diversity and sharing networks covered by the provided gold questions. Thus, it does not match any gold question.

**Rank 3** · Comp = 0.060 · ❌ fail

> Among the kinase domains identified in the contigs, what conserved catalytic residues are present and do they suggest specific kinase subfamily classifications?
>
> *Rationale:* The candidate question is about kinase domains and classification, which is unrelated to the provided gold questions concerning oyster viromes. Therefore, it scores low on match strength and coverage, but it does ground itself in a specific data file.

**Rank 4** · Comp = 0.060 · ❌ fail

> What is the prevalence and diversity of zinc finger motifs across the protein sequences, and what types of zinc finger domains (C2H2, C4, etc.) are most common in this assembly?
>
> *Rationale:* The candidate question is about zinc finger motifs, which is completely unrelated to the provided gold questions about oyster viromes and marine virus circulation. Therefore, it does not match any gold question.

**Rank 5** · Comp = 0.060 · ❌ fail

> How do the sequence lengths of ABC transporter proteins compare to other protein families in this assembly, and what might this indicate about domain architecture complexity?
>
> *Rationale:* The candidate question is about protein sequence analysis, specifically ABC transporter length and domain architecture, which does not align with the virome-focused gold questions. It provides good data grounding but is otherwise unrelated.


## 7 · `rvmt_cell_2022`

- **raw**：1 文件: `RVMT_Zenodo_V4.zip.remote.json`
- **gold**：2 个 (GQ_001, GQ_002)

### ❌ `claude-code-opus-4-7` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`

### ✅ `gpt-5.5-high` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 4 | 4.900 | 0.980 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 4 | 4.165 | 0.833 | ✅ | GQ_002 (S) |
| 3 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 4 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 5 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.980 · ✅ pass

> How does RdRP-based mining of 5,150 diverse metatranscriptomes expand the known global RNA virome and reveal novel RNA bacteriophage lineages and host associations?
>
> *Rationale:* The candidate question perfectly matches the gold's intent, covering all required elements with strong data grounding by specifying the number of metatranscriptomes. It is highly acceptable, aligning closely with the provided acceptable variants.

**Rank 2** · Comp = 0.833 · ✅ pass

> Do CRISPR spacer matches and bacteriolytic protein annotations in RVMT support prokaryotic hosts for picobirnaviruses and partitiviruses previously associated with eukaryotes?
>
> *Rationale:* The candidate question perfectly aligns with GQ_002, focusing on host association using CRISPR and gene content for specific RNA viruses. It is highly specific, well-grounded in data, and covers all required elements.

**Rank 3** · Comp = 1.000 · ✅ pass

> Does the expanded Lenarviricota signal in RVMT represent a major bacterial-linked fraction of the RNA virome across diverse metatranscriptomes?
>
> *Rationale:* The candidate question is an excellent, specific instantiation of the gold question, directly addressing the expansion of RNA virome diversity and the identification of RNA bacteriophage clades using metatranscriptomic data, with strong data grounding.

**Rank 4** · Comp = 0.646 · ✅ pass

> Which novel protein domains in RVMT RNA virus contigs are associated with inferred virus-host interactions across newly expanded RNA virus lineages?
>
> *Rationale:* The candidate question aligns with GQ_002 by focusing on host association using protein domains (a gene-content feature) for new RNA virus lineages. It is specific and well-grounded in data, though it omits CRISPR and explicit prokaryotic host mention.

**Rank 5** · Comp = 0.860 · ✅ pass

> Does the extended RVMT RdRp phylogeny support the monophyly of the five established RNA virus phyla while justifying additional bacteriophage phyla, classes, and orders?
>
> *Rationale:* The candidate question closely matches the intent of GQ_001 by focusing on phylogenetic evidence for the expansion of RNA virus diversity and the discovery of new bacteriophage taxa. It covers most required elements and is well-grounded in data, aligning with an acceptable variant.

### ✅ `claude-code-sonnet-4-6` — Comp=0.500 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 2 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 5 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 4 | 1 | 3 | 3 | 5 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.500 · ❌ fail

> Do RNA viruses discovered in under-sampled environmental metagenomes (soil, freshwater, invertebrate-associated biomes) display RdRp phylogenetic signatures associated with broad host-range transmission, and does biome-of-origin predict cross-host spillover risk better than viral taxonomy alone?
>
> *Rationale:* The candidate question is a well-grounded scientific inquiry about RNA virus spillover risk and host range using RdRp phylogenetics and biome-of-origin. However, its core intent differs significantly from the matched gold question, which focuses on discovery and expansion of RNA bacteriophage diversity.

**Rank 2** · Comp = 0.480 · ❌ fail

> Across the RNA virus families catalogued in RVMT V4, is there a statistically significant correlation between the degree of metagenomic sampling effort (number of assembled contigs per biome) and the estimated rate of novel genus-level clade discovery, and which biomes remain in the steepest discovery phase?
>
> *Rationale:* The candidate asks about the correlation between sampling effort and novel genus-level clade discovery rate in RVMT V4, and which biomes are in the steepest discovery phase. It touches on RNA virus diversity expansion but misses the specific mining methods and targets of the gold question.

**Rank 3** · Comp = 0.360 · ❌ fail

> Do endogenous RNA virus elements and retrotransposons in RVMT V4 share RdRp palm-domain structural signatures with their exogenous counterparts, and can phylogenetic placement of mobile elements identify the most recent exogenous-to-endogenous integration events across invertebrate host lineages?
>
> *Rationale:* The candidate question is a well-formed scientific inquiry but fundamentally differs from GQ_001, focusing on endogenous elements and integration events rather than global metatranscriptome mining for novel RNA virus diversity and bacteriophages. Data grounding is excellent, but the match strength and element coverage are low.

**Rank 4** · Comp = 0.480 · ❌ fail

> Do RNA viruses classified within the same ICTV-recognized family but recovered from phylogenetically distant host organisms in RVMT V4 show higher RdRp substitution rates than viruses infecting closely related hosts, consistent with a host-switching mechanism driving elevated evolutionary rate?
>
> *Rationale:* The candidate question focuses on evolutionary rates and host-switching in RNA viruses, a different intent than GQ_001's focus on diversity expansion and discovery. While some elements like RdRp and host association are present, their purpose differs. The question is well-grounded in data but doesn't match the gold's specific scope.

**Rank 5** · Comp = 0.500 · ❌ fail

> Does the RVMT V4 reference database, when used as a classification backbone for short-read metagenomic datasets from clinical respiratory surveillance samples, achieve higher sensitivity and lower false-positive rates for novel RNA virus detection compared to classification against NCBI RefSeq viral sequences alone?
>
> *Rationale:* The candidate evaluates RVMT V4 database performance for novel RNA virus detection, partially aligning with the gold's theme of RNA virus diversity expansion. It diverges in method (classification vs. mining) and specific focus (database utility vs. phage discovery), missing several key gold elements.

### ✅ `gemini-3.1-pro` — Comp=0.660 · Pass@1=1.00 · Pass@5=0.55

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 4 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 2 | 4 | 2 | 4 | 3 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 3 | 1 | 1 | 2 | 3 | 1.190 | 0.238 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |
| 5 | 3 | 2 | 4 | 3 | 2.465 | 0.493 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.620 · ✅ pass

> How does the phylogenetic diversity of RNA-dependent RNA polymerase (RdRp) sequences within the RVMT dataset correlate with the ecological biomes of their source samples, and can this reveal biome-specific evolutionary constraints on RNA viruses?
>
> *Rationale:* The candidate question aligns with GQ_001 by focusing on RNA virus diversity using RdRp from a large dataset. However, it diverges by investigating ecological biomes and evolutionary constraints, rather than the expansion of the virome and bacteriophage discovery.

**Rank 2** · Comp = 0.660 · ✅ pass

> Are there distinct, previously uncharacterized deep-branching clades of RNA viruses in the RVMT dataset that lack known eukaryotic or prokaryotic host associations?
>
> *Rationale:* The candidate question effectively seeks to discover new RNA virus diversity and their host associations within a specific dataset, aligning with the gold's intent to expand the RNA virome. It covers key elements like diversity and host evidence but omits specific methodologies and the focus on bacteriophages.

**Rank 3** · Comp = 0.238 · ❌ fail

> What is the frequency of putative cross-phylum host jumping events inferred from the phylogenetic incongruence between RNA viruses and their assigned hosts in the RVMT dataset?
>
> *Rationale:* The candidate question is about host jumping frequency via phylogenetic incongruence, which is distinct from the matched gold's focus on validating prokaryotic hosts using CRISPR/gene content. It covers few required elements and is not close to any of the gold's variants, despite being a well-formed question itself.

**Rank 4** · Comp = 0.340 · ❌ fail

> Does the geographic distribution of specific RNA virus families in the RVMT dataset exhibit latitudinal gradients similar to those seen in cellular organisms?
>
> *Rationale:* The candidate question explores ecological patterns of RNA virus distribution, which is distinct from the gold's focus on discovering new RNA virus diversity and bacteriophage clades. It broadly touches on RNA viruses but misses the core intent and most required elements of the gold question.

**Rank 5** · Comp = 0.493 · ❌ fail

> Can the sequence composition (e.g., GC content, dinucleotide frequency) of RNA viral contigs in the RVMT dataset predict their likely host domain (Bacteria, Archaea, or Eukarya)?
>
> *Rationale:* The candidate question aligns with the intent of host association for RNA viruses, using sequence composition as evidence. It covers some key elements like gene content and host prediction, but misses the specificity of CRISPR and RNA phage clades from the gold question.

### ✅ `deepseek-v4-pro` — Comp=0.540 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (U) |
| 2 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 3 | 2 | 3 | 3 | 4 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 3 | 5 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 3 | 4 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.320 · ❌ fail

> Across the global meta-transcriptomic samples in RVMT V4, does the phylogenetic breadth of RNA virus host ranges expand predictably with host body mass and geographic range size among mammalian orders?
>
> *Rationale:* The candidate question is about mammalian RNA virus host range breadth and its correlation with host traits, which is fundamentally different from the matched gold's focus on RNA bacteriophage discovery and diversity expansion. While well-grounded in data, its scientific intent does not align with the gold question.

**Rank 2** · Comp = 0.300 · ❌ fail

> Do RNA viruses sampled from chiropteran hosts in RVMT V4 exhibit significantly higher rates of amino acid change in the receptor-binding domain of their spike glycoproteins compared to those from rodent hosts?
>
> *Rationale:* The candidate question's intent to analyze evolutionary rates in specific mammalian hosts is fundamentally different from GQ_001's focus on discovering global RNA-virus diversity expansion and RNA bacteriophage clades, despite sharing the broad topic of RNA viruses and metatranscriptomes.

**Rank 3** · Comp = 0.540 · ❌ fail

> Is the global phylogenetic structure of the RNA virus family Chuviridae in RVMT V4 significantly partitioned by arthropod versus vertebrate host class, indicating host-associated lineage diversification?
>
> *Rationale:* The candidate question focuses on the phylogenetic structure and host-associated diversification of the Chuviridae family, which is a different intent from GQ_001's focus on RNA-virus diversity expansion and bacteriophage discovery, leading to low match strength and partial required element coverage. It is a well-formed question but does not align with the gold's specific variants.

**Rank 4** · Comp = 0.300 · ❌ fail

> Within individual host specimens in RVMT V4 that harbour multiple RNA viruses, do co-infecting viral genomes exhibit more similar dinucleotide composition and codon usage bias than expected under random assembly from the global viral pool?
>
> *Rationale:* The candidate question is a distinct, well-grounded scientific inquiry into within-host viral genomic convergence, which does not align with the discovery-focused intent of GQ_001. It is well-grounded in data but lacks coverage of the matched gold's specific elements.

**Rank 5** · Comp = 0.280 · ❌ fail

> Does the per-sample rate of novel RNA virus OTU discovery in RVMT V4 significantly decline with cumulative sampling effort within a host family, consistent with virome saturation in well-studied mammalian clades?
>
> *Rationale:* The candidate question, while well-formed and data-grounded, addresses RNA virus discovery saturation in mammalian hosts, which is largely unrelated to GQ_001's intent of global RNA-virus expansion and bacteriophage discovery via metatranscriptomes. It covers none of the gold's required elements.

### ✅ `glm-5` — Comp=0.060 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.060 · ❌ fail

> How accurately can vehicle trajectory prediction models generalize across different traffic density conditions using the RVMT motion tracking dataset?
>
> *Rationale:* The candidate question is about vehicle trajectory prediction, which is completely unrelated to the provided gold questions about RNA virome and bacteriophages. It does, however, ground well in the provided RVMT dataset.

**Rank 2** · Comp = 0.060 · ❌ fail

> What are the characteristic motion patterns that distinguish different vehicle types in the RVMT tracking dataset?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, which are focused on microbiology and bioinformatics. It does, however, ground itself in a specific dataset.

**Rank 3** · Comp = 0.060 · ❌ fail

> How does multi-object tracking accuracy degrade with increasing numbers of simultaneous vehicles in the RVMT dataset?
>
> *Rationale:* The candidate question is about multi-object tracking, which is completely unrelated to the biological focus of the provided gold questions on RNA viruses and bacteriophages. Therefore, no match could be made.

**Rank 4** · Comp = 0.060 · ❌ fail

> What temporal patterns in vehicle motion can be extracted for anomaly detection in traffic flow using the RVMT dataset?
>
> *Rationale:* The candidate question is completely unrelated to the provided gold questions, which focus on RNA virology. It discusses vehicle motion and anomaly detection, a topic entirely outside the scope of the gold questions.

**Rank 5** · Comp = 0.060 · ❌ fail

> How reproducible are vehicle tracking benchmarks across different subsets of the RVMT dataset?
>
> *Rationale:* The candidate question is completely unrelated to the topic of RNA viruses and bacteriophages covered by the gold questions, focusing instead on vehicle tracking benchmarks and dataset reproducibility. It grounds well in the specified RVMT dataset.

### ✅ `gemini-2.5-flash` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | None (U) |
| 4 | 0 | 1 | 0 | 3 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.060 · ❌ fail

> What are the specific scientific domains and research questions addressed by the `RVMT_Zenodo_V4.zip` dataset, and how has its scope evolved across previous versions?
>
> *Rationale:* The candidate question focuses on dataset metadata and evolution, not a scientific hypothesis. It is unrelated to the gold questions, which are about specific scientific discoveries using data.

**Rank 2** · Comp = 0.060 · ❌ fail

> How does the data structure and content of `RVMT_Zenodo_V4.zip` compare to its preceding versions (V1, V2, V3) in terms of data types, resolution, and coverage?
>
> *Rationale:* The candidate question focuses on comparing dataset versions and their technical characteristics, which is entirely unrelated to the scientific hypotheses about RNA virus diversity or host associations presented in the gold questions.

**Rank 3** · Comp = 0.060 · ❌ fail

> What are the primary applications and potential impact of the `RVMT_Zenodo_V4.zip` dataset within its scientific field, as evidenced by citations and usage patterns on Zenodo?
>
> *Rationale:* The candidate question focuses on the meta-level assessment of a dataset's impact and usage, rather than specific scientific hypotheses or discoveries related to RNA viruses or bacteriophages, making it unrelated to the provided gold questions.

**Rank 4** · Comp = 0.120 · ❌ fail

> What are the computational challenges and resource requirements for processing and analyzing the 9.3 GB `RVMT_Zenodo_V4.zip` dataset effectively?
>
> *Rationale:* The candidate question is about computational challenges for data processing, not a biological discovery question. It is unrelated to the scientific intent of any gold question, covering only one implied required element and not aligning with any variants.

**Rank 5** · Comp = 0.060 · ❌ fail

> What metadata standards and FAIR principles (Findable, Accessible, Interoperable, Reusable) are applied to the `RVMT_Zenodo_V4.zip` dataset, and how do they facilitate its long-term usability and discoverability?
>
> *Rationale:* The candidate question focuses on data management and FAIR principles, which is unrelated to the scientific discovery intent of the gold questions. It explicitly grounds in a specific dataset but does not align with the scientific scope of the rubric.

### ✅ `intern-s1` — Comp=0.060 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | null (U) |
| 5 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.000 · ❌ fail

> How do environmental humidity levels correlate with mechanical failure rates in heavy vehicles?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, which focus on RNA virology. It also references data features not present in the specified data file.

**Rank 2** · Comp = 0.000 · ❌ fail

> Does temperature variation accelerate maintenance needs in different vehicle components?
>
> *Rationale:* The candidate question is completely unrelated to the provided gold questions, which focus on RNA virome and bacteriophage research. It discusses vehicle maintenance and temperature, a topic entirely outside the scope of the gold questions.

**Rank 3** · Comp = 0.060 · ❌ fail

> Are there seasonal patterns in vehicle system failures detectable through sensor data anomalies?
>
> *Rationale:* The candidate question is entirely unrelated to the gold questions, focusing on vehicle failures and seasonality rather than virology. Consequently, it scores zero on most dimensions, though it does reference specific data features.

**Rank 4** · Comp = 0.000 · ❌ fail

> Can maintenance intervals be optimized using machine learning models trained on sensor telemetry?
>
> *Rationale:* The candidate question is completely unrelated to the scientific domain of the provided gold questions, which focus on RNA virome and bacteriophage discovery. No match could be made, and data grounding is absent for the provided file.

**Rank 5** · Comp = 0.000 · ❌ fail

> Do regional climate differences significantly affect vehicle performance metrics?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, focusing on vehicle performance and climate rather than RNA virome expansion. It lacks any relevant required elements or data grounding for the gold questions.

### ✅ `intern-s1-pro` — Comp=0.080 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | null (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | unknown (U) |
| 5 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> How does motor tracking accuracy in the RVMT task correlate with cognitive load across different age groups, and can this relationship predict early signs of neurodegenerative conditions?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, focusing on neurodegeneration and motor tracking rather than RNA viruses or bacteriophages. Consequently, it covers none of the gold's required elements or variants, but it does demonstrate strong data grounding for its own topic.

**Rank 2** · Comp = 0.060 · ❌ fail

> What are the gender-specific differences in reaction time variability during rapid visual motor tracking tasks, and how do these differences relate to attentional control mechanisms?
>
> *Rationale:* The candidate question is completely unrelated to any of the provided gold questions, resulting in low scores for match strength, coverage, and acceptability. However, it does reference a specific data file.

**Rank 3** · Comp = 0.060 · ❌ fail

> Can machine learning models trained on RVMT time-series data accurately classify participants into different cognitive performance tiers based solely on motor tracking patterns?
>
> *Rationale:* The candidate question is completely unrelated to the gold questions, focusing on machine learning for cognitive assessment rather than RNA virology. Consequently, it covers none of the gold's required elements or variants, though it does ground in specific data features.

**Rank 4** · Comp = 0.080 · ❌ fail

> How does the learning curve of motor tracking performance evolve over repeated trials in the RVMT task, and what factors predict individual differences in learning rate?
>
> *Rationale:* The candidate question is completely unrelated to the scientific domain covered by the provided gold questions, focusing instead on motor learning and individual differences. It does, however, reference a specific data file.

**Rank 5** · Comp = 0.060 · ❌ fail

> What is the relationship between visual field position and tracking accuracy in the RVMT task, and does this relationship differ between central and peripheral vision conditions?
>
> *Rationale:* The candidate question is about visual perception and tracking accuracy, a cognitive science topic, which is entirely unrelated to the molecular biology and virology focus of any provided gold questions. Therefore, it scores 0 across all match-related dimensions.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.240 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 0 | 4 | 0.800 | 0.160 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> How do mutation rates in the RVMT dataset vary across different viral lineages and geographic regions over time?
>
> *Rationale:* The candidate question focuses on viral evolutionary dynamics (mutation rates, lineages, geography, time) within an existing dataset, which is fundamentally different from the discovery and characterization of novel RNA viruses/phages from metatranscriptomes, as defined by GQ_001.

**Rank 2** · Comp = 0.160 · ❌ fail

> What is the temporal correlation between the emergence of new variants and reported case surges in the RVMT surveillance data?
>
> *Rationale:* The candidate question is about epidemiological tracking of viral variants and case surges, which is fundamentally different from the discovery of novel RNA virus diversity and bacteriophages from metatranscriptomes, as intended by GQ_001. No required elements are covered, and it doesn't align with any variants.

**Rank 3** · Comp = 0.060 · ❌ fail

> Which specific amino acid substitutions in the RVMT dataset show the strongest association with immune escape signatures across different populations?
>
> *Rationale:* The candidate question focuses on immune escape and amino acid substitutions, which is entirely unrelated to the provided gold questions about RNA virus diversity, bacteriophages, and host associations. It grounds well in the data but does not align with the rubric's gold questions.

**Rank 4** · Comp = 0.080 · ❌ fail

> How does the geographic spread of variants in the RVMT dataset correlate with travel patterns and border control measures?
>
> *Rationale:* The candidate question is completely unrelated to any gold question, focusing on epidemiological spread rather than RNA virus discovery or host association. It scores 0 across most dimensions due to this mismatch, but shows strong data grounding.

**Rank 5** · Comp = 0.240 · ❌ fail

> What is the relative contribution of within-host versus between-host evolution to the observed genetic diversity in the RVMT dataset?
>
> *Rationale:* The candidate question addresses evolutionary dynamics (within-host vs. between-host evolution) of genetic diversity, which is a different scientific intent from `GQ_001`'s focus on discovering new RNA virus diversity and bacteriophage clades. It lacks coverage of `GQ_001`'s specific required elements but is well-grounded in the provided data.


## 8 · `tara_oceans_science_2022`

- **raw**：7 文件: `44779_RdRP_contigs.fna.gz, 5504_wcANI_based_clusters_90_80.fna.gz, RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz, RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent.fasta.gz...`
- **gold**：2 个 (GQ_001, GQ_002)

### ❌ `claude-code-opus-4-7` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `gpt-5.5-high` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=0.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 4 | 1 | 2 | 3 | 5 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 5 | 1 | 2 | 2 | 5 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.500 · ❌ fail

> Do RNA viral communities in the global ocean exhibit significant depth-stratified compositional turnover across the surface, deep chlorophyll maximum, and mesopelagic zones, as resolved by whole-contig ANI-based vOTU clustering of 44,779 RdRP-positive metatranscriptomic contigs from 121 Tara Oceans stations?
>
> *Rationale:* The candidate question's intent on depth-stratified community turnover is distinct from GQ_001's focus on discovering deeply divergent evolutionary lineages. While it shares some elements like global ocean metatranscriptomes and RdRP, it misses core aspects of the gold's intent. It is a well-grounded and specific question, but not a strong match for this gold.

**Rank 2** · Comp = 0.940 · ✅ pass

> What fraction of the 5,504 Tara Oceans RNA viral OTUs (vOTUs) represent phylogenetically novel lineages with no detectable homology to characterized viruses in GenBank or Wolf et al. 2020, and do these cryptic vOTUs show distinct ocean-basin or depth-layer distributions compared to known lineages?
>
> *Rationale:* The candidate question effectively seeks to discover and characterize novel, cryptic RNA-virus lineages from Tara Oceans data, aligning well with the gold's intent to reveal deeply divergent marine RNA viruses. It is highly specific and well-grounded in available data.

**Rank 3** · Comp = 1.000 · ✅ pass

> Do the five novel RNA virus megataxa (Arctiviricota, Paraxenoviricota, Pomiviricota, Taraviricota, Wamoviricota) identified in the Tara Oceans dataset collectively account for a disproportionate share of the near-complete RdRP footprint diversity relative to their coverage in existing phylogenetic databases, as measured by their representation among the 6,238 near-complete 50%-identity centroids?
>
> *Rationale:* The candidate question is an excellent, highly specific inquiry into the evolutionary impact of novel marine RNA virus megataxa identified in the Tara Oceans dataset, directly addressing the discovery of deeply divergent lineages and their role in shaping the RNA virome's early structure.

**Rank 4** · Comp = 0.420 · ❌ fail

> Is the functional gene complement (capsid proteins, helicases, proteases, and RdRP) of the 5,504 RNA vOTUs in the Tara Oceans dataset predictive of host range (eukaryotic versus prokaryotic hosts), and does host-range prediction correlate with the prokaryotic-fraction versus eukaryotic-fraction metatranscriptome of origin encoded in contig sample IDs?
>
> *Rationale:* The candidate question's intent of host range prediction and validation is distinct from the gold's focus on evolutionary lineage discovery. It covers some elements like RdRP and ocean metatranscriptomes but misses the core evolutionary framing. Data grounding is excellent, referencing multiple specific files and features.

**Rank 5** · Comp = 0.380 · ❌ fail

> Does the contig length distribution of the 44,779 RdRP-positive Tara Oceans metatranscriptomic contigs (median 599 bp, P90 2,715 bp) correlate with the number of distinct functional domains annotated per contig, and are longer near-complete genome contigs enriched in polar (Arctic Tara Polar Circle) versus tropical ocean samples?
>
> *Rationale:* The candidate question is well-formed and highly data-grounded but fundamentally misaligned with GQ_001's intent of discovering deeply divergent RNA-virus lineages and their evolutionary structure. It focuses instead on contig characteristics (length, functional domains) and their distribution across polar vs. tropical ocean samples.

### ❌ `gemini-3.1-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 15 column 4 (char 1302)`

### ❌ `deepseek-v4-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `glm-5` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ✅ `gemini-2.5-flash` — Comp=0.646 · Pass@1=0.00 · Pass@5=0.25

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 3 | 3 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.460 · ❌ fail

> What are the most prevalent predicted functions of proteins encoded by novel viral operational taxonomic units (vOTUs) identified in the Tara Oceans metatranscriptomes?
>
> *Rationale:* The candidate question broadly concerns novel viral entities from ocean metatranscriptomes but diverges significantly from the gold's specific focus on RNA-virus evolution via RdRP. It covers some general elements but misses core framing and specific markers.

**Rank 2** · Comp = 0.646 · ✅ pass

> How do the RdRP protein sequences identified in the Tara Oceans expeditions cluster phylogenetically with known viral lineages from GenBank and Wolf et al. (2020)?
>
> *Rationale:* The candidate question closely matches the intent of GQ_002 by asking about the phylogenetic clustering of marine RdRP sequences with known viral lineages. It grounds well in the provided data but omits explicit mention of the "phylum or class level" and "taxonomy revision" aspects of the gold question.

**Rank 3** · Comp = 0.480 · ❌ fail

> What is the genomic context and average length of contigs containing RdRP sequences from the Tara Oceans expeditions?
>
> *Rationale:* The candidate question describes properties of RdRP contigs from Tara Oceans, which is a preliminary step, but it does not directly address the discovery of deeply divergent lineages or evolutionary structure as intended by GQ_001. It covers two of five required elements and is well-grounded in the specified data file.

**Rank 4** · Comp = 0.560 · ❌ fail

> Are there significant differences in the diversity or functional profiles of RdRP-containing viral communities between arctic and non-arctic Tara Oceans samples, or between prokaryotic and eukaryotic size fractions?
>
> *Rationale:* The candidate asks about environmental influences on RdRP viral community diversity and function in Tara Oceans. It broadly aligns with studying marine RNA virome but misses the gold's focus on discovering deeply divergent lineages and evolutionary structure. It grounds well in data features.

**Rank 5** · Comp = 0.300 · ❌ fail

> What is the level of sequence redundancy within the full RdRP footprint dataset, and how effectively do the 50% identity centroids represent the overall diversity?
>
> *Rationale:* The candidate question is about data redundancy and representation by centroids, a data processing concern. It does not align with the biological discovery or evolutionary intent of the gold question, despite mentioning 'RdRP' and 'diversity'.

### ❌ `intern-s1` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 15 column 4 (char 1386)`

### ❌ `intern-s1-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 15 column 4 (char 1454)`

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ❌ `intern-s2-preview` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`


## 9 · `tick_metavirome_2023`

- **raw**：1 文件: `nuccore_reported_viral_sequences.fasta`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=0.850 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 5 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Which uncharacterised TIGMIC tick-derived viral MAGs cluster phylogenetically and co-occur in the same isolate pools with known human-pathogenic tick-borne agents (SFTSV, Yezo virus, Songling virus, Brown dog tick phlebovirus 1) across China, and therefore should be prioritised as candidate emerging zoonotic pathogens?
>
> *Rationale:* The question effectively seeks to prioritize uncharacterized tick-derived viral MAGs as zoonotic pathogens by analyzing their phylogenetic clustering and co-occurrence with known human pathogens across China. It aligns well with understanding how viral lineages vary by geography and host-range category, leveraging specific data features for strong grounding.

**Rank 2** · Comp = 0.646 · ✅ pass

> Across the 19 Chinese localities sampled by TIGMIC (Hulunbuir, Zhangzhou, Tonghua, Tianjin, Lianyungang, Nanning, Luoyang, Kashgar, etc.), is the geographic structure of Botou tick virus 1 and Dabieshan tick virus genomes consistent with a single panmictic tick-borne population or with strong phylogeographic substructure that would predict locality-specific emergence risk?
>
> *Rationale:* The candidate question effectively addresses the geographic variation of tick-virus lineages, a key aspect of the matched gold question. It demonstrates strong data grounding by citing specific viruses and localities, though it omits other dimensions of variation like tick species and host range.

**Rank 3** · Comp = 0.820 · ✅ pass

> What fraction of the 1,801 reported tick viral MAGs in the TIGMIC dataset is attributable to fungal/protist mycoviruses (Toti-, Botourmia-, Narna-, Mito-, Partitiviridae) rather than to true tick or vertebrate-infecting RNA viruses, and how does this reshape our estimate of the genuine arboviral diversity carried by hard ticks?
>
> *Rationale:* The candidate question focuses on refining the understanding of the tick virome's composition by correctly attributing viral MAGs to their true hosts (fungal/protist vs. tick/vertebrate), which is a critical aspect of defining the RNA-virus genome compendium and reservoir structure. It is well-grounded in data and highly specific.

**Rank 4** · Comp = 0.520 · ❌ fail

> Within the segmented tick-borne RNA viruses in the TIGMIC collection (Orthomyxoviridae, Reoviridae, Phenuiviridae, Nairoviridae, Peribunyaviridae), do the distributions of complete-genome segment lengths reveal previously undescribed segment numbers or reassortant segment combinations indicative of cryptic novel segmented viruses?
>
> *Rationale:* The candidate partially aligns with GQ_001's goal of RNA-virus genome discovery but focuses on segmented virus architecture rather than host range. It covers few required elements but is a well-formed, data-grounded question, distinct from the provided acceptable variants.

**Rank 5** · Comp = 0.440 · ❌ fail

> Among the more than 1,200 complete viral genomes in the TIGMIC dataset, are there RdRp ORFs whose nucleotide and amino-acid identity to any known reference falls below 50%, defining candidate new genera or families of tick-associated RNA viruses worthy of formal ICTV taxonomic proposals?
>
> *Rationale:* The candidate asks about discovering novel RNA virus taxa from complete genomes, which differs from the gold's focus on metatranscriptomic discovery of reservoirs. It covers few required elements but is a highly specific, data-grounded question.

### ✅ `gpt-5.5-high` — Comp=0.714 · Pass@1=0.00 · Pass@5=0.40

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 2 | 4 | 1 | 4 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 4 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 4 | 5 | 3 | 4 | 5 | 3.570 | 0.714 | ✅ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 5 | 1.600 | 0.320 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.340 · ❌ fail

> Do dominant tick-associated viral lineages in `nuccore_reported_viral_sequences.fasta` exhibit distinct genome-length and GC-content signatures that can be used to classify and prioritize TIGMIC MAGs for surveillance?
>
> *Rationale:* The candidate question asks about genomic signatures of viral lineages for classification, which differs from the matched gold's focus on ecological/epidemiological variation. It grounds well in data by referencing specific file and features, but misses most of the gold's required elements and does not align with its acceptable variants.

**Rank 2** · Comp = 0.640 · ✅ pass

> Which viral families or named tick-virus lineages dominate the TIGMIC MAG catalog, and how is that dominance distributed between complete genomes, cRNA sequences, and RdRp or PB1 marker records?
>
> *Rationale:* The question characterizes the composition of a viral genome catalog, aligning with the 'large genome compendium' aspect of GQ_001. It explicitly references viral lineages and sequence types (complete genomes, markers) from the data, but misses elements related to tick species, host range, and metatranscriptomes.

**Rank 3** · Comp = 0.289 · ❌ fail

> Are repeated virus titles across TIGMIC isolate IDs consistent with widespread lineages or with heterogeneous sequence assemblies, based on within-title variation in length and GC content?
>
> *Rationale:* The candidate question investigates data quality and interpretation of viral sequences, which is a poor match for GQ_002's focus on ecological variation of lineages. It covers only one required element but is well-grounded in specific data features.

**Rank 4** · Comp = 0.714 · ✅ pass

> Do geographically named tick-virus records in the FASTA headers show locality-specific differences in viral lineage diversity and genome features?
>
> *Rationale:* The candidate question strongly matches GQ_002 by focusing on geographic variation of tick-virus lineages and genome features. It is well-grounded in specific data features but misses explicit mention of tick species and host-range categories from the gold's required elements.

**Rank 5** · Comp = 0.320 · ❌ fail

> How do MAG UNVERIFIED records differ from regular MAG records in sequence length, GC content, sequence descriptors, and represented viral titles?
>
> *Rationale:* The candidate question assesses data quality of viral MAG records, comparing 'UNVERIFIED' vs. 'regular' records. This intent fundamentally differs from GQ_001, which aims for biological discovery of RNA viruses and their host reservoirs in ticks, leading to a very low match.

### ✅ `claude-code-sonnet-4-6` — Comp=0.850 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 4 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Does the co-occurrence frequency of known-zoonotic virus families (Nairoviridae, Flaviviridae, and Phenuiviridae) within individual TIGMIC tick pool metagenomes vary significantly with geographic sampling location across China, and do tick pools co-harbouring all three families cluster in specific ecological zones that could predict future arboviral spillover risk?
>
> *Rationale:* The candidate question strongly aligns with GQ_002 by investigating how zoonotic virus family co-occurrence varies geographically and clusters ecologically, directly addressing variation by region and host-range. All required elements are covered, and the question is highly specific, mirroring acceptable variants. Data grounding is excellent, citing specific virus families, pool IDs, and geographic features.

**Rank 2** · Comp = 0.850 · ✅ pass

> What is the phylogeographic structure of the 41 novel Nairoviridae sequences discovered in TIGMIC Chinese tick metagenomes, and do their L-segment (RNA-dependent RNA polymerase) sequences cluster with known pathogenic nairoviruses such as Crimean-Congo hemorrhagic fever virus based on pairwise nucleotide identity analysis of the complete genomes in this dataset?
>
> *Rationale:* The candidate question perfectly aligns with GQ_002's intent to understand how viral lineages vary by geography and host range, providing specific details on phylogeographic structure and clustering with pathogenic viruses. All required elements are covered, and it demonstrates excellent data grounding.

**Rank 3** · Comp = 0.740 · ✅ pass

> Among the 1,801 metagenome-assembled viral genomes in the TIGMIC dataset, what fraction of Totiviridae, Narnaviridae, and Mitoviridae sequences are derived from fungal endosymbionts rather than tick-replicating viruses, and does the relative abundance of mycoviruses in a tick pool predict co-infection with zoonotic Phenuiviridae or Nairoviridae sequences?
>
> *Rationale:* The question partially matches GQ_001 by exploring host range (fungal vs. tick-replicating viruses) and reservoir structure (co-infection with zoonotic viruses) within tick viromes. It covers most required elements, implicitly referencing metatranscriptomes and explicitly RNA genomes, host range, and reservoir structure, but lacks broad tick sampling. It is well-grounded in specific data features and aligns with acceptable scientific framing.

**Rank 4** · Comp = 0.680 · ✅ pass

> Do the 216 location-prefixed novel tick viruses (e.g., Nanning Botou tick virus 1, Hulunbuir Chrys tick virus 1) representing newly described species in TIGMIC metagenomes show evidence of geographic endemism, or are closely related variants of the same novel virus lineage recovered from multiple geographically distant Chinese cities?
>
> *Rationale:* The candidate question effectively asks about the geographic distribution and endemism of novel tick viruses, directly addressing the 'geography' aspect of GQ_002. It is well-grounded in specific data features and is highly acceptable, though it doesn't cover all stratification factors like tick species or host range.

**Rank 5** · Comp = 0.697 · ✅ pass

> Do the 87 Dabieshan Tick Virus complete-genome sequences and 51 Lihan tick virus complete-genome sequences from TIGMIC tick metagenomes show signatures of positive selection or recombination in their RNA-dependent RNA polymerase genes that would indicate rapid adaptive evolution during spread across Chinese tick populations?
>
> *Rationale:* The candidate investigates evolutionary mechanisms (selection, recombination) in specific tick viruses (Dabieshan, Lihan) to understand their adaptive evolution and spread across Chinese tick populations. This aligns well with GQ_002's focus on how tick-virus lineages vary by geography and host-range, providing a mechanistic perspective.

### ✅ `gemini-3.1-pro` — Comp=0.595 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 4 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 4 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 3 | 2 | 0 | 3 | 4 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.595 · ❌ fail

> How does the genetic diversity and phylogenetic relationship of Botou tick virus 1 isolates correlate with their geographic distribution across China?
>
> *Rationale:* The candidate question effectively asks about the phylogeography of a specific tick virus, aligning with the gold's intent to understand how viral lineages vary by geography, though it omits broader tick species and host-range considerations. It is well-grounded in the provided FASTA data.

**Rank 2** · Comp = 0.289 · ❌ fail

> What are the patterns of codon usage bias among the different viral families (e.g., Narnaviridae, Rhabdoviridae, Flaviviridae) represented in the tick virome?
>
> *Rationale:* The candidate asks about codon usage bias patterns in viral families, a specific molecular question. It broadly relates to variation within the tick virome but differs significantly from the gold's focus on lineage variation by external factors. Data grounding is good, but coverage of gold's required elements is low.

**Rank 3** · Comp = 0.306 · ❌ fail

> Is there evidence of homologous recombination within the genomes of the widely distributed tick-borne viruses, such as the Narna tick viruses?
>
> *Rationale:* The candidate question focuses on homologous recombination in specific viral genomes, which differs significantly from GQ_002's intent of understanding lineage variation by external factors. It lacks coverage of GQ_002's required elements but is well-grounded in data.

**Rank 4** · Comp = 0.280 · ❌ fail

> Do the genomic sequences of tick-borne Flaviviridae isolates exhibit conserved RNA secondary structures in their untranslated regions (UTRs) compared to known mosquito-borne flaviviruses?
>
> *Rationale:* The candidate question is highly specific about RNA secondary structures in Flaviviridae UTRs, which is a structural genomics question. This intent is fundamentally different from GQ_001's focus on broad RNA-virus reservoir discovery and genome compendium from metatranscriptomes, resulting in a very low match.

**Rank 5** · Comp = 0.340 · ❌ fail

> What is the extent of nucleotide sequence divergence between the genomic RNA and cRNA sequences of the segmented tick-borne viruses, such as the Nairo tick viruses?
>
> *Rationale:* The candidate question focuses on molecular divergence within specific viral genomes, distinct from the gold's intent of broad virus discovery and reservoir characterization from metatranscriptomes. It covers one required element tangentially and is well-grounded in data, but its intent is largely unrelated to the matched gold question.

### ✅ `deepseek-v4-pro` — Comp=0.714 · Pass@1=1.00 · Pass@5=0.90

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 2 | 4 | 4 | 5 | 4 | 3.570 | 0.714 | ✅ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 3 | 3.060 | 0.612 | ✅ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 5 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> Do genetically distinct Botou tick virus lineages exhibit phylogeographic clustering by geographic origin across the sampled Chinese cities, consistent with local tick-population structure rather than long-distance dispersal?
>
> *Rationale:* The candidate question aligns well with understanding how tick-virus lineages vary by geography, focusing on phylogeographic clustering of Botou tick virus. It is well-grounded in data and scientifically framed, though it doesn't cover all comparative aspects of the gold question like host-range categories or variation across multiple tick species.

**Rank 2** · Comp = 0.714 · ✅ pass

> Are there statistically significant co-occurrence patterns among distinct tick virus taxa sampled from the same Chinese city, suggesting shared ecological reservoirs or tick-host species?
>
> *Rationale:* The candidate question aligns well with GQ_002 by investigating how tick-virus relationships (co-occurrence) vary by geography and host range. It covers most required elements and is highly acceptable, with strong data grounding in FASTA headers.

**Rank 3** · Comp = 0.612 · ✅ pass

> Does the ratio of DNA to RNA viral genome types recovered across sampling locations correlate with tick species composition or climatic variables in China?
>
> *Rationale:* The candidate question aligns well with understanding how tick virome characteristics vary by host and environment, specifically focusing on the DNA:RNA virus ratio. It grounds this in specific data features but misses elements related to host-range and phylogenetic lineages.

**Rank 4** · Comp = 0.629 · ✅ pass

> Do Botou tick virus variants 1 through 8 represent distinct species-level lineages with consistent pairwise nucleotide divergence thresholds across all sampled locations?
>
> *Rationale:* The candidate question effectively explores the geographic consistency and species-level distinction of specific viral lineages, aligning with the gold's focus on lineage variation by geography. It is well-grounded in data features but omits broader tick species and host-range considerations.

**Rank 5** · Comp = 0.561 · ❌ fail

> Is there evidence of inter-variant recombination among Botou tick virus genomes co-infecting the same geographic location, as detected by discordant phylogenetic signals across different genomic regions?
>
> *Rationale:* The candidate question partially aligns with GQ_002 by focusing on viral variation within a geographic context. It is a well-framed, specific scientific question about recombination, but its narrow scope on a single virus and mechanism means it doesn't fully capture the broader comparative intent of the gold question.

### ✅ `glm-5` — Comp=0.646 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 3 | 1 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 5 | 4 | 2 | 4 | 4 | 2.890 | 0.578 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.646 · ✅ pass

> What are the phylogenetic relationships and geographic distribution patterns of tick-associated viruses across China, and do specific virus types exhibit geographic clustering that suggests localized transmission dynamics?
>
> *Rationale:* The question strongly matches GQ_002 by focusing on phylogenetic relationships and geographic distribution of tick viruses. It covers three of five required elements, notably missing tick species and host-range. Data grounding is excellent, referencing specific virus types and locations in the FASTA file. It aligns well with acceptable variants.

**Rank 2** · Comp = 0.420 · ❌ fail

> Do different tick virus types (Botou, Chuvi, Dicis, Flavi, Fusar, Iflav, Mymon, Nairo) exhibit distinct genomic sequence signatures or conserved motifs that can serve as molecular markers for virus family identification?
>
> *Rationale:* The candidate question aims to identify genomic markers for known tick virus types, which differs from GQ_001's focus on RNA-virus discovery and reservoir structure. It covers few required elements but is well-grounded in specific data features.

**Rank 3** · Comp = 0.527 · ❌ fail

> What is the variation in genomic sequence length across different tick virus types, and does sequence length correlate with virus family classification or geographic origin?
>
> *Rationale:* The candidate question aligns with investigating variation in tick-virus characteristics by geography and viral classification. It is well-grounded in data but focuses on a specific genomic feature (sequence length) and omits explicit mention of tick species and host-range categories, limiting its overall scope compared to the gold.

**Rank 4** · Comp = 0.440 · ❌ fail

> Are there novel or previously uncharacterized tick virus sequences in this dataset that represent new viral species distinct from known tick-associated viruses?
>
> *Rationale:* The candidate focuses on discovering novel tick virus sequences, aligning with part of GQ_001's intent. However, it lacks specificity regarding the 'how' (metatranscriptomes, broad sampling) and 'what' (RNA-virus genomes, reservoir structure) of the gold question, and uses generic data referencing.

**Rank 5** · Comp = 0.578 · ❌ fail

> Do isolates of the same virus type from different geographic locations show genetic divergence patterns consistent with local adaptation or geographic isolation?
>
> *Rationale:* The candidate question investigates genetic divergence patterns of virus isolates across geographic locations, aligning with the geographic variation aspect of GQ_002. It provides concrete data grounding with specific virus types and locations, but omits other stratification factors like tick species and host-range.

### ✅ `gemini-2.5-flash` — Comp=0.646 · Pass@1=1.00 · Pass@5=0.70

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.646 · ✅ pass

> What are the phylogenetic relationships and evolutionary divergence among different geographic isolates and types (e.g., Botou tick virus 1 vs. Botou tick virus 2) of Botou tick virus based on their genomic sequences?
>
> *Rationale:* The candidate question aligns well with GQ_002 by focusing on viral phylogenetic relationships and their variation by geography and viral types. It explicitly grounds itself in the provided `nuccore_reported_viral_sequences.fasta` file, though some required elements like 'tick species' and 'host-range category' are not explicitly covered.

**Rank 2** · Comp = 0.629 · ✅ pass

> How much genetic diversity exists within and between different types (Botou tick virus 1, 2, 3, 4, 5) of Botou tick virus, and how does this diversity vary across geographic locations?
>
> *Rationale:* The candidate question effectively captures the intent of understanding viral variation across geography and within viral types, aligning well with GQ_002. It grounds well in the provided data but could be more explicit about tick species or host-range categories.

**Rank 3** · Comp = 0.459 · ❌ fail

> Are there specific genomic regions or genes that are highly conserved or highly variable across all Botou tick virus isolates, and do these regions correlate with viral type or geographic origin?
>
> *Rationale:* The candidate question partially aligns with understanding viral variation by geography and lineage, but is narrower in scope, focusing on genomic regions of a single virus rather than broader lineage variation across tick species and host ranges. It grounds well in the provided data.

**Rank 4** · Comp = 0.629 · ✅ pass

> What is the geographic distribution of each Botou tick virus type (1, 2, 3, 4, 5), and can the genomic data provide insights into potential transmission routes or spread patterns between locations?
>
> *Rationale:* The question effectively addresses the geographic distribution and spread of specific viral types, aligning with the gold's focus on how viral lineages vary by geography. It grounds well in the provided data but omits tick species and host-range categories.

**Rank 5** · Comp = 0.476 · ❌ fail

> Is there any discernible pattern or correlation between the accession numbers and the viral type or geographic origin of the Botou tick virus isolates?
>
> *Rationale:* The candidate partially aligns with GQ_002 by asking about geographic and viral type patterns, but its narrow focus on a single virus and accession numbers limits its match strength and required element coverage. It grounds well in the specified FASTA file.

### ✅ `intern-s1` — Comp=0.408 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 2 | 3 | 5 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 3 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | unknown (U) |
| 4 | 3 | 1 | 3 | 3 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 3 | 1.190 | 0.238 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.357 · ❌ fail

> What is the nucleotide composition bias (e.g., GC content) across the viral sequences, and does it correlate with taxonomic classifications?
>
> *Rationale:* The candidate question focuses on nucleotide composition bias and its correlation with viral taxonomy, which is a bioinformatics analysis. This differs significantly from the matched gold's intent of understanding tick-virus lineage variation across ecological factors like tick species, geography, and host range.

**Rank 2** · Comp = 0.408 · ❌ fail

> Can phylogenetic relationships among the viruses be inferred from their genomic sequences?
>
> *Rationale:* The candidate question partially aligns with GQ_002 by focusing on viral phylogeny but lacks the specific context of variation across tick species, geography, and host range. It covers only one required element and is a generic but acceptable scientific question, grounded in the provided viral sequence data.

**Rank 3** · Comp = 0.060 · ❌ fail

> Do the viral sequences exhibit evidence of recombination or horizontal gene transfer?
>
> *Rationale:* The candidate question on viral sequence recombination and HGT is unrelated to the gold questions, which focus on tick-virus discovery, host range, and ecological distribution. It does, however, ground itself in a specific data file.

**Rank 4** · Comp = 0.408 · ❌ fail

> Are there conserved functional motifs or domains within the viral sequences that suggest shared ancestry or functional constraints?
>
> *Rationale:* The candidate question partially aligns with GQ_002 by addressing 'shared ancestry' related to 'phylogenetic lineage'. However, it lacks the crucial context of variation by tick species, geography, and host-range. It's a generic sequence analysis question, not closely matching specific acceptable variants, but well-grounded in the provided viral sequence data.

**Rank 5** · Comp = 0.238 · ❌ fail

> Is there a correlation between viral genome size and the host range or pathogenicity of the viruses?
>
> *Rationale:* The candidate question asks about the correlation between viral genome size and host range/pathogenicity. It broadly touches on host range, aligning minimally with GQ_002, but misses the gold's specific focus on tick-virus lineage variation by tick species and geography. It grounds "genome size" in the provided FASTA file.

### ✅ `intern-s1-pro` — Comp=0.646 · Pass@1=1.00 · Pass@5=0.40

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 4 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 4 | 2 | 3 | 3 | 4 | 2.700 | 0.540 | ❌ | GQ_002 (U) |
| 5 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.646 · ✅ pass

> Do Botou tick virus sequences cluster phylogenetically by geographic origin (e.g., Nanning vs. Zhangzhou vs. Hulunbuir), suggesting limited viral gene flow between regions?
>
> *Rationale:* The question effectively asks about geographic variation of a specific tick-virus lineage using phylogenetic clustering, directly addressing a core aspect of GQ_002. It is well-grounded in specific data features but omits other stratification factors like tick species or host range.

**Rank 2** · Comp = 0.400 · ❌ fail

> Which genomic regions of Botou tick virus exhibit the highest sequence conservation across all isolates, potentially indicating essential functional domains or structural constraints?
>
> *Rationale:* The candidate question focuses on molecular conservation within a single virus, which is a poor match for GQ_001's intent of broad RNA-virus discovery and reservoir characterization across many tick species. It covers few required elements but demonstrates excellent data grounding.

**Rank 3** · Comp = 0.289 · ❌ fail

> What is the nucleotide substitution rate and pattern across Botou tick virus genomes, and are there signatures of positive selection in specific viral genes?
>
> *Rationale:* The candidate question on molecular evolution of a specific virus poorly matches the gold's intent of understanding lineage variation across ecological factors. It covers few required elements and is not close to acceptable variants, though it is a well-formed question with good data grounding.

**Rank 4** · Comp = 0.540 · ❌ fail

> Are there detectable recombination events between different Botou tick virus isolates, indicating genetic exchange in nature?
>
> *Rationale:* The candidate question about viral recombination is a specific evolutionary inquiry. It weakly matches `GQ_002`'s theme of lineage variation, covering some elements like geography and phylogeny, but misses the broader scope of the gold question.

**Rank 5** · Comp = 0.629 · ✅ pass

> Do different Botou tick virus types (1, 2, 3, 4, 5) show distinct evolutionary trajectories or genetic distances from each other?
>
> *Rationale:* The candidate question effectively asks about the evolutionary relationships and genetic variation among specific viral types, aligning with the gold's intent of understanding how tick-virus lineages vary, though it omits broader stratification factors. It is well-grounded in data features.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.646 · Pass@1=1.00 · Pass@5=0.30

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 3 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 4 | 1 | 1 | 3 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |
| 5 | 4 | 2 | 4 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.646 · ✅ pass

> What is the phylogenetic relationship and geographic clustering pattern among Botou tick virus isolates, and do sequences from the same geographic location form monophyletic clades suggesting localized viral evolution?
>
> *Rationale:* The candidate question strongly matches GQ_002 by investigating geographic patterns in viral lineages. It is well-grounded in data, though it is more specific than the gold question and omits some broader required elements like host-range category and explicit variation by tick species.

**Rank 2** · Comp = 0.420 · ❌ fail

> Are there evidence of recombination events between different Botou tick virus types, as suggested by the presence of repeated sequence segments in isolates like ON746333 and ON746337?
>
> *Rationale:* The candidate question is about recombination in a specific tick virus, which is a different intent from the matched gold's focus on broad RNA-virus discovery and compendium. It covers few required elements but is well-grounded in specific data.

**Rank 3** · Comp = 0.527 · ❌ fail

> What is the nucleotide diversity and substitution rate variation across different Botou tick virus types, and does this reflect differences in evolutionary pressure or replication fidelity?
>
> *Rationale:* The candidate question partially aligns with GQ_002 by asking about variation in tick virus types/lineages. However, it focuses on molecular evolutionary metrics (nucleotide diversity, substitution rates) and internal drivers (evolutionary pressure, replication fidelity), rather than the gold's emphasis on stratification by external factors like geography or host range.

**Rank 4** · Comp = 0.340 · ❌ fail

> Do conserved genomic regions exist across all Botou tick virus isolates that could represent essential viral genes or functional domains critical for replication?
>
> *Rationale:* The candidate question focuses on identifying conserved genomic regions within a specific virus, which deviates significantly from GQ_001's intent of broad RNA-virus discovery and reservoir characterization across many tick species. It covers only one required element implicitly but is well-grounded in data.

**Rank 5** · Comp = 0.595 · ❌ fail

> Is there evidence of geographic adaptation in Botou tick virus sequences, as measured by nucleotide composition biases (GC content) that correlate with specific collection locations?
>
> *Rationale:* The candidate question aligns well with understanding geographic variation in viruses, specifically focusing on adaptation through nucleotide composition. It is strongly data-grounded but misses elements related to tick host species, host range, and phylogenetic lineage from the matched gold question.


## 10 · `vertebrate_rna_viruses_2018`

- **raw**：3 文件: `41586_2018_12_MOESM1_ESM.pdf, 41586_2018_12_MOESM2_ESM.xlsx, 41586_2018_12_MOESM3_ESM.xlsx`
- **gold**：2 个 (GQ_001, GQ_002)

### ✅ `claude-code-opus-4-7` — Comp=1.000 · Pass@1=1.00 · Pass@5=1.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 4 | 3 | 5 | 5 | 4.000 | 0.800 | ✅ | GQ_001 (P) |
| 4 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 5 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.799 · ✅ pass

> Across the major vertebrate RNA-virus families recovered from this 186-species chordate meta-transcriptomic survey (e.g. Orthomyxoviridae/Influenza, Arenaviridae, Hantaviridae, Flaviviridae/Hepacivirus, Astroviridae, Picornaviridae, Caliciviridae), do the per-family virus phylogenies show statistically significant co-divergence with their vertebrate host phylogeny — implying ancient origins predating jawed vertebrates — or do they instead reflect repeated cross-class host-switching?
>
> *Rationale:* The candidate question precisely addresses the co-evolutionary relationship between virus and host phylogenies, including ancient origins and host-switching, aligning perfectly with GQ_002's core intent and demonstrating strong data grounding.

**Rank 2** · Comp = 1.000 · ✅ pass

> Given that Orthomyxoviridae (Influenza-like) sequences in this dataset are recovered from ray-finned fish, amphibians and jawless hagfish, where on the vertebrate tree of life does the most recent common ancestor of the Influenza-virus genus map, and does its placement push the genus's origin to before the divergence of Agnatha from jawed vertebrates (~500 Mya)?
>
> *Rationale:* The candidate question is an excellent, highly specific instance of GQ_001, asking about the ancient origin of the Influenza virus genus using broad vertebrate sampling. It covers all required elements, is highly acceptable, and demonstrates strong data grounding.

**Rank 3** · Comp = 0.800 · ✅ pass

> Do anglerfish (Lophiiformes) host a monophyletic, host-restricted clade of fish-specific arenaviruses that constitutes the basal sister lineage to all known mammalian Arenaviridae (Lassa, Machupo, LCMV) and therefore reshapes the evolutionary origin of this zoonotic family?
>
> *Rationale:* The candidate question is a highly specific instance of discovering ancient virus-host associations and evolutionary origins for an RNA-virus family. It is well-grounded in data and well-framed, though it lacks the "broad sampling" aspect of the gold.

**Rank 4** · Comp = 1.000 · ✅ pass

> Do non-mammalian Hepacivirus (Flaviviridae) lineages recovered predominantly from cartilaginous fish (Chondrichthyes) and squamate reptiles in this survey form basal lineages to the human Hepatitis C virus clade, indicating that the genus originated in early jawed vertebrates rather than mammals?
>
> *Rationale:* The candidate question is an excellent, highly specific instance of the gold's intent, focusing on the ancient origins of Hepacivirus in non-mammalian vertebrates. It covers all required elements, is well-framed, and strongly grounded in specific data features.

**Rank 5** · Comp = 0.640 · ✅ pass

> Across this chordate-wide dataset, is virus richness per host library predicted more strongly by host phylogenetic identity (class/order) or by sampled tissue (gut/gill/liver/lung), once sequencing depth (Data bp) is held constant?
>
> *Rationale:* The candidate question investigates factors predicting virus richness (host phylogeny vs. tissue) in a broad chordate dataset, controlling for sequencing depth. It aligns with GQ_001's "virus-host associations" and "broad phylogeny" but misses the "ancient origins" and "RNA-virus families" focus. It is strongly data-grounded.

### ✅ `gpt-5.5-high` — Comp=0.820 · Pass@1=1.00 · Pass@5=0.75

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 3 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 4 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 3 | 5 | 1.800 | 0.360 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.740 · ✅ pass

> How do vertebrate host class and sampled tissue shape the richness and novelty of RNA viruses detected in this chordate metatranscriptomic survey after accounting for sequencing depth and host-species sampling effort?
>
> *Rationale:* The candidate question aligns with GQ_001's focus on vertebrate RNA viruses and metatranscriptomic sampling, covering most required elements. However, it emphasizes richness and novelty rather than the 'deep' or 'ancient' evolutionary associations central to GQ_001. Data grounding is excellent, referencing multiple specific features.

**Rank 2** · Comp = 0.820 · ✅ pass

> Do aquatic and early-branching vertebrate lineages in the survey harbor more divergent RNA virus lineages than amphibian and reptile hosts?
>
> *Rationale:* The candidate question investigates divergent RNA virus lineages in early-branching vertebrates, aligning well with GQ_001's focus on deep virus-host associations and ancient origins across vertebrate phylogeny. It grounds well in specific data features like BLAST identities and host classes, though it omits explicit mention of meta-transcriptomic sampling.

**Rank 3** · Comp = 0.640 · ✅ pass

> Are specific RNA virus classifications preferentially associated with particular vertebrate host classes or orders in this survey?
>
> *Rationale:* The candidate question aligns with the virus-host association aspect of GQ_001 but omits the 'broad sampling' and 'ancient origins' framing. It grounds well in specific data features but is not as ambitious as the gold's acceptable variants.

**Rank 4** · Comp = 0.480 · ❌ fail

> Which sampled organs are most enriched for vertebrate-specific, putative vertebrate, and unknown divergent RNA viruses across the chordate libraries?
>
> *Rationale:* The candidate question focuses on organ-specific distribution of RNA virus types, diverging from the matched gold's intent of revealing deep evolutionary associations and ancient origins across broad vertebrate phylogeny. It covers some elements like RNA viruses and sampling but misses the core historical and broad phylogenetic framing.

**Rank 5** · Comp = 0.360 · ❌ fail

> How much of the variation in RNA virus discovery across libraries is explained by sequencing depth, host-species richness, and geographic sampling location?
>
> *Rationale:* The candidate question addresses methodological factors influencing virus discovery, which differs significantly from the gold's focus on biological insights from broad sampling. It scores low on match strength and required elements but high on data grounding due to specific feature references.

### ✅ `claude-code-sonnet-4-6` — Comp=1.000 · Pass@1=1.00 · Pass@5=0.80

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 2 | 3 | 3 | 5 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 5 | 4 | 5 | 5 | 5 | 4.600 | 0.920 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.697 · ✅ pass

> Do hepaciviruses (Flaviviridae: Hepacivirus) identified across cartilaginous fish, ray-finned fish, lungfish, and reptiles in this metatranscriptomic dataset exhibit conserved hepatotropism and phylogenetic co-divergence with their vertebrate hosts, indicating that liver-specific infection is an ancestral rather than a derived trait of the hepacivirus lineage?
>
> *Rationale:* The candidate question closely matches GQ_002 by focusing on phylogenetic co-divergence between hepaciviruses and vertebrate hosts to infer an ancestral trait. It covers most required elements, omitting EVEs. The question is highly specific and well-grounded in the provided data, referencing files and columns.

**Rank 2** · Comp = 1.000 · ✅ pass

> Does the discovery of influenza-like orthomyxoviruses in hagfish (Myxiniformes, Agnatha) — the most basal vertebrate lineage sampled — and their detection exclusively in gill tissue suggest that the ancestral niche of orthomyxovirus-like viruses was the aquatic mucosal surface of early vertebrates, predating the evolution of respiratory epithelium?
>
> *Rationale:* The candidate question precisely asks about the implications of orthomyxovirus discovery in hagfish gills for ancient viral niches, directly aligning with the gold's focus on deep virus-host associations and ancient origins from broad vertebrate sampling. All required elements are covered, and data grounding is excellent.

**Rank 3** · Comp = 0.560 · ❌ fail

> Across the 273 virus entries in this vertebrate metatranscriptomic survey, does virus family richness per host order correlate with host phylogenetic diversity or sampling depth (sequencing data in bp), and which vertebrate orders are disproportionately virus-rich relative to the sequencing effort invested?
>
> *Rationale:* The candidate analyzes virus richness and sampling bias in a vertebrate metatranscriptomic survey. While sharing the broad context of vertebrate virome discovery with GQ_001, it diverges significantly by focusing on current diversity patterns and sampling effort rather than deep evolutionary history or ancient origins. It is strongly data-grounded.

**Rank 4** · Comp = 0.940 · ✅ pass

> Do the 16 highly divergent viruses classified as 'unknown divergent' (with BLASTX identities <35% to any known virus family) show non-random distribution across host phylogenetic positions or tissue types, suggesting they represent either novel virus families with deep vertebrate ancestry or recent cross-phylum transmission events?
>
> *Rationale:* The candidate question strongly aligns with GQ_001 by investigating specific divergent viruses to uncover novel families and deep vertebrate ancestry. It is highly specific, well-grounded in data, and scientifically rigorous, though it implicitly rather than explicitly mentions the sampling method.

**Rank 5** · Comp = 0.920 · ✅ pass

> Among the six vertebrate classes surveyed, do Chondrichthyes (cartilaginous fish) harbour a disproportionately diverse Flaviviridae assemblage — including hepaciviruses, flaviviruses, and unclassified flavivirids — relative to other classes, and does this diversity support an ancient marine origin for the Flaviviridae prior to the vertebrate land transition?
>
> *Rationale:* The candidate question strongly aligns with GQ_001 by investigating ancient virus-host associations and origins for a specific RNA-virus family within vertebrates. It is highly specific, well-grounded in data, and covers all required elements.

### ✅ `gemini-3.1-pro` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What are the statistically significant differences between the experimental groups as recorded in the quantitative datasets of MOESM2 and MOESM3, and do they support the primary conclusions outlined in the MOESM1 PDF?
>
> *Rationale:* The candidate question is about data validation and statistical analysis across specific files, which is completely unrelated to the evolutionary biology and virology themes of the gold questions. It grounds well in data but does not match the scientific intent.

**Rank 2** · Comp = 0.080 · ❌ fail

> How do the data distributions and variances in the 47KB MOESM3 spreadsheet compare to those in the 22KB MOESM2 spreadsheet?
>
> *Rationale:* The candidate question focuses on comparing statistical properties of data in two specific spreadsheets, which is entirely unrelated to the scientific intent of understanding virus-host associations and ancient origins of RNA-virus families as described in the gold question.

**Rank 3** · Comp = 0.080 · ❌ fail

> Can the quantitative features present in the MOESM2 and MOESM3 Excel files be used to train a predictive model that classifies the experimental outcomes?
>
> *Rationale:* The candidate question is entirely unrelated to the gold question's focus on virus-host evolution and phylogeny. It discusses predictive modeling using Excel files, leading to a complete mismatch in intent and required elements, despite good data grounding for its own topic.

**Rank 4** · Comp = 0.060 · ❌ fail

> Are there any strong correlations or collinearities among the variables recorded in the MOESM3 Excel dataset?
>
> *Rationale:* The candidate question is a generic data analysis query about correlations in a spreadsheet, completely unrelated to the evolutionary biology and virus-host co-evolution themes of the gold questions.

**Rank 5** · Comp = 0.080 · ❌ fail

> Does the textual and visual information in the 74KB MOESM1 PDF provide a complete data dictionary and methodological context for the variables in the Excel files?
>
> *Rationale:* The candidate question focuses on data documentation and methodology for supplementary files, which is completely outside the scope of the provided gold questions concerning vertebrate viral evolution and host-virus co-divergence. It does, however, ground well in the provided data features.

### ✅ `deepseek-v4-pro` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | NO_MATCH (U) |
| 2 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | null (U) |

**Rank 1** · Comp = 0.100 · ❌ fail

> Can the primary effect sizes reported in the supplementary methods document (MOESM1) be independently recapitulated through de novo statistical analysis of the raw data tables provided in MOESM2 and MOESM3?
>
> *Rationale:* The candidate question is about statistical reproducibility using specific supplementary files, which is completely unrelated to the viral evolution and host-virus association themes of the gold questions. Therefore, it does not match any gold question.

**Rank 2** · Comp = 0.100 · ❌ fail

> Does unsupervised clustering of the primary data matrix in MOESM3 reveal biologically meaningful sample subgroups that are not fully explained by the covariate annotations provided in MOESM2?
>
> *Rationale:* The candidate question is about unsupervised clustering of data from MOESM3 and MOESM2, which is completely unrelated to the evolutionary virology themes of any gold question. It scores 0 on match strength, required elements, and acceptability, but 5 on data grounding due to specific file references.

**Rank 3** · Comp = 0.080 · ❌ fail

> Is there evidence of systematic batch effects or technical confounding in the MOESM3 measurement data that correlates with sample processing variables recorded in MOESM2?
>
> *Rationale:* The candidate question is about data quality control and batch effects, which is unrelated to the evolutionary biology themes of the provided gold questions. It grounds well in the specified data files.

**Rank 4** · Comp = 0.080 · ❌ fail

> Does the sample size documented in MOESM2 provide adequate statistical power to detect the smallest effect size claimed as significant in the MOESM1 supplementary results, given the variance structure observed in MOESM3?
>
> *Rationale:* The candidate question is about statistical power analysis, which is unrelated to the viral evolution themes of the gold questions. It scores 0 across most dimensions due to this mismatch, but scores high on data grounding for its specific file references.

**Rank 5** · Comp = 0.080 · ❌ fail

> Would non-parametric or robust statistical methods applied to the MOESM3 data yield materially different inference conclusions compared to the parametric tests described in the MOESM1 supplementary methods?
>
> *Rationale:* The candidate question is about statistical method robustness, which is entirely outside the scope of the provided gold questions concerning vertebrate viral evolution and host-virus associations. It cannot be matched to any gold question, resulting in low scores for match strength, coverage, and acceptability, despite good data grounding.

### ✅ `glm-5` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | None (U) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What is the correlation structure between the variables in the two supplementary datasets (MOESM2 and MOESM3), and does it reveal consistent biological or experimental patterns across different measurement modalities?
>
> *Rationale:* The candidate question is entirely unrelated to the provided gold questions, which focus on viral evolution. It scores 0 for match strength, required elements, and acceptability. However, it demonstrates strong data grounding by referencing specific supplementary files.

**Rank 2** · Comp = 0.080 · ❌ fail

> What is the completeness of the data in both supplementary datasets, and are there systematic patterns of missing values that could indicate experimental limitations or biological phenomena?
>
> *Rationale:* The candidate question focuses on data completeness and missing values, which is a data quality assessment, not a scientific hypothesis related to vertebrate viral evolution or virus-host associations as defined by the gold questions.

**Rank 3** · Comp = 0.100 · ❌ fail

> What are the sample sizes in each dataset, and do they provide sufficient statistical power to detect meaningful biological or experimental effects?
>
> *Rationale:* The candidate question focuses on generic data quality and statistical power, which is entirely unrelated to the specific scientific intent of the provided gold questions concerning viral evolution and host associations. It grounds well in data but fails to match any scientific question.

**Rank 4** · Comp = 0.080 · ❌ fail

> Are there distinct experimental groups or temporal patterns in the data that correspond to different study conditions or time points?
>
> *Rationale:* The candidate question focuses on identifying experimental groups or temporal patterns in generic data, which is completely unrelated to the specific topic of vertebrate RNA-virus evolution and host associations covered by the gold questions.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the distribution of values across variables in both datasets, and are there outliers or anomalies that require special consideration in the analysis?
>
> *Rationale:* The candidate question is a generic data quality and exploration question, completely unrelated to the scientific domain of viral evolution and host associations covered by the gold questions. It scores 0 on all scientific alignment dimensions but well on data grounding due to explicit file references.

### ✅ `gemini-2.5-flash` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What are the key experimental findings or datasets presented in the supplementary Excel files, and how do they support the main conclusions of the associated publication?
>
> *Rationale:* The candidate question is a generic request to understand supplementary data, which does not align with the specific scientific inquiry of the gold questions about viral evolution. It grounds well in data but fails on all other scientific alignment metrics.

**Rank 2** · Comp = 0.080 · ❌ fail

> Do the supplementary Excel datasets contain sufficient statistical power or sample size to validate the claims made in the main research article?
>
> *Rationale:* The candidate question focuses on statistical power and sample size of supplementary data, which is a generic data validation question. It does not align with the specific scientific intent of any provided gold question, which are all focused on virus-host evolution.

**Rank 3** · Comp = 0.080 · ❌ fail

> What specific methodologies or detailed protocols are described in the supplementary PDF, and how do they inform the interpretation of the experimental data in the Excel files?
>
> *Rationale:* The candidate question is about extracting methodologies from a supplementary PDF to interpret Excel data, which is completely unrelated to the evolutionary biology questions posed in the gold standards. It grounds well in the provided data features but does not match the scientific intent of any gold question.

**Rank 4** · Comp = 0.100 · ❌ fail

> Are there any discrepancies or inconsistencies between the data presented in the two Excel supplementary files, or between these files and the information implied by the PDF?
>
> *Rationale:* The candidate question addresses data consistency across supplementary files, a general data quality concern, and is entirely unrelated to the scientific inquiry of virus-host evolution posed by the gold question.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the overall scope and context of the research presented, as indicated by the titles or introductory information within the supplementary materials?
>
> *Rationale:* The candidate question is a meta-inquiry about the research's scope, not a scientific question about virus-host evolution. It lacks any scientific elements from the gold questions and therefore scores very low on match strength, coverage, and acceptability, despite good data grounding.

### ✅ `intern-s1` — Comp=0.180 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | unknown (U) |
| 2 | 0 | 0 | 3 | 3 | 0.900 | 0.180 | ❌ | unknown (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.080 · ❌ fail

> Is there a significant correlation between temperature and species richness in the dataset?
>
> *Rationale:* The candidate question explores an ecological correlation (temperature and species richness) which is completely outside the scope of the provided gold questions concerning viral evolution and host-virus associations. Thus, it does not match any gold question.

**Rank 2** · Comp = 0.180 · ❌ fail

> How does the species composition change over time in the study area?
>
> *Rationale:* The candidate question focuses on ecological species composition changes over time, which is unrelated to the virus-host evolution and phylogeny themes of the gold questions. It is a valid question but does not align with the provided scientific context.

**Rank 3** · Comp = 0.080 · ❌ fail

> Are there distinct spatial patterns in species distribution across different habitats?
>
> *Rationale:* The candidate question is about spatial patterns in species distribution, which is completely unrelated to the virus-host evolution and phylogeny themes of the gold questions. It does, however, provide good data grounding.

**Rank 4** · Comp = 0.060 · ❌ fail

> Does pH level significantly affect the abundance of a specific species?
>
> *Rationale:* The candidate question is completely unrelated to the matched gold question's intent regarding virus-host evolution. Consequently, it covers none of the required elements and is not close to any of its variants. It does, however, reference a specific data file.

**Rank 5** · Comp = 0.080 · ❌ fail

> How do species diversity indices differ between two different sampling sites?
>
> *Rationale:* The candidate question on species diversity is entirely unrelated to the virus-host evolution topic of the matched gold question, resulting in zero match strength and required element coverage. It does not resemble any gold variants but grounds its concepts in the provided file types.

### ✅ `intern-s1-pro` — Comp=0.120 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | None (U) |

**Rank 1** · Comp = 0.080 · ❌ fail

> What is the correlation between the primary experimental variables across the two Excel datasets, and is it statistically significant at p < 0.05?
>
> *Rationale:* The candidate question is a generic statistical query about correlations in Excel files, completely unrelated to the specific biological and evolutionary scope of the gold questions, which focus on vertebrate viral evolution and host-virus associations.

**Rank 2** · Comp = 0.080 · ❌ fail

> Do the experimental conditions described in the supplementary PDF show significant differences in outcome measures between treatment groups?
>
> *Rationale:* The candidate question is entirely unrelated to the scientific domain of the gold questions, focusing instead on generic experimental design and statistical analysis of treatment groups, thus scoring zero on most dimensions despite good data grounding.

**Rank 3** · Comp = 0.080 · ❌ fail

> What biological mechanisms are most strongly supported by the gene expression or molecular interaction patterns in the Excel datasets?
>
> *Rationale:* The candidate question is about general biological mechanisms and gene expression patterns, which is entirely unrelated to the specific focus of the gold questions on vertebrate viral evolution and host-virus phylogenetics.

**Rank 4** · Comp = 0.120 · ❌ fail

> How do the clinical or phenotypic outcomes correlate with molecular measurements across the experimental dataset?
>
> *Rationale:* The candidate question is entirely unrelated to the gold question's focus on vertebrate RNA-virus evolution, resulting in very low scores for match strength and required elements coverage. While well-formed, it is irrelevant to the gold's domain. It does, however, reference multiple data features and specific files.

**Rank 5** · Comp = 0.080 · ❌ fail

> What is the reproducibility and data quality of the experimental measurements across technical replicates in the Excel datasets?
>
> *Rationale:* The candidate question focuses on generic data quality and reproducibility, which is unrelated to the specific scientific inquiries about virus-host evolution and phylogeny posed by the gold questions. It is well-grounded in data but off-topic.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ✅ `intern-s2-preview` — Comp=0.100 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (U) |
| 2 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (U) |
| 4 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What are the key quantitative patterns and relationships in the supplementary experimental data that support the main findings of the Nature publication?
>
> *Rationale:* The candidate question is too generic, asking about any quantitative patterns in any supplementary data, making it unrelated to the specific virology and evolutionary biology focus of the gold questions. It grounds well in the provided data files but completely misses the scientific intent.

**Rank 2** · Comp = 0.080 · ❌ fail

> How do the variables in the supplementary Excel datasets correlate with each other, and what do these correlations reveal about the underlying biological or physical mechanisms?
>
> *Rationale:* The candidate question is a generic data analysis query about correlations in Excel files, completely missing the specific scientific intent of the gold questions regarding vertebrate viral evolution and phylogeny. It does, however, provide good data grounding by naming specific files.

**Rank 3** · Comp = 0.080 · ❌ fail

> What experimental conditions or groups are represented in the supplementary data, and how do outcomes differ across these conditions?
>
> *Rationale:* The candidate question is entirely unrelated to the gold questions, focusing instead on general experimental conditions and outcomes within supplementary data, which leads to low scores across most dimensions despite good data grounding for its own intent.

**Rank 4** · Comp = 0.080 · ❌ fail

> Are there temporal or sequential patterns in the supplementary data that suggest dynamic processes or time-dependent effects?
>
> *Rationale:* The candidate question is a generic data analysis query about temporal patterns, completely unrelated to the specific biological and evolutionary scope of the gold questions. It fails to address any core scientific intent of the rubric, despite good data grounding.

**Rank 5** · Comp = 0.100 · ❌ fail

> To what extent does the supplementary data provide independent validation of the main publication's statistical claims and effect sizes?
>
> *Rationale:* The candidate question focuses on data validation and reproducibility of statistical claims, which is entirely unrelated to the biological evolutionary questions posed in the gold set. It scores high on data grounding due to specific file references.


## 11 · `zooplankton_rna_virosphere_2022`

- **raw**：10 文件: `16945363_31352431_chrysoviridae_alignment.fas, 16945399_31352560_Narnaviridae_alignment.fas, 16945423_31352587_Picornavirales_alignment.fas, 16945426_31352578_Partitiviridae_alignment.fas...`
- **gold**：2 个 (GQ_001, GQ_002)

### ❌ `claude-code-opus-4-7` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`

### ❌ `gpt-5.5-high` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `claude-code-sonnet-4-6` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`

### ✅ `gemini-3.1-pro` — Comp=0.697 · Pass@1=1.00 · Pass@5=0.45

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 3 | 4 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.697 · ✅ pass

> How do the newly identified RdRp contigs from the Hirai dataset phylogenetically place within the established diversity of RNA virus families like Partitiviridae and Narnaviridae?
>
> *Rationale:* The candidate question aligns well with GQ_002's intent to classify RdRp contigs using family alignments, explicitly referencing relevant data files. It is specific and scientific, though it omits the zooplankton origin of the data.

**Rank 2** · Comp = 0.560 · ❌ fail

> Are there novel, unclassified viral lineages present in the 'Possible_virus_contigs' that do not align with any of the provided reference families?
>
> *Rationale:* The candidate question partially aligns with uncovering RNA virosphere diversity by seeking novel lineages, but misses the zooplankton and host-association context. It uses specific data files but lacks key gold elements like RdRP and community type, placing it as mid-quality.

**Rank 3** · Comp = 0.289 · ❌ fail

> What is the degree of sequence conservation within the RdRp gene across the different viral orders represented in the dataset (e.g., Picornavirales vs. Reoviridae)?
>
> *Rationale:* The candidate question is about sequence conservation within specific viral orders, which is a different intent than the matched gold's focus on RdRP OTU clustering and classification of viral diversity. It grounds well in specific data files but covers few required elements.

**Rank 4** · Comp = 0.629 · ✅ pass

> Do the 'Chu-like' and 'Narna-like' contigs identified in the Hirai dataset represent monophyletic clades, or are they interspersed among known members of those families?
>
> *Rationale:* The question aligns with GQ_002 by focusing on phylogenetic classification of RdRP contigs within viral families using alignments to assess monophyly. It grounds well in specific data files and features but omits explicit mention of ssRNA/dsRNA and zooplankton context.

**Rank 5** · Comp = 0.476 · ❌ fail

> Can hidden Markov models (HMMs) built from the provided family alignments successfully identify distant homologs in the 'Possible_virus_contigs' dataset?
>
> *Rationale:* The candidate partially matches GQ_002 by using family alignments for classification, but deviates significantly in method (HMMs vs. OTU clustering) and scope (general homologs vs. specific virus types/hosts). It grounds well in data but misses several core required elements.

### ❌ `deepseek-v4-pro` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 195)`

### ❌ `glm-5` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`

### ❌ `gemini-2.5-flash` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`

### ✅ `intern-s1` — Comp=0.425 · Pass@1=0.00 · Pass@5=0.00

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 4 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 1 | 1 | 3 | 4 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 3 | 1 | 0 | 3 | 2 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 4 | 0.400 | 0.080 | ❌ | GQ_002 (U) |

**Rank 1** · Comp = 0.425 · ❌ fail

> What are the evolutionary relationships between the RdRp sequences from different virus families, and do they reveal any novel phylogenetic groupings?

**Rank 2** · Comp = 0.289 · ❌ fail

> Are there conserved functional motifs in the RdRp sequences across different virus families that could serve as targets for antiviral drugs?
>
> *Rationale:* The candidate question is about identifying functional motifs in RdRp sequences for antiviral targets, which is distinct from the gold's intent of classifying virus diversity. It poorly covers the gold's required elements but is well-grounded in data.

**Rank 3** · Comp = 0.240 · ❌ fail

> Do the hypothetical proteins in the metagenomic sequences represent novel viral genes with unknown functions?
>
> *Rationale:* The candidate question focuses on identifying novel viral genes from hypothetical proteins in metagenomic sequences. This is a weak match to GQ_001, which is about RNA virosphere diversity and host-association in zooplankton. No required elements are covered.

**Rank 4** · Comp = 0.280 · ❌ fail

> Is the Capsid protein sequence under positive selection, indicating adaptation to host environments?
>
> *Rationale:* The candidate question focuses on positive selection of a specific viral protein for host adaptation, a distinct evolutionary hypothesis. It only loosely connects to the host-association aspect of GQ_001, which primarily concerns RNA virosphere discovery in zooplankton, leading to low scores.

**Rank 5** · Comp = 0.080 · ❌ fail

> Do any sequences in the dataset show evidence of horizontal gene transfer between virus families?
>
> *Rationale:* The candidate question about horizontal gene transfer is unrelated to the scope of the provided gold questions, which focus on RNA virosphere discovery or RdRP OTU classification in zooplankton. It references specific data files but does not align with any gold question's intent or required elements.

### ✅ `intern-s1-pro` — Comp=0.640 · Pass@1=0.00 · Pass@5=0.15

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 3 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 4 | 1.000 | 0.200 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.578 · ❌ fail

> What are the phylogenetic relationships among the different virus families represented in the dataset, and how do they cluster based on sequence similarity?
>
> *Rationale:* The candidate question aligns with classifying virus families using sequence similarity and clustering, similar to GQ_002's focus on RdRP OTU classification. It grounds well in data but omits specific virus types (ssRNA/dsRNA) and the zooplankton context.

**Rank 2** · Comp = 0.357 · ❌ fail

> Which regions of the RdRp (RNA-dependent RNA polymerase) gene are most conserved across the different virus families, and what might this imply about their functional importance?
>
> *Rationale:* The candidate question focuses on RdRp gene conservation and functional importance, a different intent from `GQ_002`'s classification goal. It references specific data files well but covers few of `GQ_002`'s required elements.

**Rank 3** · Comp = 0.120 · ❌ fail

> Are there detectable recombination events between different virus strains within the same family, and if so, what are the potential breakpoints?
>
> *Rationale:* The candidate question focuses on recombination events in virus strains, which is entirely unrelated to the discovery of RNA virosphere diversity or host-association questions posed by the gold question. It grounds well in data but is off-topic.

**Rank 4** · Comp = 0.640 · ✅ pass

> Based on sequence similarity to known viruses, what potential host ranges can be predicted for the unclassified ssRNA virus contigs in the dataset?
>
> *Rationale:* The candidate question is a specific host-association query for unclassified ssRNA virus contigs, aligning with a secondary aspect of GQ_001. It grounds well in data but misses the zooplankton context and the primary intent of discovering RNA virosphere diversity.

**Rank 5** · Comp = 0.200 · ❌ fail

> What regions of the viral genomes show evidence of positive selection, and what might this suggest about host-virus co-evolution?
>
> *Rationale:* The candidate question on positive selection and host-virus co-evolution is largely unrelated to the gold's focus on discovering RNA virosphere diversity from specific zooplankton data. It misses all required elements and does not align with the gold's acceptable variants, despite strong data grounding.

### ⚪ `intern-s1-mini` — 失败 （用户决定不再重测）`agent=intern-s1-mini`

### ❌ `intern-s2-preview` — 失败 `JSONDecodeError: Expecting ',' delimiter: line 9 column 4 (char 197)`
