# Elementary Data Structures

### Exercise 1

You are given an empty stack, queue, and max-priority queue, and insert the following seven keys in this order: 3, 6, 10, 8, 1, 7, 9. You then perform seven extraction operations. What is the order in which the elements are extracted?

---

### Exercise 2

Implement a stack in Python, using the built-in list as the underlying container.

---

### Exercise 3

Simulate a queue using only the stack implementation from Exercise 02. You can’t use any other data structures.

---

### Exercise 4

Simulate two stacks using a fix-sized list of length $n$. We know upfront that the number of keys contained in the data structure (i.e., in both stacks together) will never exceed $n$. Make sure the time complexity of all stack operations remain $O(1)$.

---

### Exercise 5

Modify a stack data structure so that it implements the `min` operation (that returns the minimum element in the data structure) in $O(1)$ time. Make sure that the time complexity of all other stack operations remain $O(1)$ and you don’t use more than $O(𝑛)$ extra space.

---

Exercise 6

Implement a doubly linked list. Specifically, implement the following operations:
- `insert(k)`: inserts a key at the beginning of the list
- `delete(k)`: deletes the first occurence of the key in the list
- `index(k)`: returns the index of the key in the list
- `get(i)`: returns the key on the given index in the list

Feel free to implement other, more Pythonic methods.
