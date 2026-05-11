# Graphs and Elementary Graph Algorithms

### Exercise 1

Implement the following graph operations using the adjacency list representation:
- `add_vertex(G, v)`: adds a vertex labeled with `v` to the graph `G`
- `add_edge(G, u, v)`: adds an edge between vertices `u` and `v` to the graph `G`
- `get_vertices(G)`: returns all vertices in the graph `G`
- `get_edges(G)`: returns all edges in the graph `G`
- `get_neighbors(G, v)`: returns all neighbors of the vertex `v` in graph `G`

---

### Exercise 2

Run breadth-first search on the following directed graph with vertex `A` as the starting vertex.

![Graph for Exercise 02](img/09_graphs_exercise02.svg)

---

### Exercise 3

You are given a correct and complete BFS implementation. Check the correctness of your BFS execution in Exercise 02 using the provided BFS implementation.

---

### Exercise 4

Run depth-first search on the following directed graph. Assume all vertices and their neighbors are ordered alphabetically.

![Graph for Exercise 04](img/09_graphs_exercise04.svg)

---

### Exercise 5

You are given a correct and complete DFS implementation. Check the correctness of your DFS execution in Exercise 02 using the provided DFS implementation.

---

### Exercise 6

The "Wikipedia game" is a famous game among students. All players start at the same randomly selected Wikipedia page and their goal is to reach a common destination page as quickly as possible. The only way to move from page A to page B is by clicking a link on page A that takes the player to page B. The player with the least moves from the starting page to the destination page wins the game.

You are given a list of Wikipedia pages and a list of links that can take you from page A to page B. Note that just because there exists a link on page A to page B, there might not exist a link on page B to page A. You are also given the starting and destination pages. Design and develop an algorithm that returns the optimal solution to the Wikipedia game (i.e. the lowest number of moves that takes the player to the destination page from the starting page). If the game cannot be completed, return -1.

---

### Exercise 7

You are given a list of words with equal length, and a starting and destination word. We say a word can be transformed to another if they differ in a single letter. Calculate the lowest number of transformations that can change the starting word to the destination word, if we can only transform to words in the given list. If the starting word cannot be transformed to the destination word, return -1. Note that the starting word is not necessarily in the word list.

---

### Exercise 8

You are given a rectangular two-dimensional list of non-negative integers that represents a map. Positive numbers represent land, 0 represents water. Two land tiles are connected if they share a side (i.e., only one of their coordinates differs by 1). Assume that everything outside of what the map shows is water. Design and implement an algorithm that calculates the number of islands on the map.

