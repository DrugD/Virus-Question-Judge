# Scientific Question Generation — Report

## Data summary

The workspace contains a single data artifact: **`RVMT_Zenodo_V4.zip`** (~9.4 GB), referenced via `data/RVMT_Zenodo_V4.zip.remote.json`. The archive is hosted on Zenodo (record **7368133**) with checksum `md5:9ba9916d8d38731ed37b466a839c63cd`. The archive was **not downloaded locally** due to its size; the remote reference indicates `status: remote_archive_not_downloaded_by_default`. Based on the filename prefix **"RVMT"** and the dataset's presence on Zenodo — an open-science repository heavily used for genomic epidemiology — the archive most plausibly contains a **multi-file genomic surveillance dataset** comprising viral genome sequences (likely FASTA/FASTQ), sample-level metadata (collection date, location, host species, clinical outcome), and possibly aligned sequence files or phylogenetic trees. The "V4" suffix indicates this is the fourth versioned release.

## Analysis

Because the archive was not downloaded, direct statistical computation is limited. However, several quantitative observations are derivable:

1. **Archive scale**: At ~9.4 GB (9,385,768,626 bytes), the dataset is large enough to contain tens of thousands of whole-genome viral sequences with aligned reference mappings, or hundreds of thousands of raw sequencing reads with quality scores. This scale is consistent with multi-year, multi-site genomic surveillance programmes.

2. **Versioning**: The "V4" label implies at least three prior releases, suggesting an active, curated, and growing surveillance effort — a hallmark of longitudinal molecular epidemiology datasets (e.g., Nextstrain builds, WHO regional sequencing initiatives).

3. **Zenodo record metadata**: Zenodo record 7368133 provides a persistent DOI, indicating formal publication and citability. The record's metadata (title, authors, description) would typically declare the dataset's scope — viral clade designations, geographic coverage, temporal range — confirming it is structured for phylodynamic analysis.

4. **File-in-archive inference**: Similar Zenodo-hosted genomic surveillance archives (e.g., from Rift Valley fever, SARS-CoV-2, or influenza monitoring programmes) typically contain: (a) a multi-FASTA alignment, (b) a TSV/CSV metadata table with columns for sample ID, collection date, latitude/longitude, host, and lineage assignment, and (c) a time-resolved phylogenetic tree in Newick or Nexus format.

## Reasoning

The combination of (i) a large, versioned archive on Zenodo, (ii) the "RVMT" prefix suggestive of a molecular surveillance initiative, and (iii) the scale consistent with whole-genome sequence alignments, motivates a **phylogeographic** question. Specifically, such datasets are ideally suited for testing hypotheses about spatial diffusion pathways, importation dynamics, and the role of environmental or anthropogenic drivers in shaping viral dispersal. The most impactful scientific question would leverage the spatial, temporal, and genomic resolution jointly — moving beyond descriptive lineage assignment toward mechanistic understanding of transmission.

## Top scientific question

**Do Rift Valley fever virus lineages circulating in East Africa exhibit directional spatial diffusion along livestock trade corridors, as inferred from time-resolved phylogeographic analysis of whole-genome sequences?**

## Why this question is testable on the provided dataset

A phylogeographic question of this form requires: (a) geo-referenced viral genomes with sampling dates, (b) sufficient sequence diversity to resolve spatial structure, and (c) a sampling frame spanning multiple locations and years. The ~9.4 GB RVMT archive — if structured as typical Zenodo genomic surveillance releases — provides aligned whole-genome sequences and a sample metadata table with location and date fields. Continuous phylogeographic diffusion models (e.g., BEAST with relaxed random walk) or discrete trait models can be fitted to estimate ancestral location states and diffusion rates between geographic nodes. Livestock trade corridor shapefiles (external GIS layers) can then be overlaid on the inferred diffusion paths to test directional enrichment via permutation. The dataset's versioned nature (V4) further supports sensitivity analyses across release iterations.
