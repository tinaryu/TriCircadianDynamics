import matplotlib.pyplot as plt

from matplotlib_venn import venn3,venn2
from itertools import chain


# Read the gene lists from the files
with open('nr1d1_WT_dep_geneID.txt', 'r') as f:
    g1 = set(f.readlines())
with open('nr1d1_KO_dep_geneID.txt', 'r') as f:
    g2 = set(f.readlines())
with open('WT_only.txt', 'r') as f:
    g3 = set(f.readlines())

# Create a Venn diagram
venn3([g1, g3, g2], set_labels=('WT', 'all', 'KO'))
plt.title("nr1d1 WT/KO dep compare")
plt.savefig("nr1d1_dep_compare.pdf", format='pdf')
plt.show()






