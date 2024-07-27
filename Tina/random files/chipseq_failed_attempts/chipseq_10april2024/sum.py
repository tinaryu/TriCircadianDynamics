import pandas as pd

# The path to your input file
input_file = 'gene_read_counts_CV-H3K9ac_6.txt'
# The path to your output file
output_file = 'summed_gene_read_counts_CV-H3K9ac_6.txt'

# Read the file. Assuming that the file is space-separated and contains three columns: gene name, an unused number, and the read count.
df = pd.read_csv(input_file, sep=' ', header=None, usecols=[0,1 ], names=['Gene', 'ReadCount'])

# Sum the read counts for each gene
summed_df = df.groupby('Gene')['ReadCount'].sum().reset_index()

# Save the summed counts to a new file
summed_df.to_csv(output_file, sep='\t', index=False)

print(f'Summed read counts saved to: {output_file}')

