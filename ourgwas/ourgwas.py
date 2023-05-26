"""
Script to perform whole genome association analysis with linear regression
"""
import argparse 
from ourgwas import __version__
import os
from cyvcf2 import VCF
import sklearn.decomposition
import pandas as pd
import numpy as py
import scipy



# Sets up script argument parsing
parser = argparse.ArgumentParser()

# Required Input
parser.add_argument("pheno", help="the input file containing normalized values for phenotypes of the samples")
# https://www.cog-genomics.org/plink/1.9/input#pheno

parser.add_argument("vcf", help="the input file to run pca and gwas")

# Options
parser.add_argument("--pca", metavar="n", type=int, default=5, help="specifies the number of prinicple components")
parser.add_argument("--maf", metavar="n", type=float, default=0.01, help="specifies the threshold to consider the minor allele (default = 0.01)")
parser.add_argument("--qq", action="store_true", help="add a qq plot to the output")

# Output options
parser.add_argument("-O", "--out", metavar="filename", help="specifies the output root file name (default = ourgwas.out.txt)")

# Combines all parsed args to be used
args = parser.parse_args()

def main():    
    # Check if --out was set
    if args.out is None:
        # Set default name of output file
        args.out = "ourgwas.out.txt"
        
    phenotype_array = get_phenotypes() # Gets array of normalized phenotype values
    
    # Write to output file
    with open (args.out, "w") as writer:
        column_names = ['CHR', 'SNP', 'BP', 'NMISS', 'BETA', 'P'] # Column names of the output file (same as plink)
        joined_column_names = "\t".join(column_names) + "\n"      # Align all the column names
        writer.write(joined_column_names)
        
        for variant in VCF(args.vcf):
            output_info = []
            genotype_array = []
            
            for genotype in variant.genotypes:
                # quantifies genotype
                # 0 | 0 becomes 0
                # 1 | 0 or 0 | 1 becomes 1
                # 1 | 1 becomes 2
                genotype_array.append(genotype[0] + genotype[1])

            # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
            reg = scipy.stats.linregress(genotype_array, phenotype_array)

            # All information that is outputted
            
            output_info.append(str(variant.CHROM))          # Chromosome number
            output_info.append(str(variant.ID))             # SNP identifier
            output_info.append(str(variant.POS))            # Base pair coordinate
            output_info.append(str(len(variant.genotypes))) # Number of observations
            output_info.append(str(reg.rvalue))             # Regression coefficient
            output_info.append(str(reg.pvalue))             # Asymptotic p-value for a two-sided t-test
            curr_output = "\t".join(output_info) + "\n"
            writer.write(curr_output)

# Puts the values in the third column of the phenotype file into an array
def get_phenotypes():
    phenotypes = []
    
    with open(args.pheno, "r") as pheno_reader:
        
        for line in pheno_reader:
            content = line.split("\t")
            #strip() gets rid of the newline ("\n") at the end
            phenotypes.append(float(content[2].strip()))
            
    return phenotypes


if __name__ == "__main__":
    main()