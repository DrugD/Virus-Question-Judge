# Report — Invertebrate RNA Virosphere Dataset

## 1. Data summary

The `data/` directory contains two files:

- `5905698_all_virus_genomes.fasta` (~13.6 MB): a multi-FASTA of **2,339 viral nucleotide sequences** representing genomes or genome segments. Headers follow the convention `<libraryID>_<supergroup>_<virusName>[_<segment/protein>]_len<N>`, e.g. `BHWZXX13371_Astro-Poty_Beihai_astro-like_virus_len6856`, `BHBJDX18821_Bunya-Arena_Beihai_shrimp_virus_3_RdRp_len10960`.
- `5905695_alignments_and_phylogenies.zip` (~516 KB): 60 files — trimmed amino-acid alignments (`*_RdRp_trimmed_alignment.fas`) and Newick phylogenies (`*_RdRp_phylogeny.nwk`) for 19 RNA-virus supergroups, plus a `RdRp_versus_structural/` sub-folder containing **paired RdRp vs. structural-protein (capsid S-domain, A6, A21, Alverna, etc.) trees for the same viruses** in 6 supergroups (hepe, luteo, narna, permutotetra, tombus, weivirus).

Library prefixes (e.g. `BH*`=Beihai, `WH*`=Wuhan, `WZ*`=Wenzhou, `CJ*`=Changjiang, `QTM*`, `SCM*`, `tick*`, `spider*`, `mos*`, `arthropodmix*`) link each genome back to one of ~12 geographic sampling sites in China and to invertebrate host pools (insects, spiders, ticks, mosquitoes, flies, crabs, shrimp, sipunculid worms, leeches, cockroaches, millipedes, etc.).

## 2. Analysis (derived from the files)

1. **Supergroup distribution (RdRp-defined).** The 22 labelled supergroups are dominated by *Picorna-Calici* (n=603), *Tombus-Noda* (277), *Bunya-Arena* (249), *Partiti-Picobirna* (205), *Luteo-Sobemo* (174), *Narna-Levi* (167), *Reo* (159), *Mono-Chu* (123), *Hepe-Virga* (101), *Orthomyxo* (64), *Toti-Chryso* (62), *Flavi* (46) — including newly-erected lineages *Wei/Qin/Zhao/Yan/Yuevirus*. Of the 2,339 records, **~1,153 (49%) carry an explicit segment/protein tag** (`_RdRp_`, `_Glycoprotein_`, `_Nucleoprotein_`, `_Capsid_`, `_VP[1-7]_`, numeric segment indices), evidence of segmented-genome architectures across many supergroups.
2. **Genome length distribution.** Per-sequence `len` tags give n=2,338, min=799 nt, median≈4,467 nt, mean≈5,752 nt, max=30,353 nt. The long tail (>20 kb) corresponds to *Mono-Chu* / *Nido* large negative-sense and nidoviral genomes; short sequences (<1 kb) are largely *Narna-Levi* / partitivirus segments.
3. **Host × geography matrix.** Beihai (558), Wuhan (279), Hubei (775), Wenzhou (161), Sanxia (82), Wenling (80), Shahe (88), Changjiang (66) etc.; host classes include insect (107), spider (102), shrimp (68), tick (55), fly (49), mosquito (38), crab (31), worm (30). Most novel virus names use the pattern `<location>_<host>-like_virus_<n>` (e.g. *Beihai picorna-like virus 1–101*; 405 sequences carry a `picorna-like_virus` epithet, 128 `tombus-like`, 102 `sobemo-like`).
4. **RdRp vs structural-protein phylogenies.** The `RdRp_versus_structural/` folder pairs RdRp trees with capsid/structural-domain trees (S-domain, A6, A21, Alverna) for the *same* taxa across hepe, luteo, narna, permutotetra, tombus, weivirus supergroups — explicitly designed to detect topological discordance, i.e. **modular reassortment / horizontal gene transfer of replicase vs. virion modules**.

## 3. Reasoning

The dataset's three most distinctive features are (a) extreme phylogenetic breadth across invertebrate hosts at a continental scale, (b) explicit host and geographic metadata embedded in every header, and (c) curated RdRp vs. structural-protein alignment pairs. Feature (c) is rarely shipped with virus surveys and is the clearest "scientific affordance" of the package: it directly enables a tanglegram / topological-congruence analysis of the replicase versus capsid evolutionary histories. Feature (b) lets us test whether viral diversity tracks host phylogeny (co-divergence) or geography (cross-species spillover within ecosystems). Feature (a) — the discovery of dozens of basal lineages bridging plant, fungal and animal virus families — argues for invertebrates as the evolutionary cradle of RNA viruses.

## 4. Top scientific question

**Across the six RNA virus supergroups (hepe, luteo, narna, permutotetra, tombus, weivirus) for which paired RdRp and structural-protein alignments and phylogenies are provided, do the replicase (RdRp) and virion-structural (capsid S-domain / A6 / A21 / Alverna) trees show statistically significant topological incongruence indicative of widespread modular horizontal gene transfer of replicase versus virion modules during invertebrate RNA-virus evolution?**

## 5. Why this question is testable on the provided dataset

The `RdRp_versus_structural/` directory uniquely provides matched alignments and ML trees keyed to the *same* sequence identifiers (e.g. `Hepe_BHZY60925` appears as both an RdRp tip and an Sdomain tip). This permits a direct quantitative comparison: (i) reconcile the two trees per supergroup with tanglegram / nodal-distance metrics (Robinson–Foulds, MAST, ICONG, PACo); (ii) calibrate against the parametric expectation under co-evolution by permutation; (iii) localise discordant clades and overlay them with the host/location tags from `5905698_all_virus_genomes.fasta` headers to see whether reassortment events cluster by host taxon (e.g. shrimp, spider) or sampling site (e.g. Beihai). All inputs needed — the 12 paired `*_trimal.fas` alignments and corresponding `.nwk` trees plus the labelled genome FASTA — are present in the upload, and the analysis requires no wet-lab work.
