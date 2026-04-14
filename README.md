# PageRank Implementation on Wikipedia Graph

## Overview
This project implements the **PageRank algorithm** from scratch to rank the importance of pages in a directed graph. Using a subset of Wikipedia pages related to Wisconsin, the algorithm computes page importance using **eigenvector methods**.

---

## Key Features

### 🔹 Graph Construction
- Built adjacency matrix from edge list data
- Represented directed links between pages

### 🔹 PageRank Algorithm
- Implemented PageRank using eigenvector computation
- Added smoothing factor to prevent rank sinks (trap states)
- Normalized transition matrix

### 🔹 Efficient Computation
- Used sparse matrix representation for scalability
- Computed dominant eigenvector using:
    scipy.sparse.linalg.eigs

### 🔹 Ranking Pages
- Extracted most important pages based on PageRank scores
- Sorted pages by importance

---

## Methods

### Transition Matrix
- Constructed from adjacency matrix A
- Normalized columns:
    A = A / sum(A)

### Smoothing
- Added small constant:
    A = A + ε
- Prevents dead ends and improves convergence

### Eigenvector Computation
PageRank is the dominant eigenvector:
    A v = λ v

---

## Results & Insights

- Pages with more inbound links receive higher rank  
- Graph structure strongly influences ranking  
- Small smoothing term prevents rank collapse  
- Eigenvector methods efficiently compute rankings  

---

## Technologies Used

- Python
- NumPy
- SciPy (sparse matrices & eigenvalues)

---

## How to Run

### 1. Install dependencies
```
pip install numpy scipy
```

### 2. Run the script
```
python src/pagerank.py
```

---

## Applications

- Search engine ranking
- Network analysis
- Social network influence modeling
- Recommendation systems

---

## Summary

This project demonstrates how eigenvector-based methods can be used to rank nodes in a graph, forming the foundation of modern search engine algorithms like PageRank.
