def stairs(n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    return stairs(n - 1) + stairs(n - 2)


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = stairs(1)
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = stairs(3)
        assert output == 3
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
