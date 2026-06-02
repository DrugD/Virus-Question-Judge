# Data summary

The agent-visible upload under `data/` contains one metadata file, `RVMT_Zenodo_V4.zip.remote.json`. It describes a remote Zenodo archive named `RVMT_Zenodo_V4.zip`, available through `https://zenodo.org/api/records/7368133/files/RVMT_Zenodo_V4.zip/content`, with size 9,385,768,626 bytes and MD5 checksum `9ba9916d8d38731ed37b466a839c63cd`. The file is marked `remote_archive_not_downloaded_by_default` because it is a large archive. Querying the referenced Zenodo record identified the dataset as "Expansion of the global RNA virome reveals diverse clades of bacteriophages", the RNA Virus in MetaTranscriptomes project. The record description reports mining 5,150 diverse metatranscriptomes, recovering more than 2.5 million RNA virus contigs, and analyzing more than 330,000 RNA-dependent RNA polymerases (RdRPs).

# Analysis

The remote archive is 9.386 GB in decimal units, or about 8.741 GiB, so the visible upload is a pointer to a substantial sequence-analysis product rather than a small table. Relative to the 5,150 metatranscriptomes described in the record, the dataset contains at least about 485 RNA virus contigs per metatranscriptome and at least about 64 RdRP sequences per metatranscriptome. The contig-to-RdRP scale is about 7.6:1, consistent with a broad viral contig catalog anchored by a large polymerase phylogenetic marker set. The description states that RdRP analysis corresponds to a five-fold increase in known RNA virus diversity, meaning the expanded catalog is roughly five times the prior known diversity baseline. It also states that the expanded phylum `Lenarviricota` accounts for about one third of the RNA virome, and that CRISPR spacer matches plus bacteriolytic proteins provide host-linkage evidence for prokaryotic infection by subsets of picobirnaviruses and partitiviruses.

# Reasoning

The strongest scientific opportunity is to test whether the dataset changes the inferred host range of major RNA virus groups, not merely whether it adds more sequences. The record explicitly combines three types of evidence: a very large contig catalog, an RdRP phylogeny, and host-association signals such as CRISPR spacer matches and bacteriolytic proteins. That combination can address a central virology question: whether lineages historically treated as eukaryotic RNA viruses include prokaryote-infecting bacteriophage clades.

# Top scientific question

Do CRISPR spacer matches and bacteriolytic protein domains across the RVMT RNA virus contigs show that major picobirnavirus and partitivirus lineages are prokaryote-infecting RNA bacteriophages rather than exclusively eukaryotic viruses?

# Why this question is testable on the provided dataset

The question is testable because the Zenodo record describes the necessary feature classes: millions of RNA virus contigs, hundreds of thousands of RdRPs for clade placement, gene-content annotations, CRISPR spacer matches, and bacteriolytic proteins. An analysis can map contigs or RdRP-defined lineages to picobirnavirus and partitivirus clades, quantify CRISPR spacer matches to prokaryotic hosts, test enrichment of bacteriolytic proteins in those clades, and compare the strength of prokaryotic-host evidence against lineages lacking those markers.
