import pandas as pd

# Function to parse the attributes column and return a dictionary
def parse_attributes(attributes_str):
    # Split the string by semicolon and space, then by space within each pair
    # Assuming that the GTF format is consistent with the gene_name being quoted
    return {attr.strip().split(' ')[0]: attr.strip().split(' ')[1].replace('"', '')
            for attr in attributes_str.strip().split(';') if attr}

# Load GTF file - replace with your actual file path
gtf_df = pd.read_csv('mm39.ncbiRefSeq.gtf', sep='\t', comment='#', header=None,
                     names=['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute'])

# Filter for transcripts to get TSS (assuming transcripts give the TSS)
tss_df = gtf_df[gtf_df['feature'] == 'transcript']

# Define a function to extract gene name and TSS based on the strand
def extract_tss_info(row):
    attributes = parse_attributes(row['attribute'])
    gene_name = attributes.get('gene_name', '')
    tss_start = row['start'] if row['strand'] == '+' else row['end']
    return pd.Series([gene_name, tss_start], index=['gene_name', 'tss_start'])

# Apply function to get TSS positions
tss_df[['gene_name', 'tss_start']] = tss_df.apply(extract_tss_info, axis=1)

# Calculate TSS regions (2000 bp upstream and downstream)
tss_df['tss_start'] = tss_df['tss_start'].astype(int)
tss_df['tss_end'] = tss_df['tss_start']
tss_df.loc[tss_df['strand'] == '+', 'tss_start'] = tss_df['tss_start'] - 2000
tss_df.loc[tss_df['strand'] == '-', 'tss_end'] = tss_df['tss_end'] + 2000

# Ensure the start is always less than the end
tss_df['start'] = tss_df[['tss_start', 'tss_end']].min(axis=1)
tss_df['end'] = tss_df[['tss_start', 'tss_end']].max(axis=1)

# Remove potential negative starts
tss_df['start'] = tss_df['start'].clip(lower=0)

# Create BED file format
tss_bed = tss_df[['seqname', 'start', 'end', 'gene_name', 'score', 'strand']]

# Write BED file - replace with your actual file path
tss_bed.to_csv('tss_regions.bed', sep='\t', header=False, index=False)

