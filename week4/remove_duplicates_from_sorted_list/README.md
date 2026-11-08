# Remove Duplicates from Sorted List

## 1. Problem
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## 2. Approach
We utilize a single-pointer iterative traversal:
- Maintain a pointer `current` initialized to `head`.
- Traverse the linked list while both `current` and `current.next` are not `None`.
- Compare `current.val` with `current.next.val`:
  - If equal, update `current.next = current.next.next` to bypass the duplicate node.
  - If different, advance `current = current.next`.
- Return `head`.

### Step-by-Step Written Tracing
**Input:** `head = [1 -> 1 -> 2 -> 3 -> 3]`

| Step | `current.val` | `current.next.val` | Action Taken | Modified List State |
|---|---|---|---|---|
| **Init** | `1` | `1` | Start at `head` | `1 -> 1 -> 2 -> 3 -> 3` |
| **Iter 1** | `1` | `1` | Values equal $\rightarrow$ bypass duplicate | `1 -> 2 -> 3 -> 3` |
| **Iter 2** | `1` | `2` | Values different $\rightarrow$ advance `current` | `1 -> 2 -> 3 -> 3` |
| **Iter 3** | `2` | `3` | Values different $\rightarrow$ advance `current` | `1 -> 2 -> 3 -> 3` |
| **Iter 4** | `3` | `3` | Values equal $\rightarrow$ bypass duplicate | `1 -> 2 -> 3` |
| **Exit** | `3` | `None` | `current.next` is `None` $\rightarrow$ terminate | `1 -> 2 -> 3` |

### Challenges & Failed Approaches
- **Unconditional Pointer Advancement:** Initially, I attempted to advance `current = current.next` on every iteration. For sequence inputs with multiple consecutive duplicates (e.g., `1 -> 1 -> 1`), advancing immediately skipped checking the remaining duplicates. Moving `current` only inside an `else` branch fixed this issue.
- **Hash Set Overkill:** Storing values in a `set` was considered, but since the list is sorted, auxiliary storage is unnecessary.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$
  - *Explanation:* $N$ is the number of nodes in the list. Each node is traversed at most once.
- **Space Complexity:** $O(1)$ auxiliary space
  - *Explanation:* Modifications are done in-place without auxiliary data structures.

## 4. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(N)$ time and $O(1)$ space are optimal.
- **Alternative (Recursive Approach):** Recursively clean `head.next`. Takes $O(N)$ space due to recursion call stack.
