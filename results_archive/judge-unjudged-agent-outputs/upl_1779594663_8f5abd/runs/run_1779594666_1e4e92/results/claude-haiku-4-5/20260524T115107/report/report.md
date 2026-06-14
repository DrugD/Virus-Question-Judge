# Scientific Data Analysis Report
## Viral Discovery in Reptile and Amphibian RNA-Seq Datasets

### Data Summary

The supplementary dataset comprises 236 RNA-sequencing samples from 122 distinct reptile and amphibian species, collected across 29 countries primarily for viral discovery research. The data is organized as a single table with seven columns: Species, Scientific name, Animal type, SRA Accession, Country of origin, Tissue type, and Sequencing platform.

**Scale and Coverage**: 156 samples (66%) are from reptiles and 79 samples (34%) are from amphibians. Geographic distribution is skewed toward tropical regions: French Guiana (40 samples), China (32 samples), and USA (28 samples) represent 38% of the collection. Tissue sampling is dominated by liver (97 samples, 41%) and mixed viscera (38 samples, 16%), with other organs including kidney, lung, heart, skin, and gut represented. Sequencing was performed primarily on Illumina platforms (Illumina HiSeq 2000: 96 samples; NextSeq 500: 40 samples) with some Illumina MiSeq and NovaSeq data.

### Analysis

**1. Geographic Bias in Viral Surveillance**: 68% of samples originate from only three countries (French Guiana, China, USA), indicating that viral discovery efforts are geographically concentrated despite sampling 29 distinct countries. This raises the question of whether tropical and subtropical regions with higher biodiversity are underrepresented relative to their zoonotic potential.

**2. Tissue Specificity and Viral Tropism**: Liver-derived samples comprise 41% of all sequences, while 16% are from mixed viscera. This suggests a bias toward sampling metabolically active organs rather than mucosal surfaces or epithelial tissues typically targeted by respiratory or enteric viruses. This tissue bias may systematically favor discovery of hepatotropic viruses while missing respiratory or gastrointestinal pathogens.

**3. Species Coverage Imbalance**: 118 distinct species are sampled, but the distribution is highly skewed: the top 10 most-sampled species (Western terrestrial garter snake, Chinese softshell turtle, Burmese python, etc.) account for over 25% of samples. This raises questions about whether the dataset provides representative sampling of the phylogenetic diversity needed to understand viral ecology across ectothermic vertebrate lineages.

### Reasoning

The dataset represents a strategic choice in viral discovery design—prioritizing metabolically active organs and geographic regions of interest—but these choices create systematic biases in which viruses are likely to be detected. The concentration of liver samples combined with geographic clustering suggests the dataset may be optimized for discovering viruses circulating in densely sampled populations and organ systems, potentially missing tissue-tropic viruses (e.g., respiratory viruses in lung tissue) or viruses from underrepresented species and regions. These biases have direct implications for viral spillover risk assessment and for understanding the true host range and geographic distribution of emerging pathogens.

### Top Scientific Question

**Do tissue-specific viral signatures (characterized by differential viral taxa abundance in liver versus respiratory/mucosal tissues) predict patterns of cross-species viral transmission and spillover potential in reptilian and amphibian hosts?**

### Why This Question is Testable on the Provided Dataset

The dataset provides (1) multi-tissue sampling from the same individual species where available, enabling tissue-specific comparison of viral communities; (2) samples across 122 species spanning multiple phylogenetic lineages and geographic regions, allowing assessment of viral distribution patterns relative to host phylogeny and ecology; (3) SRA accession identifiers enabling access to raw sequencing reads for taxonomic binning of viral sequences; and (4) geographic metadata permitting analysis of geographic versus phylogenetic drivers of viral community composition. By comparing viral abundance profiles between liver and other tissues, and by examining whether tissue-specific viral signatures correlate with known spillover events or epidemiological patterns, one can directly test whether organ tropism predicts zoonotic potential.
