for($i=1;$i<5;$i++){
$file1="NovaSeq8-KuangZheng-mouse-stranded-mRNAseq/GFBT-".$i."_S".$i."_R1_001.fastq.gz";
	$file2="NovaSeq8-KuangZheng-mouse-stranded-mRNAseq/GFBT-".$i."_S".$i."_R2_001.fastq.gz";
	$file0="GFBTr".$i;
	system("mkdir $file0");
	system("tophat -o $file0 -p 30 -G /mnt/data1/database/mm10/genes.gtf /mnt/data1/database/mm10/mm10 $file1 $file2");
	#$file1="NovaSeq8-KuangZheng-mouse-stranded-mRNAseq/GFW-".$i."_S".($i+4)."_R1_001.fastq.gz";
	#$file2="NovaSeq8-KuangZheng-mouse-stranded-mRNAseq/GFW-".$i."_S".($i+4)."_R2_001.fastq.gz";
	#$file0="GFCVr".$i;
	#system("mkdir $file0");
	#system("tophat -o $file0 -p 30 -G /mnt/data1/database/mm10/genes.gtf /mnt/data1/database/mm10/mm10 $file1 $file2");}
system("mkdir GFBTm");
system("cuffdiff -o GFBTCV -p 30 -u /mnt/data1/database/mm10/genes.gtf GFBTr1/accepted_hits.bam GFBTr2/accepted_hits.bam GFBTr3/accepted_hits.bam GFBTr4/accepted_hits.bam GFCVr1/accepted_hits.bam GFCVr2/accepted_hits.bam GFCVr3/accepted_hits.bam GFCVr4/accepted_hits.bam");