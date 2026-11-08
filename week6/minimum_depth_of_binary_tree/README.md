# Minimum Depth of Binary Tree

## 1. Problem
Find the minimum depth of a binary tree — the number of nodes along the shortest path from the root node down to the nearest **leaf node** (a node with no children).

## 2. Approach
Recursive DFS with explicit single-child conditional handling:
- If `root` is `None`, return 0.
- If a node has only one child, we must traverse down that existing child branch (since a missing child does NOT constitute a leaf node).
- If both children exist, return `1 + min(minDepth(left), minDepth(right))`.

### Step-by-Step Written Tracing
**Input Tree:** `2 -> Right: 3 -> Right: 4` (Skewed Tree)

| Node Visited | Left Child | Right Child | Decision Branch | Depth |
|---|---|---|---|---|
| Node(4) | `None` | `None` | Leaf Node Base Case | 1 |
| Node(3) | `None` | Node(4) | Left is `None` $\rightarrow$ `1 + minDepth(Right)` | `1 + 1 = 2` |
| Node(2) | `None` | Node(3) | Left is `None` $\rightarrow$ `1 + minDepth(Right)` | `1 + 2 = 3` |

### Challenges & Failed Approaches
- **Naive `1 + min(left, right)` Bug:** Simply using `1 + min(left, right)` on node `2` evaluated `min(0, 2) = 0`, returning depth 1. This was incorrect because node `2` has a right child and is not a leaf. Adding explicit checks for `not root.left` and `not root.right` solved the issue.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Visits nodes until leaf paths are evaluated.
- **Space Complexity:** $O(H)$ — Call stack memory bounded by tree height $H$.

## 4. Reflection / Improvement
- **BFS (Queue-based) is Faster:** BFS encounters the nearest leaf node first and can terminate early without visiting the entire tree.
