def interval_contains(a: int, b: int, c: int) -> bool:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = interval_contains(1, 3, 2)
        assert output == True
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: True, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = interval_contains(1, 3, 3)
        assert output == True
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: True, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = interval_contains(1, 3, 4)
        assert output == False
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! "
              f"Expected output: False, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = interval_contains(1, 3, -1)
        assert output == False
        print("Test #4 passed!")
    except AssertionError:
        print("Test #4 failed! "
              f"Expected output: False, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
