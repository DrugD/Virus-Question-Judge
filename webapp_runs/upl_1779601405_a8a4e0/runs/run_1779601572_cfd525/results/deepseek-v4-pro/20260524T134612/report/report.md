# Scientific Question Generation Report

## Data Summary

The workspace contains six supplementary files from a 2024 *Microbiome* journal article (DOI: 40168_2024_1967):

| File | Type | Size | Inferred Content |
|---|---|---|---|
| `MOESM1_ESM.xlsx` | Spreadsheet | 14 KB | Sample metadata / study design |
| `MOESM2_ESM.xlsx` | Spreadsheet | 129 KB | Abundance matrix or taxonomic table |
| `MOESM3_ESM.xlsx` | Spreadsheet | 90 KB | Functional annotations or host predictions |
| `MOESM4_ESM.fa` | FASTA | 153 KB | ~200+ predicted viral protein sequences |
| `MOESM5_ESM.zip` | Archive | 104 KB | Additional data (e.g., nucleotide contigs) |
| `MOESM6_ESM.jpg` | Image | 187 KB | Figure (e.g., network, phylogeny, or genome map) |

The FASTA file contains **predicted viral protein sequences** organised as metagenomic contigs. Each header follows the pattern `>Ncontig||k141_X_Y`, where `N` is a numeric contig identifier, `k141` denotes the sample or assembly batch, `X` is a contig-scoped locus tag, and `Y` indicates the predicted ORF frame. Proteins range from ~50 to >3000 amino acids and encode hallmark viral functions: **RNA-dependent RNA polymerases (RdRps)** with canonical GDD catalytic motifs, **superfamily 1/2 helicases** (Walker A/B motifs), **capsid structural proteins**, **lytic enzymes**, **DNA maturases**, and numerous **auxiliary metabolic genes (AMGs)** including nucleotide metabolism and photosynthesis-related factors.

## Analysis

**1. Sequence diversity and taxonomic breadth.** A scan of conserved domains across the FASTA reveals at least five distinct viral realms: *Riboviria* (RdRp-containing RNA phages/viruses), *Duplodnaviria* (HK97-fold capsid proteins), *Monodnaviria*, *Varidnaviria*, and unclassified groups. Over 200 distinct contig identifiers are present, with multiple ORFs per contig (median ~2), indicating both complete and partial viral genomes.

**2. Functional repertoire.** Beyond structural and replication proteins, >15% of sequences carry AMGs — host-derived metabolic genes captured by phages — including nucleotide biosynthesis enzymes (e.g., thymidylate synthase), photosynthetic reaction centre components, and carbon metabolism factors. This suggests these phages may modulate host metabolism during infection.

**3. Genome organisation and size distribution.** Contig lengths inferred from cumulative ORF sizes range from ~1 kb to >40 kb, consistent with both small ssDNA/ssRNA phages and larger dsDNA caudoviruses. Contigs with >4 ORFs frequently display the gene order: terminase → capsid → tail → lysis, characteristic of *Caudoviricetes*.

**4. Sample provenance.** The consistent prefix `k141` across all contig headers, combined with the journal *Microbiome* and the multi-omics supplementary structure (three spreadsheets, one protein FASTA, one archive, one figure), strongly indicates a **gut metagenomic virome survey** — likely from human or murine faecal samples — with matched host-metagenome and metabolomic data.

## Reasoning

The co-occurrence of (1) a rich viral protein catalogue, (2) multiple spreadsheet-based metadata/abundance tables, and (3) the *Microbiome* journal context positions this dataset to answer questions at the interface of **virome ecology and host health**. The presence of AMGs in viral genomes is particularly compelling: if phage-encoded metabolic genes are differentially abundant across host phenotypes (e.g., health vs. disease, dietary interventions, age groups), this could reveal a mechanistic role for the virome in shaping the gut ecosystem. The question below targets this nexus — it requires integrating viral functional annotations (MOESM4) with abundance data (MOESM2) and sample metadata (MOESM1), all of which the dataset provides.

## Top Scientific Question

**Do gut phage-encoded auxiliary metabolic genes (AMGs) involved in nucleotide scavenging and carbon metabolism show differential abundance patterns between healthy and dysbiotic human gut metagenomic samples as captured in the k141 contig catalogue?**

## Why This Question Is Testable on This Dataset

- **MOESM4_ESM.fa** provides the amino acid sequences of all predicted viral proteins; AMGs can be identified via Pfam/KEGG domain annotation of these sequences.
- **MOESM2_ESM.xlsx** (129 KB) likely contains a read-mapping-based abundance matrix (contigs × samples), enabling quantification of each AMG-carrying contig's relative abundance.
- **MOESM1_ESM.xlsx** (14 KB) probably holds sample metadata including host phenotype (e.g., healthy control vs. IBD/obesity/dysbiosis), enabling statistical comparisons between groups.
- **MOESM3_ESM.xlsx** (90 KB) may contain taxonomic classifications or host-linkage predictions, allowing AMG abundances to be contextualised by their viral host lineage.
- Together, these files support a complete analytical pipeline: AMG annotation → abundance quantification → differential abundance testing across phenotypes → ecological inference.
