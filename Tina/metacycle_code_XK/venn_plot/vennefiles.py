import matplotlib.pyplot as plt
from matplotlib_venn import venn3,venn2
from itertools import chain

parameters = "1.5_3"

# Read the gene lists from the files
with open('nr1d1_dependent_modify_div_'+parameters+'.txt', 'r') as f:
    g1 = set(f.readlines())

with open('hdac3_dependent_modify_div_'+parameters+'.txt', 'r') as f:
    g2 = set(f.readlines())
with open('nfil3_dependent_modify_div_'+parameters+'.txt', 'r') as f:
    g3 = set(f.readlines())

# Create a Venn diagram
venn3([g1, g2, g3], set_labels=('nr1d1_dependent', 'hdac3_dependent', 'nfil3_dependent'))
plt.title("rAMP_fold_diff > "+ parameters[:3] +" or phase_diff > " + parameters[4])
plt.savefig("dependent_modify_div_"+parameters+".pdf", format='pdf')
plt.show()


