import pandas as pd
import networkx as nx



def get_graph(path_to_data_dir='./regions_and_cities', kind='relative_travel'):
    """
    kind: {relative_travel, absolute_travel, distance}
    """
    if kind=='relative_travel':
        matx = pd.read_csv('./regions_and_cities/relative_travel_matrix.csv', index_col=0)
        g = nx.from_pandas_adjacency(matx, create_using=nx.DiGraph)
    elif kind=='absolute_travel':
        matx = pd.read_csv('./regions_and_cities/absolute_travel_matrix.csv', index_col=0)
        g = nx.from_pandas_adjacency(matx, create_using=nx.DiGraph)
    elif kind=='distance':
        matx = pd.read_csv('./regions_and_cities/raw_distances_matrix.csv', index_col=0)
        g = nx.from_pandas_adjacency(matx, create_using=nx.Graph)
    return g
