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


def is_balanced(root: BinaryTreeNode) -> bool:
    # TODO - implement is_balanced so that its running time is O(n)
    pass


if __name__ == "__main__":
    from utils import binary_tree_to_string

    # Exercise 2 (e)
    leaf1 = BinaryTreeNode("E")
    leaf2 = BinaryTreeNode("D")
    leaf3 = BinaryTreeNode("C")
    inner1 = BinaryTreeNode("B", left=leaf1, right=leaf2)
    root = BinaryTreeNode("A", left=inner1, right=leaf3)

    print("The tree for test case #1:")
    print(binary_tree_to_string(root))

    # TEST #1
    try:
        output = is_balanced(root)
        assert output == True
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! The first tree is height-balanced."
              f"Expected output: True, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")


    # Exercise 2 (b)
    leaf = BinaryTreeNode("D")
    inner1 = BinaryTreeNode("C", left=leaf)
    inner2 = BinaryTreeNode("B", left=inner1)
    root = BinaryTreeNode("A", left=inner2)

    print("The tree for test case #2:")
    print(binary_tree_to_string(root))

    # TEST #2
    try:
        output = is_balanced(root)
        assert output == False
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! The first tree is height-balanced."
              f"Expected output: False, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
