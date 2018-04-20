# Radcot Part 1
A pipeline that can:
- Identify bacterial species from a metagenomic sample
- Download genomes of said species

## In part 2 [here](https://github.com/hurwitzlab/bowcuff)
- Quantify transcripts of genes within these species
- Generate graphs of RNA count differences

## How to use:
1. Use https://www.imicrobe.us/#/apps to access the app with your [cyverse login](http://www.cyverse.org/create-account)
OR
1. git clone https://github.com/scottdaniel/centrifuge-patric
2. Get the singularity image like so: `wget [address we setup]`
3. Run the pipeline on an HPC with a slurm scheduler<sup>1</sup>

~~~~
<sup>1</sup>I assume this can be adapted to run on other 
batch-scheduled high-performance computer systems 
but this has not been tested.
~~~~
