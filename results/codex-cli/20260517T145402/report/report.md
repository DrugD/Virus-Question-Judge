# Data summary

The blind subset spans 32 anonymized runs that cover six sequencing contexts. Arthropod RNA-seq dominates (8/32) followed by vertebrate transcriptomes and soil metagenomes (6 each), while gut, plant, and aquatic sources contribute 4 runs apiece. Host or environment labels mirror those source categories with equal counts. Regions skew toward North America (11/32) and South America (6/32), yet four runs lack geographic metadata, indicating partial coverage (mean metadata completeness 0.71). The 53 RdRP-like fragments exhibit motif_strength tiers of 0:1:2 in an 8/25/20 split, so 85% carry at least two canonical motifs. Alignment families are taxonomically broad but fragmented: the top categories include unclassified RdRP (10 fragments), Cystoviridae (7), Nidovirales (6), Partitiviridae (5), and Norzivirales (5), while the rest are thinly represented. Cluster-level annotations redistribute toward Nidovirales, Picornavirales, and unclassified groups (five clusters each).

# Analysis

1. **Low similarity prevalence:** 46 of 53 fragments (86.8%) fall below 40% identity to their nearest curated reference, and 39 of 53 (73.6%) fall below 30%. This, together with ten fragments only assignable to `unclassified_RdRP`, highlights a reference desert.
2. **Novel cluster burden:** 24 of 32 sOTU clusters (75%) meet the `novel` threshold (<0.40 identity). Novel clusters slightly underperform in metadata coverage (mean 0.67) relative to borderline clusters (0.71), implying that the most interesting bins often lack rich contextual metadata.
3. **Source and region concentration:** Novel clusters map most often to arthropod RNA-seq runs (6 clusters) and vertebrate transcriptomes (5), with additional representation from plant and aquatic environments. Geographically, nine novel clusters derive from North America while six originate from runs with unknown region tags, suggesting both regional concentration and data gaps.

# Reasoning

The local subset already shows that most RdRP fragments remain <40% identical to any curated reference and cluster into sOTUs tagged as novel. When extrapolated to the upstream search over ~5.7 million runs and ~131,957 candidate novel sOTUs, even a modest regional or source skew in the subset would imply tens of thousands of polymerase fragments emerging from specific sequencing contexts that current reference taxonomies do not capture. The combined evidence (high motif strength, pervasive unclassified alignments, concentration in certain hosts, and metadata sparsity) suggests that the true virome of those hosts remains unsampled, making it urgent to formulate a question that targets how and where the unknown diversity is accumulating at petabase scale.

# Top scientific question

How does petabase-scale mining of RdRP fragments reveal geographically concentrated yet taxonomically unassigned RNA virus diversity that falls below 40% identity to curated references?

# Why this question is testable

The dataset links each RdRP fragment to its run metadata, alignment-derived percent identity, and sOTU novelty flag. By aggregating across the millions of upstream runs, investigators can stratify low-identity clusters by source ecosystem and region, quantify their taxonomic assignment gaps, and test whether they co-localize with poor metadata contexts. This approach, using only the available features (runinfo, alignment hits, and cluster annotations), directly measures the geographic and ecological concentration of <40% identity RdRP diversity and evaluates how much of that diversity lacks family-level assignments.