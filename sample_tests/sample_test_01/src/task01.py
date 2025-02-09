from typing import List


def number_of_ones(arr: List[int], n: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    assert number_of_ones([0, 0], 2) == 0
    assert number_of_ones([1, 1], 2) == 2
    assert number_of_ones([0, 0, 1, 1, 1, 1, 1], 7) == 5
    assert number_of_ones([1, 1, 1, 1, 1, 0, 0], 7) == 5
