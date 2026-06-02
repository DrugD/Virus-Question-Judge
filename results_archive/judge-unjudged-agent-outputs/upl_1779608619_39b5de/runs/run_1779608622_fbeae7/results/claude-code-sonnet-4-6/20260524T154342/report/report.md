# Technical Report: Vertebrate Virome Discovery across Chordata

## 1. Data Summary

Three supplementary files accompany a Nature 2018 paper (DOI prefix 41586_2018_12) by Yong-Zhen Zhang and colleagues describing a large-scale metagenomic virus-discovery survey of vertebrates spanning the entire phylum Chordata.

| File | Contents | Scale |
|---|---|---|
| `41586_2018_12_MOESM1_ESM.pdf` | Life Sciences Reporting Summary — experimental design, software, animal collection details | 2 pages |
| `41586_2018_12_MOESM2_ESM.xlsx` | Library inventory (Supplementary Table 1): 126 metatranscriptomic libraries from 186+ host species | 130 rows × 9 columns |
| `41586_2018_12_MOESM3_ESM.xlsx` | Virus discovery table (Supplementary Table 2): 270 newly discovered or divergent viral sequences, each with classification, genome accession, tissue source, coverage, and host metadata | 274 rows × 18 columns |

**MOESM2 columns:** Library name, Library Code, Host Class, Host Orders, Host Species, Host Organ, Locations, Data (bp), Library Accession.

**MOESM3 columns:** Order, Library, Identification, Classification, Virus Name, Strain, Segment (protein), Tissue, Accession, Length, % reads, Coverage, Host code, Host class, Host order, Host species, Blastx hits on known viruses (blast amino acid identity), Note.

Host classes represented: Actinopterygii (bony fish), Chondrichthyes (cartilaginous fish), Reptilia, Amphibia, Agnatha (jawless fish), Sarcopterygii (lobe-finned fish/lungfish), and Leptocardii (lancelets). Total sequencing data: ~806 Gbp across 126 libraries; sampling spanned gut, liver, gill, and lung tissues.

---

## 2. Analysis

### Statistic 1 — Virus family richness and dominant families

The 270 viral sequences span more than 20 virus families. The five most abundant families are:
- **Astroviridae**: 65 entries (host range: all six vertebrate classes, from hagfish to reptiles)
- **Picornaviridae**: 46 entries (Actinopterygii, Reptilia, Amphibia)
- **Caliciviridae**: 24 entries (mostly Actinopterygii)
- **Orthomyxoviridae (Influenza virus)**: 18 entries (Actinopterygii, Amphibia, Agnatha)
- **Flaviviridae: Hepacivirus (HCV-like)**: 15 entries (Chondrichthyes, Reptilia, Actinopterygii, Sarcopterygii)

Astroviridae stands out as the most host-generalist family, detected across all sampled vertebrate classes.

### Statistic 2 — Amino acid divergence from known viruses

Blastx amino acid identity to previously known viruses was parsed from 264 of 270 entries. Mean identity = **38.4%**; the distribution is:
- < 30%: 59 viruses (22%) — highly divergent
- 30–39%: 120 viruses (45%) — moderately divergent
- 40–49%: 51 viruses (19%)
- 50–59%: 19 viruses (7%)
- ≥ 60%: 15 viruses (6%)

Thus ~67% of discovered viruses share <40% amino acid identity with previously known viruses, confirming the deep novelty of this virome.

### Statistic 3 — Influenza virus phylogenetic breadth and tissue tropism

Three fully or partially segmented influenza-like viruses (18 genome segments total) were discovered in non-avian, non-mammalian vertebrates:
- **Wuhan spiny eel influenza virus** (*Mastacembelus aculeatus*, Actinopterygii) — all 8 canonical segments present (PB2, PB1, PA, NP, HA, NA, MP, NS; accessions MG600037–MG600044); detected in **gill** tissue.
- **Wuhan asiatic toad influenza virus** (*Bufo gargarizans*, Amphibia) — 6 segments; detected in **lung** tissue.
- **Wenling hagfish influenza virus** (*Eptatretus burgeri*, Agnatha) — 4 segments; detected in **gill** tissue.

This represents the first discovery of influenza-like viruses in jawless vertebrates (hagfish) and bony fish, extending the host range of Orthomyxoviridae far beyond birds and mammals.

### Statistic 4 — Hepacivirus (HCV-like) tissue restriction

All 15 hepacivirus-like sequences were detected exclusively in **liver** tissue, across phylogenetically distant hosts: sharks and rays (Chondrichthyes, 8 entries), reptiles (5 entries), bony fish (1), and lungfish (1). This liver tropism conservation across ~500 million years of vertebrate evolution mirrors the hepatotropism of human Hepatitis C virus.

---

## 3. Reasoning

The most striking finding in the data is the discovery of complete, all-8-segment influenza-like virus genomes in a bony fish (spiny eel), accompanied by related but segment-reduced influenza viruses in a frog and a hagfish. Influenza viruses are clinically critical zoonotic pathogens responsible for seasonal epidemics and pandemic threats; their evolutionary origin and the identity of ancient reservoir hosts have been debated for decades. Prior to this dataset, influenza-like viruses were only known from birds, mammals, and one fish species (*Tilapia*, with a 4-segment form). The recovery of a full 8-segment genome from a non-avian, non-mammalian bony fish — combined with partial genomes in phylogenetically basal vertebrates (hagfish, Agnatha) — establishes that the influenza virus lineage predates the divergence of jawed and jawless vertebrates. These data directly permit phylogenetic reconstruction of the deep evolutionary history of influenza virus and, through ancestral state reconstruction, can reveal which genome segments are ancestral vs. derived, which vertebrate lineage(s) served as the evolutionary reservoir, and whether segment gain or loss occurred during radiation into endothermic hosts.

---

## 4. Top Scientific Question

**Do the all-8-segment influenza-like virus genome from the spiny eel (*Mastacembelus aculeatus*, Actinopterygii) and the related partial genomes from the Asiatic toad (*Bufo gargarizans*, Amphibia) and hagfish (*Eptatretus burgeri*, Agnatha) represent ancestral lineages from which avian and mammalian influenza A viruses evolved, and can phylogenetic analysis of the PB2, PB1, PA, NP, HA, NA, MP, and NS segments (accessions MG600037–MG600054) resolve the deep evolutionary origin and segment composition history of the Orthomyxoviridae within vertebrates?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The dataset contains complete genome accessions (MG600037–MG600054) and amino acid identity figures for all three novel influenza-like viruses alongside their host taxonomy (Host class, Host order, Host species columns in MOESM3) and tissue of detection (Tissue column). Combined with publicly available influenza A/B/C/D protein sequences, maximum-likelihood or Bayesian phylogenetic trees can be built for each of the 8 segments using the software already described in the Reporting Summary (MAFFT, Trimal, PhyML, MrBayes). The presence of all canonical segments in the eel virus and reduced segment counts in hagfish allows formal testing of segment gain/loss models. Co-divergence analysis (Jane4, also listed in the software section) can further test whether virus–host co-speciation explains the phylogenetic topology. All key variables — segment identity, host phylogenetic position, tissue tropism, and genome coverage — are directly encoded in MOESM3.
