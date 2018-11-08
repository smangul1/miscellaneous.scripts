#bowtie2-build ref.fasta ref
#bowtie2 -f -x ref -1 reads_1.fasta -2 reads_2.fasta | samtools view -bh - | samtools sort -  >reads.bam
#samtools index reads.bam 
python ../split.unsorted.py reads.bam chr1 reads_chr1.bam

