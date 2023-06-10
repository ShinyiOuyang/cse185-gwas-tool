import pandas as pd
import numpy
from qqman import qqman
import matplotlib.pyplot as plt


data = pd.read_csv("wheat_gwas_covar.assoc.linear", delim_whitespace=True)
fig, (ax0, ax1) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 1]})
fig.set_size_inches((15, 5))
plt.suptitle("Plink with 3 PCs on Wheat Dataset Manhattan Plot and QQ Plot")
qqman.manhattan(data, ax=ax0)
qqman.qqplot(data, ax=ax1)
plt.show()