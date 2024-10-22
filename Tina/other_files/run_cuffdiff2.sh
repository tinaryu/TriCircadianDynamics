#!/bin/bash

NR1D1_FILES=$(ls Nr1d1_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')
HDAC3_FILES=$(ls Hdac3_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')
NFIL3_FILES=$(ls Nfil3_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')

cuffdiff -o diff_out -b refMrna.fa -p 8 -L Nr1d1,Hdac3,Nfil3 genes.gtf\
${NR1D1_FILES%,}\
${HDAC3_FILES%,}\
${NFIL3_FILES%,}

