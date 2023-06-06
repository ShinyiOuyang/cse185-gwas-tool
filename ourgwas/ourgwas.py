"""
Script to perform whole genome association analysis with linear regression
"""
import argparse 
from ourgwas import __version__
from cyvcf2 import VCF
import pandas as pd
import numpy as py
import scipy
import subprocess, logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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
parser.add_argument("-o", "--out", metavar="filename", help="specifies the output root file name (default = ourgwas.out.txt)")

# Combines all parsed args to be used
args = parser.parse_args()

def main():    
    # Check if --out was set
    if args.out is None:
        # Set default name of output file
        args.out = "ourgwas.out.txt"
        
    # Check if the input argument is valid
    if not args.vcf.endswith('.vcf') | args.vcf.endswith('.vcf.gz'):
        # Send error to user
        raise argparse.ArgumentTypeError('argument filetype must be a vcf or zipped vcf')
    
    logging.info("Pruning through vcf file with MAF threshold")

    # Prune input file using the MAF threshold
    bcftools_maf = "MAF<{}".format(args.maf)
    subprocess.run(
        "bcftools view -e '{}' {} -o intermediate.vcf".format(bcftools_maf, args.vcf),
            shell=True)
            
    phenotype_array = get_phenotypes() # Gets array of normalized phenotype values

    # Write to output file
    with open (args.out, "w") as writer:
        column_names = ['CHR', 'SNP', 'BP', 'NMISS', 'BETA', 'P'] # Column names of the output file (same as plink)
        joined_column_names = "\t".join(column_names) + "\n"      # Align all the column names
        writer.write(joined_column_names)
        
        logging.info("Parsing through variants")

        num_variants = 0
        for variant in VCF("intermediate.vcf"):
            num_variants +=1
        
        genotype_df = get_genotypes()

        # pca = sklearn.decomposition.PCA(n_components=3)
        # pca.fit(genotype_df)
        # print(pca.explained_variance_)
        # print(pca.components_)

        for variant in VCF("intermediate.vcf"):
            output_info = []
            genotype_array = genotype_df.loc[variant.ID].values

            # Failed attempt to add covariates
            # pca_array = py.empty(shape=(3+1, num_genotypes))
            # pca_array[0] = genotype_array
            # for i in range(0, len(pca.components_)):
            #     pca_array[i+1] = pca.components_[i]
            # pca_array = py.swapaxes(pca_array, 0, 1)
            # pca_array_expanded = sm.add_constant(pca_array)
            # model_pca = sm.OLS(pca_array, phenotype_array)
            # res2 = model_pca.fit()

            # model = sm.OLS(genotype_array, phenotype_array)
            # res = model.fit()

            reg = scipy.stats.linregress(genotype_array, phenotype_array)
            #t_value = reg.slope / reg.stderr

            # All information that is outputted
            output_info.append(str(variant.CHROM))          # Chromosome number
            output_info.append(str(variant.ID))             # SNP identifier
            output_info.append(str(variant.POS))            # Base pair coordinate
            output_info.append(str(num_variants)) # Number of observations
            output_info.append(str(reg.slope / reg.stderr))             # Regression coefficient
            output_info.append(str(reg.pvalue))             # Asymptotic p-value for a two-sided t-test
            curr_output = "\t".join(output_info) + "\n"
            writer.write(curr_output)

def get_genotypes():
    genotypes = []
    snps = []
    samples = VCF("intermediate.vcf").samples
    for variant in VCF("intermediate.vcf"):
        genotype_array = []
        for genotype in variant.genotypes:
            # quantifies genotype
            # 0 | 0 becomes 0
            # 1 | 0 or 0 | 1 becomes 1
            # 1 | 1 becomes 2
            genotype_array.append(genotype[0] + genotype[1])
            
        genotypes.append(genotype_array)
        snps.append(variant.ID)

    genotype_df = pd.DataFrame(genotypes, index=snps)
    genotype_df.columns = samples
    genotype_df = genotype_df.reindex(sorted(samples), axis=1)

    return genotype_df

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