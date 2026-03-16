from typing import Set


def coin_change_possibilities(F: int, P: Set[int], n: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    assert coin_change_possibilities(10, {1}, 1) == 1
    assert coin_change_possibilities(10, {1, 5}, 2) == 3
    assert coin_change_possibilities(10, {1, 5, 7}, 3) == 4
