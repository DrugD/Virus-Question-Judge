# Technical Report: Viral Metagenome Analysis of "Hirai" Sample

## 1. Data Summary

The dataset comprises 10 FASTA files totalling ~570 KB and 488 sequences from a viral metagenomics study (accession prefix LC651635–LC651651, deposited 2021, designated "Hirai"):

| File | Sequences | Description |
|---|---|---|
| `16945969_31356130_Hirai_Contigs_RdRp.fas` | 194 | All Hirai RdRp-bearing contigs, named by family similarity |
| `16958869_31373884_Possible_virus_contigs.fas` | 37 | Contigs with no BLAST hit to known virus families ("nohit") |
| `nuccore_reported_viral_sequences.fasta` | 17 | Complete CDS sequences deposited in NCBI (LC651635–651651) |
| `16945426_31352578_Partitiviridae_alignment.fas` | 67 | RdRp MSA: 56 known + 11 Hirai Partitiviridae-like |
| `16945477_31352614_Totiviridae_alignment.fas` | 44 | RdRp MSA: 34 known + 10 Hirai Totiviridae-like |
| `16945423_31352587_Picornavirales_alignment.fas` | 37 | RdRp MSA: 36 known + 1 Hirai Picornavirus-like |
| `16945456_31352599_Pocobirnaviridae_alignment.fas` | 32 | RdRp MSA: 25 known + 7 Hirai Picobirna-like |
| `16945462_31352605_Reoviridae_alignment.fas` | 26 | RdRp MSA: 25 known + 1 Hirai Reovirus-like |
| `16945363_31352431_chrysoviridae_alignment.fas` | 22 | RdRp MSA: 21 known + 1 Hirai Chrysovirus-like |
| `16945399_31352560_Narnaviridae_alignment.fas` | 10 | RdRp MSA: 8 known + 2 Hirai Narnavirus-like |

The 7 phylogenetic alignment files each contain known reference sequences from fungal/invertebrate-infecting RNA viruses aligned with novel Hirai contigs, enabling family-level placement of novel sequences. The Narnaviridae alignment includes fungal mitoviruses (*Ophiostoma*, *Cryphonectria*, *Saccharomyces*), consistent with a fungus-associated source.

## 2. Analysis

### 2.1 Family-level composition of the Hirai virome

Among the 194 RdRp-bearing contigs, 16 viral lineages were identified by sequence similarity:

- **Partiti-like**: 82 contigs (42.3%) — largest component
- **Toti-like**: 37 contigs (19.1%)
- **Picobirna-like**: 23 contigs (11.9%)
- **Reo-like**: 14 contigs (7.2%)
- **Narna-like**: 10 contigs (5.2%)
- **Endorna-like**: 7 (3.6%), **Hypo-like**: 4 (2.1%), **Virga-like**: 3 (1.5%)
- **Unclassified ssRNA**: 3, **Unclassified dsRNA**: 3 (3.1% combined)
- **Picorna-like**, **Megabirna-like**, **Chryso-like**, **Chu-like**, **Solemo-like**, **Tombus-like**: 1–2 each

The dominance of Partitiviridae and Totiviridae (both primarily fungal RNA viruses) strongly implies the "Hirai" sample is a fungus-associated metagenome.

### 2.2 Completeness and sequence-length statistics

- **12 complete RdRp contigs** (6.2% of 194); 182 are partial assemblies.
- Complete contig lengths range from **1,639 nt** (LC651647, Picobirna-like) to **11,845 nt** (LC651648, Hypo-like polyprotein).
- **17 sequences** formally deposited in NCBI (LC651635–LC651651), all annotated as "Viral metagenome 2021-JH."
- Partial RdRp contig lengths: min 484 nt, max 11,845 nt, mean 1,253 nt.

### 2.3 Novel "no-hit" contigs and phylogenetic placement

- **37 Hirai_nohit contigs** (in `16958869_31373884_Possible_virus_contigs.fas`) have no assignable family by BLAST, yet two carry structural hallmarks of viruses: `Hirai_virus_hypothetical_protein` and `Hirai_virus_capsid`. Sequence lengths range from ~500 to 3,440 nt.
- **33 Hirai contigs** were placed into 7 family-level phylogenetic alignments, spanning 6 viral families (Chryso-, Narna-, Picorna-, Partiti-, Pocobirnavirus, Reo-, Totiviridae).
- The Picornavirales alignment features **Hirai_contig_2** alongside bee-infecting picorna-like viruses (Slow bee paralysis virus, Acute bee paralysis virus, Israeli acute paralysis virus, Kashmir bee virus), suggesting this contig may infect an invertebrate host rather than a fungus.

## 3. Reasoning

The co-occurrence of 37 "no-hit" contigs alongside 194 classified RdRp contigs in a single metagenome raises a critical question: are the no-hit contigs remnants of genuinely novel, phylogenetically isolated viral lineages, or do they represent technical artifacts (assembly chimeras, host-encoded RNA-dependent polymerases, or highly diverged members of known families detectable only by structural homology)? The dataset provides exactly the evidence needed to address this: (1) paired capsid/hypothetical protein sequences for one of the nohit viruses (`Hirai_virus_capsid`, `Hirai_virus_hypothetical_protein`) allows multi-gene genome characterization; (2) the 7 curated phylogenetic alignments—spanning 205 known reference sequences—offer calibrated evolutionary distances for comparison; and (3) the 17 formally deposited NCBI sequences provide validated complete genome references from the same sample to benchmark contig quality.

## 4. Top Scientific Question

**Do the 37 no-BLAST-hit contigs from the Hirai viral metagenome (including `Hirai_virus_capsid` and `Hirai_virus_hypothetical_protein`) represent novel RNA virus families phylogenetically distinct from the 16 classified lineages (Partiti-like, Toti-like, Picobirna-like, etc.) identified in the same sample?**

## 5. Why This Question Is Testable on the Provided Dataset

The question is directly addressable using the files at hand. The `16958869_31373884_Possible_virus_contigs.fas` file contains the 37 no-hit sequences, two of which encode a putative capsid protein and a hypothetical protein that can be used for secondary structure–based homology searches (e.g., HHpred, Dali, or AlphaFold2). The seven multi-sequence alignments (`Partitiviridae`, `Totiviridae`, `Pocobirnaviridae`, `Reoviridae`, `Chrysoviridae`, `Narnaviridae`, `Picornavirales`) embed the Hirai classified contigs within a reference framework of 205 known viral sequences, providing the evolutionary scale needed to classify or reject placement of nohit contigs into those families. Pairwise distance and phylogenetic analysis using the RdRp alignment backbone can determine whether nohit sequences cluster within, sister to, or entirely outside all known family-level clades. The 17 NCBI-deposited sequences (`nuccore_reported_viral_sequences.fasta`) from the same "2021-JH" metagenome serve as positive controls for assembly quality and genome completeness.
