import pandas as pd

gene = ["hdac3", "nfil3", "nr1d1"]

for g in gene:
    difference_df = pd.read_csv(g+"_difference_modify_div.txt", sep='\t')
    dependent_df = difference_df[(difference_df['meta2d_rAMP_diff'] > 1.5) | (difference_df['meta2d_phase_diff'] > 3)]

    print(len(dependent_df))

    dependent_df.to_csv(g+"_dependent_modify_div_1.5_3.txt", sep='\t', index=False)


#nr1d1 there is no gene filtered out by rAMP diff > 2


