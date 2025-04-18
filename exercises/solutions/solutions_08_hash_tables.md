# Hash Tables - Solutions

### Exercise 1

Describe the differnce between arrays and hash tables. What is the purpose of the hash function? What requirements are imposed on hash functions?

What is a *collision*? Why do collisions happen? How can we prevent or resolve collisions?

### Solution

In arrays, either the implementation or the user specifies the index of each key, whereas in hash tables, the index of the key is given by its hash value. We call refer to the indices of hash tables as *slots*. The purpose of the hash function (typically denoted as $h$) is computing the hash value of each key (denoted as $h(k)$ where $k$ is the key). We can think of a hash function as a way of converting a key to an integer.

A good hash function is:
1. deterministic,
2. quickly computable (ideally in constant time), and
3. satisfies the simple uniform hashing condition.

The simple uniform hashing condition states that each key is equally likely to hash into any of the slots. It is very easy to design a hash function that conforms to the first two conditions but does not satisfy the simple uniform hashing condition, e.g. by always returning a constant number, but it will shortly become obvious why this is undesirable.

Hash functions can return arbitrarily large values (as long as these values can be represented by integers). Since hash values are used to locate keys in hash tables, we have to ensure that any key's hash value points to a slot in the table. We will denote the number of slots with $m$, which means the slots are indexed from $0$ to $m-1$. The simplest way to ensure all hash values point to a slot in the table is the *division method*, where a key's corresponding slot is given as $h(k) \mod m$.

*Collisions* happen when two keys have the same hash value, i.e. $h(k_1) = h(k_2)$. Given that there are typically orders of magnitude more possible keys than slots in our hash table, collisions are unavoidable, so the most crucial part of designing hash tables is handling collisions. In this practice, we review two distinct methods for handling collisions: chaining and open addressing.

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

### Solution

In almost every programming language, in order to make objects of a custom type (e.g. a class) hashable, we need to override the equality operator (`==`) and design a hash function for the custom type. In Python, these are the built-in `__eq__` and `__hash__` functions, respectively. An example implementation of these for the `MyType` class is as follows:

```py
from typing import Any


class MyType:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, MyType):
            return self.a == other.a and self.b == other.b
        return False

    def __hash__(self) -> int:
        return hash((self.a, self.b))
```

Here, the `__eq__` function simply checks if the other value is of the same type and the value of its fields is the same as the current object's fields. The `__hash__` function simply converts the object's fields into a two-element tuple (a built-in type with a good hash function) and returns this tuple's hash value.

In Python, the built-in `set` and `dict` types use hash tables. `set`s store an element at most once (just like mathematical sets), and `dict`s (also known as associative maps) store a set of keys with an associated value to each key. Somewhat interestingly, in Python, a `set` is implemented as a `dict` that stores keys without associated values.

Going back to hashing, a final thing to consider is the mutability of the type. An immutable type is one that prevents you from changing any field values of an object after it's instantiated. For example, the built-in tuple type is immutable: you cannot change, add, or remove items once the tuple is created. Immutability is important when it comes to hashing, as in a perfect implementation, only immutable objects are hashable (a workaround for this is to never modify the object's fields once it's in a container that uses hashing). While there are multiple ways to make `MyType` immutable, the simplest is to use the `dataclass` decorator with `frozen=True`:

```py
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, init=False)
class MyType:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        object.__setattr__(self, "a", a)
        object.__setattr__(self, "b", b)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, MyType):
            return self.a == other.a and self.b == other.b
        return False

    def __hash__(self) -> int:
        return hash((self.a, self.b))
```

---

### Exercise 3

Insert the following integers (in the given order) into a hash table with 10 slots ($m = 10$) that uses the division method. The hash table resolves conflicts with **chaining**.

1, 5, 21, 42, 61, 64, 52.

### Solution

With chaining, each slot contains a list (or some other data structure) of all keys that are mapped to that slot. After all insertions, the hash table would look like this:

```py
[
    [],             # slot 0
    [1, 21, 61],    # slot 1
    [42, 52],       # slot 2
    [],             # slot 3
    [64],           # slot 4
    [5],            # slot 5
    [],             # slot 6
    [],             # slot 7
    [],             # slot 8
    []              # slot 9
]
```

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

### Solution

The time complexity of all operations depends on the length of the list to which the key is mapped. In the worst case, all keys are hashed into the same list, so if we insert a key to this list, delete a key from this list, or look for a key in this list, the time complexity will be $O(n)$, where $n$ is the number of stored keys.

In the average case, the keys are distributed evenly across the slots, so we can assume that the length of the list in which we perform the insert / delete / contains operation will be *average of all lists' lengths*. This can be computed by taking the number of stored keys and dividing it by the number of slots (i.e. the number of lists): $n / m$. This ratio is also known as the *load factor* of the hash table, and the time complexity of all three operations in the average case is the load factor, i.e. $O(n / m)$.

The reason we love hash tables is their speed, as we can ensure that the time complexity of all operations remains constant in the average case. To achieve this, we must make sure the load factor does not exceed a certain limit. This limit is typically $\leq 1$, in order to ensure the constant average-case complexity and quick insert / delete / contains operations.

But what happens if the load factor exceeds this limit? This can only happen during insertions, as inserting a key increases $n$, thereby increasing the load factor. The solution is to increase $m$ (the number of slots) as well, if the load factor exceeds the specified threshold. There are multiple strategies to this, the simplest is to double the number of slots. However, simply doubling the number of slots is not enough...

Consider the following example: $m = 5$, the maximum load factor is 0.75, and the hash table is as follows:

```py
[
    [0, 5]  # slot 0
    [],     # slot 1
    [],     # slot 2
    [18],   # slot 3
    []      # slot 4
]
```

At this point, the load factor is 0.6. Let us now insert the key 7:

```py
[
    [0, 5]  # slot 0
    [],     # slot 1
    [7],    # slot 2
    [18],   # slot 3
    []      # slot 4
]
```

At this point, the load factor is 0.8, which exceeds the 0.75 threshold. Let us employ the strategy that doubles the number of slots. By *only doubling the number of slots*, we sould get the following hash table with $m = 10$ and a load factor of 0.4:

```py
[
    [0, 5]  # slot 0
    [],     # slot 1
    [7],    # slot 2
    [18],   # slot 3
    [],     # slot 4
    [],     # slot 5
    [],     # slot 6
    [],     # slot 7
    [],     # slot 8
    [],     # slot 9
]
```

However, let us now run the `contains(7)` operation:
1. $h(k) \mod m = h(7) \mod 10 = 7$, so we are looking for the key 7 in slot 7.
2. The list of slot 7 is empty, so we return `False`.

This is obviously incorrect, since we started the example by inserting the key 7 and we didn't delete it.

So what are we missing? As we increased the number of slots, the value of $m$ also changed. We use this value in computing the hash values (see the division method), so it is possible that the hash value of the stored keys changed because we modified $m$.

The solution is quite simple: when we increase the number of slots, we also re-hash and re-insert every key into the new hash table, so that they are in their correct positions. Following this analysis and explanation, the extended implementation is as follows:

```py
class HashSetChaining:
    def __init__(self, num_slots: int = 10, max_load_factor: float = 1) -> None:
        self.table = [[] for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0
        self.max_load_factor = max_load_factor

    def insert(self, key: int) -> None:
        # Insert the key in the slot given by the key's hash value
        slot = self._hash_value(key)

        # In a set a key is stored at most once
        if key not in self.table[slot]:
            self.table[slot].append(key)
            self.num_keys += 1

            # If the load factor threshold is exceeded, resize the hash table
            if self._load_factor() > self.max_load_factor:
                self._resize()

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

    def __str__(self) -> str:
        return str(self.table)

    def _load_factor(self) -> float:
        return self.num_keys / self.num_slots

    def _resize(self) -> None:
        # Double the number of slots and create a new hash table of this size
        self.num_slots *= 2
        new_table = [[] for _ in range(self.num_slots)]

        # Re-hash and re-insert all keys into the new table
        for bucket in self.table:
            for key in bucket:
                slot = self._hash_value(key)
                new_table[slot].append(key)

        # Set self.table to point to the newly created table
        self.table = new_table
```

---

### Exercise 5

Insert the following integers (in the given order) into a hash table with 10 slots ($m = 10$) that uses the division method. The hash table resolves conflicts with **open addressing** and linear probing.

1, 5, 21, 42, 61, 64, 52.

How would the hash table look if we used quadratic probing with $c_1 = 1$ and $c_2 = 1$ instead of linear probing?

### Solution

With open addressing, each slot is used to store keys directly. When a collision happens, the strategy is to traverse the slots in a specific order. This order is determined by the so-called *probe sequence* of the key, denoted as $h(k, 0), h(k, 1), ..., h(k, m-1)$, which is a permutation of the indices of the hash table.

In the `insert` method, we look for the first empty slot in the probe sequence. In the `delete` and `contains` methods, we probe each slot in the probe sequence. If we find a slot that contains NIL (`None` in Python), we can conclude that the key is not in the data structure, otherwise we continue probing until we find the key. `contains` returns `True` if we find the key in the probe sequence, `delete` deletes the key if it is found (we will talk about the latter in detail in Exercise 6).

There are three common implementations for the probe function $h(k, i)$:
1. Linear probing: $h(k, i) = (h(k) + i) \mod m$
2. Quadratic probing: $h(k, i) = (h(k) + c_1 i + c_2 i^2) \mod m$, for some $c_1$ and $c_2 > 0$
3. Double hashing: $h(k, i) = (h_1(k) + i h_2(k)) \mod m$ for some hash functions $h_1, h_2$

Note that in some textbooks, $h(k)$ is denoted as $h'(k)$, representing an auxiliary hash function. Typical implementations treat the "starting point" (i.e. when $i = 0$) to correspond to the regular hash value of the key.

With linear probing, after all insertions the hash table would look like this:

```py
[
    None,   # slot 0
    1,      # slot 1
    21,     # slot 2
    42,     # slot 3
    61,     # slot 4
    5,      # slot 5
    64,     # slot 6
    52,     # slot 7
    None,   # slot 8
    None    # slot 9
]
```

With quadratic probing, $c_1 = 1$ and $c_2 = 1$, the hash table would look like this:

```py
[
    None,   # slot 0
    1,      # slot 1
    42,     # slot 2
    21,     # slot 3
    64,     # slot 4
    5,      # slot 5
    None,   # slot 6
    61,     # slot 7
    52,     # slot 8
    None    # slot 9
]
```

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

### Solution

As hinted, the problem stems from the `delete` operation. To demonstrate the issue, consider the following sequence of operations:
```py
hs = HashSetOpenAddressing()
# Exercise 5
hs.insert(1)
hs.insert(5)
hs.insert(21)
hs.insert(42)
hs.insert(61)
hs.insert(64)
hs.insert(52)
print(hs.contains(52)) # expected: True, output: True
hs.delete(64)
print(hs.contains(52)) # expected: True, output: False (!)
```

To understand the problem, recall how searching for a key in an open-addressing hash table works, specifically when the key is not in the hash table. If we find a slot in the probe sequence with the value NIL (`None` in Python), we conclude that the key is not in the data structure. The given `delete` implementation replaces the deleted key with the value `None`, thereby "breaking" some probe sequences.

The solution is a bit tricky: we use a special flag, called the "deleted" element, to mark slots where we deleted keys from. The two other operations have to handle this deleted flag specifically:
- `insert` treats it as an empty slot
- `contains` and `delete` treat it as an occupied slot (in order to not break the probe sequence)

The fixed implementation is as follows:

```py
_deleted = object()


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
            elif self.table[slot] is None or self.table[slot] == _deleted:
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
                self.table[slot] = _deleted
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

Note that we don't have to handle the deleted key separately in `contains` and `delete`, the conditions handle all values that are not `None`, which includes the deleted flag.

We could further extend the implementation to follow the principles of Exercise 4 (monitoring the load factor and resizing accordingly), but this is quite trivial after Exercise 4, and as such, it is left as homework for the reader.

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

### Solution

This exercise is intended to showcase one of the most common use cases for dictionaries: counting occurences. A full solution is as follows:

```py
def not_unique(strings: List[str], n: int) -> Set[str]:
    # Count the occurences of all strings
    string_occurences = dict()
    for string in strings:
        if string in string_occurences:
            string_occurences[string] += 1
        else:
            string_occurences[string] = 1

    # Check which strings occured more than once
    not_unique_strings = set()
    for string, occurences in string_occurences.items():
        if occurences > 1:
            not_unique_strings.add(string)

    return not_unique_strings
```

Some notes regarding the solution:
- When used with a `dict`, the `in` keyword checks if the element is a key in the dictionary. We specifically check if a string has been inserted into the `dict`, because Python's `dict` does not assign a default value to inserted keys (unlike e.g. `std::map` in C++). This functionality is implemented in Python's `collections.defaultdict` container.
- The `items` function of a `dict` returns the list of `(key, value)` pairs stored in the dict. By default, iterating over the dict (e.g. `for string in string_occurences: ...`) iterates over the *keys* in the dictionary.
