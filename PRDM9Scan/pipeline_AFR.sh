cd sortie_qsub

chaine_bam=".bam"
chaine_sam=".sam"
chaine_bai=".bam.bai"
chaine_1.fastq="_1.fastq.gz"
chaine_2.fastq="_2.fastq.gz"

for line in $(cat /work/gad/sv347413/Alignements_PRDM9/individus1000G_AFR.txt)
do
	indv=`echo $line | cut -f1 -d*`
	lien=`echo $line | cut -fÃ2 -d*`
	fastq=`echo $line | cut -f8 -d/`
	fastq1=${fastq}${chaine_1.fastq}
	fastq2=${fastq}${chaine_2.fastq}
	BAM=${indv}${chaine_bam}
	BAI=${indv}${chaine_bai}
	SAM=${indv}${chaine_sam}

	if [ ! -e /work/gad/sv347413/Alignements_PRDM9/fastq/$fastq ]
	then
		wget $lien
	fi

	if [ ! -e /work/gad/sv347413/Alignements_PRDM9/BAM_AFR/$indv/$SAM ]
	then
		bwa mem /work/gad/.../Grch38.fa $fastq1 $fastq2 > $SAM
	fi

	if [ ! -e /work/gad/.../$BAI ]
	then
		samtools view -b $SAM | samtools sort > $BAM
		samtools index $BAM
	fi
	
	if [ -e /work/gad/sv347413/Alignements_PRDM9/BAM_AFR/$indv/$BAI ] && [ ! -e /work/gad/sv347413/Alignements_PRDM9/results_AFR/$indv ]
	then
		qsub -v BAM=/work/gad/sv347413/Alignements_PRDM9/BAM_AFR/$indv/$BAM,SORTIE=/work/gad/sv347413/Alignements_PRDM9/results_AFR/,GL=/work/gad/shared/analyse/test_HLA/HLAscan_v1.0/hla-ref-5gene/gene_list_PRDM9 /work/gad/shared/analyse/test_HLA/HLAscan_v1.0/hla-paper/haplo_scan_PRDM9.sh
	fi
	if [ -e /work/gad/sv347413/Alignements_PRDM9/results_AFR/$indv ]
	then
		echo $indv >> /work/gad/sv347413/Alignements_PRDM9/tableau_AFR
		cat /work/gad/sv347413/Alignements_PRDM9/results_AFR/$indv/Report >> /work/gad/sv347413/Alignements_PRDM9/tableau_AFR
	fi 
done
