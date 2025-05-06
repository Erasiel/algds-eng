# Sample Test 2

**Before you begin**

During the test, you do not have access to the internet. After unzipping `algds_test_02.zip`, you will find two folders: `algds_materials/` and `algds_test_02/`.

The contents of the `algds_materials/` folder are:
- `practice_materials/`: contains all practice exercises and their solutions
- `lecture_materials/`: contains all lecture slides
- `book.pdf`: the fourth edition of the Introduction to Algorithms book

The contents of the `algds_test_02/` folder are:
- `src/`: contains prepared source files for all tasks with outlines and tests
- `test_02.md`: the test itself

You are given four tasks, each worth exactly 8 points. **You have to choose three tasks to complete.** The choice is up to you, but you can only get points for three tasks. You won't get extra points for completing all four tasks. You can earn up to 24 points in this test, and, as per the requirements, you have to earn at least 8.

Create a folder in your home directory (`/home/hxxxxxx`) named `solutions`. Only work in your home directory! There, your work will be automatically saved during the time of the test and is recoverable during and after the test by the instructor. **All files outside your home directory are not secure during the test and will be lost when you shut down your PC.** You don't have to submit your solutions anywhere, leave them in the `/home/hxxxxxx/solutions` folder when you are done.

Each task contains a set of test cases as examples, but be aware that just because your algorithm passes all the example tests, it might not be correct. You are encouraged to write further test cases (specifically to test edge cases), but this is not required and will not be scored.

Feel free to use built-in data structures (e.g. `set`, `list`, `dict`) and algorithms (e.g. `sort`, `index`) unless specified otherwise. You should assume that the input parameters conform to the type hints and the constraints in the task descriptions.

You have 110 minutes to complete your work. At the end of this time, the computers will shut down, and any unsaved work or work outside your home directory will be lost.

Good luck!

---

### Task 1 - Nodes at Depth $k$

In a tree, the *depth* of a node $v$ is the length of the path from the root to $v$. The depth of the root is always zero, the depth of the root's children is one, etc. Design and implement an algorithm that determines the number of nodes at depth $k$ in a binary tree (given by its root node). Make sure your algorithm runs in at most $O(n)$ time, where $n$ is the number of nodes in the tree.

Use the following outline:

```py
from typing import Any, Optional


class BinaryTreeNode:
    def __init__(self,
                 key: Any,
                 left: Optional["BinaryTreeNode"] = None,
                 right: Optional["BinaryTreeNode"] = None
    ) -> None:
        self.key = key
        self.left = left
        self.right = right


def num_nodes_at_depth(root: BinaryTreeNode, k: int) -> int:
    # TODO
    pass
```

Tests:
```py
# Test 1
# Tree structure:
#     A
#    / \
#   B   C
#  / \
# E   D
leaf1 = BinaryTreeNode("E")
leaf2 = BinaryTreeNode("D")
leaf3 = BinaryTreeNode("C")
inner1 = BinaryTreeNode("B", left=leaf1, right=leaf2)
root = BinaryTreeNode("A", left=inner1, right=leaf3)

assert num_nodes_at_depth(root, 0) == 1
assert num_nodes_at_depth(root, 1) == 2
assert num_nodes_at_depth(root, 2) == 2
assert num_nodes_at_depth(root, 3) == 0

# Test 2
# Tree structure:
#     A
#    / \
#   B   C
#  /   / \
# D   E   F
#    /
#   G
leaf2 = BinaryTreeNode("G")
leaf3 = BinaryTreeNode("F")
inner2 = BinaryTreeNode("E", left=leaf2)
leaf1 = BinaryTreeNode("D")
inner3 = BinaryTreeNode("C", left=inner2, right=leaf3)
inner1 = BinaryTreeNode("B", left=leaf1)
root = BinaryTreeNode("A", left=inner1, right=inner3)
assert num_nodes_at_depth(root, 0) == 1
assert num_nodes_at_depth(root, 1) == 2
assert num_nodes_at_depth(root, 2) == 3
assert num_nodes_at_depth(root, 3) == 1
```

Explanations:
- Test #1:
    1. There's only the root node (A) at depth 0.
    2. The root's two children (B and C) are at depth 1.
    3. D and E are at depth 2.
    4. There are no nodes at depth 3.
- Test #2:
    1. There's only the root node (A) at depth 0.
    2. The root's two children (B and C) are at depth 1.
    3. D, E, and F are at depth 2.
    4. G is at depth 3.

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

Design and implement an algorithm that decides whether there is a circle in a directed graph. A circle is present if there are two vertices, $u$ and $v$, such that there exists a path from $u$ to $v$, and a path from $v$ to $u$.

Use the outline below, where `Graph` is an abstract class whose subclasses implement a simple Graph. The full class, along with a fully implemented `Graph` subclass (named `AdjacencyListGraph`) is given in `src/task04.py`.

```py
def contains_circle(graph: Graph) -> bool:
    # TODO
    pass
```

Tests:
```py
graph = AdjacencyListGraph(undirected=False)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
assert not contains_circle(graph)

graph = AdjacencyListGraph(undirected=False)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
assert not contains_circle(graph)

graph = AdjacencyListGraph(undirected=False)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")
assert contains_circle(graph)
```

---

### Task 4 - Network Rebuild

The country of Madeupland wants to rebuild its internet network from scratch. The requirements towards the new network are simple: it has to have a path between all pairs of cities, and it has to be as cheap as possible.

The design committee creates a map of every city in the country and connects cities that can be connected with regular networks. They calculate and note down the cost of building each of the possible connections and are appalled at how expensive the project is going to be.

Luckily for the committee, Melon Husk, a wealthy investor decided to help the project. His company offers a very efficient type of Fiber-Optic Cable that can connect *any* pair of cities. Mr. Husk made a shady deal with the government and pledged to connect $k$ pairs of cities in Madeupland for free. The committe now has to submit a cost estimation for creating the network.

Design and implement an algorithm that calculates the lowest possible cost for building the network. The input is a list of $n$ strings representing the name of the cities, a list of $m$ three-element tuples (where the first two elements are names of cities and the third is a real number that representing the cost of building the standard network between the two cities), and an integer $k$, the number of free Fiber-Optic Cables. Both standard, and Fiber-Optic connections are bidirectional. Return the total cost of building the network or `math.inf` if the network cannot be built.

Use the following outline:
```py
import math


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
