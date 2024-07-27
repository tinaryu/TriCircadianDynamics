#!/bin/bash

files=(
    "GF-H3k9ac_1.sort.bam"
    "GF-H3k9ac_2.sort.bam"
    "GF-H3k9ac_3.sort.bam"
    "GF-H3k9ac_4.sort.bam"
    "merged_CV-H3K9ac_1.sort.bam"
    "merged_CV-H3K9ac_2.sort.bam"
    "merged_CV-H3K9ac_3.sort.bam"
    "merged_CV-H3K9ac_4.sort.bam"
    "merged_CV-H3K9ac_5.sort.bam"
    "merged_CV-H3K9ac_6.sort.bam"
)

# code reference: https://www.metagenomics.wiki/tools/samtools/number-of-reads-in-bam-file
## counting only mapped (primary aligned) reads
for file in "${files[@]}"; do
    echo $file
    samtools view -c -F 260 $file
done

# samtools view -c -F 4 $file 
# count only mapped reads
#samtools view -c -F 260 $file