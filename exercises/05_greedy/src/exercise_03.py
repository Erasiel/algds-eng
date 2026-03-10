from typing import List


def car_trip(n: int, distances: List[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = car_trip(10, [5, 7, 4, 3])
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = car_trip(2, [1])
        assert output == 0
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
