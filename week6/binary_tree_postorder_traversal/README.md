# Binary Tree Postorder Traversal

## 1. Problem
Given the root of a binary tree, return the post-order traversal of its nodes' values (Left Subtree $\rightarrow$ Right Subtree $\rightarrow$ Root Node).

## 2. Approach
Recursive Depth-First Search (DFS):
- Base case: If `node is None`, return.
- Recurse on `node.left`.
- Recurse on `node.right`.
- Append `node.val` to `result` last.

### Step-by-Step Written Tracing
**Input Tree:** `1 -> Right: 2 -> Left: 3`

| Step | Action | Node | Result List |
|---|---|---|---|
| 1 | Traverse Left of 1 | `None` | `[]` |
| 2 | Traverse Right of 1 | Node(2) | `[]` |
| 3 | Traverse Left of 2 | Node(3) | `[]` |
| 4 | Append Leaf 3 | Node(3) | `[3]` |
| 5 | Append Node 2 | Node(2) | `[3, 2]` |
| 6 | Append Root 1 | Node(1) | `[3, 2, 1]` |

### Challenges & Failed Approaches
- **Stack-based Traversal Reversal:** An alternative approach generates modified pre-order (`Root -> Right -> Left`) and reverses the output. While working, direct recursive post-order is cleaner and intuitive.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Every node is visited once.
- **Space Complexity:** $O(H)$ — Call stack memory bounded by tree height $H$.

## 4. Reflection / Improvement
- **Use Case:** Post-order traversal is essential for deleting tree nodes or evaluating mathematical expression trees from bottom to top.
