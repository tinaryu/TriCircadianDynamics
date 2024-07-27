import pandas as pd
import glob


file_pattern = "summed_gene_read_counts_*.txt"
files = glob.glob(file_pattern)

# initialize empty DataFrame
all_data = pd.DataFrame()


for file in files:
    
    df = pd.read_csv(file, sep='\t')
    
    
    sample_name = file.split('/')[-1].replace('summed_gene_read_counts_', '').replace('.txt', '')
    
    
    df.rename(columns={'ReadCount': sample_name}, inplace=True)
    
    
    if all_data.empty:
        all_data = df
    else:
        all_data = pd.merge(all_data, df, on='Gene', how='outer')


all_data.fillna(0, inplace=True)


output_file = "merged_gene_read_counts.txt"
all_data.to_csv(output_file, sep='\t', index=False)

print(f"Merged data has been saved to {output_file}")

