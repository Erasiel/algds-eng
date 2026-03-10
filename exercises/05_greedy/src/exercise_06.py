from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = knapsack(C=3, items=[Item(value=2, weight=1),
                                      Item(value=3, weight=2),
                                      Item(value=4, weight=3)])
        assert output == 5
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = knapsack(C=12, items=[Item(value=5, weight=3),
                                       Item(value=4, weight=4),
                                       Item(value=5, weight=2),
                                       Item(value=5, weight=6),
                                       Item(value=4, weight=5)])
        assert output == 15
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: , actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
