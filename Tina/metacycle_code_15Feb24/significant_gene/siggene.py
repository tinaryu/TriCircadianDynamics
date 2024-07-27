import pandas as pd

filename = "nr1d1_KO.txt"

data = pd.read_csv("meta2d_results/meta2d_"+filename, sep="\t")


significant_genes = data[data['meta2d_pvalue'] < 0.05]


gene_ids = significant_genes['CycID']


gene_ids.to_csv("significant_gene_ids_"+filename, index=False)
