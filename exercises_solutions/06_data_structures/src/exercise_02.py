from typing import Any


class Stack:
    def __init__(self):
        self.container = list()

    def push(self, key: Any) -> None:
        """Inserts the key at the top of the stack."""
        self.container.append(key)

    def pop(self) -> Any:
        """Deletes the key at the top of the stack."""
        if self.empty():
            raise ValueError("You can't pop from an empty stack!")

        return self.container.pop()

    def top(self) -> Any:
        """Returns the key at the top of the stack."""
        if self.empty():
            raise ValueError("You can't query the top of an empty stack!")

        return self.container[-1]

    def empty(self) -> bool:
        return len(self.container) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(6)
    print(stack.pop()) # 6
    print(stack.pop()) # 4
    print(stack.pop()) # 3
    print(stack.empty()) # False
    stack.pop()
    print(stack.empty()) # True
    print(stack.top())
