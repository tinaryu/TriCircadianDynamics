
#choose genes from the wtonly.txt apply to all meta2d files
file_names = ['meta2d_GF.txt','meta2d_hdac3_WT.txt','meta2d_hdac3_KO.txt','meta2d_nfil3_WT.txt','meta2d_nfil3_KO.txt','meta2d_nr1d1_WT.txt','meta2d_nr1d1_KO.txt']

with open('choose_input/WT_only.txt', 'r') as f:
    cycling_genes = [line.strip() for line in f.readlines()] #all the WT only cycling genes

for file in file_names:
    selected_rows = []

    with open('choose_input/'+file, 'r') as f:
        #first attach header to the file (selected rows)
        header = f.readline().strip()  
        selected_rows.append(header)
        
        for line in f:
            gene = line.split('\t')[0]  # get the gene name for each line
            if gene in cycling_genes: # if the gene is in the WT only cycling genes, add it to the selected rows
                selected_rows.append(line.strip()) #add line to selected rows


    with open('wtonly_meta2d/wtonly_' + file, 'w') as f:
        for row in selected_rows:
            f.write(row + '\n')

