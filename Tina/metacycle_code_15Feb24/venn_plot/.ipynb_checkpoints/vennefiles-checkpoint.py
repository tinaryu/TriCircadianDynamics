import matplotlib.pyplot as plt
from matplotlib_venn import venn3,venn2
from itertools import chain

# Read the gene lists from the files
with open('nr1d1_dependent_modify_adjusted.txt', 'r') as f:
    g1 = set(f.readlines())

with open('hdac3_dependent_modify_adjusted.txt', 'r') as f:
    g2 = set(f.readlines())
with open('nfil3_dependent_modify_adjusted.txt', 'r') as f:
    g3 = set(f.readlines())

# Create a Venn diagram
venn3([g1, g2,g3], ('nr1d1_dependent', 'hdac3_dependent','nfil3_dependent'))
plt.savefig("dependent_modify.pdf", format='pdf')
plt.show()

