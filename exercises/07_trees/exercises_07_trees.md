# Trees, Binary Search Trees

### Exercise 1

Determine which of the following properties are true for the graphs below (labeled (a) to (f)). Assume the root node is always the uppermost node.
1. Tree
2. Binary tree
3. Complete binary tree
4. Nearly complete binary tree
<!-- 5. Balanced binary tree -->

![Graphs for exercise 2](./img/07_trees_exercise02.svg)
---

### Exercise 3

Design and implement a recursive algorithm that calculates the number of leaf nodes in a binary tree.

---

### Exercise 4

What is the height of a binary tree? Design and implement a recursive algorithm that calculates the height of a binary tree.

---

### Exercise 4

Your intern gave you the following code snippet with the function `height` that calculates the height of a node in a binary tree. Unbeknownst to them, the `height` function is implemented incorrectly. Demonstrate why by giving an example on which it fails to return the correct height and fix the mistake. Keep the function recursive.

```py
from typing import Optional


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


def height(node: BinaryTreeNode) -> int:
    if node.left is None and node.right is None:
        return 0

    return max(height(node.left), height(node.right)) + 1
```

---

### Exercise 5

When is a tree height-balanced? Design and implement a recursive algorithm that determines whether a tree is height-balanced.

---

### Exercise 6

When is a tree height-balanced? Design and implement a recursive algorithm that determines whether a tree is height-balanced. Make sure your algorithm runs in at most $O(n)$ time, where $n$ is the number of nodes.

---

### Exercise 7

You are given a half-complete implementation of a binary tree that implements a **set** that stores integers. Implement the following member functions:
- `insert`: inserts a key into the BST
- `contains`: returns `True` if the given key is in the BST, and `False` otherwise
- `min`: returns the minimum key in the BST
- `max`: returns the maximum key in the BST

Make sure to correctly set not only the children pointers, but the parent pointers as well.
