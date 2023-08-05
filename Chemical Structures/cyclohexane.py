import itertools
import sys

import numpy as np

sys.path.append('../Linear_Algebra_Project')

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


def concat_graphs(adj_mat1, adj_mat2):
    # print(adj_mat1.shape) # (8, 8)
    # print(adj_mat2.shape) # (8, 8)

    # Change shape
    adj_mat1 = np.concatenate((adj_mat1, np.zeros((adj_mat1.shape[0], adj_mat2.shape[1]))), axis=1)

    adj_mat2 = np.concatenate((np.zeros((len(adj_mat2), (adj_mat1.shape[1] - adj_mat2.shape[1]))), adj_mat2), axis=1) 

    adj_mat1 = np.concatenate((adj_mat1, adj_mat2), axis=0)

    # print(adj_mat1.shape) # (16, 16)

    return adj_mat1


def create_cyclohexane_ring(start_node):
    node_lst = [i for i in range(start_node, start_node + 8)]
    cyclohexane_mat = np.zeros((8, 8))
    for i in range(6):
        cyclohexane_mat[i][(i + 1) % 6] = 1
        cyclohexane_mat[(i + 1) % 6][i] = 1

    # internode 1,2
    cyclohexane_mat[1][6] = 1
    cyclohexane_mat[6][1] = 1
    cyclohexane_mat[2][6] = 1
    cyclohexane_mat[6][2] = 1
    cyclohexane_mat[4][6] = 1
    cyclohexane_mat[6][4] = 1
    cyclohexane_mat[5][6] = 1
    cyclohexane_mat[6][5] = 1

    # internode 2,3
    cyclohexane_mat[2][7] = 1
    cyclohexane_mat[7][2] = 1
    cyclohexane_mat[3][7] = 1
    cyclohexane_mat[7][3] = 1
    cyclohexane_mat[5][7] = 1
    cyclohexane_mat[7][5] = 1
    cyclohexane_mat[0][7] = 1
    cyclohexane_mat[7][0] = 1

    # print(dist_mat(cyclohexane_mat).max(axis=None))

    return cyclohexane_mat


def main():
    adj_mat = np.array([])
    for i in range(4):
        if adj_mat.any():
            # np.concatenate(adj_mat, create_cyclohexane_ring(i*8))
            adj_mat = concat_graphs(adj_mat, create_cyclohexane_ring(i*8))
        else:
            adj_mat = create_cyclohexane_ring(0)

    # Connecting individual rings

    # 0, 8
    adj_mat[0][8] = 1
    adj_mat[8][0] = 1

    # 4, 30
    adj_mat[4][30] = 1
    adj_mat[30][4] = 1

    # 12, 20
    adj_mat[12][20] = 1
    adj_mat[20][12] = 1

    # 16, 24
    adj_mat[16][24] = 1
    adj_mat[24][16] = 1

    draw_graph(adj_mat)

    print("Distance Matrix written to file 'cyclohexane_dist_mat.txt'")
    np.savetxt('cyclohexane_dist_mat.txt', dist_mat(adj_mat), fmt='%d')

    print("Max distance between any two nodes:")
    print(dist_mat(adj_mat).max(axis=None))

    # print number of each distance
    dist = dist_mat(adj_mat)
    dist = dist.astype(int).flatten().tolist()
    freq = {i: dist.count(i) for i in dist}
    print(freq)

    # print average distance
    print(f"Average distance between any two nodes: {round(np.mean(dist), 4)}")

if __name__ == '__main__':
    main()
