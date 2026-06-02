# Technical Report: Viral Discovery in Amphibian and Reptile Transcriptomes

## 1. Data Summary

The dataset consists of a single Microsoft Word document (43705_2022_180_MOESM1_ESM.docx, 2.25 MB) containing supplementary materials for a viral discovery study. The document includes:

- **Supplementary Table 1**: A comprehensive inventory of 234 unique RNA-Sequencing datasets from publicly available SRA repositories (SRR, ERR, DRR accessions)
- **Supplementary Figures 1-5**: Phylogenetic trees and genomic alignments showing novel viral discoveries including reptile Bunyavirales, reptile lyssaviruses, amphibian and reptile Hepeviridae and Astroviridae, newt influenza virus, and newt calicivirus

The table documents RNA-seq datasets from 237 tissue samples spanning amphibians (79 samples, 33%) and reptiles (158 samples, 67%) across diverse species, tissues, geographic origins, and sequencing platforms. Key fields include: species name, scientific name, animal type, SRA accession, country of origin, tissue type, and sequencing platform.

## 2. Analysis

**Taxonomic and Geographic Distribution**: The dataset encompasses an estimated 100+ distinct amphibian and reptile species sampled from 20+ countries across six continents. The highest representation comes from French Guiana (40 samples, 17%), China (32 samples, 14%), and USA (28 samples, 12%), with additional samples from Cuba, Australia, India, Madagascar, and Europe. This global sampling strategy enables detection of geographically-restricted viral lineages and assessment of viral host range across phylogenetically diverse herpetofauna.

**Tissue Type Bias and Viral Detection**: Among the 237 samples, liver tissue dominates with 97 samples (41%), followed by mixed viscera (38 samples, 16%) and kidney (20 samples, 8%). Specialized tissues include skin derivatives (nuptial pad, femoral gland, mental gland), blood, heart, lung, and reproductive organs. The predominance of metabolically active organs (liver, kidney) and mixed viscera likely reflects optimization for viral RNA detection, as these tissues accumulate viral loads during systemic infections. This tissue bias suggests the study specifically targeted detection of blood-borne and systemically-distributed viruses rather than tissue-specific or epithelial viruses.

**Technological Heterogeneity and Data Quality Variance**: Sequencing was performed on multiple Illumina platforms (HiSeq 2000, 2500, 4000; NextSeq 500; Genome Analyzer II) and 454 pyrosequencing (GS FLX, GS Junior). Platform-specific biases in read length (454: longer reads, 400-700bp; Illumina: shorter reads, 100-150bp), error profiles (454: homopolymer errors; Illumina: substitution errors), and sequencing depth create systematic variance in viral detection sensitivity. Older platforms (454, Genome Analyzer II) covering 16 samples likely have lower sensitivity for rare viral transcripts compared to modern HiSeq platforms, potentially introducing geographic and taxonomic biases in viral discovery rates if certain regions or species were preferentially sequenced on older technologies.

## 3. Reasoning

These observations reveal a critical gap in comparative virology: the dataset's heterogeneous tissue sampling, technological variance, and geographic distribution create systematic biases that may confound interpretation of viral host range, tissue tropism, and biogeographic patterns. The five identified novel viral lineages (Bunyavirales, lyssaviruses, Hepeviridae, Astroviridae, influenza-like, calicivirus) span multiple families with distinct transmission modes, host ranges, and zoonotic potential.

The most scientifically important question this dataset can answer is whether the observed tissue tropism patterns of newly discovered amphibian and reptile viruses reflect true biological host-virus specificity or are artifacts of sampling biases. Specifically, the 2.4-fold higher prevalence of liver samples versus other tissues may artificially inflate detection of hepatotropic viruses while missing neurotropic, respiratory, or skin-associated viruses. Understanding whether novel reptile lyssaviruses (typically neurotropic in mammals) are genuinely detected in liver due to systemic infection or whether they would be more abundant in brain/nervous tissue has profound implications for assessing zoonotic risk and cross-species transmission potential.

## 4. Top Scientific Question

Do the tissue-specific detection patterns of novel amphibian and reptile viruses identified in this multi-tissue RNA-seq dataset reflect genuine viral tropism or are they confounded by the 41% overrepresentation of liver samples compared to other organ systems?

## 5. Why This Question is Testable on the Provided Dataset

This question is directly testable using the provided dataset through several quantitative approaches:

1. **Tissue-stratified viral prevalence analysis**: Calculate detection rates for each viral family (Bunyavirales, lyssavirus, Hepeviridae, Astroviridae, influenza, calicivirus) across tissue types (liver n=97, mixed viscera n=38, kidney n=20, others n=82). Chi-square tests can determine if viral detection is independent of tissue type or shows significant tissue-specific enrichment.

2. **Sampling bias correction**: For each viral family, compare observed tissue distribution to null expectations based on tissue sampling frequencies. For example, if reptile lyssaviruses are detected in 15/97 liver samples (15.5%) but 0/20 kidney samples, binomial tests can assess whether this reflects true hepatotropism or insufficient kidney sampling power.

3. **Phylogenetic signal correlation**: The five supplementary figures provide phylogenetic trees showing evolutionary relationships of novel viruses to known viruses with characterized tissue tropisms. By mapping known tropism data from reference viruses onto these phylogenies, we can test whether phylogenetically-related viruses share tissue detection patterns, suggesting conserved tropism versus sampling artifacts.

4. **Multi-tissue species analysis**: Identify species sampled across multiple tissue types (e.g., Cayenne caecilian with kidney, heart, lung, liver samples) and test whether the same viral sequences are detected across tissues within individuals, indicating systemic infection, or are tissue-restricted.

The analysis requires only the data already present: tissue type labels, viral detection results (implicit in the phylogenetic figures showing which samples yielded viral sequences), and phylogenetic relationships. No wet-lab experiments are needed.
