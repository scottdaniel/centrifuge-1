#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 02:00:00
#SBATCH -p development
#SBATCH -J cntrfuge
#SBATCH --mail-type BEGIN,END,FAIL
#SBATCH --mail-user scottdaniel@email.arizona.edu

OUT_DIR="$WORK/centrifuge/test"

[[ -d "$OUT_DIR" ]] && rm -rf $OUT_DIR/*

sh run.sh -f "$WORK/in/DNA_control_R1.fastq" -r "$WORK/DNA_control_R2.fastq" -o $OUT_DIR
