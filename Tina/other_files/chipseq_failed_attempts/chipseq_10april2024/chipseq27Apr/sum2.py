
import csv

gene_count = {}

with open("chr1-Y_CV-H3K9ac_2.sort.bam_tss_counts.txt", "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        gene_name = parts[3]
        read_count = int(parts[6])
        gene_count[gene_name] = gene_count.get(gene_name, 0) + read_count

# Write the gene counts to a CSV file
with open("summed_read_count_chr1-Y_CV-H3K9ac_2.sort.bam_tss_counts.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Gene", "ReadCount"])  # Write header
    for gene, count in gene_count.items():
        writer.writerow([gene, count])