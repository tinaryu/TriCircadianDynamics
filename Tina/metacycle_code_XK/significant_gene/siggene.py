import pandas as pd

data = pd.read_csv("JTK.KO_Hdac3.txt", sep="\t")


significant_genes = data[data['ADJ.P'] < 0.05]


gene_ids = significant_genes['Geneid']


gene_ids.to_csv("significant_gene_ids.txt", index=False)

