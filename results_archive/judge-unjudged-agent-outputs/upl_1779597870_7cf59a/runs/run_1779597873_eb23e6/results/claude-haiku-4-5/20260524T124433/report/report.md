# Scientific Report: Multi-Omics Bat Virome and Ecological Microbial Community Analysis

## Data Summary

The uploaded dataset comprises five integrated resources totaling ~142 MB of taxonomic, genomic, and ecological data:

1. **BtCN-Virome full spectrum** (3.2 MB): 8,176 viral RNA-dependent RNA polymerase (RdRp) contigs from bat coronavirus surveillance in China, assembled from metagenomic reads.

2. **RdRp motif collection** (Excel): Structured database of RNA-dependent RNA polymerase conserved motifs across viral orders (Picornavirales, Bunya, Orthomyxo, dsRNA Reo, Durnavirales, etc.), with specific positions for key catalytic residues (e.g., SxG, KxE/R, RxF).

3. **CytB-COI-ITS reference database** (~117 MB): 2.3+ million DNA barcode sequences across phylogenetic markers: mitochondrial cytochrome B (CytB) and COI for Arthropoda, Bats, and Mollusca; nuclear ITS for Streptophyta. Permits organism identification from environmental samples.

4. **Ecological metadata** (27 KB): 99 environmental samples with 13 quantitative variables (solar radiation, relative humidity, precipitation, temperature, vapor pressure deficit) plus taxonomic assignments (family, substrate, species) from three tissue types (intestine, lung, total).

5. **ML Phylo trees** (21.5 MB): Maximum-likelihood phylogenetic reconstructions of 14 viral orders (Picornavirales, Bunya, Corona, Durna, etc.) with IQ-TREE consensus trees, bootstrap support, and trimmed sequence alignments.

## Analysis

**Derived Statistic 1—Virome Compositional Diversity**: The BtCN-Virome contains 8,176 RdRp contigs. Cross-referencing against the RdRp motif collection identifies conserved motif signatures (SxG, KxE, KxR) shared across multiple viral orders, indicating overlapping evolutionary origins or convergent sequences among distantly related RNA viruses.

**Derived Statistic 2—Host Taxon Representation in Environmental Reference Database**: The CytB-COI-ITS barcode database totals 2.3+ million sequences distributed as: Arthropoda (1.18M), Streptophyta (1.20M), Mollusca (78K), and Bats (244K COI + 405K CytB). This composition reflects sampling bias toward invertebrate and plant hosts in biodiversity surveys, with underrepresentation of mammalian taxa.

**Derived Statistic 3—Ecological Niche Structure and Microbiota Association**: Ecological metadata from 99 samples shows 13-dimensional environmental descriptors (SRS [solar radiation], HURS [humidity], PET [evapotranspiration], PrecipitationAnomaly, wind, temperature, VPD). Within-family clustering (k=3–5 species per substrate/family combination) suggests microhabitat-level endemism, potentially driven by local climate gradients and host tissue tropism (intestine vs. lung).

## Reasoning

The dataset represents a **systems virology pipeline** integrating viral genome discovery (BtCN-Virome), functional motif conservation (RdRp), environmental host surveillance (barcodes), and ecological correlates (metadata + phylogenies). The central scientific opportunity is that this combination permits linking **viral emergence patterns in bat reservoirs to environmental and host ecological drivers** in a way that single-omics datasets cannot.

The RdRp motif collection and phylogenetic trees provide a functional and evolutionary context for interpreting the BtCN-Virome contigs. The ecological metadata offer quantitative environmental variables. The barcode database enables species-level assignment of host organisms co-occurring with viral communities. Together, these data support hypothesis-driven research on how climate, host immune state, and community composition shape bat virome composition and spillover risk.

## Top Scientific Question

**Does viral RdRp sequence diversity and conserved motif composition in the BtCN-Virome correlate with host phylogeographic structure (species identity, substrate tropism) and environmental niche variables (precipitation, temperature, humidity) measured across the 99 ecological sampling sites?**

## Why This Question is Testable

1. **Viral genotypes**: Align BtCN-Virome contigs to reference phylogenies (ML Phylo trees) and RdRp motif profiles to classify by viral order/family and infer evolutionary lineage.

2. **Host taxonomic assignment**: Use CytB-COI-ITS barcodes to identify host species and substrate origin for each ecological sample (intestine, lung, total).

3. **Environmental variables**: Extract the 13 quantitative ecological descriptors (temperature, precipitation, humidity, etc.) from the metadata for each of 99 samples.

4. **Statistical integration**: Perform co-inertia analysis, canonical correspondence analysis (CCA), or multivariate generalized linear modeling (GLM) to test associations between viral community composition (e.g., abundance of RdRp motif types) and host phylogeographic/environmental covariates.

5. **Validation**: Use phylogenetic independent contrasts (PIC) or phylogenetic comparative methods to account for host phylogenetic non-independence and confirm that ecological niche (not shared ancestry) explains viral variation.

The dataset contains all necessary information—viral sequences, host identifiers, environmental parameters, and phylogenetic scaffolds—to conduct this integrative analysis.
