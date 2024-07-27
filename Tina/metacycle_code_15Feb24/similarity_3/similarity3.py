import networkx as nx
import pandas as pd

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


df_hdac3 = read_distances('distances_normalized_hdac3_difference.txt')
df_nr1d1 = read_distances('distances_normalized_nr1d1_difference.txt')
df_nfil3 = read_distances('distances_normalized_nfil3_difference.txt')


G = nx.Graph()

def add_edges_from_df(df, graph):
    for index, row in df.iterrows():
        graph.add_edge(row['Gene1'], row['Gene2'], weight=row['Distance'])

add_edges_from_df(df_hdac3, G)
add_edges_from_df(df_nr1d1, G)
add_edges_from_df(df_nfil3, G)


nx.write_graphml(G, "gene_network.graphml")

print("Network has been saved to gene_network.graphml")

