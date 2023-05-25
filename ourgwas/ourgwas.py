"""
Script to perform whole genome association analysis with linear regression
"""
import argparse 
from ourgwas import __version__
import os
from cyvcf2 import VCF
from sklearn.linear_model import LinearRegression
import sklearn.decomposition

# Sets up script argument parsing
parser = argparse.ArgumentParser()

# Input
parser.add_argument("--pheno")
# https://www.cog-genomics.org/plink/1.9/input#pheno

# I don't know what 'argparse.FileType('r')' is, so maybe getting rid of it
# is good
parser.add_argument("--vcf", type=argparse.FileType('r'))

# Options
parser.add_argument("--pca", type=int)
parser.add_argument("--maf", type=float)
parser.add_argument("--output", type=str)
parser.add_argument("--qq")

# Output
parser.add_argument("--out", type=argparse.FileType('w'))

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
