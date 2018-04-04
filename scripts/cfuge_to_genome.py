#!/usr/bin/env python

#script that takes a centrifuge report and just spits out taxon_id and names that have abundances greater than 0 
from __future__ import print_function #python3 style printing
import sys
import argparse
import os
import errno
#using plumbum['singularity'] instead of singularity in bash script
#from plumbum import local
import pandas as pd

#sing = local["singularity"]

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script to just print out names and taxon_ids from a centrifuge report")
    
    parser.add_argument("-r", "--report", action="store", \
            help="Centrifuge report file, usually: centrifue_report.tsv")
    parser.add_argument("-t", "--taxid", action="store_true", \
            help="Print only taxids")
    parser.add_argument("-n", "--name", action="store_true", \
            help="Print only species names")
        
    args = vars(parser.parse_args())

report = pd.read_table(args['report'],delimiter='\t')

for row in report.itertuples(index=True, name='Pandas'):
    if getattr(row, 'abundance') > 0:
        if args['taxid'] is True:
            print("{:d}".format(getattr(row, 'taxID')))
        elif args['name'] is True:
            print("{:s}".format(getattr(row, 'name')))
        else:
            print("{:d};{:s}".format(getattr(row,'taxID'),getattr(row,'name')))

