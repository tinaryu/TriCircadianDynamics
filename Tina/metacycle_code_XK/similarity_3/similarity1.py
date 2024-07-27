import pandas as pd


def read_distances(file_name):
    distances = []
    with open(file_name, 'r') as f:
        for line in f:
            parts = line.strip().split(': ')
            gene_pair = tuple(parts[0].split(' - '))
            distance = float(parts[1])
            distances.append(gene_pair + (distance,))
    return pd.DataFrame(distances, columns=['Gene1', 'Gene2', 'Distance'])


df_hdac3 = read_distances('distances_normalized_hdac3_difference.txt')
df_nr1d1 = read_distances('distances_normalized_nr1d1_difference.txt')
df_nfil3 = read_distances('distances_normalized_nfil3_difference.txt')


df_combined = pd.merge(df_hdac3, df_nr1d1, on=['Gene1', 'Gene2'], how='outer', suffixes=('_hdac3', '_nr1d1'))
df_combined = pd.merge(df_combined, df_nfil3, on=['Gene1', 'Gene2'], how='outer')
df_combined.rename(columns={'Distance': 'Distance_nfil3'}, inplace=True)


similarity_threshold = 0.05  
similar_pairs = df_combined[
    (abs(df_combined['Distance_hdac3'] - df_combined['Distance_nr1d1']) < similarity_threshold) &
    (abs(df_combined['Distance_hdac3'] - df_combined['Distance_nfil3']) < similarity_threshold) &
    (abs(df_combined['Distance_nr1d1'] - df_combined['Distance_nfil3']) < similarity_threshold)
]

output_csv_path = 'similar_gene_pairs.csv'
similar_pairs.to_csv(output_csv_path, index=False)


