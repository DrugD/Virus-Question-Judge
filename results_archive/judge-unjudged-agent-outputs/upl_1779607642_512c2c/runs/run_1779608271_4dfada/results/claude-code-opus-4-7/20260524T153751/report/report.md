# Tick Virome Report — TIGMIC Metagenomic FASTA Survey

## 1. Data summary

`data/` contains a single multi-FASTA file,
`nuccore_reported_viral_sequences.fasta` (~11.9 MB), holding **1,801 viral
nucleotide sequences** retrieved from NCBI nuccore. Accession prefixes are
`ON746xxx` (n=1,680) and `ON811xxx` / `ON812xxx` (n=121), consistent with a
single bulk submission. Every header carries the project tag
`isolate TIGMIC[_ ]N` (1,801 / 1,801), indicating a coordinated
tick-virome metagenomics study; **1,700** are flagged `MAG:` and
**101** are `MAG UNVERIFIED:`. Headers encode three orthogonal pieces of
structured metadata: (i) a Chinese geographic descriptor (e.g. *Nanning*,
*Hulunbuir*, *Zhangzhou*, *Tianjin*, *Kashgar*, *Yanbian*, *Wuhan*),
(ii) a viral taxonomic anchor — either a family-level placeholder
(`Totiviridae sp.`) or a named "tick virus" species (`Yanbian Nairo tick
virus 2`) — and (iii) an isolate counter. 1,228 records are marked
`complete genome`.

## 2. Analysis

* **Length distribution.** Lengths span **803 nt – 22,791 nt**, mean
  6,432 nt, median 6,498 nt, P10 ≈ 2,259 nt, P90 ≈ 11,681 nt — a mixture
  of small mycovirus-like RNAs and full segmented/non-segmented
  RNA-virus genomes.
* **Family composition (≥21 viral families).** Largest groups:
  *Totiviridae* 244, *Botourmiaviridae* 180, *Narnaviridae* 91,
  *Rhabdoviridae* 72, *Mitoviridae* 52, *Partitiviridae* 44,
  *Nairoviridae* 41, *Flaviviridae* 40, *Orthomyxoviridae* 37,
  *Phenuiviridae* 35, *Peribunyaviridae* 32, *Reoviridae* 20,
  *Chuviridae* 20, *Iflaviridae* 19. Vertebrate-pathogen-relevant families
  total ~190 records (Nairo-, Phenui-, Flavi-, Orthomyxo-,
  Peribunyaviridae) and include explicit hits such as
  `Nairobi sheep disease virus` (ON811840.1), `Brown dog tick
  phlebovirus 1/2`, `Sara tick phlebovirus`, and `Trinbago virus`.
* **Length × family bimodality.** Mean lengths split cleanly along
  expected genome architectures: small fungal/protist mycovirus
  families (*Botourmiaviridae* 2,537 nt, *Narnaviridae* 2,379 nt,
  *Mitoviridae* 2,399 nt, *Partitiviridae* 1,761 nt) versus
  arthropod/vertebrate RNA viruses (*Flaviviridae* 15,238 nt,
  *Rhabdoviridae* 10,904 nt, *Chuviridae* 10,866 nt, *Nairoviridae*
  10,594 nt). This bimodality signals two ecological compartments
  captured in the same tick samples.
* **Geographic granularity.** Header prefixes resolve to **≥30 Chinese
  city/region origins** (Hulunbuir, Tonghua, Lianyungang, Zhangzhou,
  Tianjin, Kashgar, Tongren, Alashan, Yanbian, Shanxi, Wuhan, Henan,
  Dabieshan, …); 131 distinct *location*+*family* combinations are
  encoded.
* **Diversity / novelty signal.** 362 distinct species labels — **282
  are singletons**, only 80 have ≥2 isolates. Site-prefixed naming
  (`Nanning Botou tick virus 1`, `Yanbian Nairo tick virus 2`) shows
  multiple geographically distinct novel viruses per family.

## 3. Reasoning

The dataset is structurally a **biogeographic virome catalogue**: every
sequence is jointly tagged with locality + viral family + project ID,
and ~190 records (≈11 %) fall in vector-borne pathogen families
(Nairo-, Phenui-, Flavi-, Orthomyxo-, Peribunyaviridae). Two priorities
emerge. First, the heavy long tail of singleton species (282 / 362)
within tick samples is precisely the regime in which **previously
undescribed tick-associated viruses with zoonotic potential** are
typically uncovered, and the family-level priors here (CCHFV-relatives
in *Nairoviridae*, SFTSV-relatives in *Phenuiviridae*) make this
directly actionable through RdRp/L-segment phylogenetics. Second, the
explicit geographic stratification across a continental gradient (from
subtropical Zhangzhou/Nanning, through arid Kashgar, to boreal
Hulunbuir) means the dataset can answer **whether and where
zoonotic-adjacent diversity concentrates** — a foundational question
for tick-borne disease surveillance. The top-1 question targets exactly
this intersection because it (a) names specific families and pathogen
references present in the file, (b) names the spatial axis encoded in
the headers, and (c) is testable end-to-end with sequence alone.

## 4. Top scientific question

> Within the 1,801 TIGMIC tick-derived metagenome-assembled sequences
> spanning 21 viral families and >30 Chinese sampling localities, which
> Nairoviridae- and Phenuiviridae-assigned contigs encode RdRp/L-segment
> ORFs that place phylogenetically sister to known human or livestock
> pathogens (e.g. CCHFV, SFTSV, Nairobi sheep disease virus), and how is
> that zoonotic-adjacent diversity geographically structured across the
> sampled Chinese sites?

## 5. Why this question is testable on the provided dataset

Every input needed is in the FASTA:

* **Family labels** are already in the headers (`Nairoviridae sp.`,
  `Phenuiviridae sp.`, plus locality-prefixed `Nairo tick virus` and
  `phlebovirus` species), so the family-level subset (41 + 35 = 76
  records) can be extracted by simple header parsing.
* **Sequence length** of these subsets (~10.6 kb and ~6.8 kb means)
  indicates many are long enough to contain the L-segment / full RdRp
  ORF needed for phylogenetics.
* **Reference anchors** are present in the file itself
  (`Nairobi sheep disease virus`, `Brown dog tick phlebovirus 1/2`,
  `Sara tick phlebovirus`), and external pathogen references (CCHFV,
  SFTSV, Heartland, Bhanja-group) are publicly available — so the
  sister-clade test is a standard ORF-call → HMMER/DIAMOND →
  multi-sequence alignment → IQ-TREE workflow.
* **Geographic axis** is encoded directly in the species names of >30
  localities, so each placement can be tagged to a city/region without
  needing extra metadata.

Pass/fail of the question is therefore decidable purely from
`data/nuccore_reported_viral_sequences.fasta` plus public reference
sequences, with no wet-lab work required.
