import pandas as pd

filepath = '/Users/tinaryu/Documents/KuangLab/metacycle_code/other/'
gene = ["hdac3", "nfil3", "nr1d1"]

parameters = "1.5_3"

for g in gene:
    df = pd.read_csv(filepath+g+"_dependent_modify_div_"+parameters+".txt", sep='\t')
    df = df.drop(columns=['meta2d_rAMP_diff','meta2d_phase_diff'])
    df.to_csv(g+"_dependent_modify_div_"+parameters+".txt", sep='\t', index=False)
