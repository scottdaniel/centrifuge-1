#!/usr/bin/env python3
"""split FASTA/Q files"""

# Author: Ken Youens-Clark <kyclark@email.arizona.edu>
# Second Author: Scott G Daniel <scottdaniel@email.arizona.edu>
import re
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

    basename, ext = os.path.splitext(os.path.basename(fastx))

    #
    # The Main Loop
    #

    # New way to do it, from biopython.org/wiki/Split_large_file
    if is_fasta(fastx) is False: #check whether its fastq
#        print("This is a fastq") #debug check
        record_iter = SeqIO.parse(open(fastx),'fastq')
        for i, batch in enumerate(batch_iterator(record_iter, max_per)):
            filename = os.path.join(out_dir, basename + '.' + str(i+1) + '.fastq')
            with open(filename, "w") as handle:
                count = SeqIO.write(batch, handle, "fastq")
            print("Wrote {:d} records to {:s}".format(count, filename))

    elif is_fasta(fastx) is True:
#        print("this is a fasta") #debug check
        record_iter = SeqIO.parse(open(fastx),'fasta')
        for i, batch in enumerate(batch_iterator(record_iter, max_per)):
            filename = os.path.join(out_dir, basename + '.' + str(i+1) + '.fasta')
            with open(filename, "w") as handle:
                count = SeqIO.write(batch, handle, "fasta")
            print("Wrote {:d} records to {:s}".format(count, filename))

    else:
        print("{} is not a valid FASTA or FASTQ file!".format(fastx))

# --------------------------------------------------
def is_fasta(filename):
    #pseudocode:
    #use re to construct something like "^[ATCGN]+$" matching pattern
    #read first 8 lines of the file
    #a fastq file will only have 2 lines that have just the pattern
    #while a fasta will have 4 lines that have just that pattern
    #Note: this will not work for multi-line fasta
    with open(filename, 'r') as f:
        nucleotide_line_count = 0
        for i in range(8):
            line = f.readline().strip()
#            print(line) #debug
            if re.fullmatch('^[ATCGN]+$',line) is not None:
                nucleotide_line_count += 1
            else:
                continue
        #debugging text
#        print("Found {} matching nucleotide lines".format(nucleotide_line_count))

        if nucleotide_line_count == 2:
            return False #fastq
        elif nucleotide_line_count == 4:
            return True #fasta
        else:
            return None



# New way to do it, from biopython.org/wiki/Split_large_file
# --------------------------------------------------
def batch_iterator(iterator, batch_size):
    """Returns lists of length batch_size.

    This can be used on any iterator, for example to batch up
    SeqRecord objects from Bio.SeqIO.parse(...), or to batch
    Alignment objects from Bio.AlignIO.parse(...), or simply
    lines from a file handle.

    This is a generator function, and it returns lists of the
    entries from the supplied iterator.  Each list will have
    batch_size entries, although the final list may be shorter.
    """
    entry = True  # Make sure we loop once
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = next(iterator)
            except StopIteration:
                entry = None
            if entry is None:
                # End of file
                break
            batch.append(entry)
        if batch:
            yield batch


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
