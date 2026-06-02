# Report — Invertebrate RNA Virus Discovery Dataset

## 1. Data summary

The upload contains two artifacts in `data/`:

- **`5905698_all_virus_genomes.fasta`** — a 13.6 MB nucleotide FASTA with **2,339 viral contigs** totalling ~13.45 Mb. Headers follow a consistent schema `>{LibraryID}_{Clade}_{VirusName}_[Segment_]len{N}` (e.g. `BHWZXX13371_Astro-Poty_Beihai_astro-like_virus_len6856`). Mean contig length ≈ 5,749 nt (median 4,454 nt; max 30,353 nt).
- **`5905695_alignments_and_phylogenies.zip`** — 60 files: 20 per-clade RdRp trimmed amino-acid alignments (`*_RdRp_trimmed_alignment.fas`) with matching Newick phylogenies (`*_RdRp_phylogeny.nwk`), plus a `RdRp_versus_structural/` sub-directory pairing RdRp alignments/trees with structural-protein (capsid S-domain, A6/A21/Alverna jelly-roll variants, etc.) trees for hepe-, luteo-, narna-, permutotetra-, tombus- and weivirus clades.

The header tokens reveal **22 viral super-clades** (Picorna-Calici 603 contigs, Tombus-Noda 277, Bunya-Arena 249, Partiti-Picobirna 205, Luteo-Sobemo 174, Narna-Levi 167, Reo 159, Mono-Chu 123, Hepe-Virga 101, Orthomyxo 64, Toti-Chryso 62, Flavi 46, Permutotetra 25, plus several "New-" putative phyla — Wei/Qin/Zhao/Yan/Yue — and Astro-Poty, Birna, Hypo, Nido). Library prefixes such as **BH** (Beihai), **WH/WHCC** (Wuhan), **WZ** (Wenzhou), **CJ/CJLX** (Changjiang), **SH/SX**, plus host-pool tags (`spider`, `tick`, `mosHB`, `arthropodmix`) encode geography (Hubei 775, Beihai 558, Wuhan 279, Wenzhou 161, Shahe 88, Sanxia 82, Changjiang 66 …) and invertebrate host group.

## 2. Analysis

**(i) Segment / protein content.** Of 2,339 contigs, 206 headers explicitly carry `_RdRp_`, 89 `_Nucleoprotein_`, 64 `_Glycoprotein_`, 68 `Capsid` — i.e., for negative-sense and segmented clades (Bunya-Arena, Mono-Chu, Orthomyxo, Reo, Partiti) multiple cognate segments from the same library are recoverable, enabling intra-virus segment co-occurrence analysis.

**(ii) Phylogenetic depth per clade.** Tree tip counts span three orders of magnitude — Picorna-Calici (≈1,062 tips), Tombus-Noda (≈585), Narna-Levi (≈387), Partiti-Picobirna (≈367), Bunya-Arena (≈339), Mono-Chu (≈337) down to New-Yanvirus (≈7) and Hypo (≈23). Trimmed alignments are a downsampled subset (e.g. Picorna-Calici 533 vs 1,062 tips), confirming the trees mix new contigs with reference taxa.

**(iii) RdRp-vs-structural decoupling.** The `RdRp_versus_structural/` sub-folder provides paired trees over the *same* taxa using either the RdRp polymerase domain or independent capsid-fold proteins (S-domain, jelly-roll A6/A21/Alverna, hepe/luteo/narna/permuto/tombus/weivirus). Visual inspection of leaves shows shared taxon labels across the two marker trees in each pair — the explicit design of this sub-directory is a **module-incongruence test for modular evolution / inter-clade recombination of RNA-replication and capsid genes**.

## 3. Reasoning

Three observations point to one dominant scientific opportunity. (a) The corpus samples a single ecological context — Chinese invertebrate metatranscriptomes — but spans nearly every Baltimore RNA-virus class, including five putative new phylum-level groups, so it is unusually well-suited to ask phylum-level evolutionary questions. (b) The directory is *deliberately* split into RdRp trees and structural-protein trees over matched taxa, which only matters if the authors anticipated **topological discordance**. (c) The host-tag prefixes (`spider`, `tick`, `mosHB`, `arthropodmix`) plus geographic codes give a host × location matrix that lets any inferred recombination event be polarised against ecology.

Together these motivate asking whether the polymerase and capsid modules have evolved as a coherent unit or whether modular reassortment has shaped the invertebrate RNA virosphere — a question with direct biomedical and surveillance significance, since modular gene flow blurs taxonomy and confounds host-range prediction for emerging zoonoses.

## 4. Top scientific question

**Across the 22 invertebrate RNA-virus clades represented in `5905698_all_virus_genomes.fasta`, do RdRp-based phylogenies (e.g. `Hepe-Virga_RdRp_phylogeny.nwk`, `Luteo-Sobemo_RdRp_phylogeny.nwk`) and matched structural-protein phylogenies in `RdRp_versus_structural/` (capsid S-domain, jelly-roll A6/A21/Alverna) exhibit topological incongruence indicative of widespread modular recombination between replication and structural genes during the diversification of the invertebrate RNA virosphere?**

## 5. Why this question is testable on the provided dataset

The `RdRp_versus_structural/` directory was constructed precisely to support this comparison: it contains *paired* trimmed amino-acid alignments and Newick trees for the RdRp domain *and* for independent structural markers (S-domain, A6/A21/Alverna jelly-roll variants) over matched taxa for hepe-, luteo-, narna-, permutotetra-, tombus- and weivirus clades. A standard test pipeline is therefore: (1) read taxon-matched leaves from each RdRp/structural Newick pair; (2) compute Robinson–Foulds, matching-cluster, or quartet distances and compare against null distributions of randomised trees with the same tip set; (3) localise discordant clades using SH or AU topology tests and visualise with tanglegrams; (4) cross-reference incongruent taxa with library/host prefixes (`spider`, `tick`, `mosHB`, BH/WH geography) in the FASTA headers to test whether putative module swaps cluster by host or sampling site. No external data are required, and the file inventory in `info.json` confirms every input listed above is present.
