import itertools

import numpy as np

from graph_plot import draw_graph


def bfs_dist(node, adj_mat, visited, dist):
    visited[node] = True
    queue = [node]
    while queue:
        s = queue.pop(0)
        for i in range(len(adj_mat)):
            if adj_mat[s][i] == 1 and not visited[i]:
                visited[i] = True
                dist[i] = dist[s] + 1
                queue.append(i)


def dist_mat(adj_mat):  # Generates a distance matrix for a graph
    n = len(adj_mat)
    dist = np.zeros((n, n))
    for i in range(n):
        visited = [False] * n
        bfs_dist(i, adj_mat, visited, dist[i])
    return dist


def create_benzene_ring(start_node):
    node_lst = [i for i in range(start_node, start_node + 8)]
    benzene_mat = np.zeros((8, 8))
    for i in range(6):
        benzene_mat[i][(i + 1) % 6] = 1
        benzene_mat[(i + 1) % 6][i] = 1

    # internode 1,2
    benzene_mat[1][6] = 1
    benzene_mat[6][1] = 1
    benzene_mat[2][6] = 1
    benzene_mat[6][2] = 1
    benzene_mat[4][6] = 1
    benzene_mat[6][4] = 1
    benzene_mat[5][6] = 1
    benzene_mat[6][5] = 1

    # internode 2,3
    benzene_mat[2][7] = 1
    benzene_mat[7][2] = 1
    benzene_mat[3][7] = 1
    benzene_mat[7][3] = 1
    benzene_mat[5][7] = 1
    benzene_mat[7][5] = 1
    benzene_mat[0][7] = 1
    benzene_mat[7][0] = 1

    print(dist_mat(benzene_mat).max(axis=None))

    return benzene_mat


def main():
    adj_mat = np.array([])
    for i in range(4):
        if adj_mat.any():
            np.concatenate(adj_mat, create_benzene_ring(i*8))
        else:
            adj_mat = create_benzene_ring(0)
    draw_graph(adj_mat)


if __name__ == '__main__':
    main()
