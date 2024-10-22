import pandas as pd

# Load the normalized data
input_file = 'normalized_merged_gene_read_counts.txt'
df = pd.read_csv(input_file, sep='\t', index_col='Gene')

# Drop rows where all values are 0
df_cleaned = df.loc[~(df == 0).all(axis=1)]

# Save the cleaned DataFrame to a new file
output_file = 'cleaned_normalized_merged_gene_read_counts.txt'
df_cleaned.to_csv(output_file, sep='\t')

print(f'Cleaned data saved to: {output_file}')

