import pysam
import gffutils


gtf_file = 'genes.gtf'  
bam_files = [
    'CV-H3K9ac_F1.sort.bam',
    'CV-H3K9ac_F2.sort.bam',
    'CV-H3K9ac_F4.sort.bam',
    'CV-H3K9ac_F5.sort.bam',
    'CV-H3K9ac_F6.sort.bam',
    'GF-H3K9ac_1.sort.bam',
    'GF-H3K9ac_2.sort.bam',
    'GF-H3K9ac_3.sort.bam',
    'GF-H3K9ac_4.sort.bam'
]
output_file_path = 'count_table_updated.txt'


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


def count_reads_around_tss(bam_file, tss_positions):
    samfile = pysam.AlignmentFile(bam_file, "rb")
    counts = {}
    for (chrom, gene_id), tss in tss_positions.items():
        key = (chrom, gene_id)
        start = max(0, tss - 2000)
        end = tss + 2000
        counts[key] = 0
        try:
            for pileupcolumn in samfile.pileup(region=f"{chrom}:{start}-{end}"):
                counts[key] += pileupcolumn.n
        except ValueError as e:
            print(f"Error processing region {chrom}:{start}-{end} for {gene_id} in {bam_file}: {e}")
    samfile.close()
    return counts


tss_positions = get_tss_positions(gtf_file)
all_counts = {}
for bam_file in bam_files:
    counts = count_reads_around_tss(bam_file, tss_positions)
    for key in counts:
        all_counts[key] = counts[key]


with open(output_file_path, 'w') as output_file:
    header = "Gene ID\t" + "\t".join(bam_files) + "\n"
    output_file.write(header)
    for (chrom, gene_id), count in all_counts.items():
        line = f'{gene_id}\t{count}\n'
        output_file.write(line)

