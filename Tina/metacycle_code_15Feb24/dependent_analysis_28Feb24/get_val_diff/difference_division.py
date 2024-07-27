import pandas as pd

gene = ["hdac3", "nfil3", "nr1d1"]

for g in gene:
    wt_df = pd.read_csv("wtonly_meta2d_"+g+"_WT.txt", sep='\t')
    ko_df = pd.read_csv("wtonly_meta2d_"+g+"_KO.txt", sep='\t')


    if not wt_df['CycID'].equals(ko_df['CycID']):
        raise ValueError("CycID columns do not match")


    difference_df = pd.DataFrame()
    difference_df['CycID'] = wt_df['CycID']
    difference_df['meta2d_phase_diff'] = (wt_df['meta2d_phase'] - ko_df['meta2d_phase']).abs()
    difference_df['meta2d_rAMP_diff'] = (wt_df['meta2d_rAMP'] / ko_df['meta2d_rAMP']).abs()
    difference_df['meta2d_rAMP_diff_sub'] = (wt_df['meta2d_rAMP'] - ko_df['meta2d_rAMP'])


    difference_df.to_csv(g+"_difference_div_sub2.txt", sep='\t', index=False)

