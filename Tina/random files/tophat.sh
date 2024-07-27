tophat -p $NUM_THREADS -G $GTF -o ${SAMPLE}_tophat_out $GENOME ${SAMPLE}.fastq



#!/bin/bash


GENOME="mm10"
GTF="genes.gtf"
NUM_THREADS=8


SAMPLES=("ZK1" "ZK2" "ZK3" "ZK4" "ZK5" "ZK6" "ZK7" "ZK8" "ZK9" "ZK10" "ZL11" "ZK12")


for SAMPLE in "${SAMPLES[@]}"; do

    tophat -p $NUM_THREADS -G $GTF -o ${SAMPLE}_tophat_out $GENOME ${SAMPLE}.fastq


    cufflinks -p $NUM_THREADS -o ${SAMPLE}_cufflinks_out ${SAMPLE}_tophat_out/accepted_hits.bam
done

tophat -G genes.gtf mm10 ZK1.fastq