# Technical Report: Petabase-Scale RdRP Discovery Analysis

## 1. Data Summary

The blind input dataset represents a systematic translated-search analysis of public sequencing archives at unprecedented scale. The upstream search processed **5,686,715 sequencing runs** spanning **10.2 petabases** of sequence data, identifying **131,957 candidate novel RdRP-containing sOTUs** (species-level operational taxonomic units).

The local subset provided for analysis includes:
- **32 sequencing runs** from diverse biological sources: arthropod RNA-seq (8 runs), vertebrate transcriptomes (6), soil metagenomes (6), gut metagenomes (4), plant transcriptomes (4), and aquatic metaviromes (4)
- **53 RdRP-like amino acid fragments** with varying confidence levels based on conserved catalytic motif detection
- **32 candidate sOTU clusters** representing distinct viral lineages
- Geographic distribution spanning all major continents (NA, EU, AS, OC, SA, AF) plus samples with unknown provenance
- Metadata completeness ranging from 0.42 to 0.98, with mean ~0.71

Among the 53 fragments, motif strength distribution indicates: 21 high-confidence candidates (motif_strength=2, all three RdRP catalytic motifs A+B+C detectable), 23 medium-confidence (motif_strength=1, motifs A+C visible), and 9 weak/partial hits (motif_strength=0).

## 2. Analysis

Three key derived statistics reveal the extent of novel RNA-virus diversity:

**Statistic 1: Reference Database Gap**
Of the 53 RdRP fragments, **46 fragments (86.8%)** exhibit percent_identity_to_nearest_reference below 0.40 (40% amino acid identity threshold). This pervasive low similarity indicates that the vast majority of detected RdRP-like sequences are highly divergent from all curated viral polymerase references, suggesting they represent deeply novel or previously unsampled viral lineages.

**Statistic 2: Novel Cluster Prevalence**
At the cluster level, **25 of 32 sOTUs (78.1%)** are flagged as "novel" based on the <0.40 identity threshold. Only 7 clusters (21.9%) fall into the "known_or_borderline" category, indicating that reference databases provide confident matches for fewer than one-quarter of the discovered viral diversity.

**Statistic 3: Unclassified RdRP Abundance**
Among alignment hits, **9 fragments (17.0%)** could not be assigned to any recognized viral family and are annotated as "unclassified_RdRP." When combined with the low-identity matches to known families, this reveals that current reference databases fail to provide adequate phylogenetic context for a substantial fraction of environmental RdRP diversity. Additionally, novel clusters appear distributed across all sampled source types (arthropods, vertebrates, soil, gut, plants, aquatic environments), indicating that this reference gap is not restricted to a single ecological niche.

## 3. Reasoning

When extrapolated to the full upstream search scale (5.7 million runs, 10.2 petabases, 131,957 candidate novel sOTUs), these statistics point to a profound scientific opportunity. The 78% novelty rate and 87% low-identity rate observed in the local subset, if representative of the full dataset, suggest that **over 100,000 candidate novel viral lineages** have been computationally detected through RdRP-targeted translated search.

This finding implies that:
1. **Curated viral reference databases severely undersample global RNA-virus diversity.** The <40% identity threshold is far below typical species- or genus-level boundaries, indicating that many detected candidates likely represent novel families or orders.
2. **Petabase-scale public sequencing archives contain a massive hidden virome.** Unlike curated databases built from targeted viral isolation studies, public archives aggregate incidental viral sequences from ecological, clinical, agricultural, and environmental sequencing projects worldwide.
3. **RdRP provides a universal marker for systematic RNA-virus discovery.** The conserved polymerase domain enables detection across highly divergent viral lineages that share no sequence similarity outside the RdRP region.
4. **The scale of discovery (>130,000 sOTUs) represents a potential order-of-magnitude expansion** of known RNA-virus diversity, comparable to or exceeding the cumulative viral sequences in existing reference collections.

These observations collectively motivate a fundamental question about whether systematic computational mining of public sequencing data can reveal RNA-virus diversity that traditional viral discovery approaches have missed.

## 4. Top Scientific Question

**Can systematic petabase-scale RdRP-targeted mining of public sequencing archives reveal extensive hidden RNA-virus diversity that is absent from curated viral reference databases?**

## 5. Why This Question Is Testable on the Provided Dataset

This question is directly testable using the blind input data:

- **RdRP-targeted mining approach**: Demonstrated by the amino acid fragment data (rdrp_aa_fragments.faa), alignment hits to viral polymerase references (alignment_hits.tsv), and motif strength annotations indicating detection of conserved RdRP catalytic domains.

- **Public sequencing archives at scale**: The data scale is explicitly provided (5.7M runs, 10.2 petabases) with sample metadata (runinfo_subset.tsv) demonstrating diversity of sources and geographic origins.

- **Hidden diversity quantification**: The candidate sOTU clusters (candidate_sotu_clusters.tsv) with novelty flags allow direct measurement of how many viral lineages fall below reference-database similarity thresholds.

- **Reference database comparison**: The percent_identity_to_nearest_reference and nearest_reference_family fields in both alignment_hits.tsv and candidate_sotu_clusters.tsv enable systematic comparison against curated viral references, quantifying the fraction of diversity absent from existing databases.

The combination of large-scale search coverage, RdRP-based detection, low reference similarity, and high novelty rates provides convergent evidence to answer the question affirmatively, while the source metadata and cluster statistics enable characterization of where and how this hidden diversity is distributed across ecosystems.
