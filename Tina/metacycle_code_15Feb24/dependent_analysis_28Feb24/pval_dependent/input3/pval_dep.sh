#!/bin/bash

for file in *.txt; do
    comm -23 WT/WT_only.txt "$file" > dep_"$file"

done