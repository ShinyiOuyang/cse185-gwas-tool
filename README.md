# ourGWAS (CSE185 Group 40)
ourGWAS is an open-source tool created to do genome wide association studies using a linear regression model. The tool is able to identify single nucleotide polymorphisms based on phenotype and vcf input data, similar to the tool [plink](https://zzz.bwh.harvard.edu/plink/) which was developed by Shaun Purcell.

# Install Instructions
Installation of our tool requires the [sklearn](https://scikit-learn.org/stable/), [qqman](https://pypi.org/project/qqman/), [numpy](https://numpy.org/), and [pandas](https://pandas.pydata.org/) libraries to be installed. You can install these libraries using pip.
```
pip install -U scikit-learn qqman numpy pandas
```
To see if the download was successful, run `python -m pip freeze` to see all packages downloaded on your virtual environment.

Additionally, the [htslib](https://github.com/samtools/htslib/releases/download/1.17/htslib-1.17.tar.bz2) library will be needed to index vcf files using `tabix`. In order to download, click the link above and follow the commands below.
```
cd htslib-1.x      # wherever it is downloaded
./configure
make
make install
```
If permission is needed in order to run `make install`, do `sudo make install` and enter the password to your user.

To check if the download was successful, running `tabix --help` should provide the usage.
# Basic Usage

# ourGWAS options

# Output

# Contributers
This repository was created by Riya Kalra, Shinyi Ouyang, and Tyler Yang with inpsiration from [plink](https://zzz.bwh.harvard.edu/plink/). 