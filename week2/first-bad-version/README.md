# First Bad Version

## 1. Problem

The task is to find the first bad version among versions from 1 to n.

Once a version is bad, all versions after it are also bad. We need to find the first bad version.

## 2. Approach

I used binary search.

I keep two variables: `left` and `right`. They represent the current range where the first bad version can be.

I check the middle version.

* If the middle version is bad, I move `right` to the middle.
* If the middle version is good, I move `left` to the middle + 1.

I repeat this until `left` and `right` become equal. That position is the first bad version.

## 3. Time Complexity

**O(log n)**

Each time I check a version, I remove approximately half of the possible versions.

Therefore, the number of checks grows logarithmically with the number of versions.

## 4. Space Complexity

**O(1)**

I only use a few variables such as `left`, `right`, and `middle`.

I do not create any additional data structures.

## 5. Reflection / Improvement

At first, I tried a simple linear search with O(n) time complexity.

It worked for smaller test cases, but LeetCode gave a Time Limit Exceeded error on a large test case.

I improved the solution by using binary search. This reduced the time complexity from O(n) to O(log n).

The improved solution also makes much fewer calls to the `isBadVersion()` API.
