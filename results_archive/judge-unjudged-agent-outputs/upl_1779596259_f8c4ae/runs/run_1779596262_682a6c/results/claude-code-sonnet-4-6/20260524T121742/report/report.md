# Technical Report: Novel Invertebrate RNA Virus Survey

## 1. Data Summary

The dataset contains two files:

| File | Size | Description |
|------|------|-------------|
| `nuccore_reported_viral_sequences.fasta` | ~1.06 MB | 170 nucleotide sequences from GenBank (KM817593–KM817764) |
| `elife-05378-supp-v1.zip` | ~5.2 MB | Three EPS figure supplements from eLife paper e05378 |

The FASTA file contains sequences associated with the Shi et al. 2015 study (eLife paper e05378), which reported a large-scale metatranscriptomic survey of RNA viruses from diverse invertebrate arthropods and other invertebrates collected across China. Sequences represent 170 entries encoding viral genes: primarily RNA-dependent RNA polymerase (L gene, n=77 entries annotated), glycoprotein (G, n=50), nucleocapsid (N, n=48), matrix protein (n=13), phosphoprotein (n=11), and PB1 segments (n=14). Seven entries represent complete genomes; 138 represent complete CDS; 16 are partial CDS. The 170 sequences derive from ~170 distinct virus/strain/gene combinations spanning at least 90 named novel viral species.

**Host distribution:** Tick-associated viruses dominate (n=38 sequences), followed by fly/louse-fly viruses (n=37), insect/unspecified (n=27), mosquito (n=25), spider (n=12), aquatic invertebrates—shrimp and crab (n=9), water strider (n=7), cockroach (n=6), millipede (n=3), bedbug (n=3), ant (n=1).

**Geographic origin:** All viruses are named after Chinese localities—Wuhan (n=59), Shuangao (n=20), Tacheng (n=10), Wenzhou/Whenzhou (n=12), Shayang (n=8), and ~18 other sites across China.

---

## 2. Analysis

### 2.1 Sequence Length Distribution by Host Taxon

| Host group | N sequences | Mean length (bp) | Range (bp) |
|------------|-------------|-----------------|------------|
| Tick | 38 | 7,147 | ~800–15,000+ |
| Fly/Louse-fly | 37 | 6,430 | ~600–15,462 |
| Mosquito | 25 | 5,218 | ~600–10,000 |
| Spider | 12 | 6,262 | — |
| Aquatic (shrimp/crab) | 9 | 6,056 | — |
| Cockroach | 6 | 4,000 | — |
| Other insects | 27 | 5,764 | — |

Tick-associated viruses have the longest mean sequence length (~7,147 bp vs. 5,218 bp for mosquito viruses), consistent with tick-borne viruses encoding more complex multi-gene arrangements.

### 2.2 Genomic Completeness and Gene Content

- **7 complete genomes** (unsegmented or fully reconstructed)
- **138 complete CDS** entries
- **16 partial CDS**
- **53 sequences** annotated as encoding only RNA-dependent RNA polymerase (L gene alone), suggesting many novel viruses were detected by polymerase phylogeny but not fully sequenced
- **15 sequences** encode the full mononegavirales-like repertoire (N + G + L), indicative of rhabdovirus-like or paramyxovirus-like architectures
- **14 PB1-containing sequences**, indicating orthomyxovirus-like segmented negative-sense RNA viruses from multiple invertebrate hosts

### 2.3 GC Content Variation

Across all 170 sequences:
- **Minimum GC:** 24.7%
- **Maximum GC:** 60.0%
- **Mean GC:** 41.4%

The wide GC range (35.3 percentage points) across arthropod RNA viruses is substantially broader than typically seen within a single established viral family, reflecting the taxonomic diversity of these viruses spanning multiple families and possible novel clades.

### 2.4 Viral Architecture Diversity

The dataset encodes representatives of at least four major genome architectures:
1. **Mononegavirales-like** (N+G+L mono-partite negative-sense): ~15+ complete entries
2. **Bunyavirus/phlebovirus-like** (segmented N+G+L with ORF2/NSs): present in tick and water-strider viruses
3. **Orthomyxovirus-like** (PB1-bearing segmented): n=14
4. **Novel/unclassified** (L gene only or novel ORF arrangements): n=53+

---

## 3. Reasoning

The dataset represents a landmark systematic discovery of RNA viruses from ecologically diverse Chinese invertebrates. The most scientifically compelling observation is the **unprecedented breadth of viral genomic architectures and apparent host-virus associations** encoded across arthropod lineages. Specifically:

- Tick-associated viruses are over-represented and carry the longest and most complete genomes, while they are also known to be medically important vectors. Yet a large fraction of all viruses (~31%) have only the RNA polymerase sequenced, leaving phylogenetic placement and host range unresolved.
- The PB1-bearing orthomyxovirus-like group spans mosquitoes, flies, louse flies, water striders, spiders, and cockroaches—host orders that span hundreds of millions of years of divergence—raising a fundamental question about whether host ecology (blood-feeding vs. predation vs. detritivory) predicts viral genome architecture.
- The distinct GC% distribution and gene content across host-specific viral clusters suggest host-associated evolutionary pressures that could be quantitatively tested with the existing L gene sequences.

---

## 4. Top Scientific Question

**Do the RNA-dependent RNA polymerase (L gene) phylogenies of the novel invertebrate viruses recovered from blood-feeding arthropods (ticks, mosquitoes, louse flies) form host-ecology-associated clades distinct from those infecting non-blood-feeding invertebrates (spiders, cockroaches, water striders, millipedes) in the KM817593–KM817764 sequence set, indicating that hematophagous feeding behavior is a consistent predictor of arthropod-virus phylogenetic clustering?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The dataset includes 77 L gene (RNA-dependent RNA polymerase) sequences across arthropods with documented feeding ecologies: blood-feeders (ticks, mosquitoes, louse flies, horseflies) and non-blood-feeders (spiders, cockroaches, water striders, millipedes, ants, bedbugs). A multiple sequence alignment of the L gene sequences (extractable directly from `nuccore_reported_viral_sequences.fasta`) followed by maximum-likelihood or Bayesian phylogenetic reconstruction would produce a tree in which nodes can be labeled by host feeding ecology. Ancestral state reconstruction or permutation tests (e.g., BaTS, ANOVA on phylogenetic distances) can then quantify whether blood-feeding vs. non-blood-feeding host ecology is a significant predictor of viral clade membership. All necessary sequences are present in the FASTA file; no wet-lab experiments are required.
