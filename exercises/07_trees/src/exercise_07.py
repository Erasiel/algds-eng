from typing import Optional

from utils import binary_tree_to_string


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
        # If the node has a non-empty right subtree, its successor is the
        # leftmost node in its right subtree
        if node.right is not None:
            curr = node.right
            while curr.left is not None: curr = curr.left
            return curr

        # Otherwise, the first ancestor with a key lower than the node's key is
        # its successor
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

    def __str__(self) -> str:
        lines = binary_tree_to_string(self.root, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))


if __name__ == "__main__":
    # Start by re-creating the initial tree from Exercise 6
    bst = BinarySearchTree()
    bst.insert(22)
    bst.insert(17)
    bst.insert(36)
    bst.insert(2)
    bst.insert(32)
    bst.insert(8)
    print(f"The initial tree from Exercise 6:\n{bst}")

    # Insert operations from Exercise 6
    bst.insert(20)
    print(f"After inserting 20:\n{bst}")
    bst.insert(11)
    print(f"After inserting 11:\n{bst}")
    bst.insert(27)
    print(f"After inserting 27:\n{bst}")
    bst.insert(40)
    print(f"After inserting 40:\n{bst}")

    # Contains operations from Exercise 6
    print(f"contains(11): {bst.contains(11)}")
    print(f"contains(35): {bst.contains(35)}")

    # Min / Max
    print(f"min: {bst.min()}")
    print(f"max: {bst.max()}")

    # Deletes from Exercise 6
    bst.delete(40)
    print(f"After deleting 40:\n{bst}")

    bst.delete(8)
    print(f"After deleting 8:\n{bst}")

    bst.delete(22)
    print(f"After deleting 22:\n{bst}")
