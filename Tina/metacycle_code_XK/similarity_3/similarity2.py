def read_distances(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            gene_pair = parts[0].strip()
            distance = float(parts[1].strip())
            gene1, gene2 = gene_pair.split(' - ')
            data.append({'Gene1': gene1, 'Gene2': gene2, 'Distance': distance})
    return pd.DataFrame(data)
import pandas as pd
from scipy import stats


def descriptive_statistics(df):
    return {
        'mean': df['Distance'].mean(),
        'median': df['Distance'].median(),
        'std_dev': df['Distance'].std(),
        'variance': df['Distance'].var()
    }


df_hdac3 = read_distances('distances_normalized_hdac3_difference.txt')
df_nr1d1 = read_distances('distances_normalized_nr1d1_difference.txt')
df_nfil3 = read_distances('distances_normalized_nfil3_difference.txt')


stats_hdac3 = descriptive_statistics(df_hdac3)
stats_nr1d1 = descriptive_statistics(df_nr1d1)
stats_nfil3 = descriptive_statistics(df_nfil3)
anova_data = [df_hdac3['Distance'], df_nr1d1['Distance'], df_nfil3['Distance']]
f_stat, p_value = stats.f_oneway(*anova_data)


results = pd.DataFrame({
    'Dataset': ['HDAC3', 'NR1D1', 'NFIL3'],
    'Mean': [stats_hdac3['mean'], stats_nr1d1['mean'], stats_nfil3['mean']],
    'Median': [stats_hdac3['median'], stats_nr1d1['median'], stats_nfil3['median']],
    'Standard Deviation': [stats_hdac3['std_dev'], stats_nr1d1['std_dev'], stats_nfil3['std_dev']],
    'Variance': [stats_hdac3['variance'], stats_nr1d1['variance'], stats_nfil3['variance']],
    'ANOVA F-Statistic': [f_stat] * 3,
    'ANOVA P-Value': [p_value] * 3
})


results.to_csv('combined_stats_results.csv', index=False)

print('All results have been saved to combined_stats_results.csv')

