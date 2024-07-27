#!/bin/bash

# This takes as input replicated data and remove genes that don't have >1 FPKM in at least one sample

for file in *.txt; do
if [ "$file" = "nfil3_WT.txt" ] || [ "$file" = "nfil3_KO.txt" ]; then
    awk '$2 > 1 || $3 > 1 || $4 > 1 || $5 > 1 || $6 > 1 || $7 > 1' "$file" > expressed_"$file" 
else
    awk '$2 > 1 || $3 > 1 || $4 > 1 || $5 > 1' "$file" > expressed_"$file" 
fi

done

for file in *.txt; do
    if [ "$file" = "nfil3_WT.txt" ] || [ "$file" = "nfil3_KO.txt" ]; then
        awk '$2 > 1 || $3 > 1 || $4 > 1 || $5 > 1 || $6 > 1 || $7 > 1' "$file" > expressed_"$file"
    else
        awk '$2 > 1 || $3 > 1 || $4 > 1 || $5 > 1' "$file" > expressed_"$file"
    fi
done