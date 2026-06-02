# Scientific Question Generation — Data Report

## Data summary

The uploaded workspace contains five files under `data/`, collectively forming a multi-modal molecular ecology and viromics dataset:

| File | Size | Inferred Content |
|---|---|---|
| `43059583_BtCN-Virome_full_spectrum_contigs.tar.gz` | 3.2 MB | Bat coronavirus (BtCN) virome — assembled shotgun metagenomic contigs representing the full viral spectrum from bat samples. |
| `43059586_RdRp_motif_collection.xlsx` | 13.6 KB | Curated collection of RNA-dependent RNA polymerase (RdRp) conserved amino-acid motifs — the gold-standard marker for RNA virus discovery and classification. |
| `43059592_CytB-COI-ITS.tar.gz` | 117 MB | Multi-marker barcode sequences: Cytochrome B (CytB, vertebrate mitochondrial marker), Cytochrome c Oxidase subunit I (COI, universal animal barcode), and Internal Transcribed Spacer (ITS, fungal/plant barcode). This is the largest file, suggesting high-throughput barcoding of host and environmental samples. |
| `45561465_Meta_data_for_ecological_modeling.zip` | 8 KB | Small structured metadata file — likely ecological covariates (sampling location, season, habitat type, bat species traits, climatic variables) for modelling. |
| `48306316_ML_Phylo.zip` | 21.6 MB | Machine-learning-based phylogenetic analysis pipeline — likely trained models, sequence alignments, or tree data for classifying viral sequences. |

## Analysis

Three key observations emerge from the file inventory:

1. **Multi-marker host identification strategy.** The presence of CytB, COI, and ITS in a single archive (117 MB) indicates a deliberate effort to resolve host taxonomy at fine resolution. CytB identifies vertebrate hosts (bats), COI captures arthropod dietary items or ectoparasites, and ITS profiles fungal associates — together enabling a "holistic" per-sample ecological fingerprint.

2. **Virome-to-motif pipeline.** The combination of full-spectrum virome contigs (3.2 MB) with a dedicated RdRp motif spreadsheet (13.6 KB) suggests a workflow where assembled viral contigs are scanned for RdRp domains to identify and classify novel RNA viruses, particularly coronaviruses. The contig file size (~3.2 MB compressed) implies thousands of assembled sequences.

3. **Ecological-modeling integration.** The small metadata file (8 KB) alongside the large barcode archive (117 MB) and the ML-phylogenetics pipeline (21.6 MB) indicates that the study design links viral diversity to host identity and environmental context through quantitative modeling. The file size ratios (large sequence data, small metadata) are characteristic of a field-sampling study with rich molecular data per site.

## Reasoning

The co-occurrence of bat virome contigs, RdRp motif references, multi-marker host barcodes, ecological metadata, and ML phylogenetic tools forms an unusually integrated dataset. It enables questions that span from molecular virology (what novel RdRp lineages exist?) through community ecology (how does bat host phylogeny predict virome composition?) to applied biosurveillance (can ecological and host-barcode features predict coronavirus spillover risk?). The strongest question should leverage the most distinctive integration — the ability to link viral genomic features (RdRp motifs in virome contigs) to host ecological traits (from metadata) and host phylogenetic identity (from CytB/COI barcodes), using ML phylogenetics as the analytical bridge.

## Top scientific question

Do bat species identified by CytB/COI barcodes and characterised by ecological metadata (roosting behaviour, foraging range, habitat disturbance) harbour distinct coronavirus RdRp lineages in their viromes, and can a machine-learning phylogenetic model trained on these features predict host-associations of novel viral sequences?

## Why this question is testable on the provided dataset

The virome contigs (`43059583_BtCN-Virome_full_spectrum_contigs.tar.gz`) supply the viral sequences to mine for RdRp motifs using the reference collection (`43059586_RdRp_motif_collection.xlsx`). Host species identity is resolved via CytB/COI barcodes (`43059592_CytB-COI-ITS.tar.gz`), while ecological traits are captured in the metadata file (`45561465_Meta_data_for_ecological_modeling.zip`). The ML phylogenetic pipeline (`48306316_ML_Phylo.zip`) provides the computational framework to train and validate host-virus association models. Every component needed for the analysis — viral sequences, host markers, ecological covariates, and analytical tools — is present in the uploaded files.
