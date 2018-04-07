#!/usr/bin/env python3
"""split FASTA/Q files"""

# Author: Ken Youens-Clark <kyclark@email.arizona.edu>
# Second Author: Scott G Daniel <scottdaniel@email.arizona.edu>

import argparse
import os
from Bio import SeqIO

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    fastx = args.fastx
    out_dir = args.out_dir
    max_per = args.num

    if not os.path.isfile(fastx):
        print('--fastx "{}" is not a file'.format(fastx))
        exit(1)

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    if max_per < 1:
        print("--num cannot be less than one")
        exit(1)

    i = 0
    nseq = 0
    nfile = 0
    out_fh = None
    basename, ext = os.path.splitext(os.path.basename(fastx))

    #
    # The Main Loop
    #

    if is_fasta(fastx) is False: #check whether its fastq
        for record in SeqIO.parse(fastx, "fastq"):
            if i == max_per: #check whether reached max records for a file
                i = 0
                if out_fh is not None: #if it has reached max, close the file
                    out_fh.close() #that way, we'll have a new one
                    out_fh = None

            i += 1
            nseq += 1 #keep track of TOTAL number of sequences
            if out_fh is None:
                nfile += 1 #keep track of TOTAL number of file written
                path = os.path.join(out_dir, basename + '.' + str(nfile) + ext)
                out_fh = open(path, 'wt') #open up a new file

            SeqIO.write(record, out_fh, "fastq") #write the next record to the file, repeat until i reaches the max_per
    elif is_fasta(fastx) is True:
        for record in SeqIO.parse(fastx, "fasta"):
            if i == max_per:
                i = 0
                if out_fh is not None:
                    out_fh.close()
                    out_fh = None

            i += 1
            nseq += 1
            if out_fh is None:
                nfile += 1
                path = os.path.join(out_dir, basename + '.' + str(nfile) + ext)
                out_fh = open(path, 'wt')

            SeqIO.write(record, out_fh, "fasta")
    else:
        print("{} is not a valid FASTA or FASTQ file!".format(fastx))

    #
    # Logging message
    #

    print('Done, wrote {} sequence{} to {} file{}'.format(
        nseq, '' if nseq == 1 else 's',
        nfile, '' if nfile == 1 else 's'))

# --------------------------------------------------
def is_fasta(filename):
    with open(filename, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Split FASTA/Q files')
    parser.add_argument('-f', '--fastx', help='FASTA/Q input file',
                        type=str, metavar='FILE', required=True)
    parser.add_argument('-n', '--num', help='Number of records per file',
                        type=int, metavar='NUM', default=50)
    parser.add_argument('-o', '--out_dir', help='Output directory',
                        type=str, metavar='DIR', default='fxsplit')
    return parser.parse_args()

# --------------------------------------------------
if __name__ == '__main__':
    main()
