# Technical Report: RNA Virome of Invertebrates — Scientific Question Analysis

## 1. Data Summary

Two files were provided under `data/`:

| File | Size | Description |
|------|------|-------------|
| `5905698_all_virus_genomes.fasta` | 13.0 MB | 2,339 RNA virus genome/segment sequences from invertebrate metatranscriptomics |
| `5905695_alignments_and_phylogenies.zip` | 504 KB | 60 files: 20 RdRp-based phylogenies (Newick), 20 trimmed RdRp multiple-sequence alignments, and 20 supplementary structural-protein alignments/trees, including a `RdRp_versus_structural/` subdirectory with paired RdRp and capsid-protein phylogenies for congruence analysis |

The FASTA headers encode rich metadata in a structured `<ID>_<superfamily>_<location>_<virusname>_len<N>` format. **22 distinct virus superfamilies** (Picorna-Calici, Tombus-Noda, Bunya-Arena, Partiti-Picobirna, Luteo-Sobemo, Narna-Levi, Reo, Mono-Chu, Hepe-Virga, Orthomyxo, Toti-Chryso, Flavi, Permutotetra, New-Weivirus, New-Qinvirus, Nido, Astro-Poty, New-Zhaovirus, New-Yanvirus, New-Yuevirus, Hypo, Birna) and ~1,885 distinct virus names are represented, sourced from sampling sites across China (Hubei, Beihai, Wuhan, Wenzhou, Changjiang, Sanxia, Shahe, Wenling, and others). Invertebrate hosts include arthropods, crustaceans, molluscs, nematodes, and marine invertebrates.

---

## 2. Analysis

**Statistic 1 — Genome size distribution:**
Across 2,339 sequences: mean 5,749 bp, median 4,467 bp, Q1 2,724 bp, Q3 8,935 bp, range 799–30,353 bp.  Size classes: <3 kb = 705 (30%), 3–6 kb = 638 (27%), 6–12 kb = 891 (38%), 12–20 kb = 92 (4%), >20 kb = 13 (<1%). Most RNA virus families fall in the 3–12 kb range typical of positive-sense or small negative-sense genomes; 13 sequences exceed 20 kb.

**Statistic 2 — Nidovirus genome lengths in invertebrate hosts:**
The 12 Nido-group sequences range from 5,040 bp (a shrimp gill-associated virus segment) to 30,353 bp (Xinzhou toro-like virus), with 8 of 12 exceeding 15 kb. This contrasts with vertebrate nidoviruses (coronaviruses ~30 kb) and, critically, substantially extends the known size range of invertebrate RNA virus genomes, suggesting that large-genome complexity among RNA viruses is not restricted to vertebrate-infecting lineages.

**Statistic 3 — Novel lineage discovery:**
Five entirely new virus superfamilies are represented — New-Weivirus (21 sequences), New-Qinvirus (17), New-Zhaovirus (9), New-Yanvirus (5), New-Yuevirus (4) — accounting for 56 sequences with no prior classification. Four of these new lineages (Weivirus, Qinvirus, Zhaovirus, Yuevirus) have dedicated RdRp phylogenies in the ZIP, and all four have sequences with characteristics (e.g., ciliate genetic code usage in New-Qinvirus and New-Zhaovirus) suggesting protozoan or unicellular eukaryote hosts embedded within broader invertebrate sampling pools.

**Statistic 4 — RdRp versus structural protein phylogenies:**
The `RdRp_versus_structural/` subdirectory contains paired RdRp and structural-protein (capsid S-domain, A21, A6, Alverna fold) PhyML trees for the same taxa across six virus groups (Hepe, Luteo, Narna, Permutotetra, Tombus, Weivirus). The paired Newick files allow direct topological comparison to test whether the replication machinery (RdRp) and capsid proteins share congruent evolutionary histories — a test for RNA virus modularity and capsid gene exchange across lineages.

---

## 3. Reasoning

The combination of (a) a massive, broadly-sampled invertebrate RNA virome, (b) 20 RdRp-centric phylogenies spanning established and entirely novel superfamilies, and (c) paired structural-protein phylogenies for the same virus sets creates a uniquely powerful comparative framework. The most scientifically significant opportunity is to ask whether the evolutionary history inferred from RdRp — the universally conserved replication marker — is congruent with the evolutionary history inferred from capsid/structural proteins. Incongruence would indicate modular evolution or capsid gene exchange between distantly related lineages, reshaping our understanding of how RNA virus diversity arose. The dataset provides not just the sequences but already-computed, publication-grade phylogenies for exactly this comparison.

---

## 4. Top Scientific Question

**Do the RdRp-based and structural-protein-based phylogenies of the invertebrate RNA viruses in `RdRp_versus_structural/` show statistically congruent topologies across the Hepe-Virga, Luteo-Sobemo, Narna-Levi, Permutotetra, Tombus-Noda, and New-Weivirus lineages, or do systematic incongruences implicate modular capsid evolution and inter-lineage structural gene exchange in the diversification of the invertebrate RNA virome?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The `RdRp_versus_structural/` subdirectory contains six pairs of trimmed multiple-sequence alignments (`.fas`) and PhyML Newick trees (`.nwk`) for matched RdRp and structural protein sequences from the same virus sets. Topological congruence can be assessed directly by (i) computing the Robinson-Foulds distance between each paired RdRp and structural tree, (ii) performing AU tests or SH tests using the alignments against the alternative topologies, and (iii) visualising tanglegrams of the paired trees. All required inputs — alignments and trees — are present in the provided ZIP file. No additional wet-lab data are needed.
