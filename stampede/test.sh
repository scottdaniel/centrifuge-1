#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 24:00:00
#SBATCH -p normal
#SBATCH -J cntrfuge
#SBATCH --mail-type BEGIN,END,FAIL
#SBATCH --mail-user scottdaniel@email.arizona.edu

OUT_DIR="$WORK/scottdaniel/gzip_test"

export MY_PARAMRUN="$HOME/launcher/paramrun"

[[ -d "$OUT_DIR" ]] && rm -rf $OUT_DIR/*

<<<<<<< HEAD
bash run.sh -q "$WORK/in" -f fastq -o $OUT_DIR -x 9606,32630
||||||| merged common ancestors
sh run.sh -q "$WORK/data/dolphin/fasta/Dolphin_1_z04.fa" -q "$WORK/data/dolphin/fasta/Dolphin_3_z11.fa" -o $OUT_DIR
=======
sh run.sh -i nt -q "$WORK/data/dolphin/fasta/Dolphin_1_z04.fa" -q "$WORK/data/dolphin/fasta/Dolphin_3_z11.fa" -o $OUT_DIR

#sh run.sh -q "$WORK/data/human_salivary/fizkin/query" -o "$WORK/data/human_salivary/centrifuge-shared" -x 9606
>>>>>>> 6cdbc66c6abced72fd41ebe182361bf4dd23acc7
