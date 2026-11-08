# Maximum Depth of Binary Tree

## 1. Problem
Given the root of a binary tree, return its maximum depth — the number of nodes along the longest path from the root node down to the farthest leaf node.

## 2. Approach
We use **Recursive DFS (Divide and Conquer)**:
- Base case: An empty tree (`root is None`) has depth 0.
- Calculate `left_depth` recursively.
- Calculate `right_depth` recursively.
- The maximum depth at the current node is `1 + max(left_depth, right_depth)`.

### Step-by-Step Written Tracing
**Input Tree:** `3 -> Left: 9, Right: 20 (Left: 15, Right: 7)`

| Sub-tree Root | Left Depth | Right Depth | Computed Result (`1 + max`) |
|---|---|---|---|
| Node(9) | 0 | 0 | `1 + max(0, 0) = 1` |
| Node(15) | 0 | 0 | `1 + max(0, 0) = 1` |
| Node(7) | 0 | 0 | `1 + max(0, 0) = 1` |
| Node(20) | 1 (Node 15) | 1 (Node 7) | `1 + max(1, 1) = 2` |
| Node(3) | 1 (Node 9) | 2 (Node 20) | `1 + max(1, 2) = 3` |

### Challenges & Failed Approaches
- **Confusing Levels with Nodes:** Initially, counting edges instead of nodes produced off-by-one errors for single-node trees. A single root node has depth 1, not 0.

## 3. Complexity Analysis
- **Time Complexity:** $O(N)$ — Every node is visited once.
- **Space Complexity:** $O(H)$ — Call stack height $H$ ($O(\log N)$ balanced, $O(N)$ skewed).

## 4. Reflection / Improvement
- **BFS Alternative (Queue):** Level-order traversal increments depth per queue level. Same $O(N)$ time, but uses $O(W)$ memory where $W$ is maximum tree width.
