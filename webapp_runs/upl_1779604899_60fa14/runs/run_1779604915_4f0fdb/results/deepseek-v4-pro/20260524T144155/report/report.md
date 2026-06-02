# Scientific Question Generation Report

## Data Summary

The dataset originates from the Tara Oceans (2009–2013) metatranscriptomic survey of marine RNA viruses, accompanying the study "Cryptic and abundant marine viruses at the evolutionary origins of Earth's RNA virome." The workspace contains seven files:

- **`functional-annotation-table.tsv`** (1.94 MB, TSV): The primary analyzable file, containing domain-level functional annotations of proteins from viral operational taxonomic units (vOTUs). Columns: `qseqid`, `strand`, `dom_start`, `dom_end`, `desc`, `prob`, `evalue`, `score`, `database`. Three annotation databases are used: `hhblits-pfam`, `diamond`, and `hhblits-Wolf-et-al-2018`. Query IDs encode sampling station, depth layer (SRF=surface, DCM=deep chlorophyll maximum, MES=mesopelagic), size fraction (0.22–3 µm), and k-mer assembly parameters.
- **`44779_RdRP_contigs.fna.gz`** (16.6 MB): 44,779 nucleotide contigs harboring RNA-dependent RNA polymerase (RdRP) domains.
- **`5504_wcANI_based_clusters_90_80.fna.gz`** (4.8 MB): 5,504 vOTU representative sequences clustered at ≥90% ANI over ≥80% alignment length.
- **`RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz`** (16.7 MB): RdRP footprint protein sequences from Tara Oceans, GenBank, and Wolf et al. (2020).
- **`RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent.fasta.gz`** (3.0 MB): 50%-identity cluster centroids.
- **`RdRp_footprints_Tara_Genbank_Wolf2020_centroids_50_percent_near_complete.faa.gz`** (2.0 MB): Near-complete centroid sequences.
- **`cyverse_readme.txt`** (12 KB): Dataset documentation confirming seven original subdirectories and the manuscript context.

## Analysis

Three key quantitative observations were derived from the functional annotation table:

1. **Annotation landscape**: The `desc` field reveals at least 20 distinct domain families including RdRP_1 (picorna-like), RdRP_2, RdRP_3 (nodavirus-like), RdRP_4, Birna_RdRp, Mitovir_RNA_pol, Bunya_RdRp, Flavi_NS5, RNA_replicase_B, and numerous auxiliary domains (Peptidase_C3G, Viral_helicase1, Methyltrans_Mon, capsid proteins). Domain annotations span all three databases with variable confidence (prob from ~90% to 100%; evalue from near-zero up to 0.005).

2. **Depth-stratified sampling**: Query IDs systematically encode three depth layers — SRF (surface), DCM (deep chlorophyll maximum), and MES (mesopelagic). For example, entries like `TARA_093_DCM_0.22-3_k119_*` vs. `TARA_093_SRF_0.22-3_k119_*` allow direct comparison of RdRP diversity across depth zones from the same station.

3. **Multi-domain architecture**: Many contigs carry multiple annotated domains in a defined order (e.g., Vmethyltransf → Viral_helicase1 → RdRP_2 → Peptidase_C36 → capsid), reflecting complete or near-complete viral genome segments. Domain boundaries (`dom_start`, `dom_end`) enable mapping of genome organization. High-confidence annotations (prob ≥ 99%, evalue < 1e-20) are abundant, supporting robust statistical comparisons.

## Reasoning

The depth-encoding in query IDs combined with rich domain-level annotations creates a rare opportunity to study how RNA virus polymerase diversity stratifies across the ocean water column. The three depth layers (SRF, DCM, MES) represent distinct ecological niches differing in light, nutrients, and host communities. Comparing the relative abundance and phylogenetic breadth of RdRP types across these layers can reveal whether deep-ocean RNA viromes harbor distinct evolutionary lineages versus surface waters — a question at the frontier of marine viral ecology. The presence of three annotation databases provides complementary classification schemes that can be cross-validated.

## Top Scientific Question

Do RNA-dependent RNA polymerase (RdRP) domain types encoded by marine RNA viruses exhibit statistically significant stratification in their relative abundance and phylogenetic diversity across surface (SRF), deep chlorophyll maximum (DCM), and mesopelagic (MES) depth layers in the Tara Oceans metatranscriptomes?

## Why This Question Is Testable on the Provided Dataset

The `functional-annotation-table.tsv` directly provides depth-annotated query IDs and RdRP domain classifications with statistical confidence scores. By parsing the depth label (SRF/DCM/MES) from each `qseqid` and cross-referencing with the `desc` field (which names the specific RdRP family), one can construct depth × RdRP-type contingency tables. The `prob` and `score` columns allow filtering for high-confidence annotations. Chi-square or Fisher's exact tests can assess non-random distribution of RdRP types across depth layers. Shannon diversity indices computed per depth layer can quantify phylogenetic breadth. The large sample size (tens of thousands of annotated domains) ensures statistical power, while the Tara Oceans spatial coverage (121 sampling sites) provides replication across ocean provinces.
