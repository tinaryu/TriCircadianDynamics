import pandas as pd

# The path to your input file
input_files = ['chr1-Y_CV-H3K9ac_1.sort.bam_tss_counts.txt',"chr1-Y_CV-H3K9ac_2.sort.bam_tss_counts.txt","chr1-Y_CV-H3K9ac_3.sort.bam_tss_counts.txt","chr1-Y_CV-H3K9ac_4.sort.bam_tss_counts.txt","chr1-Y_CV-H3K9ac_5.sort.bam_tss_counts.txt","chr1-Y_CV-H3K9ac_6.sort.bam_tss_counts.txt","chr1-Y_GF-H3K9ac_1.sort.bam_tss_counts.txt","chr1-Y_GF-H3K9ac_2.sort.bam_tss_counts.txt","chr1-Y_GF-H3K9ac_3.sort.bam_tss_counts.txt","chr1-Y_GF-H3K9ac_4.sort.bam_tss_counts.txt"]

input_file = 'chr1-Y_CV-H3K9ac_1.sort.bam_tss_counts.txt'
# The path to your output file
output_file = 'summed_gene_read_count_chr1-Y_CV-H3K9ac_1.txt'

# Read the file. Assuming that the file is space-separated and contains three columns: gene name, an unused number, and the read count.
df = pd.read_csv(input_file, sep=' ', header=None, usecols=[1,3 ], names=['ReadCount', 'Gene'])

# Sum the read counts for each gene
summed_df = df.groupby('Gene')['ReadCount'].sum().reset_index()

# Save the summed counts to a new file
summed_df.to_csv(output_file, sep='\t', index=False)

print(f'Summed read counts saved to: {output_file}')

