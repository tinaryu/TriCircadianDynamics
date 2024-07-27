#!/bin/bash

batch1="batch1_CV-H3K9ac_"
batch2="CV-H3K9ac_"

for i in {2..6}; do
    output="merged_${batch2}${i}"
    echo "Merging ${batch1}${i} and ${batch2}${i}..."
    samtools merge ${output}.bam ${batch1}${i}.sort.bam ${batch2}${i}.sort.bam 
    echo "Sorting and indexing ${output}..."
    samtools sort ${output}.bam -o ${output}.sort.bam
    samtools index ${output}.sort.bam
done
