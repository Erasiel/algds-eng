from typing import Any


class Stack:
    def __init__(self):
        self.container = list()
        self.min_stack = list()

    def push(self, key: Any) -> None:
        """Inserts the key at the top of the stack."""
        if self.empty():
            self.container.append(key)
            self.min_stack.append(key)
        else:
            self.container.append(key)
            prev_min = self.min()
            self.min_stack.append(min(prev_min, key))


    def pop(self) -> Any:
        """Deletes the key at the top of the stack."""
        if self.empty():
            raise ValueError("You can't pop from an empty stack!")

        self.min_stack.pop()
        return self.container.pop()

    def top(self) -> Any:
        """Returns the key at the top of the stack."""
        if self.empty():
            raise ValueError("You can't query the top of an empty stack!")

        return self.container[-1]

    def min(self) -> Any:
        """Returns the minimum key in the stack."""
        if self.empty():
            raise ValueError("You can't query the minimum of an empty stack!")

        return self.min_stack[-1]

    def empty(self) -> bool:
        return len(self.container) == 0


if __name__ == "__main__":
    ds = Stack()
    ds.push(8)
    ds.push(7)
    ds.push(9)
    ds.push(5)
    ds.push(6)
    ds.push(6)
    ds.push(4)
    print(ds.top()) # 4
    print(ds.min()) # 4
    print("-" * 10)
    ds.pop()
    print(ds.min()) # 5