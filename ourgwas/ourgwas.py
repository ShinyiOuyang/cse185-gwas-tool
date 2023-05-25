"""
Script to perform whole genome association analysis with linear regression
"""
import argparse 
from ourgwas import __version__
import os
import cyvcf2 as vcf

# Sets up script argument parsing
parser = argparse.ArgumentParser()

# Input
parser.add_argument("--pheno", type=argparse.FileType('r'))
# https://www.cog-genomics.org/plink/1.9/input#pheno

parser.add_argument("--vcf", type=argparse.FileType('r'))

#Options
parser.add_argument("--pca", type=int)
parser.add_argument("--maf", type=float)

# Output
parser.add_argument("--out", type=argparse.FileType('w'))

args = parser.parse_args()

# TODO
def main():
    #for variant in vcf(args.vcf):
    print("Hello World")


if __name__ == "__main__":
    main()
