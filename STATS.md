# Per-qset × Per-Agent · 5-Candidate 完整明细（按 qset 合并 · 重复取最高 · 完整问题文本）

qset 总数：**11** · 当前 agent：7 个 · 合并规则：**同一 qset 跨多次上传只保留 rank-1 composite_score 最高的那次**

## 0 · 覆盖矩阵

| qset | cc-opus-4-7 | gpt-5.5-high | cc-sonnet-4-6 | gem-3.1-pro | ds-v4-pro | glm-5 | gem-2.5-flash | 重复上传 |
|---|---|---|---|---|---|---|---|---|
| `amphibian_reptile_virome_2022` | ✅ | ✅ | ✅ | 🟨 | ✅ | 🟨 | ✅ | 1 |
| `arthropod_neg_sense_2015` | ✅ | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `bat_btcn_virome_2024` | ✅×2 | ✅×3 | ✅×4 | ✅×3 | ✅×3 | ✅ | ✅×3 | 9 |
| `flavi_jingmen_jvi_2016` | ✅ | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `invertebrate_rna_virosphere_2016` | 🟨 | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `oyster_rna_virome_2024` | ✅ | 🟨 | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `rvmt_cell_2022` | ✅ | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `tara_oceans_science_2022` | ✅ | 🟨 | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `tick_metavirome_2023` | ✅ | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `vertebrate_rna_viruses_2018` | ✅ | ✅ | ✅ | ✅ | ✅ | 🟨 | ✅ | 1 |
| `zooplankton_rna_virosphere_2022` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 |
| **合计 ✅** | **10/11** | **9/11** | **11/11** | **10/11** | **11/11** | **2/11** | **11/11** |  |


---
## 1 · `amphibian_reptile_virome_2022`

- **数据**：1 文件 · 2,250,456 bytes · 例：43705_2022_180_MOESM1_ESM.docx
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779594663_8f5abd)
- **已评测 agent**：5/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779594663_8f5abd`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 3 | 4 | 3 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 4 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 5 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.820 · ✅ pass

> Across the 234 publicly archived herptile RNA-Seq libraries catalogued in Supplementary Table 1, do library chemistry (poly(A) vs total-RNA), tissue type, and host clade (Amphibia vs Reptilia) jointly bias the recoverable viral family spectrum, in particular the detection of negative-sense RNA viruses such as Bunyavirales and Rhabdoviridae (e.g. the alligator-associated rabies lyssavirus shown in Supplementary Figure 2)?
>
> *Rationale:* Matches GQ_001's public herptile transcriptome-mining intent but pivots to quantifying detection biases (poly(A), tissue, host clade) for negative-sense RNA viruses; strongly grounded in Supplementary Table 1 and Figures 1–2.

**Rank 2** · Comp = 0.850 · ✅ pass

> Does the alligator-associated rabies lyssavirus identified in Crocodylus/Alligator RNA-Seq libraries (Supplementary Figure 2) represent a previously unrecognised non-mammalian reservoir lineage of Lyssavirus, and is its nucleoprotein gene phylogenetically nested inside Rabies lyssavirus rather than forming a sister clade?
>
> *Rationale:* The candidate precisely asks whether reptile-associated lyssaviruses form a novel non-mammalian reservoir lineage and whether the N-gene is nested within Rabies lyssavirus, matching the phylogenetic-novelty gold question.

**Rank 3** · Comp = 0.595 · ❌ fail

> Do the novel amphibian and reptile Hepeviridae and Astroviridae genomes identified in Supplementary Figure 3 share a common recombination breakpoint between non-structural and structural genes, indicating an ancient inter-family recombination event in the herptile gut virome?
>
> *Rationale:* Matches GQ_002 because it studies phylogenetic relationships of recovered herptile viruses within known families, with strong evidence grounding; however it asks about inter-family recombination rather than basal/divergent placement, so partial intent alignment (3/5) and high element coverage (4/5).

**Rank 4** · Comp = 0.850 · ✅ pass

> Is the novel newt orthomyxovirus reported in Supplementary Figure 4, recovered from Cynops pyrrhogaster mixed-viscera RNA-Seq, a divergent influenza virus that expands the known host range of Orthomyxoviridae into Caudata, and does its PB1 polymerase cluster outside known influenza A/B/C/D clades?
>
> *Rationale:* Direct, specific match to GQ_002: tests whether a public RNA-seq–derived newt orthomyxovirus occupies a divergent/basal position within Orthomyxoviridae using PB1 phylogeny, grounded in SRR1553357 and Supplementary Figure 4.

**Rank 5** · Comp = 0.740 · ✅ pass

> Does viral discovery yield, measured as the number of distinct viral families recovered per library, scale predictably with sequencing depth/platform (e.g. HiSeq 2000 vs NextSeq 500 vs HiSeq X Ten) and with the country/biogeographic origin of the herptile host across the libraries listed in Supplementary Table 1?
>
> *Rationale:* The candidate aligns with the primary intent of mining public herptile transcriptomes for viral diversity but shifts emphasis to quantifying technical and biogeographic determinants of per-library viral-family recovery; it is well grounded in named supplementary tables/figures.

### ✅ `gpt-5.5-high` · src = `upl_1779594663_8f5abd`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 4 | 5 | 4.800 | 0.960 | ✅ | GQ_001 (P) |
| 4 | 3 | 4 | 2 | 4 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 5 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> What novel RNA viruses can be detected in publicly available amphibian and reptile RNA-seq datasets, and how do their phylogenetic placements within Bunyavirales, reptile lyssaviruses, Hepeviridae, Astroviridae, influenza viruses, and caliciviruses expand known herptile virus diversity?
>
> *Rationale:* The candidate precisely targets discovery of novel viruses in public amphibian/reptile RNA-seq and their phylogenetic placement, matching the gold question's intent and grounded in the supplied DOCX accession table and family-specific supplementary figures.

**Rank 2** · Comp = 0.940 · ✅ pass

> How does the uneven distribution of host class, tissue type, country of origin, and sequencing platform in the 235 amphibian and reptile RNA-seq accessions shape the likelihood of detecting novel herptile RNA viruses?
>
> *Rationale:* The candidate faithfully targets public amphibian/reptile RNA-seq to assess discovery of novel viruses and is tightly grounded in accession-table metadata; only the explicit mention of 'assembly or transcriptome mining' is missing.

**Rank 3** · Comp = 0.960 · ✅ pass

> Do amphibian and reptile transcriptomes from geographically concentrated sampling regions such as French Giana, China, the USA, Australia, Cuba, India, Denmark, and Madagascar reveal distinct pools of novel RNA viruses?
>
> *Rationale:* The candidate directly asks whether amphibian/reptile transcriptome mining reveals novel viruses and ties this to SRA accessions and country metadata, fully matching the gold question's intent while adding geographic testing of sampling effects.

**Rank 4** · Comp = 0.544 · ❌ fail

> Do the novel amphibian and reptile hepevirus and astrovirus contigs show different structural and non-structural gene phylogenies consistent with recombination near the common breakpoint indicated in the supplementary figure?
>
> *Rationale:* The candidate clearly involves phylogenetic analysis of recovered amphibian/reptile viruses and references families and supplement figures, but its focus on recombination/topology incongruence does not ask whether these viruses occupy basal/divergent positions as GQ_002 does.

**Rank 5** · Comp = 0.820 · ✅ pass

> Which amphibian and reptile host lineages in the public RNA-seq accession table are the strongest priorities for future herptile RNA virus surveillance based on taxonomic representation, tissue coverage, and the viral families highlighted in the supplementary figures?
>
> *Rationale:* The candidate aligns well with GQ_001 by using public amphibian/reptile RNA-seq and supplementary viral findings to prioritize surveillance (strong data grounding), but it omits explicit mention of 'under-sampled' hosts and reframes discovery as surveillance prioritization.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779594663_8f5abd`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 3 | 4 | 2 | 5 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 4 | 2 | 4 | 3 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Does the number of distinct tissue types sampled per host species predict the total number of novel RNA virus families detected in that species' transcriptomes across the 236-accession herptile RNA-seq dataset?
>
> *Rationale:* The candidate explicitly tests whether sampling breadth in a public herptile RNA‑seq dataset predicts discovery of novel RNA virus families, matching GQ_001's public transcriptome mining for hidden viral diversity with strong dataset grounding.

**Rank 2** · Comp = 1.000 · ✅ pass

> Do amphibians and reptiles differ in their per-species RNA virome breadth (number of novel virus families detected) after controlling for the number of tissues and SRA accessions sampled in this 236-accession herptile metatranscriptomic dataset?
>
> *Rationale:* The candidate is a specific, data-grounded test of whether public amphibian/reptile RNA-seq reveals differing hidden viral family richness, matching the gold question's scope and required elements.

**Rank 3** · Comp = 0.561 · ❌ fail

> Is tissue-specific viral tropism detectable among the novel Hepeviridae and Astroviridae identified in herptile transcriptomes when the tissue of origin (liver, kidney, skin, viscera) is mapped against virus clade membership across the 236-accession dataset?
>
> *Rationale:* The candidate aligns with GQ_002 on recovered herptile viruses and phylogenetic clades but shifts focus to tissue tropism, omitting the core question about basal/divergent phylogenetic positions while being well grounded in specific supplementary figures and table columns.

**Rank 4** · Comp = 0.527 · ❌ fail

> Does geographic origin (country of collection) predict the phylogenetic clade of novel Bunyavirales and lyssaviruses identified from herptile RNA-seq transcriptomes in the 236-accession dataset?
>
> *Rationale:* Matches GQ_002 moderately: shares phylogenetic analysis of recovered herptile viruses and known viral groups but shifts focus to geographic prediction rather than testing basal/divergent placement; most required elements present except basal/divergent positions, and the question is well grounded in supplementary figures/tables.

**Rank 5** · Comp = 0.580 · ❌ fail

> Does the use of polyA-selection during library preparation (as flagged by asterisked platforms in Supplementary Table 1) systematically reduce the detection rate of non-polyadenylated RNA viruses such as Bunyavirales and Rhabdoviridae in the 236-accession herptile transcriptome dataset?
>
> *Rationale:* Matches the primary topic of mining herptile transcriptomes but shifts to library-prep bias (polyA-selection) rather than testing whether public data reveal hidden or novel viruses; however it is strongly grounded in specific supplementary files/columns.

### 🟨 `gemini-3.1-pro` — **未评测（待补）**

### ✅ `deepseek-v4-pro` · src = `upl_1779594663_8f5abd`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 0 | 3 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> Are there significant effect-measure modifications by age group and baseline severity in the primary exposure-outcome associations reported across the supplementary tables of this 2022 biomedical study, and do these modifications remain robust under alternative confounding-adjustment strategies?
>
> *Rationale:* The candidate is about clinical effect modification in a 2022 supplementary .docx (well grounded) and is semantically unrelated to the gold's RNA-seq virome-mining question, so match strength and required-element coverage are nil.

**Rank 2** · Comp = 0.060 · ❌ fail

> What is the dose-response shape linking the primary exposure variable to the main study outcome, and does the shape differ when modeled with categorical versus continuous-spline specifications as reported in this supplementary material?
>
> *Rationale:* The candidate concerns biomedical dose-response/spline modeling in a .docx supplement and is semantically unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viruses; it does reference the provided .docx file but matches no required elements.

**Rank 3** · Comp = 0.100 · ❌ fail

> Do the study's primary findings exhibit evidence of publication or reporting bias when the supplementary sensitivity analyses — including leave-one-out estimates, trim-and-fill results, and funnel-plot asymmetry tests — are evaluated collectively?
>
> *Rationale:* The candidate concerns meta-analysis publication bias in a supplementary .docx and is unrelated to the gold question about mining amphibian/reptile RNA-seq for novel viruses, so it fails to match required elements though it is grounded to the MOESM1 file.

**Rank 4** · Comp = 0.100 · ❌ fail

> How consistent are the study's primary effect estimates across the pre-specified sensitivity and subgroup analyses, and which study-level covariates — such as geographic region, study design, or quality score — most strongly moderate the observed effect sizes?
>
> *Rationale:* The candidate is a meta-analysis question about subgroup/sensitivity analyses and covariate moderation, which does not address transcriptome mining or virome discovery in amphibians/reptiles as required by the matched gold.

**Rank 5** · Comp = 0.100 · ❌ fail

> What is the comparative ranking of multiple candidate risk factors or interventions by their adjusted effect magnitudes and precision, and does the ranking remain stable when the outcome definition is varied across the alternative case definitions reported in this supplementary material?
>
> *Rationale:* The candidate focuses on ranking risk factors across outcome definitions in a specific supplement (.docx), which is unrelated to the gold question about mining amphibian/reptile RNA-seq for hidden viruses, so no required elements are covered.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779594663_8f5abd`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 2 | 0.400 | 0.080 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What is the relationship between experimental treatment conditions and observed biological outcomes in the study described in the supplementary material?
>
> *Rationale:* The candidate concerns experimental treatment effects in a supplementary DOCX and is semantically unrelated to the gold question about mining public amphibian/reptile RNA-seq for hidden viruses; it contains none of the required viromics elements but does reference the specific supplementary file.

**Rank 2** · Comp = 0.080 · ❌ fail

> Are there specific molecular markers or phenotypic characteristics that are significantly altered under different experimental conditions?
>
> *Rationale:* The candidate is a generic biomarker/phenotype differential question unrelated to the gold's focus on mining amphibian/reptile RNA‑seq for hidden viruses; it references one supplementary DOCX but lacks any of the required topical elements.

**Rank 3** · Comp = 0.100 · ❌ fail

> How do various patient demographic or clinical parameters correlate with the experimental results presented in the supplementary data?
>
> *Rationale:* The candidate addresses clinical metadata correlations in a supplementary DOCX, which is semantically unrelated to the gold question about mining public amphibian/reptile RNA-seq for novel viruses; it references a specific file but contains none of the required viromics elements.

**Rank 4** · Comp = 0.080 · ❌ fail

> What is the statistical significance and magnitude of the observed differences or associations reported within the supplementary data?
>
> *Rationale:* The candidate requests general statistical evaluation of supplementary results and contains none of the domain-specific elements (amphibian/reptile RNA-seq, viral discovery, transcriptome mining) required by GQ_001, so it is an unrelated, low-quality match despite referencing a DOCX supplement.

**Rank 5** · Comp = 0.100 · ❌ fail

> Does the supplementary material provide sufficient detail on experimental methods and data quality to ensure reproducibility and validate the study's findings?
>
> *Rationale:* The candidate concerns reproducibility and supplementary methods, which is semantically unrelated to the gold question about mining public amphibian/reptile RNA-seq for hidden viruses; it does, however, cite a specific DOCX supplement file.


---
## 2 · `arthropod_neg_sense_2015`

- **数据**：2 文件 · 6,528,071 bytes · 例：elife-05378-supp-v1.zip, nuccore_reported_viral_sequences.fasta
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779596259_f8c4ae)
- **已评测 agent**：6/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 4 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 4 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.748 · ✅ pass

> Across the 170 KM817593–KM817764 arthropod-derived RNA virus sequences, does host arthropod order (e.g. Ixodida ticks vs. Diptera flies/mosquitoes vs. Araneae spiders) explain more of the variance in RdRp (L-gene) phylogenetic placement than does Chinese sampling locality, and where do the orthomyxo-like (PB1-bearing) and bunya-/phenui-like (N+G+L) lineages place relative to known vector-borne pathogens of vertebrates?
>
> *Rationale:* The candidate closely matches GQ_002 by using RdRp/L trees and explicit segmented vs orthomyxo-/bunya-like lineage comparisons with strong grounding in the KM817593–KM817764 FASTA metadata, while adding host vs geography variance partitioning as an extra analysis.

**Rank 2** · Comp = 0.850 · ✅ pass

> Among the 170 arthropod RNA virus genomes in KM817593–KM817764, do segmented (bunya-/orthomyxo-like) versus unsegmented (mononega-like) genome architectures cluster non-randomly within particular host arthropod orders, and what does this distribution imply about the deep ancestry of negative-sense RNA virus segmentation?
>
> *Rationale:* Strong match to GQ_002: asks if segmented vs unsegmented arthropod viruses cluster by host order and what that implies about segmentation transitions, cites specific accessions and annotations, covers all required elements and aligns with acceptable phrasing.

**Rank 3** · Comp = 0.740 · ✅ pass

> Do the tick-derived virus lineages within KM817593–KM817764 (Bole, Changping, Huangpi, Tacheng, Wenzhou, Yongjia, Lihan, Dabieshan tick viruses) form a monophyletic phlebo-/phenui-like clade with the SFTS-virus group, and does branch-level genetic divergence correlate with sampling latitude across these Chinese collection sites?
>
> *Rationale:* The candidate is a well-grounded, specific phylogenetic and phylogeographic test of tick-derived phenuivirus-like sequences (strong data grounding) but is narrower than the gold's broad arthropod/RNA-seq and basal-lineage discovery scope.

**Rank 4** · Comp = 0.578 · ❌ fail

> Do the 25 mosquito-associated virus sequences in KM817593–KM817764 (Wuhan/Wutai/Qingnian/Jiangxia/Shuangao Mosquito Viruses) carry RdRp / PB1 sequences whose closest published relatives are arboviruses of medical importance, suggesting candidate insect-specific viruses for vector-competence screening?
>
> *Rationale:* Matches GQ_002's arthropod + RdRp phylogeny theme but omits the segmentation/phylogenetic-gap focus; well-grounded in specific accessions and files, so useful but narrower than the gold intent.

**Rank 5** · Comp = 0.640 · ✅ pass

> Within the KM817593–KM817764 arthropod virome, can RdRp-based open-reading-frame length and gene-architecture annotations (presence/absence of NSs, ORF1/ORF2/ORF3 accessory frames) be used to operationally define new virus genera or families that are currently unclassified by ICTV, and how many such candidate taxa are recoverable?
>
> *Rationale:* Matches GQ_001 on arthropod data and genome-architecture use but shifts focus to ICTV-style taxonomic delimitation rather than testing basal lineage/ancestry; three of five required elements are present and the question is strongly data-grounded.

### ✅ `gpt-5.5-high` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 2 | 2 | 3 | 5 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 5 | 1.105 | 0.221 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.697 · ✅ pass

> Do the reported invertebrate viral RNA-dependent RNA polymerase sequences reveal host-associated lineages that bridge or expand established negative-sense RNA virus families?
>
> *Rationale:* The candidate strongly matches GQ_002 by asking if invertebrate RdRp sequences bridge/expand negative-sense virus families and cites concrete fasta and supplement phylogeny data, but it omits explicit mention of segmented vs non-segmented genome transitions required by the gold question.

**Rank 2** · Comp = 0.500 · ❌ fail

> Are tick-associated viral sequences disproportionately represented in polymerase, glycoprotein, and nucleocapsid markers compared with other invertebrate host groups in this dataset?
>
> *Rationale:* The candidate examines sampling bias of tick-associated records and marker completeness relevant to negative-sense virus phylogenetic placement, so it partially matches GQ_001 but lacks explicit focus on arthropod RNA-seq, basal lineages, and genome architecture.

**Rank 3** · Comp = 0.646 · ✅ pass

> Do segmented invertebrate virus records in the FASTA correspond to phylogenetic placements near known segmented negative-sense RNA virus groups?
>
> *Rationale:* The candidate is a focused, data-grounded test of whether segmented invertebrate FASTA records map to known segmented negative-strand clades, matching GQ_002's intent but narrower (omits explicit non-segmented comparisons and 'bridging' language).

**Rank 4** · Comp = 0.460 · ❌ fail

> Which invertebrate host-associated virus groups have enough paired polymerase, glycoprotein, and nucleocapsid sequence data to support comparative genome-architecture analysis?
>
> *Rationale:* The candidate aligns with the gold's genome-architecture focus but is dataset-completeness oriented and omits key elements (arthropod RNA-seq, negative-sense/basal ancestry), so it partially matches but lacks core intent.

**Rank 5** · Comp = 0.221 · ❌ fail

> Do sequence length and completeness annotations differ systematically among the host-associated viral records reported from ticks, mosquitoes, flies, and other invertebrates?
>
> *Rationale:* Candidate is about metadata (length/completeness) across arthropod hosts and is well grounded in the nuccore FASTA, but it does not address GQ_002's core phylogenetic/segmentation questions, so the semantic match is poor.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 3 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 4 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.544 · ❌ fail

> Do the RNA-dependent RNA polymerase (L gene) phylogenies of the novel invertebrate viruses recovered from blood-feeding arthropods (ticks, mosquitoes, louse flies, horseflies) form host-ecology-associated clades distinct from those infecting non-blood-feeding invertebrates (spiders, cockroaches, water striders, millipedes) in the KM817593–KM817764 sequence set, indicating that hematophagous feeding behavior is a consistent predictor of arthropod-virus phylogenetic clustering?
>
> *Rationale:* Selected GQ_002 because of the explicit L-protein phylogeny and arthropod-virus focus; the candidate tests host-ecology clustering rather than segmentation or bridging gaps, so it partially matches required elements but misses core segmentation/transition goals.

**Rank 2** · Comp = 0.540 · ❌ fail

> Do novel arthropod RNA viruses encoding the full mononegavirales-like gene repertoire (nucleocapsid N, glycoprotein G, and RNA-dependent RNA polymerase L) in the KM817593–KM817764 dataset show significantly higher genomic GC content and longer coding sequences in tick-associated strains compared to dipteran (fly and mosquito)-associated strains, suggesting that tick vector biology selects for distinct genome composition constraints?
>
> *Rationale:* The candidate is well grounded in dataset specifics and addresses genome architecture of arthropod negative-sense viruses, but it does not ask about basal lineages or phylogenetic ancestry required by the matched gold question, so it partially aligns but diverges in intent.

**Rank 3** · Comp = 0.760 · ✅ pass

> Among the novel orthomyxovirus-like (PB1-bearing) RNA viruses from diverse Chinese arthropods in the KM817593–KM817764 dataset, do the PB1 polymerase sequences from blood-feeding hosts (mosquitoes, louse flies) cluster phylogenetically with known vertebrate-infecting influenza-like viruses more closely than those from non-blood-feeding hosts (spiders, cockroaches, water striders), suggesting that orthomyxovirus-like lineages capable of vertebrate spillover preferentially evolved in hematophagous arthropods?
>
> *Rationale:* The candidate aligns well with GQ_001 by using arthropod PB1 sequences to test phylogenetic relationships to vertebrate influenza-like viruses and is strongly data-grounded, but it lacks explicit inquiry into basal lineages and genome/segment architecture.

**Rank 4** · Comp = 0.860 · ✅ pass

> Do novel RNA viruses from aquatic invertebrates (shrimp and crabs; Wenzhou Crab Virus 1-2, Wenzhou Shrimp Virus 1-2 in the KM817593–KM817764 dataset) encode glycoprotein (G) and nucleocapsid (N) sequences that are phylogenetically distinct from all known arthropod terrestrial RNA virus clades, suggesting that aquatic arthropod environments have harbored independent evolutionary radiations of negative-sense RNA viruses?
>
> *Rationale:* The candidate strongly matches GQ_001 by testing whether aquatic arthropod viruses form deep, distinct negative-sense clades with genomic gene evidence (G/N) and is well-grounded in specific accession data, but it does not explicitly state 'arthropod RNA-seq' nor focus on segmentation per se.

**Rank 5** · Comp = 0.646 · ✅ pass

> Among the 53 novel arthropod RNA viruses in the KM817593–KM817764 dataset for which only the RNA-dependent RNA polymerase (L gene) was sequenced, does the phylogenetic placement of their L gene sequences relative to the 17 viruses with complete multi-gene assemblies predict the gene architecture (number of ORFs, presence of glycoprotein) of the undescribed viruses, suggesting that L gene phylogeny alone is sufficient to infer genome complexity in this invertebrate virome?
>
> *Rationale:* The candidate closely matches GQ_002 by using L-gene (RdRP) phylogeny of novel arthropod viruses to infer genome architecture with strong dataset-specific grounding, but it omits explicit focus on segmented vs non-segmented transitions and phylogenetic gap-bridging.

### ✅ `gemini-3.1-pro` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 2 | 4 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 2 | 2 | 2 | 4 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.760 · ✅ pass

> What are the phylogenetic relationships and evolutionary divergence patterns among the diverse arthropod-borne RNA viruses in this dataset, based on the conserved regions of their nucleocapsid (N) genes and complete genomes?
>
> *Rationale:* Strong semantic match on phylogenetics and negative-sense virus ancestry with concrete file/sequence references; missing explicit 'arthropod RNA-seq' phrasing and mention of genome architecture/segmentation, so partial but solid alignment to GQ_001.

**Rank 2** · Comp = 0.240 · ❌ fail

> Are there conserved RNA secondary structural motifs within the untranslated regions (UTRs) of the complete viral genomes, such as Bole Tick Virus 3 and Changping Tick Virus 2, that indicate shared regulatory mechanisms across different arthropod host species?
>
> *Rationale:* The candidate is tightly data-grounded (specific FASTA and complete genomes) but asks about UTR secondary structure and regulatory motifs, which is semantically distinct from GQ_001's focus on arthropod RNA-seq, negative-sense virus ancestry, and genome architecture, so it is a poor match.

**Rank 3** · Comp = 0.391 · ❌ fail

> Does the dinucleotide frequency, specifically CpG depletion, vary significantly between the segmented genomes of Lishi Spider Virus 1 and the unsegmented genomes of the tick viruses, suggesting different host immune evasion pressures?
>
> *Rationale:* The question captures the segmented vs. unsegmented comparison but shifts to CpG/immune-evasion analysis and omits phylogenetic bridging, RdRP tree work, and explicit negative-sense virus framing required by GQ_002.

**Rank 4** · Comp = 0.440 · ❌ fail

> What is the extent of sequence homology and potential recombination events between the nucleocapsid (N) genes of viruses infecting different arthropod vectors, such as mosquitoes and ticks?
>
> *Rationale:* The candidate concerns arthropod virus evolution but centers on recombination of N genes, not the GQ_001 emphasis on arthropod RNA-seq recovering basal negative-sense lineages and genome architectures; it is data-grounded but semantically divergent.

**Rank 5** · Comp = 0.380 · ❌ fail

> Can we identify novel, unannotated open reading frames (ORFs) or overlapping genes within the complete genomes of the tick-borne viruses that share sequence similarity with known viral accessory proteins?
>
> *Rationale:* The candidate targets genome annotation within specific tick virus genomes (matching 'genome architecture') but lacks the gold's focus on arthropod RNA-seq sampling and phylogenetic inference of basal negative-sense virus lineages.

### ✅ `deepseek-v4-pro` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 3 | 5 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 2 | 2 | 3 | 4 | 4 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.374 · ❌ fail

> Do the nucleocapsid protein sequences of the tick-associated RNA viruses in this dataset form a monophyletic clade distinct from those of insect- and spider-associated viruses, or does phylogenetic signal follow geographic collection site rather than arthropod host order?
>
> *Rationale:* Mapped to GQ_002 because both concern arthropod-virus phylogenetics, but the candidate focuses on nucleocapsid clustering and geography versus host order and omits segmentation, negative-sense framing, and RdRP-based trees, though it is strongly grounded in the supplied FASTA and supplement.

**Rank 2** · Comp = 0.493 · ❌ fail

> Is there evidence of inter-segment reassortment among the multi-segmented arthropod viruses (e.g., Lishi Spider Virus, Wuchang Cockroach Virus) that would indicate past co-infection and genetic exchange within shared arthropod hosts?
>
> *Rationale:* The candidate is on-topic for GQ_002 (segmentation and phylogeny) and is well-grounded in specific GenBank accessions, but it focuses on reassortment within multi-segmented viruses rather than testing connections to non-segmented clades or using the RdRP/L-protein tree.

**Rank 3** · Comp = 0.220 · ❌ fail

> Do the glycoprotein genes of the arthropod-associated viruses show elevated rates of non-synonymous substitution in predicted receptor-binding domains compared to the nucleocapsid genes, consistent with host-driven diversifying selection?
>
> *Rationale:* The candidate studies gene-level selection in arthropod viruses, which is a different molecular-evolution question than GQ_001's phylogenetic/genome-architecture focus; it is well grounded in the provided fasta but misses all required elements of the matched gold.

**Rank 4** · Comp = 0.280 · ❌ fail

> Does codon usage bias in arthropod-associated RNA viruses reflect the tRNA pool of their known arthropod host species, and can this metric distinguish tick-adapted from insect-adapted viral lineages?
>
> *Rationale:* Mapped to GQ_001 because both concern arthropod-associated viruses, but the candidate focuses on codon usage/tRNA adaptation (host-level molecular ecology) rather than negative-sense virus phylogeny or genome architecture; it is grounded to one specific FASTA file.

**Rank 5** · Comp = 0.527 · ❌ fail

> Are there conserved amino acid motifs in the RNA-dependent RNA polymerase (RdRp) sequences that unite the unclassified arthropod viruses in this dataset with established families such as Phenuiviridae or Nairoviridae, enabling taxonomic placement of currently orphan viral sequences?
>
> *Rationale:* The candidate aligns with GQ_002's RdRp-centered phylogenetic/taxonomic intent (uses RdRp motifs and specific fasta entries) but omits explicit focus on segmentation and bridging gaps between segmented vs non-segmented negative-sense groups.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779596259_f8c4ae`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 2 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 2 | 3 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.306 · ❌ fail

> What is the genetic diversity and phylogenetic relationship among the viral sequences reported in the nuccore_reported_viral_sequences.fasta dataset?
>
> *Rationale:* The candidate is a generic phylogenetic question grounded in a specific FASTA file but lacks the GQ_002 focus on arthropod-derived, negative-sense viruses, segmentation, and RdRP-based phylogenies.

**Rank 2** · Comp = 0.220 · ❌ fail

> Are there specific genetic markers or motifs that are conserved or highly variable across different viral strains within the nuccore_reported_viral_sequences.fasta dataset?
>
> *Rationale:* The candidate studies conserved motifs in a nuccore fasta (concrete data grounding) but omits arthropod RNA-seq, negative-sense virus focus, basal lineages, segmentation and phylogenetic ancestry, so it poorly matches GQ_001.

**Rank 3** · Comp = 0.140 · ❌ fail

> Can the geographical origin or host range of the viruses be inferred from the strain names or sequence characteristics in the nuccore_reported_viral_sequences.fasta file?
>
> *Rationale:* The candidate is data‑grounded in a FASTA file and asks about host/geography from strain names, but it does not address arthropod RNA‑seq, negative‑sense viruses, or phylogenetic/genome‑architecture questions posed by GQ_001, so the semantic match is nil.

**Rank 4** · Comp = 0.100 · ❌ fail

> What is the distribution of genome lengths among the complete viral genomes present in the nuccore_reported_viral_sequences.fasta dataset?
>
> *Rationale:* The candidate targets sequence-length distribution in a nuccore FASTA and lacks all GQ_001 elements (arthropod RNA-seq, negative-sense viruses, basal lineages, segmentation, phylogenetic ancestry), so it does not match the gold question's intent.

**Rank 5** · Comp = 0.100 · ❌ fail

> Are there any indications of recombination events or gene transfer among the viral sequences in the nuccore_reported_viral_sequences.fasta dataset?
>
> *Rationale:* The candidate focuses on recombination in a provided fasta file and therefore is data-grounded, but it does not address any GQ_001 required elements (arthropod RNA-seq, negative-sense viruses, basal lineages, segmentation, or phylogenetic ancestry), so it is semantically unrelated.


---
## 3 · `bat_btcn_virome_2024`

- **数据**：5 文件 · 142,152,882 bytes · 例：43059583_BtCN-Virome_full_spectrum_contigs.tar.gz, 43059586_RdRp_motif_collection.xlsx, 43059592_CytB-COI-ITS.tar.gz
- **Gold 标注问题**：2
- **重复上传次数**：9 (upl_1779536266_ca7789, upl_1779545263_371ab1, upl_1779549037_9c1bea, upl_1779550675_a26b0e, upl_1779552724_fc0059, upl_1779554133_2bd4d5, upl_1779554290_54c659, upl_1779597870_7cf59a, upl_1779612969_bee81c)
- **已评测 agent**：7/7

### ✅ `claude-code-opus-4-7` · 取自 2 次跑数中分最高（rank-1 comp = 0.850, src = `upl_1779597870_7cf59a`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 5 | 4 | 5 | 3.740 | 0.748 | ✅ | GQ_002 (S) |
| 3 | 3 | 3 | 2 | 5 | 3.000 | 0.600 | ✅ | GQ_001 (P) |
| 4 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 5 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Which combination of long-term climatic variables (e.g., tas10, pr10, hurs10, vpd10, pet10) and land-use variables (e.g., nt, sl, gm, cy, bx) at the bat-roost scale most strongly predicts pool-level RNA virome richness (tvs) across Chinese bat families and tissue compartments, and does this climate-richness relationship differ for zoonotically relevant RdRp lineages (Coronaviridae, Bunyavirales, Mononegavirales) versus arthropod- and plant-borne lineages (Picornavirales, Stellavirales)?
>
> *Rationale:* The candidate precisely targets environmental and land-use predictors of bat RNA-virus richness, includes host and geographic scope, proposes statistical models, and references specific dataset variables and files, matching GQ_002 fully.

**Rank 2** · Comp = 0.748 · ✅ pass

> Do specific bat host families (Vespertilionidae, Rhinolophidae, Pteropodidae, Hipposideridae, Emballonuridae) and tissue compartments (intestine, lung, kidney, liver, brain) harbor phylogenetically distinct sub-clades of RdRp-defined RNA-virus orders, indicating host- and tissue-specific viral evolutionary trajectories within Chinese bats?
>
> *Rationale:* The candidate targets which host and tissue covariates explain viral phylogenetic composition using specific phylogenetic tests and named data files, matching GQ_002's ecological-modeling intent with strong data grounding.

**Rank 3** · Comp = 0.600 · ✅ pass

> Across the 13 RNA-virus orders represented in the BtCN-Virome ML phylogenies, how many candidate novel viral families and genera (defined by RdRp clades that are well-supported, separated from existing GenBank reference clades by deep branches, and lack any reference annotation) can be delineated, and what is their dominant Chiroptera host range?
>
> *Rationale:* Partial match to GQ_001: strong taxonomic and host-range focus with excellent data grounding (ML phylogenies, RdRp motifs, barcodes) but missing ecological-driver and human-settlement/circulation elements.

**Rank 4** · Comp = 0.760 · ✅ pass

> Within the BtCN-Virome contig set, what fraction of full-length and near-full-length contigs (>=5 kb) encode RNA-dependent RNA polymerases that contain noncanonical or permuted catalytic motif arrangements (e.g., the C-A-B permutation typical of Permutotetraviridae or atypical GDD/SDD substitutions), and which bat-host pools are these unusual polymerases concentrated in?
>
> *Rationale:* The candidate is a well-grounded, specific question about RdRp motif diversity and host-pool distribution in BtCN-Virome contigs, matching GQ_001's metatranscriptome and RNA-virus focus but missing explicit human-settlement circulation and broader ecological driver analysis.

**Rank 5** · Comp = 0.799 · ✅ pass

> Do bat-virome contigs that fall within plant- or arthropod-associated viral clades on the ML_Phylo trees (e.g., Picornavirales, Stellavirales, Sobelivirales, Tolivirales, Permutotetraviridae) co-occur in pools whose land-use covariates indicate higher cropland (cy), shrub (sy), or natural-vegetation (nt) cover, supporting a dietary or arthropod-vector route of acquisition rather than true bat infection?
>
> *Rationale:* The candidate precisely targets environmental/dietary predictors of viral composition and proposes a concrete regression analysis grounded in specified files, matching GQ_002 well; it omits an explicit geography element (e.g., spatial coordinates or regional framing).

### ✅ `gpt-5.5-high` · 取自 3 次跑数中分最高（rank-1 comp = 0.850, src = `upl_1779536266_ca7789`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 3 | 1 | 1 | 1 | 4 | 1.300 | 0.260 | ❌ | GQ_001 (P) |
| 4 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (U) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Which host-family, tissue, climate, and land-use variables are associated with higher BtCN bat RNA-virus richness and phylogenetic novelty across Chinese pooled samples?

**Rank 2** · Comp = 0.697 · ✅ pass

> Do intestinal bat pools contain higher RNA-virus richness than lung, liver, kidney, and brain pools after accounting for host family, sample size, and environmental covariates?

**Rank 3** · Comp = 0.260 · ❌ fail

> Which BtCN/VIRES RdRp lineages form the most distinct bat-associated clades relative to ZOVER-bat and EVRD/reference sequences across Picornavirales, Durnavirales, Mononegavirales, Reovirales, Tolivirales, and Ghabrivirales?

**Rank 4** · Comp = 0.799 · ✅ pass

> Are arthropod-, mollusk-, plant-, or bat-derived marker assignments from the full-spectrum contigs associated with differences in BtCN viral richness across pooled bat samples?

**Rank 5** · Comp = 0.120 · ❌ fail

> Do BtCN RdRp sequences preserve the expected conserved polymerase motifs across major RNA-virus groups, and where do motif deviations coincide with phylogenetically divergent VIRES clades?

### ✅ `claude-code-sonnet-4-6` · 取自 4 次跑数中分最高（rank-1 comp = 0.850, src = `upl_1779552724_fc0059`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 3 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 4 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 5 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Does landscape Shannon entropy (H10), by aggregating multiple bat host species in spatially heterogeneous habitats, predict elevated intestinal RNA virome species richness (tv) across Chinese bat communities independently of climate covariates (tas10, pr10, vpd10)?
>
> *Rationale:* The candidate precisely targets which environmental and host covariates explain intestinal RNA-virus richness and proposes a regression test with named variables and files, matching GQ_002 fully and grounded in the provided metadata.

**Rank 2** · Comp = 0.850 · ✅ pass

> Does bat co-occurring species diversity (btsm) mediate the relationship between landscape Shannon entropy (H10) and intestinal RNA virome richness (tv) in Chinese bat pools, consistent with a diversity-amplification mechanism rather than direct climate forcing?
>
> *Rationale:* The candidate is a highly specific ecological-modeling question that tests how environmental heterogeneity and host co-occurrence drive intestinal RNA-virus richness, specifying data sources and mediation/SEM methods, thus fully matching GQ_002.

**Rank 3** · Comp = 0.731 · ✅ pass

> Do Chinese bat pools dominated by Rhinolophidae host significantly higher RNA virome species richness (tvs) compared to other bat families (Vespertilionidae, Pteropodidae, Hipposideridae, Emballonuridae) after controlling for tissue type and climatic variables?
>
> *Rationale:* The candidate is a focused ecological-modeling question testing host-family and climatic predictors of RNA-virus richness with concrete metadata and statistical plan, matching GQ_002 well but omitting an explicit geographic covariate.

**Rank 4** · Comp = 0.460 · ❌ fail

> Can the conserved RdRp motif signatures (motifs A–G) catalogued in the reference collection be used to classify novel bat virome contigs from BtCN-Virome into known RNA virus orders, and what fraction of contigs belong to unclassified lineages with non-canonical motif combinations?
>
> *Rationale:* The candidate is a sequence‑classification question well grounded in provided motif and contig files, so it overlaps GQ_001 on RNA‑virus diversity and BtCN‑Virome mention but fails to address ecological drivers, human‑settlement circulation, and host/geographic context required by the gold question.

**Rank 5** · Comp = 0.850 · ✅ pass

> Does the species-level bat host identity inferred from chiroptera CytB and COI barcode sequences predict the taxonomic composition of co-associated RNA viromes in Chinese bat metagenomes more strongly than geographic location or sampling year?
>
> *Rationale:* The candidate precisely tests host vs geographic/temporal covariates for virome composition using barcode-derived host IDs and PERMANOVA on pool-level contig data, matching GQ_002 in scope and data grounding.

### ✅ `gemini-3.1-pro` · 取自 3 次跑数中分最高（rank-1 comp = 0.850, src = `upl_1779597870_7cf59a`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 5 | 3 | 5 | 4 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 4 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 5 | 4 | 5 | 5 | 5 | 3.910 | 0.782 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> How do host evolutionary relationships (inferred from CytB/COI/ITS barcodes) and environmental factors (from ecological metadata) interact to shape the diversity, distribution, and cross-species transmission networks of RNA viruses (identified via RdRp motifs) in Chinese bat populations?
>
> *Rationale:* The candidate fully addresses GQ_002 by combining host phylogeny, ecological metadata, RNA-virus identification (RdRp), and explicit statistical modeling to explain viral diversity and transmission across Chinese bat populations.

**Rank 2** · Comp = 0.400 · ❌ fail

> To what extent do the maximum likelihood phylogenies of bat hosts and their associated RNA viruses exhibit congruence, indicating long-term virus-host co-divergence versus frequent cross-species spillover events?
>
> *Rationale:* The candidate addresses host–virus evolutionary congruence (cophylogeny) using ML phylogenies, which is well-grounded in provided files but semantically diverges from GQ_001's ecological/metatranscriptome focus, so it only partially matches the gold question.

**Rank 3** · Comp = 0.731 · ✅ pass

> Which specific ecological variables from the metadata are the most significant predictors of RNA viral richness and the presence of specific viral clades within the Chinese bat virome?
>
> *Rationale:* The candidate precisely asks which ecological predictors drive viral richness/clade presence (full intent match), covers 4/5 required elements (missing host traits), closely matches an acceptable variant, and references the metadata and contig files for modeling (strong data grounding).

**Rank 4** · Comp = 0.460 · ❌ fail

> Can the analysis of full-spectrum virome contigs and RdRp motifs uncover novel, highly divergent RNA virus lineages that expand our understanding of viral evolution in bat reservoirs?
>
> *Rationale:* The candidate is strongly data-grounded and targets RNA-virus discovery from BtCN contigs and RdRp motifs, but it fails to address the ecological drivers, human-settlement circulation, and host/geographic details required by GQ_001.

**Rank 5** · Comp = 0.782 · ✅ pass

> Do specific geographic regions or ecological niches, as defined by the ecological modeling metadata, serve as hotspots for viral diversity and inter-taxa viral sharing among sympatric bat species?
>
> *Rationale:* Matches GQ_002 well: focuses on geography/environmental covariates and viral richness with explicit use of ecological metadata and modeling; well grounded in listed metadata and sequence files.

### ✅ `deepseek-v4-pro` · 取自 3 次跑数中分最高（rank-1 comp = 0.850, src = `upl_1779597870_7cf59a`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 3 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 5 | 5 | 4 | 5 | 5 | 3.995 | 0.799 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Does host phylogenetic distance, estimated from concatenated CytB-COI mitochondrial barcodes, predict the proportion of shared RNA virus operational taxonomic units (vOTUs) classified by RdRp palm-print motifs across sympatric bat species, after accounting for environmental niche overlap?
>
> *Rationale:* The candidate precisely targets which host and environmental covariates explain viral composition using concrete sequence and metadata files, matching GQ_002 fully and demonstrating strong data grounding and appropriate statistical framing.

**Rank 2** · Comp = 0.646 · ✅ pass

> Can machine learning classifiers trained on RdRp motif fingerprints and host barcode-derived ecological traits predict whether a bat species harbors Betacoronavirus-like contigs, and which features are most predictive?
>
> *Rationale:* The candidate aligns well with GQ_002 by proposing model-based identification of ecological covariates using specified data files, but it narrows scope to Betacoronavirus presence and omits geography and community-level richness/composition.

**Rank 3** · Comp = 0.799 · ✅ pass

> Does virome richness, measured as the number of distinct RdRp-classified viral families per bat individual, correlate positively with fungal community diversity inferred from ITS metabarcoding of guano or roost substrate samples?
>
> *Rationale:* This candidate narrowly, concretely tests an environmental covariate (ITS-inferred fungal diversity) against RdRp-defined virome richness using mixed models and named files, aligning well with the gold question about covariates explaining RNA-virus richness but omitting geography.

**Rank 4** · Comp = 0.340 · ❌ fail

> Is there significant co-phylogenetic congruence between bat host trees reconstructed from CytB-COI and RNA virus trees inferred from RdRp amino acid alignments, consistent with long-term host-virus co-divergence?
>
> *Rationale:* The candidate addresses host-virus evolutionary congruence (phylogenetics and co-divergence) rather than GQ_002's covariate-driven explanation of viral richness, so it only meets the statistical-model element but is well grounded in the supplied sequence/phylogeny files.

**Rank 5** · Comp = 0.799 · ✅ pass

> Do environmental gradients captured in the ecological modeling metadata — specifically temperature seasonality, precipitation, and land-use intensity — explain significant variation in RNA virome composition across bat sampling sites after controlling for host species identity?
>
> *Rationale:* The candidate precisely targets environmental covariates, host control, and explicit statistical tests to explain virome composition (strongly matching GQ_002); geography is implied by 'sampling sites' but not explicitly named.

### ✅ `glm-5` · src = `upl_1779612969_bee81c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 2 | 2 | 3 | 3 | 4 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 5 | 4 | 3 | 5 | 4 | 3.315 | 0.663 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.731 · ✅ pass

> How does RNA virus diversity, as characterized by RdRp motif variation, correlate with host species phylogenetic distance and ecological niche partitioning in bat communities?
>
> *Rationale:* The candidate strongly matches the ecological modeling intent of GQ_002 by targeting host phylogeny and ecological covariates and grounding the question in specific RdRp and metadata files, only omitting explicit geographic covariates.

**Rank 2** · Comp = 0.540 · ❌ fail

> What patterns of RdRp motif conservation and diversification exist across RNA virus families detected in bat viromes, and do these patterns indicate host-specific adaptive constraints?
>
> *Rationale:* The candidate is a molecular evolution question focused on RdRp motifs and host-specific adaptation; it uses BtCN virome and barcode files (good data grounding) but lacks the ecological/human-settlement scope required by GQ_001.

**Rank 3** · Comp = 0.520 · ❌ fail

> Can mitochondrial and nuclear barcode markers (CytB, COI, ITS) resolve bat species diversity and phylogeographic structure to inform viral reservoir identification?
>
> *Rationale:* The candidate addresses host barcode-based species delimitation and phylogeography relevant to reservoir ID, aligning partially with GQ_001's host/geography intent but omitting metatranscriptome and virus-diversity/ecological-driver elements; it cites specific dataset files.

**Rank 4** · Comp = 0.300 · ❌ fail

> How do machine learning phylogenetic methods compare to traditional approaches in resolving RNA virus evolutionary relationships from virome contig data?
>
> *Rationale:* The candidate is a computational phylogenetics benchmarking question that references specific files, so it is grounded in data but fails to address the ecological and human-exposure focus required by GQ_001.

**Rank 5** · Comp = 0.663 · ✅ pass

> What ecological and environmental factors predict viral richness and community composition in bat populations?
>
> *Rationale:* Strong semantic match to GQ_002: asks about predictors of viral richness/composition and cites specific metadata and virome files and statistical approaches, but omits explicit host-trait and geographic covariates.

### ✅ `gemini-2.5-flash` · 取自 3 次跑数中分最高（rank-1 comp = 0.578, src = `upl_1779597870_7cf59a`）

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 4 | 1.615 | 0.323 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.578 · ❌ fail

> How do environmental factors, as described in the ecological metadata, influence the genetic diversity and distribution of viral contigs and specific RdRp motifs within the studied ecosystem?
>
> *Rationale:* The candidate aligns with GQ_002's covariate→viral composition aim and cites specific files and modeling, but it omits host and geographic elements (mentions only environmental factors and 'studied ecosystem').

**Rank 2** · Comp = 0.323 · ❌ fail

> Can machine learning models, utilizing phylogenetic data, accurately predict the host range or ecological niche of novel viruses identified from the virome contigs?
>
> *Rationale:* The candidate is a predictive/phylogenetic modeling question grounded in provided contigs and ML/phylogeny files, but it does not ask about covariates, geography, or viral richness/composition required by GQ_002.

**Rank 3** · Comp = 0.476 · ❌ fail

> What is the phylogenetic relationship and evolutionary history of organisms based on the CytB, COI, and ITS markers, and how does this relate to the observed viral diversity?
>
> *Rationale:* The candidate focuses on host phylogeny as a predictor of viral diversity (matching GQ_002's covariate-driven aim) but omits environmental/geographic covariates and explicit statistical modeling, though it is well grounded in specific files.

**Rank 4** · Comp = 0.578 · ❌ fail

> Are there specific RdRp motifs that are consistently associated with particular environmental conditions or host types, as indicated by the ecological metadata and virome data?
>
> *Rationale:* Matches GQ_002's covariate-focused ecological modeling but at the genetic-motif level rather than virus richness/composition; covers host/environmental covariates and statistical testing and is well grounded in specific files.

**Rank 5** · Comp = 0.510 · ❌ fail

> What is the overall taxonomic and functional diversity of the virome, as inferred from the full-spectrum contigs, and how does this diversity compare across different ecological samples?
>
> *Rationale:* The candidate aligns with GQ_002's aim to explain variation in viral diversity across sampling contexts but is descriptive (diversity comparison) and lacks explicit covariate, geographic, host-trait, and modeling demands.


---
## 4 · `flavi_jingmen_jvi_2016`

- **数据**：1 文件 · 320,534 bytes · 例：nuccore_reported_viral_sequences.fasta
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779599288_208bd6)
- **已评测 agent**：6/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 2 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 3 | 4 | 5 | 4 | 5 | 4.400 | 0.880 | ✅ | GQ_001 (P) |
| 4 | 1 | 1 | 3 | 5 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 5 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.760 · ✅ pass

> Across the 18 invertebrate-associated RNA viruses in the KR902709-KR902741 panel, does host phylum/class (Insecta, Arachnida, Crustacea, Chilopoda, Chondrichthyes) systematically predict whether the virus has a four-segmented genome architecture versus a single large polyprotein-encoding genome, and is host-class also reflected in segment-length conservation and per-genome GC content?
>
> *Rationale:* The candidate tests host-class associations with segmentation, segment-length conservation, and GC% using concrete FASTA records (arthropods + shark), matching GQ_001's core intent though it omits explicit 'flavi-like/Flaviviridae' terminology and 'transcriptomes'.

**Rank 2** · Comp = 0.520 · ❌ fail

> Among the five fully-sequenced four-segmented arthropod RNA viruses in this panel (Wuhan cricket virus WHXS-1, Wuhan flea virus WHZM, Shuangao insect virus 7 SKC, Wuhan aphid virus 1 WHYC-1, Wuhan aphid virus 2 WHYC-2), is the per-segment length and GC-content profile sufficiently conserved to define a shared genome-architecture signature that could be used to assign newly discovered arthropod-associated contigs to the same viral lineage?
>
> *Rationale:* The candidate targets genome-architecture signatures among segmented arthropod viruses (matching the gold's genome-organization intent) but omits transcriptome-mining, explicit jingmenvirus/flavi-like labels, and Flaviviridae-evolution framing, while being strongly grounded in specific sequence accessions and numeric segment statistics.

**Rank 3** · Comp = 0.880 · ✅ pass

> Is Wenling shark virus (KR902729.1) compositionally and length-wise an outlier relative to the 17 invertebrate-associated polyprotein and segmented viruses in this panel, consistent with the hypothesis that the same superfamily of large polyprotein-encoding ssRNA viruses has crossed between invertebrate and vertebrate (Chondrichthyes) hosts?
>
> *Rationale:* The candidate targets host-range and Flaviviridae evolution using a concrete vertebrate (KR902729.1) vs invertebrate comparison and composition/length outlier tests, matching GQ_001's intent though at a narrower, single-sequence-analysis scale.

**Rank 4** · Comp = 0.360 · ❌ fail

> Do the two tick-associated viruses in this panel (Bole tick virus 4, BLP-1 and Tacheng tick virus 8, TCP-2) share elevated GC content and polyprotein length relative to other arachnid-associated viruses (Xinzhou spider virus 2 and 3, Shayang spider virus 4), suggesting that haematophagous tick ecology selects for distinct nucleotide composition compared with predatory spider ecology?
>
> *Rationale:* The candidate concerns compositional and polyprotein-length contrasts among known arachnid viruses (ticks vs spiders), so it is concrete and data-grounded but diverges from GQ_001's transcriptome-discovery and Flaviviridae/jingmenvirus focus.

**Rank 5** · Comp = 0.440 · ❌ fail

> Within each of the five fully-sequenced four-segmented arthropod RNA viruses, are the four segments codon- and composition-coupled (i.e. all four segments share the same GC content and dinucleotide profile) to a degree that distinguishes co-replicating segments from incidental contigs, providing a sequence-only criterion for assembling segmented genomes from metagenomic surveys?
>
> *Rationale:* Candidate studies composition coupling within four-segmented arthropod viruses (useful for assembly/binning) but does not address jingmenvirus/flavi-like identity, vertebrate data, or Flaviviridae evolutionary questions, though it is strongly grounded in specific accession- and per-segment metrics.

### ✅ `gpt-5.5-high` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 2 | 3 | 1 | 4 | 4 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 3 | 3 | 1 | 3 | 5 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 4 | 3 | 1 | 2 | 5 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 5 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.520 · ❌ fail

> Do the complete four-segment arthropod viral genomes in `nuccore_reported_viral_sequences.fasta` share a conserved segment-length and nucleotide-composition architecture that distinguishes them from the long polyprotein CDS viruses?
>
> *Rationale:* The candidate well targets genome-architecture differences in arthropod segmented genomes with strong file-level grounding, but it omits jingmenvirus/flavi-like framing, vertebrate/transcriptome context, and explicit Flaviviridae evolutionary claims.

**Rank 2** · Comp = 0.459 · ❌ fail

> Are the five complete four-segment viruses in `nuccore_reported_viral_sequences.fasta` consistent with a shared segmented RNA-virus lineage based on conserved segment number, segment-size ordering, and terminal nucleotide patterns?
>
> *Rationale:* The candidate aligns with GQ_002's genome-architecture intent (segment counts, ordering, termini) and is well-grounded in the nuccore fasta and named viruses, but it omits NS3/NS5 phylogenetic analysis and explicit comparison to unsegmented flavi-like relatives.

**Rank 3** · Comp = 0.520 · ❌ fail

> Do host-associated virus names in `nuccore_reported_viral_sequences.fasta` correspond to systematic differences in viral genome size, segmentation status, or GC content?
>
> *Rationale:* Matches GQ_001's host-vs-genome-organization intent but omits transcriptome-based discovery and explicit flavi-like/jingmenvirus/Flaviviridae framing; strongly grounded in the specific FASTA file and header fields.

**Rank 4** · Comp = 0.480 · ❌ fail

> Are the long polyprotein CDS viruses in `nuccore_reported_viral_sequences.fasta` separable into compositionally distinct groups that may reflect different viral lineages or host-associated evolutionary pressures?
>
> *Rationale:* The candidate is well grounded in the provided fasta and sequence statistics (high data grounding) and aims at lineage/host signals (partial intent match) but omits key Flaviviridae-specific elements and transcriptome framing, so required-element coverage and acceptability are low.

**Rank 5** · Comp = 0.220 · ❌ fail

> Can ambiguous nucleotides and compositional outliers in `nuccore_reported_viral_sequences.fasta` identify specific viral records that need targeted validation before comparative evolutionary analysis?
>
> *Rationale:* The candidate is a practical sequence-quality/validation question grounded in a FASTA file and specific records, but it does not address flavi-like/jingmenvirus discovery or Flaviviridae evolutionary questions required by the matched gold.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 4 | 4 | 2 | 3 | 5 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 5 | 1.700 | 0.340 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.700 · ✅ pass

> Do the four-segment genome-architecture RNA viruses (Wuhan cricket virus, Wuhan flea virus, Wuhan aphid virus 1, Wuhan aphid virus 2, Shuangao insect virus 7) exhibit significantly lower host-range breadth and higher between-segment GC covariation than the co-sampled polyprotein-encoding invertebrate RNA viruses (KR902729–KR902741), indicating that segmented genome organization imposes a co-packaging constraint that restricts cross-order host switching in invertebrate RNA virome evolution?
>
> *Rationale:* The candidate aligns with GQ_001's focus on segmentation-driven host-range and genome-evolution questions and is strongly data-grounded, but it omits explicit transcriptome/RNA-seq framing and the 'flavi-like/Flaviviridae' labels required by the gold question.

**Rank 2** · Comp = 0.540 · ❌ fail

> Is there a significant positive correlation between genome size and host phylogenetic diversity among the 13 polyprotein-encoding invertebrate RNA viruses (KR902729–KR902741), such that viruses with larger genomes (e.g., Gamboa mosquito virus at 26,315 bp; Xinzhou spider virus 2 at 24,521 bp) infect hosts from more diverse arthropod lineages than smaller-genome viruses (e.g., Wenling shark virus at 9,653 bp)?
>
> *Rationale:* The candidate aligns with GQ_001's host-range and genome-evolution theme and is well-grounded in FASTA entries, but it omits transcriptome-mining framing and explicit mention of jingmenvirus/flavi-like taxa required by the gold question.

**Rank 3** · Comp = 0.300 · ❌ fail

> Does the GC content of tick-associated RNA viruses (Bole tick virus 4: 56.1% GC; Tacheng tick virus 8: 44.1% GC) significantly exceed that of insect-associated RNA viruses from the same dataset (mean 41.5% GC), reflecting a host-driven nucleotide compositional bias linked to the tick cellular environment?
>
> *Rationale:* The candidate addresses host-associated GC composition across viruses (a different empirical question) and is data-grounded, but it does not target jingmenviruses, flavi-like viruses, or transcriptome-based discovery central to GQ_001.

**Rank 4** · Comp = 0.660 · ✅ pass

> Do the two aphid-infecting segmented RNA viruses, Wuhan aphid virus 1 (KR902721–KR902724) and Wuhan aphid virus 2 (KR902725–KR902728), share significantly greater nucleotide sequence identity across homologous segments than either does with the other co-sampled segmented viruses (Wuhan cricket virus, Wuhan flea virus, Shuangao insect virus 7), indicating recent host-restricted divergence within a single invertebrate host species rather than convergent host adaptation?
>
> *Rationale:* The candidate is a well-grounded, specific test of recent divergence among segmented (likely jingmen) aphid viruses, matching GQ_001's intent on segmented viruses and host-range/genome evolution but lacking explicit transcriptome/flavi-like framing.

**Rank 5** · Comp = 0.340 · ❌ fail

> Among the 13 non-segmented polyprotein RNA viruses in this dataset, does genome length correlate with the number of predicted open reading frames or functional domain complexity, and does the largest genome (Gamboa mosquito virus, 26,315 bp, KR902733) encode auxiliary replication or immune-evasion domains absent from the smallest polyprotein genome (Wenling shark virus, 9,653 bp, KR902729), consistent with nidovirus-like genome expansion driven by replication fidelity mechanisms?
>
> *Rationale:* The candidate is a genome-architecture question grounded in dataset accessions and lengths but does not address NS3/NS5 phylogenies, jingmenvirus/flavi-like relationships central to GQ_002, so it only weakly matches that gold question.

### ✅ `gemini-3.1-pro` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 1 | 2 | 5 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 2 | 2 | 2 | 2 | 4 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 4 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 5 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.408 · ❌ fail

> Does the Wuhan cricket virus strain WHXS-1 segment 1 encode a functional RNA-dependent RNA polymerase (RdRp) responsible for viral replication?
>
> *Rationale:* The candidate is a data-grounded, narrow test of whether segment 1 encodes an RdRp (matches the polymerase element of GQ_002) but omits the comparative phylogenetic and genome-architecture scope required by the gold question.

**Rank 2** · Comp = 0.440 · ❌ fail

> What are the structural proteins encoded by the Wuhan flea virus strain WHZM, and how do they compare to those of other known flea-borne viruses?
>
> *Rationale:* The candidate is a concrete, data-grounded question about a specific segmented flea virus' structural proteins, but it does not pursue the broader jingmenvirus/flavi-like evolutionary and transcriptome-mining scope central to GQ_001.

**Rank 3** · Comp = 0.500 · ❌ fail

> Is the multipartite genome organization of the Shuangao insect virus 7 strain SKC conserved across different insect host species?
>
> *Rationale:* Matches GQ_001 on segmented genome organization and host-range questions but is narrower (single virus, insects only) and lacks transcriptome/RNA-seq framing and explicit links to jingmen-/flavi-like viruses or Flaviviridae evolution.

**Rank 4** · Comp = 0.374 · ❌ fail

> What is the evolutionary relationship between Wuhan aphid virus 1 and Wuhan aphid virus 2 based on their genomic sequences?
>
> *Rationale:* The candidate is a narrow phylogenetic comparison of two Wuhan aphid virus strains with explicit sequence accessions, so it matches GQ_002 only on phylogeny (and RdRp/NS5) but misses the core jingmenvirus/flavi-like and segmentation scope.

**Rank 5** · Comp = 0.357 · ❌ fail

> Do the different segments of the Wuhan cricket virus strain WHXS-1 exhibit distinct evolutionary rates or selective pressures?
>
> *Rationale:* The candidate is a focused selection-analysis question on WHXS-1 segments grounded in provided FASTA accessions, but it does not perform the NS3/NS5 phylogeny or explicit segmented-vs-unsegmented flavi-like comparisons required by GQ_002.

### ✅ `deepseek-v4-pro` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 4 | 3 | 3 | 5 | 3.600 | 0.720 | ✅ | GQ_001 (P) |
| 3 | 1 | 1 | 2 | 4 | 1.500 | 0.300 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 2 | 5 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 2 | 3 | 2.125 | 0.425 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.580 · ❌ fail

> Do the RNA-dependent RNA polymerase (RdRp) phylogenies of these novel arthropod viruses reveal host-order-level clustering consistent with long-term co-divergence, or do they show interleaving of viruses from different arthropod orders indicative of frequent cross-order host switching?
>
> *Rationale:* The candidate aligns with GQ_001's host-range/evolution focus but only partially: it tests RdRp phylogenies for co-divergence among arthropods and is well-grounded in specific accessions and the provided fasta, yet it omits explicit flavi-like/jingmenvirus and vertebrate-transcriptome elements.

**Rank 2** · Comp = 0.720 · ✅ pass

> Are there conserved terminal nucleotide motifs across the genome segments of these multi-segment arthropod viruses that suggest a shared ancestral packaging or replication mechanism despite divergent host ranges?
>
> *Rationale:* Good semantic fit to GQ_001 on segmentation, genome organization and host-range evolution, well grounded in the provided FASTA; misses transcriptome-mining angle and explicit 'flavi-like' terminology, so partial required-element coverage and mid-level acceptability.

**Rank 3** · Comp = 0.300 · ❌ fail

> Can codon usage bias patterns in these viral polyprotein genes statistically discriminate among the arthropod host orders, reflecting differential adaptation to host tRNA pools?
>
> *Rationale:* The candidate focuses on codon usage-driven host adaptation across arthropod orders (well grounded in listed fasta sequences) but does not pursue GQ_001's core aim of discovering or revising Flaviviridae host range/genome evolution via transcriptome mining, so semantic match is weak.

**Rank 4** · Comp = 0.459 · ❌ fail

> Is there evidence of inter-virus recombination or reassortment among the segmented genomes of co-circulating arthropod viruses sampled from overlapping geographic locations such as the Wuhan metropolitan area?
>
> *Rationale:* The candidate aligns with GQ_002 on using segment-level phylogenies for evolutionary inference but omits NS3/NS5 and comparisons to unsegmented flavi-like viruses, while being strongly grounded in specific Wuhan sequence data.

**Rank 5** · Comp = 0.425 · ❌ fail

> Do the predicted RNA secondary structures in the 3′ and 5′ untranslated regions of these novel viral genomes cluster by host taxonomy rather than by viral phylogeny, suggesting host-driven constraints on UTR folding?
>
> *Rationale:* Matched to GQ_002 because both interrogate phylogenetic signals versus other features, but the candidate emphasizes UTR structure and host-driven convergence and omits NS3/NS5 and explicit jingmenvirus/flavi-like scope.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779599288_208bd6`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 4 | 3 | 2.210 | 0.442 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.476 · ❌ fail

> What is the genetic diversity and phylogenetic relationship among the different segments of the 'Wuhan cricket virus', 'Wuhan flea virus', 'Shuangao insect virus 7', and 'Wuhan aphid virus' strains present in the dataset?
>
> *Rationale:* The candidate is a phylogeny-focused, data-grounded question about segments of named segmented viruses (from the fasta file), aligning partially with GQ_002 but lacking NS3/NS5 and explicit flavi-like/unsegmented comparisons.

**Rank 2** · Comp = 0.442 · ❌ fail

> Are there any conserved genomic regions or motifs across the different viral segments and strains, and what are their potential functional implications?
>
> *Rationale:* The candidate concerns genome organization and conserved motifs across segments (matching GQ_002's architecture focus) but omits NS3/NS5, explicit phylogenetic analysis, and mention of jingmen-/flavi-like taxa; it is grounded in the nuccore_reported_viral_sequences.fasta file. Scores reflect partial alignment, low required-element coverage, good acceptability, and concrete data grounding.

**Rank 3** · Comp = 0.459 · ❌ fail

> Do the different segments within each viral strain show evidence of reassortment or recombination events?
>
> *Rationale:* The candidate targets segment-level phylogenetic incongruence (reassortment/recombination) and references the fasta file, aligning partially with GQ_002's phylogeny/genome-architecture aim but missing protein-specific (NS3/NS5) and taxon-specific (jingmenvirus/flavi-like) elements.

**Rank 4** · Comp = 0.360 · ❌ fail

> What is the codon usage bias for the protein-coding regions predicted within these viral sequences, and how does it compare across different viral strains or segments?
>
> *Rationale:* Best match is GQ_001 because both concern viral genome evolution, but the candidate focuses on codon usage from nuccore sequences rather than discovering jingmen/flavi-like viruses in arthropod/vertebrate transcriptomes, so coverage is minimal though data grounding is concrete.

**Rank 5** · Comp = 0.180 · ❌ fail

> Can specific genetic markers or signatures be identified that differentiate between the 'Wuhan cricket virus', 'Wuhan flea virus', 'Shuangao insect virus 7', and 'Wuhan aphid virus' strains?
>
> *Rationale:* The candidate addresses strain-level marker discovery from a fasta of named insect viruses, which does not match GQ_001's transcriptome-driven, Flaviviridae/jingmenvirus evolutionary questions; it is, however, well grounded in the provided sequence file.


---
## 5 · `invertebrate_rna_virosphere_2016`

- **数据**：2 文件 · 14,116,622 bytes · 例：5905695_alignments_and_phylogenies.zip, 5905698_all_virus_genomes.fasta
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779600049_710827)
- **已评测 agent**：5/7

### 🟨 `claude-code-opus-4-7` — **未评测（待补）**

### ✅ `gpt-5.5-high` · src = `upl_1779600049_710827`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 2 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.820 · ✅ pass

> How do the uploaded viral genome records, when placed in the provided RdRp and structural-protein phylogenies, reshape known RNA-virus evolutionary relationships and reveal possible modular exchange between polymerase and structural genes?
>
> *Rationale:* The candidate strongly matches GQ_001's phylogenetic redefinition intent and is well grounded in the provided RdRp/structural files, but it fails to explicitly reference 'invertebrate transcriptomes', so coverage is high but not perfect.

**Rank 2** · Comp = 0.860 · ✅ pass

> Which RNA-virus groups gain the largest amount of phylogenetic diversity from the uploaded genome records relative to reference sequences in the provided RdRp alignments and trees?
>
> *Rationale:* The candidate aligns well with GQ_001 by using assembled genomes and RdRp phylogenies to quantify added RNA‑virus diversity and deep lineages, is tightly data-grounded, and only omits an explicit mention of 'invertebrate transcriptomes'.

**Rank 3** · Comp = 0.540 · ❌ fail

> Do host-like and geographic labels embedded in the viral genome headers correspond to clustering patterns in the provided RdRp phylogenies?
>
> *Rationale:* The candidate aligns with GQ_001's phylogenetic focus but narrows to host/geography label mapping and lacks the transcriptome/breadth/deep-lineage scope required by the gold question.

**Rank 4** · Comp = 0.561 · ❌ fail

> How does genome segmentation vary among the uploaded RNA-virus groups, and is segment composition associated with placement in RdRp phylogenies?
>
> *Rationale:* The candidate matches GQ_002's focus on genome architecture and segmentation and is well grounded in the provided FASTA and alignment files, but it does not address genome length or the explicit goal of pinpointing sequences needing manual curation.

**Rank 5** · Comp = 0.760 · ✅ pass

> Which uploaded viral genome records are the strongest candidates for deeply divergent novel RNA-virus lineages based on genome length, RdRp tree placement, and branch-length patterns?
>
> *Rationale:* The candidate robustly targets deep divergent RNA-virus lineages using genome and RdRp-tree evidence (well grounded in supplied FASTA and Newick files) but omits explicit invertebrate-transcriptome framing and broader 'virosphere breadth' language.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779600049_710827`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 4 | 2 | 1 | 3 | 5 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 5 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.580 · ❌ fail

> Do the RdRp-based and structural-protein-based phylogenies of invertebrate RNA viruses within the Tombus-Noda, Luteo-Sobemo, Hepe-Virga, Narna-Levi, Permutotetra, and Weivirus supergroups show topological incongruence consistent with ancient modular recombination events, as revealed by the paired trimmed alignments and PhyML trees in RdRp_versus_structural/?
>
> *Rationale:* The candidate is a well-grounded, phylogeny-focused question about module-specific incongruence (partial match to GQ_001) but omits key elements about transcriptome mining, assembled genomes, and redefining virosphere breadth.

**Rank 2** · Comp = 0.820 · ✅ pass

> Across the 22 RNA virus supergroups recovered from Chinese invertebrate metatranscriptomes, does host taxonomic breadth (number of distinct arthropod orders infected) correlate positively with supergroup phylogenetic diversity as measured by total RdRp tree branch length in the trimmed alignments?
>
> *Rationale:* The candidate is a well-grounded, specific test of diversity and phylogenetic signal from invertebrate-derived virus sequences (uses FASTA headers, RdRp trees, 22 supergroups) that aligns closely with GQ_001 but omits explicit focus on discovering novel deep lineages.

**Rank 3** · Comp = 0.820 · ✅ pass

> Do the four newly described RNA virus families (New-Weivirus, New-Qinvirus, New-Zhaovirus, New-Yanvirus) occupy phylogenetically intermediate positions between established supergroups in RdRp maximum-likelihood trees, supporting their origin through horizontal gene transfer or recombination between ancestral lineages?
>
> *Rationale:* The candidate closely matches the gold's phylogenetic intent—testing placement of novel virus groups in RdRp trees with strong file-level grounding—but is narrower (specific families) and omits explicit mention of invertebrate transcriptomes.

**Rank 4** · Comp = 0.440 · ❌ fail

> Do RNA virus supergroups infecting marine invertebrates (shrimp, crabs, barnacles) in the Beihai coastal samples show significantly higher within-supergroup nucleotide diversity in the RdRp gene compared to those from freshwater or terrestrial arthropods (mosquitoes, flies, spiders) sampled at Wuhan and Wenzhou?
>
> *Rationale:* Partial match: addresses invertebrate virus diversity using assembled genomes and RdRp alignments (well grounded in files), but it tests within-supergroup nucleotide diversity across habitats rather than redefining RNA-virosphere breadth, deep lineages, or performing phylogenetic reanalysis.

**Rank 5** · Comp = 0.731 · ✅ pass

> Is there evidence that negative-sense RNA virus genome segment lengths in the Bunya-Arena and Mono-Chu supergroups follow a trimodal distribution corresponding to the canonical large (RdRp), medium (glycoprotein), and small (nucleoprotein) segment classes, and do the newly discovered arthropod-associated members maintain this segmentation architecture?
>
> *Rationale:* Matches GQ_002's segmentation and architecture intent using FASTA-derived lengths and segment labels; lacks explicit request about manual curation required by the gold question.

### ✅ `gemini-3.1-pro` · src = `upl_1779600049_710827`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 4 | 4 | 4 | 3.600 | 0.720 | ✅ | GQ_001 (P) |
| 2 | 3 | 3 | 5 | 4 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 2 | 4 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 5 | 2 | 2 | 3 | 4 | 2.400 | 0.480 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.720 · ✅ pass

> What is the evolutionary relationship and evidence for shared ancestry or recombination between Astroviridae and Potyviridae, as suggested by the 'Astro-Poty' viral genomes?
>
> *Rationale:* The candidate aligns with GQ_001's phylogenetic/deep-lineage intent and is grounded in provided FASTA and alignment files, but is narrower and fails to mention the required invertebrate-transcriptome sampling frame.

**Rank 2** · Comp = 0.595 · ❌ fail

> Do the 'astro-like' and 'poty-like' viruses exhibit a conserved genome organization that bridges the gap between typical Astroviruses and Potyviruses?
>
> *Rationale:* The candidate matches GQ_002's focus on genome architecture using provided FASTA records and length examples, but it omits segmentation assessment and any explicit manual curation needs, so it partially fulfills the gold question.

**Rank 3** · Comp = 0.560 · ❌ fail

> Does the phylogenetic analysis of the 'Astro-Poty' group suggest a historical host jump between plants and animals?
>
> *Rationale:* The candidate aligns with GQ_001 on phylogenetic analysis and assembled genomes but lacks the invertebrate-transcriptome and broad RNA-virosphere/deep-lineage framing; it is well grounded in the provided FASTA and tree files.

**Rank 4** · Comp = 0.580 · ❌ fail

> Are there specific highly conserved motifs within the RNA-dependent RNA polymerase (RdRp) that are unique to the 'Astro-Poty' clade?
>
> *Rationale:* The candidate is a focused molecular question about RdRp motifs that connects to phylogenetic deep-lineage interests of GQ_001 but omits invertebrate-transcriptome framing and virosphere-scale breadth; it is well grounded in the provided alignment and genome files.

**Rank 5** · Comp = 0.480 · ❌ fail

> How much genetic diversity exists within the 'astro-like' and 'poty-like' viral populations sampled in this dataset?
>
> *Rationale:* The candidate is a narrower, population-level diversity question that uses the provided FASTA (covers assembled genomes and phylogenetic/distance analyses) but omits transcriptome context and the gold's focus on virosphere breadth/deep lineages, yielding moderate match and good data grounding.

### ✅ `deepseek-v4-pro` · src = `upl_1779600049_710827`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 3 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.820 · ✅ pass

> Do the chimeric invertebrate RNA virus groups Astro-Poty, Bunya-Arena, and Toti-Chryso represent genuine phylogenetic intermediates blurring established family boundaries, as evidenced by RdRp-based maximum-likelihood phylogenies and codon-aligned genome alignments?
>
> *Rationale:* The candidate closely matches GQ_001 by testing phylogenetic placement of invertebrate-assembled viruses using RdRp ML trees and provided alignments, but it is narrower (specific chimeric groups) and omits the explicit wording 'deep lineages.'

**Rank 2** · Comp = 0.540 · ❌ fail

> Does the phylogenetic clustering of invertebrate RNA viruses in this dataset correlate more strongly with host taxonomy than with geographic sampling location across the Beihai, Hubei, Wuhan, and Wenling sites?
>
> *Rationale:* Mapped to GQ_001 because both address phylogenetics of invertebrate RNA viruses; candidate is concrete and data-grounded but focuses on host vs geography rather than discovery of breadth or deep lineages, so it only covers some required elements.

**Rank 3** · Comp = 0.680 · ✅ pass

> Are there statistically significant differences in genome length and segment number between the Astro-Poty, Birna, Bunya-Arena, and Toti-Chryso viral groups, reflecting distinct genomic strategies among invertebrate RNA virus lineages?
>
> *Rationale:* Strong alignment with GQ_002: targets genome length, segmentation, and architecture using assembled FASTA headers and concrete tests; however it omits explicit mention of manual curation required by the gold question.

**Rank 4** · Comp = 0.578 · ❌ fail

> Do the RdRp and structural protein (Glycoprotein/Capsid) phylogenies show congruent topologies within the Bunya-Arena group, or is there evidence of reassortment among the segmented genome components?
>
> *Rationale:* The candidate targets segment-level phylogenetic incongruence in Bunya-Arena viruses (segmentation/architecture) and is well grounded in the provided FASTA and alignment/phylogeny files, but it doesn't address genome length or explicitly request manual curation.

**Rank 5** · Comp = 0.580 · ❌ fail

> Can conserved RNA secondary structure elements be identified in the untranslated regions of Astro-Poty virus genomes, and do these structures show evidence of purifying selection across divergent host-associated lineages?
>
> *Rationale:* The candidate is a specific, data-grounded evolutionary question about UTR structural conservation in assembled Astro-Poty genomes across invertebrate hosts, matching the phylogenetic/evolution intent of GQ_001 but lacking the broader virosphere breadth/deep-lineage framing.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779600049_710827`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 3 | 3 | 1.700 | 0.340 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 4 | 3 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 3 | 1.800 | 0.360 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What is the genetic diversity and phylogenetic relationship among the viruses represented in the 5905698_all_virus_genomes.fasta dataset?
>
> *Rationale:* Matches GQ_001's diversity + phylogeny focus via the provided FASTA and alignments but omits the key invertebrate-transcriptome scope and explicit goal of redefining deep RNA virosphere lineages.

**Rank 2** · Comp = 0.340 · ❌ fail

> Are there conserved genomic regions or specific genetic markers present across different viral genomes in the dataset?
>
> *Rationale:* Mapped to GQ_002 because both focus on genome-level features of assembled viral genomes, but the candidate targets conserved regions/markers rather than segmentation, architecture, length, or the need for manual curation, so coverage is limited.

**Rank 3** · Comp = 0.493 · ❌ fail

> What is the distribution of genome lengths among the viruses in the 5905698_all_virus_genomes.fasta file, and does it correlate with viral classification?
>
> *Rationale:* Matches GQ_002: focuses on genome lengths in the provided FASTA (covered), but misses segmentation, architecture context, and the manual curation aspect; grounded to the specific fasta file.

**Rank 4** · Comp = 0.360 · ❌ fail

> Can novel or uncharacterized viral sequences be identified within the 5905698_all_virus_genomes.fasta dataset by comparing them to known viral databases?
>
> *Rationale:* The candidate targets novel-virus discovery in a named fasta (matches discovery theme) but omits invertebrate-host context, RNA-virosphere scope, and phylogenetic/deep-lineage framing central to GQ_001, so it only partially aligns and is grounded to the provided file.

**Rank 5** · Comp = 0.360 · ❌ fail

> What is the prevalence of specific viral families or genera within the 5905698_all_virus_genomes.fasta dataset, based on sequence annotation?
>
> *Rationale:* The candidate is a taxonomy/prevalence question grounded in a specific FASTA file but omits the invertebrate, deep-lineage, and phylogenetic scope required by the matched gold question.


---
## 6 · `oyster_rna_virome_2024`

- **数据**：6 文件 · 676,853 bytes · 例：40168_2024_1967_MOESM1_ESM.xlsx, 40168_2024_1967_MOESM2_ESM.xlsx, 40168_2024_1967_MOESM3_ESM.xlsx
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779601405_a8a4e0)
- **已评测 agent**：5/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779601405_a8a4e0`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 5 | 5 | 4.600 | 0.920 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 4 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 5 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.920 · ✅ pass

> Which RdRp-defined RNA-virus lineages in the Magallana gigas virome are persistent, oyster-resident infections — distinguishable by simultaneously high covered-fraction and TPM across the 16 longitudinal Luchao batches and detection in Magallana hongkongensis — versus transient, environmentally acquired signals shared with Yangshan harbour seawater or with co-sampled non-oyster mollusks?
>
> *Rationale:* The candidate closely matches GQ_001 by using RdRp contigs and read-mapping (covered-fraction, TPM) across oyster and non-oyster libraries plus seawater to test resident versus shared/transient viruses, and is well grounded in the provided MOESM files.

**Rank 2** · Comp = 0.493 · ❌ fail

> Do the 16 longitudinal Magallana gigas batches collected at Luchao Port between June 2016 and July 2017 reveal seasonal abundance dynamics for individual RdRp lineages — particularly within the dominant Marnaviridae (≈44% of contigs) — that are consistent with temperature- or spawning-driven proliferation in oyster aquaculture?
>
> *Rationale:* Candidate aligns well with RdRp abundance analysis in oysters using MOESM1/2/5, but omits novelty and explicit indicator/marine-circulation framing required by GQ_002.

**Rank 3** · Comp = 0.527 · ❌ fail

> How many of the 154 oyster-assembled RdRp ORFs represent novel RNA-virus species or genera at established RdRp percent-identity and bitscore thresholds, and how is this novelty distributed across the nine viral orders/families separately phylogenied in MOESM5?
>
> *Rationale:* The candidate precisely asks about RdRp novelty and lineage-resolved counts (well grounded in MOESM3/MOESM5) but omits abundance, indicator value, and marine-circulation aspects required by GQ_002.

**Rank 4** · Comp = 0.940 · ✅ pass

> Which oyster RdRp lineages are shared between Magallana gigas (Luchao Port, Shanghai) and Magallana hongkongensis (Lianjiang, Beihai, Shenzhen, Tanwei in southern China), and does this overlap form a Magallana-specific 'core virome' distinct from the broader mollusc and seawater pool?
>
> *Rationale:* The candidate tightly addresses RdRP-based sharing between oyster species and contrasts that overlap with mollusc/seawater pools, cites sheet-level TPM/covered-fraction and prevalence flags in MOESM2, but does not explicitly state 'digestive-tissue' metatranscriptomes.

**Rank 5** · Comp = 0.640 · ✅ pass

> Among the 156 oyster RNA-virus contigs, do the 40 'Dominant (>90% coverage)' contigs preferentially come from RNA-virus families known to infect eukaryotic invertebrates (Marnaviridae, Picornavirales, Nodaviridae) versus families that typically infect microbial or fungal hosts in mollusc microbiomes (Narnaviridae, Partitiviridae, Fiersviridae)?
>
> *Rationale:* The candidate aligns with GQ_001's focus on oyster virome composition and uses coverage/read-mapping evidence, but it omits RdRP-focused and seawater-sharing/network elements required by the gold question.

### 🟨 `gpt-5.5-high` — **未评测（待补）**

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779601405_a8a4e0`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 3 | 4 | 5 | 4.200 | 0.840 | ✅ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 3 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 4 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 5 | 2 | 1 | 3 | 5 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.840 · ✅ pass

> Do the high-abundance Marnaviridae and Picobirnaviridae RNA viruses detected in Yangshan harbor seawater serve as the environmental reservoir driving persistent, near-universal infection of Magallana gigas at Luchao Port across 13 months of seasonal sampling?
>
> *Rationale:* The candidate tightly matches the oyster–seawater virus-sharing intent with strong dataset grounding and temporal scope, but it omits explicit RdRP/palm-domain sequence evidence and only implicitly addresses virome diversity.

**Rank 2** · Comp = 0.493 · ❌ fail

> Are the 39 highly divergent RNA virus contigs (best RdRp amino-acid identity <50% to known references) in Magallana gigas phylogenetically novel enough to represent new species or genera within the nine RNA virus orders documented in this study?
>
> *Rationale:* The candidate strongly targets RdRP-based novelty and species demarcation with concrete file references, but it omits abundance/indicator and marine-circulation components central to GQ_002.

**Rank 3** · Comp = 0.578 · ❌ fail

> Do specific RNA virus families, particularly Marnaviridae and Picobirnaviridae, exhibit host-generalist distributions across ecologically diverse mollusks (bivalves, gastropods, cephalopods) from multiple Chinese coastal and freshwater sites, and does cross-host prevalence predict higher viral abundance within Magallana gigas?
>
> *Rationale:* The candidate aligns with GQ_002 on abundance and indicator value and is strongly grounded in MOESM2 spreadsheet evidence, but it omits explicit RdRP and novelty components required by the gold question.

**Rank 4** · Comp = 0.760 · ✅ pass

> Does the individual-level variability in Marnaviridae RNA abundance (coefficient of variation >2 across 17 oyster libraries) reflect stochastic viral acquisition from seawater rather than stable, heritable endogenous infection in Magallana gigas?
>
> *Rationale:* The candidate aligns with GQ_001's seawater–mollusk sharing/network intent using 17 oyster metatranscriptomes and TPM/CV evidence, but is narrower (taxon-specific) and omits explicit RdRP/palm-domain and broad virome framing.

**Rank 5** · Comp = 0.440 · ❌ fail

> Is the RNA virome composition of Magallana gigas at Luchao Port, Shanghai, dominated by a core set of fewer than five viral contigs that consistently account for over 80% of total viral RNA expression (TPM) across all 16 monthly sampling batches spanning June 2016 to July 2017?
>
> *Rationale:* The candidate asks a specific, well-grounded abundance/dominance question about oyster viral contigs but misses GQ_001's emphasis on RdRP/palm-domain discovery and seawater/mollusk sharing, so it only partially matches the primary intent.

### ✅ `gemini-3.1-pro` · src = `upl_1779601405_a8a4e0`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 2 | 1 | 3 | 4 | 1.785 | 0.357 | ❌ | GQ_002 (S) |
| 3 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 4 | 3 | 1 | 3 | 3 | 2.400 | 0.480 | ❌ | GQ_001 (P) |
| 5 | 3 | 1 | 2 | 4 | 2.300 | 0.460 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.560 · ❌ fail

> What is the phylogenetic diversity and evolutionary relationship of the novel RNA viruses identified in this dataset compared to known viral lineages?
>
> *Rationale:* The candidate focuses on phylogenetic diversity using RdRp sequences from the provided FASTA (matches GQ_001's diversity/RdRp elements) but omits explicit oyster digestive-tissue framing and the mollusk–seawater sharing/network and read-mapping evidence required by GQ_001.

**Rank 2** · Comp = 0.357 · ❌ fail

> How does the relative abundance of these viral contigs vary across different samples or environmental conditions?
>
> *Rationale:* Captures only the abundance aspect of GQ_002 and is grounded in two provided Excel files, but omits RdRP, novelty, indicator framing, and explicit marine-circulation scope.

**Rank 3** · Comp = 0.500 · ❌ fail

> What are the predicted host ranges or ecological niches of the identified RNA viruses?
>
> *Rationale:* The candidate captures the host-sharing/network aspect of GQ_001 but is missing explicit oyster metatranscriptome framing, RdRP evidence, and read-mapping/network data; it is grounded by cited supplement files.

**Rank 4** · Comp = 0.480 · ❌ fail

> Are there specific functional domains or accessory genes conserved among these viral contigs beyond the core RdRp?
>
> *Rationale:* Candidate centers on domain architecture beyond RdRp and links to the FASTA sequences, matching GQ_001's RdRp focus but missing the metatranscriptome, diversity, sharing/network, and read-mapping elements.

**Rank 5** · Comp = 0.460 · ❌ fail

> Does the taxonomic classification of these viral contigs align with their phylogenetic placement based on the RdRp gene?
>
> *Rationale:* GQ_001 was chosen because the candidate centers on RdRp phylogeny and viral contigs; it partially matches but omits oyster-specific samples, sharing/network analysis, and virome diversity, covering only the RdRp element though it is well grounded in supplemental files.

### ✅ `deepseek-v4-pro` · src = `upl_1779601405_a8a4e0`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 2 | 5 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 1 | 4 | 1.700 | 0.340 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 4 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 5 | 1 | 1 | 2 | 5 | 1.360 | 0.272 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.391 · ❌ fail

> Do gut phage-encoded auxiliary metabolic genes (AMGs) involved in nucleotide scavenging and carbon metabolism show differential abundance patterns between healthy and dysbiotic human gut metagenomic samples as captured in the k141 contig catalogue?
>
> *Rationale:* The candidate shares the indicator/abundance intent of GQ_002 but targets human gut phage AMGs (not RdRP RNA viruses), lacks novelty/marine-circulation elements, yet is strongly grounded in specific MOESM files and data features.

**Rank 2** · Comp = 0.340 · ❌ fail

> What is the taxonomic composition and host-range distribution of the viral community represented by the k141 metagenomic contigs, and does viral lineage diversity correlate with sample metadata variables such as age, diet, or disease status?
>
> *Rationale:* The candidate is a general virome/taxonomy question grounded in provided FASTA and spreadsheets but misses the oyster-digestive-tissue and seawater-sharing focus of the matched gold, so it partially aligns only via RdRp presence.

**Rank 3** · Comp = 0.140 · ❌ fail

> Can complete or near-complete phage genomes be assembled from the k141 contig catalogue, and do their genome architectures (gene order, genome size, GC content) cluster by predicted bacterial host phylum?
>
> *Rationale:* The candidate is about phage genome assembly and host-phylum clustering (unrelated to oyster RNA viromes), so match and required-element coverage are zero, acceptability is low, but data grounding is high due to explicit MOESM file references and numeric criteria.

**Rank 4** · Comp = 0.374 · ❌ fail

> Do RNA phage (Leviviricetes) contigs identified in the k141 dataset via their characteristic single-subunit RdRp sequences exhibit distinct abundance dynamics or sample prevalence compared to DNA phage contigs across the sampled conditions?
>
> *Rationale:* GQ_002 best matches because both involve RdRP-bearing viruses and prevalence/abundance, but the candidate studies gut RNA phages vs DNA phages rather than novel oyster RdRP viruses as marine indicators, so semantic alignment is limited; grounding in MOESM files is strong.

**Rank 5** · Comp = 0.272 · ❌ fail

> Are there specific phage-encoded carbohydrate-active enzymes (CAZymes) in the k141 viral proteome, and does their abundance correlate with dietary fibre intake or short-chain fatty acid levels recorded in the host metadata?
>
> *Rationale:* Chose GQ_002 because both involve viral abundance and indicator-like questions, but the candidate is about phage CAZymes and host diet (gut/SCFA), not RdRP oyster viruses or marine circulation, so semantic overlap is minimal despite strong dataset grounding.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779601405_a8a4e0`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 2 | 4 | 0.800 | 0.160 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 4 | 2 | 1 | 2 | 3 | 1.530 | 0.306 | ❌ | GQ_002 (S) |
| 5 | 0 | 0 | 2 | 3 | 0.700 | 0.140 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.160 · ❌ fail

> What are the functional annotations and potential biological pathways associated with the proteins identified in `40168_2024_1967_MOESM4_ESM.fa`, and how do these functions correlate with experimental conditions or observations detailed in the supplementary Excel files?
>
> *Rationale:* The candidate concerns protein functional annotation from a provided FASTA and correlations with Excel data, which is concrete and data-grounded but does not address the virome/RdRP/shared-network focus of the matched gold question.

**Rank 2** · Comp = 0.100 · ❌ fail

> Do the protein sequences in `40168_2024_1967_MOESM4_ESM.fa` exhibit significant sequence variation or evidence of post-translational modifications that might be linked to specific biological states or conditions?
>
> *Rationale:* The candidate is about protein sequences and PTMs in a specific FASTA file and thus does not address the RNA virome, RdRP evidence, or host–seawater sharing required by GQ_001, though it is grounded to the named file.

**Rank 3** · Comp = 0.220 · ❌ fail

> What is the evolutionary origin and conservation of the proteins encoded in `40168_2024_1967_MOESM4_ESM.fa` across different species or taxonomic groups?
>
> *Rationale:* The candidate addresses sequence-based evolutionary analysis of a provided FASTA but omits oyster-specific, RdRP/virome, sharing-network, and read-mapping elements central to GQ_001, so it is only marginally related by virtue of sequence data.

**Rank 4** · Comp = 0.306 · ❌ fail

> Are there any novel or uncharacterized protein sequences within `40168_2024_1967_MOESM4_ESM.fa` that do not have significant homology to known proteins in public databases?
>
> *Rationale:* The candidate targets sequence novelty in a specific FASTA, aligning weakly with GQ_002's novelty focus but omitting RdRP specificity, abundance, indicator value, and marine circulation required by the gold question.

**Rank 5** · Comp = 0.140 · ❌ fail

> What are the predicted structural features (e.g., transmembrane domains, signal peptides, secondary structure) of the proteins in `40168_2024_1967_MOESM4_ESM.fa`, and how might these features relate to their cellular localization or function?
>
> *Rationale:* The candidate is about protein structural predictions from MOESM4.fa and thus is unrelated to GQ_001's virome/network focus, though it does reference a specific FASTA file from the provided supplements.


---
## 7 · `rvmt_cell_2022`

- **数据**：1 文件 · 334 bytes · 例：RVMT_Zenodo_V4.zip.remote.json
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779604445_29adbe)
- **已评测 agent**：6/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 2 | 4 | 3 | 4 | 4 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 3 | 2 | 1 | 3 | 4 | 2.100 | 0.420 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 4 | 4 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.820 · ✅ pass

> In the RVMT V4 catalog, which environmental and host-community features (sample biome, prokaryotic vs. eukaryotic 16S/18S co-occurrence, latitude, and salinity) most strongly predict the presence of putative RNA bacteriophage clades (e.g., Lenarviricota-adjacent and the newly proposed phyla) versus eukaryote-infecting Riboviria, and do these predictors generalise across independent metatranscriptomic studies?
>
> *Rationale:* The candidate well matches GQ_001 by using RdRp-derived clusters and host co-occurrence across thousands of metatranscriptomes to evaluate RNA bacteriophage clades and is strongly grounded in the RVMT V4 files, but it omits explicit testing of a 'large expansion' of diversity.

**Rank 2** · Comp = 0.740 · ✅ pass

> Within the RVMT V4 RdRp-clustered species-like OTUs, what is the species-accumulation curve as a function of sequenced metatranscriptomic depth, and does the curve indicate that global RNA-virus diversity is approaching saturation or remains far from it for specific Riboviria phyla?
>
> *Rationale:* The candidate well targets RdRP-based, metatranscriptome-driven diversity estimation and saturation per phylum (matching GQ_001's core intent) but lacks explicit RNA-phage and host-association evidence required for a full match.

**Rank 3** · Comp = 0.420 · ❌ fail

> Across the RVMT V4 RdRp phylogeny, where on the tree do horizontal segment-reassortment or recombination breakpoints (detectable as RdRp/non-RdRp gene incongruence on the same contig) cluster, and do they preferentially occur at the boundaries between newly proposed phyla and the established five Riboviria phyla?
>
> *Rationale:* The candidate is RdRp-centered and well-grounded in RVMT V4 files but diverges from GQ_001's core intent of metatranscriptome-driven virome expansion and RNA-phage discovery, hence moderate alignment and strong data grounding.

**Rank 4** · Comp = 0.660 · ✅ pass

> Do RdRp protein sequences in RVMT V4 exhibit phylum-specific dinucleotide / codon-usage signatures that allow accurate inference of host kingdom (bacteria, archaea, fungi, plant, metazoan, protist) for the ~70% of contigs lacking direct host annotation?
>
> *Rationale:* Matches GQ_001 on RdRP-based host-evidence using RVMT V4 but misses the gold's emphasis on demonstrating a major virome expansion and specifically exposing RNA bacteriophage clades; well-grounded in dataset files for host-inference analysis.

**Rank 5** · Comp = 0.510 · ❌ fail

> Among RVMT V4 contigs that encode auxiliary metabolic or accessory genes alongside RdRp, which functional categories (e.g., translation factors, glycosyl hydrolases, photosynthesis genes) are over-represented in specific biomes, and what does this imply about RNA-virus contributions to host metabolism in those environments?
>
> *Rationale:* The candidate aligns with GQ_002 by using gene-content signals from RdRp-containing contigs to infer host-related functions, but it lacks CRISPR spacer evidence and an explicit prokaryotic-host association test, so it partially matches the gold intent.

### ✅ `gpt-5.5-high` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 3 | 3 | 4 | 4 | 3.300 | 0.660 | ✅ | GQ_001 (P) |
| 4 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 5 | 4 | 5 | 5 | 4 | 4.500 | 0.900 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.850 · ✅ pass

> Do CRISPR spacer matches and bacteriolytic protein domains across the RVMT RNA virus contigs show that major picobirnavirus and partitivirus lineages are prokaryote-infecting RNA bacteriophages rather than exclusively eukaryotic viruses?
>
> *Rationale:* Exact semantic match to GQ_002: the candidate tests CRISPR spacers and bacteriolytic gene content as host evidence for specified RNA-virus clades in the RVMT archive, covering all required elements and citing concrete dataset features.

**Rank 2** · Comp = 0.940 · ✅ pass

> How does mining 5,150 diverse metatranscriptomes reshape global RdRP phylogeny by expanding known RNA virus diversity five-fold and revealing two additional putative bacteriophage phyla?
>
> *Rationale:* The candidate faithfully captures GQ_001's scope—global metatranscriptome RdRP mining and large diversity expansion with putative RNA bacteriophage clades—and is well grounded in dataset-specific numbers, but it omits explicit host-association evidence (e.g., CRISPR/gene-content support).

**Rank 3** · Comp = 0.660 · ✅ pass

> Which metatranscriptome sources contribute disproportionately to the more than 2.5 million RNA virus contigs and more than 330,000 RdRPs recovered by the RVMT project?
>
> *Rationale:* The candidate focuses on which source categories drive the large RVMT discovery counts, matching GQ_001's discovery-scale intent but omitting RNA-phage and host-association components, and is well grounded in the Zenodo/RVMT counts cited.

**Rank 4** · Comp = 0.820 · ✅ pass

> Are novel protein domains in RVMT RNA virus contigs enriched in specific RdRP clades, indicating repeated acquisition of virus-host interaction functions across the expanded RNA virome?
>
> *Rationale:* The candidate aligns well with GQ_001 by leveraging RVMT RdRP clades and gene-content to probe virome-wide patterns, missing only explicit mention of RNA bacteriophage clades; it is well grounded in the provided RVMT/Zenodo metadata.

**Rank 5** · Comp = 0.900 · ✅ pass

> Does the expanded Lenarviricota catalog in RVMT account for roughly one third of RNA virome diversity because bacterial-associated lineages dominate newly recovered RdRP clades?
>
> *Rationale:* The candidate aligns with GQ_001 by using RVMT metatranscriptomes and RdRP evidence to link Lenarviricota expansion to bacterial-associated (phage) lineages; it's phylum-specific but includes required elements and is grounded in the Zenodo RVMT record.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 0 | 0.200 | 0.040 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 1 | 0.300 | 0.060 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 0 | 0.200 | 0.040 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 0 | 0.000 | 0.000 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.040 · ❌ fail

> Do specific agent governance architecture patterns — namely role-based tool isolation, constraint-aware corrective memory, and human-in-the-loop checkpoints — causally and additively improve target-level success rate and reproducibility in multi-step LLM-based drug discovery pipelines, as measured across a standardized multi-target benchmark spanning target identification, lead optimization, ADMET screening, and virtual docking?
>
> *Rationale:* Topically unrelated: the candidate is about LLM governance in drug discovery, while GQ_001 concerns global metatranscriptome RdRP mining for RNA-virus/phage discovery, so match and grounding scores are minimal.

**Rank 2** · Comp = 0.060 · ❌ fail

> Is there a systematic relationship between the number of agent architecture components (RAG, memory, reflection, multi-agent collaboration, tool governance) and reported task performance in LLM-based drug discovery systems, or do specific component combinations yield disproportionate gains relative to their individual contributions?
>
> *Rationale:* The candidate is about LLM agent architecture and performance in drug discovery, which is entirely different from the metatranscriptome/RNA-virus discovery intent of GQ_001; it contains none of the gold's required elements and is weakly grounded in the provided uploaded files.

**Rank 3** · Comp = 0.040 · ❌ fail

> Do LLM-based drug discovery agents that incorporate explicit audit trails and traceable execution logs achieve higher reproducibility and lower hallucination rates in multi-step pharmaceutical workflows than those relying solely on prompt-level self-reflection?
>
> *Rationale:* The candidate is about LLMs, audit trails, and reproducibility in drug discovery—entirely different from the virome/RdRP discovery focus of the gold question, so it fails to match or cover any required elements and lacks grounding in the provided data.

**Rank 4** · Comp = 0.000 · ❌ fail

> Across the corpus of LLM-based drug discovery agents published 2023–2026, is the proportion of systems with credible wet-lab experimental validation (as opposed to in-silico-only evaluation) increasing over time, and does the presence of wet-lab validation correlate with specific agent architecture patterns such as closed-loop design or HITL checkpoints?
>
> *Rationale:* The candidate concerns LLM drug‑discovery agents and wet‑lab validation trends, which is unrelated to the RNA‑virome metatranscriptome discovery question (GQ_001); it matches no required elements and cites no uploaded data files.

**Rank 5** · Comp = 0.000 · ❌ fail

> Does the use of RAG-enhanced retrieval with dynamic biomedical knowledge bases in multi-agent drug discovery systems, as instantiated in CLADD, GraPPI, and AgenticGraphRAGHepa, yield statistically significant improvements over static fine-tuned domain LLMs on drug property prediction, molecular captioning, and drug-target interaction tasks, and what retrieval granularity (molecule-level, pathway-level, literature-level) produces the largest gains?
>
> *Rationale:* The candidate addresses RAG-based retrieval and drug-discovery benchmarks, not RdRP/metatranscriptome-driven RNA-virus discovery or host-association evidence, so it fails to match GQ_001 on intent or required elements.

### ✅ `gemini-3.1-pro` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 2 | 4 | 2.600 | 0.520 | ❌ | GQ_001 (P) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 2 | 3 | 2.500 | 0.500 | ❌ | GQ_001 (P) |
| 4 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 5 | 3 | 1 | 2 | 3 | 2.200 | 0.440 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.520 · ❌ fail

> How does the inclusion of highly divergent environmental RNA virus sequences alter the deep branching order and inferred evolutionary origins of the major RNA virus phyla?
>
> *Rationale:* Mapped to GQ_001 because it concerns how novel environmental sequences reshape RNA-virus diversity and deep phylogeny; it captures diversity-expansion intent and cites RVMT files but omits explicit metatranscriptome mining, phage clade, and host-association evidence.

**Rank 2** · Comp = 0.560 · ❌ fail

> What is the frequency and phylogenetic distribution of alternative genetic codes among the newly discovered RNA virus lineages in the master tree?
>
> *Rationale:* The candidate aligns with GQ_001's use of large metatranscriptomes and host-related inference but shifts focus to alternative genetic codes and phylogenetic mapping rather than demonstrating RdRP-driven expansion or discovering RNA bacteriophage clades; it is well grounded to the RVMT file.

**Rank 3** · Comp = 0.500 · ❌ fail

> Do the evolutionary rates of RNA-dependent RNA polymerase (RdRp) sequences vary significantly across different viral phyla, and does this correlate with their inferred host domains?
>
> *Rationale:* The candidate shares RdRp and host-association elements with GQ_001 but asks about evolutionary rates across phyla rather than metatranscriptome-driven virome expansion or RNA-phage discovery; it is grounded in the RVMT tree file.

**Rank 4** · Comp = 0.510 · ❌ fail

> Can the phylogenetic clustering of uncharacterized environmental RNA viruses be used to accurately predict their ecological niches or host associations based on the metadata of closely related known viruses?
>
> *Rationale:* The candidate addresses predicting host/ecology via phylogeny and metadata, aligning with GQ_002's host-association intent but missing CRISPR/gene-content and explicit prokaryotic-host evidence, though it is grounded in the provided RVMT dataset.

**Rank 5** · Comp = 0.440 · ❌ fail

> What are the patterns of conservation and variation in the core catalytic motifs of the RdRp across the entire RNA virus megataxonomy, and do they reveal novel mechanisms of viral replication?
>
> *Rationale:* The candidate is an RdRp-focused, mechanistic conservation question that partially aligns with GQ_001's RdRp theme but omits metatranscriptome mining, virome expansion, phage discovery and host-evidence components.

### ✅ `deepseek-v4-pro` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 3 | 0.765 | 0.153 | ❌ | GQ_002 (S) |
| 4 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> Do Rift Valley fever virus lineages circulating in East Africa exhibit directional spatial diffusion along livestock trade corridors, as inferred from time-resolved phylogeographic analysis of whole-genome sequences?
>
> *Rationale:* The candidate concerns RVF phylogeography using whole genomes and trade-corridor hypotheses, which does not address GQ_001's metatranscriptome/RdRP-driven RNA virome expansion and RNA-phage discovery aims.

**Rank 2** · Comp = 0.100 · ❌ fail

> Are inter-annual fluctuations in Rift Valley fever outbreak intensity predictable from satellite-derived climate variables such as Normalized Difference Vegetation Index (NDVI) and sea-surface temperature anomalies in the Indian Ocean?
>
> *Rationale:* The candidate concerns climate-driven forecasting of Rift Valley fever using NDVI/SST and the RVMT archive, which is unrelated to the gold question about global RdRP-based metatranscriptome mining and RNA phage discovery.

**Rank 3** · Comp = 0.153 · ❌ fail

> Does host species identity (livestock vs. wildlife vs. human) predict clustering topology in the Rift Valley fever virus phylogeny, and can host-jump events be temporally mapped to periods of high vector abundance?
>
> *Rationale:* Candidate is a vertebrate-host phylogenetic question and not about CRISPR/gene-content evidence for prokaryotic RNA-phage hosts, so GQ_002 is the closest gold but alignment is poor; it does reference the provided RVMT file.

**Rank 4** · Comp = 0.100 · ❌ fail

> What is the relative contribution of cross-border importation versus local persistence in sustaining Rift Valley fever virus circulation across Kenya, Tanzania, and Uganda, as estimated by discrete phylogeographic ancestral state reconstruction?
>
> *Rationale:* Chose GQ_001 as the closest gold by broad viral topic, but the candidate is a phylogeography question about RVF in East Africa and does not address metatranscriptome/RdRP-based RNA virome expansion or RNA phage discovery; it is, however, grounded to a specific RVMT file.

**Rank 5** · Comp = 0.220 · ❌ fail

> Does within-outbreak genetic diversity of Rift Valley fever virus, measured as pairwise nucleotide diversity across whole-genome sequences, correlate with outbreak size as estimated from epidemiological incidence data?
>
> *Rationale:* The candidate is a distinct epidemiological/genomic question about intra-outbreak diversity of Rift Valley fever virus and does not address metatranscriptome-scale RNA virome discovery, so it only loosely matches GQ_001 by the general concept of viral diversity while missing required elements.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779604445_29adbe`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.100 · ❌ fail

> What is the intended scientific domain and purpose of the RVMT_Zenodo_V4 dataset, based on its metadata?
>
> *Rationale:* The candidate asks only about dataset metadata for RVMT_Zenodo_V4 and is unrelated to the RNA virome discovery goals of GQ_001; it contains no required elements but is concretely grounded in a specific metadata file.

**Rank 2** · Comp = 0.100 · ❌ fail

> What is the approximate size and format of the RVMT_Zenodo_V4 dataset, as indicated by its remote metadata?
>
> *Rationale:* The candidate is a dataset metadata question (size/format) tied to a specific remote JSON file, which does not address GQ_001's scientific intent about RdRP-based global RNA virome expansion or RNA phage discovery.

**Rank 3** · Comp = 0.100 · ❌ fail

> How does the checksum provided in the metadata ensure the integrity of the RVMT_Zenodo_V4 dataset?
>
> *Rationale:* The candidate concerns MD5/checksum metadata for RVMT_Zenodo_V4 (data integrity), which is unrelated to GQ_001's scientific intent about metatranscriptome RdRP mining and RNA-phage discovery; no required elements are present.

**Rank 4** · Comp = 0.280 · ❌ fail

> What are the implications of the RVMT_Zenodo_V4 dataset being a 'remote_archive_not_downloaded_by_default' for immediate research?
>
> *Rationale:* The candidate concerns dataset availability for RVMT_Zenodo_V4 (data-access issue) rather than scientific mining or host/virus discovery; it references one concrete metadata file but omits core scientific elements like RdRP mining and host-association evidence.

**Rank 5** · Comp = 0.280 · ❌ fail

> What steps would be required to access and utilize the full RVMT_Zenodo_V4 dataset for scientific analysis, given its current remote status?
>
> *Rationale:* The candidate is a practical data-access question about RVMT_Zenodo_V4 (file-level, status/reason fields) and does not pose the scientific hypotheses (RdRP mining, virome expansion, phage clades, host evidence) central to GQ_001.


---
## 8 · `tara_oceans_science_2022`

- **数据**：7 文件 · 44,987,932 bytes · 例：44779_RdRP_contigs.fna.gz, 5504_wcANI_based_clusters_90_80.fna.gz, RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779604899_60fa14)
- **已评测 agent**：5/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779604899_60fa14`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 5 | 5 | 5 | 3.910 | 0.782 | ✅ | GQ_002 (S) |
| 2 | 3 | 2 | 2 | 5 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 3 | 4 | 4 | 5 | 5 | 4.300 | 0.860 | ✅ | GQ_001 (P) |
| 4 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 5 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.782 · ✅ pass

> Which RNA-virus RdRp super-groups (Pfam classes RdRP_1–4, Mitovir_RNA_pol, Birna_RdRp, Bunya_RdRp, Mononeg_RNA_pol) are differentially enriched between surface (SUR), deep chlorophyll maximum (DCM), and mesopelagic (MES) Tara Oceans metatranscriptomes, and do the depth-enriched super-groups correspond to the near-complete RdRp centroids that fall outside known phyla (i.e., the proposed Taraviricota/Pomiviricota/Paraxenoviricota/Wamoviricota/Arctiviricota megataxa)?
>
> *Rationale:* Candidate aligns with GQ_002 by using Tara RdRP contigs/centroids and phylogenetic placement to test phylum-level taxonomy (proposed megataxa), is fully grounded in provided files/counts, and adds a depth-enrichment ecological angle consistent with the gold's intent.

**Rank 2** · Comp = 0.459 · ❌ fail

> Do the 5,028 vOTU annotations carrying a viral marker (|vir tag) show a non-random co-occurrence of RdRp-family hits with picorna-like capsid markers (Calici_coat, CRPV_capsid, Waikav_capsid_1, Dicistro_VP4) on the same contig, suggesting that long marine vOTUs preserve full Picornavirales-like genome architectures rather than being assembly artefacts?
>
> *Rationale:* Moderate match to GQ_002: uses marine RdRP-containing contigs with strong dataset grounding, but asks about RdRp–capsid co-occurrence/genome architecture rather than performing phylogenetic or taxonomic revision at phylum/class level.

**Rank 3** · Comp = 0.860 · ✅ pass

> How much of the marine RdRp diversity captured in the 209,588-sequence Tara+GenBank+Wolf2020 footprint set is novel relative to GenBank, as quantified by the fraction of the 13,109 50%-AAI centroids whose closest reference in REF_* sequences is below the 50% AAI threshold and which therefore define putative new RdRp clades?
>
> *Rationale:* The candidate tightly targets discovery of novel/divergent marine RdRPs using Tara footprints and 50%-AAI centroids (well grounded in files/numbers) but stops short of directly addressing impacts on early RNA-virus evolutionary structure.

**Rank 4** · Comp = 0.527 · ❌ fail

> Among the 5,504 wcANI-based vOTU representatives, does contig length (a proxy for genome completeness) predict the breadth of detectable functional domains per vOTU, and does this length-versus-domain-count relationship differ between Mitovir-like (capsid-less, mitochondrial) lineages and picorna-like (capsid-encoding) lineages?
>
> *Rationale:* Matches GQ_002 by comparing RdRP-defined marine lineages and using wcANI vOTUs, but lacks phylogenetic methods and any explicit taxonomy-revision aim; well grounded in specific files and annotations.

**Rank 5** · Comp = 0.850 · ✅ pass

> Are the 1,136 polar (ZZZ-coded) and 445 mixed-layer (MIX-coded) Tara contigs phylogenetically biased toward a specific RdRp super-group relative to non-polar SUR/DCM contigs, identifying a candidate cold-water-restricted RNA-virus clade consistent with the proposed Arctiviricota megataxon?
>
> *Rationale:* The candidate directly uses Tara RdRP contigs and phylogenetic placement to test a phylum-level (Arctiviricota) signal in polar vs non-polar samples, matching GQ_002's goal of evaluating high-level RNA-virus phylogeny using marine RdRPs and available files.

### 🟨 `gpt-5.5-high` — **未评测（待补）**

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779604899_60fa14`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 3 | 3 | 5 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 4.250 | 0.850 | ✅ | GQ_002 (S) |
| 4 | 3 | 2 | 4 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 5 | 3 | 2 | 2 | 5 | 2.295 | 0.459 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.560 · ❌ fail

> Do depth-layer gradients (surface vs. deep chlorophyll maximum vs. mesopelagic) predict the relative abundance of Picorna-like (RdRP_3) versus Birna-like (Birna_RdRp) RNA virus lineages among the 5,504 marine vOTUs from Tara Oceans and Tara Oceans Polar Circle metatranscriptomes, independent of geographic region?
>
> *Rationale:* The candidate aligns with GQ_001's use of Tara RdRP data but focuses on ecological depth distribution of known RdRP-defined lineages rather than discovering deeply divergent lineages or addressing evolutionary origins.

**Rank 2** · Comp = 0.940 · ✅ pass

> What fraction of the 5,504 vOTU clusters defined at 90% ANI / 80% coverage from Tara Oceans metatranscriptomes represent phylogenetically novel RNA virus lineages with no detectable homology to the 160,167 Genbank reference RdRP sequences, and are these novel lineages disproportionately associated with specific ocean depth layers or size fractions?
>
> *Rationale:* Strong semantic match to GQ_001: concrete RdRP-based novelty question grounded in Tara datasets and centroid/cluster files, but it omits explicit linkage to reshaping early RNA-virus evolutionary structure.

**Rank 3** · Comp = 0.850 · ✅ pass

> Do the 641 Tara Oceans vOTU contigs encoding both an RdRP domain and a structural capsid/coat protein represent sufficient genome completeness to resolve the host range and taxonomic affiliation of the five proposed novel RNA virus phyla (Arctiviricota, Taraviricota, Pomiviricota, Paraxenoviricota, Wamoviricota) described from these metatranscriptomes?
>
> *Rationale:* The candidate directly proposes phylogenomic tests using Tara RdRP-containing contigs to resolve phylum-level taxonomy for five novel phyla and cites specific uploaded files and counts, so it strongly matches GQ_002 in intent, coverage, acceptability, and data grounding.

**Rank 4** · Comp = 0.620 · ✅ pass

> Is the abundance and diversity of Mitovirus-like RNA polymerase (Mitovir_RNA_pol) sequences among the 44,779 Tara Oceans RdRP contigs consistent with persistent mitoviral infection of marine eukaryotic phytoplankton across all three depth layers (SUR, DCM, MES) and across tropical versus polar Tara Oceans sampling stations?
>
> *Rationale:* Partial match: the candidate strongly addresses RdRP-based abundance/diversity in Tara metatranscriptomes with concrete data grounding, but it does not target deep divergence or claims about reshaping early RNA-virus evolutionary structure.

**Rank 5** · Comp = 0.459 · ❌ fail

> Does the size-fraction origin of vOTU contigs (prokaryote-enriched fraction 1 vs. eukaryote-enriched fraction 2, as encoded in Tara Oceans sample identifiers) predict RdRP domain family composition in the functional annotation table, and can this be used to infer host kingdom (prokaryotic vs. eukaryotic) for the 5,504 marine RNA vOTUs?
>
> *Rationale:* Matches GQ_002 on use of marine RdRP data and Tara metadata but diverges in intent: focuses on host-kingdom inference via size-fraction and domain composition rather than phylogenetic or taxonomy-level revision.

### ✅ `gemini-3.1-pro` · src = `upl_1779604899_60fa14`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 2 | 3 | 1.100 | 0.220 | ❌ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 3 | 2 | 2 | 3 | 4 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 5 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 5 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.220 · ❌ fail

> How does the functional repertoire of marine RNA viruses differ between surface waters and the deep chlorophyll maximum?
>
> *Rationale:* The candidate asks a depth-based functional question about marine RNA viruses grounded in the functional-annotation-table, which is relevant to marine virology but does not address RdRP-driven discovery or deep evolutionary structure central to GQ_001.

**Rank 2** · Comp = 0.680 · ✅ pass

> What are the evolutionary relationships and major phylogenetic clades of the RNA viruses identified in the Tara Oceans dataset compared to known global viromes?
>
> *Rationale:* The candidate targets phylogenetic relationships of marine RdRP sequences from Tara Oceans and compares them to global viromes, matching GQ_002's focus on RdRP-based phylogenetics though it stops short of explicitly proposing formal taxonomy revision.

**Rank 3** · Comp = 0.408 · ❌ fail

> Which accessory protein domains most frequently co-occur with specific types of RNA-dependent RNA polymerases (RdRPs) in marine viral genomes?
>
> *Rationale:* The candidate uses marine RdRP contigs and specific files, aligning with GQ_002's RdRP focus but not its phylogenetic/taxonomic revision aim—covers 2/5 required elements and is well grounded in available tables and contig files.

**Rank 4** · Comp = 0.680 · ✅ pass

> What is the extent of sequence divergence and clustering among the newly assembled marine RNA viral contigs?
>
> *Rationale:* The candidate aligns with GQ_001's discovery/divergence aim by focusing on RdRP-containing contigs and diversity but lacks explicit global/Tara metatranscriptome framing and phylogenetic/evolutionary implications.

**Rank 5** · Comp = 0.280 · ❌ fail

> Are there distinct strand-coding biases for specific viral functional domains in the assembled marine RNA viromes?
>
> *Rationale:* The candidate is on the general topic of marine RNA viromes but shifts to genome organization/annotation (strand bias) rather than RdRP-based discovery or phylogenetic expansion, so it weakly matches GQ_001 while being well grounded in the functional-annotation-table.tsv.

### ✅ `deepseek-v4-pro` · src = `upl_1779604899_60fa14`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 2 | 5 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 3 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 3 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 4 | 2 | 3 | 3 | 4 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 5 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.459 · ❌ fail

> Do RNA-dependent RNA polymerase (RdRP) domain types encoded by marine RNA viruses exhibit statistically significant stratification in their relative abundance and phylogenetic diversity across surface (SRF), deep chlorophyll maximum (DCM), and mesopelagic (MES) depth layers in the Tara Oceans metatranscriptomes?
>
> *Rationale:* The candidate is a well-grounded Tara/RdRP question about depth stratification and phylogenetic diversity, aligning partially with GQ_002's RdRP/phylogeny focus but lacking explicit phylum/class-level taxonomy revision required by the gold.

**Rank 2** · Comp = 0.540 · ❌ fail

> Are mitovirus-like RdRP sequences (Mitovir_RNA_pol) proportionally more abundant in mesopelagic (MES) samples compared to surface (SRF) samples, consistent with a deep-ocean host association?
>
> *Rationale:* The candidate is a depth-stratified abundance test of mitovirus-like RdRPs grounded in functional-annotation-table.tsv (SRF/DCM/MES), matching GQ_001's RdRP/metatranscriptome focus but missing the core evolutionary/diversity discovery aims, so it's a partial match.

**Rank 3** · Comp = 0.400 · ❌ fail

> Do contigs annotated with multiple domains (e.g., helicase + RdRP + capsid) exhibit systematically higher annotation confidence scores than contigs bearing only a single RdRP domain, and does this signal more complete viral genome recovery?
>
> *Rationale:* The candidate is RdRP-focused and well-grounded in specific files/columns but asks about annotation confidence and genome completeness rather than the discovery of deeply divergent marine RNA-virus lineages, so it only partially matches GQ_001.

**Rank 4** · Comp = 0.459 · ❌ fail

> Does the phylogenetic composition of RdRP types differ significantly between the prokaryotic-fraction and eukaryotic-fraction metatranscriptomes from Tara Oceans sampling sites?
>
> *Rationale:* The candidate aligns with GQ_002's RdRP/phylogeny theme and uses Tara data, but it targets host-fraction composition rather than phylum-/class-level phylogenetic revision or taxonomy changes; it is well grounded in provided files.

**Rank 5** · Comp = 0.527 · ❌ fail

> Can the 5,504 wcANI-clustered vOTU representatives (5504_wcANI_based_clusters_90_80.fna.gz) be cross-referenced with their functional annotations to determine whether specific RdRP clades are associated with larger or more gene-rich contigs, suggesting distinct genome-size strategies among marine RNA virus lineages?
>
> *Rationale:* The candidate is a phylogenetically informed, data-grounded question about RdRP clades and genome-size associations in marine RNA viruses, but it does not target phylum/class-level taxonomy revision requested by GQ_002.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779604899_60fa14`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 3 | 5 | 3.200 | 0.640 | ✅ | GQ_001 (P) |
| 2 | 1 | 2 | 2 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 2 | 4 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.640 · ✅ pass

> What is the diversity and biogeographical distribution of RNA viruses, specifically those containing RdRP domains, across different Tara Oceans sampling sites?
>
> *Rationale:* The candidate aligns with GQ_001 on RdRP-centric analysis of Tara metatranscriptomes and geographic diversity with strong file/column grounding, but it omits searching for deeply divergent lineages and implications for early RNA-virus evolutionary structure.

**Rank 2** · Comp = 0.360 · ❌ fail

> What are the most prevalent functional domains, besides RdRP, found in the predicted protein sequences of marine RNA viruses from the Tara Oceans expeditions, and how do these domains co-occur?
>
> *Rationale:* The candidate is a concrete, data-grounded question about functional-domain prevalence in Tara annotations (covers dataset and RdRP mention) but does not ask about discovering divergent lineages or reshaping RNA-virus evolutionary structure, so it only weakly matches GQ_001.

**Rank 3** · Comp = 0.476 · ❌ fail

> How do the predicted 3D structures of RdRP proteins from novel megataxa compare to known RdRP structures, and what evolutionary insights can be derived from these comparisons?
>
> *Rationale:* The question aligns with GQ_002 by using RdRP footprints to draw evolutionary inferences, but it emphasizes 3D structural comparison rather than explicit phylogenetic/taxonomic revision and lacks explicit marine/taxonomy framing.

**Rank 4** · Comp = 0.391 · ❌ fail

> What is the genomic context of RdRP-containing contigs, specifically regarding the presence and arrangement of other functionally annotated genes within the same contig?
>
> *Rationale:* The candidate focuses on genomic context of RdRP contigs (well grounded in files/columns) but does not address phylogenetic or taxonomic revision at phylum/class levels required by GQ_002, so it only partially matches the gold intent.

**Rank 5** · Comp = 0.493 · ❌ fail

> How do the RdRP HMM profiles, built from RdRP footprint sequences, classify the RdRP domains identified in the functional annotation table, and what new RdRP types are identified?
>
> *Rationale:* The candidate is focused on classifying RdRP domains using Tara-derived footprints and HMMs (well grounded in files) but stops short of performing or asking for phylum/class-level phylogenetic revision required by GQ_002.


---
## 9 · `tick_metavirome_2023`

- **数据**：1 文件 · 11,888,536 bytes · 例：nuccore_reported_viral_sequences.fasta
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779607642_512c2c)
- **已评测 agent**：6/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 4 | 5 | 3.485 | 0.697 | ✅ | GQ_002 (S) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 4 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 5 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.697 · ✅ pass

> Within the 1,801 TIGMIC tick-derived metagenome-assembled sequences spanning 21 viral families and >30 Chinese sampling localities, which Nairoviridae- and Phenuiviridae-assigned contigs encode RdRp/L-segment ORFs that place phylogenetically sister to known human or livestock pathogens (e.g. CCHFV, SFTSV, Nairobi sheep disease virus), and how is that zoonotic-adjacent diversity geographically structured across the sampled Chinese sites?
>
> *Rationale:* The candidate closely matches GQ_002 by asking about phylogenetic placement relative to pathogens and geographic structuring with strong dataset grounding, but it omits explicit tick-species-level stratification required by GQ_002.

**Rank 2** · Comp = 1.000 · ✅ pass

> Across the 1,801 TIGMIC tick metagenome assemblies, can the bimodal genome-length distribution (mycovirus-like families Botourmia-/Narna-/Mito-/Partiti-/Totiviridae at ~1.8-7.4 kb mean vs. arthropod/vertebrate RNA-virus families Flavi-/Rhabdo-/Chu-/Nairoviridae at ~10.6-15.2 kb mean) be used to disentangle which viral lineages reflect the tick's fungal/protist microbiome versus genuine arthropod-replicating viruses?
>
> *Rationale:* Strong semantic alignment: the candidate uses extensive assemblies and family-level genome-length patterns to ask exactly which viruses are microbiome-associated versus tick-replicating, with rich dataset citation but substitutes 'metagenome' for 'metatranscriptome'.

**Rank 3** · Comp = 0.578 · ❌ fail

> Given that 282 of 362 distinct species labels in the TIGMIC FASTA are singletons and species names are constructed from Chinese-locality prefixes (e.g. 'Nanning Botou tick virus 1', 'Yanbian Nairo tick virus 2'), to what extent does viral-family community composition vary as a function of sampling locality, and is there a detectable latitudinal or climate-zone gradient in tick virome richness?
>
> *Rationale:* The candidate is a well-grounded, geographically focused virome-diversity question that aligns with GQ_002's regional/lineage aims but misses explicit tick-species and host-range components required by the gold question.

**Rank 4** · Comp = 0.700 · ✅ pass

> Among the 40 Flaviviridae and 20 Chuviridae contigs in the TIGMIC assembly set (mean lengths ~15.2 kb and ~10.9 kb respectively, several flagged 'complete genome'), are there candidate near-complete tick-borne flavivirus and chuvirus genomes whose predicted polyprotein architecture and 5'/3' UTR structures match the Tick-Borne Encephalitis serocomplex or Jingmenvirus group?
>
> *Rationale:* Targets discovery of near-complete tick RNA-virus genomes (Flaviviridae/Chuviridae) in TIGMIC assemblies with strong file/accession grounding, but lacks explicit broad tick-species sampling, host-range comparisons, and reservoir-level analysis.

**Rank 5** · Comp = 0.400 · ❌ fail

> Across the TIGMIC dataset, do the 101 'MAG UNVERIFIED' assemblies differ systematically from the 1,700 verified MAGs in length, family distribution, or proportion of singleton species labels, and what does that tell us about the reliability boundary of metagenomic viral discovery from pooled tick samples?
>
> *Rationale:* Candidate addresses viral genome quality in tick-derived assemblies (good data grounding) but diverges from GQ_001's core intents about metatranscriptomic breadth, host-range (specialist vs generalist), and reservoir structure, so it's a low semantic match.

### ✅ `gpt-5.5-high` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 5 | 2.000 | 0.400 | ❌ | GQ_001 (P) |
| 3 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 4 | 3 | 2 | 3 | 5 | 2.465 | 0.493 | ❌ | GQ_002 (S) |
| 5 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.561 · ❌ fail

> How much taxonomic and genome-feature diversity is captured in the reported TIGMIC tick-associated viral sequences, and which viral families or locality-named lineages account for the dominant complete-genome diversity?
>
> *Rationale:* The candidate aligns well with GQ_002 on lineage, geography, and genome-distribution analysis (hence moderate match), but it omits explicit tick-species and host-range questions required by the gold, while grounding claims in specific FASTA features.

**Rank 2** · Comp = 0.400 · ❌ fail

> Do the dominant family-level MAG labels such as Totiviridae sp., Botourmiaviridae sp., Narnaviridae sp., and Rhabdoviridae sp. represent internally coherent sequence groups with characteristic genome lengths and GC contents?
>
> *Rationale:* The candidate concerns internal coherence of family-level viral labels and sequence properties in a fasta file, which is about viral genomes but does not address ticks, sampling breadth, host-range categories, or reservoir structure central to the matched gold question.

**Rank 3** · Comp = 0.578 · ❌ fail

> Among the locality-named tick virus records, which Chinese locality tokens and abbreviated viral lineages show the greatest apparent richness in the reported TIGMIC sequence set?
>
> *Rationale:* The candidate targets geographic variation in viral-lineage richness within locality-named FASTA headers, aligning with GQ_002's geography and lineage aims but missing tick-species and host-range elements; it is well grounded in the provided FASTA counts and header tokens.

**Rank 4** · Comp = 0.493 · ❌ fail

> Are cRNA sequence annotations concentrated in negative-sense or segmented tick-virus groups compared with records annotated as genomic sequences or complete genomes?
>
> *Rationale:* The candidate best matches GQ_002 by addressing lineage-level genome distribution (cRNA vs genomic) with concrete counts, but it omits species, geography, and host-range elements required by the gold question.

**Rank 5** · Comp = 0.500 · ❌ fail

> Which repeated named viruses, including Dabieshan Tick Virus, Lihan tick virus, Wuhan mivirus, and Brown dog tick phleboviruses, show the greatest isolate-level nucleotide diversity across TIGMIC isolate identifiers?
>
> *Rationale:* The question addresses RNA-virus genome diversity for repeated taxa using the nuccore fasta and isolate IDs, so it partially matches GQ_001's genome focus but lacks the required tick-metatranscriptome, sampling breadth, host-range, and reservoir components.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 2 | 3 | 5 | 2.125 | 0.425 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 3 | 4 | 4 | 5 | 3.700 | 0.740 | ✅ | GQ_001 (P) |
| 4 | 4 | 4 | 5 | 5 | 3.655 | 0.731 | ✅ | GQ_002 (S) |
| 5 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.425 · ❌ fail

> Do tick pools (TIGMIC isolates) that harbor Phenuiviridae sequences show significantly higher co-occurrence rates with Nairoviridae, Flaviviridae, or Orthomyxoviridae sequences compared to pools lacking Phenuiviridae, indicating non-random co-vectoring of medically important tick-borne viruses across Chinese tick populations?
>
> *Rationale:* The candidate targets geographic and abundance distribution of viral families within pools and is tightly data-grounded, but it lacks the tick-species, host-range, and phylogenetic lineage comparisons central to GQ_002.

**Rank 2** · Comp = 0.527 · ❌ fail

> Does viral richness (number of distinct viral species per TIGMIC tick pool) correlate with the geographic latitude of the sampling city, suggesting a latitudinal gradient in tick virome diversity across China?
>
> *Rationale:* Candidate aligns with GQ_002 on geography and viral richness but omits tick-species, host-range, and phylogenetic lineage; well grounded in FASTA headers and reported counts, making it close to an acceptable regional-variation variant.

**Rank 3** · Comp = 0.740 · ✅ pass

> Are novel tick-associated Flaviviridae sequences recovered from Chinese TIGMIC pools more closely related to tick-borne encephalitis virus or to insect-specific flaviviruses based on genome length and sequence identity, clarifying their potential for vertebrate host spillover?
>
> *Rationale:* The candidate aligns with GQ_001's specialist vs generalist intent and is well grounded in specific Flaviviridae sequences, but it lacks the broad multispecies tick sampling (31 species) central to the gold question.

**Rank 4** · Comp = 0.731 · ✅ pass

> Do tick pools from Hulunbuir (northern steppe) versus Zhangzhou (southern coastal) harbor phylogenetically distinct viral communities, reflecting ecological and tick-species-driven divergence in virome composition?
>
> *Rationale:* The candidate is a geographically specific, species-aware test of phylogenetic and community-level virome differences, well aligned with GQ_002 except for missing host-range (generalist vs specialist) considerations.

**Rank 5** · Comp = 0.646 · ✅ pass

> Does the proportion of TIGMIC tick pools carrying Nairoviridae sequences vary significantly across Chinese geographic regions, and does this geographic risk structure align with known distribution of Crimean-Congo hemorrhagic fever virus-competent tick species?
>
> *Rationale:* The candidate is a geographically focused, data-grounded question about Nairoviridae prevalence and tick-species distribution, aligning well with GQ_002's emphasis on species and region but missing phylogenetic lineage and explicit host-range categorization.

### ✅ `gemini-3.1-pro` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 2 | 4 | 1.900 | 0.380 | ❌ | GQ_001 (P) |
| 3 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 4 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.561 · ❌ fail

> How does the geographic distribution of Botou tick virus isolates across different regions correlate with their genomic divergence and evolutionary history?
>
> *Rationale:* The candidate is a phylogeographic question aligned with GQ_002's geography and phylogeny focus, but it studies a single virus and omits tick-species and host-range, though it is well grounded in the provided fasta isolate headers.

**Rank 2** · Comp = 0.380 · ❌ fail

> Are there identifiable recombination events within the genomes of the different Phenuiviridae sp. isolates?
>
> *Rationale:* The candidate is a genome-focused, sequence-grounded recombination question that aligns weakly with the gold's genome theme but omits the key tick-sampling, host-range, and reservoir elements required by GQ_001.

**Rank 3** · Comp = 0.280 · ❌ fail

> What are the highly conserved genomic regions across the different isolates of the Wuhan mivirus?
>
> *Rationale:* The candidate is a narrow, sequence-level question about Wuhan mivirus conserved regions grounded in the fasta file, whereas the matched gold asks about broad tick metatranscriptomic sampling and reservoir-level RNA-virus diversity, so semantic overlap is minimal.

**Rank 4** · Comp = 0.544 · ❌ fail

> How do the genomic sequences of the 'Brown dog tick phlebovirus' isolates compare to other tick-borne phleboviruses in terms of gene content and arrangement?
>
> *Rationale:* The candidate aligns with GQ_002's comparative/phylogenetic aim and is well grounded in the provided FASTA (specific isolates named), but it omits geography and explicit host-range-category framing requested by the gold question.

**Rank 5** · Comp = 0.459 · ❌ fail

> What is the phylogenetic relationship of the 'Dabieshan Tick Virus' isolate TIGMIC_19 to other known tick-borne viruses in the dataset?
>
> *Rationale:* The candidate asks a focused phylogenetic question about one isolate using the provided viral sequences file, aligning partially with GQ_002's lineage focus but omitting species, geography, and host-range dimensions.

### ✅ `deepseek-v4-pro` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 3 | 3 | 3 | 4 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 3 | 2.295 | 0.459 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 2 | 3 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 5 | 3 | 4 | 4 | 4 | 3.060 | 0.612 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.561 · ❌ fail

> Do tick-associated viral communities assembled from metagenomes across different Chinese geographic regions exhibit phylogenetically clustered co-occurrence patterns that correlate with the geographic distance between sampling locations?
>
> *Rationale:* The candidate focuses on geographic and phylogenetic structuring of tick viromes and is well-grounded in the provided FASTA headers, but it omits tick-species and host-range dimensions required by GQ_002.

**Rank 2** · Comp = 0.527 · ❌ fail

> Does the completeness of metagenome-assembled viral genomes from tick samples vary systematically by viral family or by geographic region, and does this variation correlate with viral genome type (segmented vs. non-segmented)?
>
> *Rationale:* Moderate match to GQ_002: strong grounding and explicit lineage/geography focus, but missing tick-species and host-range elements required for full alignment.

**Rank 3** · Comp = 0.459 · ❌ fail

> Can phylogenetic analysis of Botou tick virus genomic sequences sampled from 13+ Chinese cities reveal signatures of recent geographic expansion, population structure, and lineage dispersal routes across China's major biogeographic barriers?
>
> *Rationale:* Matches GQ_002 on geography and phylogenetic lineage (phylogeography of Botou tick virus across China) but misses tick-species, host-range, and explicit abundance/genome-distribution elements; reasonably grounded to the provided fasta file.

**Rank 4** · Comp = 0.476 · ❌ fail

> Is there evidence of inter-viral family recombination or horizontal gene transfer among co-infecting tick-associated viruses as inferred from incongruent phylogenetic topologies or mosaic genome segments within the same TIGMIC isolate?
>
> *Rationale:* The candidate aligns partially with GQ_002 by focusing on phylogenetic incongruence and genome mosaics in co-infecting viruses and cites the fasta and TIGMIC isolates, but it omits explicit tick-species and host-range comparisons required by the gold question.

**Rank 5** · Comp = 0.612 · ✅ pass

> Do the nucleotide composition and codon usage patterns of tick-borne viral MAGs differ between viruses found in northern (Hulunbuir, Tonghua, Tianjin) versus southern (Nanning, Zhangzhou) sampling sites, and does this signal reflect host-adaptation or climate-driven mutational bias?
>
> *Rationale:* The candidate aligns with GQ_002 on geographic and host-range questions and uses sequence-level genomic features, but it does not explicitly address variation by tick species or viral abundance, making it a partial but specific match grounded in the provided fasta file.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779607642_512c2c`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 0 | 3 | 3 | 1.445 | 0.289 | ❌ | GQ_002 (S) |
| 2 | 3 | 1 | 3 | 3 | 2.040 | 0.408 | ❌ | GQ_002 (S) |
| 3 | 1 | 1 | 2 | 3 | 1.400 | 0.280 | ❌ | GQ_001 (P) |
| 4 | 3 | 1 | 2 | 3 | 2.200 | 0.440 | ❌ | GQ_001 (P) |
| 5 | 3 | 3 | 4 | 3 | 2.720 | 0.544 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.289 · ❌ fail

> What is the overall genetic diversity among the reported viral sequences in the dataset?
>
> *Rationale:* The question is a valid, data-grounded genetic-diversity query tied to the FASTA file but misses GQ_002's essential stratifiers (tick species, geography, host-range, phylogenetic/abundance context), so it only partially aligns with that gold question.

**Rank 2** · Comp = 0.408 · ❌ fail

> What are the phylogenetic relationships between the different viral sequences, and do they cluster into distinct groups?
>
> *Rationale:* Candidate targets phylogenetic analysis (matches GQ_002's lineage focus) but omits essential contextual elements (tick species, geography, host-range, abundance), and grounds itself in one specific FASTA file for sequence-based tree construction.

**Rank 3** · Comp = 0.280 · ❌ fail

> What is the distribution of genome lengths and GC content among the reported viral sequences?
>
> *Rationale:* The candidate targets sequence-level statistics from nuccore_reported_viral_sequences.fasta, matching only the 'RNA-virus genomes' aspect of GQ_001 and omitting tick sampling, host-range, and reservoir structure, so it is a weak semantic match.

**Rank 4** · Comp = 0.440 · ❌ fail

> Can specific viral families or genera be identified and characterized based on unique sequence motifs or highly conserved regions within the dataset?
>
> *Rationale:* The candidate aligns with the genome-discovery aspect of GQ_001 via sequence motif analysis using the provided fasta, but it omits all tick-specific sampling and reservoir/host-range elements, so it partially matches but is incomplete.

**Rank 5** · Comp = 0.544 · ❌ fail

> Do the viral sequence headers provide sufficient information to infer potential host organisms or geographical origins, and how does this correlate with genetic relatedness?
>
> *Rationale:* The candidate aligns with GQ_002 by probing geography, host-range, and phylogenetic correlation using FASTA headers, but it omits explicit comparison across tick species and lacks abundance/distribution elements.


---
## 10 · `vertebrate_rna_viruses_2018`

- **数据**：3 文件 · 144,766 bytes · 例：41586_2018_12_MOESM1_ESM.pdf, 41586_2018_12_MOESM2_ESM.xlsx, 41586_2018_12_MOESM3_ESM.xlsx
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779608619_39b5de)
- **已评测 agent**：6/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 4 | 4 | 5 | 4.500 | 0.900 | ✅ | GQ_001 (P) |
| 2 | 5 | 4 | 5 | 5 | 4.700 | 0.940 | ✅ | GQ_001 (P) |
| 3 | 2 | 2 | 2 | 5 | 2.300 | 0.460 | ❌ | GQ_001 (P) |
| 4 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.900 · ✅ pass

> To what extent do the phylogenies of vertebrate-associated RNA virus families recovered across the Chordata (Agnatha, Sarcopterygii, Actinopterygii, Chondrichthyes, Amphibia and Reptilia) — in particular Astroviridae, Picornaviridae, Caliciviridae, Hepeviridae, Hantaviridae, Arenaviridae, Flaviviridae/Hepacivirus and Orthomyxoviridae — exhibit deep co-divergence with their vertebrate hosts versus recent cross-class host switching, and does this push the origins of these families back to the root of the vertebrate lineage?
>
> *Rationale:* The candidate richly targets GQ_001's intent—asking if deep co-divergence across chordates among many RNA-virus families implies ancient origins—and is tightly grounded in Tab S2 and BLASTx metrics, but it omits the explicit phrase 'meta-transcriptomic sampling.'

**Rank 2** · Comp = 0.940 · ✅ pass

> Do the new fish, amphibian, reptile and jawless-vertebrate Orthomyxovirus, Hantavirus, Arenavirus and Hepacivirus genomes recovered in this survey (n = 18, 15, 9 and 15 respectively in Tab S2) reposition the deepest root of these mammalian-pathogen-containing families to non-mammalian vertebrates, implying an aquatic/ectothermic origin for human-relevant viral lineages?
>
> *Rationale:* The candidate tightly matches GQ_001 by testing whether broad sampling of non-mammalian vertebrates re-roots mammal-associated RNA-virus families; it is well grounded in Tab S2 but omits explicit mention of 'meta-transcriptomic sampling.'

**Rank 3** · Comp = 0.460 · ❌ fail

> Is RNA viral richness and family-level composition in vertebrate meta-transcriptomes structured by host tissue (gut vs gill vs liver vs lung) once host-class is controlled for, and which viral families are strictly tissue-restricted versus ubiquitous across organs?
>
> *Rationale:* The candidate is a tissue-tropism/metatranscriptome question that matches GQ_001's data type but not its evolutionary aim; it is well grounded in the supplied tables (Tab S2) yet omits broad phylogeny and ancient-association elements.

**Rank 4** · Comp = 0.760 · ✅ pass

> Across the 31 viral families recovered, is the BLASTx amino-acid divergence to nearest known relative (mean 38.4 %, ≥87 % of hits <50 %) systematically greater for hits from the most basal vertebrate hosts (Agnatha, Sarcopterygii, Chondrichthyes) than for those from Actinopterygii, Amphibia and Reptilia, indicating that under-sampling of basal vertebrates accounts for most of the unexplored RNA virosphere?
>
> *Rationale:* The candidate maps to GQ_001 by testing phylogenetic sampling effects on viral divergence using concrete BLASTx data across host classes; it covers phylogeny, metatranscriptomic data, and RNA-virus families but omits explicit virus-host association analyses and statements about ancient origins.

**Rank 5** · Comp = 0.760 · ✅ pass

> Do the 16 'Unknown divergent' and 12 'Putative vertebrate virus' contigs in Tab S2, together with the 'Astro-Poty-like vert' (n=8) and 'Mono-Chu-like' lineages, define one or more genuinely new vertebrate-infecting viral families when their RdRp domains are placed in the global RNA-virus phylogeny?
>
> *Rationale:* The candidate is a specific, well-grounded metatranscriptome question about novel vertebrate RNA-virus families (matches GQ_001 intent) but lacks explicit broad-phylogeny sampling and discussion of ancient origins.

### ✅ `gpt-5.5-high` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 4 | 3 | 5 | 3.900 | 0.780 | ✅ | GQ_001 (P) |
| 2 | 4 | 4 | 4 | 5 | 4.100 | 0.820 | ✅ | GQ_001 (P) |
| 3 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 4 | 5 | 4 | 4 | 5 | 4.500 | 0.900 | ✅ | GQ_001 (P) |
| 5 | 3 | 4 | 4 | 4 | 3.600 | 0.720 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 0.780 · ✅ pass

> How do vertebrate host taxonomy and tissue tropism jointly shape RNA virus richness, abundance, and family composition across the 126-library chordate metatranscriptomic survey?
>
> *Rationale:* The candidate aligns well with GQ_001 on metatranscriptomic sampling and host–virus associations (explicit file/column grounding) but omits the gold's core element of investigating ancient origins of RNA-virus families.

**Rank 2** · Comp = 0.820 · ✅ pass

> Are basal aquatic vertebrate lineages enriched for low-identity or unknown divergent RNA viruses compared with amphibian and reptile hosts?
>
> *Rationale:* The candidate aligns well with GQ_001 by testing divergent RNA viruses across broad vertebrate classes using BLASTx identities (well-grounded in the provided spreadsheet), but it omits explicit mention of metatranscriptomic sampling and is framed as a narrower comparative enrichment question.

**Rank 3** · Comp = 0.580 · ❌ fail

> Which sampled organs are most productive for detecting vertebrate-specific RNA viruses after accounting for sequencing depth and host class?
>
> *Rationale:* The candidate is grounded in the provided files and targets RNA-virus detection via metatranscriptomes (good data grounding) but focuses on organ-level sampling efficiency and omits phylogenetic breadth and ancient evolutionary questions central to GQ_001.

**Rank 4** · Comp = 0.900 · ✅ pass

> Do major RNA virus families span multiple vertebrate host classes in patterns consistent with ancient host association or repeated host switching?
>
> *Rationale:* Strong semantic match to GQ_001: asks if RNA-virus families span vertebrate classes consistent with ancient association vs host-switching and cites specific ESM table columns; missing explicit mention of meta-transcriptomic sampling.

**Rank 5** · Comp = 0.720 · ✅ pass

> Which host orders and library types contain the highest normalized richness and abundance of newly cataloged RNA viruses in this chordate survey?
>
> *Rationale:* The candidate aligns with GQ_001's sampling-and-discovery intent by using host orders and metatranscriptomic library data to quantify RNA-virus richness, but it omits the gold question's emphasis on ancient origins and deep virus–host codivergence.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 2 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 3 | 5 | 5 | 5 | 5 | 5.000 | 1.000 | ✅ | GQ_001 (P) |
| 4 | 2 | 4 | 3 | 5 | 3.100 | 0.620 | ✅ | GQ_001 (P) |
| 5 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |

**Rank 1** · Comp = 1.000 · ✅ pass

> Do the complete 8-segment influenza-like virus genome from spiny eel (Mastacembelus aculeatus, Actinopterygii; accessions MG600037-MG600044) and the partial influenza-like genomes from Asiatic toad (Bufo gargarizans, Amphibia; MG600045-MG600050) and hagfish (Eptatretus burgeri, Agnatha; MG600051-MG600054), as catalogued in MOESM3, represent deep-branching ancestral lineages that resolve the aquatic vertebrate origin of Orthomyxoviridae and reveal whether the canonical 8-segment genome architecture predates the divergence of jawed and jawless vertebrates?
>
> *Rationale:* The candidate precisely uses MOESM3 metatranscriptome entries across basal vertebrates (Actinopterygii, Amphibia, Agnatha) to test deep-branching Orthomyxoviridae lineages and the antiquity of the 8-segment genome, matching GQ_001 in scope and data grounding.

**Rank 2** · Comp = 1.000 · ✅ pass

> Is the strict hepatotropism of Hepacivirus (HCV-like) viruses, observed across phylogenetically distant vertebrate classes including Chondrichthyes (sharks/rays; 8 entries), Reptilia (5 entries), Actinopterygii (1 entry), and Sarcopterygii (1 entry) in MOESM3, an ancestral biological constraint of the Flaviviridae: Hepacivirus lineage that predates the origin of tetrapods rather than a derived feature of human Hepatitis C virus?
>
> *Rationale:* The candidate precisely targets whether conserved hepatotropism across diverse vertebrate hosts in MOESM3 reflects an ancestral trait of Hepacivirus, matching GQ_001 in scope, required elements, and dataset grounding.

**Rank 3** · Comp = 1.000 · ✅ pass

> Does Astroviridae represent the most ancient and host-generalist vertebrate RNA virus family in the Chordata virome, given that 65 astrovirus-like sequences in MOESM3 span all six sampled vertebrate classes (Actinopterygii, Amphibia, Reptilia, Chondrichthyes, Agnatha, and Sarcopterygii) with mean amino acid identities below 40% to known astroviruses, and does the phylogenetic breadth of these sequences support an aquatic vertebrate origin predating the water-to-land transition?
>
> *Rationale:* The candidate precisely tests GQ_001's core claim using MOESM2/MOESM3 metatranscriptomic evidence across six vertebrate classes to ask if Astroviridae show deep, host-generalist origins and an aquatic origin predating terrestrial vertebrates.

**Rank 4** · Comp = 0.620 · ✅ pass

> Do the 270 novel vertebrate viruses discovered across 126 metatranscriptomic libraries in MOESM2 and MOESM3 show tissue-specific infection patterns that are conserved across distantly related host classes, and specifically, is the gut the primary site of RNA virus diversification in vertebrates as suggested by 110 of 270 virus-tissue associations being gut-derived?
>
> *Rationale:* Matches GQ_001's metatranscriptomic and vertebrate scope but shifts intent to tissue tropism and gut-centered diversification; covers four of five required elements (missing ancient origins) and is strongly grounded in MOESM2/MOESM3 file columns and counts.

**Rank 5** · Comp = 0.700 · ✅ pass

> Do the 16 highly divergent sequences classified as unknown divergent viruses and 12 putative vertebrate viruses in the Note column of MOESM3 — sharing less than 30% amino acid identity with any known virus — represent entirely new virus families that extend the known RNA virus phylogeny of vertebrates beyond currently recognized taxonomic boundaries?
>
> *Rationale:* Candidate strongly targets discovery of novel RNA-virus families in vertebrate data and is well grounded in MOESM3 metadata, but it omits explicit mention of broad phylogenetic sampling, metatranscriptomic methodology, and host-association / ancient-origin framing required by GQ_001.

### ✅ `gemini-3.1-pro` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 0 | 3 | 4 | 1.800 | 0.360 | ❌ | GQ_001 (P) |
| 2 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 3 | 1 | 0 | 1 | 3 | 0.900 | 0.180 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 2 | 4 | 0.800 | 0.160 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.360 · ❌ fail

> What are the key significant features or relationships detailed in the supplementary data tables (MOESM2 and MOESM3) that support the main conclusions of the associated 2018 Nature publication?
>
> *Rationale:* The candidate is a generic, data-focused request tied to specific supplementary files (good grounding) but lacks the explicit virology and phylogenetic elements required to match GQ_001's scientific intent.

**Rank 2** · Comp = 0.240 · ❌ fail

> How do the data presented in MOESM2_ESM.xlsx differ from or complement the data in MOESM3_ESM.xlsx?
>
> *Rationale:* The candidate is a file-structure comparison of two supplementary Excel files and does not address the gold question's scientific intent about broad vertebrate sampling or ancient RNA-virus evolution, though it is well grounded in the specific supplied files.

**Rank 3** · Comp = 0.180 · ❌ fail

> What specific experimental or analytical methodology is described or supported by the supplementary text or figures in the PDF file?
>
> *Rationale:* The candidate requests methods in the supplementary PDF, which is a generic, file-focused query and does not address the gold question's required elements about broad vertebrate sampling, metatranscriptomics, or ancient RNA-virus host associations; it does, however, name the specific PDF file.

**Rank 4** · Comp = 0.120 · ❌ fail

> Are there any specific gene lists, protein interactions, or other biological entities detailed in the Excel files that are central to the study's hypothesis?
>
> *Rationale:* The candidate inspects gene/protein lists in specific Excel supplements (strong data grounding) but is unrelated to the gold question about broad vertebrate metatranscriptomic sampling and ancient RNA-virus host associations, so match and required-element coverage are zero.

**Rank 5** · Comp = 0.160 · ❌ fail

> What statistical thresholds or criteria were used to define significance in the supplementary data tables?
>
> *Rationale:* The candidate is a methodological question about significance thresholds in supplementary Excel tables and is unrelated to the biological-evolutionary focus of GQ_001, though it is well-grounded in specific supplementary files.

### ✅ `deepseek-v4-pro` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 5 | 0.700 | 0.140 | ❌ | GQ_001 (P) |
| 4 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 0 | 5 | 0.500 | 0.100 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.120 · ❌ fail

> Does the burden of somatic mutations in haematopoietic tissue increase monotonically with donor age and differ significantly between individuals with and without atherosclerotic cardiovascular disease after adjusting for sex, smoking status, and sequencing depth?
>
> *Rationale:* The candidate concerns human somatic mutations, age, and CVD using MOESM Excel tables, which is data-grounded but entirely unrelated to the gold question about vertebrate RNA-virus evolution.

**Rank 2** · Comp = 0.140 · ❌ fail

> Are somatic mutations in DNMT3A, TET2, and ASXL1 — the three most commonly mutated drivers of clonal haematopoiesis — associated with elevated all-cause mortality independent of chronological age in this cohort?
>
> *Rationale:* The candidate is a human clinical genetics question about clonal haematopoiesis and mortality (DNMT3A/TET2/ASXL1) and thus is semantically unrelated to the gold question about vertebrate RNA-virus evolution; no required elements match, though the candidate is well-grounded in the listed MOESM files.

**Rank 3** · Comp = 0.140 · ❌ fail

> What is the minimum variant allele fraction (VAF) threshold at which somatic mutations in peripheral blood become predictive of future haematological malignancy diagnosis, and how does this threshold vary by gene?
>
> *Rationale:* The candidate addresses clinical VAF thresholds for human blood cancers, not vertebrate metatranscriptomics or RNA-virus evolution, so it fails to meet any required elements of the matched gold question but is strongly grounded in the provided MOESM1–3 files.

**Rank 4** · Comp = 0.100 · ❌ fail

> Do individuals carrying multiple distinct somatic clones (clonal mosaicism) exhibit faster longitudinal expansion of their largest clone compared to individuals harbouring a single clone, as measured by variant allele fraction change over follow-up?
>
> *Rationale:* The candidate question is about human somatic clonal dynamics and VAF trajectories, which is unrelated to the gold virus-evolution question; it contains no required elements from GQ_001 but is well grounded in the listed MOESM2/MOESM3 files.

**Rank 5** · Comp = 0.100 · ❌ fail

> Is the age-adjusted prevalence of clonal haematopoiesis of indeterminate potential (CHIP) significantly higher in this December 2018 Nature cohort compared to the prevalence reported in the contemporaneous UK Biobank and Icelandic deCODE cohorts, after harmonizing variant-calling pipelines?
>
> *Rationale:* The candidate is about human CHIP prevalence and cross-cohort comparison, not vertebrate RNA-virus evolution; it matches no required elements but is well grounded in the listed MOESM files.

### 🟨 `glm-5` — **未评测（待补）**

### ✅ `gemini-2.5-flash` · src = `upl_1779608619_39b5de`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 0 | 0 | 2 | 4 | 0.800 | 0.160 | ❌ | GQ_001 (P) |
| 2 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |
| 3 | 0 | 0 | 1 | 3 | 0.500 | 0.100 | ❌ | GQ_001 (P) |
| 4 | 1 | 0 | 2 | 4 | 1.200 | 0.240 | ❌ | GQ_001 (P) |
| 5 | 0 | 0 | 1 | 4 | 0.600 | 0.120 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.160 · ❌ fail

> What are the key experimental findings or datasets presented in the supplementary materials that support the main conclusions of the associated publication?
>
> *Rationale:* The candidate is a generic question about supplementary datasets and explicitly cites the three files, but it contains none of GQ_001's specific required elements about vertebrate RNA-virus evolution, so it is unrelated to the gold intent.

**Rank 2** · Comp = 0.120 · ❌ fail

> Do the two Excel supplementary files (MOESM2_ESM.xlsx and MOESM3_ESM.xlsx) contain distinct types of data, such as raw experimental measurements versus processed or summarized results?
>
> *Rationale:* The candidate is a technical metadata question about two Excel supplement files and does not engage GQ_001's scientific aims about vertebrate-wide metatranscriptomic discovery of ancient RNA-virus host associations.

**Rank 3** · Comp = 0.100 · ❌ fail

> Does the PDF supplementary file (MOESM1_ESM.pdf) provide extended methodological details or additional figures that were not included in the main body of the associated publication?
>
> *Rationale:* The candidate asks about the content of a supplementary PDF file (MOESM1_ESM.pdf) and thus does not address the scientific elements of GQ_001; it is nonetheless concretely grounded to a listed file.

**Rank 4** · Comp = 0.240 · ❌ fail

> What specific variables or parameters are measured and reported across the datasets contained within the supplementary Excel files?
>
> *Rationale:* The candidate is a file-level data-discovery question about Excel variables and does not address the scientific intent of GQ_001 about broad vertebrate sampling and ancient RNA-virus-host associations.

**Rank 5** · Comp = 0.120 · ❌ fail

> What is the overall scientific domain or research area that these supplementary materials belong to, based on the nature of the provided data files?
>
> *Rationale:* The candidate is a generic file-domain classification question unrelated to vertebrate RNA-virus evolutionary questions, so it matches none of the gold question's required elements though it is grounded in the listed supplementary filenames.


---
## 11 · `zooplankton_rna_virosphere_2022`

- **数据**：10 文件 · 570,352 bytes · 例：16945363_31352431_chrysoviridae_alignment.fas, 16945399_31352560_Narnaviridae_alignment.fas, 16945423_31352587_Picornavirales_alignment.fas
- **Gold 标注问题**：2
- **重复上传次数**：1 (upl_1779611309_f833e5)
- **已评测 agent**：7/7

### ✅ `claude-code-opus-4-7` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 4 | 3.145 | 0.629 | ✅ | GQ_002 (S) |
| 3 | 3 | 2 | 2 | 5 | 2.700 | 0.540 | ❌ | GQ_001 (P) |
| 4 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.680 · ✅ pass

> Do the 194 Hirai RdRp contigs — particularly the 82 Partiti-like and 37 Toti-like sequences — define previously undescribed family- or genus-level clades within the dsRNA virosphere when co-aligned with curated Partitiviridae, Totiviridae, Picobirnaviridae, Reoviridae and Chrysoviridae RdRp references, and do those clades cluster phylogenetically with diatom- or aquatic-invertebrate-associated reference taxa rather than with terrestrial fungal/plant taxa?
>
> *Rationale:* Candidate strongly targets family-level RdRp alignment and phylogenetic classification with concrete contig counts and multiple family alignments (high grounding), but omits ssRNA scope and an explicit bulk-zooplankton statement, so it largely matches GQ_002 with minor gaps.

**Rank 2** · Comp = 0.629 · ✅ pass

> Do the 35 Hirai 'no-hit' nucleotide contigs together with the Hirai_virus_hypothetical_protein and Hirai_virus_capsid sequences contain conserved RdRp- or capsid-like motifs that, after six-frame translation and HMM-profile comparison against the family-level RdRp alignments provided, betray a cryptic relationship to the same dsRNA viral lineages dominating the annotated contigs?
>
> *Rationale:* The candidate aligns well with GQ_002 by using family-level RdRp alignments and HMMs to classify no-hit contigs into dsRNA viral lineages, but it omits OTU clustering and explicit bulk-zooplankton/ssRNA considerations.

**Rank 3** · Comp = 0.540 · ❌ fail

> Are the 17 GenBank-deposited 2021-JH viral metagenome records (LC651635–LC651651), which include paired RdRp/capsid/hypothetical-protein genes, consistent with multi-segmented dsRNA virus genomes whose segments co-occur within the same Hirai assembly contigs, indicating that complete multipartite virus genomes can be reconstructed from this single metagenomic sample?
>
> *Rationale:* The candidate aligns with GQ_001 on RdRp and dsRNA-virus focus and is well grounded in files/accessions, but it omits FLDS/metatranscriptome and explicit zooplankton/host-association framing, shifting intent from community-level virome discovery to multipartite-genome reconstruction.

**Rank 4** · Comp = 0.760 · ✅ pass

> Within the Picornavirales alignment, do the Hirai picorna-like contigs (notably contig_2_LC651642 and contig_231_Picorna-like_partial) branch with insect-/crustacean-pathogenic dicistroviruses (e.g. Acute bee paralysis virus, Cricket paralysis virus, Taura syndrome virus, Mud crab virus) rather than with vertebrate or plant picornaviruses, suggesting an arthropod or crustacean host for the Hirai sample?
>
> *Rationale:* The candidate is a specific, well-grounded host-attribution phylogenetic test using Picornavirales RdRp sequences and Hirai contigs, aligning strongly with GQ_001's host-association aim but omitting explicit FLDS/metatranscriptome and zooplankton-community mention.

**Rank 5** · Comp = 0.646 · ✅ pass

> Across the seven family-stratified RdRp alignments, does the count and divergence of Hirai contigs per family follow the predicted relationship between viral genome architecture (dsRNA vs ssRNA, segmented vs monopartite) and the prevalence of novel virus discovery in eukaryotic metagenomes — specifically, are dsRNA Partiti- and Toti-like contigs both more numerous and more divergent from their nearest reference than ssRNA Narna- or Picorna-like contigs in this dataset?
>
> *Rationale:* The candidate aligns with GQ_002 by using family-level RdRp alignments to contrast ssRNA vs dsRNA diversity and classification, is well grounded in specific alignment files and contig counts, but omits explicit mention of OTU clustering and 'bulk zooplankton'.

### ✅ `gpt-5.5-high` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 2 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 5 | 2.900 | 0.580 | ❌ | GQ_001 (P) |
| 4 | 4 | 2 | 4 | 5 | 3.500 | 0.700 | ✅ | GQ_001 (P) |
| 5 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |

**Rank 1** · Comp = 0.580 · ❌ fail

> What is the diversity, novelty, and phylogenetic placement of RdRp-bearing RNA viruses recovered from the Hirai viral metagenome across the partiti-like, toti-like, picobirna-like, reo-like, narna-like, picorna-like, and related viral groups?
>
> *Rationale:* The candidate closely matches GQ_001's RdRP-centered virome discovery and uses multiple supplied alignment files and contig counts, but it omits the required zooplankton/FLDS and host-association elements, so it is a partial but concrete match.

**Rank 2** · Comp = 0.527 · ❌ fail

> Do the Hirai RdRp contigs reveal a virome dominated by divergent dsRNA virus lineages, especially partiti-like, toti-like, picobirna-like, and reo-like viruses?
>
> *Rationale:* The candidate aligns with GQ_002's family-level RdRp classification focus and is well grounded in specific Hirai contig counts and alignments, but it omits explicit OTU-clustering and comparison to ssRNA groups and doesn't mention bulk zooplankton sampling.

**Rank 3** · Comp = 0.580 · ❌ fail

> Which Hirai viral contigs correspond to near-complete or complete reported viral CDS records, and how do those complete sequences represent the broader RdRp contig diversity?
>
> *Rationale:* Captures RdRp-contig and virome-representation intent and is well-grounded in files/counts, but omits FLDS/metatranscriptome, explicit zooplankton context, and host-association caveats.

**Rank 4** · Comp = 0.700 · ✅ pass

> Are the 37 Hirai no-hit possible viral contigs candidates for additional highly divergent viruses beyond the annotated RdRp-bearing contigs?
>
> *Rationale:* The candidate is a focused virome-discovery question that leverages specific contig counts and files (strong data grounding) and matches the gold's discovery intent but omits FLDS/metatranscriptome, explicit zooplankton context, and host-association considerations.

**Rank 5** · Comp = 0.646 · ✅ pass

> How consistently do the family-specific amino-acid alignments support the virus-like classifications assigned in the Hirai RdRp contig headers?
>
> *Rationale:* The candidate closely targets family-level alignment-based classification of RdRp contigs (matching GQ_002) and is well grounded in the Hirai contigs and multiple alignment files, but it omits explicit OTU clustering, zooplankton wording, and ssRNA/dsRNA framing.

### ✅ `claude-code-sonnet-4-6` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 4 | 2 | 4 | 5 | 2.975 | 0.595 | ❌ | GQ_002 (S) |
| 2 | 4 | 3 | 4 | 5 | 3.800 | 0.760 | ✅ | GQ_001 (P) |
| 3 | 3 | 3 | 3 | 5 | 2.720 | 0.544 | ❌ | GQ_002 (S) |
| 4 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.595 · ❌ fail

> Do the 37 no-BLAST-hit contigs from the Hirai viral metagenome (including Hirai_virus_capsid and Hirai_virus_hypothetical_protein) represent novel RNA virus families phylogenetically distinct from the 16 classified lineages (Partiti-like, Toti-like, Picobirna-like, Reo-like, Narna-like, and others) identified in the same sample?
>
> *Rationale:* The candidate maps well to family-level classification goals in GQ_002 and is strongly data-grounded, but it omits explicit OTU-clustering, ssRNA/dsRNA framing, and the 'bulk zooplankton' context, so coverage is partial though acceptable in form.

**Rank 2** · Comp = 0.760 · ✅ pass

> Does the dominance of Partiti-like (42.3%) and Toti-like (19.1%) RNA viruses in the Hirai metagenome reflect a fungal host virome, and can the co-occurrence of an invertebrate-associated Picornavirales contig (Hirai_contig_2) be attributed to a non-fungal organism in the same sample?
>
> *Rationale:* Strongly aligned on RdRp-based virome discovery and host-association with detailed file/contig references, but it omits explicit zooplankton-community provenance and uses 'metagenome' rather than the FLDS/metatranscriptome wording required by the gold.

**Rank 3** · Comp = 0.544 · ❌ fail

> Are the 12 complete RdRp contigs from the Hirai metagenome (including the six Partiti-like complete sequences LC651639–LC651651 and the 11,845-nt Hypo-like polyprotein LC651648) sufficient to define new virus species according to ICTV species demarcation criteria within Partitiviridae, Hypoviridae, and Picobirnaviridae?
>
> *Rationale:* The candidate aligns with GQ_002 on RdRp-based family-level classification and uses provided alignment files and contig identifiers, but it shifts focus to ICTV species demarcation and omits OTU clustering, ssRNA/dsRNA partitioning, and explicit zooplankton context.

**Rank 4** · Comp = 0.561 · ❌ fail

> Do the 11 Hirai Partitiviridae-like contigs placed in the family alignment cluster into a single novel genus or multiple genera, based on the phylogenetic depth of their divergence from the 56 reference Partitiviridae sequences?
>
> *Rationale:* The candidate well covers RdRp-based family-level classification using provided Partitiviridae alignment files but narrows to genus-level questions and omits explicit ssRNA/dsRNA comparison and bulk-zooplankton framing from GQ_002.

**Rank 5** · Comp = 0.527 · ❌ fail

> Can the Hirai metagenome Picornavirales contig (Hirai_contig_2, LC651642, complete 9,274 nt polyprotein) be assigned to a new invertebrate-infecting picorna-like virus genus based on its phylogenetic distance from bee-infecting Dicistroviridae and Iflaviridae reference sequences in the Picornavirales alignment?
>
> *Rationale:* The candidate aligns with GQ_002's family-alignment/classification theme but is narrower (single Picornavirales polyprotein phylogeny) and omits RdRP clustering, dsRNA comparison, and bulk zooplankton context, while being strongly grounded in specific alignment files and accessioned sequence data.

### ✅ `gemini-3.1-pro` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 4 | 2.550 | 0.510 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 4 | 3 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 3 | 2 | 3 | 4 | 2.380 | 0.476 | ❌ | GQ_002 (S) |
| 4 | 0 | 1 | 1 | 3 | 0.800 | 0.160 | ❌ | GQ_001 (P) |
| 5 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.510 · ❌ fail

> Where do the newly assembled "Hirai" contigs place phylogenetically within established RNA virus families such as Chrysoviridae, Narnaviridae, and Partitiviridae?
>
> *Rationale:* The candidate aligns with GQ_002's family-level classification intent (uses specific family alignments and asks taxonomic placement) but misses RdRP OTU-clustering, ssRNA/dsRNA distinction, and explicit bulk zooplankton framing.

**Rank 2** · Comp = 0.374 · ❌ fail

> Do the unclassified sequences in the dataset contain conserved viral domains that could classify them into new or existing viral families?
>
> *Rationale:* Mapped to GQ_002 because both ask about classifying viral sequences into families; the candidate lacks the GQ_002-specific focus on RdRP OTU clustering, family alignments, ssRNA/dsRNA partitioning, and bulk zooplankton context.

**Rank 3** · Comp = 0.476 · ❌ fail

> How conserved are the core catalytic motifs of the RNA-dependent RNA polymerase (RdRp) across the diverse RNA virus families represented in the metagenome?
>
> *Rationale:* Matched GQ_002 because the candidate centers on comparative RdRp family-level alignments, but it omits OTU clustering, explicit ssRNA/dsRNA separation, bulk zooplankton context, and classification aims while being grounded in specific RdRp files.

**Rank 4** · Comp = 0.160 · ❌ fail

> What is the predicted genome organization and coding capacity of the complete viral genomes reported in the 2021-JH metagenome?
>
> *Rationale:* Candidate is a genome-annotation question about a 2021 metagenome file and lacks the zooplankton/FLDS/metatranscriptome and virosphere-host framing of GQ_001, so match is poor (0) though it does mention RdRp (1/5 required elements) and cites a specific file (data grounding 3).

**Rank 5** · Comp = 0.500 · ❌ fail

> Can the potential hosts of the newly discovered Picornavirales and Reoviridae contigs be inferred based on their phylogenetic clustering with viruses of known host ranges?
>
> *Rationale:* Matches GQ_001 on host-association but misses dataset and zooplankton framing; contains strong file-level grounding (two family alignments) yet only one of five required elements is present.

### ✅ `deepseek-v4-pro` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 2 | 4 | 5 | 2.635 | 0.527 | ❌ | GQ_002 (S) |
| 2 | 2 | 1 | 3 | 5 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 3 | 4 | 3 | 4 | 5 | 3.230 | 0.646 | ✅ | GQ_002 (S) |
| 4 | 4 | 3 | 5 | 5 | 3.400 | 0.680 | ✅ | GQ_002 (S) |
| 5 | 3 | 1 | 3 | 5 | 2.210 | 0.442 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.527 · ❌ fail

> Do the 17 Hirai_nohit contigs in `Possible_virus_contigs.fas` represent one or more novel RNA virus families that are phylogenetically distinct from the seven established families in the reference alignments, and can conserved RdRp domain architecture place them relative to known orders such as Picornavirales, Reoviridae, and Narnaviridae?
>
> *Rationale:* The candidate is well grounded in specific RdRp reference alignments and asks about family-level phylogenetic placement, matching GQ_002's classification focus but missing explicit OTU clustering, ssRNA/dsRNA distinction, and the bulk zooplankton context.

**Rank 2** · Comp = 0.374 · ❌ fail

> To what extent do the complete viral genomes deposited in nuccore (LC651635–LC651638) correspond to specific Hirai metagenomic contigs, and does the gene content and genome organization (RdRp, capsid, hypothetical proteins) of these complete genomes reveal architectures that differ from those of reference viruses in the seven family alignments?
>
> *Rationale:* The question is grounded in specific files and family alignments and involves RdRp-containing contigs, so it loosely matches GQ_002's family-alignment theme but fails to ask about OTU clustering, ssRNA/dsRNA partitioning, bulk zooplankton context, or classification.

**Rank 3** · Comp = 0.646 · ✅ pass

> Within the Partitiviridae and Picornavirales alignments—the two largest family datasets—what is the distribution of pairwise RdRp amino acid divergence between Hirai contigs and their closest known reference sequences, and does this divergence exceed the intra-family divergence range observed among previously characterized members?
>
> *Rationale:* The candidate well matches GQ_002's use of family alignments and RdRp-based classification, quantitatively comparing Hirai contigs to references, but it omits OTU-clustering, explicit ssRNA/dsRNA partitioning, and the bulk-zooplankton context.

**Rank 4** · Comp = 0.680 · ✅ pass

> Do the three contigs annotated as 'Unclassified_ssRNA_virus_partial' within the Hirai Contigs RdRp file share conserved RdRp catalytic motifs (GDD, SGxxxT, Walker A/B) with the 17 Hirai_nohit sequences, and do they form a shared phylogenetic cluster distinct from the seven reference families?
>
> *Rationale:* The candidate is a focused, data-grounded instantiation of GQ_002—testing RdRp motif conservation and phylogenetic monophyly versus reference families—but omits dsRNA scope and explicit bulk-zooplankton framing.

**Rank 5** · Comp = 0.442 · ❌ fail

> Is there evidence of inter-family recombination or modular RdRp evolution among Hirai contigs that span multiple RNA virus families, as detectable by discordant phylogenetic signal between the N-terminal and C-terminal RdRp domains when aligned against the seven reference family alignments?
>
> *Rationale:* Matches GQ_002 via RdRp family alignments and Hirai contigs but shifts intent to recombination/phylogenetic discordance rather than OTU clustering or ssRNA/dsRNA classification; well-grounded in specific alignment files.

### ✅ `glm-5` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 4 | 2.805 | 0.561 | ❌ | GQ_002 (S) |
| 2 | 4 | 2 | 4 | 4 | 3.400 | 0.680 | ✅ | GQ_001 (P) |
| 3 | 2 | 2 | 2 | 4 | 1.870 | 0.374 | ❌ | GQ_002 (S) |
| 4 | 3 | 1 | 3 | 5 | 2.210 | 0.442 | ❌ | GQ_002 (S) |
| 5 | 3 | 2 | 2 | 5 | 2.295 | 0.459 | ❌ | GQ_002 (S) |

**Rank 1** · Comp = 0.561 · ❌ fail

> What novel RNA virus families or genera are represented by the unclassified 'Hirai_nohit' contigs, and how do they phylogenetically relate to established virus taxa based on conserved RdRp motifs?
>
> *Rationale:* Candidate aligns with GQ_002's classification/phylogeny intent via RdRp and family alignments but omits OTU clustering, explicit ssRNA/dsRNA partitioning, and the bulk zooplankton context; well grounded in multiple alignment and contig files.

**Rank 2** · Comp = 0.680 · ✅ pass

> What are the predicted host organisms for the novel 'Hirai_contig' and 'Hirai_nohit' viruses based on their phylogenetic relationships to known viruses with characterized hosts?
>
> *Rationale:* The candidate focuses tightly on host prediction for specific RdRP contigs using the provided alignments (good data grounding and host-association match) but omits FLDS/metatranscriptome and zooplankton-context and broader diversity framing from the gold question.

**Rank 3** · Comp = 0.374 · ❌ fail

> Which conserved catalytic motifs and functional domains are present in the novel RdRp sequences from 'Hirai_contig' and 'Hirai_nohit' viruses, and how do they compare to established RdRp motif patterns?
>
> *Rationale:* The candidate is clearly about RdRp sequence analysis and uses specific alignment files (good data grounding) but asks about motif/domain comparison rather than OTU clustering, family-level classification, or ssRNA/dsRNA separation required by GQ_002.

**Rank 4** · Comp = 0.442 · ❌ fail

> How does the genetic diversity and sequence divergence of novel viruses in the Hirai dataset compare across the seven represented virus families?
>
> *Rationale:* The candidate is a family-level, alignment-based comparative-diversity question grounded in Hirai RdRp and seven family alignments, but it omits OTU clustering, ssRNA/dsRNA separation, and explicit classification in bulk zooplankton.

**Rank 5** · Comp = 0.459 · ❌ fail

> What is the completeness and quality of the novel viral contigs in the Hirai dataset, and do they represent full-length or partial RdRp genes?
>
> *Rationale:* Candidate matches GQ_002 on RdRp-focused analysis but lacks OTU clustering, taxonomic partitioning (ssRNA/dsRNA), and zooplankton/classification context; it is, however, tightly grounded in specific RdRp and alignment files.

### ✅ `gemini-2.5-flash` · src = `upl_1779611309_f833e5`

| rank | match | req_elem | accept | data_grnd | Raw /5 | Comp 0–1 | passed | matched_gold |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 3 | 3 | 4 | 5 | 2.890 | 0.578 | ❌ | GQ_002 (S) |
| 2 | 3 | 2 | 3 | 4 | 2.800 | 0.560 | ❌ | GQ_001 (P) |
| 3 | 3 | 1 | 2 | 4 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 4 | 2 | 1 | 4 | 4 | 1.955 | 0.391 | ❌ | GQ_002 (S) |
| 5 | 3 | 1 | 3 | 4 | 2.500 | 0.500 | ❌ | GQ_001 (P) |

**Rank 1** · Comp = 0.578 · ❌ fail

> What is the phylogenetic relationship between the RdRp sequences found in the 'Hirai_Contigs_RdRp.fas' and 'Possible_virus_contigs.fas' files and known viral families represented in the alignment files?
>
> *Rationale:* The candidate well-targets family-level alignment-based classification of RdRp contigs (matching GQ_002's classification aim) but omits explicit OTU-clustering, ssRNA/dsRNA partitioning, and the bulk zooplankton context.

**Rank 2** · Comp = 0.560 · ❌ fail

> Are there novel viral sequences or families present in the 'Possible_virus_contigs.fas' and 'Hirai_Contigs_RdRp.fas' files that do not show significant homology to the provided viral family alignments or the 'nuccore_reported_viral_sequences.fasta'?
>
> *Rationale:* The candidate matches GQ_001's discovery aim by querying RdRP contigs for novel viruses and cites specific files, but it omits the zooplankton/FLDS sampling context and the host-association caveat required by the gold question.

**Rank 3** · Comp = 0.391 · ❌ fail

> What is the sequence conservation level within the RdRp gene across different viral families represented in the alignment files?
>
> *Rationale:* The candidate focuses on RdRp sequence conservation across provided family alignment files (good data grounding) but misses GQ_002's central tasks: OTU clustering, ssRNA/dsRNA partitioning, zooplankton context, and classification.

**Rank 4** · Comp = 0.391 · ❌ fail

> Can specific sequence motifs or signatures be identified within the RdRp sequences that are unique to particular viral families present in the alignment files?
>
> *Rationale:* The candidate focuses on family-level RdRp alignments and motif discovery, matching GQ_002's alignment aspect but missing OTU clustering, ss/dsRNA separation, bulk zooplankton context, and classification intent.

**Rank 5** · Comp = 0.500 · ❌ fail

> What is the distribution of sequence lengths for the contigs identified as 'RdRp' in 'Hirai_Contigs_RdRp.fas' and 'Possible_virus_contigs.fas', and how does this compare to the full-length RdRp genes of known viruses?
>
> *Rationale:* The candidate tightly focuses on contig length/completeness for RdRp sequences (well grounded in specific files) but does not address the broader GQ_001 goals of virome diversity or host-association, so it partially matches but is narrower.

