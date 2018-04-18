# Radcot
A pipeline that can:
- Identify bacterial species from a metagenomic sample
- Download genomes of said species
- Quantify transcripts of genes within these species

## How to use:
1. Use https://www.imicrobe.us/#/apps to access the app with your [cyverse login](http://www.cyverse.org/create-account)
OR
1. git clone https://github.com/scottdaniel/centrifuge-patric
2. Get the singularity image like so: `wget [address we setup]`
3. Run the pipeline on an HPC with a slurm scheduler^1

~~~~
^1 I assume this can be adapted to run on other batch-scheduled high-performance computer systems but I haven't tested that.
~~~~
