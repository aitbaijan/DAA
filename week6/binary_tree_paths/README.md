# Binary Tree Paths

## 1. Problem
Given the root of a binary tree, return all root-to-leaf paths in any order represented as string path formats (e.g., `"1->2->5"`).

## 2. Approach
Backtracking / String Accumulation (DFS):
- Maintain an accumulated path string `current_path`.
- Append `->node.val` to `current_path`.
- If current node is a leaf node (`not node.left and not node.right`), store `current_path` into `paths`.
- Recurse on `left` and `right` subtrees.

### Step-by-Step Written Tracing
**Input Tree:** `1 -> Left: 2 (Right: 5), Right: 3`

| Node | Accumulated Path String | Leaf Check | Action |
|---|---|---|---|
| Node(1) | `"1"` | False | Recurse Left (Node 2) |
| Node(2) | `"1->2"` | False | Recurse Right (Node 5) |
| Node(5) | `"1->2->5"` | True | Add `"1->2->5"` to `paths` |
| Node(3) | `"1->3"` | True | Add `"1->3"` to `paths` |

**Output:** `["1->2->5", "1->3"]`

### Challenges & Failed Approaches
- **Shared Mutable List State:** Passing a single mutable list `path.append()` without backtracking popping caused elements from the left branch to leak into the right branch. Immutable string concatenation (`current_path + "->"`) naturally isolates branch states.

## 3. Complexity Analysis
- **Time Complexity:** $O(N^2)$ worst-case
  - *Explanation:* String concatenation takes $O(L)$ time for path length $L$. For $N$ nodes, total time is bounded by $O(N^2)$.
- **Space Complexity:** $O(N^2)$ to store string paths output.

## 4. Reflection / Improvement
- **List Backtracking with Join:** Pass a list of integers, `pop()` on return, and run `"->".join()` only at leaf nodes to reduce string copy overhead.
