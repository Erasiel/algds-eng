import math
from typing import List, Tuple


# The design of the algorithm is as follows:
# This is obviously a minimum spanning tree problem with a twist, so we can
# start by copy-pasting an MST algorithm and its dependencies. I chose
# Kruskal's algorithm, not only for its simplicity, but also because it
# returns the MST's edges in sorted order, which is useful in solving this
# problem. This immediately adds ~150 lines of code, all of which is prepared
# for us in advance.
# The first step is to transform the input into a graph. This is very easy,
# the cities are the vertices and the edges are given by the costs. Next, we
# compute the graph's MST (more precisely its minimum spanning forest, as the
# graph may not be connected). The k free edges can be used to substitute
# expensive edges, or fill in for missing edges in order to minimize the cost
# of the MST. Let n_edges be the number of edges in the minimum spanning
# forest, as discovered by the MST algorithm. Altogether, there are 3 cases:
# 1. (n_edges + k) < (|V| - 1)
#   The MST cannot be built, the cost is infinite.
# 2. (n_edges + k) >= (|V| - 1)
#   The MST can be built
#   2.1 n_edges >= (|V| - 1)
#       Replace the k MST edges with the highest cost with free edges
#   2.2 n_edges < (|V| - 1)
#       Some of the free edges have to be used to connect the MST, the rest
#       can be used to replace the most expensive edges.



class WeightedGraph:
    def __init__(self, undirected: bool = False) -> None:
        self.undirected = undirected
        self.adjacency_list = dict()

    def add_vertex(self, vertex_id: str) -> None:
        if vertex_id not in self.adjacency_list.keys():
            self.adjacency_list[vertex_id] = list()

    def add_edge(self, vertex_from: str, vertex_to: str, weight: float) -> None:
        # Add the vertices if they are not already in the graph
        self.add_vertex(vertex_from)
        self.add_vertex(vertex_to)

        # Check if the edge is not a duplicate and add it
        if not self.edge_exists(vertex_from, vertex_to):
            self.adjacency_list[vertex_from].append((vertex_to, weight))

        # In undirected graphs, the existence of the edge u -> v means the the
        # edge v -> u also exists
        if self.undirected and not self.edge_exists(vertex_to, vertex_from):
            self.adjacency_list[vertex_to].append((vertex_from, weight))

    def get_vertices(self) -> List[str]:
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex_id: str) -> List[Tuple[str, float]]:
        if vertex_id in self.adjacency_list.keys():
            return self.adjacency_list[vertex_id]
        raise ValueError(f"Vertex {vertex_id} is not in the graph!")

    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        if vertex_from in self.adjacency_list.keys():
            for neighbor, weight in self.adjacency_list[vertex_from]:
                if neighbor == vertex_to:
                    return True
        return False

    def get_edges(self) -> List[Tuple[str, str, float]]:
        edges = list()
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor, weight in neighbors:
                edges.append((vertex, neighbor, weight))
        return edges

    def get_edge_weight(self, vertex_from: str, vertex_to: str) -> float:
        if self.edge_exists(vertex_from, vertex_to):
            for neighbor, weight in self.adjacency_list[vertex_from]:
                if neighbor == vertex_to:
                    return weight
        else:
            raise ValueError(f"The edge {vertex_from} -> {vertex_to} is not "
                             "in the graph!")


class DisjointSet:
    def __init__(self) -> None:
        self.elements = {}

    def make_set(self, elem: str) -> None:
        """Creates a new one-element set."""
        self.elements[elem] = elem

    def union(self, u: str, v: str) -> None:
        """Unites the two sets that contain `u` and `v`."""
        rep_u = self.find(u)
        rep_v = self.find(v)
        for elem in self.elements:
            if self.find(elem) == rep_u:
                self.elements[elem] = rep_v

    def find(self, u: str) -> str:
        """Finds the representative of the set that contains `u`."""
        return self.elements[u]


def edge_weight(edge: Tuple[str, str, float]) -> float:
    """Returns the weight of a weighted edge."""
    return edge[2]


def filter_duplicate_edges(edges: List[Tuple[str, str, float]]
) -> List[Tuple[str, str, float]]:
    """Filters duplicate undirected edges."""
    unique_edges = []
    for edge in edges:
        vertex_from, vertex_to, weight = edge
        if not ((vertex_from, vertex_to, weight) in unique_edges or
                (vertex_to, vertex_from, weight) in unique_edges):
            unique_edges.append(edge)
    return unique_edges


def kruskal_mst(graph: WeightedGraph) -> List[Tuple[str, str, float]]:
    # Create a disjoint set (union-find) data structure for managing the
    # different trees
    trees = DisjointSet()

    # Initially, every vertex is in its own, one-element tree
    for vertex in graph.get_vertices():
        trees.make_set(vertex)

    # Sort the edges by weight in ascending order
    # Note: since the graph is undirected, every edge will appear twice, i.e.
    # for the edge (u, v) with weight w, there will be an entry (u, v, w) and
    # another entry (v, u, w) in the ordered list. We filter these with the
    # filter_duplicate_edges function, but the algorithm is correct even
    # without this step.
    edges = filter_duplicate_edges(graph.get_edges())
    sorted_edges = sorted(edges, key=edge_weight)

    # Store the list of MST edges
    mst_edges = []

    # Traverse the edges in sorted order
    for edge in sorted_edges:

        # If the edge connects two different trees, add it to the MST and
        # unite these two trees in the disjoint set
        source, dest, weight = edge
        tree_1 = trees.find(source)
        tree_2 = trees.find(dest)

        if tree_1 != tree_2:
            mst_edges.append(edge)
            trees.union(tree_1, tree_2)

    # Return the edges of the MST
    return mst_edges


def network_rebuild(cities: List[str],
                    costs: List[Tuple[str, str, float]],
                    k: int,
                    n: int,
                    m: int
) -> float:
    # Transform the input into a graph
    graph = WeightedGraph(undirected=True)
    for city in cities:
        graph.add_vertex(city)

    for city_from, city_to, cost in costs:
        graph.add_edge(city_from, city_to, cost)

    # Compute the minimum spanning forest of the graph
    mst_edges = kruskal_mst(graph)
    n_mst_edges = len(mst_edges)
    n_vertices = len(graph.get_vertices())

    # Case 1: the MST cannot be built
    if (k + n_mst_edges) < n_vertices - 1:
        return math.inf

    # Case 2: the MST can be built
    else:
        # Here, I combined case 2.1 and 2.2 by indirectly calculating how many
        # edges are missing from the MST (and should be filled with a free
        # edge) and as such, how many of the minimum spanning forest's edges
        # can be replaced by free edges
        n_desired_edges = n_vertices - 1
        n_removable_edges = (n_mst_edges + k) - n_desired_edges

        # We can use free edges to replace the most costly edges
        # Here, I make use of the fact that Kruskal's algorithm returns the
        # edges of the minimum spanning forest in sorted order (by edge
        # weight), so by removing the last element of the list, I always
        # remove the edge with the highest cost
        for _ in range(n_removable_edges):
            if len(mst_edges) > 0:
                mst_edges.pop(-1)

        # Sum the cost of the edges that are not replaced with free edges
        cost = 0
        for _, _, w in mst_edges:
            cost += w

        return cost


if __name__ == "__main__":
    cities = ["A", "B", "C"]
    costs = [
        ("A", "B", 10.2),
        ("B", "C", 5.3),
        ("A", "C", 7.2)
    ]
    assert network_rebuild(cities, costs, 1, 3, 3) == 5.3   # note: k = 1
    assert network_rebuild(cities, costs, 2, 3, 3) == 0     # note: k = 2

    cities = ["A", "B", "C", "D"]
    costs = [
        ("A", "B", 2.0),
        ("C", "D", 3.0)
    ]
    assert network_rebuild(cities, costs, 1, 4, 2) == 5.0   # note: k = 1
