def factorial(n: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = factorial(1)
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = factorial(2)
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = factorial(3)
        assert output == 6
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 6, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = factorial(0)
        assert output == 1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
