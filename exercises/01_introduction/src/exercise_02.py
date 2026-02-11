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
    except:
        print("Test #1 failed! "
              f"Expected output: True, actual output: {output}")

    # TEST #2
    try:
        output = interval_contains(1, 3, 3)
        assert output == True
        print("Test #2 passed!")
    except:
        print("Test #2 failed! "
              f"Expected output: True, actual output: {output}")

    # TEST #3
    try:
        output = interval_contains(1, 3, 4)
        assert output == False
        print("Test #3 passed!")
    except:
        print("Test #3 failed! "
              f"Expected output: False, actual output: {output}")

    # TEST #4
    try:
        output = interval_contains(1, 3, -1)
        assert output == False
        print("Test #4 passed!")
    except:
        print("Test #4 failed! "
              f"Expected output: False, actual output: {output}")
