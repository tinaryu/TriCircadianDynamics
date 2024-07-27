
for($i=1;$i<7;$i++){
	$file="HS406-Lane-5-*/Sample-ID-12".$i."/*R1*.fastq.gz";
	$file2="CV-H3K9ac_".$i.".sam";
	system("bowtie2 -p 24 -x /media/breck/DATA/Databases/mm10/mm10 -U $file -S $file2");
	$file3="CV-H3K9ac_".$i.".bam";
	$file4="CV-H3K9ac_".$i.".sort.bam";
	$file5="CV-H3K9ac_".$i.".sort";
	system("samtools view -bS $file2 > $file3");
	system("samtools sort $file3 $file5");
	system("samtools index $file4");
	#system("rm $file");
	system("rm $file3");
}


for($i=127;$i<130;$i++){
	$file="HS406-Lane-5-*/Sample-ID-".$i."/*R1*.fastq.gz";
	$file2="L5_".$i.".sam";
	system("bowtie2 -p 24 -x /media/breck/DATA/Databases/mm10/mm10 -U $file -S $file2");
	$file3="L5_".$i.".bam";
	$file4="L5_".$i.".sort.bam";
	$file5="L5_".$i.".sort";
	system("samtools view -bS $file2 > $file3");
	system("samtools sort $file3 $file5");
	system("samtools index $file4");
	#system("rm $file");
	system("rm $file3");
}

for($i=1;$i<7;$i++){
	$file="HS406-Lane-6-*/Sample-ID-13".($i-1)."/*R1*.fastq.gz";
	$file2="CV-H3K4me3_".$i.".sam";
	system("bowtie2 -p 24 -x /media/breck/DATA/Databases/mm10/mm10 -U $file -S $file2");
	$file3="CV-H3K4me3_".$i.".bam";
	$file4="CV-H3K4me3_".$i.".sort.bam";
	$file5="CV-H3K4me3_".$i.".sort";
	system("samtools view -bS $file2 > $file3");
	system("samtools sort $file3 $file5");
	system("samtools index $file4");
	#system("rm $file");
	system("rm $file3");
}

for($i=136;$i<139;$i++){
	$file="HS406-Lane-6-*/Sample-ID-".$i."/*R1*.fastq.gz";
	$file2="L6_".$i.".sam";
	system("bowtie2 -p 24 -x /media/breck/DATA/Databases/mm10/mm10 -U $file -S $file2");
	$file3="L6_".$i.".bam";
	$file4="L6_".$i.".sort.bam";
	$file5="L6_".$i.".sort";
	system("samtools view -bS $file2 > $file3");
	system("samtools sort $file3 $file5");
	system("samtools index $file4");
	#system("rm $file");
	system("rm $file3");
}

for($i=1;$i<7;$i++){
	$file="HS406-Lane-7-*/Sample-ID-".($i+138)."/*R1*.fastq.gz";
	$file2="CV-H4K5ac_".$i.".sam";
	system("bowtie2 -p 24 -x /media/breck/DATA/Databases/mm10/mm10 -U $file -S $file2");
	$file3="CV-H4K5ac_".$i.".bam";
	$file4="CV-H4K5ac_".$i.".sort.bam";
	$file5="CV-H4K5ac_".$i.".sort";
	system("samtools view -bS $file2 > $file3");
	system("samtools sort $file3 $file5");
	system("samtools index $file4");
	#system("rm $file");
	system("rm $file3");
}


