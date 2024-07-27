import pandas as pd


wt_df = pd.read_csv("wtonly_meta2d_nfil3_WT.txt", sep='\t')
ko_df = pd.read_csv("wtonly_meta2d_nfil3_KO.txt", sep='\t')


if not wt_df['CycID'].equals(ko_df['CycID']):
    raise ValueError("CycID columns do not match")


wt_df_p_filtered = wt_df[(wt_df['meta2d_pvalue'] < 0.5)]
ko_df_p_filtered = ko_df[(wt_df['meta2d_pvalue'] < 0.5)]


difference_df = pd.DataFrame()
difference_df['CycID'] = wt_df_p_filtered['CycID']
difference_df['meta2d_phase_diff'] = (wt_df_p_filtered['meta2d_phase'] - ko_df_p_filtered['meta2d_phase']).abs()
difference_df['meta2d_rAMP_diff'] = (wt_df_p_filtered['meta2d_rAMP'] - ko_df_p_filtered['meta2d_rAMP']).abs()


difference_df.to_csv("nfil3_difference_p_filtered.txt", sep='\t', index=False)

