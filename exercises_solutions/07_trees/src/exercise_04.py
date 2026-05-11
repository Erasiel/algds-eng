from typing import Optional, Any


class BinaryTreeNode:
    def __init__(self,
                 key: Any,
                 left: Optional["BinaryTreeNode"] = None,
                 right: Optional["BinaryTreeNode"] = None
    ) -> None:
        self.key = key
        self.left = left
        self.right = right


# Note: the fixed implementation can be found in exercise_04.py
def height(node: BinaryTreeNode) -> int:
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

    from utils import binary_tree_to_string

    # An input on which the algorithm is incorrect (Exercise 01 (d)):
    leaf1 = BinaryTreeNode("D")
    leaf2 = BinaryTreeNode("E")
    leaf3 = BinaryTreeNode("F")
    inner1 = BinaryTreeNode("B", left=leaf1)
    inner2 = BinaryTreeNode("C", left=leaf2, right=leaf3)
    root = BinaryTreeNode("A", left=inner1, right=inner2)
    print(binary_tree_to_string(root))
    print(height(root)) # Error
