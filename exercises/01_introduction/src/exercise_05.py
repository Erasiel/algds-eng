def num_unique_characters(s: str) -> str:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = num_unique_characters("00101")
        assert output == 2
        print("Test #1 passed!")
    except:
        print("Test #1 failed! "
              f"Expected output: 2, actual output: {output}")

    # TEST #2
    try:
        output = num_unique_characters("12345432123454321")
        assert output == 5
        print("Test #2 passed!")
    except:
        print("Test #2 failed! "
              f"Expected output: 5, actual output: {output}")

    # TEST #3
    try:
        output = num_unique_characters("")
        assert output == 0
        print("Test #3 passed!")
    except:
        print("Test #3 failed! "
              f"Expected output: 0, actual output: {output}")
