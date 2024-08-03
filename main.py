import numpy as np
import itertools

from graph_plot import draw_graph
from fib_mat_gen import fib_sum_mat_gen

adj_mat = [[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]]

node_lst = [1, 2, 3, 4]


# adj_mat = [[0, 0, 1, 0],
#            [0, 0, 0, 1],
#            [1, 0, 0, 0],
#            [0, 1, 0, 0]]
#
# node_lst = [1, 2, 3, 4]

# adj_mat = [[0, 0, 1, 0, 0],
#            [0, 0, 0, 0, 1],
#            [1, 0, 0, 1, 0],
#            [0, 0, 1, 0, 0],
#            [0, 1, 0, 0, 0]]
#
# node_lst = [1, 2, 3, 4, 5]


def main(adj_mat=None, node_lst=None):
    if adj_mat is None:
        node_lst = list(map(int, input("Enter nodes: ").split()))

        adj_mat = []

        for i in node_lst:
            while True:
                r_lst = list(map(int, input(f"Enter adjacency list for node {i}: ").split()))
                if len(r_lst) != len(node_lst):
                    print("Invalid adjacency list. Try again.")
                else:
                    adj_mat.append(r_lst)
                    break

        if len(adj_mat) != len(node_lst) or len(adj_mat[0]) != len(node_lst):
            print("Invalid matrix")
            exit()

    adj_mat = np.array(adj_mat)  # Convert adjacency matrix to numpy array

    draw_graph(adj_mat, node_lst)

    n = len(adj_mat)  # Number of nodes

    inter_node_lst = list((itertools.combinations(node_lst, 2)))  # List of all possible node pairs

    arr_temp = []  # Temporary array to store node pairs that are connected

    for (i, j) in inter_node_lst:
        if adj_mat[node_lst.index(i)][node_lst.index(j)] == 1:
            arr_temp.append([i, j])

    inter_node_lst = arr_temp  # Update inter_node_lst

    print("Inter-node list: " + str(inter_node_lst))

    b = np.zeros((n, len(inter_node_lst)))  # B matrix
    b_dist = np.zeros((n, len(inter_node_lst)))  # B matrix for distance

    adj_dist = adj_mat.copy()  # A matrix for distance

    for (i, j) in inter_node_lst:  # Iterates through all node pairs
        for k in node_lst:  # Iterates through all nodes
            if k == i or k == j:  # If node is one of the nodes in the node pair
                b[node_lst.index(k)][inter_node_lst.index([i, j])] = 1  # That node is connected to the node pair
                b_dist[node_lst.index(k)][
                    inter_node_lst.index([i, j])] = 1  # That node is connected to the node pair directly
            else:
                if adj_mat[node_lst.index(i)][node_lst.index(k)] == 0 and adj_mat[node_lst.index(j)][
                    node_lst.index(k)] == 0:  # If both nodes in the node pair are not connected to the node k
                    b[node_lst.index(k)][inter_node_lst.index([i, j])] = 1
                    b_dist[node_lst.index(k)][inter_node_lst.index([i, j])] = 1
                    adj_dist[node_lst.index(i)][node_lst.index(k)] = 2
                    adj_dist[node_lst.index(j)][node_lst.index(k)] = 2
                    adj_dist[node_lst.index(k)][node_lst.index(i)] = 2
                    adj_dist[node_lst.index(k)][node_lst.index(j)] = 2

                elif adj_mat[node_lst.index(i)][
                    node_lst.index(k)] == 0:  # If only node i in the node pair is not connected to the node k
                    adj_dist[node_lst.index(i)][node_lst.index(k)] = 2
                    adj_dist[node_lst.index(k)][node_lst.index(i)] = 2
                    b_dist[node_lst.index(k)][inter_node_lst.index([i, j])] = 2

                elif adj_mat[node_lst.index(j)][
                    node_lst.index(k)] == 0:  # If only node j in the node pair is not connected to the node k
                    adj_dist[node_lst.index(j)][node_lst.index(k)] = 2
                    adj_dist[node_lst.index(k)][node_lst.index(j)] = 2
                    b_dist[node_lst.index(k)][inter_node_lst.index([i, j])] = 2

    print("\nB Matrix:\n", b)

    a_b = np.concatenate((adj_dist, b_dist), axis=1)
    print("\nA_B Matrix:\n", a_b)

    k_mat = (np.ones((len(inter_node_lst), len(inter_node_lst))) - np.identity(len(inter_node_lst))) * 2

    final_mat = np.concatenate((np.concatenate((adj_mat, b), axis=1),
                                np.concatenate((b.T, np.zeros((len(inter_node_lst), len(inter_node_lst)))), axis=1)),
                               axis=0)
    print("\nFinal Matrix:\n", final_mat.astype(int))

    new_node_lst = node_lst + [f"{i}, {j}" for (i, j) in inter_node_lst]
    draw_graph(final_mat, new_node_lst)

    final_dist_mat = np.concatenate((a_b, np.concatenate((b_dist.T, k_mat), axis=1)), axis=0)
    print("\nFinal Distance Matrix:\n", final_dist_mat.astype(int))


if __name__ == "__main__":
    n = int(input('Enter the number of nodes: '))
    adj_mat = fib_sum_mat_gen(n)
    node_lst = list(range(1, n + 1))
    main(adj_mat, node_lst)
