# Trees, Binary Search Trees - Solutions

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

### Solution

Most of these definitions can be found in the materials of the lecture, so we refer the reader to those, or the Introduction to Algorithms book. We discuss the definitions that are used in Exercise 2:
- Tree: connected, acyclic graph
- Binary tree: a rooted tree where each node can have at most 2 children
- Complete binary tree: a binary tree in which all levels are fully filled
- Nearly complete binary tree: a binary tree in which all levels are fully filled, except possibly the last level

---

### Exercise 2

Determine which of the following properties are true for the graphs below (labeled (a) to (f)). Assume the root node is always the uppermost node.
1. Tree
2. Binary tree
3. Complete binary tree
4. Nearly complete binary tree
<!-- 5. Balanced binary tree -->

![Graphs for exercise 2](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/07_trees/img/07_trees_exercise02.svg)

### Solution

1. Tree: (a), (b), (c), (d), (e)
2. Binary tree: (b), (c), (d), (e)
3. Complete binary tree: (c)
4. Nearly complete binary tree: (c), (d), (e)

---

### Exercise 3

How can we represent rooted trees with unbounded branching (i.e. the number of children of every node is unbounded)? Describe and illustrate at least two approaches. Can we represent binary trees differently?

### Solution

Regardless of branching, we always represent nodes as objects and edges as pointers between objects. The two types of node representations, when branching is unbounded (i.e. a node can have arbitrarily many children) are the following:

**Child edge-list:** every node contains a list that stores pointers to its children. Traversing a node's children is as simple as iterating over this list.

**Left-child right-sibling**: every node contains a pointer to its leftmost child and right sibling. Traversing a node's children is similar to traversing a linked list: treat the pointer to the leftmost child as the `head` pointer, and the children's pointers to their right siblings as the `next` pointers.

**Binary trees** don't have unbounded branching, which allows us to store pointers to the left and right children separately. A simple implementation can be seen in Exercise 4.

Note that by default, trees are undirected graphs. To represent this, and for use in many applications, every node stores a pointer to its parent.

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

Example: the following code snippet creates a (simplified) binary tree with the same structure as the one in Exercise 2 (e). For this tree, the call `height(root)` returns the correct height. Your task is to create an example on which the algorithm does not work correctly, and then fix the algorithm.

```py
leaf1 = BinaryTreeNode(1)
leaf2 = BinaryTreeNode(1)
leaf3 = BinaryTreeNode(1)
inner1 = BinaryTreeNode(1, left=leaf1, right=leaf2)
root = BinaryTreeNode(1, left=inner1, right=leaf3)
assert height(root) == 2, "The height of this tree should be 2"
```

### Solution

To discuss the solution, we first have to define the height of a node (even though it is clearly defined in the lecture's materials). The height of a node $x$ is the length of the longest downward path from $x$ to a leaf. Knowing this definition we can clearly see that the recursive formula in the implementation is correct.

The mistake in the implementation is the base case, which checks whether the node is a leaf. If the node is not a leaf, we recursively call the `height` function on both its left and right children, take the maximum of these values, and add 1 to this, which will be the height of the parameter node.

We can illustrate the problem with this implementation by calling the function on a tree that has at least one node with *exactly* one child, for example the tree in Exercise 2 (d):

```py
leaf1 = BinaryTreeNode(1)
leaf2 = BinaryTreeNode(1)
leaf3 = BinaryTreeNode(1)
inner1 = BinaryTreeNode(1, left=leaf1)
inner2 = BinaryTreeNode(1, left=leaf2, right=leaf3)
root = BinaryTreeNode(1, left=inner1, right=inner2)
assert height(root) == 2, "The height of this tree should be 2"
```

Because `inner1` is not a leaf, the recursive calls will happen, however, its `right` pointer is `None`. The recursive call to this missing child will start by checking whether it is a leaf, first by checking its `.left` property, but the value `None` does not have this property, so we will get the following error: `AttributeError: 'NoneType' object has no attribute 'left'`, which is similar to the `NullPointerException` in Java.

Fixing this issue is fairly simple, but serves as a very important lesson in writing recursive functions that traverse binary trees: the `None` value should be handled as at least one of the base cases.

In this case, we can remove the leaf node base case, and focus on only the `None` node base case. In order to keep the height of leaf nodes as 0, we will set the `None` node's height as -1. This way, the recursive formula will return 0 as the height for a leaf node.

The fixed implementation of the `height` function is as follows:

```py
def height(node: BinaryTreeNode) -> int:
    if node is None: return -1

    return max(height(node.left), height(node.right)) + 1
```

---

### Exercise 5

When is a binary tree *height-balanced*? Implement a *recursive* algorithm that checks whether a binary tree (given by its root node) is balanced. Use the `height` function from Exercise 4, along with the following outline:

```py
def is_balanced(root: BinaryTreeNode) -> bool:
    # TODO
```

### Solution

A binary tree is height-balanced if and only if the following holds true for every node $x$ in the tree:

```math
|\text{height}(x.\text{left}) - \text{height}(x.\text{right})| \leq 1
```

In other words, for every node, the difference between the height of its children must not exceed 1.

A very simple implementation to check this condition is as follows:

```py
def is_balanced(root: BinaryTreeNode) -> bool:
    if root is None: return True

    return (is_balanced(root.left) and
            is_balanced(root.right) and
            abs(height(root.left) - height(root.right)) <= 1)
```

The first recursive call checks whether the node's left subtree contains a node that does not satisfy the condition above, the second recursive call does the same for the right subtree, and the third part of the formula checks if the parameter node is height-balanced.

The keen-eyed will notice that this implementation, while simple, is not optimal. This is because both subtrees are being traversed twice, once with the `is_balanced` calls, and once with the `height` calls. The time complexity of this algorithm is $O(n^2)$, where $n$ is the number of nodes in the tree.

A more efficient implementation computes the height and checks if the subtree is balanced in a single traversal, by combining the two functions:

```py
from typing import Tuple


def _height_and_balanced(node: BinaryTreeNode) -> Tuple[int, bool]:
    if node is None: return (-1, True)

    left_height, left_balanced = _height_and_balanced(node.left)
    right_height, right_balanced = _height_and_balanced(node.right)

    node_height = max(left_height, right_height) + 1
    node_balanced = (left_balanced and
                     right_balanced and
                     abs(left_height - right_height) <= 1)

    return (node_height, node_balanced)


def is_balanced(root: BinaryTreeNode) -> bool:
    return _height_and_balanced(root)[1]
```

The time complexity of this implementation is $O(n)$.

---

### Exercise 6

What is a binary search tree (BST)? What are the algorithms for insertion, search, deletion, predecessor/successor, min/max? To demonstrate how these algorithms work, start with the following binary search tree:

![Initial BST](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/07_trees/img/07_trees_exercise06.svg)

and execute the following operations subsequently (i.e. execute each operation on the tree that results from the previous operation):
1. Insertion: `insert(20)`, `insert(11)`, `insert(27)`, `insert(40)`
2. Search / contains: `contains(11)`, `contains(35)`
3. Minimum, maximum: `min()`, `max()`
4. Successor: `successor(22)`, `successor(11)`, `successor(40)`
5. Deletion: `delete(40)`, `delete(8)`, `delete(22)`

What is the time complexity of these operations?

### Solution

1\. After the insertion operations:

![BST after insertions](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/07_trees_exercise06_solutions_part01.svg)

2\. The order in which we traverse the nodes:
- `contains(11)`: 22 &rarr; 17 &rarr; 2 &rarr; 8 &rarr; 11
- `contains(35)`: 22 &rarr; 36 &rarr; 32 &rarr; `None` (right child of the node with the key 32)

3\. To find the minimum node, we always go left until the next step would be the `None` node. Finding the maximum node is the same, but mirrored (we always go right).

4\.
- `successor(22)`: the node with the key 22 has a right child, so the successor of 22 is the minimum in its right subtree, which is 27
- `successor(11)`: the node with the key 11 does not have a right child, so its successor is its first ancestor with a key larger than 11, which is 17
- `successor(40)`: same as `successor(11)`, however, no ancestor's key is larger than 40, so it does not have a successor (note: 40 is the maximum key in the tree)

5\. After deleting 40:

![After deleting 40](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/07_trees_exercise06_solutions_part02.svg)


After deleting 8:

![After deleting 8](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/07_trees_exercise06_solutions_part03.svg)

After deleting 22:

![After deleting 22](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/07_trees_exercise06_solutions_part04.svg)


---

### Exercise 7

Below, you are given a half-complete implementation of a binary tree that implements a **set** that stores integers. Implement the following member functions:
- `insert`: inserts a key into the BST
- `contains`: returns `True` if the given key is in the BST, and `False` otherwise
- `min`: returns the minimum key in the BST
- `max`: returns the maximum key in the BST

Make sure to correctly set not only the children pointers, but the parent pointers as well. Test your implementation on the tree and the operations of Exercise 6, which are given in the file `exercise_07.py`.

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


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key: int) -> None:
        """Inserts a new key into the tree."""
        # TODO
        pass

    def contains(self, key: int) -> bool:
        """Returns True if `key` is in the tree, and False otherwise."""
        # TODO
        pass

    def min(self) -> int:
        """Returns the minimum key in the tree."""
        # TODO
        pass

    def max(self) -> int:
        """Returns the maximum key in the tree."""
        # TODO
        pass

    def delete(self, key) -> None:
        """Deletes a key from the tree."""
        curr = self.root

        # Find the node that contains the key
        while curr is not None:
            if key == curr.key: break
            elif key < curr.key: curr = curr.left
            else: curr = curr.right

        # If the key is in the tree, delete the node that cointains it
        if curr is not None:
            self._delete_node(curr)

    def _delete_node(self, node: BinaryTreeNode) -> None:
        """Deletes the given node from the tree."""
        if node.left is None:
            self._replace(node, node.right)
        elif node.right is None:
            self._replace(node, node.left)
        else:
            successor = self._successor_node(node)
            if successor != node.right:
                self._replace(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._replace(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _successor_node(self, node: BinaryTreeNode) -> BinaryTreeNode:
        """Returns the successor of the given node."""
        if node.right is not None:
            curr = node.right
            while curr.left is not None: curr = curr.left
            return curr
        else:
            curr = node.parent
            while curr is not None:
                if curr.key > node.key: return curr
                else: curr = curr.parent
            return None

    def _replace(self, u: BinaryTreeNode, v: BinaryTreeNode) -> None:
        """Replaces the subtree rooted at `u` with the subtree rooted at `v`."""

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
        if v is not None:
            v.parent = u.parent
```

### Solution

The implementation of `contains`, `min`, and `max` should be trivial. The only edge-case we have to pay attention to in all of these methods is the empty tree.

The `insert` operation is a bit more involved. Its implementation is very similar to Exercise 3 of last week, where we implemented the index-based insertion operation in linked lists. There, we found the preceding element (at `index - 1`) and inserted the new element as its next neighbor. Here, we will find the parent of the new key (according to the search tree property), and insert the new node as its child.

The complete implementation is as follows:

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


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key: int) -> None:
        """Inserts a new key into the tree."""

        # If the tree is empty, create a new root
        if self.root is None:
            self.root = BinaryTreeNode(key)
        else:
            parent = None
            child = self.root
            while child is not None:
                parent = child

                # In sets, duplication is not allowed
                if key == child.key: return

                # If the key is less than the current node's key, go left
                if key < child.key:
                    child = child.left

                # Otherwise, go right
                else:
                    child = child.right

            # Insert the key as a new node in the tree
            new_node = BinaryTreeNode(key, parent=parent)
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

    def contains(self, key: int) -> bool:
        """Returns True if `key` is in the tree, and False otherwise."""
        curr = self.root
        while curr is not None:
            if key == curr.key: return True
            elif key < curr.key: curr = curr.left
            else: curr = curr.right
        return False

    def min(self) -> int:
        """Returns the minimum key in the tree."""

        # There is no minimum in the empty tree
        if self.root == None: return None

        # Go left while we can
        curr = self.root
        while curr.left is not None:
            curr = curr.left

        return curr.key

    def max(self) -> int:
        """Returns the maximum key in the tree."""

        # There is no maximum in the empty tree
        if self.root == None: return None

        # Go right while we can
        curr = self.root
        while curr.right is not None:
            curr = curr.right

        return curr.key

    def delete(self, key) -> None:
        """Deletes a key from the tree."""
        curr = self.root

        # Find the node that contains the key
        while curr is not None:
            if key == curr.key: break
            elif key < curr.key: curr = curr.left
            else: curr = curr.right

        # If the key is in the tree, delete the node that cointains it
        if curr is not None:
            self._delete_node(curr)

    def _delete_node(self, node: BinaryTreeNode) -> None:
        """Deletes the given node from the tree."""
        if node.left is None:
            self._replace(node, node.right)
        elif node.right is None:
            self._replace(node, node.left)
        else:
            successor = self._successor_node(node)
            if successor != node.right:
                self._replace(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._replace(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _successor_node(self, node: BinaryTreeNode) -> BinaryTreeNode:
        """Returns the successor of the given node."""
        if node.right is not None:
            curr = node.right
            while curr.left is not None: curr = curr.left
            return curr
        else:
            curr = node.parent
            while curr is not None:
                if curr.key > node.key: return curr
                else: curr = curr.parent
            return None

    def _replace(self, u: BinaryTreeNode, v: BinaryTreeNode) -> None:
        """Replaces the subtree rooted at `u` with the subtree rooted at `v`."""

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
        if v is not None:
            v.parent = u.parent
```
