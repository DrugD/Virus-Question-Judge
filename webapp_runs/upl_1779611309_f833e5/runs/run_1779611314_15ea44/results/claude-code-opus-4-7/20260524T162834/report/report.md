# Report: Scientific question generation from a Hirai-study viral RdRp dataset

## 1. Data summary

The `data/` directory contains 10 FASTA files totalling ~570 KB:

- **Seven family-level RdRp alignments** (amino-acid, gapped): `chrysoviridae` (22 seqs), `Narnaviridae` (10), `Picornavirales` (37), `Partitiviridae` (67), `Pocobirnaviridae`/Picobirnaviridae (32), `Reoviridae` (26) and `Totiviridae` (44). Each alignment mixes named GenBank/RefSeq references (e.g. `AJ781166`, `NC_001479_Cardiovirus_A`, `KR902507_Equine_picobirnavirus`, `BAU79524_Diatom_colony_associated_virus`) with `Hirai_contig_*` query sequences placed at homologous RdRp positions.
- **`16945969_31356130_Hirai_Contigs_RdRp.fas`** — 194 nucleotide contigs (mean length 1254 nt, median 992 nt, max 11 846 nt) carrying RdRp-like ORFs. Header taxonomy strings show: 82 *Partiti-like*, 37 *Toti-like*, 23 *Picobirna-like*, 14 *Reo-like*, 10 *Narna-like*, 7 *Endorna-like*, 4 *Hypo-like*, 3 *Virga-like*, 2 *Picorna-like*, 2 *Megabirna-like*, 1 each of *Tombus-like*, *Solemo-like*, *Chu-like*, *Chryso-like*, plus 6 *Unclassified ssRNA/dsRNA*. Twelve are flagged `complete` (with linked GenBank IDs `LC651635`–`LC651650`); 182 are `partial`.
- **`16958869_31373884_Possible_virus_contigs.fas`** — 37 nucleotide contigs (`Hirai_nohit1`–`Hirai_nohit35`, plus `Hirai_virus_hypothetical_protein` and `Hirai_virus_capsid`) with no BLAST hits to known viruses.
- **`nuccore_reported_viral_sequences.fasta`** — 17 GenBank-deposited "Viral metagenome 2021-JH01…JH17" records (RdRp, capsid, polyprotein, hypothetical proteins) accessions `LC651635.1`–`LC651651.1`.

## 2. Analysis

1. **Taxonomic skew.** Of 194 RdRp contigs, 78% (151) fall into *dsRNA* lineages (Partiti-, Toti-, Picobirna-, Reo-, Chryso-, Megabirna-, Endorna-, Hypo-like; the latter two have dsRNA replication strategies in their mycoviral hosts), versus ~13% in clearly ssRNA(+) lineages (Narna-, Picorna-, Virga-, Tombus-, Solemo-, Chu-like). The dataset is therefore dsRNA-virus-dominated.
2. **Reference composition for the Totiviridae alignment** is enriched for *diatom-* and *aquatic-invertebrate*-associated viruses (`Diatom_colony_associated_dsRNA_virus_3/4/6`, `Diatom_totivirus_1`, `Beihai_victori-like_virus`, `Aedes_camptorhynchus_toti-like_virus`, `Schistocephalus_solidus_toti-like_virus`), suggesting the source sample is a planktonic / aquatic eukaryote community.
3. **Saturation of novelty.** The 12 `complete` Hirai contigs match exactly the 17 deposited `LC651635–LC651651` records (5 of those are non-RdRp partners — capsid/polyprotein/hypothetical), so the published GenBank entries represent <7% of all RdRp contigs detected; 182 partial RdRp contigs and 35 "no-hit" contigs constitute unreported viral diversity captured but not formally described.
4. **Length distribution.** The contig length distribution is heavily right-skewed (median 992 nt, mean 1254 nt, single 11 846 nt outlier — likely a near-complete dsRNA segment), implying most contigs cover only a fragment of the RdRp gene yet still resolve to specific viral families on amino-acid alignment.

## 3. Reasoning

The dataset is structured for **phylogenetic placement and quantification of novel RNA virus diversity** in a single metagenomic survey. The combination of (a) family-stratified RdRp alignments with curated references, (b) hundreds of partially-assembled query contigs annotated with their nearest viral family, and (c) a residual pool of "no-hit" contigs is the canonical input for asking *what new viral lineages exist and how they re-shape known viral phylogeny*. The strong dsRNA bias (esp. Partiti- and Toti-like), together with diatom/marine references in the Toti alignment, motivates a question that interrogates whether the Hirai contigs represent **new family-level branches** (i.e., not just new species inside known families) and whether host signal can be inferred from those branches. This is the highest-leverage scientific question the data can address without wet-lab work.

## 4. Top scientific question

**Do the 194 Hirai RdRp contigs — particularly the 82 Partiti-like and 37 Toti-like sequences — define previously undescribed family- or genus-level clades within the dsRNA virosphere when co-aligned with curated Partitiviridae, Totiviridae, Picobirnaviridae, Reoviridae and Chrysoviridae RdRp references, and do those clades cluster phylogenetically with diatom- or aquatic-invertebrate-associated reference taxa rather than with terrestrial fungal/plant taxa?**

## 5. Why this question is testable on the provided dataset

Every ingredient required is on disk: (i) the seven family-level multiple sequence alignments already place Hirai contigs at homologous RdRp columns alongside type-species references — a maximum-likelihood or Bayesian tree can be inferred directly from each `*_alignment.fas`; (ii) bootstrap support and branch length to the nearest reference quantify whether Hirai contigs form deep, well-supported sister clades (= putative new families/genera) versus terminal twigs nested inside an existing genus; (iii) the reference-tip metadata embedded in headers (host species, e.g. `Diatom_colony_associated_…`, `Eriocheir_sinensis_reovirus`, `Heterobasidion_partitivirus_1`) lets us label internal nodes by host ecology and test the aquatic-vs-terrestrial host-association hypothesis with a phylogenetic ANOVA / parsimony reconstruction. No external data are required.
