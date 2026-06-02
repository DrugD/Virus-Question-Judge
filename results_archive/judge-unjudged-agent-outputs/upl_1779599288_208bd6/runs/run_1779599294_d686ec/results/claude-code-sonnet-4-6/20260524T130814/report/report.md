# Technical Report: Novel Invertebrate RNA Viruses — Sequence Analysis

## 1. Data Summary

**File:** `data/nuccore_reported_viral_sequences.fasta`
**Size:** 320,534 bytes; 313,499 total nucleotides
**Sequences:** 33 entries spanning accessions KR902709.1–KR902741.1

The dataset contains complete genome sequences of 18 novel RNA viruses discovered from diverse invertebrate and one vertebrate host. Two distinct genome architectures are represented:

- **Segmented viruses (4-segment):** 5 viral species × 4 segments = 20 sequences. Species include *Wuhan cricket virus* (strain WHXS-1), *Wuhan flea virus* (strain WHZM), *Wuhan aphid virus 1* (WHYC-1), *Wuhan aphid virus 2* (WHYC-2), and *Shuangao insect virus 7* (SKC).
- **Polyprotein (non-segmented) viruses:** 13 viral species, each a single complete genome. Hosts include spider, tick, mosquito, fly, centipede, barnacle, lacewing, water strider, cricket, and shark.

Hosts span 5 invertebrate orders plus one vertebrate (shark). Most sequences originate from field surveys in Wuhan, China (17 sequences), with additional isolates from Xinzhou, Shuangao, Beihai, Wenling, Shayang, and one record from Gamboa (Gamboa mosquito virus).

---

## 2. Analysis

### Statistic 1: Genome Size Bimodality by Architecture
Segmented virus segments range from 1,845–3,170 bp (mean 2,687 bp per segment; total genome ~10.4–11.0 kb). Non-segmented polyprotein genomes range from 9,653 bp (*Wenling shark virus*) to 26,315 bp (*Gamboa mosquito virus*, mean 19,981 bp). This ~2× size difference reflects fundamentally distinct coding strategies.

### Statistic 2: Conserved Segment-Size Hierarchy
Across all five segmented viruses, segment lengths consistently follow the ordering **seg1 > seg3 ≈ seg4 > seg2** (e.g., Wuhan aphid virus 1: 3,156 > 2,841 ≈ 2,829 > 2,166 bp). Intra-virus GC variance per segmented virus is uniformly low (0.37–1.17), indicating coordinated genome composition within each viral species consistent with co-packaging constraints.

### Statistic 3: GC Content Variation Across Host Groups
Mean GC content differs markedly between host-associated viral lineages: tick-associated viruses average 50.1% GC (*Bole tick virus 4*: 56.1%; *Tacheng tick virus 8*: 44.1%), the shark virus reaches 55.2%, while centipede and water strider viruses are AT-rich (35.2% and 34.3%). Segmented insect viruses cluster narrowly at 38–47% GC. This inter-lineage GC divergence exceeds the intra-virus segment variance by an order of magnitude, suggesting host-driven or clade-specific nucleotide compositional pressures.

### Statistic 4: Polyprotein Genome Size Scales with Host Taxonomic Distance from Insects
The largest polyprotein genomes belong to viruses with arthropod hosts phylogenetically distant from the segmented-virus insect hosts (mosquito: 26,315 bp; spider × 2: 24,521 and 21,414 bp; centipede: 23,676 bp), while the vertebrate-infecting shark virus is the smallest polyprotein genome (9,653 bp). This raises questions about whether genome expansion is linked to host range breadth or replication compartment.

---

## 3. Reasoning

The dataset captures two phylogenetically distinct RNA virus lineages co-sampled from overlapping geographic regions and partially overlapping host taxa (e.g., both segmented and non-segmented viruses found in crickets: *Wuhan cricket virus* [segmented] and *Xingshan cricket virus* [polyprotein]). This dual-architecture, multi-host dataset is ideally suited to test whether genome architecture (segmented vs. polyprotein) correlates with host-switching breadth or with nucleotide compositional adaptation to host biology. The highly conserved segment-size hierarchy (Statistic 2) across all five segmented viruses implies strong purifying selection on segment identity, while the large GC divergence between tick and insect viruses (Statistic 3) suggests lineage-specific compositional drift. Together, these patterns motivate asking whether the segmented genome architecture constrains or facilitates host range compared with the polyprotein strategy.

---

## 4. Top Scientific Question

**Do the four-segment genome-architecture RNA viruses (Wuhan cricket virus, Wuhan flea virus, Wuhan aphid virus 1, Wuhan aphid virus 2, Shuangao insect virus 7) exhibit significantly lower host-range breadth and higher between-segment GC covariation than the co-sampled polyprotein-encoding invertebrate RNA viruses (KR902729–KR902741), indicating that segmented genome organization imposes a co-packaging constraint that restricts cross-order host switching in invertebrate RNA virome evolution?**

*(Copied verbatim from `agent_questions.json`, rank 1.)*

---

## 5. Testability on the Provided Dataset

This question is directly testable using the sequences in `nuccore_reported_viral_sequences.fasta`:

1. **GC covariation test:** Compute pairwise GC correlations across the four segments of each segmented virus; compare with nucleotide compositional similarity of polyprotein genomes from the same host orders. The data show intra-virus GC variance of 0.37–1.17 for segmented viruses, providing a baseline.
2. **Host-range breadth proxy:** Count distinct arthropod orders represented among hosts of segmented vs. polyprotein viruses using the header metadata. Segmented viruses are found only in Insecta (3 orders: Orthoptera, Siphonaptera, Hemiptera), while polyprotein viruses span Insecta, Arachnida, Myriapoda, Crustacea, and Chondrichthyes—a measurable breadth difference.
3. **Segment co-occurrence analysis:** The strict 4-segment organization and conserved size hierarchy (seg1 > seg3 ≈ seg4 > seg2 across all 5 species) quantify the co-packaging signature; divergence from this hierarchy would signal reassortment or host switching.

All three analyses require only the sequence headers and nucleotide compositions already extracted from the single FASTA file provided.
