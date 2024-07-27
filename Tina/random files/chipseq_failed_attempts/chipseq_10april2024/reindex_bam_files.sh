#!/bin/bash

# Directory where the BAM files are located
DIR="/mnt/data2/xuek/chip_analysis_25Mar2024"

# Array of BAM file names
BAM_FILES=("CV-H3K9ac_1.sort.bam" "CV-H3K9ac_2.sort.bam" "CV-H3K9ac_3.sort.bam" "CV-H3K9ac_4.sort.bam" "CV-H3K9ac_5.sort.bam" "CV-H3K9ac_6.sort.bam" "GF-H3K9ac_1.sort.bam" "GF-H3K9ac_2.sort.bam" "GF-H3K9ac_3.sort.bam" "GF-H3K9ac_4.sort.bam")

# Loop through the BAM files and index each one
for BAM in "${BAM_FILES[@]}"
do
  samtools index "$DIR/$BAM"
done

