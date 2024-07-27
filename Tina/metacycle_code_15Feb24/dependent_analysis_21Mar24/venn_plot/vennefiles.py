import matplotlib.pyplot as plt

from matplotlib_venn import venn3,venn2
from itertools import chain

par = "2_0.2"
# Read the gene lists from the files
with open(par+'/nr1d1_dep_geneID.txt', 'r') as f:
    g1 = set(f.readlines())
with open(par+'/hdac3_dep_geneID.txt', 'r') as f:
    g2 = set(f.readlines())
with open(par+'/nfil3_dep_geneID.txt', 'r') as f:
    g3 = set(f.readlines())

# Create a Venn diagram
venn3([g1, g2, g3], set_labels=('nr1d1 dependent', 'hdac3 dependent', 'nfil3 dependent'))
plt.title(par+" dependent genes overlap")
plt.savefig(par+"/"+par+"_dependent.pdf", format='pdf')
plt.show()






