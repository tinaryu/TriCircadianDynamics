#!/bin/bash

# Define file paths
GENOME_FA="mm39.fa" # Path to the genome fasta file
GENOME_FAI="mm39.fa.fai" # Path to the genome fasta index file
TSS_BED="tss_regions.bed" # Original TSS regions BED file

# Filter and sort the TSS BED file according to the genome
sort -k1,1 -k2,2n $TSS_BED | awk 'BEGIN{OFS="\t"}{print $1, $2, $3, $4, $5, $6}' > sorted_tss_regions.bed

# BAM files for WT and GF
declare -a BAM_FILES=("CV-H3K9ac_1.sort.bam" "CV-H3K9ac_2.sort.bam" "CV-H3K9ac_3.sort.bam" 
"CV-H3K9ac_4.sort.bam" "CV-H3K9ac_5.sort.bam" "CV-H3K9ac_6.sort.bam" 
"GF-H3K9ac_1.sort.bam" "GF-H3K9ac_2.sort.bam" "GF-H3K9ac_3.sort.bam" "GF-H3K9ac_4.sort.bam")

# Loop through each BAM file to re-sort and index according to the genome file
for BAM_FILE in "${BAM_FILES[@]}"
do
    # Re-sort BAM files according to mm39.fa.fai
    echo "Re-sorting $BAM_FILE according to $GENOME_FAI..."
    SORTED_BAM="sorted_$BAM_FILE"
    samtools sort -o $SORTED_BAM -T temp_prefix -@ 4 --reference $GENOME_FA $BAM_FILE

    # Index the sorted BAM files
    echo "Indexing $SORTED_BAM..."
    samtools index $SORTED_BAM
done

# Run bedtools coverage using sorted and indexed BAM files
for BAM_FILE in "${BAM_FILES[@]}"
do
    SORTED_BAM="sorted_$BAM_FILE"
    OUTPUT_FILE="${SORTED_BAM}_tss_counts.txt"
    echo "Calculating coverage for $SORTED_BAM..."
    bedtools coverage -a sorted_tss_regions.bed -b $SORTED_BAM -sorted -g $GENOME_FAI > $OUTPUT_FILE
done

echo "Coverage calculation complete."

