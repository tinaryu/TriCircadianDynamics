
with open('WT_only.txt', 'r') as f:
    ko_genes = [line.strip() for line in f.readlines()]


selected_rows = []

with open('meta2d_nfil3_KO.txt', 'r') as f:
    header = f.readline().strip()  
    selected_rows.append(header)
    
    for line in f:
        gene = line.split('\t')[0]  
        if gene in ko_genes:
            selected_rows.append(line.strip())


with open('wtonly_meta2d_nfil3_KO.txt', 'w') as f:
    for row in selected_rows:
        f.write(row + '\n')

