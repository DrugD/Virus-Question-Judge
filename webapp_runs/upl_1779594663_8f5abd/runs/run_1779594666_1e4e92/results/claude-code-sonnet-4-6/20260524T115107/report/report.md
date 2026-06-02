# Technical Report: Viral Discovery in Herptile Transcriptomes

## 1. Data Summary

**File:** `data/43705_2022_180_MOESM1_ESM.docx` (2.25 MB) — supplementary material from a peer-reviewed study on novel virus discovery in amphibians and reptiles (herptiles).

The document contains:
- **Supplementary Table 1**: A structured dataset of 236 publicly available RNA-sequencing (RNA-seq) accessions used for viral metatranscriptomic discovery. Columns: Species (common name), Scientific name, Animal type (Amphibian / Reptile), SRA Accession, Country of origin, Tissue, Sequencing platform.
- **5 embedded TIFF figures** (phylogenetic trees): Bunyavirales, Lyssaviridae/Rhabdoviridae, Hepeviridae, Astroviridae, Orthomyxoviridae (influenza-like), and Caliciviridae — representing 6 distinct novel virus families or genera identified through BLAST-based screening of the transcriptomes.

**Scale:** 236 SRA accessions × 7 metadata fields; 123 unique species; 166 distinct species–tissue combinations.

---

## 2. Analysis

### 2.1 Taxonomic Distribution
- **Reptiles** dominate the dataset: 156 samples (66%) across snakes, lizards, turtles, crocodilians, and tuatara.
- **Amphibians** comprise 79 samples (33%), including caecilians (40 samples from French Guiana), frogs, toads, salamanders, and a newt.
- **123 unique species** are represented, making this among the broadest herptile virome surveys to date.

### 2.2 Tissue Representation
The 10 most common tissue types sampled are:
| Tissue | Count |
|---|---|
| Liver | 97 |
| Mixed viscera | 38 |
| Kidney | 20 |
| Nuptial pad | 9 |
| Heart | 8 |
| Skin | 8 |
| Blood | 6 |
| Small intestine | 6 |
| Lung | 5 |
| Mixed tadpole viscera | 5 |

Liver dominates (41% of samples), creating a strong bias toward hepatotropic virus detection. Only 7 species (all caecilians from *Caecilia*, *Typhlonectes*, *Rhinatrema*, and *Microcaecilia* genera) were sampled across ≥3 distinct tissue types, with *Caecilia tentaculata* sampled across 9 tissues (foregut, heart, kidney, liver, lung, muscle, skin, spleen, testis).

### 2.3 Geographic and Platform Diversity
- Samples originate from **≥20 countries**, with French Guiana (n=40), China (n=32), USA (n=28), Unknown (n=22), and Australia (n=17) contributing most.
- Sequencing platforms include Illumina HiSeq 2000/2500/4000, NextSeq 500, HiSeq X Ten, 454 GS FLX/Junior, and Illumina Genome Analyzer II — introducing platform-level read-quality heterogeneity.
- **6 novel virus families/genera** were discovered (phylogenetic trees shown for Bunyavirales, Rhabdoviridae/Lyssaviridae, Hepeviridae, Astroviridae, Orthomyxoviridae, Caliciviridae), all identified via BLAST of protein databases against assembled transcriptomic contigs.

---

## 3. Reasoning

The strong tissue bias (41% liver, only 7 species with ≥3 tissues sampled) means viral discovery is almost certainly incomplete for the 116 species sampled from a single tissue. Caecilian species with multi-tissue sampling already yielded novel viruses from multiple families. The dataset structure allows a direct test of whether tissue breadth per host species predicts virome diversity — a question with major implications for surveillance design, because RNA viruses with restricted organ tropism would be missed by single-tissue surveys. Furthermore, the 6 discovered virus families span RNA virus orders with very different replication niches (cytoplasmic vs nuclear, positive vs negative sense), suggesting that herptile viromes are architecturally diverse and largely uncharacterised. The dataset is uniquely positioned to address whether viral richness per species scales with number of tissues sampled.

---

## 4. Top Scientific Question

**Do the number of distinct tissue types sampled per host species predict the total number of novel RNA virus families detected in that species' transcriptomes across the 236-accession herptile RNA-seq dataset?**

---

## 5. Testability on the Provided Dataset

This question is directly testable using the metadata in Supplementary Table 1 combined with the phylogenetic/discovery results in the five supplementary figures. For each of the 123 species, one can count (a) the number of distinct tissues sampled (from the "Tissue" column) and (b) the number of novel virus families detected (from the figures, which annotate host species per virus clade). A Spearman or Poisson regression of viral family richness on tissue-type count, controlling for total read depth (linked via SRA accession), would directly answer whether sampling strategy — not just host biology — drives the apparent viral diversity gap between caecilians (multi-tissue) and the majority of reptiles (single-tissue). The test requires no additional data beyond what is present in this supplementary document.
