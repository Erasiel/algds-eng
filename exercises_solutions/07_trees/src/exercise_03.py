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


def height(node: BinaryTreeNode) -> int:
    # The empty subtree has a height of -1. With this base case, leaf nodes
    # will have a height of 0.
    if node is None: return -1

    # The height of a node is the longest downward path from the node to a
    # leaf. Recursively calculate the longest downward path from the two
    # children to leaf nodes, and add 1, which represents the edge from the
    # current node to its children.
    return max(height(node.left), height(node.right)) + 1


if __name__ == "__main__":
    # Exercise 1 (e)
    leaf1 = BinaryTreeNode("E")
    leaf2 = BinaryTreeNode("D")
    leaf3 = BinaryTreeNode("C")
    inner1 = BinaryTreeNode("B", left=leaf1, right=leaf2)
    root = BinaryTreeNode("A", left=inner1, right=leaf3)

    from utils import binary_tree_to_string
    print(f"The tree for test cases #1 - #3:")
    print(binary_tree_to_string(root))


    output = None

    # TEST #1
    try:
        output = height(root)
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! The height of the tree is 2."
              f"Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = height(inner1)
        assert output == 1
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! The height of the node B is 1."
              f"Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = height(leaf3)
        assert output == 0
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! The height of the leaf node C is 0."
              f"Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")