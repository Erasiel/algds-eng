from typing import List, Union


def rpn_eval(rpn: List[Union[str, float]]) -> float:
    # The empty list is also a correct RPN
    if len(rpn) == 0: return 0

    stack = list()

    for elem in rpn:

        # Push numbers in the RPN to the stack
        if type(elem) == float:
            stack.append(elem)

        # Execute arithmetic operations on the top two elements of the stack
        else:
            right = stack.pop()
            left = stack.pop()
            if elem == "+":   stack.append(left + right)
            elif elem == "-": stack.append(left - right)
            elif elem == "*": stack.append(left * right)
            else:             stack.append(left / right)

    return stack[-1]


if __name__ == "__main__":

    import traceback

    output = None

    # TEST #1
    try:
        output = rpn_eval([5.0, 4.0, "*", 3.0, "+"])
        assert output == 23
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 23, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = rpn_eval([5.0, 4.0, 3.0, "*", "+"])
        assert output == 17
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 17, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = rpn_eval([5.0, 4.0, "*", 3.0, 2.0, "*", "+"])
        assert output == 26
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 26, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = rpn_eval([5.0, 3.0, "+", 4.0, 2.0, "-", "/"])
        assert output == 4
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()

    # TEST #5
    try:
        output = rpn_eval([1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"])
        assert output == 5
        print("Test #5 passed!")
    except AssertionError:
        print(f"Test #5 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #5:\n{exception}")
        traceback.print_exc()
