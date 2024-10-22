import os
from collections import defaultdict

# Function to process read_counts_per_gene.txt files and extract counts per gene
def process_gene_counts(file_path):
    gene_counts = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line by whitespace and take the last element as gene name
            gene_name = line.strip().split()[-1]
            # Increment count for the gene
            gene_counts[gene_name] += int(line.strip().split()[0])  # Assuming the count is the first element in the line
    return gene_counts

# Function to write total count table
def write_total_count_table(file_paths, output_file):
    total_counts = defaultdict(dict)

    # Process each read_counts_per_gene.txt file
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        gene_counts = process_gene_counts(file_path)
        total_counts[file_name] = gene_counts

    # Write total count table
    with open(output_file, 'w') as out_file:
        # Write header row
        out_file.write("gene\t" + "\t".join(total_counts.keys()) + "\n")
        all_genes = set()
        for counts in total_counts.values():
            all_genes.update(counts.keys())
        for gene in sorted(all_genes):
            out_file.write(gene + "\t")
            for file_name, counts in total_counts.items():
                out_file.write(str(counts.get(gene, 0)) + "\t")
            out_file.write("\n")

# List of read_counts_per_gene.txt file paths
gene_count_files = ['read_counts_per_gene_CV-H3K9ac_1.txt','read_counts_per_gene_CV-H3K9ac_2.txt','read_counts_per_gene_CV-H3K9ac_3.txt','read_counts_per_gene_CV-H3K9ac_4.txt','read_counts_per_gene_CV-H3K9ac_5.txt','read_counts_per_gene_CV-H3K9ac_6.txt','read_counts_per_gene_GF-H3K9ac_1.txt','read_counts_per_gene_GF-H3K9ac_2.txt','read_counts_per_gene_GF-H3K9ac_3.txt','read_counts_per_gene_GF-H3K9ac_4.txt'] 

# Output file path for total count table
output_file_path = 'total_count_table_intersect.txt'  # Update with your desired output file path

# Generate total count table
write_total_count_table(gene_count_files, output_file_path)