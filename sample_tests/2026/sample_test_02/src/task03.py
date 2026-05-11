from typing import List


def repeating_row_filter(mtx: List[List[int]]) -> List[List[int]]:
    # TODO
    pass


if __name__ == "__main__":

    import traceback

    output = None

    # TEST #1
    try:
        output = repeating_row_filter([[1], [0]])
        expected = [[1], [0]]
        assert output == expected
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: {expected}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = repeating_row_filter([[1, 1], [1, 1]])
        expected = [[1, 1]]
        assert output == expected
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: {expected}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = repeating_row_filter([[0, 0, 1, 1],
                                       [1, 0, 1, 0],
                                       [1, 0, 1, 0],
                                       [1, 1, 1, 1],
                                       [0, 0, 1, 1]])
        expected = [[0, 0, 1, 1],
                    [1, 0, 1, 0],
                    [1, 1, 1, 1]]
        assert output == expected
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: {expected}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()
