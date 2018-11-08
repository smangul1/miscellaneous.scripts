ls *bam | awk -F ".bam" '{print $1}' >samples.txt


while read line
do

echo "~/project/anaconda2/bin/python /u/home/s/serghei/code/miscellaneous.scripts/split.by.chr.only.mapped.unsorted/split.unsorted.py ${line}.bam 1 ${line}_chr1.bam">run.${line}.sh

echo "~/project/anaconda2/bin/samtools sort ${line}_chr1.bam >${line}_chr1.sort.bam">>run.${line}.sh
echo "/u/home/s/serghei/project/anaconda2/bin/htseq-count --format bam --order pos --mode=intersection-strict --stranded=no ${line}_chr1.sort.bam /u/home/s/serghei/project/Homo_sapiens/Ensembl/Homo_sapiens.GRCh38.79.gtf >${line}_chr1.counts">>run.${line}.sh


qsub -cwd -V -N counts -l h_data=12G,highp,time=10:00:00 run.${line}.sh

done<samples.txt
