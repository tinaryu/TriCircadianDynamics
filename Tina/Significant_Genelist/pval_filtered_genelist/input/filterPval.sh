#!/bin/bash

# This takes as input replicated data and remove genes that don't have >1 FPKM in at least one sample

for file in *.txt; do
    awk '$17 < 0.05' "$file" > pval_"$file"
done

for file in pval_*.txt; do
    cut -f 1 "$file" > geneID_"$file"

done