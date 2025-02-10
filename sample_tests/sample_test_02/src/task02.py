from typing import List


def repeating_row_filter(mtx: List[List[int]],
                         n: int,
                         m: int
) -> List[List[int]]:
    # TODO
    pass


if __name__ == "__main__":
    mtx1 = [
        [1],
        [0]
    ]
    assert repeating_row_filter(mtx1, 2, 1) == [[1], [0]]

    mtx2 = [
        [1, 1],
        [1, 1]
    ]
    assert repeating_row_filter(mtx2, 2, 2) == [[1, 1]]

    mtx3 = [
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
    ]
    assert repeating_row_filter(mtx3, 5, 4) == [[0, 0, 1, 1],
                                                [1, 0, 1, 0],
                                                [1, 1, 1, 1]]

