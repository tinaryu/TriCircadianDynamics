
import matplotlib.pyplot as plt
from matplotlib_venn import venn3,venn2
from itertools import chain


# Read the gene lists from the files
with open('conventional_genes.txt', 'r') as f:
    g1 = set(f.readlines())
with open('sig_GF.txt', 'r') as f:
    g2 = set(f.readlines())

# Create a Venn diagram
venn2([g1, g2], set_labels=('CV', ''))
plt.title("CV vs GF")
plt.savefig("CVvsGF.pdf", format='pdf')
plt.show()


