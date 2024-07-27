import pandas as pd

def compute_fpkm(file_name):

    counts = pd.read_csv(file_name + '_counts.txt', sep='\t', skiprows=1, index_col=0)

   
    gene_lengths = counts['Length']
    gene_counts = counts[file_name + '_sorted.bam']

   
    counts['RPK'] = gene_counts / gene_lengths * 1e3

    counts['FPKM'] = counts['RPK'] / counts['RPK'].sum() * 1e6


    counts[['FPKM']].to_csv(file_name + '_new_fpkm.txt', sep='\t')


compute_fpkm('GFRNA1')
compute_fpkm('GFRNA2')
compute_fpkm('GFRNA3')
compute_fpkm('GFRNA4')
