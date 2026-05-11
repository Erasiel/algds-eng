from typing import Any


class DoubleStack:
    def __init__(self, n: int) -> None:
        self.container = [None] * n
        self.stack1_index = 0
        self.stack2_index = n - 1

    def push_stack1(self, key: Any) -> None:
        """Inserts a key at the top of the first stack"""
        self.container[self.stack1_index] = key
        self.stack1_index += 1

    def push_stack2(self, key: Any) -> None:
        """Inserts a key at the top of the second stack"""
        self.container[self.stack2_index] = key
        self.stack2_index -= 1

    def pop_stack1(self) -> Any:
        """Deletes the key at the top of the first stack."""
        if self.empty_stack1():
            raise ValueError("Cannot pop from an empty Stack #1!")

        deleted_element = self.top_stack1()
        self.container[self.stack1_index - 1] = None
        self.stack1_index -= 1
        return deleted_element

    def pop_stack2(self) -> Any:
        """Deletes the key at the top of the second stack."""
        if self.empty_stack2():
            raise ValueError("Cannot pop from an empty Stack #2!")

        deleted_element = self.top_stack2()
        self.container[self.stack2_index + 1] = None
        self.stack2_index += 1
        return deleted_element

    def top_stack1(self) -> Any:
        """Returns the key at the top of the first stack."""
        if self.empty_stack1():
            raise ValueError("Cannot query the top of an empty Stack #1!")

        return self.container[self.stack1_index - 1]

    def top_stack2(self) -> Any:
        """Returns the key at the top of the second stack."""
        if self.empty_stack2():
            raise ValueError("Cannot query the top of an empty Stack #2!")

        return self.container[self.stack2_index + 1]

    def empty_stack1(self) -> bool:
        """Returns whether the first stack is empty."""
        return self.stack1_index == 0

    def empty_stack2(self) -> bool:
        """Returns whether the second stack is empty."""
        return self.stack2_index == len(self.container) - 1

if __name__ == "__main__":
    ds = DoubleStack(n=10)
    ds.push_stack1(1)
    ds.push_stack1(2)
    ds.push_stack2(3)
    ds.push_stack2(4)
    ds.push_stack2(5)
    print(ds.top_stack1()) # 2
    print(ds.top_stack2()) # 5
    print(ds.pop_stack1()) # 2
    print(ds.pop_stack2()) # 5
    print(ds.pop_stack2()) # 4
    print(ds.top_stack1()) # 1
    print(ds.top_stack2()) # 3
    print("-"*10)
    print(ds.empty_stack1()) # False
    ds.pop_stack1()
    print(ds.empty_stack1()) # True
    print("-"*5)
    print(ds.empty_stack2()) # False
    ds.pop_stack2()
    print(ds.empty_stack2()) # True
    ds.top_stack2()
