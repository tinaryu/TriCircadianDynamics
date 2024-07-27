import pysam
import gffutils
import pandas as pd
import os

# 文件路径
gtf_file = 'genes.gtf'
f3_file = 'CV-H3K9ac_F3.txt'
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

# 解析 GTF 文件以获取 TSS 位置
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

# 解析 F3 文件位置
def parse_f3_positions(file_path):
    positions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            positions.append((parts[0], int(parts[1])))
    return positions

# 计算 TSS 附近的 reads 计数
def count_reads_around_tss(bam_file, tss_positions, window=2000):
    samfile = pysam.AlignmentFile(bam_file, "rb")
    counts = {}
    for (chrom, gene_id), tss in tss_positions.items():
        start = max(1, tss - window)  # 避免负坐标
        end = tss + window
        region = f"{chrom}:{start}-{end}"
        counts[gene_id] = 0
        try:
            for pileupcolumn in samfile.pileup(region=region):
                counts[gene_id] += pileupcolumn.n
        except ValueError as e:
            print(f"Error processing region {region} for {gene_id} in {bam_file}: {e}")
    samfile.close()
    return counts

# 加载或初始化 DataFrame
if os.path.exists(output_file_path) and os.path.getsize(output_file_path) > 0:
    df = pd.read_csv(output_file_path, sep='\t', index_col='Gene ID')
else:
    df = pd.DataFrame(index=[gene_id for _, gene_id in get_tss_positions(gtf_file).items()])
    for bam_file in bam_files:
        df[bam_file] = 0

# 更新 DataFrame 数据
for bam_file in bam_files:
    bam_counts = count_reads_around_tss(bam_file, get_tss_positions(gtf_file))
    for gene_id, count in bam_counts.items():
        if gene_id in df.index:
            df.loc[gene_id, bam_file] = count

# 处理 F3 文件数据
f3_positions = parse_f3_positions(f3_file)
f3_counts = {gene_id: 0 for gene_id in df.index}
for (chrom, pos) in f3_positions:
    tss_positions = get_tss_positions(gtf_file)
    for (tss_chrom, gene_id), tss in tss_positions.items():
        if chrom == tss_chrom and abs(tss - pos) <= 2000:
            if gene_id in f3_counts:
                f3_counts[gene_id] += 1
df['F3_counts'] = pd.Series(f3_counts).fillna(0).astype(int)

# 保存 DataFrame 到文件
df.to_csv(output_file_path, sep='\t', index_label='Gene ID')

# 打印头部数据以确认
print(df.head())

