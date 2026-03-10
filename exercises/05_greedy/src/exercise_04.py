from typing import List


def interval_cover(K: List[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = interval_cover([0.1, 0.3, 0.7, 1.2, 1.3, 1.4, 1.6, 1.8])
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = interval_cover([0.0, 1.0])
        assert output == 1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = interval_cover([])
        assert output == 0
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
