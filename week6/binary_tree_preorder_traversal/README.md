# Binary Tree Preorder Traversal

## 1. Problem
Given the root of a binary tree, return the pre-order traversal of its nodes' values (Root Node $\rightarrow$ Left Subtree $\rightarrow$ Right Subtree).

## 2. Approach
Recursive Depth-First Search (DFS):
- Base case: If `node is None`, return.
- Append `node.val` to `result` first.
- Recurse on `node.left`.
- Recurse on `node.right`.

### Step-by-Step Written Tracing
**Input Tree:** `1 -> Right: 2 -> Left: 3`

| Step | Action | Visited Node | Result List |
|---|---|---|---|
| 1 | Visit Root | Node(1) | `[1]` |
| 2 | Recurse Left | `None` | `[1]` |
| 3 | Recurse Right | Node(2) | `[1]` |
| 4 | Visit Root | Node(2) | `[1, 2]` |
| 5 | Recurse Left | Node(3) | `[1, 2, 3]` |

### Challenges & Failed Approaches
- **Order Mix-Up:** Placing `result.append()` after `traverse(node.left)` inadvertently converts the traversal to in-order. Pre-order requires visiting the root value before child calls.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Each node visited once.
- **Space Complexity:** $O(H)$ — Call stack depth bounded by tree height $H$.

## 4. Reflection / Improvement
- **Iterative Approach:** Uses an explicit stack by pushing `right` child first, then `left` child to process root-left-right iteratively in $O(N)$ time and $O(H)$ space.
