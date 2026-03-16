# Name:
# Neptun:
# h-id:


from typing import Set


def coin_change_possibilities(F: int, P: Set[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = coin_change_possibilities(10, {1})
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = coin_change_possibilities(10, {1, 5})
        assert output == 3
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = coin_change_possibilities(10, {1, 5, 7})
        assert output == 4
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = coin_change_possibilities(10, {3, 6, 9})
        assert output == 0
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()

    # TEST #5
    try:
        output = coin_change_possibilities(0, {1, 5, 7})
        assert output == 1
        print("Test #5 passed!")
    except AssertionError:
        print(f"Test #5 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #5:\n{exception}")
        traceback.print_exc()

