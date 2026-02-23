def survival(n: int, m: int, x: int, y: int, k: int) -> float:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = survival(1, 1, 1, 1, 1)
        assert output == 0
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = survival(2, 2, 1, 1, 1)
        assert output == 0.5
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0.5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
