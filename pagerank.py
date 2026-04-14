"""
PageRank on Wikipedia Wisconsin Graph

- Builds adjacency matrix
- Prevents rank sinks
- Computes importance using eigenvector
"""

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import eigs


# ----------------------------
# Load Data
# ----------------------------
edges_file = open('wisconsin_edges.csv', "r")
nodes_file = open('wisconsin_nodes.csv', "r")

nodes_dict = {}
for line in nodes_file:
    idx, name = line.split(',',1)
    nodes_dict[int(idx.strip())] = name.strip()

n = len(nodes_dict)


# ----------------------------
# Build Adjacency Matrix
# ----------------------------
A = np.zeros((n,n))

for line in edges_file:
    i, j = line.split(',')
    A[int(j), int(i)] = 1.0


# ----------------------------
# PageRank Computation
# ----------------------------
A = A + 0.001  # prevent traps
A = A / A.sum(axis=0)

vals, vecs = eigs(csc_matrix(A), k=1)
scores = np.abs(np.real(vecs)).flatten()


# ----------------------------
# Top Pages
# ----------------------------
ranked = np.argsort(scores)[::-1]

print("Top 1 Page:", nodes_dict[ranked[0]])
print("Top 3 Page:", nodes_dict[ranked[2]])