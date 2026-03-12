def reverse(string: str, idx: int = 0) -> str:
    if idx >= len(string): return ""
    return reverse(string, idx + 1) + string[idx]


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = reverse("apple")
        assert output == "elppa"
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: 'elppa', actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = reverse("")
        assert output == ""
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: '', actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
