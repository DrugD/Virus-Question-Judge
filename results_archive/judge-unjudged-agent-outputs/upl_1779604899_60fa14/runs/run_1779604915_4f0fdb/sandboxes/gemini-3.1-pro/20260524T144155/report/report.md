# Report on Marine RNA Virome Dataset

## Data summary
The provided dataset originates from the Tara Oceans and Tara Oceans Polar Circle expeditions, focusing on the discovery and characterization of marine RNA viruses. The workspace contains several key files:
- `cyverse_readme.txt`: A detailed description of the dataset, explaining the contents of various subdirectories (Assemblies, Contigs, Corrected Long Reads, Functional Annotations, Predicted 3D Structures, RdRP HMMs, and RdRP footprints).
- `functional-annotation-table.tsv`: A comprehensive table detailing the functional annotations of protein sequences encoded by viral operational taxonomic units (vOTUs). It includes contig IDs, strand information, domain start/end positions, Pfam descriptions (e.g., RdRP_1, Viral_helicase1, Calici_coat), probabilities, and E-values.
- `44779_RdRP_contigs.fna.gz`: A FASTA file containing 44,779 contigs assembled from metatranscriptome reads that encode RNA-dependent RNA polymerases (RdRPs).
- `5504_wcANI_based_clusters_90_80.fna.gz`: A FASTA file of 5,504 representative sequences clustered based on average nucleotide identity (ANI).
- `RdRp_footprints_Tara_Genbank_Wolf2020.faa.gz` and related centroid files: Protein sequences of RdRP footprints from this study, GenBank, and previous literature, used for phylogenetic analysis.

## Analysis
An initial analysis of the `functional-annotation-table.tsv` reveals that the contig identifiers encode valuable metadata, specifically the sampling depth (e.g., `SUR` for surface waters and `DCM` for the deep chlorophyll maximum). The table also shows that many contigs encode multiple functional domains, such as various RdRP families, helicases, methyltransferases, and capsid proteins. The presence of both raw contigs and clustered representatives indicates a highly diverse viral population that has been systematically categorized into vOTUs.

## Reasoning
Given the rich metadata embedded in the contig IDs and the detailed functional annotations, the dataset is perfectly suited for ecological and evolutionary studies of marine RNA viruses. The most compelling avenue of research is to understand how these viruses adapt to different oceanic environments. The surface and deep chlorophyll maximum represent distinct ecological niches with varying light, temperature, and host availability. By comparing the functional domains of viruses from these two depths, we can uncover specific genomic adaptations.

## Top scientific question
How does the functional repertoire of marine RNA viruses differ between surface waters and the deep chlorophyll maximum?

## Why testable on this dataset
This question is highly testable using the provided data. The `functional-annotation-table.tsv` contains all the necessary information: the contig IDs (which include `SUR` or `DCM` to indicate depth) and the annotated Pfam domains for each contig. A researcher can parse this table, group the contigs by depth, and calculate the frequencies of different functional domains (e.g., structural proteins vs. replication machinery) in each group. Statistical tests can then be applied to identify domains that are significantly enriched in either surface or DCM environments, providing insights into depth-specific viral adaptations.