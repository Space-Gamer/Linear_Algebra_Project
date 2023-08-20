import numpy as np
import sys

from fib_mat_gen import fib_diff_mat_gen

sys.path.append('../Linear_Algebra_Project')

from graph_plot import draw_graph

def main(adj_mat, node_lst):
    
    def get_node_degree(adj_mat):
        return np.sum(adj_mat, axis=0)
    
    def get_edge_weight(adj_mat, nd_degree, asc=True):
        edge_weights = {}
        for i in range(len(adj_mat)):
            for j in range(len(adj_mat)):
                if adj_mat[i][j] == 1 and (j, i) not in edge_weights.keys():
                    edge_weights[(i, j)] = int(min(nd_degree[i], nd_degree[j]))
        if asc:
            edge_weights = dict(sorted(edge_weights.items(), key=lambda x: x[1]))
        return edge_weights
    
    def get_non_neighbour_nodes(adj_mat, node):
        non_neighbour_nodes = []
        for i in range(len(adj_mat)):
            if adj_mat[node][i] == 0 and i != node:
                non_neighbour_nodes.append(i)
        return non_neighbour_nodes
    
    def create_inter_node(adj_mat, node_i, node_j):
        adj_mat = np.append(adj_mat, np.zeros((1, len(adj_mat))), axis=0) # Add new row
        adj_mat = np.append(adj_mat, np.zeros((len(adj_mat), 1)), axis=1) # Add new column
        # Add a new node to the node list
        node_lst.append(f"{node_i}, {node_j}")
        # Join the new node to node_i and node_j
        adj_mat[node_i][-1] = 1
        adj_mat[-1][node_i] = 1
        adj_mat[node_j][-1] = 1
        adj_mat[-1][node_j] = 1

        return adj_mat, node_lst

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

    def get_max_dist(adj_mat):
        return np.max(dist_mat(adj_mat))
    
    
    edge_weights = get_edge_weight(adj_mat, get_node_degree(adj_mat))

    new_nodes = []

    while get_max_dist(adj_mat) > 2:
        i, j = list(edge_weights.keys())[0]
        nn_i = get_non_neighbour_nodes(adj_mat, i)
        nn_j = get_non_neighbour_nodes(adj_mat, j)
        inter_node = False
        for k in nn_i:
            if k in nn_j:
                if not inter_node:
                    new_nodes.append([i, j])
                    adj_mat, node_lst = create_inter_node(adj_mat, i, j)
                    inter_node = True
                adj_mat[k][-1] = 1 # Join the new node to k
                adj_mat[-1][k] = 1 # Join k to the new node
        del edge_weights[(i, j)]

    print("Number of nodes to be added: ", len(new_nodes))
    print("Nodes to be added: ", new_nodes)

    return adj_mat, node_lst

if __name__ == "__main__":
    n = int(input("Enter the number of nodes: "))

    fib_diff_mat = fib_diff_mat_gen(n)
    node_lst = list(range(0, n))
    
    draw_graph(fib_diff_mat, node_lst)

    fib_diff_mat, node_lst = main(fib_diff_mat, node_lst)

    draw_graph(fib_diff_mat, node_lst)