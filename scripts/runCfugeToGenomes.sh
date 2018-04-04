#!/usr/bin/env bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l place=free:shared
#PBS -l select=1:ncpus=1:mem=1gb
#PBS -l walltime=12:00:00
#PBS -l cput=12:00:00
#PBS -M scottdaniel@email.arizona.edu
#PBS -m bea

module load singularity
unset module
set -u

cd $PBS_O_WORKDIR

if [[ -e $SCRIPT_DIR/config.sh ]]; then
    source $SCRIPT_DIR/config.sh
else
    echo no source file...quitting
    exit 1
fi

echo Host \"$(hostname)\"

echo Started $(date)

TMP_FILES=$(mktemp)

get_lines $TODO $TMP_FILES $PBS_ARRAY_INDEX $STEP_SIZE

NUM_FILES=$(lc $TMP_FILES)

if [[ $NUM_FILES -lt 1 ]]; then
    echo Something went wrong or no files to process
    exit 1
else
    echo Found \"$NUM_FILES\" files to process
fi

mkdir -p $GENOME_DIR

cd $GENOME_DIR

#for REPORT in $(cat $TODO); do
#
#    echo Working on report $REPORT
#
#    python $WORKER_DIR/cfuge_report_to_genome.py -r $REPORT
#    
#    echo Unzipping gotten fastas and gffs
#
#    find ./ -iname "*.gz" | xargs -I file gunzip file
#
#done

#Not using the python script anymore
#Patric apparently has better function annotation of the refseq gffs!

export p3="singularity exec $SING_IMG/p3-tools.img"

while read REPORT; do

    echo Working on report $REPORT

    mkdir $(basename $REPORT)
    cd $(basename $REPORT)

    TEMPFILE=$(mktemp)

    python $WORKER_DIR/cfuge_report_filter.py -r $REPORT > $TEMPFILE

    while read LINE; do
       
        taxon_id=$(echo $LINE | cut -f 1 -d ';')
        name=$(echo $LINE | cut -f 2 -d ';')

        echo "Taxon ID is $taxon_id"
        echo "Species is $name"

#not using -e species,"$name" 

        for patricID in $($p3 p3-all-genomes -e taxon_id,"$taxon_id" -e genome_status,"Complete" | egrep -v "genome"); do

            echo "Getting PATRIC genome_id $patricID in fasta and Refseq gff formats"

            wget ftp://ftp.patricbrc.org/genomes/"$patricID"/"$patricID".fna
            
            wget ftp://ftp.patricbrc.org/genomes/"$patricID"/"$patricID".RefSeq.gff

            #if the RefSeq.gff does not exist or it is too small (usually just means its just a header and nothing else) we get the PATRIC.gff
            if [[ ( ! -e "$patricID".RefSeq.gff ) || \
                ( $(lc "$patricID".RefSeq.gff) -lt 5 ) ]]; then
                
                wget ftp://ftp.patricbrc.org/genomes/"$patricID"/"$patricID".PATRIC.gff

                #naturally this will give an error if it does not exist
                #but we can ignore that
                rm "$patricID".RefSeq.gff &> /dev/null

            fi

        done

    done < $TEMPFILE

done < $TMP_FILES

echo Done at $(date)
