# Data summary

The visible data consist of a Nature life-sciences reporting summary PDF and two Excel supplements. `data/41586_2018_12_MOESM2_ESM.xlsx` is a sequencing-library inventory with 126 actual library rows after excluding the total and footnote rows. Its key fields are `Library Code`, `Host Class`, `Host Orders`, `Host Species`, `Host Organ`, `Locations`, `Data (bp)`, and `Library Accession`. `data/41586_2018_12_MOESM3_ESM.xlsx` is a virus-catalog table with 270 actual virus records after excluding its footnote row. It includes `Classification`, `Virus Name`, `Tissue`, `Accession`, `Length`, `% reads *`, `Coverage *`, `Host class`, `Host order`, `Host species`, `Blastx hits on known viruses (blast amino acid identity)`, and `Note`. The PDF states that the study surveyed more than 186 chordate host species for virus discovery, with viral genomes confirmed by next-generation and Sanger sequencing and analyses including phylogenetics and co-divergence.

# Analysis

The 126 library rows contain 805.75 Gb of sequence data, with a median of 6.17 Gb per library and a range from 2.83 to 15.68 Gb. Library sampling spans 185 host-species strings and is concentrated in Actinopterygii (44 library mentions), Chondrichthyes (38), Amphibia (18), Reptilia (17), and Agnatha (17), with smaller Sarcopterygii and Leptocardii representation. The most common library organs are gut (45 single-organ libraries), liver (33), gill (30), and lung (6), with additional mixed-organ libraries.

The virus table contains 228 unique virus names and 270 unique accessions across 31 classifications. The leading classifications are `Astroviridae` (57 records), `Picornaviridae` (46), `Caliciviridae` (24), `Orthomyxoviridae: Influenza virus` (18), `Flaviviridae: Hepacivirus` (15), and `Bunyavirales: Hantaviridae` (15). Host-class counts are uneven: Actinopterygii account for 138 virus records, Reptilia 50, Chondrichthyes 32, Amphibia 31, Agnatha 15, and Sarcopterygii 4. Expanded tissue counts show 164 gut detections, 80 gill, 78 liver, and 32 lung. Read fraction and coverage are strongly coupled on a log scale (Pearson r = 0.94, n = 259), supporting their joint use as abundance evidence. The BLASTx identities are mostly low: among 243 parseable identities, the median is 35%, and 173 are at or below 40%.

# Reasoning

The strongest scientific opportunity is not simply cataloging viruses, but testing how virome composition varies across host evolutionary strata and anatomical sampling sites while accounting for sequencing depth and abundance. The dataset links library-level sampling effort to virus-level host taxonomy, tissue, classification, abundance, coverage, and similarity to known viruses. The combination of broad chordate host coverage, many low-identity viruses, and repeated tissue categories makes host taxonomy versus tissue tropism the central testable axis.

# Top scientific question

How do vertebrate host taxonomy and tissue tropism jointly shape RNA virus richness, abundance, and family composition across the 126-library chordate metatranscriptomic survey?

# Why this question is testable on the provided dataset.

The question can be tested by joining `Library Code` from the library inventory to `Library` in the virus catalog, then modeling virus richness and family composition using `Host Class`, `Host Orders`, `Host Species`, `Host Organ`/`Tissue`, and `Data (bp)`. `% reads *` and `Coverage *` provide abundance measures, while `Classification` and `Virus Name` support diversity and composition analyses across host and tissue groups.
