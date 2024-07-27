import gffutils

# 定义GTF文件路径
gtf_file = 'genes.gtf'

# 解析GTF文件以提取TSS位置
def get_tss_positions(gtf_file):
    db = gffutils.create_db(gtf_file, dbfn=':memory:', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
    tss_positions = {}
    for gene in db.features_of_type('gene'):
        exons = list(db.children(gene, featuretype='exon', order_by='start'))
        if not exons:  # 如果没有exon，跳过这个基因
            continue
        if gene.strand == '+':
            tss_positions[gene.attributes['gene_id'][0]] = exons[0].start
        else:
            tss_positions[gene.attributes['gene_id'][0]] = exons[-1].end
    return tss_positions

# 获取TSS位置
tss_positions = get_tss_positions(gtf_file)

# 将TSS位置保存到文件
tss_output_file = 'tss_positions.txt'
with open(tss_output_file, 'w') as f:
    for gene_id, position in tss_positions.items():
        f.write(f'{gene_id}\t{position}\n')

