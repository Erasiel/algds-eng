def invert_binary_string(string: str) -> str:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = invert_binary_string("00101")
        assert output == "11010"
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: '11010', actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = invert_binary_string("1100")
        assert output == "0011"
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: '0011', actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = invert_binary_string("")
        assert output == ""
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! "
              f"Expected output: '', actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
