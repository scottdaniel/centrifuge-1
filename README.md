## [centrifuge-patric - Radcot Part One - YOU ARE HERE](https://github.com/scottdaniel/centrifuge-patric)
- Identify bacterial species from a metagenomic sample
- Download genomes of said species

### [bowtie-samtools - Radcot Part Two - 2nd step](https://github.com/hurwitzlab/bowtie-samtools)
- Quantify transcripts of genes within these species

### [cuffdiff-keggR - Radcot Part Three - 3rd step](https://github.com/hurwitzlab/cuffdiff-keggR)
- Annotate RNA counts of genes with KEGG pathway information
- Generate graphs of RNA count differences per KEGG module

## How to use:
1. Use https://www.imicrobe.us/#/apps to access the app with your [cyverse login](http://www.cyverse.org/create-account)
OR
1. git clone https://github.com/scottdaniel/centrifuge-patric
2. Get the singularity image like so: `wget [address we setup]`
3. Run the pipeline on an HPC with a slurm scheduler<sup>1</sup>

---
<sup>1</sup>I assume this can be adapted to run on other 
batch-scheduled high-performance computer systems 
but this has not been tested.
