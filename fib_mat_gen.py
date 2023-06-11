import numpy as np


def is_perfect_square(n):
    return n ** 0.5 == int(n ** 0.5)


def fib_check(n):
    if n == 1:
        return True
    elif is_perfect_square(5 * n ** 2 + 4) or is_perfect_square(5 * n ** 2 - 4):
        return True
    else:
        return False


def fib_mat_gen(n):  # Generates an adjacency matrix for a graph with n nodes which are connected if the sum of their
    # labels is a Fibonacci number
    if n > 1:
        adj_mat = np.zeros((n, n))
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if fib_check(i + j):
                    adj_mat[i - 1][j - 1] = 1
                    adj_mat[j - 1][i - 1] = 1
        print("Fibonacci adjacency matrix:" + "\n" + str(adj_mat))
        return adj_mat
    else:
        return [[0]]
