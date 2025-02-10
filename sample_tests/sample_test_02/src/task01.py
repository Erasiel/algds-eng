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


def num_nodes_at_depth(root: BinaryTreeNode, k: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    leaf1 = BinaryTreeNode(1)
    leaf2 = BinaryTreeNode(1)
    leaf3 = BinaryTreeNode(1)
    inner1 = BinaryTreeNode(1, left=leaf1, right=leaf2)
    root = BinaryTreeNode(1, left=inner1, right=leaf3)

    assert num_nodes_at_depth(root, 0) == 1
    assert num_nodes_at_depth(root, 1) == 2
    assert num_nodes_at_depth(root, 2) == 2
