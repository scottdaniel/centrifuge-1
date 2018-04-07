#!/usr/bin/env python3

#script that takes a centrifuge report and just spits out taxon_id and names that have abundances greater than 0 
import sys
import argparse
import os
import errno
from plumbum import local
import pandas as pd

p3_all_genomes = local['p3-all-genomes']
egrep = local['egrep']
wget = local['wget']
lc = local['lc']

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script to just print out names and taxon_ids from a centrifuge report")
    
    parser.add_argument("-r", "--report", action="store", \
            help="Centrifuge report, usually: centrifuge_report.tsv", \
            default='./centrifuge_report.tsv')
    parser.add_argument("-t", "--taxid", action="store_true", \
            help="Print only taxids")
    parser.add_argument("-n", "--name", action="store_true", \
            help="Print only species names")
    parser.add_argument("-o", "--output", action="store", \
            help="Output directory for genomes and annotations", \
            default='./')
    parser.add_argument("-a", "--min_abundance", action="store", \
            help="Minimum abundance needed to download a species\' genome", \
            default='.01', type=float)
        
    args = parser.parse_args()

def filter_report(report):
    
    holder = []

    for row in report.itertuples(index=True, name='Pandas'):
        if getattr(row, 'abundance') > args.min_abundance:
            if args.taxid is True and args.name is False:
                print("{:d}".format(getattr(row, 'taxID')))
                holder.append(getattr(row, 'taxID'))
            elif args.name is True and args.taxid is False:
                print("{:s}".format(getattr(row, 'name')))
                holder.append(getattr(row, 'name'))
            else:
                print("{:d}\t{:s}".format(getattr(row,'taxID'),getattr(row,'name')))
                holder.append(str(getattr(row,'taxID'))+'\t'+str(getattr(row,'name')))

def download_genomes(filtered_list):
    for taxID in holder:
        chain = p3_all_genomes('-e', 'taxon_id', taxID, '-e', \
                'genome_status', 'Complete') | egrep('-v', 'genome')
        for patricID in chain():

            print('Getting PATRIC genome_id {} in fasta and Refseq gff formats'.format(patricID))

            wget('ftp://ftp.patricbrc.org/genomes/' + patricID + '/' + \
                    patricID + '.fna')
            
            wget('ftp://ftp.patricbrc.org/genomes/' + patricID + '/' + \
                    patricID + '.RefSeq.gff')
            #if the RefSeq.gff does not exist or it is too small (usually just means its just a header and nothing else) we get the PATRIC.gff

            if not os.path.isfile(patricID + '.RefSeq.gff') or lc(patricID + '.RefSeq.gff') < 5:
                wget('ftp://ftp.patricbrc.org/genomes/' + patricID + '/' + \
                    patricID + '.PATRIC.gff')

            if os.path.isfile(patricID + '.RefSeq.gff'):

                os.remove(patricID + '.RefSeq.gff')

report = pd.read_table(args.report,delimiter='\t')
list_of_taxids_or_names = filter_report(report)
download_genomes(list_of_taxids_or_names)
print('Done!')

