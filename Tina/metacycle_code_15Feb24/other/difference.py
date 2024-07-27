import pandas as pd


wt_df = pd.read_csv("wtonly_meta2d_nr1d1_WT.txt", sep='\t')
ko_df = pd.read_csv("wtonly_meta2d_nr1d1_KO.txt", sep='\t')


if not wt_df['CycID'].equals(ko_df['CycID']):
    raise ValueError("CycID columns do not match")


difference_df = pd.DataFrame()
difference_df['CycID'] = wt_df['CycID']
difference_df['meta2d_phase_diff'] = (wt_df['meta2d_phase'] - ko_df['meta2d_phase']).abs()
difference_df['meta2d_rAMP_diff'] = (wt_df['meta2d_rAMP'] - ko_df['meta2d_rAMP']).abs()


difference_df.to_csv("nr1d1_difference.txt", sep='\t', index=False)

