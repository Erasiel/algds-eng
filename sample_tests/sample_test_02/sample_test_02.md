# Sample Test 2

**Before you begin**

During the test, you don't have access to any website other than CooSpace. In the `algds_test` folder, you are given all practice materials (including solutions), all slides of the lecture, the fourth edition of the Introduction to Algorithms book, and the test itself.

Before you start writing the test, mount your home directory (the `/home/hxxxxxx` directory). Any work in this directory will be automatically saved during the time of the test and is recoverable during and after the test by the instructor. Your solutions should be submitted through the CooSpace system, but files in your home directory can be considered if you fail to upload them. **All files outside your home directory are not secure during the test and will be lost when you shut down your PC.**

You are given four tasks, each worth exactly 8 points. **You have to choose three tasks to complete.** The choice is entirely up to you, but you can only get points for three tasks. You won't get extra points for attempting all four tasks. You can earn up to 24 points in this test, and, as per the requirements, you have to earn at least 8.

Feel free to use built-in data structures (e.g. `set`, `list`, `dict`) and algorithms (e.g. `sort`, `index`) unless specified otherwise.

Each task contains a set of test cases as examples, but be aware that just because your algorithm passes all the example tests, it might not be correct. You are encouraged to write further test cases (specifically to test edge cases), but this is not required. You don't have to test the type of input parameters in your implementation, everything is as seen in the type hints.

You have 110 minutes to complete your work. You can upload your solutions in CooSpace either as separate files for each task, or as one file.

Good luck!

---

### Task 1 - Nodes at Depth $k$

In a tree, the *depth* of a node $v$ is the length of the path from the root to $v$. The depth of the root is always zero. Design and implement an algorithm that determines the number of nodes at depth $k$ in a binary tree (given by its root node). Make sure your algorithm runs in at most $O(n)$ time, where $n$ is the number of nodes in the tree.

Use the following outline:

```py
class BinaryTreeNode:
    def __init__(self,
                 key: int,
                 parent: Optional["BinaryTreeNode"] = None,
                 left: Optional["BinaryTreeNode"] = None,
                 right: Optional["BinaryTreeNode"] = None
    ) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def num_nodes_at_depth(root: BinaryTreeNode, k: int) -> int:
    # TODO
    pass
```

Tests:
```py
leaf1 = BinaryTreeNode(1)
leaf2 = BinaryTreeNode(1)
leaf3 = BinaryTreeNode(1)
inner1 = BinaryTreeNode(1, left=leaf1, right=leaf2)
root = BinaryTreeNode(1, left=inner1, right=leaf3)

assert num_nodes_at_depth(root, 0) == 1
assert num_nodes_at_depth(root, 1) == 2
assert num_nodes_at_depth(root, 2) == 2
```

Explanations:
1. There's only the root node at depth 0.
2. The root's two children are at depth 1.
3. The two children of the root's left child are at depth 2. The root's right child has no children, so there are only two nodes at depth 2.

---

### Task 2 - Repeating Row Filter

Design and implement an algorithm that filters the repeating rows in a two-dimensional binary array (i.e. an array that only contains ones and zeros). The $i^\text{th}$ row is *repeating* if there exists $j < i$ such that the $j^\text{th}$ row is the same as the $i^\text{th}$ row. Your algorithm should return a copy of the input matrix with the repeating rows removed. Make sure your algorithm runs in $O(nm)$ time in the average case, where $n$ and $m$ are the dimensions of the matrix.

Use the following outline:
```py
def repeating_row_filter(mtx: List[List[int]], n: int, m: int) -> List[List[int]]:
    # TODO
    pass
```

Tests:
```py
mtx1 = [
    [1],
    [0]
]
assert repeating_row_filter(mtx1, 2, 1) == [[1], [0]]

mtx2 = [
    [1, 1],
    [1, 1]
]
assert repeating_row_filter(mtx2, 2, 2) == [[1, 1]]

mtx3 = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
]
assert repeating_row_filter(mtx3, 5, 4) == [[0, 0, 1, 1],
                                            [1, 0, 1, 0],
                                            [1, 1, 1, 1]]

```

---

### Task 3 - Circle

Design and implement an algorithm that decides whether there is a circle in a directed graph. A circle is present if there are two nodes, $u$ and $v$, such that there exists a path from $u$ to $v$, and a path from $v$ to $u$.

Use the outline below, where `Graph` is an abstract class whose subclasses implement a simple Graph. The full implementation, including a fully implemented `Graph` subclass (named `GraphImpl`) is given in `src/task04.py`.

```py
def contains_circle(graph: Graph) -> bool:
    # TODO
    pass
```

Tests:
```py
graph = GraphImpl(undirected=False)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
assert not contains_circle(graph)

graph = GraphImpl(undirected=False)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
assert not contains_circle(graph)

graph = GraphImpl(undirected=False)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")
assert contains_circle(graph)
```

---

### Task 4 - Network Rebuild

The country of Madeupland wants to rebuild its internet network from scratch. The requirements towards the new network is simple: it has to have a path between all pairs of cities, and it has to be as cheap as possible.

The design committee creates a map of every city in the country and connects cities that can be connected with regular networks. They calculate and note down the cost of building each of the possible connections and are appalled at how expensive the project is going to be.

Luckily for the committee, Melon Husk, a wealthy investor decided to help the project. His company offers a very efficient type of Fiber-Optic Cable that can connect *any* pair of cities. Mr. Husk made a shady deal with the government and pledged to connect $k$ pairs of cities in Madeupland for free. The committe now has to submit a cost estimation for creating the network.

Design and implement an algorithm that calculates the lowest possible cost for building the network. The input is a list of $n$ strings representing the name of the cities, a list of $m$ three-element tuples (where the first two elements are names of cities and the third is a real number that representing the cost of building the standard network between the two cities), and an integer $k$, the number of free Fiber-Optic Cables. Both standard, and Fiber-Optic connections are bidirectional. Return the total cost of building the network or `math.inf` if the network cannot be built.

Use the following outline:
```py
def network_rebuild(cities: List[str],
                    costs: List[Tuple[str, str, float]],
                    k: int,
                    n: int,
                    m: int
) -> float:
    # TODO
    pass
```

Tests:
```py
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
assert network_rebuild(cities, costs, 1, 3, 3) == 5.0   # note: k = 1
```

Explanations:
1. We can connect 1 pair of cities for free, so we build the cheapest connection between `B` and `C` and connect `A` to either `B` or `C`.
2. We can connect 2 pairs of cities for free, so we can build the network for free.
3. Even if we build the two possible connections, our network isn't complete. We need to use the free connection to connect all cities, so our cost is 5.
