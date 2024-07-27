import pandas as pd
import matplotlib.pyplot as plt

difference_df = pd.read_csv("nfil3_difference_modify.txt", sep='\t')
dependent_df = pd.read_csv("nfil3_dependent_modify_adjusted.txt", sep='\t')


total_genes = len(difference_df)
dependent_genes = len(dependent_df)
non_dependent_genes = total_genes - dependent_genes


sizes = [dependent_genes, non_dependent_genes]
labels = ['Dependent Genes', 'Other Genes']
colors = ['#ff9999','#66b3ff']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

ax1.axis('equal')  
plt.title('nfil3 Dependent Ratio')
plt.savefig("nfil3_pie_modify.pdf")

plt.show()

