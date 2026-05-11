# Sample Test 2

**Before you begin**

During the test, you do not have access to the internet. After unzipping `algds_test_02.zip`, you will find two folders: `algds_materials/` and `algds_test_02/`.

The contents of the `algds_materials/` folder are:
- `practice_materials/`: contains all practice exercises and their solutions
- `lecture_materials/`: contains all lecture slides
- `book.pdf`: the fourth edition of the Introduction to Algorithms book

The contents of the `algds_test_02/` folder are:
- `src/`: contains prepared source files for all tasks with outlines and tests
- `test_02.md`: the test itself

You are given four tasks, each worth exactly 8 points. You can earn up to 24 points in this test, and, as per the requirements, you have to earn at least 8.

Create a folder in your home directory (`/home/hxxxxxx`) named `solutions`. Only work in your home directory! There, your work will be automatically saved during the time of the test and is recoverable during and after the test by the instructor. **All files outside your home directory are not secure during the test and will be lost when you shut down your PC.** You don't have to submit your solutions anywhere, leave them in the `/home/hxxxxxx/solutions` folder when you are done. **Make sure to fill in your name, neptun code and h-id at the beginning of each source file.**

Each task contains a set of test cases as examples, but be aware that just because your algorithm passes all the example tests, it might not be correct. You are encouraged to write further test cases (specifically to test edge cases), but this is not required and will not be scored.

Feel free to use built-in data structures (e.g. `set`, `list`, `dict`) and algorithms (e.g. `sort`, `index`) unless specified otherwise. You should assume that the input parameters conform to the type hints and the constraints in the task descriptions.

You have 110 minutes to complete your work. At the end of this time, the computers will shut down, and any unsaved work or work outside your home directory will be lost.

Good luck!

---

### Task 1 - RPN evaluation

Design and implement an algorithm that evaluates an arithmetic expression that is in Reverse Polish Notation (RPN). The input is a list of $n$ strings and numbers, where every element of the list is one of the following:
- One of the four basic arithmetic operators: `"+"`, `"-"`, `"*"`, `"/"`
- A real number of type `float`

Make sure your algorithm runs in at most $O(n)$ time.

**Constraints:**
- The input is a valid RPN
- $n \geq 0$
- All elements of the input list are either a float or a string, and every string is a basic arithmetic operator
- Division with zero is never present in the input

**Examples:**

| Original (infix) formula      | Reverse Polish Notation | Input of the algorithm                                    | Solution |
|-------------------------------|-------------------------|-----------------------------------------------------------|----------|
| `5 * 4 + 3`                   | `5 4 * 3 +`             | `[5.0, 4.0, "*", 3.0, "+"]`                               | 23       |
| `5 + 4 * 3`                   | `5 4 3 * +`             | `[5.0, 4.0, 3.0, "*", "+"]`                               | 17       |
| `5 * 4 + 3 * 2`               | `5 4 * 3 2 * +`         | `[5.0, 4.0, "*", 3.0, 2.0, "*", "+"]`                     | 26       |
| `(5 + 3) / (4 - 2)`           | `5 3 + 4 2 - /`         | `[5.0, 3.0, "+", 4.0, 2.0, "-", "/"]`                     | 4        |
| `((1 + 2) * 3 + 6) / (8 - 5)` | `1 2 + 3 * 6 + 8 5 - /` | `[1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"]` | 5        |

---

### Task 2 - Nodes at Depth $k$

In a tree, the *depth* of a node $v$ is the length of the path from the root to $v$. The depth of the root is always zero, the depth of the root's children is one, etc. Design and implement an algorithm that determines the number of nodes at depth $k$ in a binary tree (given by its root node). Make sure your algorithm runs in at most $O(n)$ time, where $n$ is the number of nodes in the tree.

**Constraints:**
- $k \geq 0$

**Examples:**

Let us consider the following binary tree:
```
    A
   / \
  B   C
 /   / \
D   E   F
   /
  G
```
The following are true:
- At depth 0, there is 1 node (the root)
- At depth 1, there are 2 nodes (B and C)
- At depth 2, there are 3 nodes (D, E, and F)
- At depth 4, there is only 1 node (G)
- There are zero nodes at any depth larger than 4

---

### Task 3 - Repeating Row Filter

Design and implement an algorithm that filters the repeating rows in a two-dimensional binary list (i.e. a list that only contains ones and zeros). The $i^\text{th}$ row is *repeating* if there exists $j < i$ such that the $j^\text{th}$ row is the same as the $i^\text{th}$ row. Your algorithm should return a copy of the input matrix with the repeating rows removed. Make sure your algorithm runs in $O(nm)$ time in the average case, where $n$ and $m$ are the dimensions of the matrix.

**Constraints:**
- $n, m > 0$
- The input only contains ones and zeros

**Examples:**

Given the following input:
```py
[[0, 0, 1, 1],
 [1, 0, 1, 0],
 [1, 0, 1, 0],
 [1, 1, 1, 1],
 [0, 0, 1, 1]]
```
The output of the algorithm should be as follows:
```py
[[0, 0, 1, 1], # 1st row
 [1, 0, 1, 0], # 2nd row
 [1, 1, 1, 1]] # 4th row
```
The first, second and fourth rows are kept from the input. The third row is filtered out because it is the same as the second, and the fifth row is filtered out because it is the same as the first.

---

### Task 4 - Circular reference

You decided to re-implement the basic functionalities of the famous sheet management software Excel, including the evaluation of formulas in cells. Some formulas reference the content of other cells, which can lead to a problem: circular references. For example, if the formula in cell `A1` references the content of cell `B2`, and the formula in `B2` references the content of `A1`, neither formula can be evaluated because there is a circle in the references.

Given a list of $n$ references, where every reference is a two-element tuple in the form of `("<cell with a formula>", "<referenced cell>")`, e.g., `[("A1", "B2"), ("B2", "A1")]` for the above example, design and implement an algorithm that determines if there is at least one circular reference. Return `True` if the sheet contains at least one circular reference and `False` otherwise.

**Constraints:**
- $n \geq 0$
- Every reference is a two-element tuple of strings in the form `("<cell with a formula>", "<referenced cell>")`

**Examples:**
For the following reference list, the algorithm should return `False`.

```py
[("A1", "A2"), ("A2", "A3"), ("A3", "A4"), ("A4", "A5"), ("A5", "A6")]
```

For the following reference list, the algorithm should return `True`, as the references form a circle.

```py
[("A1", "A2"), ("A2", "A3"), ("A3", "A4"), ("A4", "A5"), ("A5", "A1")]
```
