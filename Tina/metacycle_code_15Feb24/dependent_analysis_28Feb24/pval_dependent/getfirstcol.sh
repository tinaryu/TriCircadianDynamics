#!/bin/bash
# this cuts the first column -> just get geneID

mkdir -p output

for file in *.txt; do
    # Extract the first column and save it to a new file in the output directory
    cut -f 1 "$file" > "output/geneID_${file}"
done

