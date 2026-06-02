# Technical Report: Viral Discovery in Reptile and Amphibian Transcriptomes

## 1. Data Summary

**File:** `data/43705_2022_180_MOESM1_ESM.docx` — Supplementary materials from a viral metagenomics study of herpetofauna (reptiles and amphibians). The document contains:

- **Supplementary Table 1**: A dataset inventory of 235 publicly available RNA-Seq samples (from NCBI SRA and ENA) used for viral discovery by transcriptome mining.
- **Supplementary Figures 1–5**: Phylogenetic trees of novel viruses discovered through BLAST-based searches against herptile transcriptomes, covering Bunyavirales, lyssaviruses (Rhabdoviridae), Hepeviridae, Astroviridae, an influenza-like orthomyxovirus, and a calicivirus.

**Table schema:** Species (common name), Scientific name, Animal type (Amphibian/Reptile), SRA Accession, Country of origin, Tissue, Sequencing platform.

**Scale:** 235 samples × 7 fields; 122 unique species; 40 amphibian and 82 reptile species.

---

## 2. Analysis

### 2.1 Sample composition and taxonomic breadth

| Category | Count |
|---|---|
| Total samples | 235 |
| Amphibian samples | 79 (34%) |
| Reptile samples | 156 (66%) |
| Unique amphibian species | 40 |
| Unique reptile species | 82 |
| Unique countries represented | 29 |

### 2.2 Tissue representation and sampling bias

Liver is by far the most sampled tissue (97/235 samples, 41%), driven largely by reptile samples. Mixed viscera accounts for 38 samples (16%). Amphibian-specific tissues include nuptial pad (n=9), skin (n=8), and secretory glands (mental, femoral, pectoral, axillary). Reptile-enriched tissues include liver (82/156 = 53%) and small intestine (6, all Burmese python *Python bivittatus*).

Tissue distribution by animal type:
- **Amphibians**: Liver (15), nuptial pad (9), skin (8), lung (5), mixed tadpole viscera (5), kidney (5)
- **Reptiles**: Liver (82), mixed viscera (35), kidney (15), blood (6), small intestine (6), heart (6)

### 2.3 Novel viral families identified per phylogenetic analysis

Five distinct viral families were discovered via transcriptome mining (BLAST against NCBI protein database + RAxML phylogenetics, 500 bootstrap replicates):

1. **Bunyavirales** — novel reptile viruses; nucleoprotein (582 aa) phylogeny (Fig. 1)
2. **Rhabdoviridae / Lyssavirus** — alligator-associated rabies lyssavirus and anole lyssa-like virus; N-gene phylogeny (Fig. 2). The alligator-associated virus falls within the *Lyssavirus* genus alongside classical rabies virus.
3. **Hepeviridae** — novel amphibian and reptile hepeviruses; separate non-structural and structural (capsid) gene phylogenies (Fig. 3B, D)
4. **Astroviridae** — novel amphibian and reptile astroviruses with a recombination breakpoint in the genome (Fig. 3A, C)
5. **Orthomyxoviridae** (influenza-like) — newt influenza virus in *Cynops pyrrhogaster* (Japan); PB1 phylogeny (Fig. 4)
6. **Caliciviridae** — newt calicivirus (7390 nt polyprotein) in *Cynops pyrrhogaster* (Fig. 5)

### 2.4 Species with replicated samples enabling within-lineage analysis

| Species | Samples | Tissues covered |
|---|---|---|
| *Thamnophis elegans* (W. garter snake) | 13 | Liver (13 individuals, USA) |
| *Pelodiscus sinensis* (Chinese softshell turtle) | 11 | Liver |
| *Python bivittatus* (Burmese python) | 11 | Liver, small intestine |
| *Microcaecilia unicolor* | 10 | Skin, foregut, kidney, liver, muscle, lung |
| *Caecilia tentaculata* | 10 | 9 distinct tissues |
| *Rhinatrema bivittatum* | 9 | 7 distinct tissues |

### 2.5 Library preparation heterogeneity

39/235 samples (17%) used polyA selection (marked with * in Supplementary Table 1), which reduces recovery of non-polyadenylated RNA viruses. Platforms span Illumina HiSeq 2000/2500/4000, NextSeq 500, legacy Illumina Genome Analyzer II, and 454 GS FLX/Junior. This heterogeneity is a potential confounder for comparative viral prevalence analyses across taxa.

---

## 3. Reasoning

The discovery of a rabies lyssavirus (family Rhabdoviridae, genus *Lyssavirus*) associated with an American alligator (*Alligator mississippiensis*, SRR629636, liver tissue) is the most scientifically consequential finding in this dataset. Classical rabies virus (RABV) causes ~59,000 human deaths annually and has long been considered restricted to mammals as competent hosts. The phylogenetic placement of the alligator-associated rabies lyssavirus within the *Lyssavirus* genus (Fig. 2), close to RABV, challenges this paradigm and raises urgent questions about the evolutionary host range of Lyssavirus, cross-order transmission potential, and whether reptiles serve as a reservoir for lyssavirus lineages ancestral to mammalian rabies.

The dataset includes multiple crocodilian representatives (American alligator SRR629636, Chinese alligator SRR957515/SRR4210197/SRR4212880/SRR4212883, Siamese crocodile SRR1612398/SRR1693772), spanning two continents (USA, China) and multiple tissues (liver, blood, kidney), enabling phylogenetic and prevalence comparisons within Crocodylia. The multi-tissue caecilian and lizard sampling further supports tissue-tropism analyses for co-discovered viral families (Hepeviridae, Astroviridae).

---

## 4. Top Scientific Question

Does the alligator-associated rabies lyssavirus identified in *Alligator mississippiensis* liver transcriptome (SRR629636) form a sister lineage to mammalian rabies virus or represent a more divergent lyssavirus clade, and does its N-gene nucleotide identity to classical RABV fall below the 80% species-demarcation threshold established by the International Committee on Taxonomy of Viruses?

---

## 5. Why This Question Is Testable on the Provided Dataset

The dataset provides SRA accessions for American alligator (SRR629636), Chinese alligator (SRR957515, SRR4210197, SRR4212880, SRR4212883), and Siamese crocodile (SRR1612398, SRR1693772) liver/blood/kidney transcriptomes. Supplementary Figure 2 already demonstrates that viral contigs were assembled and a partial N-gene phylogeny was produced using RAxML with 500 bootstrap replicates. The question is directly testable by: (1) extracting lyssavirus-like contigs from the listed SRA runs via de novo assembly, (2) translating and aligning the N-gene against GenBank lyssavirus reference sequences using MAFFT, (3) computing pairwise nucleotide identities, and (4) placing the novel sequences in a maximum-likelihood tree. All required data (SRA accessions, tissue source, animal taxonomy) are enumerated in Supplementary Table 1, and the phylogenetic framework is already established in Fig. 2.
