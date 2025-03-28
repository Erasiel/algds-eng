from typing import List, Union


# This solution uses one of the Stack implementations from Week 6 to emphasize
# that this task should be solved by using a stack. Of course, using the
# `append` and `pop` operations of a built-in `list` is also fine.


class Stack:
    def __init__(self):
        self.container = list()

    def push(self, key: float) -> None:
        """Inserts the key at the top of the stack."""
        self.container.append(key)

    def pop(self) -> float:
        """Deletes the key at the top of the stack."""

        # If the stack is empty, raise an error
        if len(self.container) == 0: raise ValueError("Empty stack!")

        # Save the top item for the return statement before deleting it
        top = self.container.pop()
        return top

    def top(self) -> float:
        """Returns the key at the top of the stack."""

        if len(self.container) == 0: raise ValueError("Empty stack!")

        return self.container[-1]


def rpn_eval(rpn: List[Union[str, float]], n: int) -> float:

    # The empty list is also a correct RPN
    if len(rpn) == 0: return 0

    stack = Stack()
    for elem in rpn:

        # Push numbers in the RPN to the stack
        if type(elem) == float:
            stack.push(elem)

        # Execute arithmetic operations on the top two elements of the stack
        else:
            right = stack.pop()
            left = stack.pop()
            if elem == "+":   stack.push(left + right)
            elif elem == "-": stack.push(left - right)
            elif elem == "*": stack.push(left * right)
            else:             stack.push(left / right)

    return stack.top()


if __name__ == "__main__":
    assert rpn_eval([5.0, 4.0, "*", 3.0, "+"], 5) == 23
    assert rpn_eval([5.0, 4.0, 3.0, "*", "+"], 5) == 17
    assert rpn_eval([5.0, 4.0, "*", 3.0, 2.0, "*", "+"], 7) == 26
    assert rpn_eval([5.0, 3.0, "+", 4.0, 2.0, "-", "/"], 7) == 4
    assert rpn_eval([1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"], 11) == 5
