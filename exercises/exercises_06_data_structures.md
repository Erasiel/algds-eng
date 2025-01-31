# Elementary Data Structures

### Exercise 1

What is an abstract data structure? Briefly describe the following abstract data structures:
- List
- Set
- Stack
- Queue
- Priority Queue

---

### Exercise 2

What is the difference between a `List` implementation that uses an array (e.g. `java.util.ArrayList` in Java or `std::vector` in C++) and a linked list implementation? When is one more effective than the other? Is one better than the other?

Which variant is used in Python?

---

### Exercise 3

Implement a doubly linked list that stores strings using the outline below. For simplicity, feel free to ignore negative indices in all index-based methods.

```py
class LinkedListItem:
    def __init__(self,
                 key: str,
                 prev: Optional["LinkedListItem"] = None,
                 next: Optional["LinkedListItem"] = None
    ) -> None:
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        # TODO
        pass

    def insert(self, key: str) -> None:
        """Inserts an element at the beginning of the list."""
        # TODO
        pass

    def find(self, key: str) -> int:
        """Finds the index of the key or -1 if the key is not in the list."""
        # TODO
        pass

    def get(self, index: int) -> str:
        """Returns the key at the specified index in the list."""
        # TODO
        pass

    def delete_key(self, key: str) -> str:
        """Deletes the first occurence of the key from the list."""
        # TODO
        pass

    def delete_index(self, index: int) -> str:
        """Deletes the key at the specified index."""
        # TODO
        pass
```

---

### Exercise 4

Implement a stack that stores strings using the `LinkedList` implementation from the previous exercise as the underlying container. Make sure all methods run in $O(1)$ time. Use the following outline:

```py
class Stack:
    def __init__(self):
        # TODO
        self.container = LinkedList()
        pass

    def push(self, key: str) -> None:
        """Inserts the key at the top of the stack."""
        # TODO
        pass

    def pop(self) -> str:
        """Deletes the key at the top of the stack."""
        # TODO
        pass

    def top(self) -> str:
        """Returns the key at the top of the stack."""
        # TODO
        pass
```

How would you modify the solution to implement a queue instead of a stack?

---

### Exercise 5

Simulate a queue (FIFO list) using the `Stack` implementation from the previous exercise. You can't use any other data structures. Use the following outline:

```py
class Queue:
    def __init__(self) -> None:
        # TODO
        pass

    def enqueue(self, key: str) -> None:
        """Inserts the key at the end of the queue."""
        # TODO
        pass

    def dequeue(self) -> str:
        """Deletes the key at the start of the queue."""
        # TODO
        pass

    def first(self) -> str:
        """Returns the key at the start of the queue."""
        # TODO
        pass
```

---

### Exercise 6

Simulate *two* stacks that store strings with one fix-sized array of length $n$. We know upfront that the number of keys contained in the data structure (i.e. in both stacks together) will never exceed $n$. Make sure the time complexity of all stack operations remain $O(1)$. Use the following outline:

```py
class DoubleStack:
    def __init__(self, n: int) -> None:
        self.container = [None] * n

    def push_stack1(self, key: str) -> None:
        """Inserts a key at the top of the first stack"""
        # TODO
        pass

    def push_stack2(self, key: str) -> None:
        """Inserts a key at the top of the second stack"""
        # TODO
        pass

    def pop_stack1(self) -> str:
        """Deletes the key at the top of the first stack."""
        # TODO
        pass

    def pop_stack2(self) -> str:
        """Deletes the key at the top of the second stack."""
        # TODO
        pass

    def top_stack1(self) -> str:
        """Returns the key at the top of the first stack."""
        # TODO
        pass

    def top_stack2(self) -> str:
        """Returns the key at the top of the second stack."""
        # TODO
        pass
```

---

### Exercise 7

Modify a stack data structure that stores integers (e.g. the one from exercise 4) so that it implements the `min` operation (that returns the minimum element in the data structure) in $O(1)$ time. Make sure that the time complexity of all other stack operations (`push`, `pop`, `top`) remain $O(1)$ and you don't use more than $O(n)$ extra space. Use the following outline:

```py
class Stack:
    def __init__(self):
        # TODO
        pass

    def push(self, key: int) -> None:
        """Inserts the key at the top of the stack."""
        # TODO
        pass

    def pop(self) -> int:
        """Deletes the key at the top of the stack."""
        # TODO
        pass

    def top(self) -> int:
        """Returns the key at the top of the stack."""
        # TODO
        pass

    def min(self) -> int:
        """Returns the minimum key in the stack."""
        # TODO
        pass
```
