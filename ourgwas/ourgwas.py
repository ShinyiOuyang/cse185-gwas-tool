"""
Script to perform whole genome association analysis with linear regression
"""
import argparse 
from ourgwas import __version__
import os
from cyvcf2 import VCF
from sklearn.linear_model import LinearRegression
import sklearn.decomposition
import pandas as pd
import numpy as py

# Sets up script argument parsing
parser = argparse.ArgumentParser()

# Input
parser.add_argument("in.pheno", type=argparse.FileType('r'), help="the input file containing normalized values for phenotypes of the samples")
# https://www.cog-genomics.org/plink/1.9/input#pheno

parser.add_argument("in.vcf.gz", type=argparse.FileType('r'), help="the input file to run pca and gwas")

# Options
parser.add_argument("--pca", metavar="n", type=int, help="specifies the number of prinicple components")
parser.add_argument("--maf", metavar="n", type=float, default=0.01, help="specifies the threshold to consider the minor allele (default = 0.01)")
parser.add_argument("--qq", action="store_true", help="add a qq plot to the output")

# Output
parser.add_argument("-O", "--out", metavar="filename", type=argparse.FileType('w'), help="specifies the output root file name")

args = parser.parse_args()

print(args.vcf)
print(args.pheno)
# TODO
def main():
    print("Hello World")
    phenotype_array = get_phenotypes()
    print(phenotype_array)
    for variant in VCF(args.vcf):
        #print(variant)
        genotype_array = []
        for genotype in variant.genotypes:
            genotype_array.append(genotype[0]+ genotype[1])
        #print(genotype_array)

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
