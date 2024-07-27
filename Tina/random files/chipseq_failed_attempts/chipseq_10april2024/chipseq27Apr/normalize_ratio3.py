import pandas as pd

# Load the count table
count_table_path = 'final_counts_matrix.csv'
count_df = pd.read_csv(count_table_path, sep=',', index_col='GeneName')

# Print column names for diagnostics
print("Columns in count table:", count_df.columns.tolist())

# Mapped read counts for each BAM file with corrected keys if necessary

mapped_reads = {
    'merged_CV-H3K9ac_1': 31868965,
    'merged_CV-H3K9ac_2': 27094693,
    'merged_CV-H3K9ac_3': 43558764,
    'merged_CV-H3K9ac_4': 17689102,
    'merged_CV-H3K9ac_5': 12941845,
    'merged_CV-H3K9ac_6': 11526573,
    'GF-H3K9ac_1' : 23181470,
    'GF-H3K9ac_2': 32969015,
    'GF-H3K9ac_3': 26425333,
    'GF-H3K9ac_4': 25698509,
}
# Print BAM files in the dictionary for diagnostics
print("BAM files in mapped reads dictionary:", mapped_reads.keys())

# Find the smallest mapped read count
min_mapped_reads = min(mapped_reads.values())

# Calculate normalization factors for each file
normalization_factors = {bam_file: min_mapped_reads / mapped_reads_count for bam_file, mapped_reads_count in mapped_reads.items()}

# Apply normalization factors
normalized_df = count_df.copy()
for bam_file in count_df.columns:
    try:
        normalized_df[bam_file] = normalized_df[bam_file] * normalization_factors[bam_file]
    except KeyError as e:
        print(f"KeyError encountered for: {bam_file}. This file may not exist in the 'mapped_reads' dictionary.")

# Save the normalized count table
normalized_output_path = 'normalized_final_counts_matrix.txt'
normalized_df.to_csv(normalized_output_path, sep='\t')

