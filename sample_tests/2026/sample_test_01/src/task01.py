# Name:
# Neptun:
# h-id:


from typing import List


def number_of_ones(arr: List[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = number_of_ones([0, 0])
        assert output == 0
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = number_of_ones([1, 1])
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = number_of_ones([0, 0, 1, 1, 1, 1, 1])
        assert output == 5
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = number_of_ones([1, 1, 1, 1, 1, 0, 0])
        assert output == 5
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()
