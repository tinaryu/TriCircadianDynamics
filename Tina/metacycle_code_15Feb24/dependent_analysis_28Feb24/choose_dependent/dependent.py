import pandas as pd

gene = ["hdac3", "nfil3", "nr1d1"]

for g in gene:
    difference_df = pd.read_csv(g+"_difference_modify_div.txt", sep='\t')
    dependent_df = difference_df[(difference_df['meta2d_rAMP_diff'] > 2) | (difference_df['meta2d_phase_diff'] > 6) | (difference_df['meta2d_rAMP_diff_sub'] > 0.2)]

    print("num genes dependent on",g,len(dependent_df))

    dependent_df.to_csv("dep_2_6_0.2B/"+g+"_dep.txt", sep='\t', index=False)


#nr1d1 there is no gene filtered out by rAMP diff > 2


