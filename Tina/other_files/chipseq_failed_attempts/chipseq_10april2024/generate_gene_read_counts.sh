#!/bin/bash

# Define the path to the sorted and filtered TSS regions BED file
TSS_BED="sorted_tss_regions.bed"

# Define your BAM files. Assuming they are already sorted and you want to use the corresponding coverage files.
declare -a BAM_FILES=("CV-H3K9ac_1.sort.bam" "CV-H3K9ac_2.sort.bam" "CV-H3K9ac_3.sort.bam"
"CV-H3K9ac_4.sort.bam" "CV-H3K9ac_5.sort.bam" "CV-H3K9ac_6.sort.bam"
"GF-H3K9ac_1.sort.bam" "GF-H3K9ac_2.sort.bam" "GF-H3K9ac_3.sort.bam" "GF-H3K9ac_4.sort.bam")

# Loop through each BAM file
for BAM_FILE in "${BAM_FILES[@]}"
do
    # Extract the basename of the BAM file for naming the output
    BASENAME=$(basename "$BAM_FILE" .sort.bam)
    
    # Define the input coverage file generated from bedtools coverage
    COVERAGE_FILE="sorted_${BASENAME}.sort.bam_tss_counts.txt"
    
    # Define the output file for gene read counts
    OUTPUT_FILE="gene_read_counts_${BASENAME}.txt"
    
    echo "Processing $COVERAGE_FILE to generate $OUTPUT_FILE..."
    
    # Perform the analysis and write the output
    awk '{print $4, $7}' "$COVERAGE_FILE" | sort | uniq -c | awk '{print $2, $3, $1}' > "$OUTPUT_FILE"
done

echo "All files processed."

