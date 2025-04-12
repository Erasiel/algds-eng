# Hash Tables

### Exercise 1

Describe the differnce between arrays and hash tables. What is the purpose of the hash function? What requirements are imposed on hash functions?

What is a *collision*? Why do collisions happen? How can we prevent or resolve collisions?

---

### Exercise 2

How is hashing implemented in Python? What is the connection between Python's `set`, `dict`, and hashing? Are all objects hashable?

Extend the implementation of `MyType` in the code snippet below, so that neither of the assertions fail.

```py
class MyType:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    # TODO

v1 = MyType(1, 2)
v2 = MyType(1, 2)
assert v1 == v2

s = set()
s.add(v1)
s.add(v2)
assert len(s) == 1
```

---

### Exercise 3

Insert the following integers (in the given order) into a hash table with 10 slots ($m = 10$) that uses the division method. The hash table resolves conflicts with **chaining**.

1, 5, 21, 42, 61, 64, 52.

---

### Exercise 4

You are given the implementation of a **set** data structure that stores integers. The implementation uses a hash table with the division method, and resolves collisions with chaining (here, we use the built-in `list` data structure instead of a linked list). Analyze the time complexity of the `insert`, `delete` and `contains` operations in the worst case, and the average case as well.

Based on your analysis, modify the implementation to ensure that the time complexity of all operations is $O(1)$ *in the average case*.

```py
class HashSetChaining:
    def __init__(self, num_slots: int = 10) -> None:
        self.table = [[] for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0

    def insert(self, key: int) -> None:
        # Insert the key in the slot given by the key's hash value
        slot = self._hash_value(key)

        # In a set a key is stored at most once
        if key not in self.table[slot]:
            self.table[slot].append(key)
            self.num_keys += 1

    def delete(self, key: int) -> None:
        # Delete the key from the slot given by the key's hash value
        slot = self._hash_value(key)

        # Only delete the key if it's in the slot's list
        if key in self.table[slot]:
            self.table[slot].remove(key)
            self.num_keys -= 1

    def contains(self, key: int) -> bool:
        # Find the key in the slot given by the key's hash value
        slot = self._hash_value(key)
        return key in self.table[slot]

    def _hash_value(self, key: int) -> int:
        # Note: for integer keys, hash(key) == key, but for other types the
        # hash(...) call would be required. We write hash(key) instead of key
        # to emphasize the use of hashing.
        return hash(key) % self.num_slots
```

---

### Exercise 5

Insert the following integers (in the given order) into a hash table with 10 slots ($m = 10$) that uses the division method. The hash table resolves conflicts with **open addressing** and linear probing.

1, 5, 21, 42, 61, 64, 52.

How would the hash table look if we used quadratic probing with $c_1 = 1$ and $c_2 = 1$ instead of linear probing?

---

### Exercise 6

This week, your intern gave you an implementation of a **set** data structure that stores integers. The implementation uses a hash table with the division method, and resolves collisions with open addressing and linear probing.

Yet again, their implementation is incorrect. Demonstrate why through a sequence of operations that end up giving incorrect results and fix the mistake. Hint: recall how to delete a key from a hash table with open addressing.

As further practice, extend the implementation with the functionality discussed in Exercise 4.

```py
class HashSetOpenAddressing:
    def __init__(self, num_slots: int = 10) -> None:
        self.table = [None for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0

    def insert(self, key: int) -> None:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # In a set a key is stored at most once
            if self.table[slot] == key:
                return

            # If the slot is empty, insert the key
            elif self.table[slot] is None:
                self.table[slot] = key
                self.num_keys += 1
                return

        # If there are no more empty slots, raise an error
        raise ValueError("The hash table is full!")

    def delete(self, key: int) -> None:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # If the current slot is empty, the key is not in the hash table
            if self.table[slot] is None:
                return

            # If the slot contains the key, set the slot's content to None
            if self.table[slot] == key:
                self.table[slot] = None
                self.num_keys -= 1
                return

    def contains(self, key: int) -> bool:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # If the current slot is empty, the key is not in the hash table
            if self.table[slot] is None:
                return False
            elif self.table[slot] == key:
                return True

        # This line is only executed if the table is full and the key is not in
        # the table
        return False

    def _probe(self, key: int, i: int) -> int:
        return self._probe_linear(key, i)

    def _probe_linear(self, key, i) -> int:
        return (hash(key) + i) % self.num_slots
```

---

### Exercise 7

Given a list of strings, determine which strings are *not* unique in the list. Design and implement an algorithm for this task that runs in $O(n)$ time in the average case, where $n$ is the number of strings in the input. Feel free to use built-in data structures (e.g. `list`, `set`, `dict`).

**Constraints:**
- $n \geq 0$

Use the following outline:

```py
from typing import List, Set


def not_unique(strings: List[str], n: int) -> Set[str]:
    # TODO
```

Example: for $n$ = 6 and the list `["apple", "peach", "apple", "strawberry", "peach", "apple"]` the output of your algorithm should be `{"apple", "peach"}`.
