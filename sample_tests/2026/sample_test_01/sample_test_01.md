# Sample Test 1

**Before you begin**

During the test, you do not have access to the internet. After unzipping `algds_test_01.zip`, you will find two folders: `algds_materials/` and `algds_test_01/`.

The contents of the `algds_materials/` folder are:
- `practice_materials/`: contains all practice exercises and their solutions
- `lecture_materials/`: contains all lecture slides
- `book.pdf`: the fourth edition of the Introduction to Algorithms book

The contents of the `algds_test_01/` folder are:
- `src/`: contains prepared source files for all tasks with outlines and tests
- `test_01.md`: the test itself

You are given four tasks, each worth exactly 8 points. You can earn up to 24 points in this test, and, as per the requirements, you have to earn at least 8.

Create a folder in your home directory (`/home/hxxxxxx`) named `solutions`. Only work in your home directory! There, your work will be automatically saved during the time of the test and is recoverable during and after the test by the instructor. **All files outside your home directory are not secure during the test and will be lost when you shut down your PC.** You don't have to submit your solutions anywhere, leave them in the `/home/hxxxxxx/solutions` folder when you are done. **Make sure to fill in your name, neptun code and h-id at the beginning of each source file.**

Each task contains a set of test cases as examples, but be aware that just because your algorithm passes all the example tests, it might not be correct. You are encouraged to write further test cases (specifically to test edge cases), but this is not required and will not be scored.

Feel free to use built-in data structures (e.g. `set`, `list`, `dict`) and algorithms (e.g. `sort`, `index`) unless specified otherwise. You should assume that the input parameters conform to the type hints and the constraints in the task descriptions.

You have 110 minutes to complete your work. At the end of this time, the computers will shut down, and any unsaved work or work outside your home directory will be lost.

Good luck!

---

### Task 1 - Number of Ones

Design and implement an algorithm that calculates the number of ones in a sorted binary list (i.e. an list that only contains ones and zeros). Note that the input can be sorted in either ascending or descending order. Make sure your algorithm runs in at most $O(\log n)$ time, where $n$ is the length of the list.

**Constraints:**
- $n \geq 0$
- Each element of the input is either 0 or 1
- The input list is sorted

**Examples:**

If the input list is either `[0, 0, 1, 1, 1, 1, 1]` or `[1, 1, 1, 1, 1, 0, 0]`, your algorithm should return 5, as both lists contain 5 ones. The first list is sorted in ascending, the second in descending order.

---

### Task 2 - Coin Change Possibilities

You are given an amount of money $F$ and a set of denominations $P = \{ p_1, ..., p_n\}$, with an infinite number of coins of each denomination. Design and implement an algorithm that calculates the number of different coin combinations *irrespective of the order of coins* that add up to $F$. Two combinations are different if they are not permutations of each other. If the change cannot be made, your algorithm should return 0. Make sure your algorithm's time complexity is polynomial in $|P|$ and $F$.

**Constraints:**
- $F \geq 0$
- $p_i > 0$ for all $i = 1, ..., n$
- $n > 0$

**Examples:**

For $F=10$ and $P = \{1, 5\}$, the desired output is 3. The three ways of changing 10 money are:
- 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1 + 5
- 5 + 5

For $F=10$ and $P = \{1, 5, 7\}$, the desired output is 4. The four ways of changing 10 money are 1 + 1 + 1 + 7 and the three ways in the first example.


---

### Task 3 - Making up for lost time

Instead of doing housework, you wasted your precious time playing video games, to the point where you have only one day to do your chores. Unfortunately, every one of your tasks can only be completed in a specific time of day, but as an experienced procrastinator, you know exactly how long each task takes to complete. Of course, some tasks overlap. You can only work on one task at a time, and you can't pause a task to return to it later. Your job is to complete as many tasks as possible.

Your input is a list of two-element tuples `(start, end)`, where both `start` and `end` are strings in the form of `"hh:mm"` representing valid timestamps (e.g. `"09:15"`), and a number $n$, which is the length of the list. Design and implement an algorithm that determines the maximum number of tasks you can complete. Make sure your algorithm runs in at most $O(n \log n)$ time.

**Constraints:**
- $n \geq 0$
- When treated as timestamps, for each element of the input list, `start` < `end`
- The lowest possible `start` value is `"00:00"`, the highest possible `end` value is `"23:59"`
- All `start` and `end` values are correct timestamps, i.e., hours range between 00 and 23 and minutes range between 00 and 59

**Examples:**

If the tasks are `("09:15", "09:45")` and `("09:45", "13:00")`, there is no overlap between them, your algorithm should return 2.

If the tasks are `("09:15", "09:45")` and `("09:30", "13:00")`, then the optimum is 1, as the two tasks overlap.

If the tasks are `("09:30", "13:00")`, `("09:15", "09:45")`, and `("10:00", "18:00")`, then the optimum is 2, as the first task overlaps with the two others, but the second and third tasks don't overlap, so they can be done.

---

### Task 4 - The Biggest Square

You are given a rectangular binary matrix of size $n \times m$, meaning a matrix of $n$ rows, $m$ columns, and every element of the matrix is either 0 or 1. Design and implement an algorithm that determines the size of the largest square-shaped submatrix that only contains ones. Your algorithm should return the side length of this square, e.g., if the largest square-shaped submatrix of ones is of size $3 \times 3$, your algorithm should return 3. Make sure your algorithm runs in at most $O(nm)$ time.

**Constraints:**
- $n, m>0$
- The input matrix only contains ones and zeros

**Examples:**

$$
\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{pmatrix}
$$

In this matrix, the largest square submatrix of ones is of size $1\times 1$, so your algorithm should return 1.

$$
\begin{pmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 0
\end{pmatrix}
$$

In this matrix, the largest square submatrix of ones is of size $2\times 2$, so your algorithm should return 2.
