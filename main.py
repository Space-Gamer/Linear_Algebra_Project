import numpy as np
import itertools

# Adjacency matrix
# 1-2-3-4
adj_mat = [[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]]

# Adding intermediate nodes
# Matrix dimension increases from n->n*(n-1)
# def add_intermediate_nodes(adj_mat):
#     n = len(adj_mat)
#     adj_mat = np.array(adj_mat)
#     adj_mat = np.kron(adj_mat, np.identity(n-1))
#     adj_mat = np.kron(np.identity(n-1), adj_mat)
#     return adj_mat
#
# new_arr = add_intermediate_nodes(adj_mat)
# print(new_arr.shape)
n = len(adj_mat)

b = [[0 for i in range(n-1)] for j in range(n)]

arr = list((itertools.combinations(range(0, n), 2)))

print(arr)

# b matrix will be in the form 0-1, 1-2, 2-3

arr_temp = []

for (i,j) in arr:
    if adj_mat[i][j] == 1:
        arr_temp.append([i,j])

arr = arr_temp

print(arr)

for i in range(len(arr)):
    pass