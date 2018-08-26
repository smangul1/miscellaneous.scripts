
if [ $# -lt 2 ]
then


echo "[1] - Directory with fastq files"
echo "[2] - id for Google drive"
exit 1
fi

dirSource="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


cd $1

i=0; 
for f in *; 
do 
    d=data_$(printf %03d $((i/10+1))); 
    mkdir -p $d; 
    mv "$f" $d;
    let i++;
done


var=0
var1=1
for d in data_*
do
echo "$var"

echo "done">${d}/done.txt
echo "${dirSource}/gdrive upload -r --parent $2 $d">run.transfer.${d}.sh
#echo "screen -d -m -S $d bash -c '${dirSource}/gdrive upload -r --parent $2 $d'"
if [ "$var" -eq 0 ]
then
echo "var==0"
echo "qsub -cwd -V -N data_$var -l h_data=1G,time=05:00:00 run.transfer.${d}.sh"
else
echo "qsub -hold_jid data_$var -cwd -V -N data_$var1 -l h_data=1G,time=05:00:00 run.transfer.${d}.sh"
fi
((var++))
((var1++))
done




