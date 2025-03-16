# Elementary Data Structures - Solutions

### Exercise 1

What is an abstract data structure? Briefly describe the following abstract data structures:
- List
- Set
- Stack
- Queue
- Priority Queue

### Solution

An abstract data structure is practically an interface that specifies the necessary functionalities of every implementation of that interface. An abstract data structure can have multiple different implementations and the complexity of each functionality can be different across implementations.

A brief description of each of the mentioned abstract data structures:
- List: data is stored in a linear order, each element has an index, a key can be stored more than once
- Set: the order of data storage is not specified, elements don't have to have an index, a key is stored at most once
- Stack: last-in, first-out (LIFO) list
- Queue: first-in, first-out (FIFO) list
- Priority Queue: the order of data storage is not specified, but elements are extracted in sorted order

---

### Exercise 2

What is the difference between a `List` implementation that uses a direct access array (e.g. `java.util.ArrayList` in Java or `std::vector` in C++) and a linked list implementation? When is one more effective than the other? Is one better than the other?

Which variant is used in Python?


### Solution

ArrayLists implement lists using an array (how surprising), making use of direct access to achieve fast (constant time) indexing. When the array is full, a new, larger array (that typically doubles the size of the previous one) is allocated and all items are copied from the full array to this new, larger array. Inserting at any index $i$ is slow (linear time), as items on indices $\geq i$ have to be shifted by one index.

LinkedLists wrap keys in linked list items that contain a pointer to the next element, and in most implementations a pointer to the previous element as well. Since these list items can be anywhere in the memory, indexing is slow (linear time), because we have to traverse the entire list in the worst case. Insertion at, and deletion from the beginning of the list (or after any list item object *that we already have access to*) is fast (constant time), as only a few pointers have to be set in both cases.

The *exact* `list` implementation in Python depends on the variant of Python we use, but the core concept is similar across all variants. In Jython (the Python variant written in Java), it's an ArrayList. In Cython (the Python variant written in C), it's a direct access array that contains pointers to the stored elements. Ultimately, both variants use the direct access array implementation.

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


### Solution

Both methods rely on finding the item at the specified index, which we can copy from the `get` method. In the implementation of `delete_index`, the part where we delete the item can be copied from the `delete` method.

When inserting the new item in the `insert_index` method, we have to pay attention to setting the `next` and `prev` pointers accordingly. Note that we allow the user to insert at the end of the list (i.e. the parameter `index` equals the length of the list). The easiest strategy to manage this is to find the item at `index - 1` and add the new element as its next neighbor.

The complete solution is as follows:

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

        # Python supports negative indices
        if index < 0: index = self.length + index

        # If the index wouldn't be in the list even after the insertion, raise
        # an IndexError
        if index > self.length or index < 0: raise IndexError("Invalid index")

        # If the requested index is 0, we can use the `insert` method
        if index == 0:
            self.insert(key)

        # Otherwise, we have to find the location of the new item in the list
        # The strategy is to find the item at index - 1 and insert the new item
        # as its next item. This approach handles the case when the new item is
        # added at the last index (index == self.length).
        else:
            new_item = LinkedListItem(key)
            curr = self.head
            iter_idx = 0

            while curr is not None and iter_idx < index - 1:
                curr = curr.next
                iter_idx += 1

            prev_item = curr
            next_item = curr.next

            # Set the pointers of the new item and its two neighbors
            new_item.prev = prev_item
            new_item.next = next_item
            prev_item.next = new_item
            if next_item is not None: next_item.prev = new_item

            # Increase the length counter
            self.length += 1

    def delete_index(self, index: int) -> None:
        """Deletes the key at the specified index."""

        # Python supports negative indices
        if index < 0: index = self.length + index

        # If the queried index is not in the list, raise an IndexError
        if index >= self.length or index < 0: raise IndexError("Invalid index")

        # Find the item at the specified index
        curr = self.head
        iter_idx = 0

        while iter_idx != index:
            curr = curr.next
            iter_idx += 1

        # Delete the item from the list
        next_item = curr.next
        prev_item = curr.prev
        if next_item is not None: next_item.prev = prev_item
        if prev_item is not None: prev_item.next = next_item

        # If the first item is to be deleted, set the head pointer to its
        # next neighbor
        if curr == self.head: self.head = curr.next

        # Decrease the length counter
        self.length -= 1


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

### Solution

Once we implemented all methods in the `LinkedList` class of Exercise 3, the solution to this exercise is quite simple:

```py
class Stack:
    def __init__(self):
        self.container = LinkedList()

    def push(self, key: str) -> None:
        """Inserts the key at the top of the stack."""
        self.container.insert_index(key)

    def pop(self) -> str:
        """Deletes the key at the top of the stack."""
        top = self.top()
        self.container.delete_index(0)
        return top

    def top(self) -> str:
        """Returns the key at the top of the stack."""
        return self.container.get(0)
```

However, with this solution, we are relying on the implementation of the underlying container to raise errors when we are trying to get or delete the first item and the stack is empty. If we are more cautious - and we should be - we can check this ourselves and guarantee that an error is raised:

```py
class Stack:
    def __init__(self):
        self.size = 0
        self.container = LinkedList()

    def push(self, key: str) -> None:
        """Inserts the key at the top of the stack."""
        self.container.insert(key)
        self.size += 1

    def pop(self) -> str:
        """Deletes the key at the top of the stack."""

        # If the stack is empty, raise an error
        if self.size == 0: raise ValueError("Empty stack!")

        # Save the top item for the return statement before deleting it
        top = self.top()
        self.container.delete_index(0)
        self.size -= 1
        return top

    def top(self) -> str:
        """Returns the key at the top of the stack."""

        if self.size == 0: raise ValueError("Empty stack!")

        return self.container.get(0)

    def __len__(self) -> int:
        return self.size
```

Modifying this implementation to a Queue is simple, because the `LinkedList` class implements index-based modifying operations.

```py
class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.container = LinkedList()

    def enqueue(self, key: str) -> None:
        self.container.insert(key)
        self.size += 1

    def dequeue(self) -> str:
        if self.size == 0: raise ValueError("Empty queue!")

        first = self.first()
        self.container.delete_index(self.size - 1)
        self.size -= 1
        return first

    def first(self) -> str:
        if self.size == 0: raise ValueError("Empty queue!")
        return self.container.get(self.size - 1)

    def __len__(self) -> int:
        return self.size
```

However, note that `dequeue` will take $O(n)$ time instead of $O(1)$, because we have to find the last element in the list. With a circular linked list, or a list that allows double-ended modifications in $O(1)$ time, the time complexity of `dequeue` can be improved to $O(1)$.

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

### Solution

While the exercise specifies that we can only use stacks, it does not specify that we can only use *one* stack, so we will use *two stacks*. One will be used as a regular stack, storing all items in LIFO order. We will use this for the `enqueue` operation, as we want to preserve the order of the items. The problem is that we want to simulate the FIFO behavior, so the `dequeue` and `first` operations need to have access to the element that is at the bottom of the first stack. This is when the second stack comes into play: when calling either `dequeue` or `first`, we `pop` all elements from the first stack and `push` them onto the second stack. Afterwards, the first element in the FIFO order is at the top of the second stack, so from this point, implementation of `dequeue` and `first` is quite simple:

```py
class Queue:
    def __init__(self) -> None:
        self.lifo_order_stack = Stack()
        self.fifo_order_stack = Stack()
        self.size = 0

    def enqueue(self, key: str) -> None:
        """Inserts the key at the end of the queue."""
        while len(self.fifo_order_stack) > 0:
            self.lifo_order_stack.push(self.fifo_order_stack.pop())

        self.lifo_order_stack.push(key)
        self.size += 1

    def dequeue(self) -> str:
        """Deletes the key at the start of the queue."""
        if self.size == 0: raise ValueError("Empty queue!")

        while len(self.lifo_order_stack) > 0:
            self.fifo_order_stack.push(self.lifo_order_stack.pop())
        first = self.fifo_order_stack.pop()
        self.size -= 1
        return first

    def first(self) -> str:
        """Returns the key at the start of the queue."""
        if self.size == 0: raise ValueError("Empty queue!")

        while len(self.lifo_order_stack) > 0:
            self.fifo_order_stack.push(self.lifo_order_stack.pop())

        return self.fifo_order_stack.top()

    def __len__(self) -> int:
        return self.size
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

### Solution

Knowing that we don't have to account for stack overflow errors, the simple strategy is to grow one stack from the beginning from the array and the other from the end of the array. Note that the two stacks are growing in the opposite direction.

The complete solution is as follows:

```py
class DoubleStack:
    def __init__(self, n: int) -> None:
        self.container = [None] * n
        self.stack1_top_idx = 0
        self.stack2_top_idx = n - 1
        self.stack1_size = 0
        self.stack2_size = 0

    def push_stack1(self, key: str) -> None:
        """Inserts a key at the top of the first stack"""
        self.container[self.stack1_top_idx] = key
        self.stack1_top_idx += 1
        self.stack1_size += 1

    def push_stack2(self, key: str) -> None:
        """Inserts a key at the top of the second stack"""
        self.container[self.stack2_top_idx] = key
        self.stack2_top_idx -= 1
        self.stack2_size += 1

    def pop_stack1(self) -> str:
        """Deletes the key at the top of the first stack."""
        if self.stack1_size == 0: raise ValueError("Empty stack 1!")

        self.stack1_top_idx -= 1
        stack1_top = self.container[self.stack1_top_idx]
        self.container[self.stack1_top_idx] = None
        self.stack1_size -= 1
        return stack1_top

    def pop_stack2(self) -> str:
        """Deletes the key at the top of the second stack."""
        if self.stack2_size == 0: raise ValueError("Empty stack 1!")

        self.stack2_top_idx += 1
        stack2_top = self.container[self.stack2_top_idx]
        self.container[self.stack2_top_idx] = None
        self.stack2_size -= 1
        return stack2_top

    def top_stack1(self) -> str:
        """Returns the key at the top of the first stack."""
        return self.container[self.stack1_top_idx - 1]

    def top_stack2(self) -> str:
        """Returns the key at the top of the second stack."""
        return self.container[self.stack2_top_idx + 1]
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

### Solution

The exercise's description gives away a key to solving this problem: using extra memory. The strategy is to use another stack that will store the minimum element for each level in the stack. Since the time complexity of stack operations is $O(1)$, doing two inserts and deletes instead of one will remain $O(1)$. At any given time, the minimum element will be at the top of the second stack.

The complete implementation is as follows:

```py
class Stack:
    def __init__(self):
        self.size = 0
        self.container = LinkedList()
        self.min_container = LinkedList()

    def push(self, key: int) -> None:
        """Inserts the key at the top of the stack."""
        self.container.insert(key)
        if self.size > 0:
            self.min_container.insert(min(key, self.min_container.get(0)))
        else:
            self.min_container.insert(key)
        self.size += 1

    def pop(self) -> int:
        """Deletes the key at the top of the stack."""
        # If the stack is empty, raise an error
        if self.size == 0: raise ValueError("Empty stack!")

        # Save the top item for the return statement before deleting it
        top = self.top()
        self.container.delete_index(0)
        self.min_container.delete_index(0)
        return top

    def top(self) -> int:
        """Returns the key at the top of the stack."""

        if self.size == 0: raise ValueError("Empty stack!")

        return self.container.get(0)

    def min(self) -> int:
        """Returns the minimum key in the stack."""

        if self.size == 0: raise ValueError("Empty stack!")

        return self.min_container.get(0)

    def __str__(self) -> str:
        return str(self.container)
```
