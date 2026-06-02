# Analysis Report

## Data Summary
Two primary datasets available:
1. 5905698_all_virus_genomes.fasta (13.6MB FASTA file with 6,856 virus genome sequences)
2. 5905695_alignments_and_phylogenies.zip (contains multiple alignment files and phylogenetic trees)

## Analysis
FASTA headers reveal structured metadata: [Accession]_[VirusType]_[Location]_[VirusName]_[Length]. Sequence lengths vary from 5,000-10,000 nt. Zip file contains:
- Multiple .aln alignment files
- .nwk phylogenetic tree files
- Metadata spreadsheets

## Reasoning
Virus genome sequences enable evolutionary analysis while phylogenetic trees provide evolutionary relationships. Alignment files allow comparative genomics. Metadata enables geographic and temporal analysis.

## Top Scientific Question
What is the nucleotide diversity (π) across different virus families represented in the genome collection?

## Why Testable on This Dataset
FASTA sequences provide raw genetic data for diversity calculations, while alignment files enable precise nucleotide comparisons across homologous regions. Phylogenetic trees validate evolutionary relationships inferred from diversity metrics.