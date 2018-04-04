#!/usr/bin/env bash
#
# Script to get genomes from centrifuge report file using python!!!!
#

set -u

CONFIG="./config.sh"

if [ -e $CONFIG ]; then
    . "$CONFIG"
else
    echo Missing config \"$CONFIG\" ermagod!
    exit 12345
fi

mkdir -p $MY_TEMP_DIR
export CWD="$PWD"
export STEP_SIZE=1

PROG=`basename $0 ".sh"`
STDOUT_DIR="$CWD/out/$PROG"

init_dir "$STDOUT_DIR" 

cd $PRJ_DIR

export CFUGELIST="$MY_TEMP_DIR/report_list"

find $CFUGE_DIR -iname "*report.tsv" > $CFUGELIST

export TODO="$MY_TEMP_DIR/files_todo"

if [ -e $TODO ]; then
    rm $TODO
fi

#TODO: optional logic to check if file has been processed

cat $CFUGELIST >> $TODO

NUM_FILES=$(lc $TODO)

echo Found \"$NUM_FILES\" files in \"$CFUGE_DIR\" to work on

JOB=$(qsub -J 1-$NUM_FILES:$STEP_SIZE -V -N get-genomes -j oe -o "$STDOUT_DIR" $WORKER_DIR/runCfugeToGenomes.sh)

if [ $? -eq 0 ]; then
  echo -e "Submitted job \"$JOB\" for you in steps of \"$STEP_SIZE.\"
 "Make no small plans for they have no power to stir the soul."
   ~Niccolo Machiavelli"
else
  echo -e "\nError submitting job\n$JOB\n"
fi
echo done $(date)

