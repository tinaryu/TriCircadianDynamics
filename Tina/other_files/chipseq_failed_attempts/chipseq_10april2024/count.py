import pysam
import gffutils


gtf_file = 'genes.gtf'
bam_files = [
    'CV-H3K9ac_1.sort.bam',
    'CV-H3K9ac_2.sort.bam',
    'CV-H3K9ac_3.sort.bam',
    'CV-H3K9ac_4.sort.bam',
    'CV-H3K9ac_5.sort.bam',
    'CV-H3K9ac_6.sort.bam',
    'GF-H3K9ac_1.sort.bam',
    'GF-H3K9ac_2.sort.bam',
    'GF-H3K9ac_3.sort.bam',
    'GF-H3K9ac_4.sort.bam'
]
output_file_path = 'count_table_new.txt'

# get TSS positions
def get_tss_positions(gtf_file):
    db = gffutils.create_db(gtf_file, dbfn=':memory:', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
    tss_positions = {}
    for gene in db.features_of_type('gene'):
        # 初始化该基因的exon列表
        exons = list(db.children(gene, featuretype='exon', order_by='start'))
        if not exons:  # 如果没有exon，跳过这个基因
            continue
        if gene.strand == '+':
            tss_positions[gene.attributes['gene_id'][0]] = exons[0].start
        else:
            tss_positions[gene.attributes['gene_id'][0]] = exons[-1].end
    return tss_positions

# count reads - 2kb near TSS
def count_reads_around_tss(bam_file, tss_positions):
    samfile = pysam.AlignmentFile(bam_file, "rb")
    counts = {gene_id: 0 for gene_id in tss_positions}
    for gene_id, position in tss_positions.items():
        start = max(0, position - 2000)
        end = position + 2000
        for pileupcolumn in samfile.pileup(region="chr1", start=start, end=end):
            counts[gene_id] += pileupcolumn.n
    samfile.close()
    return counts


tss_positions = get_tss_positions(gtf_file)
all_counts = {}
for bam_file in bam_files:
    all_counts[bam_file] = count_reads_around_tss(bam_file, tss_positions)

# save
with open(output_file_path, 'w') as output_file:
    header = "Gene ID\t" + "\t".join(bam_files) + "\n"
    output_file.write(header)
    for gene_id in tss_positions.keys():
        line = f'{gene_id}'
        for bam_file in bam_files:
            line += f'\t{all_counts[bam_file][gene_id]}'
        line += '\n'
        output_file.write(line)

