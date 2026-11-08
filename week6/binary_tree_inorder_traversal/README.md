# Binary Tree Inorder Traversal

## 1. Problem
Given the head node of a binary tree, return the in-order traversal of its nodes' values (Left Subtree $\rightarrow$ Root Node $\rightarrow$ Right Subtree).

## 2. Approach
We use **Recursive Depth-First Search (DFS)**:
- Base case: If the current node is `None`, return immediately.
- Recursively visit the left child (`traverse(node.left)`).
- Append the current node's value (`node.val`) to the result list.
- Recursively visit the right child (`traverse(node.right)`).

### Step-by-Step Written Tracing
**Input Tree:** `1 -> Right: 2 -> Left: 3`

| Step | Current Node | Call Stack Action | Traversal Result |
|---|---|---|---|
| **1** | Node(1) | Recurse left (`None`) | `[]` |
| **2** | Node(1) | Visit root value `1` | `[1]` |
| **3** | Node(2) | Recurse left (`Node(3)`) | `[1]` |
| **4** | Node(3) | Recurse left (`None`) $\rightarrow$ Visit `3` | `[1, 3]` |
| **5** | Node(3) | Recurse right (`None`) $\rightarrow$ Return | `[1, 3]` |
| **6** | Node(2) | Visit root value `2` | `[1, 3, 2]` |
| **7** | Node(2) | Recurse right (`None`) $\rightarrow$ Complete | `[1, 3, 2]` |

### Challenges & Failed Approaches
- **Forgetting Base Case:** In initial testing, omitting `if not node: return` led to `AttributeError` when trying to access `.left` on `None`.
- **Iterative Stack Complexity:** Attempting an iterative approach without a call stack required maintaining an explicit list stack, which proved harder to maintain than the clean recursive structure.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$
  - *Explanation:* $N$ is the total number of nodes in the binary tree. Every node is visited exactly once.
- **Space Complexity:** $O(N)$ worst-case, $O(\log N)$ average
  - *Explanation:* Call stack space depends on tree height. A skewed tree consumes $O(N)$ stack memory, whereas a balanced tree consumes $O(\log N)$.

## 4. Reflection / Improvement
- **Morris Traversal ($O(1)$ Extra Space):** Modifies tree links temporarily to traverse without a stack or recursion.
- *Comparison:* Morris Traversal reduces space complexity to $O(1)$ at the cost of temporary tree structure mutation.
