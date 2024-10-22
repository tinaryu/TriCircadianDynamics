import pandas as pd

# Load the count table
count_table_path = 'total_count_table_intersect.txt'
count_df = pd.read_csv(count_table_path, sep='\t', index_col='gene')

# Print column names for diagnostics
print("Columns in count table:", count_df.columns.tolist())

# Mapped read counts for each BAM file with corrected keys if necessary

mapped_reads = {
    'read_counts_per_gene_CV-H3K9ac_1.txt': 31868965,
    'read_counts_per_gene_CV-H3K9ac_2.txt': 27094693,
    'read_counts_per_gene_CV-H3K9ac_3.txt': 43558764,
    'read_counts_per_gene_CV-H3K9ac_4.txt': 17689102,
    'read_counts_per_gene_CV-H3K9ac_5.txt': 12941845,
    'read_counts_per_gene_CV-H3K9ac_6.txt': 11526573,
    'read_counts_per_gene_GF-H3K9ac_1.txt': 23181470,
    'read_counts_per_gene_GF-H3K9ac_2.txt': 32969015,
    'read_counts_per_gene_GF-H3K9ac_3.txt': 26425333,
    'read_counts_per_gene_GF-H3K9ac_4.txt': 25698509,
}

# mapped_reads = {

#     'merged_CV-H3K9ac_1.sort.bam': 31868965,
#     'merged_CV-H3K9ac_2.sort.bam': 27094693,
#     'merged_CV-H3K9ac_3.sort.bam': 43558764,
#     'merged_CV-H3K9ac_4.sort.bam': 17689102,
#     'merged_CV-H3K9ac_5.sort.bam': 12941845,
#     'merged_CV-H3K9ac_6.sort.bam': 11526573,
#     'GF-H3K9ac_1.sort.bam': 23181470,
#     'GF-H3K9ac_2.sort.bam': 32969015,
#     'GF-H3K9ac_3.sort.bam': 26425333,
#     'GF-H3K9ac_4.sort.bam': 25698509,
# }

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
normalized_output_path = 'normalized_total_count_table_intersect.txt'
normalized_df.to_csv(normalized_output_path, sep='\t')

