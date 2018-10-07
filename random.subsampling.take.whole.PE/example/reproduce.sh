bwa index ref.fasta
bwa mem -a ref.fasta reads_1.fasta reads_2.fasta | samtools view -bh - | samtools sort -  >reads.bam
samtools index reads.bam 
python ../subsampleBam.py reads.bam reads_0.5.bam 0.51

