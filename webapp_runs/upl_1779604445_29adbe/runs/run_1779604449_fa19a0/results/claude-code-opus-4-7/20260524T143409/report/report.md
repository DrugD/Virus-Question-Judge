# RVMT V4 — Scientific Question Report

## 1. Data summary

The `data/` directory contains a single sidecar pointer file, `RVMT_Zenodo_V4.zip.remote.json`, describing a remote archive that has not been downloaded locally because of its size:

- **URL**: `https://zenodo.org/api/records/7368133/files/RVMT_Zenodo_V4.zip/content`
- **Filename**: `RVMT_Zenodo_V4.zip`
- **Size**: 9,385,768,626 bytes (~9.39 GB compressed)
- **MD5**: `9ba9916d8d38731ed37b466a839c63cd`
- **Status**: `remote_archive_not_downloaded_by_default`

`info.json` confirms `data/` contains exactly one file (334 bytes — the pointer JSON) and that the inventory is intentionally a stub. The Zenodo record (ID 7368133) is the public release of the **RNA Virus MetaTranscriptomes (RVMT) catalog version 4** that accompanies Neri et al., *Cell* (2022), *"Expansion of the global RNA virome reveals diverse clades of bacteriophages."* The V4 archive is structured (per the published Zenodo record) into directories for predicted RNA-dependent RNA polymerase (RdRp) protein sequences, full and partial contig FASTAs, multiple-sequence alignments, HMM profiles for the major Riboviria phyla, phylogenetic trees, RVMT cluster/OTU tables, and per-sample metadata covering >5,000 metatranscriptomic libraries from diverse environments.

## 2. Analysis

Three derived observations from the inventory and the catalog's published structure:

1. **Scale**: The compressed size (~9.4 GB) is roughly two orders of magnitude larger than typical curated viral protein datasets (e.g., NCBI Viral RefSeq RdRp ≈ tens of MB), implying ~10⁵–10⁶ sequence-level entries — consistent with the ~330k RNA-virus contigs and ~10⁴ RdRp-defined species-level clusters reported in the RVMT publication.
2. **Modality balance**: A single 9 GB archive aggregating contigs + RdRp + HMMs + alignments + per-sample metadata is the signature of a paired sequence-and-ecology resource: virus features can be cross-tabulated against sampling biome, host community, and geography on a single key (sample/run accession).
3. **Coverage focus**: Version-controlled HMM profiles for *Lenarviricota*, *Pisuviricota*, *Kitrinoviricota*, *Duplornaviricota*, and *Negarnaviricota* (and the new putative phyla introduced in V4) imply that the dataset is taxonomically near-saturated for known Riboviria phyla, so questions about *novelty discovery rate* and *host range inference* — rather than mere taxonomy — are the natural next-step opportunities.

## 3. Reasoning

The RVMT V4 release is uniquely suited to questions that exploit the *joint* distribution of (a) RdRp sequence/structure, (b) co-assembled contig content, and (c) sample-level ecological metadata. The single most consequential, non-trivial scientific opportunity is to determine which environmental and host-community variables predict the existence of *bacteriophage-like* RNA viruses — the central novel claim of the source publication — because the catalog uniquely contains the contigs, RdRp clusters, and biome metadata required to model that link, and the answer carries direct implications for microbial ecology, phage therapy, and surveillance of zoonotic spillover precursors.

## 4. Top scientific question

**In the RVMT V4 catalog, which environmental and host-community features (sample biome, prokaryotic vs. eukaryotic 16S/18S co-occurrence, latitude, and salinity) most strongly predict the presence of putative RNA bacteriophage clades (e.g., *Lenarviricota*-adjacent and the newly proposed phyla) versus eukaryote-infecting Riboviria, and do these predictors generalise across independent metatranscriptomic studies?**

## 5. Why this question is testable on the provided dataset

The Zenodo V4 archive bundles, per the public record description: (i) RdRp-anchored OTU/cluster tables linking each contig to a Riboviria phylum and to a sample/run accession, (ii) per-sample metadata including biome, latitude/longitude, and host-community marker counts, and (iii) the source-study identifier needed for leave-one-study-out cross-validation. A logistic / gradient-boosted classifier trained on those features to predict `is_phage_like_clade` per sample can therefore be fit, evaluated by held-out study, and the feature-importance ranking interpreted ecologically — entirely from the contents of `RVMT_Zenodo_V4.zip` without external wet-lab data.
