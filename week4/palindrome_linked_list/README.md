# Palindrome Linked List

## 1. Problem
Given the head of a singly linked list, return `True` if it is a palindrome or `False` otherwise.

## 2. Approach
We implement an **In-Place Reversal of the Second Half**:
1. **Find Middle:** Use `slow` and `fast` pointers.
2. **Reverse Second Half:** Reverse the sublist starting from `slow` iteratively.
3. **Compare Halves:** Compare node values step-by-step from `head` and the reversed head (`second`).

### Step-by-Step Written Tracing
**Input:** `head = [1 -> 2 -> 2 -> 1]`

| Phase | State / Pointers | Description |
|---|---|---|
| **1. Find Middle** | `slow` at index 2 (`2`), `fast` at `None` | `slow` locates middle node |
| **2. Reverse Second** | Original: `2 -> 1` $\rightarrow$ Reversed: `1 -> 2` | In-place link reversal |
| **3. Compare** | `1 == 1` then `2 == 2` | All values match |
| **Exit** | `second` reaches `None` | Return `True` |

### Challenges & Failed Approaches
- **Array Conversion ($O(N)$ Space):** Storing values in a list `vals` and checking `vals == vals[::-1]` is easy but takes $O(N)$ extra space. In-place reversal achieves $O(1)$ space complexity.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$
  - *Explanation:* Finding middle ($N/2$), reversing half ($N/2$), comparing ($N/2$) $\rightarrow O(N)$.
- **Space Complexity:** $O(1)$ auxiliary space
  - *Explanation:* Nodes are reversed in-place without allocated extra memory.

## 4. Reflection / Improvement
- **Trade-off:** Array conversion is simpler to code ($O(N)$ space), while the two-pointer in-place reversal is optimal for memory ($O(1)$ space).
