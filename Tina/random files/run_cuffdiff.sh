#!/bin/bash

NR1D1_FILES=$(ls Nr1d1_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')
HDAC3_FILES=$(ls Hdac3_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')
NFIL3_FILES=$(ls Nfil3_mm10/*_cufflinks_out/transcripts.gtf | tr '\n' ',')

cuffdiff -o diff_out -b refMrna.fa -p 8 -L Nr1d1,Hdac3,Nfil3 genes.gtf \
${NR1D1_FILES%,} \
${HDAC3_FILES%,} \
${NFIL3_FILES%,}


cuffdiff -o diff_out -b refMrna.fa -p 8 -L Nr1d1,Hdac3,Nfil3 transcripts.gtf\transcripts1.gtf\transcripts2.gtf

cuffdiff -o diff_out -b refMrna.fa -p 8  genes.gtf 


cuffdiff -o diff_out -b refMrna.fa -p 8 -L Nr1d1,Hdac3,Nfil3 genes.gtf \ Nr1d1_mm10/ZK1_cufflinks_out/transcripts.gtf \ Hdac3_mm10/ZK1_cufflinks_out/transcripts.gtf \ Nfil3_mm10/ZK1_cufflinks_out/transcripts.gtf


kuanguser@kuanglabnslook:/mnt/data2/XueK$ cuffdiff  genes.gtf \transcripts.gtf \transcripts1.gtf \transcripts2.gtf
Warning: Could not connect to update server to verify current version. Please check at the Cufflinks website (http://cufflinks.cbcb.umd.edu).
terminate called after throwing an instance of 'std::length_error'
  what():  basic_string::_M_replace_aux


cuffdiff genes.gtf \transcripts.gtf\transcripts1.gtf \transcripts2.gtf

cuffdiff genes.gtf \transcripts.gtf



cuffdiff -o diff_out -b refMrna.fa -p 8 -L ZK1,ZK2,ZK3,ZK4 -u ZK1_cufflinks_out/transcripts.gtf ZK1_tophat_out/accepted_hits.bam ZK2_tophat_out/accepted_hits.bam ZK3_tophat_out/accepted_hits.bam ZK4_tophat_out/accepted_hits.bam


cuffdiff -o diff_out -b refMrna.fa -p 8 -L ZK1,ZK2,ZK3,ZK4 -u ZK1_cufflinks_out/transcripts.gtf \ ZK1_cufflinks_out/genes.fpkm_tracking ZK2_cufflinks_out/genes.fpkm_tracking \ ZK3_cufflinks_out/genes.fpkm_tracking \ ZK4_cufflinks_out/genes.fpkm_tracking


cuffdiff -o output_directory -b reference_genome.fa annotations.gtf \sample1/genes.fpkm_tracking \sample2/genes.fpkm_tracking

cuffmerge transcripts.gtf transcripts1.gtf transcripts2.gtf