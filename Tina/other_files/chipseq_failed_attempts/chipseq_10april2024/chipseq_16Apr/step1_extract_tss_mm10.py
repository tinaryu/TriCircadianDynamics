import pandas as pd

# Load GTF file - replace with your actual file path
gtf_df = pd.read_csv('genes.gtf', sep='\t', comment='#', header=None,
                     names=['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute'])

# Filter for transcripts to get 'feature' == 'exons'
tss_df = gtf_df[gtf_df['feature'] == 'exon']
# Function to parse the attributes column and return a dictionary
def parse_attributes(attributes_str):
    # Split the string by semicolon and space, then by space within each pair
    # Assuming that the GTF format is consistent with the gene_name being quoted
    return {attr.strip().split(' ')[0]: attr.strip().split(' ')[1].replace('"', '')
            for attr in attributes_str.strip().split(';') if attr}

# Define a function to extract gene name and TSS based on the strand
def extract_tss_info(row):
    tss_start = row['start'] if row['strand'] == '+' else row['end']
    return pd.Series([tss_start], index=['tss_start'])

#add a column consisting of gene names
def extract_gene_name(row):
    attributes = parse_attributes(row['attribute'])
    gene_name = attributes.get('gene_name', '')
    return pd.Series([gene_name], index=['gene_name'])

#add gene name column
tss_df[['gene_name']] = tss_df.apply(extract_gene_name, axis=1)

print('getting all unique gene names...')
#get all unique gene names
genes = pd.unique(tss_df['gene_name'])
print(len(genes))


#if the strand is -, keep the rightmost exon and if the strand is +, keep the leftmost exon
#drop everything else
def remove_exons(genes, tss_df):
    for gene in genes:
        sub_df = tss_df.loc[tss_df['gene_name']==gene]
        dir = sub_df['strand'].iloc[0]
        for i,row in sub_df.iterrows():
            if i == sub_df.index[0] and dir == '+':
                continue
            if i == sub_df.index[-1] and dir == '-':
                continue
            print(i)
            tss_df = tss_df.drop(i)
    return tss_df


print('now removing exons...')
#remove exons that are not relevant to tss
tss_df = remove_exons(genes,tss_df)

print('now adding tss info...')
#get tss_start position based on strand direction
tss_df['tss_start'] = tss_df.apply(extract_tss_info, axis = 1)

print('now calculating tss regions...')
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
tss_bed.to_csv('tss_regions_mm10.bed', sep='\t', header=False, index=False)