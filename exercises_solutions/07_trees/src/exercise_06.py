from typing import Optional, Any, Tuple


class BinaryTreeNode:
    def __init__(self,
                 key: Any,
                 left: Optional["BinaryTreeNode"] = None,
                 right: Optional["BinaryTreeNode"] = None
    ) -> None:
        self.key = key
        self.left = left
        self.right = right


def _height_and_balanced(node: BinaryTreeNode) -> Tuple[int, bool]:
    # The empty subtree has a height of -1 and it's balanced
    if node is None: return (-1, True)

    # Recursively calculate the height of both subtrees and whether they are
    # balanced
    left_height, left_balanced = _height_and_balanced(node.left)
    right_height, right_balanced = _height_and_balanced(node.right)

    # Calculate and return the height of the current node, and whether the
    # subtree rooted at the current node is balanced
    node_height = max(left_height, right_height) + 1
    node_balanced = (left_balanced and
                     right_balanced and
                     abs(left_height - right_height) <= 1)

    return (node_height, node_balanced)


def is_balanced(root: BinaryTreeNode) -> bool:
    # Combine height and is_balanced into one function so that we don't have
    # to traverse the same subtree multiple times. For a subtree, this
    # function returns two things: the height of the subtree (int) and if
    # every node in the subtree is balanced (bool)
    return _height_and_balanced(root)[1]


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
