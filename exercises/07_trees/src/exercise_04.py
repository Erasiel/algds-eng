from typing import Optional, Any


class BinaryTreeNode:
    def __init__(self,
                 key: Any,
                 parent: Optional["BinaryTreeNode"] = None,
                 left: Optional["BinaryTreeNode"] = None,
                 right: Optional["BinaryTreeNode"] = None
    ) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def height(node: BinaryTreeNode) -> int:
    # TODO no. 2: find and fix the mistake in the implementation
    if node.left is None and node.right is None:
        return 0

    return max(height(node.left), height(node.right)) + 1



if __name__ == "__main__":
    # Exercise 2 (e)
    leaf1 = BinaryTreeNode("E")
    leaf2 = BinaryTreeNode("D")
    leaf3 = BinaryTreeNode("C")
    inner1 = BinaryTreeNode("B", left=leaf1, right=leaf2)
    root = BinaryTreeNode("A", left=inner1, right=leaf3)
    assert height(root) == 2, "The height of this tree should be 2"

    # TODO no. 1: find an input on which the algorithm does not work correctly
