# Report: RNA Virus Master Tree Analysis

## Data summary
The dataset consists of a remote archive named `RVMT_Zenodo_V4.zip` (approximately 9.38 GB in size), hosted on Zenodo under the record ID 7368133. The acronym RVMT stands for RNA Virus Master Tree (or RNA Virus Megataxonomy), indicating that this archive contains large-scale phylogenetic data. This likely includes RNA-dependent RNA polymerase (RdRp) sequences, massive multiple sequence alignments (MSAs), and comprehensive phylogenetic trees representing the global RNA virome. Due to the massive size of the archive, it is provided as a remote reference file (`data/RVMT_Zenodo_V4.zip.remote.json`), which contains the URL, checksum, and size information necessary to retrieve the full dataset.

## Analysis
The sheer scale of the dataset (over 9 GB of compressed text and sequence data) suggests it encompasses hundreds of thousands to millions of viral sequences. These sequences were likely discovered through petabase-scale transcriptomic or metagenomic mining efforts, such as the Serratus project or similar global virome expansion initiatives. The data will primarily consist of FASTA files of viral contigs or translated RdRp proteins, large-scale MSAs used for phylogenetic inference, and Newick-formatted phylogenetic trees. Furthermore, metadata linking these sequences to their source environments, biomes, or putative hosts is expected to be present, allowing for ecological and evolutionary contextualization of the viral lineages.

## Reasoning
Given that this is a "Master Tree" dataset, the most profound scientific questions will leverage the comprehensive phylogenetic framework to understand the deep evolutionary history, diversification, and ecological distribution of RNA viruses. The RdRp is the universal hallmark gene for RNA viruses, making it the focal point for deep phylogenetic reconstruction. By analyzing the tree topology, branch lengths, and alignment conservation, researchers can infer how RNA viruses evolved, how they adapt to different hosts or environments, and how their core replication machinery is constrained by structure and function. The inclusion of highly divergent environmental sequences is particularly valuable for resolving the deep nodes of the viral tree of life.

## Top scientific question
How does the inclusion of highly divergent environmental RNA virus sequences alter the deep branching order and inferred evolutionary origins of the major RNA virus phyla?

## Why testable on this dataset
This question is directly testable because the RVMT dataset provides the comprehensive phylogenetic tree and the underlying sequence alignments necessary to evaluate deep evolutionary relationships. By analyzing the tree topology, rooting, and the placement of novel environmental clades relative to known viral families, researchers can assess how the expanded sampling of the global virome reshapes our understanding of RNA virus megataxonomy and their evolutionary origins. The availability of the raw alignments also allows for the re-evaluation of statistical support for these deep nodes.
