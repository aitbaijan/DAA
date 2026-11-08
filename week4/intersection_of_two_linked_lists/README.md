# Intersection of Two Linked Lists

## 1. Problem
Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If they do not intersect, return `None`.

## 2. Approach
We use **Two Pointers with Path Alignment**:
- Initialize `pA` at `headA` and `pB` at `headB`.
- Advance both pointers step by step.
- When `pA` reaches `None`, redirect it to `headB`. When `pB` reaches `None`, redirect it to `headA`.
- Both pointers traverse an equal total distance ($Length(A) + Length(B)$) and meet at the intersection node or at `None`.

### Step-by-Step Written Tracing
**Input:** List A: `4 -> 1 -> 8 -> 4 -> 5`, List B: `5 -> 6 -> 1 -> 8 -> 4 -> 5` (Intersect at node `8`).

| Step | `pA` Node | `pB` Node | Status / Action |
|---|---|---|---|
| **Start** | `4` (headA) | `5` (headB) | `pA != pB` |
| **1** | `1` | `6` | `pA != pB` |
| **2** | `8` | `1` | `pA != pB` |
| **3** | `4` | `8` | `pA != pB` |
| **4** | `5` | `4` | `pA != pB` |
| **5** | `None` (end A) | `5` | Redirect `pA` to `headB` |
| **6** | `5` (headB) | `None` (end B) | Redirect `pB` to `headA` |
| **7** | `6` | `4` (headA) | `pA != pB` |
| **8** | `1` | `1` | `pA != pB` (different instances) |
| **9** | **`8`** | **`8`** | **`pA == pB` (Intersection found)** |

### Challenges & Failed Approaches
- **Value Comparison Mistake:** Checking node values (`pA.val == pB.val`) failed because separate nodes can share the same value before intersection. Pointers must be compared by reference (`pA == pB`).
- **Nested Loop Brute Force ($O(N \times M)$):** Comparing every node of List A with List B timed out on long lists.
- **Hash Set Extra Memory ($O(N)$ Space):** Storing List A nodes in a hash set worked but violated the $O(1)$ memory requirement.

## 3. Complexity Analysis
- **Time Complexity:** $O(N + M)$
  - *Explanation:* Each pointer travels at most $N + M$ steps before colliding or reaching `None`.
- **Space Complexity:** $O(1)$ auxiliary space
  - *Explanation:* Only two pointer variables (`pA`, `pB`) are maintained.

## 4. Reflection / Improvement
- **Alternative (Length Difference Method):** Measure lengths $L_A$ and $L_B$, advance the longer list's pointer by $|L_A - L_B|$, then traverse together. Achieves the same $O(N + M)$ time and $O(1)$ space.
