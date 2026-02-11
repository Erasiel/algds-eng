def func(a, b, c):
    return a[0] + b[0] * c


if __name__ == "__main__":
    output = None

    # Test #1
    try:
        output = func([0, 1, 2], [1, 2, 3], 4)
        assert output == 4
        print("Test #1 passed!")
    except:
        print(f"Test #1 failed! Expected output: 4, actual output: {output}")

    # Test #2
    try:
        output = func([2, 3], [4, 5, 6], -1)
        assert output == -2
        print("Test #2 passed!")
    except:
        print(f"Test #2 failed! Expected output: 4, actual output: {output}")
