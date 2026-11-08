# Sum of Left Leaves

## 1. Problem
Given the root of a binary tree, return the sum of all **left leaves** (a leaf node that is the left child of its parent).

## 2. Approach
Recursive Tree Traversal with Parent Validation:
- Base case: If `root is None`, return 0.
- Check if `root.left` is a leaf node (`root.left` exists and has no left or right children).
- If it is a left leaf, add `root.left.val` to `total_sum`.
- Recursively add results from `sumOfLeftLeaves(root.left)` and `sumOfLeftLeaves(root.right)`.

### Step-by-Step Written Tracing
**Input Tree:** `3 -> Left: 9, Right: 20 (Left: 15, Right: 7)`

| Sub-tree Node | `root.left` Condition | Action Taken | Current Sum |
|---|---|---|---|
| Node(3) | `Node(9)` is a leaf! | Add `9` | 9 |
| Node(20) | `Node(15)` is a leaf! | Add `15` | $9 + 15 = 24$ |
| Node(7) | No left child | Return 0 | 24 |

**Output:** `24`

### Challenges & Failed Approaches
- **Confusing Left Nodes with Left Leaves:** Summing all left children (even internal non-leaf nodes) produced incorrect sums. Nodes must satisfy both conditions: being a **left child** AND a **leaf**.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Visits every node once.
- **Space Complexity:** $O(H)$ — Call stack memory bounded by tree height $H$.

## 4. Reflection / Improvement
- **Boolean Flag Parameter:** Passing `is_left: bool` flag to sub-calls simplifies checking leaf status inside child frames.
