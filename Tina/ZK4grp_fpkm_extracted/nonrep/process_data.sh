#!/bin/bash

# This duplicates columns to make duplicated data

for file in *.txt; do
if [ "$file" = "nfil3_WT.txt" ] || [ "$file" = "nfil3_KO.txt" ]; then
    paste <(cut -f 1-7 "$file") <(cut -f 2-7 "$file") > rep/"$file"
else
    paste <(cut -f 1-5 "$file") <(cut -f 2-5 "$file") > rep/"$file"
fi

done