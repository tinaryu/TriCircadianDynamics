#!/bin/bash

# # Step 1: Create TSS_regions.bed from genes.gtf
# awk '{
#     if ($3 == "exon" && $7 == "+") {
#         start = ($4 - 1001 > 0) ? $4 - 1001 : 0;
#         end = $4 + 1000;
#         print $1 "\t" start "\t" end "\t" $10 "\t" $18;
#     } else if ($3 == "exon" && $7 == "-") {
#         start = ($5 - 1000 > 0) ? $5 - 1000 : 0;
#         end = $5 + 1001;
#         print $1 "\t" start "\t" end "\t" $10 "\t" $18;
#     }
# }' genes.gtf | tr -d '";' > TSS_regions.bed

# echo "TSS regions prepared."

# Step 2: Run count_reads.sh to perform read counting
output_dir="./counts_per_sample"
mkdir -p $output_dir


echo "Counting reads around TSS..."
for bam in merged_CV-H3K9ac_1.sort.bam \
           merged_CV-H3K9ac_2.sort.bam \
           merged_CV-H3K9ac_3.sort.bam \
           merged_CV-H3K9ac_4.sort.bam \
           merged_CV-H3K9ac_5.sort.bam \
           merged_CV-H3K9ac_6.sort.bam \
           GF-H3K9ac_1.sort.bam \
           GF-H3K9ac_2.sort.bam \
           GF-H3K9ac_3.sort.bam \
           GF-H3K9ac_4.sort.bam
do
    echo "Processing $bam..."
    sample_name=$(basename $bam .sort.bam)
    bedtools intersect -a tss_regions_mm10.bed -b $bam -c | \
    awk -v OFS='\t' '{print $4, $6}' > "${output_dir}/${sample_name}_counts.tsv"
done

echo "Read counts done."

# Step 3: Run combine.py to consolidate counts
echo "Combining counts into a single file..."
python combine.py

echo "Pipeline completed."

