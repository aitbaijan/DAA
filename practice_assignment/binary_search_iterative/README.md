# Iterative Binary Search

## 1. Description
Binary Search is a search algorithm for sorted arrays. It repeatedly divides the search interval in half.

## 2. 3 Execution Examples & Progress Visualization

Array: `arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` ($N=10$)

### Example 1: Target = 23

| Iteration | `low` | `high` | `mid` | `arr[mid]` | Action | Active Subarray |
|---|---|---|---|---|---|---|
| **1** | 0 | 9 | 4 | 16 | $16 < 23 \rightarrow$ `low = 5` | `[23, 38, 56, 72, 91]` |
| **2** | 5 | 9 | 7 | 56 | $56 > 23 \rightarrow$ `high = 6` | `[23, 38]` |
| **3** | 5 | 6 | 5 | 23 | **$23 == 23 \rightarrow$ Found at index 5** | `[23]` |

---

### Example 2: Target = 5

| Iteration | `low` | `high` | `mid` | `arr[mid]` | Action | Active Subarray |
|---|---|---|---|---|---|---|
| **1** | 0 | 9 | 4 | 16 | $16 > 5 \rightarrow$ `high = 3` | `[2, 5, 8, 12]` |
| **2** | 0 | 3 | 1 | 5 | **$5 == 5 \rightarrow$ Found at index 1** | `[5]` |

---

### Example 3: Target = 100 (Not in Array)

| Iteration | `low` | `high` | `mid` | `arr[mid]` | Action | Active Subarray |
|---|---|---|---|---|---|---|
| **1** | 0 | 9 | 4 | 16 | $16 < 100 \rightarrow$ `low = 5` | `[23, 38, 56, 72, 91]` |
| **2** | 5 | 9 | 7 | 56 | $56 < 100 \rightarrow$ `low = 8` | `[72, 91]` |
| **3** | 8 | 9 | 8 | 72 | $72 < 100 \rightarrow$ `low = 9` | `[91]` |
| **4** | 9 | 9 | 9 | 91 | $91 < 100 \rightarrow$ `low = 10` | `[]` |
| **Exit** | 10 | 9 | - | - | `low > high` $\rightarrow$ Return -1 | Empty |

## 3. Complexity Analysis
- **Time Complexity:** $O(\log N)$ — The array is split in half each step.
- **Space Complexity:** $O(1)$ — Only pointer variables are maintained.
