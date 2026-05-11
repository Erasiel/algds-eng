# Hash Tables

### Exercise 1

Insert the following keys (in the given order) into an initially empty hash table with $m=5$ slots. Use $h(k) = k \mod m$ and resolve collisions with chaining.

The integers are: 27, 2, 31, 63, 16

---

### Exercise 2

You are given the implementation of a **set** data structure that stores integers. The implementation uses a hash table with the division method, and resolves collisions with chaining (here, we use the built-in `list` data structure instead of a linked list).

Analyze the time complexity of the `insert`, `delete` and `contains` operations in the worst case, and the average case as well. Based on your analysis, modify the implementation to ensure that the time complexity of all operations is $O(1)$ *in the average case*.

---

### Exercise 3

Insert the following integers (in the given order) into a hash table with 10 slots ($m = 10$) that uses the division method. The hash table resolves conflicts with **open addressing** and linear probing, i.e., $h(k, i) = (h'(k) + i) \mod m$.

The integers are: 1, 5, 21, 42, 61, 64, 52.

---

### Exercise 4

From the same hash table as Exercise 3, after all insertions are complete, delete the key 42, and then search for the key 61, and insert 31.

---

### Exercise 5

This week, your intern gave you an implementation of a **set** data structure that stores integers. The implementation uses a hash table with the division method, and resolves collisions with open addressing and linear probing.

Yet again, their implementation is incorrect. Demonstrate why through a sequence of operations that end up giving incorrect results and fix the mistake. Hint: recall how to delete a key from a hash table with open addressing.

As further practice, extend the implementation so that every operation runs in $O(1)$ time in the average case, similar to Exercise 2.

---

### Exercise 6

Given a list of strings, design and implement an algorithm that determines which strings are *not unique* in the input list. Make sure your algorithm runs in $O(n)$ time in the average case, where $n$ is the number of strings in the input. Feel free to use built-in data structures (e.g. `list`, `set`, `dict`).

**Constraints:**
- $n \geq 0$

---

### Exercise 7

Given two strings, design and implement an algorithm that checks if they are anagrams. Two strings are anagrams if one can be obtained by rearranging the letters of the other. Make sure your algorithm runs in $O(n + m)$ time in the average case, where $n$ and $m$ are the lengths of the two strings.

**Constraints:**
- $n, m \geq 0$
- $n$ is not guaranteed to be equal to $m$

---

### Exercise 8

Given a list of whole numbers $(c_1, c_2, ..., c_n)$, design and implement an algorithm that finds an index pair $(i, j)$ such that $c_i + c_j = 0$ and $i < j$. If multiple such index pairs exist, return only one. If no such index pair exists, return `(-1, -1)`. Make sure your algorithm runs in $O(n)$ time in the average case, where $n$ is the length of the input list.
