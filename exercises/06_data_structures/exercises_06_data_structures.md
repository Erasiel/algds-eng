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

What is the difference between a `List` implementation that uses a direct access array (e.g. `java.util.ArrayList` in Java or `std::vector` in C++) and a linked list implementation? When is one more effective than the other? Is one better than the other?

Which variant is used in Python?

---

### Exercise 3

The following code snippet cointains a half-complete implementation of a doubly linked list that stores strings. The following methods are implemented:
- `insert`: inserts a key at the beginning of the list
- `delete`: deletes the first occurence of a key
- `search`: returns the index of the given key
- `get`: returns the key at the given index

An example usage of the implementation is included in the code snippet.

Your task is to implement the following methods:
- `insert_index`: inserts a key at the given index
- `delete_index`: deletes the key at the given index

Feel free to take inspiration from the already implemented methods.

```py
from typing import Optional


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
        self.head = None
        self.length = 0

    def insert(self, key: str) -> None:
        """Inserts an element at the beginning of the list."""

        # Wrap the new key in a LinkedListItem
        new_item = LinkedListItem(key)

        # If the list is not empty, set the new item's `next` pointer to the
        # current first item and the current first item's `prev` pointer to the
        # new item
        if self.head is not None:
            new_item.next = self.head
            self.head.prev = new_item

        # Set the new item as the first element and increase the length counter
        self.head = new_item
        self.length += 1

    def search(self, key: str) -> int:
        """Returns the index of the key or -1 if the key is not in the list."""

        # Start the search from the head of the list at index 0
        curr = self.head
        iter_idx = 0

        # While the current item is not None (i.e. the end of the list)
        while curr is not None:

            # If we found the first occurence, return its index
            if curr.key == key: return iter_idx

            # Otherwise, step to the next item
            curr = curr.next
            iter_idx += 1
        return -1

    def get(self, index: int) -> str:
        """Returns the key at the specified index in the list."""

        # Python supports negative indices
        if index < 0: index = self.length + index

        # If the queried index is not in the list, raise an IndexError
        if index >= self.length or index < 0: raise IndexError("Invalid index")

        # Start the search from the head of the list at index 0
        curr = self.head
        iter_idx = 0

        # While the current item's index is not the queried index, step to the
        # next item
        while iter_idx != index:
            curr = curr.next
            iter_idx += 1
        return curr.key

    def delete(self, key: str) -> None:
        """Deletes the first occurence of the key from the list.

        Returns True if the delete is successful, or False if the key is not in
        the list.
        """

        # Find the item that contains the first occurence of the key
        curr = self.head
        while curr is not None and curr.key != key:
            curr = curr.next

        # If the key is not in the list, return False
        if curr is None:
            return False

        # Otherwise, delete the item from the list by setting the previous and
        # next items' corresponding pointers to each other
        else:
            next_item = curr.next
            prev_item = curr.prev
            if next_item is not None: next_item.prev = prev_item
            if prev_item is not None: prev_item.next = next_item

            # If the first item is to be deleted, set the head pointer to its
            # next neighbor
            if curr == self.head: self.head = curr.next

            # Decrease the length counter and return True to indicate a
            # succesful delete
            self.length -= 1
            return True

    def __str__(self) -> str:
        """Returns the string representation of the list."""
        if self.head is None:
            return "[]"
        else:
            s = f"'{self.head.key}'"
            curr = self.head.next
            while curr is not None:
                s += f", '{curr.key}'"
                curr = curr.next
            return f"[{s}]"

    def __len__(self) -> int:
        """Returns the length of the list."""
        return self.length

    def insert_index(self, key: str, index: int) -> None:
        """Inserts the key at the specified index."""
        # TODO
        pass

    def delete_index(self, index: int) -> None:
        """Deletes the key at the specified index."""
        # TODO
        pass


# Example usage
linked_list = LinkedList()
linked_list.insert("s0")            # insert "s0" at the beginning of the list
linked_list.insert("s1")            # insert "s1" at the beginning of the list
linked_list.insert("s2")            # insert "s2" at the beginning of the list
print(linked_list)                  # expected output: ['s2', 's1', 's0']
linked_list.delete("s1")            # delete the first occurence of "s1"
print(linked_list)                  # expected output: ['s2', 's0']
linked_list.delete("s3")            # no effect, "s3" is not in the list
print(linked_list)                  # expected output: ['s2', 's0']
print(linked_list.get(1))           # expected output: s0
# print(linked_list.get(2))           # invalid index, the length of the list is 2

# Testing your work
linked_list.insert_index("s3", 1)   # insert "s3" at index 1
print(linked_list)                  # expected output: ['s2', 's3', 's0']
linked_list.insert_index("s4", 3)   # insert "s4" at index 4 (end of the list)
print(linked_list)                  # expected output: ['s2', 's3', 's0', 's4']
linked_list.delete_index(2)         # delete the item at index 2
print(linked_list)                  # expected output: ['s2', 's3', 's4']
linked_list.delete_index(0)         # delete the first item
print(linked_list)                  # expected output: ['s3', 's4']
```

---

### Exercise 4

Implement a stack that stores strings using the `LinkedList` implementation from the previous exercise as the underlying container. Make sure all methods run in $O(1)$ time. Use the outline below!

Alternatively, you can use the built-in `list` or `collections.deque` as the underlying container, as it was discussed in the lecture.

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
