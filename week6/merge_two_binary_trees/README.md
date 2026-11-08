# Merge Two Binary Trees

## 1. Problem
Given two binary trees `root1` and `root2`, merge them into a single binary tree. If two nodes overlap, sum their values. Otherwise, the non-null node is used as the node of the new tree.

## 2. Approach
We use **Pre-Order Recursive Merging**:
- Base cases:
  - If `root1 is None`, return `root2`.
  - If `root2 is None`, return `root1`.
- For overlapping nodes, create `merged = TreeNode(root1.val + root2.val)`.
- Recursively compute `merged.left = mergeTrees(root1.left, root2.left)`.
- Recursively compute `merged.right = mergeTrees(root1.right, root2.right)`.
- Return `merged`.

### Step-by-Step Written Tracing
**Input:** Tree 1 (`1 -> Left: 3`), Tree 2 (`2 -> Left: 1, Right: 3`)

| Level / Branch | Node 1 | Node 2 | Merged Value |
|---|---|---|---|
| Root | Node(1) | Node(2) | `1 + 2 = 3` |
| Left Branch | Node(3) | Node(1) | `3 + 1 = 4` |
| Right Branch | `None` | Node(3) | Reuse Node(3) |

**Output Tree:** `3 -> Left: 4, Right: 3`

### Challenges & Failed Approaches
- **In-Place Mutation Bugs:** Attempting to mutate `root1` directly without returning subtrees created reference assignment errors when one subtree was missing. Returning the non-null node directly handles non-overlapping branches cleanly.

## 3. Complexity Analysis
- **Time Complexity:** $O(\min(N, M))$
  - *Explanation:* Recursion stops as soon as one tree branch is `None`. Thus, operations are bounded by the smaller tree size.
- **Space Complexity:** $O(\min(H_1, H_2))$ stack memory.

## 4. Reflection / Improvement
- **In-Place Mutation:** Mutating `root1` in-place avoids allocating new node objects, achieving $O(1)$ extra space beyond recursion stack.
