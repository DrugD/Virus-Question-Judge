# Technical Report: Arthropod-Associated RNA Virus Diversity Dataset

## 1. Data Summary

Two files constitute this dataset:

| File | Size | Description |
|---|---|---|
| `5905698_all_virus_genomes.fasta` | 13.6 MB | 2,339 RNA virus genome or segment sequences |
| `5905695_alignments_and_phylogenies.zip` | 516 KB | 20 trimmed RdRp multiple-sequence alignments (.fas) + PhyML phylogenies (.nwk), plus 10 structural-protein alignments/trees in a `RdRp_versus_structural/` subdirectory |

**FASTA header format:** `{SampleID}_{SupergroupLabel}_{VirusName}[_Segment]_len{NtLength}`

The 2,339 sequences span **22 virus supergroups**: Picorna-Calici (603), Tombus-Noda (277), Bunya-Arena (249), Partiti-Picobirna (205), Luteo-Sobemo (174), Narna-Levi (167), Reo (159), Mono-Chu (123), Hepe-Virga (101), Orthomyxo (64), Toti-Chryso (62), Flavi (46), Permutotetra (25), New-Weivirus (21), New-Qinvirus (17), Nido (12), Astro-Poty (10), New-Zhaovirus (9), New-Yanvirus (5), New-Yuevirus (4), Hypo (4), and Birna (2).

Sampling sites are predominantly coastal and riverine China: Beihai (558 seqs), Wuhan (279), Wenzhou (161), Wenling (80), Changjiang (66), Xinzhou (20). Hosts are exclusively invertebrates: spiders, ticks, mosquitoes, flies, crabs, shrimp, centipedes, barnacles, isopods, nematodes, crickets, and mixed arthropod pools.

---

## 2. Analysis

### 2.1 Sequence Length Distribution

Genome/segment lengths range from **799 bp to 30,353 bp** (mean = 5,752 bp, n = 2,338 with parseable length fields). The broad range reflects single-segment genomes (Picorna-Calici, mean ~8–10 kb), multi-segment genomes counted individually (Bunya-Arena RdRp ~6.5 kb, glycoprotein ~1.8 kb, nucleoprotein ~1.8 kb), and very short sub-genomic entries.

### 2.2 Supergroup and Host Cross-Distribution

Cross-tabulating supergroup labels with host terms embedded in sequence names reveals extensive host-range breadth within single supergroups:

- **Picorna-Calici** infects shrimp (18 seqs), insects (12), worms (8), crabs (8), spiders (5), mosquitoes (5), isopods (5), applesnails (6), and barnacles.
- **Bunya-Arena** (negative-sense) spans mosquitoes (12), insects (8), crabs (5), shrimp (6), and ticks.
- **Orthomyxo** includes mosquito (8) and earthworm (6) lineages.
- **Luteo-Sobemo** spans shrimp (7), mosquitoes (6), and centipedes (6).

Among the 22 supergroups, four bear "New-" prefixes (New-Weivirus, New-Qinvirus, New-Zhaovirus, New-Yanvirus, New-Yuevirus), indicating previously unclassified virus families discovered in this survey.

### 2.3 Alignment and Phylogenetic Coverage

The 20 per-supergroup RdRp trimmed alignments range from **5 sequences** (New-Yanvirus) to **533 sequences** (Picorna-Calici). Per-alignment sequence counts: Picorna-Calici 533, Tombus-Noda 294, Narna-Levi 195, Partiti-Picobirna 185, Negative_Mono-Chu 170, Luteo-Sobemo 165, Hepe-Virga 164, Negative_Bunya-Arena 171, Reo 86, Toti-Chryso 110, Negative_Orthomyxo 34, Nido 36, Permutotetra 24, New-Weivirus 21, Hypo 13, Astro-Poty 15, Birnaviridae 10, New-Qinvirus 9, New-Zhaovirus 9, New-Yanvirus 5.

The `RdRp_versus_structural/` subdirectory contains paired alignments of RdRp domains versus structural proteins (capsid fold families A6, A21, Alverna, S-domain) for six RNA supergroups, enabling direct comparison of replication-module versus structural-module phylogenies.

### 2.4 Proportion of Novel Lineages

Of 2,339 sequences, approximately 56 (2.4%) belong to the four formally unnamed "New-*" supergroups. These are placed in their own alignment+tree files, signaling that they represent divergent clades without prior classification. Their occurrence in diverse arthropod hosts (nematodes, insects, crabs) broadens the known host range for unclassified RNA virus families.

---

## 3. Reasoning

The dataset's most distinctive feature is the combination of: (a) 22 RNA virus supergroups spanning both positive-sense and negative-sense genomes, (b) sampling exclusively from invertebrate hosts across multiple phyla, and (c) paired RdRp + structural-protein phylogenies for six supergroups. This architecture was explicitly designed to test whether the evolutionary history of RNA virus replication modules (RdRp) is congruent with the evolutionary history of their structural modules — a test of RNA virus modular evolution via recombination/reassortment. The broad arthropod host sampling provides the ecological interface where cross-phylum host-jumps and inter-supergroup recombination are most likely to have occurred. The "New-*" supergroups, identifiable from the data, are precisely those predicted to occupy intermediate phylogenetic positions if such recombination events shaped current RNA virus diversity.

---

## 4. Top Scientific Question

**Do the RdRp-based and structural-protein-based phylogenies of invertebrate RNA viruses within the Tombus-Noda, Luteo-Sobemo, Hepe-Virga, Narna-Levi, Permutotetra, and Weivirus supergroups show topological incongruence consistent with ancient modular recombination events, as revealed by the paired trimmed alignments and PhyML trees in `RdRp_versus_structural/`?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The `RdRp_versus_structural/` subdirectory contains both a trimmed RdRp alignment and a matching structural-protein alignment for each of the six listed supergroups, alongside PhyML maximum-likelihood trees for each. Topological congruence between each RdRp tree and its corresponding structural tree can be directly assessed using tree-comparison statistics (Robinson-Foulds distance, ICONG, or Shimodaira-Hasegawa tests) computed from the `.nwk` files. Significant incongruence — taxa whose structural genes group with a different supergroup's clade than their RdRp — would constitute evidence for ancient recombination between replication and structural modules. All necessary alignments and trees are available in the uploaded files, making this a fully self-contained computational test.
