from typing import Any

from exercise_02 import Stack


class Queue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, key: Any) -> None:
        """Inserts the key at the end of the queue."""
        self.stack1.push(key)

    def dequeue(self) -> Any:
        """Deletes the key at the start of the queue."""
        if self.empty():
            raise ValueError("You can't dequeue from an empty queue!")

        # Move all keys from stack1 to stack2
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())

        dequeued_element = self.stack2.pop()

        # Move all keys back to stack1
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

        return dequeued_element

    def first(self) -> Any:
        """Returns the key at the start of the queue."""
        if self.empty():
            raise ValueError("You can't query the first element of an empty queue!")

        # Move all keys from stack1 to stack2
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())

        first_elemet = self.stack2.top()

        # Move all keys back to stack1
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

        return first_elemet

    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()



if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.first())    # 1
    print(queue.dequeue())  # 1
    print(queue.dequeue())  # 2
    print(queue.dequeue())  # 3
    print(queue.empty())    # False
    print(queue.dequeue())  # 4
    print(queue.empty())    # True
    print(queue.dequeue())  # error
