# Invert Binary Tree

## 1. Problem
Given the root of a binary tree, invert the tree (mirror image) and return its root.

## 2. Approach
Recursive Swapping (DFS):
- Base case: If `root is None`, return `None`.
- Swap child pointers: `root.left, root.right = root.right, root.left`.
- Recursively invert the new `root.left` and `root.right` subtrees.
- Return `root`.

### Step-by-Step Written Tracing
**Input Tree:** `4 -> Left: 2, Right: 7`

| Step | Current Node | Before Swap | After Swap |
|---|---|---|---|
| 1 | Root(4) | Left=2, Right=7 | Left=7, Right=2 |
| 2 | Recurse Node(7) | Left=None, Right=None | Left=None, Right=None |
| 3 | Recurse Node(2) | Left=None, Right=None | Left=None, Right=None |

**Output Tree:** `4 -> Left: 7, Right: 2`

### Challenges & Failed Approaches
- **Overwriting Subtree Pointers:** Swapping children sequentially without simultaneous tuple assignment (`root.left = root.right` followed by `root.right = root.left`) overwrites `root.left` before saving it. Simultaneous swap `root.left, root.right = root.right, root.left` fixes this.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Each node is visited once.
- **Space Complexity:** $O(H)$ — Auxiliary stack memory proportional to tree height $H$.

## 4. Reflection / Improvement
- **BFS Queue Approach:** Swap children level-by-level using a queue. Achieves $O(N)$ time and $O(W)$ space.
