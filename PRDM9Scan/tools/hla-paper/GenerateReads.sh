#!/bin/bash

./readsCreator.py ../hla-ref-5gene/IMGT_HLA/PRDM9/$1.fa 30 $1
echo $1
./bwa mem -p hg38.fa $1.fq $1.fq > $1.sam
echo "done"
rm $11.fq
rm $12.fq
samtools view -b -h $1.sam > $1.bam
echo "done"
rm $1.sam
samtools sort $1.bam > $1sorted.mapped.illumina.bwa.ref.exome.30.bam
echo "done"
rm $1.bam
samtools index $1sorted.mapped.illumina.bwa.ref.exome.30.bam
