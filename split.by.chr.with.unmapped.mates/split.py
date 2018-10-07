import pysam
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('inbam', help='')
ap.add_argument('chr', help='')
ap.add_argument('out', help='')
args = ap.parse_args()

samfile = pysam.AlignmentFile(args.inbam, "rb")

#out_samfile = pysam.AlignmentFile(args.out, "wb", template=samfile)


dict={}
k=0

for read in samfile.fetch():
    if read.is_paired:
        if read.is_unmapped:
            dict[read.query_name]=read
            k+=1
    else:
        print "Warning : Unpaired read", read
samfile.close()

print "Number of unmapped reads", k


#mapped from particular chr
samfile = pysam.AlignmentFile(args.inbam, "rb")
out_sam = pysam.AlignmentFile(args.out, "wb", template=samfile)

k=0

for read in samfile.fetch(args.chr):
    if read.is_paired:
        if not read.is_unmapped:
            out_sam.write(read)
            #print read.query_name, read.is_read1, read.mate_is_unmapped,read
            if read.mate_is_unmapped:
                out_sam.write(dict[read.query_name])
                k+=1
#k+=1
samfile.close()

print "Number of reads from ", args.chr, " which are discordant - ", k


samfile.close()








