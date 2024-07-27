#!/bin/bash

files=(
    "merged_CV-H3K9ac_1.sort.bam"
    "merged_CV-H3K9ac_2.sort.bam"
    "merged_CV-H3K9ac_3.sort.bam"
    "merged_CV-H3K9ac_4.sort.bam"
    "merged_CV-H3K9ac_5.sort.bam"
    "merged_CV-H3K9ac_6.sort.bam"
    "GF-H3k9ac_1.sort.bam"
    "GF-H3k9ac_2.sort.bam"
    "GF-H3k9ac_3.sort.bam"
    "GF-H3k9ac_4.sort.bam"
)

names=(
    "CV-H3K9ac_1"
    "CV-H3K9ac_2"
    "CV-H3K9ac_3"
    "CV-H3K9ac_4"
    "CV-H3K9ac_5"
    "CV-H3K9ac_6"
    "GF-H3k9ac_1"
    "GF-H3k9ac_2"
    "GF-H3k9ac_3"
    "GF-H3k9ac_4"
)

for ((i=0; i<= 9; i++))
do
    echo ${names[i]}
    bedtools intersect -a tss_regions_mm10.bed -b ${files[i]} -bed -wa -wb > intersected_${names[i]}.bed
    awk '{print $4}' intersected_${names[i]}.bed | sort | uniq -c > read_counts_per_gene_${names[i]}.txt
done