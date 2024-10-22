#!/bin/bash


declare -a BAM_FILES=("CV-H3K9ac_1.sort.bam" "CV-H3K9ac_2.sort.bam" "CV-H3K9ac_3.sort.bam" "CV-H3K9ac_4.sort.bam" "CV-H3K9ac_5.sort.bam" "CV-H3K9ac_6.sort.bam" "GF-H3K9ac_1.sort.bam" "GF-H3K9ac_2.sort.bam" "GF-H3K9ac_3.sort.bam" "GF-H3K9ac_4.sort.bam")

# loop through the BAM files and filter them by chromosomes 1-19, X,Y, M
for BAM_FILE in "${BAM_FILES[@]}"
do
    echo "Processing $BAM_FILE..."
    filtered_BAM="chr1-M_$BAM_FILE"
    samtools view -L chr1-M.bed $BAM_FILE -b -o $filtered_BAM
done