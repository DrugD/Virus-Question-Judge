# Technical Report: Invertebrate RNA Virosphere Dataset

## 1. Data Summary

Two files were provided under `data/`:

| File | Size | Description |
|---|---|---|
| `5905698_all_virus_genomes.fasta` | 13.6 MB | Full-genome nucleotide FASTA sequences |
| `5905695_alignments_and_phylogenies.zip` | 516 KB | Trimmed amino-acid alignments (RdRp and structural proteins) and PhyML phylogenetic trees in Newick format |

**FASTA file structure:** Each header follows the pattern `<sample_ID>_<family_group>_<location>_<virusname>_[segment_]len<nt>`. The dataset contains **2,339 sequences** representing **1,886 distinct virus genomes/segments** across **22 RNA virus family-level groups**, collected from diverse invertebrate hosts across multiple sampling sites in China (Hubei, Beihai, Wuhan, Wenzhou, Wenling, Shahe, Sanxia, Changjiang, and others).

**Alignment/phylogeny ZIP contents:** 20 trimmed RdRp protein alignment + PhyML tree pairs spanning the major RNA virus lineages, plus a `RdRp_versus_structural/` subdirectory containing 6 paired RdRp/structural protein alignments (4 structural domain types: S-domain, A6 fold, A21 fold, Alverna) and matching PhyML trees specifically for testing congruence between RNA replication and capsid protein evolution.

---

## 2. Analysis

### Derived Statistic 1 — Taxonomic distribution across 22 RNA virus supergroups
The most species-rich families are Picorna-Calici (603 sequences; avg. genome 9,299 nt), Tombus-Noda (277; avg. 3,629 nt), Bunya-Arena (249; avg. 5,276 nt), Partiti-Picobirna (205; avg. 1,649 nt), and Luteo-Sobemo (174; avg. 2,990 nt). Five putative new families — New-Weivirus, New-Qinvirus, New-Yanvirus, New-Zhaovirus, and New-Yuevirus — collectively contribute 56 sequences whose phylogenetic affinities are unclear or do not match any established taxon.

### Derived Statistic 2 — Host breadth across invertebrate phyla
Sequence headers explicitly name hosts including: mosquitoes (~57), ticks (~55), spiders (~102), shrimp/crustaceans (~68), barnacles (~18), centipedes/myriapods (~56), blood flukes (~22), nematodes (~20), earwigs (~16), crickets (~21), flies (~92), aphids (~12), and isopods (~13). This spans Arthropoda (insects, arachnids, crustaceans, myriapods), Nematoda, Platyhelminthes, and Mollusca — documenting an invertebrate RNA virosphere far broader than previously sampled.

### Derived Statistic 3 — Incongruence between RdRp and structural protein phylogenies
The `RdRp_versus_structural/` subdirectory provides direct evidence for phylogenetic incongruence. The Tombus-Noda RdRp alignment contains 34 taxa, while the S-domain structural protein alignment for the same lineage contains 48 taxa with different compositions; the resulting PhyML trees show different topologies. For example, in the RdRp tree, Flock House Virus and Nodamura Virus (Nodaviridae) cluster with Pariacoto Virus and novel invertebrate sequences, whereas in the S-domain tree, Nodamura Virus relatives cluster with Hepe-Virga-related sequences bearing Alverna/A-fold capsids. Similar incongruences appear for Hepe-Virga (RdRp vs. Alverna structural proteins; 7 vs. 11 taxa) and Narna-Levi (RdRp vs. A21 fold; 4 vs. 10 taxa). These mismatches support an ancient modular evolutionary event in which capsid genes were independently acquired multiple times by lineages sharing the same RdRp ancestry.

---

## 3. Reasoning

The dataset documents the largest survey of RNA viruses from non-vertebrate invertebrate hosts reported at the time of publication (corresponding to Shi et al. 2016, *Nature*). The taxonomic breadth (22 supergroups, 1,886 distinct genomes) and the explicit pairing of RdRp with structural-protein alignments and trees create a uniquely powerful comparative resource. The most scientifically consequential signal in the data is the incongruence between RdRp-based and structural-gene-based phylogenies across multiple lineages (Tombus-Noda, Hepe-Virga, Narna-Levi). This incongruence reveals that the capsid module was not co-inherited with the replication module, implying deep-time recombination or independent horizontal gene acquisition of structural genes — a question that can be tested directly using the provided paired alignments and trees.

---

## 4. Top Scientific Question

**Do the RNA-dependent RNA polymerase (RdRp) and structural protein (capsid S-domain, A6-fold, A21-fold, Alverna-fold) phylogenies of invertebrate RNA viruses spanning the Tombus-Noda, Hepe-Virga, and Narna-Levi supergroups exhibit statistically significant topological incongruence, implying that capsid modules were acquired independently from replication modules during the deep evolution of positive-sense RNA viruses?**

---

## 5. Testability on the Provided Dataset

The question is directly answerable using the resources in `5905695_alignments_and_phylogenies.zip`. The `RdRp_versus_structural/` subdirectory contains paired trimmed protein alignments (e.g., `RdRp_tombus_trimal.fas` / `Structure_Sdomain_trimal.fas`, `RdRp_hepe_trimal.fas` / `Structure_Alverna_trimal.fas`, `RdRp_narna_trimal.fas` / `Structure_A21_trimal.fas`) and their corresponding PhyML-inferred trees. Topological congruence can be quantified using the Robinson-Foulds distance or Shimodaira-Hasegawa tests applied to shared taxa across each RdRp/structural pair. The 1,886 genome sequences in `5905698_all_virus_genomes.fasta` provide the sequence universe from which additional taxa can be drawn to improve resolution. If the RdRp trees and structural trees yield significantly different topologies (as preliminary inspection of the Newick files suggests), this would constitute quantitative evidence for modular evolution and ancient capsid gene exchange across multiple RNA virus supergroups.
