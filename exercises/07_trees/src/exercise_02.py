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


def num_leaf_nodes(node: BinaryTreeNode) -> int:
    # TODO
    pass



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
        output = num_leaf_nodes(root)
        assert output == 3
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! The tree has 3 leaf nodes."
              f"Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_leaf_nodes(inner1)
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! The subtree rooted at B has 2 leaf nodes."
              f"Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_leaf_nodes(leaf3)
        assert output == 1
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! The subtree rooted at C has 1 leaf node."
              f"Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")