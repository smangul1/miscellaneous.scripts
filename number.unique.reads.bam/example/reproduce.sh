bwa index ref.fasta
bwa mem -a ref.fasta reads_1.fasta reads_2.fasta | samtools view -bh - | samtools sort -  >reads.bam
samtools index reads.bam 
python ../number.reads.bam.py $PWD/reads.bam reads.csv
