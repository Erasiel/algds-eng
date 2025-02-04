# Trees, Binary Search Trees

### Exercise 1

Define or briefly describe the following concepts:
- Tree
- Rooted tree
- Types of nodes
  - Root
  - Leaf
  - Inner node
- Relations between nodes:
  - Child, parent
  - Descendant, ancestor
  - Sibling
  - Subtree
- Height (of trees and nodes)
- Special types of trees:
  - Binary tree
  - Complete binary tree
  - Nearly complete binary tree
  <!-- - Balanced binary tree -->

---

### Exercise 2

Determine which of the following properties are true for the graphs below (labeled (a) to (f)):
1. Tree
2. Binary tree
3. Complete binary tree
4. Nearly complete binary tree
<!-- 5. Balanced binary tree -->

![Graphs for exercise 2](./img/07_trees_exercise02.svg)
---

### Exercise 3

How can we represent rooted trees? Describe and illustrate at least two approaches. Can we represent binary trees differently?

---

### Exercise 4

Your intern gave you the following code snippet with the function `height` that calculates the height of a node in a binary tree. Unbeknownst to them, the `height` function is implemented incorrectly. Demonstrate why by giving an example on which it fails to return the correct height and fix the mistake. Keep the function recursive.

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


def height(node: BinaryTreeNode) -> int:
    if node.left is None and node.right is None:
        return 0

    return max(height(node.left), height(node.right)) + 1
```

Example: the following code snippet creates a (simplified) binary tree with the same structure as the one in Exercise 2 (e). For this tree, the call `height(root)` returns the correct height. Your task is to create an example on which the algorithm does not work correctly, and then fix the algorithm.

```py
leaf1 = BinaryTreeNode(1)
leaf2 = BinaryTreeNode(1)
leaf3 = BinaryTreeNode(1)
inner1 = BinaryTreeNode(1, left=leaf1, right=leaf2)
root = BinaryTreeNode(1, left=inner1, right=leaf3)
assert height(root) == 2, "The height of this tree should be 2"
```

---

### Exercise 5

When is a binary tree *height-balanced*? Implement a recursive algorithm that checks whether a binary tree (given by its root node) is balanced. Use the `height` function from Exercise 4, along with the following outline:

```py
def is_balanced(root: BinaryTreeNode) -> bool:
    # TODO
```

---

### Exercise 6

What is a binary search tree (BST)? What are the algorithms for insertion, search, deletion, predecessor/successor, min/max? To demonstrate how these algorithms work, start with the following binary search tree:

![Initial BST](img/07_trees_exercise06.svg)

and execute the following operations subsequently (i.e. execute each operation on the tree that results from the previous operation):
1. Insertion: `insert(20)`, `insert(11)`, `insert(27)`, `insert(40)`
2. Search / contains: `contains(11)`, `contains(35)`
3. Minimum, maximum: `min()`, `max()`
4. Successor: `successor(22)`, `successor(11)`, `successor(40)`
5. Deletion: `delete(40)`, `delete(8)`, `delete(22)`

What is the time complexity of these operations?

---

### Exercise 7

Implement a binary search tree for storing a set of integers. Use the outline below, but feel free to extend it with any (private) functions. Focus on `insert`, `contains`, `min`, `max`, and `delete`, as well as setting not only children, but parent references correctly.

The private helper function `_replace` is already implemented for you. This function replaces the subtree with root `u` with the subtree with root `v` in the tree. It might come in handy with the implementation of `delete`.

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


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key: int) -> None:
        # If the tree is empty, create a new root
        if self.root is None:
            self.root = BinaryTreeNode(key)
        # TODO

    def contains(self, key: int) -> bool:
        # TODO
        pass

    def min(self) -> int:
        # TODO
        pass

    def max(self) -> int:
        # TODO
        pass

    def delete(self, key) -> int:
        # TODO
        pass

    def successor(self, key) -> int:
        # TODO
        pass

    def predecessor(self, key) -> int:
        # TODO
        pass

    def _replace(self, u: BinaryTreeNode, v: BinaryTreeNode) -> None:
        """Replaces the subtree with root `u` with the subtree with root `v`."""

        # u is the root node
        if u.parent is None:
            self.root = v

        # u is the left child of its parent
        elif u.parent.left == u:
            u.parent.left = v

        # u is the right child of its parent
        else:
            u.parent.right = v

        # Set v's parent as u's original parent
        v.parent = u.parent
```

