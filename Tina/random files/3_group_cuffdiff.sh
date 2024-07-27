#!/bin/bash

NR1D1_FILES=(Nr1d1_mm10/*_cufflinks_out/transcripts.gtf)
HDAC3_FILES=(Hdac3_mm10/*_cufflinks_out/transcripts.gtf)
NFIL3_FILES=(Nfil3_mm10/*_cufflinks_out/transcripts.gtf)

cuffdiff -o diff_out -b refMrna.fa -p 8 -L Nr1d1,Hdac3,Nfil3 genes.gtf \
"${NR1D1_FILES[@]}" \
"${HDAC3_FILES[@]}" \
"${NFIL3_FILES[@]}"

