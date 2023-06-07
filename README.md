# ourgwas (CSE185 Group 40)
ourgwas is an open-source tool created to do genome wide association studies using a linear regression model. The tool is able to identify single nucleotide polymorphisms based on phenotype and vcf input data, similar to the tool [plink](https://zzz.bwh.harvard.edu/plink/) which was developed by Shaun Purcell.

# Install Instructions

***NOTE***: As this is a rudimentary tool created quickly to do gwas, we do NOT recommend installation on a Windows device as this seems to cause multiple extra steps in installation. If you are on a Windows device, we recommend installing on JupyterHub at [Datahub](https://datahub.ucsd.edu/hub/spawn)

Installation of our tool requires the [sklearn](https://scikit-learn.org/stable/), [qqman](https://pypi.org/project/qqman/), [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), and [cyvcf2](https://brentp.github.io/cyvcf2/) libraries to be installed. You can install these libraries using pip:
```
pip install -U scikit-learn qqman numpy pandas cyvcf2
```

***Note***: if you do not have root access, install the same packages locally with:

```
pip install --user -U scikit-learn qqman numpy pandas cyvcf2
```

Additionally, the [bcftools](http://www.htslib.org/download/) library will be needed to index vcf files using and filter variants. In order to download, click the link above to download bcftools as a `.tar.bz2` zip file. To uncompress this file, either double click the file in your file explorer or use the `tar` command:
```
tar -xvzf bcftools-1.x.tar.bz2`
```
Afterwards, follow the command below:
```
cd bcftools-1.x      # wherever it is downloaded
./configure          # NOTE: Windows users may need to install other programs such as GCC and/or zlib
make
make install
```
If permission is needed in order to run `make install`, do `sudo make install` and enter the password to your user.

To check if the download was successful, running `bcftools --help` should provide the usage.

Once these required libraries are installed, you can install `ourgwas` with the following command:
```
python setup.py install  # add the --user tag if needed

# if installing on Jupyter Notebook, instead run

python setup.py install --prefix=$HOME
```

If successful, running `ourgwas --help` should output the usage. 

# Basic Usage

The basic usage of `ourgwas` is:
```
ourGWAS [other options] pheno-file vcf-file
```

NOTE: If you are using VSCode or other virutal environments, please check to make sure the python version is matched with the version on your computer. Otherwise, some packages may not load correctly.

To run `ourgwas` on some of the small test files in our repo, you can run:
```
ourgwas ./example-files/lab3_gwas.phen ./example-files/lab3_gwas_small.vcf.gz
```
This should output [this text file](https://github.com/ShinyiOuyang/cse185-gwas-tool/blob/main/ourgwas.out.txt).

<!--insert the output of the test files here-->

# ourgwas options

The input required with our tool is a sorted and indexed vcf file and a phenotype file with normalized data for the samples on the specific phenotype being viewed.

Users may also specify additional options below:
```
--output FILE: specifies output root file name, by default, the file will be called ourGWAS.

--maf FLOAT: a decimal number from 0-1 which specifies the minimum minor allele frequency threshold to be considered. By default, this value is 0.01.

--pca INT: specifies the number of principle components (PCs) to use as covariates. By default, this number is 0.

--qq: outputs a qq plot along with the regular output.
```

# Output
The output file format is a text file similar to the one output by [plink's --linear option](https://www.cog-genomics.org/plink/1.9/formats#assoc_linear).

# Contributers
This repository was created by Riya Kalra, Shinyi Ouyang, and Tyler Yang with inspiration from [plink](https://zzz.bwh.harvard.edu/plink/). 
