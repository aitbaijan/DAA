# Sort List

## 1. Problem
Given the head of a linked list, return the list after sorting it in ascending order in $O(N \log N)$ time complexity and constant or logarithmic memory.

## 2. Approach
We use **Top-Down Merge Sort on Linked Lists**:
1. **Find Mid & Split:** Use fast (`fast = head.next`) and slow (`slow = head`) pointers to locate the midpoint. Break the link (`slow.next = None`) to divide the list into two sublists (`head` and `mid`).
2. **Recursive Sort:** Recursively call `sortList` on both halves.
3. **Merge:** Combine the two sorted halves into a single list using a dummy header node.

### Step-by-Step Written Tracing
**Input:** `head = [4 -> 2 -> 1 -> 3]`

| Phase | Action | List Structure State |
|---|---|---|
| **Split 1** | Fast/slow pointers find midpoint at node `2` | Left: `4 -> 2`, Right: `1 -> 3` |
| **Split 2** | Sublists split into single nodes | `[4]`, `[2]` and `[1]`, `[3]` |
| **Merge 1** | `merge([4], [2])` and `merge([1], [3])` | Left: `2 -> 4`, Right: `1 -> 3` |
| **Merge 2** | `merge([2 -> 4], [1 -> 3])` | Compare heads: pick `1`, then `2`, then `3`, then `4` $\rightarrow$ `1 -> 2 -> 3 -> 4` |

### Challenges & Failed Approaches
- **Infinite Recursion / Stack Overflow:** In initial testing, initializing both pointers to `head` (`slow = head`, `fast = head`) caused two-node lists (e.g., `[2 -> 1]`) to split into `[2 -> 1]` and `[]`, creating an infinite recursion loop. Setting `fast = head.next` fixed the midpoint split.
- **Array Conversion Copying ($O(N)$ Space):** Converting node values into a Python array, calling `array.sort()`, and rebuilding nodes works in $O(N \log N)$ time, but consumes $O(N)$ auxiliary memory. Sorting nodes directly via pointer manipulation is cleaner and optimal.

## 3. Complexity Analysis
- **Time Complexity:** $O(N \log N)$
  - *Explanation:* Finding the middle takes $O(N/2)$ steps and merging takes $O(N)$ steps per recursion level. Splitting occurs $\log_2 N$ times $\rightarrow O(N \log N)$.
- **Space Complexity:** $O(\log N)$ auxiliary space
  - *Explanation:* Recursion stack depth is bounded by the tree height $\log_2 N$. No new nodes are created.

## 4. Reflection / Improvement
- **Is there a more efficient approach?**
  - **Bottom-Up Iterative Merge Sort:** Avoids recursion entirely by merging sublists of sizes 1, 2, 4, 8... iteratively.
  - *Complexity of Bottom-Up:* Time $O(N \log N)$, Space strict $O(1)$.
