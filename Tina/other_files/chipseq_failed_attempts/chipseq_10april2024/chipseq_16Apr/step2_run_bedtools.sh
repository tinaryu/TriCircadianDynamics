#!/bin/bash

# Define file paths
GENOME_FA="/mnt/data2/database/mm10/chromFa/mm10.fa" # Path to the genome fasta file
GENOME_FAI="/mnt/data2/database/mm10/chromFa/mm10.fa.fai" # Path to the genome fasta index file
TSS_BED="tss_regions_mm10.bed" # Original TSS regions BED file

# Filter and sort the TSS BED file according to the genome
sort -k1,1 -k2,2n $TSS_BED | awk 'BEGIN{OFS="\t"}{print $1, $2, $3, $4, $5, $6}' > sorted_tss_regions.bed


sort -k1,1 -k2,2n new_tss_mm10.bed | awk 'BEGIN{OFS="\t"}{print $1, $2, $3, $4, $5, $6}' > sorted_new_tss_mm10.bed

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

samtools sort -o shGF1_sorted.bam -T temp_prefix -@ 4 --reference /mnt/data2/database/mm10/chromFa/mm10.fa shGF1_filt.sort.bam
samtools index shGF1_sorted.sort.bam




# Run bedtools coverage using sorted and indexed BAM files
for BAM_FILE in "${BAM_FILES[@]}"
do
    SORTED_BAM="sorted_$BAM_FILE"
    OUTPUT_FILE="${SORTED_BAM}_tss_counts.txt"
    echo "Calculating coverage for $SORTED_BAM..."
    bedtools coverage -a sorted_tss_regions.bed -b $SORTED_BAM -sorted -g $GENOME_FAI > $OUTPUT_FILE
done

bedtools coverage -a sorted_new_tss_mm10.bed -b sorted_GF-H3K9ac_1.sort.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > test_tss_counts.txt

bedtools coverage -a new_tss_mm10.bed -b shGF1_filtered.bam -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > test_tss_counts.txt


bedtools coverage -a sorted_tss_regions.bed -b shGF1_filt_rh_.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > test_RHfiltGF1_tss_counts.txt

bedtools coverage -a sorted_new_tss_mm10.bed -b shGF1_sorted.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > tss_counts_shGF1.txt

echo "Coverage calculation complete."

bedtools coverage -a sorted_new_tss_mm10.bed -b shGF1_sorted.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > test_tss_counts2.txt


bedtools coverage -a sorted_tss_regions.bed -b shGF1_sorted.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > testtt.bam

bedtools coverage -a sortedmm10tss.bed -b shGF1_sorted.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > testtt.bam

bedtools sort -faidx /mnt/data2/database/mm10/chromFa/mm10.fa.fai -i new_tss_mm10.bed > sortedmm10tss.bed

bedtools coverage -a sortedmm10tss.bed -b shGF1_sorted.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > testtt.txt


samtools sort -o sorted_chr1-M_CV-H3K9ac_1.sort.bam -T temp_prefix -@ 4 --reference /mnt/data2/database/mm10/chromFa/mm10.fa.fai chr1-M_CV-H3K9ac_1.sort.bam

samtools index sorted_chr1-M_CV-H3K9ac_1.sort.bam

bedtools coverage -a sortedmm10tss.bed -b sorted_chr1-M_CV-H3K9ac_1.sort.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > chr1-M_CV-H3K9ac_1.sort.bam_tss_counts.txt

bedtools coverage -a sortedmm10tss.bed -b chr1-Y_CV-H3K9ac_1.sort.bam -sorted -g /mnt/data2/database/mm10/chromFa/mm10.fa.fai > chr1-Y_CV-H3K9ac_1.sort.bam_tss_counts.txt


samtools view -L chr1-Y.bed CV-H3K9ac_1.sort.bam -b -o chr1-Y_CV-H3K9ac_1.sort.bam


