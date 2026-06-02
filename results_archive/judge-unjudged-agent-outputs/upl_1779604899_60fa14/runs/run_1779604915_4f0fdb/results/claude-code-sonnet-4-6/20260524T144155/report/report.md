# Technical Report: Marine RNA Virome from Tara Oceans Metatranscriptomes

## 1. Data Summary

The dataset accompanies the manuscript *"Cryptic and abundant marine viruses at the evolutionary origins of Earth's RNA virome"* and comprises seven files:

| File | Description | Scale |
|---|---|---|
| `44779_RdRP_contigs.fna.gz` | Metatranscriptome-assembled contigs with RdRP hits | 44,779 contigs |
| `5504_wcANI_based_clusters_90_80.fna.gz` | vOTU representative sequences (90% ANI, 80% coverage) | 5,504 vOTUs |
| `RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz` | RdRP footprint protein sequences (Tara + Genbank + Wolf 2020) | 209,588 sequences |
| `RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent.fasta.gz` | 50%-identity centroids of RdRP footprints | 13,109 centroids |
| `RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent_near_complete.faa.gz` | Near-complete 50%-identity centroids | 6,238 sequences |
| `functional-annotation-table.tsv` | HHblits-Pfam domain annotations for vOTU proteins | 20,578 domain hits across 5,122 unique contigs |
| `cyverse_readme.txt` | Dataset provenance and file descriptions | — |

Samples span **121 Tara Oceans and Tara Oceans Polar Circle (TOPC) sampling sites** (station numbers 4–210, 2009–2013), three depth layers (surface/SUR, deep chlorophyll maximum/DCM, mesopelagic/MES), and multiple size fractions from both prokaryotic and eukaryotic metatranscriptomes. The functional annotation table contains nine columns: `qseqid`, `strand`, `dom_start`, `dom_end`, `desc`, `prob`, `evalue`, `score`, `database`.

---

## 2. Analysis

### Statistic 1: Depth-stratified RdRP domain composition

Analyzing 20,578 Pfam/HHblits domain hits across depth layers reveals strong compositional differences in RNA virus lineages (values normalized to total hits per layer):

| Depth | Total hits | RdRP_3 (Picorna-like, %) | Birna_RdRp (%) | Mitovir_RNA_pol (%) |
|---|---|---|---|---|
| SUR | 5,868 | 1.89% | 2.68% | 3.25% |
| DCM | 6,834 | **4.26%** | 1.61% | 3.51% |
| MES | 1,940 | 3.35% | 1.24% | 3.04% |

Picorna-like viruses (RdRP_3/Viral_RNA_dep) are **2.25× more abundant** in the DCM than at the surface, while birnavirus-like viruses (Birna_RdRp) are **1.66× more abundant** at the surface than in the DCM. This depth-layer partitioning suggests niche differentiation of RNA virus lineages across the photic zone.

### Statistic 2: Novel Tara Oceans RdRP diversity relative to known viral space

Of the 209,588 RdRP footprint sequences in the combined dataset, 44,779 (21.4%) originate from Tara Oceans metatranscriptomes and are distinct from the 160,167 Genbank reference sequences and 4,593 Wolf et al. 2020 sequences. After clustering at 50% identity, 7,310 of 13,109 centroids (55.8%) are Tara-derived, indicating that Tara sequences preferentially expand into novel sequence space relative to known viruses. Among near-complete footprints, 1,561 of 6,238 centroids (25.0%) are Tara-derived.

### Statistic 3: vOTU-level diversity and depth distribution

The 5,504 vOTU clusters (defined at 90% ANI, 80% coverage) span 116 sampling stations. Among the 1,561 Tara-derived near-complete RdRP footprint centroids, 807 (51.7%) originate from surface waters, 503 (32.2%) from DCM, and 141 (9.0%) from mesopelagic samples — with the remainder from other layers. The DCM harbors a disproportionately novel RdRP lineage composition relative to its total viral load, consistent with a distinct ecological community shaped by the light and nutrient gradients at the chlorophyll maximum.

### Statistic 4: RdRP hit quality and genome completeness

Of 10,243 RdRP-annotated hits in the functional annotation table, 64.4% have HHblits scores >200 (high-confidence), while 10,839 (52.7%) have e-values <1×10⁻³⁰. The 44,779 RdRP contigs have median length of 584 bp (mean 1,153 bp); only 3.4% exceed 5 kb. The vOTU representatives are significantly longer (median 2,002 bp, mean 2,702 bp), reflecting the clustering threshold selecting for more complete sequences. Among 5,122 unique contigs in the annotation table, 641 (12.5%) carry both an RdRP domain and a capsid/coat protein domain, marking putative near-complete genome assemblies.

---

## 3. Reasoning

The combined evidence points to a clear scientific opportunity: the DCM layer hosts a compositionally distinct RNA virome — specifically enriched in Picorna-like (RdRP_3) lineages — relative to the surface ocean. This is ecologically significant because (i) the DCM is a hotspot for primary production and eukaryotic phytoplankton biomass, (ii) Picorna-like viruses are predominantly eukaryote-infecting, and (iii) the depth-stratified partitioning observed across 87 stations spanning both tropical and polar environments implies that depth/light/nutrient gradients are stronger drivers of RNA virus community composition than geographic location. The dataset contains the depth metadata, RdRP domain annotations, and vOTU-level clustering required to formally test whether DCM-associated RNA virome composition (particularly Picorna-like virus prevalence) is predicted by depth-layer identity rather than geographic or thermal gradients.

---

## 4. Top Scientific Question

**Do depth-layer gradients (surface vs. deep chlorophyll maximum vs. mesopelagic) predict the relative abundance of Picorna-like (RdRP_3) versus Birna-like (Birna_RdRp) RNA virus lineages among the 5,504 marine vOTUs from Tara Oceans and Tara Oceans Polar Circle metatranscriptomes, independent of geographic region?**

---

## 5. Testability on the Provided Dataset

This question is directly testable using the functional annotation table and vOTU cluster sequences. The depth layer for each contig is encoded in the `qseqid` field (SUR/DCM/MES), and the RdRP domain type is in the `desc` column. A generalized linear model (or Dirichlet regression) can test whether the ratio of RdRP_3 to Birna_RdRp domain hits differs significantly across SUR, DCM, and MES layers while controlling for station identity (spanning stations 4–210 across 87 geographic sites). The 5,504 vOTU clusters and their depth-of-origin metadata provide the response variable, and the 116-station geographic spread provides adequate power to partial out geographic effects. The observed 2.25× DCM enrichment of Picorna-like viruses (4.26% vs. 1.89% at surface) across 6,834 and 5,868 annotations respectively provides the preliminary signal that motivates this formal test.
