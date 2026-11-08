# Sort an Array

## 1. Problem
Given an array of integers `nums`, sort the array in ascending order and return it without using built-in sorting functions in $O(N \log N)$ time complexity.

## 2. Approach
We implement **Merge Sort** (Divide and Conquer):
1. **Divide:** Recursively split the array `nums` into two halves at index `mid = len(nums) // 2`.
2. **Conquer:** Continue splitting until sub-arrays contain 1 element (base case).
3. **Combine:** Merge two sorted sub-arrays (`left` and `right`) back together in linear time using two pointers (`i` and `j`).

### Step-by-Step Written Tracing
**Input:** `nums = [5, 2, 3, 1]`

| Phase | Sub-array State | Description |
|---|---|---|
| **Split 1** | `[5, 2]` and `[3, 1]` | Divide array at middle index 2 |
| **Split 2** | `[5]`, `[2]` and `[3]`, `[1]` | Divide into single-element base cases |
| **Merge Level 1** | `merge([5], [2])` $\rightarrow$ `[2, 5]` <br> `merge([3], [1])` $\rightarrow$ `[1, 3]` | Compare elements and combine into sorted pairs |
| **Merge Level 2** | `merge([2, 5], [1, 3])` $\rightarrow$ `[1, 2, 3, 5]` | Two-pointer comparison: compare 2 vs 1 (take 1), 2 vs 3 (take 2), 5 vs 3 (take 3), append remainder 5 |

### Challenges & Failed Approaches
- **O(N²) Algorithms (Bubble / Insertion Sort):** My initial naive approach used Bubble Sort. While simple, it resulted in Time Limit Exceeded (TLE) on LeetCode because $N = 50,000$ requires $\approx 2.5 \times 10^9$ operations.
- **Quick Sort with Bad Pivot Choice:** I tested Quick Sort picking the first element as the pivot. On pre-sorted or near-sorted arrays, the recursion depth degraded to $O(N)$, causing stack overflow and $O(N^2)$ time. Switching to Merge Sort guaranteed $O(N \log N)$ worst-case performance.

## 3. Complexity Analysis
- **Time Complexity:** $O(N \log N)$
  - *Explanation:* The array is recursively split $\log_2 N$ times. At each level of the recursion tree, merging sub-arrays takes $O(N)$ operations. Total time $= O(N \log N)$ for best, average, and worst cases.
- **Space Complexity:** $O(N)$ auxiliary space
  - *Explanation:* Temporary sub-arrays are created during array slicing and merging operations.

## 4. Reflection / Improvement
- **Is there a more efficient approach?**
  - **Heap Sort:** Achieves $O(N \log N)$ time and $O(1)$ auxiliary space by sorting in-place using a max-heap.
  - **Timsort (Standard Python `sort()`):** Hybrid of Merge Sort and Insertion Sort that achieves $O(N)$ time on nearly sorted data.
