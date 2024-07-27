#!/bin/bash


declare -a BAM_FILES=("CV-H3K9ac_1.sort.bam" "CV-H3K9ac_2.sort.bam" "CV-H3K9ac_3.sort.bam" "CV-H3K9ac_4.sort.bam" "CV-H3K9ac_5.sort.bam" "CV-H3K9ac_6.sort.bam" "GF-H3K9ac_1.sort.bam" "GF-H3K9ac_2.sort.bam" "GF-H3K9ac_3.sort.bam" "GF-H3K9ac_4.sort.bam")

# loop through the BAM files and filter them by chromosomes 1-19, X,Y, M
for BAM_FILE in "${BAM_FILES[@]}"
do
    echo "Processing $BAM_FILE..."
    filtered_BAM="chr1-Y_$BAM_FILE"
    samtools view -L chr1-Y.bed $BAM_FILE -b -o $filtered_BAM

    
    OUTPUT_FILE="${filtered_BAM}_tss_counts.txt"
    echo "Calculating coverage for $BAM_FILE..."
    bedtools coverage -a sortedmm10tss.bed -b $filtered_BAM -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > $OUTPUT_FILE
done


