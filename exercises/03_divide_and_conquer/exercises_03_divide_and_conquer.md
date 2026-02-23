# The Divide and Conquer Paradigm

### Exercise 1

Design and implement a **recursive** algorithm that takes a non-negative integer $n$ and returns the value of $n!$, i.e., the factorial of $n$.

---

### Exercise 2

Design and implement a **recursive** algorithm that reverses a string.

---

### Exercise 3

Design and implement a **recursive** algorithm that takes a positive integer $n$ and returns the $n$-th Fibonacci number.

---

### Exercise 4

Implement the binary search algorithm (see Exercise 2 from last week) using recursion.

---

### Exercise 5

Our goal is to get to the top of the $n$-th step in a very long flight of stairs. We start on the ground and we can only move either one or two steps at a time and we can not go backwards. Design and implement a **recursive** algorithm that finds the number of distinct movement sequences we can take to get to get on top of the $n$-th step.

**Constraints:**
- $n > 0$

Example: if $n=3$, the answer is 3. We can either move 1 step 3 times, move 2 steps followed by a 1-step move or move 1 step followed by a 2-step move.

---

### Exercise 6

On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the bottom-right corner.

**Constraints**
- $n, m > 0$

Example: if $n=m=2$, the answer is 2. We can either start by moving down, followed by a right move, or start with a right move, followed by a move down.

---

### Exercise 7

*Note: the description of the following exercise is not based on real events and any similarity to real life is merely coincidental.*

A pirate named Andras got very drunk once and Captain Mark decided to throw him overboard. Luckily for Andras, the crew instead decided to leave him on the $(x, y)$ position of an island that happens to be a perfect rectangle of $n \times m$ positions. Captain Mark shows mercy and offers Andras a deal: if, after $k$ moves, Andras is still on the island, he will take him back on board. However, Andras is still very drunk so he cannot control his movement, and the island is surrounded by sharks who will eat him the moment he steps off the island.

The movement of Andras is very restricted, he can only move one position up, down, left, or right at a time, and he cannot move diagonally. He is moving perfectly randomly, meaning the chance of the four possible moves is equal. Design and implement a recursive algorithm that calculates the probability of survival for our drunken pirate after $k$ steps. Assume the positions on the island start with $(1, 1)$ and end with $(n, m)$.

**Constraints:**
- $n, m > 0$
- $1 \leq x\leq n,\; 1 \leq y \leq m$
- $k \geq 0$

Use the following outline:

Example: if $n=m=2$, $x=y=1$ and $k=1$, the answer is 0.5. That is because with Andras will step to positions $(0, 1)$, $(1, 0)$, $(1, 2)$ and $(2, 1)$ with a 25% chance each, so in 50% of the cases he will step off the island.

---

### Exercise 8

Implement the merge sort algorithm using recursion.

---

### Exercise 9

Using the $O$-notation, analyze the time complexity of the algorithms of the following previous exercises:
- Exercise 1: `factorial`
- Exercise 2: `reverse`
- Exercise 3: `fibonacci`
- Exercise 4: `index`
- Exercise 5: `stairs`
- Exercise 6: `board`
- Exercise 7: `survival`
- Exercise 8: `merge_sort`
