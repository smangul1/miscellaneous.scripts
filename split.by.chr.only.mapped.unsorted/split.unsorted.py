import pysam
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('inbam', help='')
ap.add_argument('chr', help='')
ap.add_argument('out', help='')
args = ap.parse_args()

samfile = pysam.AlignmentFile(args.inbam, "rb")

#out_samfile = pysam.AlignmentFile(args.out, "wb", template=samfile)





#mapped from particular chr
samfile = pysam.AlignmentFile(args.inbam, "rb")
out_sam = pysam.AlignmentFile(args.out, "wb", template=samfile)

k=0

for read in samfile.fetch(until_eof=True):
    if read.is_paired:
        if not read.is_unmapped and read.reference_name==args.chr:
            out_sam.write(read)
            k+=1
            #print read.query_name, read.is_read1, read.mate_is_unmapped,read
            if read.mate_is_unmapped:
                out_sam.write(read)
                k+=1



print "Number of reads from ", args.chr, " which are mapped - ", k


samfile.close()
out_sam.close()







