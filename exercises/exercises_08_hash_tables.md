# Hash Tables

### Exercise 1

Describe the differnce between arrays and hash tables. What is the purpose of the hash function? What requirements are imposed on hash functions?

What is a *collision*? Why do collisions happen? How can we prevent or resolve collisions?

---

### Exercise 2

How is hashing implemented in Python? What is the connection between Python's `set` and hashing? Are all types hashable?

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

Implement a set for storing strings with a hash table with a fixed number of slots. Resolve conflicts with chaining. Use the following outline:

```py
class HashSetChaining:
    def __init__(self, num_slots: int) -> None:
        # TODO
        pass

    def insert(self, key: str) -> None:
        # TODO
        pass

    def delete(self, key: str) -> None:
        # TODO
        pass

    def contains(self, key: str) -> bool:
        # TODO
        pass
```

---

### Exercise 4

Analyze the time complexity of conflict resolution with chaining. What are the wors case and average case time complexities of `insert`, `delete`, and `contains`?

How can we make the *average* case time complexity of these methods $O(1)$?

---

### Exercise 5

Extend the `HashSet` implementation from Exercise 3 so that `insert`, `delete` and `contain` run in $O(1)$ time in the average case. If you want to start from scratch, feel free to use the following outline:

```py
class HashSetChaining:
    def __init__(self, num_slots: int, max_load_factor: float) -> None:
        # TODO
        pass

    def insert(self, key: str) -> None:
        # TODO
        pass

    def delete(self, key: str) -> None:
        # TODO
        pass

    def contains(self, key: str) -> bool:
        # TODO
        pass
```

---

### Exercise 6

What is the difference between conflict resolution with chaining and with open addressing? What is probing, and what are probe sequences? What are the three main types of probing?

How is `delete` implemented with open addressing?

---

### Exercise 7

Implement a set for storing strings with a hash table with a fixed number of initial slots. Resolve conflicts with open addressing, with either linear or quadratic probing. Use the following outline:

```py
class HashSetOpenAddressing:
    def __init__(self, num_slots: int, max_load_factor: float) -> None:
        # TODO
        pass

    def insert(self, key: str) -> None:
        # TODO
        pass

    def delete(self, key: str) -> None:
        # TODO
        pass

    def contains(self, key: str) -> bool:
        # TODO
        pass

    def _probe(self, key: str, i: int) -> int:
        # TODO
        pass
```

---

### Exercise 8

Given a list of strings, determine which strings are *not* unique in the list. Design and implement an algorithm for this task that runs in $O(n)$ time in the average case, where $n$ is the number of strings in the input. Feel free to use built-in data structures. Use the following outline:

```py
from typing import List, Set


def not_unique(strings: List[str], n: int) -> Set[str]:
    # TODO
```

Example: for $n$ = 6 and the list `["apple", "peach", "apple", "strawberry", "peach", "apple"]` the output of your algorithm should be `{"apple", "peach"}`.
