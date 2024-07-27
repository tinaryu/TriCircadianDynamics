
<?php
$files = ['CV-H3K9ac1_CGATGT_L008_R1_001.fastq.gz','CV-H3K9ac2_TGACCA_L008_R1_001.fastq.gz','CV-H3K9ac3_ACAGTG_L008_R1_001.fastq.gz','CV-H3K9ac4_GCCAAT_L008_R1_001.fastq.gz','CV-H3K9ac5_CAGATC_L008_R1_001.fastq.gz','CV-H3K9ac6_CTTGTA_L008_R1_001.fastq.gz'];
for ($i = 1; $i < 7; $i++) {
    $file = "/mnt/data2/Seqdata/20151216_ChIPseq/Project_HS375-Lane8/" . $files[$i-1];
	$file2="batch1_CV-H3K9ac_".$i.".sam";
    $file6="batch1_CV-H3K9ac_".$i.".log";
    echo "Running alignment for $file\n";
	system("bowtie2 -p 24 -x /mnt/data2/database/mm10/mm10 -U $file -S $file2 2> $file6");
	###bowtie2 -p 24 -x /mnt/data2/database/mm10/mm10 -U /mnt/data2/Seqdata/20160217_ChIPseq/HS406-Lane-5-*/Sample-ID-122/*R1*.fastq.gz -S CV-H3K9ac_2.sam 2> CV-H3K9ac_2.log
	$file3="batch1_CV-H3K9ac_".$i.".bam";
	$file4="batch1_CV-H3K9ac_".$i.".sort.bam";
    system("echo 'converting sam to bam'");
	system("samtools view -bS $file2 > $file3");
	#samtools view -bS CV-H3K9ac_2.sam > CV-H3K9ac_2.bam
    system("echo 'sorting'");

	system("samtools sort $file3 -o $file4");
    system("echo 'indexing'");
    system("samtools index $file4");
	#samtools sort CV-H3K9ac_2.bam  -o CV-H3K9ac_2.sort
	#samtools index CV-H3K9ac_2.sort.bam
	#system("rm $file3");
}
?> 

