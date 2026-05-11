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


if __name__ == "__main__":
    import traceback

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

    try:
        assert num_nodes_at_depth(root, 0) == 1
        assert num_nodes_at_depth(root, 1) == 2
        assert num_nodes_at_depth(root, 2) == 2
        assert num_nodes_at_depth(root, 3) == 0
        print(f"All cases of test #1 passed!")
    except AssertionError:
        print(f"One of the test cases of test #1 failed!")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

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

    try:
        assert num_nodes_at_depth(root, 0) == 1
        assert num_nodes_at_depth(root, 1) == 2
        assert num_nodes_at_depth(root, 2) == 3
        assert num_nodes_at_depth(root, 3) == 1
        assert num_nodes_at_depth(root, 4) == 0
        print(f"All cases of test #2 passed!")
    except AssertionError:
        print(f"One of the test cases of test #2 failed!")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()
