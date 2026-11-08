# Path Sum

## 1. Problem
Given the root of a binary tree and an integer `targetSum`, return `True` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

## 2. Approach
We use **Top-Down DFS with Subtraction**:
- At each node, subtract `root.val` from `targetSum`.
- Check if the current node is a leaf node (`not root.left and not root.right`). If it is a leaf, check if the remaining `targetSum == 0`.
- If not a leaf, recursively test left OR right branches.

### Step-by-Step Written Tracing
**Input:** Tree `5 -> Left: 4 -> Left: 11`, `targetSum = 20`

| Node | Current `targetSum` Before Node | Subtracted Node Val | Remaining `targetSum` | Leaf Check | Result |
|---|---|---|---|---|---|
| Node(5) | 20 | 5 | 15 | False | Recurse Left |
| Node(4) | 15 | 4 | 11 | False | Recurse Left |
| Node(11) | 11 | 11 | 0 | True (Leaf!) | `0 == 0` $\rightarrow$ **True** |

### Challenges & Failed Approaches
- **Non-Leaf Matching:** Initially returning `targetSum == 0` at an intermediate node (with one child) caused false positives for incomplete root-to-leaf paths. The check must strictly happen at leaf nodes.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Evaluates nodes along candidate leaf paths.
- **Space Complexity:** $O(H)$ — Recursion call stack space.

## 4. Reflection / Improvement
- **Optimal Complexity:** $O(N)$ time and $O(H)$ space are optimal for un-ordered binary tree path searches.
