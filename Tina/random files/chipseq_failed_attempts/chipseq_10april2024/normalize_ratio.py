import pandas as pd

# Load the count table
count_table_path = 'count_table_new.txt'
count_df = pd.read_csv(count_table_path, sep='\t', index_col='Gene ID')

# Print column names for diagnostics
print("Columns in count table:", count_df.columns.tolist())

# Mapped read counts for each BAM file with corrected keys if necessary
mapped_reads = {
    'CV-H3K9ac_1.sort.bam': 9799442,
    'CV-H3K9ac_2.sort.bam': 7228047,
    'CV-H3K9ac_3.sort.bam': 28301531,
    'CV-H3K9ac_4.sort.bam': 4694190,
    'CV-H3K9ac_5.sort.bam': 3470347,
    'CV-H3K9ac_6.sort.bam': 3412814,
    'GF-H3K9ac_1.sort.bam': 23181470,
    'GF-H3K9ac_2.sort.bam': 32969015,
    'GF-H3K9ac_3.sort.bam': 26425333,
    'GF-H3K9ac_4.sort.bam': 25698509,
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
normalized_output_path = 'normalized_count_table.txt'
normalized_df.to_csv(normalized_output_path, sep='\t')

