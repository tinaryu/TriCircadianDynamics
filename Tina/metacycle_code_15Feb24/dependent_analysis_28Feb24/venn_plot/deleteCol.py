import pandas as pd


parameters = "2_6_0.2B"

filepath = '../choose_dependent/dep_'+parameters+'/'
gene = ["hdac3", "nfil3", "nr1d1"]

for g in gene:
    df = pd.read_csv(filepath+g+"_dep.txt", sep='\t')
    df = df.drop(columns=['meta2d_rAMP_diff','meta2d_phase_diff','meta2d_rAMP_diff_sub'])
    df.to_csv(parameters+"/"+g+"_dep_geneID.txt", sep='\t', index=False)