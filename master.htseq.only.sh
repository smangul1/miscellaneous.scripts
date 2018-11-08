ls *bam | awk -F ".bam" '{print $1}' >samples.txt

while read line
do

echo ". /u/local/Modules/default/init/modules.sh">run.${line}.sh
echo "module load python">>run.${line}.sh
gtf=/u/home/s/serghei/project/Homo_sapiens/Ensembl/Homo_sapiens.GRCh38.79.gtf



htseq=/u/home/s/serghei/project/anaconda2/bin/htseq-count

echo "~/project/anaconda2/bin/samtools sort ${line}.bam >${line}.sort.bam" >>run.${line}.sh
echo "~/project/anaconda2/bin/samtools index ${line}.sort.bam">>run.${line}.sh

echo "$htseq --format bam --order pos --mode=intersection-strict --stranded=no ${line}.sort.bam $gtf >${line}.counts">>run.${line}.sh

qsub -cwd -V -N count -l h_data=24G,highp,time=24:00:00 run.${line}.sh




done<samples.txt
