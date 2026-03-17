from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def value_per_weight(item: Item) -> float:
    return item.value / item.weight


def knapsack(C: int, items: List[Item]) -> int:
    # Greedy choice: pick the item with the largest value / weight and add it
    # to the knapsack. If we need to break an item, it is guaranteed to be the
    # final item before the knapsack is full.

    # Start by sorting the items by their value / weight coefficient in
    # descending order. This makes the 'select the largest value / weight
    # item' part easy, as we just have to traverse the items in sorted order.
    sorted_items = sorted(items, key=value_per_weight, reverse=True)
    remaining_capacity = C
    total_value = 0

    for item in sorted_items:
        # Can we use the complete item?
        if item.weight <= remaining_capacity:
            remaining_capacity -= item.weight
            total_value += item.value

        # If there is unused capacity in the knapsack, but the whole item does
        # not fit, break it and fill the knapsack.
        else:
            total_value += remaining_capacity * value_per_weight(item)
            remaining_capacity = 0

        if remaining_capacity == 0: break

    return total_value


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
        assert output == 16.5
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 16.5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
