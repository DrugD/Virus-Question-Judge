# Report: Vertebrate (Chordata) RNA Virome Survey — Scientific Question Generation

## 1. Data summary

The `data/` directory contains three supplementary files belonging to a Nature 2018 vertebrate virus discovery study (corresponding author Yong-Zhen Zhang):

- `41586_2018_12_MOESM1_ESM.pdf` — Life Sciences Reporting Summary. It states the goal as a virus-discovery survey of >186 host species across the phylum **Chordata**, using meta-transcriptomic RNA-seq with a fixed bioinformatic pipeline (Trimmomatic → Trinity → BLASTn/x/p → MAFFT → PhyML/MrBayes → BaTS, Jane4 for **virus–host co-divergence**).
- `41586_2018_12_MOESM2_ESM.xlsx` (Sheet1, 130×9) — RNA-seq library inventory: 126 sequencing libraries with columns `Library1, Library Code, Host Class, Host Orders, Host Species, Host Organ, Locations, Data (bp), Library Accession`. Total raw output ≈ **8.06 × 10¹¹ bp**.
- `41586_2018_12_MOESM3_ESM.xlsx` (Sheet1, 274×22) — Virus catalog: 270 virus records with columns including `Classification`, `Virus Name`, `Tissue`, `Accession`, `Length`, `% reads`, `Coverage`, `Host class/order/species`, `Blastx hits on known viruses (blast amino acid identity)`, `Note`.

## 2. Analysis (derived statistics)

**(a) Host‑class coverage.** Libraries span all major non‑mammalian/non‑avian vertebrate classes: Actinopterygii (38 libraries), Chondrichthyes (29), Reptilia (16), Amphibia (15), Agnatha (8), Sarcopterygii (6), plus pooled libraries — covering jawless fish through reptiles. Sampled tissues are dominated by **Gut (45), Liver (33), Gill (30)**, with smaller numbers of Lung and whole-body libraries.

**(b) Virus catalog composition.** Of 270 virus records (228 unique virus names spanning **31 viral families/orders**), the top families are **Astroviridae (57), Picornaviridae (46), Caliciviridae (24), Orthomyxoviridae/Influenza (18), Flaviviridae/Hepacivirus (15), Hantaviridae (15), Reoviridae/Orthoreovirus (11), Arenaviridae (9), Hepeviridae (8)**. The `Note` field labels 236 viruses as "Vertebrate specific", 12 "Putative vertebrate", 16 "Unknown divergent", and 6 "Vertebrate virus related to vector-borne virus".

**(c) Host distribution of viruses.** Virus counts by host class — Actinopterygii 138, Reptilia 50, Chondrichthyes 32, Amphibia 31, Agnatha 15, Sarcopterygii 4 — show that bony fish carry the largest absolute viral diversity, but importantly, **hagfish (Agnatha)** and lungfish/coelacanth-relatives (Sarcopterygii) are also virus-positive, extending many vertebrate-defining families to the deepest vertebrate lineages. Tissue tropism is non-uniform: gut samples yield 110 viruses vs 55 in gill and 32 in liver.

**(d) Sequence divergence.** Parsing the BLASTx hit identities (n=264) gives **mean = 38.4 % aa identity** to closest known virus (min 22 %, max 100 %). The distribution is heavily left-shifted: 87 % of hits fall below 50 % identity (59 < 30 %; 171 in 30–49 %), indicating that the catalog is dominated by **highly novel viruses** rather than near-duplicates of GenBank entries — exactly the regime where co-phylogenetic / ancestral-host inference becomes informative.

## 3. Reasoning

Three observations together motivate the top question. First, the dataset's defining feature is **broad host phylogenetic coverage of Chordata** — every major class from Agnatha to Reptilia is represented (Tab S1). Second, the same virus families recur across distant host classes (e.g., Astroviridae, Picornaviridae, Caliciviridae, Hantaviridae, Arenaviridae, Hepeviridae, Influenza-like Orthomyxoviridae, Hepacivirus), meaning a **family-level phylogeny can be re-rooted with non-mammalian taxa**. Third, the deep BLASTx divergence (mean 38 % aa identity, with 22 % at the floor) implies that the new sequences span most of each family's evolutionary depth, which is a prerequisite for robust **virus–host co-divergence testing** — a method the reporting summary explicitly names (Jane4, BaTS). The natural, non-trivial scientific opportunity is therefore to ask whether the joint phylogenies show co-divergence with vertebrate evolution rather than recent host-switching.

## 4. Top scientific question

**To what extent do the phylogenies of vertebrate-associated RNA virus families recovered across the Chordata (Agnatha → Sarcopterygii → Actinopterygii → Chondrichthyes → Amphibia → Reptilia) — in particular Astroviridae, Picornaviridae, Caliciviridae, Hepeviridae, Hantaviridae, Arenaviridae, Flaviviridae/Hepacivirus and Orthomyxoviridae — exhibit deep co-divergence with their vertebrate hosts versus recent cross-class host switching, and does this push the origins of these families back to the root of the vertebrate lineage?**

## 5. Why this question is testable on the provided dataset

Both supplementary tables supply exactly what the test requires. Tab S1 anchors every library to a specific Host Class, Host Order, and Host Species spanning all major Chordata clades. Tab S2 supplies, per virus, its viral family (`Classification`), accession, contig length, host taxonomy, and BLASTx identity to its closest known relative. With ≥8 viruses in each of the named families and host hits distributed across multiple vertebrate classes (e.g., Astroviridae spans Actinopterygii, Chondrichthyes, Amphibia, Reptilia), one can build per-family virus phylogenies (MAFFT + PhyML/MrBayes — already in the published pipeline) and test topological congruence against the host tree using the named co-divergence and clustering tools (Jane4, BaTS). The deep BLASTx divergence (mean 38 % aa identity) ensures the signal is evolutionary, not epidemiological, so the co-divergence vs host-switch dichotomy is empirically separable from these tables alone.
