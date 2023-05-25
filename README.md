# ourGWAS (CSE185 Group 40)
ourGWAS is an open-source tool created to do genome wide association studies using a linear regression model. The tool is able to identify single nucleotide polymorphisms based on phenotype and vcf input data, similar to the tool [plink](https://zzz.bwh.harvard.edu/plink/) which was developed by Shaun Purcell.

# Install Instructions
Installation of our tool requires the [sklearn](https://scikit-learn.org/stable/), [qqman](https://pypi.org/project/qqman/), [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), and [cyvcf2](https://brentp.github.io/cyvcf2/) libraries to be installed. You can install these libraries using pip:
```
pip install -U scikit-learn qqman numpy pandas cyvcf2
```
To see if the download was successful, run `python -m pip freeze` to see all packages downloaded on your virtual environment.

Note: if you do not have root access, install the same packages locally with:

```
pip install --user -U scikit-learn qqman numpy pandas cyvcf2
```

Additionally, the [htslib](https://github.com/samtools/htslib/releases/download/1.17/htslib-1.17.tar.bz2) library will be needed to index vcf files using `tabix`. In order to download, click the link above and follow the commands below:
```
cd htslib-1.x      # wherever it is downloaded
./configure
make
make install
```
If permission is needed in order to run `make install`, do `sudo make install` and enter the password to your user.

To check if the download was successful, running `tabix --help` should provide the usage.

Once these required libraries are installed, you can install `ourGWAS` with the following command:
```
python setup.py install  # add the --user tag if needed

# if installing on Jupyter Notebook, instead run

python setup.py install --prefix=$HOME
```

If successful, running `ourGWAS --help` should output the usage. 

# Basic Usage

*work in progress*

The basic usage of `ourGWAS` is:
```
ourGWAS [--pheno in.phen] [other options] in.vcf
```

To run `ourGWAS` on some of the small test files in our repo, you can run:
```
ourGWAS --pheno test.pheno --maf 0.05 --ouput out.vcf test.gwas
```
This should output:

<!--insert the output of the test files here-->

# ourGWAS options

The input required with our tool is a sorted and indexed vcf file and a phenotype file with normalized data for the samples on the specific phenotype being viewed.

Users may also specify additional options below:
```
--output FILE: specifies output root file name, by default, the file will be called ourGWAS.

--maf FLOAT: a decimal number from 0-1 which specifies the minimum minor allele frequency threshold to be considered. By default, this value is 0.01.

--pca INT: specifies the number of principle components (PCs) to use as covariates. By default, this number is 0.

--qq: outputs a qq plot along with the regular output.
```

# Output
The output file format is a text file similar to the one outputted by [plink's --linear option](https://www.cog-genomics.org/plink/1.9/formats#assoc_linear).

# Contributers
This repository was created by Riya Kalra, Shinyi Ouyang, and Tyler Yang with inpsiration from [plink](https://zzz.bwh.harvard.edu/plink/). 