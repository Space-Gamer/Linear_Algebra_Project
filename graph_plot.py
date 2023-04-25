import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(adj_mat, labels=None):
    g = nx.convert_matrix.from_numpy_array(np.array(adj_mat), parallel_edges=True)
    if labels is not None:
        g = nx.relabel.relabel_nodes(g, {i: labels[i] for i in range(len(labels))})
    nx.draw(g, with_labels=True)
    plt.show()

