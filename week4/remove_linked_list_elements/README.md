# Remove Linked List Elements

## 1. Problem
Given the head of a linked list and an integer `val`, remove all nodes from the linked list that have `Node.val == val`, and return the new head.

## 2. Approach
We utilize a **Dummy Header Node** pattern:
- Create `dummy = ListNode(-1)` pointing to `head`.
- Pointer `current` starts at `dummy`.
- Traverse while `current.next` is not `None`:
  - If `current.next.val == val`, update `current.next = current.next.next`.
  - Otherwise, move `current = current.next`.
- Return `dummy.next`.

### Step-by-Step Written Tracing
**Input:** `head = [1 -> 2 -> 6 -> 3 -> 6]`, `val = 6`

| Step | `current.val` | `current.next.val` | Action Taken | List State |
|---|---|---|---|---|
| **Init** | `-1` (dummy) | `1` | Start at `dummy` | `-1 -> 1 -> 2 -> 6 -> 3 -> 6` |
| **Iter 1** | `-1` | `1` | `1 != 6` $\rightarrow$ advance `current` | `-1 -> 1 -> 2 -> 6 -> 3 -> 6` |
| **Iter 2** | `1` | `2` | `2 != 6` $\rightarrow$ advance `current` | `-1 -> 1 -> 2 -> 6 -> 3 -> 6` |
| **Iter 3** | `2` | `6` | `6 == 6` $\rightarrow$ remove node `6` | `-1 -> 1 -> 2 -> 3 -> 6` |
| **Iter 4** | `2` | `3` | `3 != 6` $\rightarrow$ advance `current` | `-1 -> 1 -> 2 -> 3 -> 6` |
| **Iter 5** | `3` | `6` | `6 == 6` $\rightarrow$ remove node `6` | `-1 -> 1 -> 2 -> 3` |
| **Exit** | `3` | `None` | `current.next` is `None` $\rightarrow$ exit | `1 -> 2 -> 3` |

### Challenges & Failed Approaches
- **Direct Head Modification Error:** Direct head updating without a dummy node failed when target elements occurred at the start (e.g., `6 -> 6 -> 1`). The dummy node simplifies edge cases by ensuring there is always a node prior to `head`.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$
  - *Explanation:* $N$ is the number of nodes. Every node is visited once.
- **Space Complexity:** $O(1)$ auxiliary space
  - *Explanation:* Uses only two pointers (`dummy`, `current`).

## 4. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(N)$ time and $O(1)$ space is optimal.
- **Alternative (Recursive Solution):** Recursively filter `head.next`. Requires $O(N)$ auxiliary stack space.
