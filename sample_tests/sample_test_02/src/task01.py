from typing import Any, Optional


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


def num_nodes_at_depth(root: BinaryTreeNode, k: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
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
