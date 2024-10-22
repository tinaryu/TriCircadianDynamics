import pysam
import gffutils

gtf_file = 'genes.gtf'
bam_files = [
    'CV-H3K9ac_1.sort.bam', 'CV-H3K9ac_2.sort.bam', 'CV-H3K9ac_3.sort.bam', 'CV-H3K9ac_4.sort.bam', 'CV-H3K9ac_5.sort.bam', 'CV-H3K9ac_6.sort.bam', 'GF-H3K9ac_1.sort.bam', 'GF-H3K9ac_2.sort.bam', 'GF-H3K9ac_3.sort.bam', 'GF-H3K9ac_4.sort.bam'
]
output_file_path = 'count_table_3.txt'

def get_tss_positions(gtf_file):
    db = gffutils.create_db(gtf_file, dbfn=':memory:', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
    tss_positions = {}
    for gene in db.features_of_type('gene'):
        exons = list(db.children(gene, featuretype='exon', order_by='start'))
        if not exons:
            continue
        chromosome = gene.seqid
        tss = exons[0].start if gene.strand == '+' else exons[-1].end
        gene_id = gene.attributes['gene_id'][0]
        tss_positions[(chromosome, gene_id)] = tss
    return tss_positions

def check_bam_headers(bam_files):
    for bam_file in bam_files:
        samfile = pysam.AlignmentFile(bam_file, "rb")
        print(f"Header for {bam_file}:")
        for ref in samfile.header.references:
            print(f"{ref} with length {samfile.header.get_reference_length(ref)}")
        samfile.close()

def count_reads_around_tss(bam_file, tss_positions):
    samfile = pysam.AlignmentFile(bam_file, "rb")
    counts = {}
    for (chrom, gene_id), tss in tss_positions.items():
        key = (chrom, gene_id)
        start = max(0, tss - 2000)
        end = tss + 2000
        counts[key] = 0
        print(f"Processing {chrom}:{start}-{end} for {gene_id} in {bam_file}")
        try:
            for pileupcolumn in samfile.pileup(region=f"{chrom}:{start}-{end}"):
                counts[key] += pileupcolumn.n
        except ValueError as e:
            print(f"Error processing region {chrom}:{start}-{end} for {gene_id} in {bam_file}: {e}")
    samfile.close()
    return counts

# Check BAM file headers to understand the chromosome naming and sizes
check_bam_headers(bam_files)

tss_positions = get_tss_positions(gtf_file)
all_counts = {}
for bam_file in bam_files:
    counts = count_reads_around_tss(bam_file, tss_positions)
    for key in counts:
        if key in all_counts:
            all_counts[key].append(counts[key])
        else:
            all_counts[key] = [counts[key]]

with open(output_file_path, 'w') as output_file:
    header = "Gene ID\t" + "\t".join(bam_files) + "\n"
    output_file.write(header)
    for (chrom, gene_id), counts in all_counts.items():
        line = f'{gene_id}\t' + "\t".join(map(str, counts)) + '\n'
        output_file.write(line)

