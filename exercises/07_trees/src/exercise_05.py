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


def is_balanced(root: BinaryTreeNode) -> bool:
    # TODO
    pass


if __name__ == "__main__":
    # Exercise 2 (e)
    leaf1 = BinaryTreeNode("E")
    leaf2 = BinaryTreeNode("D")
    leaf3 = BinaryTreeNode("C")
    inner1 = BinaryTreeNode("B", left=leaf1, right=leaf2)
    root = BinaryTreeNode("A", left=inner1, right=leaf3)
    assert is_balanced(root) == True, "The first tree should be balanced"

    # Exercise 2 (b)
    leaf = BinaryTreeNode("D")
    inner1 = BinaryTreeNode("C", left=leaf)
    inner2 = BinaryTreeNode("B", left=inner1)
    root = BinaryTreeNode("A", left=inner2)
    assert is_balanced(root) == False, "The second tree should not be balanced"
