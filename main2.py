import numpy as np
import itertools

from graph_plot import draw_graph
from fib_mat_gen import fib_mat_gen

adj_mat = [[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]]

node_lst = [1, 2, 3, 4]


def node_degree(adj_mat):
    return np.sum(adj_mat, axis=0)


def single_node_degree(node, adj_mat):
    return np.sum(adj_mat[node])


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

    # node_deg = node_degree(adj_mat)
    # print(f"Node degree: {node_deg}")
    #
    # print(f"Distance matrix: \n{dist_mat(adj_mat)}")

    # sorted_node_lst = sorted(node_lst, key=lambda x: single_node_degree(x-1, adj_mat))

    sorted_inter_node_lst = sorted(list(itertools.combinations(node_lst, 2)), key=lambda x: (
        single_node_degree(x[0] - 1, adj_mat) + single_node_degree(x[1] - 1, adj_mat),
        min(single_node_degree(x[0] - 1, adj_mat), single_node_degree(x[1] - 1, adj_mat))))

    arr_temp = []  # Temporary array to store node pairs that are connected

    for (i, j) in sorted_inter_node_lst:
        if adj_mat[node_lst.index(i)][node_lst.index(j)] == 1:
            arr_temp.append([i, j])

    sorted_inter_node_lst = arr_temp  # Update inter_node_lst

    print("Sorted node pairs: ", sorted_inter_node_lst)

    additional_nodes = []

    while dist_mat(adj_mat).max(axis=None) > 2:
        i, j = sorted_inter_node_lst.pop(0)

        # Adding a new node in adjacency matrix
        new_adj_mat = np.zeros((len(adj_mat) + 1, len(adj_mat) + 1))  # Create a new array with one more row and column
        new_adj_mat[:-1, :-1] = adj_mat  # Copy the old array into the new array
        new_adj_mat[node_lst.index(i)][-1] = 1  # Connect new node to node i
        new_adj_mat[-1][node_lst.index(i)] = 1  # Connect node i to new node
        new_adj_mat[node_lst.index(j)][-1] = 1  # Connect new node to node j
        new_adj_mat[-1][node_lst.index(j)] = 1  # Connect node j to new node
        adj_mat = new_adj_mat  # Update adj_mat
        additional_nodes.append([i, j])  # Add node pair to additional_nodes

        for k in node_lst:
            if k != i and k != j:  # If node is not in the node pair
                if adj_mat[node_lst.index(i)][node_lst.index(k)] == 0 and adj_mat[node_lst.index(j)][node_lst.index(k)] \
                        == 0:  # If node is not connected to either node in the node pair
                    adj_mat[node_lst.index(k)][-1] = 1  # Connect node to new node
                    adj_mat[-1][node_lst.index(k)] = 1  # Connect new node to node

        print(f"New adjacency matrix: \n{adj_mat}")
        print("Maximum distance: ", dist_mat(adj_mat).max(axis=None))
        new_node_lst = node_lst + [f"{i}, {j}" for (i, j) in additional_nodes]
        draw_graph(adj_mat, new_node_lst)


if __name__ == "__main__":
    n = int(input('Enter the number of nodes: '))
    adj_mat = fib_mat_gen(n)
    node_lst = list(range(1, n + 1))
    main(adj_mat, node_lst)  # Only works when nodes are numbered from 1 to n
