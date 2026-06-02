# Report — Scientific Question Generation from `nuccore_reported_viral_sequences.fasta`

## 1. Data summary

`data/` contains a single FASTA file, `nuccore_reported_viral_sequences.fasta`
(~320 kB; 313,499 bp total) with **33 GenBank nucleotide records spanning a
contiguous accession block KR902709.1 – KR902741.1**. Two structural classes
of records are present:

* **Segmented viruses (20 records, 5 viruses × 4 segments).** All four
  segments are reported as "complete sequence" for each strain:
  Wuhan cricket virus (WHXS-1), Wuhan flea virus (WHZM),
  Shuangao insect virus 7 (SKC), Wuhan aphid virus 1 (WHYC-1),
  and Wuhan aphid virus 2 (WHYC-2). Segment lengths cluster tightly
  (seg1 ≈ 3.0–3.2 kb; seg2 ≈ 1.8–2.2 kb; seg3 ≈ 2.7–2.9 kb;
  seg4 ≈ 2.7–2.9 kb), consistent with a shared 4-segmented genome
  architecture.
* **Unsegmented "polyprotein gene, complete cds" records (13 records).**
  Lengths 9.7–26.3 kb, characteristic of large positive-sense ssRNA
  virus polyproteins. Hosts named in the headers include
  shark (Wenling shark virus), spiders (Xinzhou spider virus 2 & 3,
  Shayang spider virus 4), barnacle (Beihai barnacle virus 1),
  fly (Shayang fly virus 4), mosquito (Gamboa mosquito virus),
  lacewing, centipede, cricket, water strider, and ticks.

The accessions and naming conventions (Wuhan/Shuangao/Xinzhou/Beihai/Tacheng…)
match the published Shi et al. invertebrate RNA virosphere series, so this
dataset is best interpreted as a **curated invertebrate-/arthropod-centric
RNA virus reference panel** plus one vertebrate (shark) outlier.

## 2. Analysis (derived statistics)

1. **Genome architecture distribution.** 5/18 viruses (28%) are 4-segmented;
   13/18 (72%) are unsegmented polyprotein-encoding. All five 4-segmented
   viruses come from terrestrial arthropod hosts (cricket, flea, aphid×2,
   "insect"); none of the polyprotein viruses are reported as segmented.
2. **Length distribution.** Segmented-virus entries: 1,845–3,170 bp
   (median 2,770). Polyprotein entries: 9,653–26,315 bp (median ≈ 20.4 kb;
   Gamboa mosquito virus is the longest at 26,315 bp). The bimodal length
   distribution cleanly separates the two genome classes.
3. **GC content.** Per-virus mean GC ranges from **34.3% (Sanxia water
   strider virus 6)** to **56.1% (Bole tick virus 4)**, a >20-percentage-point
   spread. Within each segmented virus the four segments are tightly clustered
   (e.g. Wuhan flea virus: 44.3–47.2%; Wuhan cricket virus: 38.4–41.1%),
   indicating co-replication, while the polyprotein records show host-linked
   structure (the two tick-borne viruses, Bole tick virus 4 56.1% and
   Tacheng tick virus 8 44.1%, are markedly higher than spider/centipede
   viruses at 35–37%).
4. **Host taxonomy.** 17/18 viruses are invertebrate-associated; one
   (Wenling shark virus) is the only vertebrate-associated polyprotein
   virus and has the highest GC of any unsegmented entry (55.2%), making
   it a clear outlier worth flagging.

## 3. Reasoning

The dataset is a small but **structurally rich reference panel**: it
deliberately pairs a 4-segmented genome architecture (5 strains, full
segment sets) against a phylogenetically diverse set of large
polyprotein-encoding ssRNA virus genomes spanning >10 distinct invertebrate
host orders plus a vertebrate. Because every segmented virus has all four
segments and because GC content varies systematically with host, the data
support comparative-genomics questions about how genome architecture and
nucleotide composition co-vary with host phylogeny — a central open
question in the invertebrate RNA virosphere literature.

The most non-trivial scientific opportunity is therefore **not** "what
viruses are here?" (the headers already say) but **whether host taxonomy
predicts genome architecture and base composition** across this panel,
because that links a sequence-level signal to ecology and to potential
host-switching / emergence risk.

## 4. Top scientific question

> **Across the 18 invertebrate-associated RNA viruses in this KR902709–KR902741 panel, does host phylum/class (e.g. Insecta vs Arachnida vs Crustacea vs Chilopoda vs Chondrichthyes) systematically predict whether the virus has a segmented four-piece genome architecture versus a single large polyprotein-encoding genome, and is host-class also reflected in segment-length conservation and per-genome GC content?**

## 5. Why this question is testable on the provided dataset

* **Genome architecture label** is recoverable directly from the FASTA
  headers: 20 records say "segment N, complete sequence" and 13 say
  "polyprotein gene, complete cds" — a clean binary outcome.
* **Putative host class** is encoded in every virus name (cricket/aphid/
  fly/mosquito/lacewing → Insecta; spider → Arachnida; tick → Arachnida-
  Acari; barnacle → Crustacea; centipede → Chilopoda; shark →
  Chondrichthyes; flea → Insecta-Siphonaptera; water strider → Insecta-
  Hemiptera) and can be coded as a categorical predictor.
* **Segment-length conservation** is computable: across the five 4-segment
  strains, segment-1 lengths span only 3,040–3,170 bp, segment-2 1,845–
  2,236 bp, etc., so a within-segment ANOVA / coefficient-of-variation
  analysis is feasible with n = 5 strains per segment.
* **GC content** is a one-line calculation per record (already shown to
  range 34.3–56.1%), enabling a Fisher's-exact / logistic test of
  architecture ~ host-class and a Kruskal-Wallis test of GC ~ host-class.
* No external data or wet-lab assays are required; everything needed is
  in the 33 FASTA records and their header annotations.
